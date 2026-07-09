import { useState } from "react";
import API from "./api";

import Sidebar from "./components/Sidebar";
import StatCard from "./components/StatCard";
import PredictionCard from "./components/PredictionCard";
import Recommendation from "./components/Recommendation";
import CampaignCard from "./components/CampaignCard";


function App() {


  const [data, setData] = useState(null);

  const [loading, setLoading] = useState(false);

  const [error, setError] = useState("");



  async function analyzeCustomer() {


    try {

      setLoading(true);
      setError("");


      const customer = {

        age:25,

        website_visits:15,

        pages_viewed:25,

        time_spent:50,

        cart_added:1,

        previous_purchase:5,

        email_open_rate:0.8,

        discount_used:1

      };



      const prediction = await API.post(
        "/predict",
        customer
      );



      const campaign = await API.post(
        "/generate_campaign",
        {

          customer_segment:
          "High intent customer",


          product:
          "RTX Gaming Laptop",


          channel:
          "Email",


          offer:
          "10% discount",


          goal:
          "Increase conversions"

        }
      );



      setData({

        ...prediction.data,

        campaign:
        campaign.data

      });


    }


    catch(err){

      console.log(err);

      setError(
        "Unable to connect with AI service"
      );

    }


    finally{

      setLoading(false);

    }

  }




  return (

    <div className="
    flex
    min-h-screen
    bg-slate-950
    text-white
    ">


      <Sidebar />



      <main className="
      flex-1
      p-8
      overflow-y-auto
      ">



        {/* Header */}

        <div className="mb-10">


          <h1 className="
          text-4xl
          font-bold
          tracking-tight
          ">

          Customer Intelligence Dashboard

          </h1>



          <p className="
          text-slate-400
          mt-2
          ">

          AI powered customer analytics and
          marketing automation platform

          </p>


        </div>




        {/* Statistics */}


        <div className="
        grid
        grid-cols-1
        md:grid-cols-3
        gap-6
        mb-8
        ">


          <StatCard

          title="Customers Analyzed"

          value="50,000"

          />



          <StatCard

          title="Conversion Rate"

          value="91%"

          />



          <StatCard

          title="Campaigns Generated"

          value="8,230"

          />


        </div>





        {/* Analyze Button */}


        <button


        onClick={analyzeCustomer}


        disabled={loading}


        className="
        bg-blue-600
        hover:bg-blue-700
        disabled:bg-gray-600
        transition
        px-8
        py-3
        rounded-xl
        font-semibold
        shadow-lg
        ">


        {

          loading

          ?

          "Analyzing..."

          :

          "Analyze Customer"

        }


        </button>





        {
          error &&

          <p className="
          mt-5
          text-red-400
          ">

          {error}

          </p>

        }






        {

        data &&

        <div className="
        mt-10
        grid
        grid-cols-1
        md:grid-cols-2
        gap-6
        ">




          <PredictionCard

          data={data}

          />





          <Recommendation

          data={data.recommendation}

          />





          <CampaignCard

          data={data.campaign}

          />



        </div>


        }




      </main>



    </div>

  );

}


export default App;