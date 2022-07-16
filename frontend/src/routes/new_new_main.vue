<template>
  <div class="main-container">
    <video-player :options="videoOptions" />
  </div>
</template>

<script>
import VideoPlayer from "@/components/video.vue";

export default {
  name: "VideoExample",
  components: {
    VideoPlayer,
  },
  data() {
    return {
      videoOptions: {
        autoplay: true,
        controls: false,
        sources: [
          {
            src: "/main_page/Brainstem..mp4",
            type: "video/mp4",
          },
        ],
      },
    };
  },
};
</script>

<style lang="scss">
.main-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.global-footer {
  display: none;
}
</style>
