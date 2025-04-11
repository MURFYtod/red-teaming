# LLM Security Dashboard

A demonstration tool for showcasing LLM vulnerabilities and their detection mechanisms.

## Features
- Interactive demonstration of LLM vulnerabilities
- Real-time detection of malicious prompts
- Visual feedback on security measures
- Educational examples of prompt injection, jailbreaking, and data extraction

## Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Docker and Docker Compose (for containerized deployment)

## Installation

### Option 1: Local Installation
1. Clone the repository:
```bash
git clone <repository-url>
cd llm-security-dashboard
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Option 2: Docker Installation
1. Clone the repository:
```bash
git clone <repository-url>
cd llm-security-dashboard
```

2. Build and run using Docker Compose:
```bash
docker-compose up --build
```

## Running the Application

### Local Run
1. Start the Flask server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

### Docker Run
1. The application will be available at:
```
http://localhost:5000
```

## Sharing Options

### 1. Local Network Sharing
To share with others on your local network:
1. Find your computer's IP address:
   - Windows: Run `ipconfig` in Command Prompt
   - Linux/Mac: Run `ifconfig` in Terminal
2. Start the server with host parameter:
```bash
python app.py --host 0.0.0.0
```
3. Others can access using: `http://<your-ip>:5000`

### 2. Docker Network Sharing
1. Run the container with:
```bash
docker-compose up --build
```
2. Share your IP address with others on your network
3. They can access using: `http://<your-ip>:5000`

### 3. Cloud Deployment Options

#### Option A: Docker on Cloud Provider
1. Push your Docker image to a registry (Docker Hub, ECR, etc.)
2. Deploy to your preferred cloud provider
3. Configure networking and security groups
4. Access via the provided URL

#### Option B: Heroku with Docker
1. Install Heroku CLI
2. Login to Heroku
3. Create a new app
4. Deploy using:
```bash
heroku container:push web
heroku container:release web
```

## Security Considerations
- This is a demonstration tool - do not deploy in production without proper security measures
- Keep the application behind a firewall when sharing
- Use HTTPS in production
- Consider adding authentication for sensitive deployments

## Troubleshooting
- If port 5000 is in use, you can change it in docker-compose.yml
- Make sure all dependencies are installed
- Check firewall settings if others can't connect
- Ensure Docker is properly installed and running
- For Docker issues, try:
  ```bash
  docker-compose down
  docker-compose up --build
  ```

## License
This project is for educational purposes only. 