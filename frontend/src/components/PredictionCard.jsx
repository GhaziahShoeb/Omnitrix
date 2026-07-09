export default function PredictionCard({data}){


return (

<div className="
bg-white
p-6
rounded-2xl
shadow
">


<h2 className="
text-xl
font-bold
">

Customer Intent

</h2>


<p className="
text-4xl
font-bold
mt-5
text-blue-600
">

{data.intent}

</p>



<p className="mt-4">

Probability:

<b>
 {data.purchase_probability}%
</b>

</p>



<div className="
bg-gray-200
rounded-full
h-3
mt-3
">


<div

className="
bg-blue-600
h-3
rounded-full
"

style={{
width:`${data.purchase_probability}%`
}}

></div>


</div>



<h3 className="font-bold mt-6">

Reasons

</h3>


{
data.reasons.map(
(r,i)=>
<p key={i}>
{r}
</p>
)
}


</div>

)

}