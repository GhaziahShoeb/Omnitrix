from google import genai
import os
import json


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_campaign(
    customer_segment,
    product,
    channel,
    offer,
    goal
):

    prompt = f"""
You are an expert digital marketing strategist.

Create a personalized marketing campaign.

Customer Segment:
{customer_segment}

Product:
{product}

Channel:
{channel}

Offer:
{offer}

Goal:
{goal}


Return ONLY valid JSON:

{{
    "subject": "",
    "message": "",
    "call_to_action": ""
}}

Keep it concise and conversion focused.
"""


    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )


    text = response.text


    # Remove markdown if Gemini returns ```json
    text = text.replace(
        "```json",
        ""
    ).replace(
        "```",
        ""
    )


    return json.loads(text)