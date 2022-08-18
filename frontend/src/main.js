import { createApp } from "vue";
import App from "./App.vue";
import ElementPlus from "element-plus";
import "element-plus/dist/index.css";
// import "animate.css";
import "./bootstrap.min.css"; // css от старой главной страницы
import "./red.css"; // css от старой главной страницы
import "./style.css"; // css от старой главной страницы

import router from "./router";
import Particles from "vue-particles"; // нужно для главной страницы
import VueWriter from "vue-writer";
import RuLocale from "element-plus/es/locale/lang/ru";
import VueAnimateOnScroll from "vue3-animate-onscroll";

import store from "./store";

const app = createApp(App).use(router);
app.use(ElementPlus, { locale: RuLocale });
app.use(VueAnimateOnScroll);
app.use(Particles);
app.use(VueWriter);
app.use(store);

app.mount("#app");
