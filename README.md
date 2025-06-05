# DAiTE

DAiTE is an AI-concierge dating platform that builds a personal agent for every user. It matches compatible agents, plans real-world dates and captures post-date feedback.

## Getting Started

These instructions help you set up the project on macOS using a Python virtual environment.

1. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the tests**
   ```bash
   pytest -q
   ```

SQLAlchemy is required and listed in `requirements.txt`. If you do not have network access, ensure the package wheel is available locally.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
