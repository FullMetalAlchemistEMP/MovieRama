# 🎬 MovieRama

**MovieRama** is a social movie sharing app where users can post their favorite films and vote on others with either a *like* or a *hate*.

---

## 🚀 Features
Core Features:

- ✅ User sign up, login, and logout
- ✅ Submit movies (title, description, created date, and owner)
- ✅ View list of all submitted movies
- ✅ Like or hate any movie (except your own)
- ✅ Users can:
  - Vote have one vote per movie
  - Switch vote from like ↔ hate
  - Retract vote altogether
- ✅ Filter movies by user (click the username)
- ✅ Sort movies by:
  - 👍 Likes
  - 👎 Hates
  - 🕒 Most recent

Extra:

- ✅ Show sorting and filter status in the UI
- ✅ Vote status is visible to the user
- ✅ Page scroll is preserved after voting

---

## 📦 Setup Instructions



```bash
### 1. Clone the repo

git clone https://github.com/YOUR_USERNAME/MovieRama.git
cd MovieRama

### 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Apply database migrations
python manage.py migrate

### 5. Start the development server
python manage.py runserver

Visit: http://localhost:8000