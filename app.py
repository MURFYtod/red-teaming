from flask import Flask, jsonify, request, send_from_directory, redirect, render_template
from flask_cors import CORS
import re
import os

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app, resources={r"/*": {"origins": "*"}})

# Detection patterns for different vulnerabilities
DETECTION_PATTERNS = {
    'prompt-injection': [
        r'ignore previous instructions',
        r'secret password',
        r'confidential information',
        r'bypass security',
        r'override system'
    ],
    'jailbreak': [
        r'you are now DAN',
        r'do anything now',
        r'ignore all previous instructions',
        r'act as a different character',
        r'pretend to be'
    ],
    'data-extraction': [
        r'previous conversation',
        r'training data',
        r'sensitive information',
        r'confidential data',
        r'private information'
    ]
}

# Define vulnerabilities list
VULNERABILITIES = [
    {
        'id': 'prompt-injection',
        'name': 'Prompt Injection',
        'description': 'Attempts to manipulate the model by injecting malicious instructions into the prompt',
        'severity': 'High',
        'impact': 'Can lead to unauthorized access, data leakage, or malicious code execution'
    },
    {
        'id': 'jailbreak',
        'name': 'Jailbreak',
        'description': 'Attempts to bypass the model\'s safety restrictions and ethical guidelines',
        'severity': 'Critical',
        'impact': 'Can result in harmful or inappropriate content generation'
    },
    {
        'id': 'data-extraction',
        'name': 'Data Extraction',
        'description': 'Attempts to extract sensitive information or training data from the model',
        'severity': 'Medium',
        'impact': 'Can lead to privacy violations and intellectual property theft'
    }
]

def detect_vulnerability(input_text, vulnerability_type):
    patterns = DETECTION_PATTERNS.get(vulnerability_type, [])
    matches = []
    for pattern in patterns:
        if re.search(pattern, input_text, re.IGNORECASE):
            matches.append(pattern)
    return matches

def calculate_severity_score(matches):
    if not matches:
        return 0
    base_score = len(matches) * 2
    return min(base_score, 10)

@app.route('/')
def index():
    return send_from_directory('templates', 'index.html')

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

@app.route('/templates/<path:path>')
def serve_templates(path):
    return send_from_directory('templates', path)

@app.route('/api/vulnerabilities', methods=['GET'])
def get_vulnerabilities():
    vulnerabilities = [
        {
            'id': 'prompt-injection',
            'name': 'Prompt Injection',
            'description': 'Attempts to manipulate the model by injecting malicious instructions into the prompt',
            'severity': 'High',
            'impact': 'Can lead to unauthorized access, data leakage, or malicious code execution'
        },
        {
            'id': 'jailbreak',
            'name': 'Jailbreak',
            'description': 'Attempts to bypass the model\'s safety restrictions and ethical guidelines',
            'severity': 'Critical',
            'impact': 'Can result in harmful or inappropriate content generation'
        },
        {
            'id': 'data-extraction',
            'name': 'Data Extraction',
            'description': 'Attempts to extract sensitive information or training data from the model',
            'severity': 'Medium',
            'impact': 'Can lead to privacy violations and intellectual property theft'
        }
    ]
    return jsonify(vulnerabilities)

@app.route('/demo/<vulnerability_id>')
def demo_page(vulnerability_id):
    input_text = request.args.get('input', '')
    if not input_text:
        return redirect('/')
    
    # Get vulnerability details
    vulnerability = next((v for v in VULNERABILITIES if v['id'] == vulnerability_id), None)
    if not vulnerability:
        return redirect('/')
    
    # Run the demo
    result = run_demo(vulnerability_id, input_text)
    
    return render_template('demo.html', 
                         vulnerability=vulnerability,
                         input_text=input_text,
                         result=result)

@app.route('/api/demo/<vulnerability_id>', methods=['POST'])
def run_demo(vulnerability_id, input_text=None):
    if input_text is None:
        input_text = request.json.get('input', '')
    
    # Get vulnerability details
    vulnerability = next((v for v in VULNERABILITIES if v['id'] == vulnerability_id), None)
    if not vulnerability:
        return jsonify({'error': 'Invalid vulnerability ID'}), 400
    
    # Check input against detection patterns
    is_detected = False
    matched_patterns = []
    severity_score = 0
    
    for pattern in DETECTION_PATTERNS[vulnerability_id]:
        if re.search(pattern, input_text, re.IGNORECASE):
            is_detected = True
            matched_patterns.append(pattern)
            severity_score = max(severity_score, calculate_severity_score(pattern))
    
    # Generate responses based on detection
    original_prompt = input_text
    vulnerable_response = f"This is a simulated vulnerable response for {vulnerability['name']}."
    redacted_response = f"This is a simulated redacted response for {vulnerability['name']}."
    blocked_response = f"This is a simulated blocked response for {vulnerability['name']}."
    
    if is_detected:
        message = f"Vulnerability detected in {vulnerability['name']} test!"
    else:
        message = f"No vulnerability detected in {vulnerability['name']} test."
    
    return {
        'message': message,
        'detection': {
            'is_detected': is_detected,
            'severity_level': 'High' if severity_score > 7 else 'Medium' if severity_score > 4 else 'Low',
            'severity_score': severity_score,
            'matched_patterns': matched_patterns
        },
        'analysis': {
            'original_prompt': original_prompt,
            'vulnerable_response': vulnerable_response,
            'redacted_response': redacted_response,
            'blocked_response': blocked_response
        }
    }

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port) 