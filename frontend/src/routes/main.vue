<template>
  <div class="wrapper">
    <section class="home">
      <video src="@/assets/video.mp4" autoplay muted loop></video>
      <Particles id="particles-js" />
      <div class="home-content">
        <h1 class="hero-title">
          <span>New Method to <br />Fast Recover</span>
        </h1>
        <p class="top_45">
          <span style="color: #004d85"
            >Beginning level to fast recover 1/3</span
          >
          <br />
          <VueWriter
            :array="arr"
            :typeSpeed="45"
            :eraseSpeed="20"
            :caret="'cursor'"
          />
        </p>
      </div>
    </section>

    <div class="cont">
      <section id="portfolio" class="portfolio">
        <div class="row text-center">
          <div class="col-md-6 top_30">
            <h2>Русский</h2>
            <p class="bottom_30">
              Для того чтобы мы начали изучать ваш инсульт более углубленно — вы
              должны пройти опрос перед началом нового метода по восстановлению
              / После окончания всех этапов метода по восстановлению вам будут
              выданы товары защищающие вас от повреждений.
            </p>
            <router-link to="/ru/terms/" class="site-btn2" style="margin: auto"
              >Начать</router-link
            >
          </div>
          <div class="col-md-6 top_30">
            <h2>English</h2>
            <p class="bottom_30">
              In order for us to study your stroke more closely — we must to
              make a more accurate selection with you — it starts after ﬁlling
              out all questions \ After ﬁnishing all steps from our recovery
              method — you will receive goods\devices to protect you from
              damages and our method to recover.
            </p>
            <router-link to="/en/terms/" class="site-btn2" style="margin: auto"
              >Start</router-link
            >
          </div>
        </div>
      </section>
    </div>
    <!-- cont end -->
  </div>
</template>

<style></style>

<script>
import Particles from "@/components/particles.vue";
export default {
  name: "MainPage",
  metaInfo: {
    // if no subcomponents specify a metaInfo.title, this title will be used
    title: "New Method to Fast Recover",
    // all titles will be injected into this template
    // titleTemplate: "%s | My Awesome Webapp",
  },
  components: {
    Particles,
  },
  data() {
    return {
      arr: [
        "Get early preparati",
        "Newest way of treatment after stroke",
        "Recovering from stroke experts (2-8 weeks)",
        "Get early preparation for our fast recovery method — Online",
        "Rehabilitate with new generation",
      ],
    };
  },
};
</script>
