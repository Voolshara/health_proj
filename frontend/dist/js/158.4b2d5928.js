"use strict";(self["webpackChunkfrontend"]=self["webpackChunkfrontend"]||[]).push([[158],{3158:function(e,l,a){a.r(l),a.d(l,{default:function(){return C}});var t=a(3396),n=a(7139);const i={class:"container-user"},c=(0,t._)("img",{src:"/img/user.png",class:"image"},null,-1),s={class:"info-cont"},m={style:{display:"flex","justify-content":"center"}},d={class:"main-container"},o=(0,t._)("p",{style:{"margin-top":"70px","font-size":"50px","margin-bottom":"30px"}}," Заполнение пациента ",-1),_=(0,t.Uk)("Пока ещё не готово ("),b=(0,t.Uk)("Пока ещё не готово ("),r=(0,t.Uk)("Пока ещё не готово (");function w(e,l,a,w,f,u){const g=(0,t.up)("el-col"),y=(0,t.up)("el-descriptions-item"),k=(0,t.up)("el-descriptions"),p=(0,t.up)("el-row"),h=(0,t.up)("Selection"),W=(0,t.up)("el-tab-pane"),U=(0,t.up)("el-tabs");return(0,t.wg)(),(0,t.iD)("div",i,[(0,t.Uk)((0,n.zw)(f.data)+" ",1),(0,t.Wm)(p,{class:"top-bunner"},{default:(0,t.w5)((()=>[(0,t.Wm)(g,{span:9},{default:(0,t.w5)((()=>[c])),_:1}),(0,t.Wm)(g,{span:12},{default:(0,t.w5)((()=>[(0,t._)("div",s,[(0,t.Wm)(k,{title:"Информация о пользователе",column:1,border:""},{default:(0,t.w5)((()=>[(0,t.Wm)(y,{label:"ID пользователя","label-align":"left",align:"center","label-class-name":"my-label","class-name":"my-content",width:"0"},{default:(0,t.w5)((()=>[(0,t.Uk)((0,n.zw)(f.data["id"]),1)])),_:1}),(0,t.Wm)(y,{label:"Почта","label-align":"left",align:"center","label-class-name":"my-label","class-name":"my-content",width:"0"},{default:(0,t.w5)((()=>[(0,t.Uk)((0,n.zw)(f.data["email"]),1)])),_:1}),(0,t.Wm)(y,{label:"Имя","label-align":"left",align:"center","label-class-name":"my-label","class-name":"my-content",width:"0"},{default:(0,t.w5)((()=>[(0,t.Uk)((0,n.zw)(f.data["name"]),1)])),_:1}),(0,t.Wm)(y,{label:"Фамилия","label-align":"left",align:"center","label-class-name":"my-label","class-name":"my-content",width:"0"},{default:(0,t.w5)((()=>[(0,t.Uk)((0,n.zw)(f.data["last_name"]),1)])),_:1}),(0,t.Wm)(y,{label:"Пол","label-align":"left",align:"center","label-class-name":"my-label","class-name":"my-content",width:"0"},{default:(0,t.w5)((()=>[(0,t.Uk)((0,n.zw)(f.data["gender"]),1)])),_:1}),(0,t.Wm)(y,{label:"Страна","label-align":"left",align:"center","label-class-name":"my-label","class-name":"my-content",width:"0"},{default:(0,t.w5)((()=>[(0,t.Uk)((0,n.zw)(f.data["Country"]),1)])),_:1}),(0,t.Wm)(y,{label:"Телефон","label-align":"left",align:"center","label-class-name":"my-label","class-name":"my-content",width:"0"},{default:(0,t.w5)((()=>[(0,t.Uk)((0,n.zw)(f.data["Phone"]),1)])),_:1}),(0,t.Wm)(y,{label:"Был ли у вас инсульт?","label-align":"left",align:"center","label-class-name":"my-label","class-name":"my-content",width:"0"},{default:(0,t.w5)((()=>[(0,t.Uk)((0,n.zw)(f.is_been_stroke),1)])),_:1})])),_:1})])])),_:1})])),_:1}),(0,t._)("div",m,[(0,t._)("div",d,[o,(0,t.Wm)(U,{modelValue:f.activeTab,"onUpdate:modelValue":l[0]||(l[0]=e=>f.activeTab=e),class:"demo-tabs",onTabClick:e.handleClick},{default:(0,t.w5)((()=>[(0,t.Wm)(W,{label:"Отборная анкета",name:1,class:"selection"},{default:(0,t.w5)((()=>[(0,t.Wm)(h,{data:f.data,no_stroke_mes:f.some_text},null,8,["data","no_stroke_mes"])])),_:1}),(0,t.Wm)(W,{label:"Первая форма",name:2},{default:(0,t.w5)((()=>[_])),_:1}),(0,t.Wm)(W,{label:"Вторая форма",name:3},{default:(0,t.w5)((()=>[b])),_:1}),(0,t.Wm)(W,{label:"Задание 1 - 8",name:4},{default:(0,t.w5)((()=>[r])),_:1})])),_:1},8,["modelValue","onTabClick"])])])])}const f={key:0},u=(0,t._)("p",{class:"no-stroke-text"},"У пацианта нет инсульта",-1),g={class:"no-stroke-mes"},y=(0,t._)("p",null,"Сообщение:",-1),k={key:1},p={key:0},h={key:1};function W(e,l,a,i,c,s){const m=(0,t.up)("el-descriptions-item"),d=(0,t.up)("el-descriptions");return a.data["Selection"]?((0,t.wg)(),(0,t.iD)("div",k,[(0,t.Wm)(d,{column:1,border:""},{default:(0,t.w5)((()=>[(0,t.Wm)(m,{label:"Дата Инсульта","label-align":"left",align:"center","label-class-name":"my-label","class-name":"my-content",width:"0"},{default:(0,t.w5)((()=>[(0,t.Uk)((0,n.zw)(this.data["Selection_dict"]["date_of_stroke"].split(" ")[1]+" "+this.data["Selection_dict"]["date_of_stroke"].split(" ")[2]+" "+this.data["Selection_dict"]["date_of_stroke"].split(" ")[3]),1)])),_:1}),(0,t.Wm)(m,{label:"Вид Инсульта","label-align":"left",align:"center","label-class-name":"my-label","class-name":"my-content",width:"0"},{default:(0,t.w5)((()=>[(0,t.Uk)((0,n.zw)(a.data["Selection_dict"]["type_of_stroke"]),1)])),_:1}),(0,t.Wm)(m,{label:"Знает ли пользователь причину?","label-align":"left",align:"center","label-class-name":"my-label","class-name":"my-content",width:"0"},{default:(0,t.w5)((()=>[(0,t.Uk)((0,n.zw)(a.data["Selection_dict"]["is_knew_reason"]),1)])),_:1}),(0,t.Wm)(m,{label:"Проецент воспринимаемой информации","label-align":"left",align:"center","label-class-name":"my-label","class-name":"my-content",width:"0"},{default:(0,t.w5)((()=>[(0,t.Uk)((0,n.zw)(a.data["Selection_dict"]["percent_of_information"])+"%",1)])),_:1}),(0,t.Wm)(m),(0,t.Wm)(m,{label:"Имеется ли движения на поражённой ноге?","label-align":"left",align:"center","label-class-name":"my-label","class-name":"my-content",width:"0"},{default:(0,t.w5)((()=>[(0,t.Uk)((0,n.zw)(a.data["Selection_dict"]["is_injured_leg_movemented"]),1)])),_:1}),"Да"==a.data["Selection_dict"]["is_injured_leg_movemented"]?((0,t.wg)(),(0,t.iD)("div",p,[(0,t.Wm)(m,{label:"На сколько % работает нога?","label-align":"left",align:"center","label-class-name":"my-label","class-name":"my-content",width:"0"},{default:(0,t.w5)((()=>[(0,t.Uk)((0,n.zw)(a.data["Selection_dict"]["percent_of_injured_leg_movemented"])+"% ",1)])),_:1}),(0,t.Wm)(m,{label:"Имеется ли у вас движения в голеностопе?","label-align":"left",align:"center","label-class-name":"my-label","class-name":"my-content",width:"0"},{default:(0,t.w5)((()=>[(0,t.Uk)((0,n.zw)(a.data["Selection_dict"]["is_injured_ankle_movemented"]),1)])),_:1}),(0,t.Wm)(m,{label:"Может ли пациент сидеть без опоры под спину?","label-align":"left",align:"center","label-class-name":"my-label","class-name":"my-content",width:"0"},{default:(0,t.w5)((()=>[(0,t.Uk)((0,n.zw)(a.data["Selection_dict"]["is_can_sit"]),1)])),_:1}),(0,t.Wm)(m,{label:"Может ли пациент самостоятельно стоять?","label-align":"left",align:"center","label-class-name":"my-label","class-name":"my-content",width:"0"},{default:(0,t.w5)((()=>[(0,t.Uk)((0,n.zw)(a.data["Selection_dict"]["is_can_state"]),1)])),_:1}),(0,t.Wm)(m,{label:"Может ли пациент ходить с опорой?","label-align":"left",align:"center","label-class-name":"my-label","class-name":"my-content",width:"0"},{default:(0,t.w5)((()=>[(0,t.Uk)((0,n.zw)(a.data["Selection_dict"]["is_patient_walk_with_supports"]),1)])),_:1}),(0,t.Wm)(m,{label:"Сгибается ли нога в колленом суставе?","label-align":"left",align:"center","label-class-name":"my-label","class-name":"my-content",width:"0"},{default:(0,t.w5)((()=>[(0,t.Uk)((0,n.zw)(a.data["Selection_dict"]["is_knee_bend"]),1)])),_:1}),(0,t.Wm)(m,{label:"Имеются ли у вас движения на поражённой руке?","label-align":"left",align:"center","label-class-name":"my-label","class-name":"my-content",width:"0"},{default:(0,t.w5)((()=>[(0,t.Uk)((0,n.zw)(a.data["Selection_dict"]["is_knee_unbend"]),1)])),_:1})])):(0,t.kq)("",!0),(0,t.Wm)(m),(0,t.Wm)(m,{label:"Имеются ли у вас движения на поражённой руке?","label-align":"left",align:"center","label-class-name":"my-label","class-name":"my-content",width:"0"},{default:(0,t.w5)((()=>[(0,t.Uk)((0,n.zw)(a.data["Selection_dict"]["is_injured_arm_movemented"]),1)])),_:1}),"Да"==a.data["Selection_dict"]["is_injured_arm_movemented"]?((0,t.wg)(),(0,t.iD)("div",h,[(0,t.Wm)(m,{label:"На сколько % работает рука?","label-align":"left",align:"center","label-class-name":"my-label","class-name":"my-content",width:"0"},{default:(0,t.w5)((()=>[(0,t.Uk)((0,n.zw)(a.data["Selection_dict"]["percent_of_injured_arm_movemented"])+"%",1)])),_:1}),(0,t.Wm)(m,{label:"Сгибается ли рука в локтевом суставе?","label-align":"left",align:"center","label-class-name":"my-label","class-name":"my-content",width:"0"},{default:(0,t.w5)((()=>[(0,t.Uk)((0,n.zw)(a.data["Selection_dict"]["is_elbow_bend"]),1)])),_:1}),(0,t.Wm)(m,{label:"Разгибается ли рука в локтевом суставе?","label-align":"left",align:"center","label-class-name":"my-label","class-name":"my-content",width:"0"},{default:(0,t.w5)((()=>[(0,t.Uk)((0,n.zw)(a.data["Selection_dict"]["is_elbow_unbend"]),1)])),_:1}),(0,t.Wm)(m,{label:"Сгибается ли рука в предплечье?","label-align":"left",align:"center","label-class-name":"my-label","class-name":"my-content",width:"0"},{default:(0,t.w5)((()=>[(0,t.Uk)((0,n.zw)(a.data["Selection_dict"]["is_forearm_bend"]),1)])),_:1}),(0,t.Wm)(m,{label:"Разгибается  ли рука в предплечье?","label-align":"left",align:"center","label-class-name":"my-label","class-name":"my-content",width:"0"},{default:(0,t.w5)((()=>[(0,t.Uk)((0,n.zw)(a.data["Selection_dict"]["is_forearm_unbend"]),1)])),_:1}),(0,t.Wm)(m,{label:"Имеются ли у вас движения в пальцах на руке?","label-align":"left",align:"center","label-class-name":"my-label","class-name":"my-content",width:"0"},{default:(0,t.w5)((()=>[(0,t.Uk)((0,n.zw)(a.data["Selection_dict"]["is_injured_finger_movemented"]),1)])),_:1})])):(0,t.kq)("",!0),(0,t.Wm)(m),(0,t.Wm)(m,{label:"В каком году планируетe восстанавливаться?","label-align":"left",align:"center","label-class-name":"my-label","class-name":"my-content",width:"0"},{default:(0,t.w5)((()=>[(0,t.Uk)((0,n.zw)(a.data["Selection_dict"]["now_year_to_repair"].replace("now","В этом").replace("later","В последующих")),1)])),_:1}),(0,t.Wm)(m,{label:"Где собираетесь восстанавливаться?","label-align":"left",align:"center","label-class-name":"my-label","class-name":"my-content",width:"0"},{default:(0,t.w5)((()=>[(0,t.Uk)((0,n.zw)(a.data["Selection_dict"]["where_to_repair"].replace("outside","За пределами страны").replace("in_my_country","В моей стране").replace("home","На дому")),1)])),_:1})])),_:1})])):((0,t.wg)(),(0,t.iD)("div",f,[u,(0,t._)("div",g,[y,(0,t._)("p",null,(0,n.zw)(a.no_stroke_mes),1)])]))}var U={name:"SelectionInPanel",props:{data:JSON,no_stroke_mes:String}},S=a(89);const z=(0,S.Z)(U,[["render",W]]);var v=z,j={name:"UserInPanel",components:{Selection:v},data(){return{data:{},is_been_stroke:"",activeTab:1,some_text:""}},mounted(){fetch("http://localhost:5600/panel/get_user_data",{method:"POST",mode:"cors",cache:"no-cache",credentials:"same-origin",headers:{"Content-Type":"application/json","Access-Control-Allow-Private-Network":!0},redirect:"follow",referrerPolicy:"no-referrer",body:JSON.stringify({user_id:this.$route.params.id})}).then((e=>e.json())).then((e=>{this.data=e["data"],this.some_text=this.data["Selection_dict"]["problem_no_strokes"]})).catch((()=>{}))}};const x=(0,S.Z)(j,[["render",w]]);var C=x}}]);
//# sourceMappingURL=158.4b2d5928.js.map