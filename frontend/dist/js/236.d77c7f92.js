"use strict";(self["webpackChunkfrontend"]=self["webpackChunkfrontend"]||[]).push([[236],{2629:function(t,e,l){l.d(e,{Z:function(){return w}});var s=l(3396);const i=t=>((0,s.dD)("data-v-904be2b4"),t=t(),(0,s.Cn)(),t),a={class:"two-sliders"},n={style:{display:"flex","flex-direction":"column"}},o=i((()=>(0,s._)("p",null,"Укажите силу",-1))),r={class:"slider-demo-block"},d={style:{display:"flex","flex-direction":"column"}},m=i((()=>(0,s._)("p",null,"Укажите силу",-1))),f={class:"slider-demo-block"},c=(0,s.Uk)("Отправить запрос на восстановление");function p(t,e,l,i,p,u){const h=(0,s.up)("el-slider"),_=(0,s.up)("el-form-item"),w=(0,s.up)("el-button"),g=(0,s.up)("el-form");return(0,s.wg)(),(0,s.j4)(g,{model:p.form,class:"container-form"},{default:(0,s.w5)((()=>[(0,s._)("div",a,[(0,s.Wm)(_,{style:{"margin-left":"0"}},{default:(0,s.w5)((()=>[(0,s._)("div",n,[o,(0,s._)("div",r,[(0,s.Wm)(h,{modelValue:p.form.left,"onUpdate:modelValue":e[0]||(e[0]=t=>p.form.left=t),vertical:"",height:"400px",min:0,max:5,step:.1,size:"large",marks:p.marks},null,8,["modelValue","step","marks"])])])])),_:1}),(0,s.Wm)(_,null,{default:(0,s.w5)((()=>[(0,s._)("div",d,[m,(0,s._)("div",f,[(0,s.Wm)(h,{modelValue:p.form.right,"onUpdate:modelValue":e[1]||(e[1]=t=>p.form.right=t),vertical:"",height:"400px",min:0,max:5,step:.1,size:"large",marks:p.marks},null,8,["modelValue","step","marks"])])])])),_:1})]),(0,s.Wm)(_,null,{default:(0,s.w5)((()=>[(0,s.Wm)(w,{type:"primary",onClick:t.onSubmit},{default:(0,s.w5)((()=>[c])),_:1},8,["onClick"])])),_:1})])),_:1},8,["model"])}var u={name:"BottomSlider",data(){return{form:{left:1,right:1},marks:{0:"0x",1:"1x",2:"2x",3:"3x",4:"4x",5:"5x"}}},props:{task_num:String},onSubmit:function(){const t=this.form;t["task_num"]=this.task_num,fetch("http://45.91.8.150:5600/tasks",{method:"POST",mode:"cors",cache:"no-cache",credentials:"same-origin",headers:{"Content-Type":"application/json","Access-Control-Allow-Private-Network":!0},redirect:"follow",referrerPolicy:"no-referrer",body:JSON.stringify({data:t})}).then((t=>t.json())).then((t=>{this.form_is_send=!0,console.log(t)})).catch((t=>(console.error("Error:",t),null)))}},h=l(89);const _=(0,h.Z)(u,[["render",p],["__scopeId","data-v-904be2b4"]]);var w=_},236:function(t,e,l){l.r(e),l.d(e,{default:function(){return j}});var s=l(3396);const i=t=>((0,s.dD)("data-v-53ff4c4c"),t=t(),(0,s.Cn)(),t),a={class:"container-form"},n=i((()=>(0,s._)("p",{class:"main-par"},"Задание 3",-1))),o=i((()=>(0,s._)("p",{class:"sub_information",style:{"font-size":"20px"}}," Данное движение необходимо совершить пациенту с максимальной силой (на столько быстро на сколько это возможно) как показано на видео ниже. Каждую мышцу следует проверять поочередно (с применением силы ассистента), регулируйте каждый ползунок для уточнения силы данной мышцы у пациента ",-1))),r=i((()=>(0,s._)("p",{style:{"text-align":"left",width:"30vw"}}," Первоначальное состояние пациента - сидя на стуле / со спиной в 90° ",-1))),d=i((()=>(0,s._)("p",{style:{"text-align":"left",width:"30vw"}}," Первоначальное положение обеих сторон - нога слегка вытянута , носок слегка вытянут вперед ",-1))),m=i((()=>(0,s._)("div",{style:{"text-align":"left",width:"30vw"}},[(0,s._)("p",null," Место проверки для обеих сторон от лица ассистента - обхватить ребро наружной стороны стопы Сопротивление ассистента - 0/5 (просто приложить) "),(0,s._)("p",null,"Сила пациента - MAX ↑"),(0,s._)("p",null,"Скорость пациента - MAX ↑")],-1))),f={style:{display:"flex"}},c=i((()=>(0,s._)("div",{style:{width:"30px"}},null,-1))),p=i((()=>(0,s._)("div",{style:{"text-align":"left",width:"30vw"}},[(0,s._)("p",null," Конечное положение обеих сторон - поворот стопы в наружную сторону без поворота ноги ")],-1))),u={style:{display:"flex"}},h=i((()=>(0,s._)("div",{style:{width:"30px"}},null,-1))),_=(0,s.Uk)("Левая нога"),w=(0,s.Uk)("Правая нога"),g=i((()=>(0,s._)("video",{width:"300",height:"300",controls:""},[(0,s._)("source",{src:"/img/task1/p_leg_1.mp4",type:"video/mp4"})],-1))),k=i((()=>(0,s._)("video",{width:"300",height:"300",controls:""},[(0,s._)("source",{src:"/img/task1/p_leg_2.mp4",type:"video/mp4"})],-1)));function x(t,e,l,i,x,y){const v=(0,s.up)("el-divider"),W=(0,s.up)("el-col"),b=(0,s.up)("el-image"),j=(0,s.up)("el-row"),S=(0,s.up)("BottomSlider");return(0,s.wg)(),(0,s.iD)("div",a,[n,o,(0,s.Wm)(v),(0,s.Wm)(j,{class:"task-container"},{default:(0,s.w5)((()=>[(0,s.Wm)(W,{span:13},{default:(0,s.w5)((()=>[r])),_:1}),(0,s.Wm)(W,{span:11},{default:(0,s.w5)((()=>[(0,s.Wm)(b,{style:{width:"200px",height:"200px"},src:"/img/task1/1.jpg",fit:t.fit},null,8,["fit"])])),_:1})])),_:1}),(0,s.Wm)(j,{class:"task-container"},{default:(0,s.w5)((()=>[(0,s.Wm)(W,{span:13},{default:(0,s.w5)((()=>[d])),_:1}),(0,s.Wm)(W,{span:11},{default:(0,s.w5)((()=>[(0,s.Wm)(b,{style:{width:"200px",height:"200px"},src:"/img/task1/2.jpg",fit:t.fit},null,8,["fit"])])),_:1})])),_:1}),(0,s.Wm)(j,{class:"task-container"},{default:(0,s.w5)((()=>[(0,s.Wm)(W,{span:13},{default:(0,s.w5)((()=>[m])),_:1}),(0,s.Wm)(W,{span:11},{default:(0,s.w5)((()=>[(0,s._)("div",f,[(0,s.Wm)(b,{style:{width:"200px",height:"200px"},src:"/img/task1/3.1.jpg",fit:t.fit},null,8,["fit"]),c,(0,s.Wm)(b,{style:{width:"200px",height:"200px"},src:"/img/task1/3.2.jpg",fit:t.fit},null,8,["fit"])])])),_:1})])),_:1}),(0,s.Wm)(j,{class:"task-container"},{default:(0,s.w5)((()=>[(0,s.Wm)(W,{span:13},{default:(0,s.w5)((()=>[p])),_:1}),(0,s.Wm)(W,{span:11},{default:(0,s.w5)((()=>[(0,s._)("div",u,[(0,s.Wm)(b,{style:{width:"200px",height:"200px"},src:"/img/task1/4.1.jpg",fit:t.fit},null,8,["fit"]),h,(0,s.Wm)(b,{style:{width:"200px",height:"200px"},src:"/img/task1/4.2.jpg",fit:t.fit},null,8,["fit"])])])),_:1})])),_:1}),(0,s.Wm)(j,{style:{"margin-top":"50px"}},{default:(0,s.w5)((()=>[(0,s.Wm)(W,{span:15},{default:(0,s.w5)((()=>[_])),_:1}),(0,s.Wm)(W,{span:4},{default:(0,s.w5)((()=>[w])),_:1})])),_:1}),(0,s.Wm)(j,{style:{"margin-top":"30px"}},{default:(0,s.w5)((()=>[(0,s.Wm)(W,{span:15},{default:(0,s.w5)((()=>[g])),_:1}),(0,s.Wm)(W,{span:3},{default:(0,s.w5)((()=>[k])),_:1})])),_:1}),(0,s.Wm)(S,{task_num:"task3"})])}var y=l(2629),v={name:"FormFirst",components:{BottomSlider:y.Z},data(){return{form:{left:1,right:1}}},methods:{onSubmit:function(){fetch("http://localhost:5600/form1",{method:"POST",mode:"cors",cache:"no-cache",credentials:"same-origin",headers:{"Content-Type":"application/json","Access-Control-Allow-Private-Network":!0},redirect:"follow",referrerPolicy:"no-referrer",body:JSON.stringify({data:this.form})}).then((t=>t.json())).then((t=>{this.form_is_send=!0,console.log(t)})).catch((t=>(console.error("Error:",t),null)))}}},W=l(89);const b=(0,W.Z)(v,[["render",x],["__scopeId","data-v-53ff4c4c"]]);var j=b}}]);
//# sourceMappingURL=236.d77c7f92.js.map