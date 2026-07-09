import pandas as pd
import numpy as np


np.random.seed(42)

customers = 50000


df = pd.DataFrame({

    "user_id": range(1, customers+1),

    "age": np.random.randint(18,60,customers),

    "website_visits": np.random.randint(1,30,customers),

    "pages_viewed": np.random.randint(1,50,customers),

    "time_spent": np.random.randint(1,120,customers),

    "cart_added": np.random.randint(0,2,customers),

    "previous_purchase": np.random.randint(0,20,customers),

    "email_open_rate": np.random.uniform(0,1,customers),

    "discount_used": np.random.randint(0,2,customers)

})


# ----------------------------
# Customer Purchase Intent Logic
# ----------------------------

intent_score = (

    df["cart_added"] * 40 +

    df["website_visits"] * 1.5 +

    df["pages_viewed"] * 0.8 +

    df["time_spent"] * 0.3 +

    df["previous_purchase"] * 2 +

    df["email_open_rate"] * 20 +

    df["discount_used"] * 5
)


# Convert score into probability

probability = (
    intent_score - intent_score.min()
) / (
    intent_score.max() - intent_score.min()
)


# Customers with higher intent convert

df["conversion"] = (
    probability > 0.45
).astype(int)


# Add realistic mistakes (customer unpredictability)

noise = np.random.choice(
    df.index,
    size=2500,
    replace=False
)


df.loc[
    noise,
    "conversion"
] = 1 - df.loc[
    noise,
    "conversion"
]

print(df.head())
print(df["conversion"].value_counts())