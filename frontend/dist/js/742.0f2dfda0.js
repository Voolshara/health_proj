"use strict";(self["webpackChunkfrontend"]=self["webpackChunkfrontend"]||[]).push([[742],{2629:function(e,t,l){l.d(t,{Z:function(){return w}});var a=l(3396);const o=e=>((0,a.dD)("data-v-904be2b4"),e=e(),(0,a.Cn)(),e),i={class:"two-sliders"},n={style:{display:"flex","flex-direction":"column"}},s=o((()=>(0,a._)("p",null,"Укажите силу",-1))),r={class:"slider-demo-block"},d={style:{display:"flex","flex-direction":"column"}},m=o((()=>(0,a._)("p",null,"Укажите силу",-1))),u={class:"slider-demo-block"},f=(0,a.Uk)("Отправить запрос на восстановление");function p(e,t,l,o,p,c){const h=(0,a.up)("el-slider"),_=(0,a.up)("el-form-item"),w=(0,a.up)("el-button"),g=(0,a.up)("el-form");return(0,a.wg)(),(0,a.j4)(g,{model:p.form,class:"container-form"},{default:(0,a.w5)((()=>[(0,a._)("div",i,[(0,a.Wm)(_,{style:{"margin-left":"0"}},{default:(0,a.w5)((()=>[(0,a._)("div",n,[s,(0,a._)("div",r,[(0,a.Wm)(h,{modelValue:p.form.left,"onUpdate:modelValue":t[0]||(t[0]=e=>p.form.left=e),vertical:"",height:"400px",min:0,max:5,step:.1,size:"large",marks:p.marks},null,8,["modelValue","step","marks"])])])])),_:1}),(0,a.Wm)(_,null,{default:(0,a.w5)((()=>[(0,a._)("div",d,[m,(0,a._)("div",u,[(0,a.Wm)(h,{modelValue:p.form.right,"onUpdate:modelValue":t[1]||(t[1]=e=>p.form.right=e),vertical:"",height:"400px",min:0,max:5,step:.1,size:"large",marks:p.marks},null,8,["modelValue","step","marks"])])])])),_:1})]),(0,a.Wm)(_,null,{default:(0,a.w5)((()=>[(0,a.Wm)(w,{type:"primary",onClick:e.onSubmit},{default:(0,a.w5)((()=>[f])),_:1},8,["onClick"])])),_:1})])),_:1},8,["model"])}var c={name:"BottomSlider",data(){return{form:{left:1,right:1},marks:{0:"0x",1:"1x",2:"2x",3:"3x",4:"4x",5:"5x"}}},props:{task_num:String},onSubmit:function(){const e=this.form;e["task_num"]=this.task_num,fetch("http://45.91.8.150:5600/tasks",{method:"POST",mode:"cors",cache:"no-cache",credentials:"same-origin",headers:{"Content-Type":"application/json","Access-Control-Allow-Private-Network":!0},redirect:"follow",referrerPolicy:"no-referrer",body:JSON.stringify({data:e})}).then((e=>e.json())).then((e=>{this.form_is_send=!0,console.log(e)})).catch((e=>(console.error("Error:",e),null)))}},h=l(89);const _=(0,h.Z)(c,[["render",p],["__scopeId","data-v-904be2b4"]]);var w=_},7862:function(e,t,l){l.d(t,{Z:function(){return f}});var a=l(3396);const o=e=>((0,a.dD)("data-v-870486c8"),e=e(),(0,a.Cn)(),e),i=(0,a.Uk)("Отправить"),n=o((()=>(0,a._)("p",null,"*Это окно свёрстано, но ещё не подключено!!!*",-1))),s=o((()=>(0,a._)("p",null,"*Нажмите куда либо за пределы окна*",-1)));function r(e,t,l,o,r,d){const m=(0,a.up)("el-input"),u=(0,a.up)("el-form-item"),f=(0,a.up)("el-button"),p=(0,a.up)("el-form"),c=(0,a.up)("el-dialog");return(0,a.wg)(),(0,a.j4)(c,{modelValue:r.dialogVisible,"onUpdate:modelValue":t[2]||(t[2]=e=>r.dialogVisible=e),title:"Введите номер своего личного кабинета",width:"40%","show-close":!1},{default:(0,a.w5)((()=>[(0,a.Wm)(p,{model:r.form,"label-width":"100px",style:{margin:"40px","margin-bottom":"0","margin-left":"10px"}},{default:(0,a.w5)((()=>[(0,a.Wm)(u,{label:"Ваша почта","label-width":e.formLabelWidth},{default:(0,a.w5)((()=>[(0,a.Wm)(m,{modelValue:r.form.email,"onUpdate:modelValue":t[0]||(t[0]=e=>r.form.email=e),autocomplete:"off"},null,8,["modelValue"])])),_:1},8,["label-width"]),(0,a.Wm)(u,{label:"Код","label-width":e.formLabelWidth},{default:(0,a.w5)((()=>[(0,a.Wm)(m,{modelValue:r.form.password,"onUpdate:modelValue":t[1]||(t[1]=e=>r.form.password=e),autocomplete:"off"},null,8,["modelValue"])])),_:1},8,["label-width"]),(0,a.Wm)(u,null,{default:(0,a.w5)((()=>[(0,a.Wm)(f,{type:"primary",onClick:e.onSubmit},{default:(0,a.w5)((()=>[i])),_:1},8,["onClick"])])),_:1})])),_:1},8,["model"]),n,s])),_:1},8,["modelValue"])}var d={name:"DialogForm2",data(){return{dialogVisible:!0,form:{email:"",password:""}}},methods:{}},m=l(89);const u=(0,m.Z)(d,[["render",r],["__scopeId","data-v-870486c8"]]);var f=u},1742:function(e,t,l){l.r(t),l.d(t,{default:function(){return C}});var a=l(3396);const o=e=>((0,a.dD)("data-v-0271cf29"),e=e(),(0,a.Cn)(),e),i={class:"container-form"},n=o((()=>(0,a._)("p",{class:"main-par"},"Задание 3",-1))),s=o((()=>(0,a._)("p",{class:"sub_information",style:{"font-size":"20px"}}," Данное движение необходимо совершить пациенту с максимальной силой (на столько быстро на сколько это возможно) как показано на видео ниже. Каждую мышцу следует проверять поочередно (с применением силы ассистента), регулируйте каждый ползунок для уточнения силы данной мышцы у пациента ",-1))),r=o((()=>(0,a._)("p",{style:{"text-align":"left",width:"30vw"}}," Первоначальное состояние пациента - сидя на стуле / со спиной в 90° ",-1))),d=o((()=>(0,a._)("p",{style:{"text-align":"left",width:"30vw"}}," Первоначальное положение обеих сторон - нога слегка вытянута , носок слегка вытянут вперед ",-1))),m=o((()=>(0,a._)("div",{style:{"text-align":"left",width:"30vw"}},[(0,a._)("p",null," Место проверки для обеих сторон от лица ассистента - обхватить ребро наружной стороны стопы Сопротивление ассистента - 0/5 (просто приложить) "),(0,a._)("p",null,"Сила пациента - MAX ↑"),(0,a._)("p",null,"Скорость пациента - MAX ↑")],-1))),u={style:{display:"flex"}},f=o((()=>(0,a._)("div",{style:{width:"30px"}},null,-1))),p=o((()=>(0,a._)("div",{style:{"text-align":"left",width:"30vw"}},[(0,a._)("p",null," Конечное положение обеих сторон - поворот стопы в наружную сторону без поворота ноги ")],-1))),c={style:{display:"flex"}},h=o((()=>(0,a._)("div",{style:{width:"30px"}},null,-1))),_=(0,a.Uk)("Левая нога"),w=(0,a.Uk)("Правая нога"),g=o((()=>(0,a._)("video",{width:"300",height:"300",controls:""},[(0,a._)("source",{src:"/img/task1/p_leg_1.mp4",type:"video/mp4"})],-1))),W=o((()=>(0,a._)("video",{width:"300",height:"300",controls:""},[(0,a._)("source",{src:"/img/task1/p_leg_2.mp4",type:"video/mp4"})],-1)));function k(e,t,l,o,k,v){const x=(0,a.up)("Dialog"),y=(0,a.up)("el-divider"),b=(0,a.up)("el-col"),V=(0,a.up)("el-image"),C=(0,a.up)("el-row"),j=(0,a.up)("BottomSlider");return(0,a.wg)(),(0,a.iD)("div",i,[(0,a.Wm)(x),n,s,(0,a.Wm)(y),(0,a.Wm)(C,{class:"task-container"},{default:(0,a.w5)((()=>[(0,a.Wm)(b,{span:13},{default:(0,a.w5)((()=>[r])),_:1}),(0,a.Wm)(b,{span:11},{default:(0,a.w5)((()=>[(0,a.Wm)(V,{style:{width:"200px",height:"200px"},src:"/img/task1/1.jpg",fit:e.fit},null,8,["fit"])])),_:1})])),_:1}),(0,a.Wm)(C,{class:"task-container"},{default:(0,a.w5)((()=>[(0,a.Wm)(b,{span:13},{default:(0,a.w5)((()=>[d])),_:1}),(0,a.Wm)(b,{span:11},{default:(0,a.w5)((()=>[(0,a.Wm)(V,{style:{width:"200px",height:"200px"},src:"/img/task1/2.jpg",fit:e.fit},null,8,["fit"])])),_:1})])),_:1}),(0,a.Wm)(C,{class:"task-container"},{default:(0,a.w5)((()=>[(0,a.Wm)(b,{span:13},{default:(0,a.w5)((()=>[m])),_:1}),(0,a.Wm)(b,{span:11},{default:(0,a.w5)((()=>[(0,a._)("div",u,[(0,a.Wm)(V,{style:{width:"200px",height:"200px"},src:"/img/task1/3.1.jpg",fit:e.fit},null,8,["fit"]),f,(0,a.Wm)(V,{style:{width:"200px",height:"200px"},src:"/img/task1/3.2.jpg",fit:e.fit},null,8,["fit"])])])),_:1})])),_:1}),(0,a.Wm)(C,{class:"task-container"},{default:(0,a.w5)((()=>[(0,a.Wm)(b,{span:13},{default:(0,a.w5)((()=>[p])),_:1}),(0,a.Wm)(b,{span:11},{default:(0,a.w5)((()=>[(0,a._)("div",c,[(0,a.Wm)(V,{style:{width:"200px",height:"200px"},src:"/img/task1/4.1.jpg",fit:e.fit},null,8,["fit"]),h,(0,a.Wm)(V,{style:{width:"200px",height:"200px"},src:"/img/task1/4.2.jpg",fit:e.fit},null,8,["fit"])])])),_:1})])),_:1}),(0,a.Wm)(C,{style:{"margin-top":"50px"}},{default:(0,a.w5)((()=>[(0,a.Wm)(b,{span:15},{default:(0,a.w5)((()=>[_])),_:1}),(0,a.Wm)(b,{span:4},{default:(0,a.w5)((()=>[w])),_:1})])),_:1}),(0,a.Wm)(C,{style:{"margin-top":"30px"}},{default:(0,a.w5)((()=>[(0,a.Wm)(b,{span:15},{default:(0,a.w5)((()=>[g])),_:1}),(0,a.Wm)(b,{span:3},{default:(0,a.w5)((()=>[W])),_:1})])),_:1}),(0,a.Wm)(j,{task_num:"task3"})])}var v=l(7862),x=l(2629),y={name:"FormFirst",components:{Dialog:v.Z,BottomSlider:x.Z},data(){return{form:{left:1,right:1}}},methods:{onSubmit:function(){fetch("http://localhost:5600/form1",{method:"POST",mode:"cors",cache:"no-cache",credentials:"same-origin",headers:{"Content-Type":"application/json","Access-Control-Allow-Private-Network":!0},redirect:"follow",referrerPolicy:"no-referrer",body:JSON.stringify({data:this.form})}).then((e=>e.json())).then((e=>{this.form_is_send=!0,console.log(e)})).catch((e=>(console.error("Error:",e),null)))}}},b=l(89);const V=(0,b.Z)(y,[["render",k],["__scopeId","data-v-0271cf29"]]);var C=V}}]);
//# sourceMappingURL=742.0f2dfda0.js.map