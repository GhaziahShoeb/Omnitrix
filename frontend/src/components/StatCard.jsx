export default function StatCard({title,value}){


return (

<div className="
bg-white
rounded-2xl
shadow-sm
p-6
border
border-slate-200
">


<p className="text-slate-500">
{title}
</p>


<h2 className="
text-3xl
font-bold
mt-3
">

{value}

</h2>


</div>

)

}