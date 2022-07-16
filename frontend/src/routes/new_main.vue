<template>
  <div class="main-container">
    <div id="app">
      <Preview />
      <!-- <video ref="videoRef" src="" class="start-video"></video> -->
    </div>
    sfdfdwfds
  </div>
</template>

<script>
import Preview from "@/components/first_page/preview.vue";
export default {
  name: "MainPage",
  components: {
    Preview,
  },
  // mounted: function () {
  //   this.$refs.videoRef.src = "/main_page/Preview-pc.mp4";
  //   this.$refs.videoRef.play();
  // },
};
</script>

<style lang="scss">
@import url("https://fonts.googleapis.com/css2?family=Montserrat:wght@800&display=swap");

::-webkit-scrollbar {
  display: none;
}

.global-footer {
  display: none;
}
</style>
