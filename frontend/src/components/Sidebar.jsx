import {
LayoutDashboard,
Users,
Megaphone,
BarChart3
} from "lucide-react";


export default function Sidebar(){


return (

<aside className="
w-72
bg-slate-900
border-r
border-slate-800
p-6
">


<h1 className="
text-2xl
font-bold
mb-10
">

OmniCX AI

</h1>


<div className="space-y-5">


<div className="
flex
gap-3
items-center
text-slate-300
hover:text-white
cursor-pointer
">

<LayoutDashboard size={20}/>
Dashboard

</div>


<div className="
flex
gap-3
items-center
text-slate-300
hover:text-white
cursor-pointer
">

<Users size={20}/>
Customers

</div>


<div className="
flex
gap-3
items-center
text-slate-300
hover:text-white
cursor-pointer
">

<Megaphone size={20}/>
Campaigns

</div>


<div className="
flex
gap-3
items-center
text-slate-300
hover:text-white
cursor-pointer
">

<BarChart3 size={20}/>
Analytics

</div>


</div>


</aside>

)

}