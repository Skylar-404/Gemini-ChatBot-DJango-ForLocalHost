# Gemini Mini Chatbot

A lightweight chatbot powered by Google’s Gemini API, built with Django.  
This project is ready-to-use once configured — ideal for quick deployment and customization.

---

## 🚀 Getting Started

### 1. Clone the Repository
```
git clone https://github.com/Skylar-404/Gemini-ChatBot-DJango-ForLocalHost.git
```
### 2. Ensure Python is Installed

Make sure you already have Python 3.9+ installed on your machine.
Verify with:
```
python --version
```
For Python3 (Linux):
```
python3 --version
```
### 3. Create a Virtual Environment

It’s recommended to use a dedicated virtual environment:
```
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```
### 4. Install Requirements

Install dependencies from requirements.txt:

```
pip install -r requirements.txt
```
For Python3 (Linux):

```
pip3 install -r requirements.txt
```
### 5. Configure Environment Variables

Locate the file named `.env.example`

Rename it to `.env` (delete `.example` and add `.` in front)

Go to Google AI Studio and generate your API key

Copy the key and paste it into `.env`:
```
GOOGLE_API_KEY=your_generated_api_key_here
```
### 6. Run the Django Server

Start the development server:
```
python manage.py runserver
```

For Python3 (Linux):
```
python3 manage.py runserver
```
Your chatbot will be available at:
http://127.0.0.1:8000/

## 🎨 Customization

You can modify the chatbot interface by editing:

```
/templates/chat.html
```
This allows you to adjust the UI to your own style and needs.

## 📂 Project Structure

manage.py → Django entry point

requirements.txt → Dependencies

.env → Environment variables (API key)

/templates/chat.html → Chatbot interface

## 🛠 Notes

Always keep your API key private.

Add .env to .gitignore before pushing to GitHub.

For production, configure Django settings accordingly.

**Feel free to fork, customize, and submit pull requests.
This project is open-source and designed for flexibility.**
