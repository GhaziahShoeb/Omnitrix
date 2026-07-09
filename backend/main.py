from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
load_dotenv()
import joblib
import numpy as np
from backend.utils.recommendation import recommend_action
from backend.utils.campaign_generator import generate_campaign

app = FastAPI(
    title="OmniCX AI API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
model = joblib.load(
    "backend/model/intent_model.pkl"
)



class Customer(BaseModel):

    age:int

    website_visits:int

    pages_viewed:int

    time_spent:int

    cart_added:int

    previous_purchase:int

    email_open_rate:float

    discount_used:int


class CampaignRequest(BaseModel):

    customer_segment: str

    product: str

    channel: str

    offer: str

    goal: str

@app.get("/")
def home():

    return {
        "message":
        "OmniCX AI is running"
    }



@app.post("/predict")
def predict(customer:Customer):


    data=np.array([[

    customer.age,

    customer.website_visits,

    customer.pages_viewed,

    customer.time_spent,

    customer.cart_added,

    customer.previous_purchase,

    customer.email_open_rate,

    customer.discount_used

]])


    probability = model.predict_proba(data)[0][1]


    if probability > 0.7:
        intent="HIGH"

    elif probability > 0.4:
        intent="MEDIUM"

    else:
        intent="LOW"



    reasons=[]


    if customer.cart_added:
        reasons.append(
            "Customer added product to cart"
        )


    if customer.previous_purchase > 0:
        reasons.append(
            "Previous purchase history"
        )


    if customer.time_spent > 30:
        reasons.append(
            "High website engagement"
        )


    recommendation = recommend_action(
    customer,
    intent
)

    recommendation = recommend_action(
        customer,
        intent
    )
    return {

    "purchase_probability":
    round(probability*100,2),

    "intent":
    intent,

    "reasons":
    reasons,

    "recommendation":
    recommendation

    }
@app.post("/generate_campaign")
def generate_campaign_endpoint(
    request: CampaignRequest
):

    result = generate_campaign(
        request.customer_segment,
        request.product,
        request.channel,
        request.offer,
        request.goal
    )

    return result