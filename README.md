# 🎬 MovieRama

**MovieRama** is a social movie sharing app where users can post their favorite films and vote on others with either a *like* or a *hate*.

---

## 🚀 Features
### Core Features

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

### Extras

- ✅ Approval rating (% of likes)
- ✅ Sort by rating
- ✅ Sorting and filter state shown in the UI
- ✅ Vote status visible to the user
- ✅ Pagination with sort/filter support
- ✅ Demo data auto-population
- ✅ Health check endpoint for Render
- ✅ Scroll position preserved after vote actions

---

## 📦 Setup Instructions




### 1. Clone the repo
```bash
git clone https://github.com/FullMetalAlchemistEMP/MovieRama.git
cd MovieRama
```
### 2. Create your `.env` file

Copy the example environment file and rename it:

```bash
cp .env.example .env
```

### 3. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```
### 4. Install dependencies
```bash
pip install -r requirements.txt
```
### 5. Apply database migrations
```bash
python manage.py migrate
```
### 6. Start the development server
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
