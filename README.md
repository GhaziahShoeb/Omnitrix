# Omnitrix AI

## AI-Powered Customer Intelligence and Marketing Automation Platform

<div align="center">

Predict customer purchase intent, recommend the next best action, and generate personalized marketing campaigns using Machine Learning and Generative AI.

</div>


---

## Overview

OmniCX AI is an intelligent customer analytics platform that helps businesses understand customer behavior, predict conversion probability, and automate personalized marketing strategies.

The platform combines predictive machine learning models with generative AI capabilities to transform customer data into actionable business decisions.

Instead of using generic marketing approaches, OmniCX AI enables businesses to deliver personalized experiences by identifying:

- Which customers are most likely to convert
- What action should be taken next
- Which marketing channel should be used
- What personalized message should be delivered


---

# Key Features


## Customer Purchase Intent Prediction

OmniCX AI analyzes customer behavior and predicts the probability of conversion using machine learning.

The model considers:

- Website visits
- Pages viewed
- Time spent on platform
- Cart activity
- Previous purchase history
- Email engagement
- Discount usage


Example:

```
Purchase Probability: 91%

Customer Intent: HIGH

Reasons:
- Product added to cart
- Previous purchase history
- High website engagement
```


---

## Next Best Action Recommendation

The platform provides actionable marketing recommendations based on customer intent.

Example:

```
Channel:
Email

Action:
Send cart recovery campaign

Offer:
10% discount

Recommended Time:
7 PM
```


This helps businesses optimize customer engagement and improve conversion rates.


---

## AI Campaign Generation

OmniCX AI integrates Generative AI to automatically create personalized marketing content.

Generated outputs include:

- Email subject lines
- Marketing messages
- Call-to-action suggestions


Example:

```
Subject:
Level up your setup: 10% off your RTX laptop awaits


Message:
You have been exploring high-performance gaming hardware.
Upgrade today with an exclusive discount.


Call To Action:
Claim My Discount
```


---

## Analytics Dashboard

A modern dashboard provides:

- Customer insights
- Prediction results
- Marketing recommendations
- AI-generated campaigns


The interface is designed as a SaaS-style business intelligence platform.


---

# System Architecture


```
                    Customer Data
                         |
                         |
                         v

              Machine Learning Model

              Random Forest Classifier

                         |
                         |
                         v

              Purchase Intent Prediction

                         |
          --------------------------------
          |                              |
          v                              v

 Next Best Action                Gemini AI Generator

          |                              |
          --------------------------------

                         |
                         v

                 React Dashboard

```


---

# Technology Stack


## Machine Learning

| Technology | Purpose |
|------------|---------|
| Python | Model Development |
| Scikit-learn | Machine Learning |
| Pandas | Data Processing |
| NumPy | Numerical Operations |


## Backend

| Technology | Purpose |
|------------|---------|
| FastAPI | API Development |
| Uvicorn | Server Deployment |


## Generative AI

| Technology | Purpose |
|------------|---------|
| Google Gemini API | Marketing Content Generation |


## Frontend

| Technology | Purpose |
|------------|---------|
| React.js | User Interface |
| Vite | Frontend Development |
| Tailwind CSS | Styling Framework |
| Lucide Icons | UI Components |


---

# Project Structure


```
OmniCX-AI/

│
├── backend/
│   ├── main.py
│   └── utils/
│       └── campaign_generator.py
│
├── frontend/
│   ├── src/
│   ├── components/
│   └── package.json
│
├── ml/
│   ├── dataset_generator.py
│   └── train_model.py
│
├── models/
│   └── customer_model.pkl
│
├── data/
│   └── customers.csv
│
└── README.md

```


---

# Machine Learning Performance


Model:

```
Random Forest Classifier
```


Performance:

```
Accuracy: 93%

Precision: 93%

Recall: 93%

F1 Score: 93%
```


Important Features:

```
1. Cart Activity
2. Time Spent
3. Email Engagement
4. Previous Purchases
5. Website Interaction
```


---

# Installation and Setup


## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/OmniCX-AI.git

cd OmniCX-AI
```


---

## Backend Setup


Create virtual environment:

```bash
python3 -m venv venv
```


Activate:

```bash
source venv/bin/activate
```


Install dependencies:

```bash
pip install -r requirements.txt
```


Start backend:

```bash
uvicorn backend.main:app --reload
```


API available at:

```
http://127.0.0.1:8000
```


---

## Frontend Setup


Navigate to frontend:

```bash
cd frontend
```


Install dependencies:

```bash
npm install
```


Start application:

```bash
npm run dev
```


Frontend available at:

```
http://localhost:5173
```


---

# Environment Configuration


Create a `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```


Do not commit API keys or sensitive credentials.


---

# Application Workflow


```
Customer Behavior Data

        |

        v

Machine Learning Prediction

        |

        v

Customer Intent Classification

        |

        v

Next Best Action Recommendation

        |

        v

Generative AI Campaign Creation

        |

        v

Marketing Execution

```


---

# Future Improvements


## Customer Intelligence

- Real-time customer tracking
- Advanced customer segmentation
- Lifetime value prediction


## Marketing Automation

- Multi-channel campaigns
- Automated email scheduling
- WhatsApp and SMS integration


## AI Enhancements

- Large-scale customer personalization
- Conversational marketing assistant
- Revenue forecasting


---

# Motivation


Traditional marketing systems analyze historical customer behavior.

OmniCX AI goes a step further by predicting future customer actions and recommending the most effective engagement strategy.

The goal is to help businesses create personalized customer experiences powered by artificial intelligence.


---


Building intelligent customer experiences through AI-driven decision making.
