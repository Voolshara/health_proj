import { createApp } from "vue";
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

const app = createApp(App).use(router);
app.use(ElementPlus, { locale: RuLocale });
app.use(Particles);
app.use(VueWriter);

app.mount("#app");

export function isValidJwt(jwt) {
  if (!jwt || jwt.split(".").length < 3) {
    return false;
  }
  const data = JSON.parse(atob(jwt.split(".")[1]));
  const exp = new Date(data.exp * 1000); // JS deals with dates in milliseconds since epoch
  const now = new Date();
  return now < exp;
}
