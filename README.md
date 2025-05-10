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




### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/MovieRama.git
cd MovieRama
```
### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Apply database migrations
```bash
python manage.py migrate
```
### 5. Start the development server
```bash
python manage.py runserver
```
Visit: http://localhost:8000

---

## 🧪 Optional: Populate Demo Data

You can prefill the app with demo users, movies, and votes for quick testing or showcasing:
```bash
python manage.py populate_demo
```

## 🧪 Running Tests

To run tests:

```bash
python manage.py test movies
```

## 🔗 Live Demo

You can try the app live at:  
👉 [https://movierama-95ih.onrender.com](https://movierama-95ih.onrender.com)
