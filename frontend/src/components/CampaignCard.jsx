export default function CampaignCard({data}){


return (

<div className="
bg-white
rounded-2xl
shadow
p-8
mt-8
">


<h2 className="
text-xl
font-bold
">

AI Campaign Studio

</h2>



<h3 className="
font-semibold
mt-5
">

{data.campaign.subject}

</h3>



<p className="
mt-4
text-gray-600
">

{data.campaign.message}

</p>



<button

className="
mt-6
bg-blue-600
text-white
px-6
py-3
rounded-xl
"

>

{data.campaign.call_to_action}

</button>


</div>

)

}