import { createApp } from "vue";
import store from "./store/index";
import App from "./App.vue";
import ElementPlus from "element-plus";
import "element-plus/dist/index.css";
// import "animate.css";
import "./bootstrap.min.css";
import "./red.css";
import "./style.css";
import "animate.css";
import router from "./router";
import Particles from "vue-particles";
import VueWriter from "vue-writer";
import RuLocale from "element-plus/es/locale/lang/ru";
import VueAnimateOnScroll from "vue3-animate-onscroll";

const app = createApp(App).use(router);
app.use(ElementPlus, { locale: RuLocale });
app.use(VueAnimateOnScroll);
app.use(Particles);
app.use(VueWriter);
app.use(store);

app.mount("#app");
