function result(el,el2,text='по')
{
    year=Number(el.value.slice(0,4))
    mounth=Number(el.value.slice(5,7))
    day=Number(el.value.slice(8,10))
    after=new Date(year,mounth-1,day+6,5)
    year=after.toISOString().slice(0,4)
    mounth=after.toISOString().slice(5,7)
    day=after.toISOString().slice(8,10)
    el2.innerHTML=text+" "+day+'-'+mounth+'-'+year

}
const el5 = document.getElementById('save-2');
const el6=document.querySelector('.save-3')
if (el6!==null)
    el5.scrollIntoView();
div_modal=document.getElementById("exampleModal")
if (div_modal!==null)
{   document.onclick=((e)=>{
     if (div_modal.style.display==="block")
        div_modal.style.display="none"
})}
div_hour=document.querySelector(".forjs")
// text_scientis=document.getElementById('text1')
// text_scientis.oninput=()=>{
//     console.log(text_scientis.value)
//     if (text_scientis.value.trim()==='') {
//         div_hour.hidden = true;
//         console.log("Nee");
//     }
//     else
//         div_hour.hidden=false
// }
el3=document.getElementById("23")
el4=document.querySelector(".data_after_user")
result(el3,el4)
el3.addEventListener("click",()=>{result(el3,el4);
})
el=document.getElementById("12345");
if (el!==null) {
    el2 = document.querySelector(".data_after_admin");
    result(el, el2)
    el.addEventListener("click", function () {
        result(el, el2)
    });
}
data_option=document.getElementById('data_opt')
if  (data_option!==null)
    result(el3,data_option,'')
see=document.getElementById("modal-otchet-full")
saw=document.getElementById("modal-otchet-load")
full=document.getElementById("full")
load=document.getElementById("load")
if (full!==null){
    full.addEventListener("click",()=>{
        see.hidden=false
     saw.hidden=true
    })
    load.addEventListener("click",()=>{
        see.hidden=true
        saw.hidden=false
    })
    }
