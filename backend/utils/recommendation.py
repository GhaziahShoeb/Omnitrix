def recommend_action(customer, intent):


    # High intent customers

    if intent == "HIGH":

        if customer.cart_added:

            return {

                "channel":"Email",

                "action":
                "Send cart recovery campaign",

                "best_time":
                "7 PM",

                "offer":
                "10% discount",

                "reason":
                "Customer abandoned cart with high purchase intent"

            }


        return {

            "channel":"Push Notification",

            "action":
            "Send personalized product recommendation",

            "best_time":
            "6 PM",

            "offer":
            "Free shipping",

            "reason":
            "Customer is actively researching"

        }



    # Medium intent

    elif intent == "MEDIUM":

        return {

            "channel":"Social Ads",

            "action":
            "Run retargeting campaign",

            "best_time":
            "Weekend",

            "offer":
            "Limited time offer",

            "reason":
            "Customer needs additional engagement"

        }



    # Low intent

    else:

        return {

            "channel":"Newsletter",

            "action":
            "Send awareness content",

            "best_time":
            "Weekly",

            "offer":
            "No discount",

            "reason":
            "Customer is still exploring"

        }