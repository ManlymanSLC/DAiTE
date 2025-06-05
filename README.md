# DAiTE — *AI-Concierge Dating Platform*  
Smart matches • Human-first safety • Real-world plans

---

## 0. TL;DR

```bash
# clone + enter repo
git clone https://github.com/<your-org>/DAiTE.git && cd DAiTE

# Python 3.12 virtual-env (macOS / Linux)
python3 -m venv venv && source venv/bin/activate

# install deps, incl. the real SQLAlchemy
pip install -r requirements.txt

# spin up a throw-away SQLite DB & run tests
pytest -q
