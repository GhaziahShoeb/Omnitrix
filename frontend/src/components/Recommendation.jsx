export default function Recommendation({data}){


return (

<div className="
bg-white
p-6
rounded-2xl
shadow
">


<h2 className="text-xl font-bold">

Next Best Action

</h2>


<p className="mt-5">

Channel:

<b>
{data.recommendation.channel}
</b>

</p>


<p className="mt-3">

Action:

{data.recommendation.action}

</p>


<p className="mt-3">

Offer:

{data.recommendation.offer}

</p>


<p className="mt-3">

Best Time:

{data.recommendation.best_time}

</p>


</div>

)

}