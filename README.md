# 🧠 SabiBiz AI

AI-Powered User Modeling & Recommendation Agent for Personalized Reviews and Business Discovery

## Overview

SabiBiz AI is an intelligent recommendation and user-modeling system designed to:

* Generate personalized reviews and ratings based on user behavior
* Recommend businesses using context-aware search
* Explain recommendations with AI insights
* Show business images and locations
* Support Nigerian conversational/localized outputs
* Run as a web app, Telegram bot, and Docker container

Built for the **BCT x DSN Hackathon**.

---

# Problem Statement

Traditional recommendation systems often:

* Ignore user personality
* Provide generic recommendations
* Lack explainability
* Fail to localize outputs culturally

SabiBiz AI addresses these gaps through AI-generated reviews, behavioral modeling, and contextual recommendations.

---

# Features

## Task 1 — User Modeling Agent

Input:

* User persona/history
* Selected business/product

Output:

* Predicted rating
* AI-generated review
* Behavioral analysis
* Personality classification

Examples:

* Positive reviewer
* Critical reviewer
* Balanced reviewer

---

## Task 2 — Recommendation Agent

Input:

Natural language query:

Examples:

```text
African restaurant in Tucson
Best pizza in Tampa
Cafe in Philadelphia
```

Output:

* Ranked recommendations
* Ratings
* Review counts
* Images
* Maps
* AI insights

---

# Project Structure

```text
SabiBiz_AI/
│
├── app/
│   ├── pages/
│   │      └── 1_User_Model_Agent.py
│   │
│   ├── dashboard.py
│   ├── telegram_bot.py
│   ├── router.py
│   ├── search_engine.py
│   ├── user_model.py
│   ├── review_generator.py
│   ├── business_explainer.py
│   ├── image_search.py
│   ├── main.py
│
├── data/
│   ├── businesses.csv
│   └── reviews_sample.csv
│
├── Dockerfile
├── requirements.txt
├── README.md
└── .env
```
## 🧠 Task A – AI Backend System
- FastAPI recommendation engine
- AI agent logic
- Business recommendation system

## 📊 Task B – User Interface Layer
- Streamlit dashboard
- Telegram bot interface
- Real-time interaction layer
---

# Dataset

Datasets used:

### businesses.csv

Contains:

* Business name
* Categories
* Ratings
* Review count
* Location

### reviews_sample.csv

Contains:

* User IDs
* Historical reviews
* Ratings

Inspired by Yelp business/review datasets.

---

# Installation

Clone repository:

```bash
git clone YOUR_GITHUB_LINK
cd SabiBiz_AI
```

Create environment:

```bash
python -m venv .venv
```

Activate:

Windows:

```bash
.venv\Scripts\activate
```

Install packages:

```bash
pip install -r requirements.txt
```

---

# Run Streamlit Dashboard

```bash
streamlit run app/dashboard.py
```

Open:

```text
http://localhost:8501
```

---

# Run User Modeling Agent

```bash
streamlit run app/pages/1_User_Model_Agent.py
```

---

# Run Telegram Bot

Add keys in:

```env
TELEGRAM_BOT_TOKEN=
GROQ_API_KEY=
PEXELS_API_KEY=
```

Then:

```bash
python app/telegram_bot.py
```

---

# Docker

Build:

```bash
docker build -t sabibiz-ai .
```

Run:

```bash
docker run -p 8501:8501 --env-file .env sabibiz-ai
```

Open:

```text
http://localhost:8501
```

---

# Tech Stack

* Python
* Pandas
* Streamlit
* FastAPI
* Docker
* Groq API
* Telegram Bot API
* Pexels API

---

# Future Improvements

Possible upgrades:

* Long-term memory
* Collaborative filtering
* Better personalization
* Real-time learning
* Stronger Nigerian contextualization

---

# Authors

Developed by:

Azeez Samad & Team

For:

BCT x DSN Hackathon

---

# License

Educational / Hackathon Use
