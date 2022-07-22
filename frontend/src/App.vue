<template>
  <router-view />
  <el-button
    :icon="ChatLineRound"
    circle
    v-if="type_problem !== null"
    @click="drawer = true"
    class="bot-invoker"
    type="success"
  />

  <el-drawer
    v-model="drawer"
    title="I am the title"
    :with-header="false"
    size="70%"
    v-if="isMobile()"
  >
    <Bot />
  </el-drawer>

  <el-drawer
    v-model="drawer"
    title="I am the title"
    :with-header="false"
    v-else
  >
    <Bot />
  </el-drawer>

  <Footer />
</template>

<script>
import Footer from "@/components/footer.vue";
import Bot from "./components/bot.vue";
import { ChatLineRound } from "@element-plus/icons-vue";
export default {
  name: "App",
  components: {
    Footer,
    Bot,
  },
  data() {
    return {
      drawer: false,
      ChatLineRound: ChatLineRound,
    };
  },
  methods: {
    isMobile() {
      if (
        /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(
          navigator.userAgent
        )
      ) {
        return true;
      } else {
        return false;
      }
    },
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&display=swap");

* {
  font-family: Montserrat;
  font-weight: 500;
}

.bot-invoker {
  position: fixed;
  z-index: 99999999;
  bottom: 8vh;
  right: 15vw;
}

.global-footer {
  display: contents;
}
</style>
