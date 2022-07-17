<template>
  <div class="preview-container">
    <div class="main-par">
      <el-image
        class="main-par-img"
        src="/main_page/bg_header.png"
        :fit="fit"
      />
    </div>
    <div class="main-p">
      <p class="p2">NEW METHOD TO FAST</p>
      <p class="p1">RECOVER</p>

      <p class="p3">TM</p>

      <p class="p4"><span>⌵</span><span>⌵</span></p>
    </div>
  </div>
</template>

<script>
export default {
  name: "FiPagePreview",
};
</script>

<style lang="scss">
.main-container {
  display: flex;
  flex-direction: column;

  .preview-container {
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;

    .main-par {
      .main-par-img {
        animation-name: bg-image;
        animation-duration: 1.5s;
        animation-fill-mode: forwards;
        position: relative;
        z-index: 1;
      }
    }

    .main-p {
      .p1 {
        animation: no-letter, letter-apper, fadeIn; /* referring directly to the animation's @keyframe declaration */
        animation-duration: 2s, 1s, 1s; /* don't forget to set a duration! */
        animation-delay: 0s, 2s, 2s;

        color: #0836b5;
        font-style: normal;
        font-weight: 900;
        font-size: 16vw;
        line-height: 12vw;
        margin-bottom: 0;
      }

      .p2 {
        animation: no-letter, letter-apper, fadeInDown; /* referring directly to the animation's @keyframe declaration */
        animation-duration: 3.5s, 1s, 1s; /* don't forget to set a duration! */
        animation-delay: 0s, 3.5s, 3.5s;

        color: #0836b5;
        font-style: normal;
        font-weight: 900;
        font-size: 4vw;
        line-height: 5vh;
        margin-bottom: 0;

        text-align: start;
      }

      .p3 {
        animation: no-letter, letter-apper, fadeInUp; /* referring directly to the animation's @keyframe declaration */
        animation-duration: 3.5s, 1s, 1s; /* don't forget to set a duration! */
        animation-delay: 0s, 3.5s, 3.5s;

        color: #0836b5;
        font-style: normal;
        font-weight: 900;
        font-size: 4vw;
        line-height: 5vh;
        margin-bottom: 0;

        text-align: end;
      }

      .p4 {
        animation: no-letter, letter-apper, fadeInDown, top-down; /* referring directly to the animation's @keyframe declaration */
        animation-duration: 5s, 1s, 1s, 2s; /* don't forget to set a duration! */
        animation-delay: 0s, 5s, 5s, 7.5s;
        animation-iteration-count: 1, 1, 1, infinite;
        display: flex;
        flex-direction: column;

        color: #0836b5;
        font-style: normal;
        font-weight: 900;
        font-size: 19vw;
        margin-bottom: 0;
        position: relative;
        line-height: 10px;
        top: 55vw;

        text-align: center;
      }

      position: absolute;
      align-items: center;
      z-index: 2;
    }

    @keyframes top-down {
      0% {
        top: 55vw;
      }
      50% {
        top: 50vw;
      }
      100% {
        top: 55vw;
      }
    }

    @keyframes no-letter {
      0% {
        opacity: 0;
      }
      100% {
        opacity: 0;
      }
    }

    @keyframes letter-apper {
      0% {
        opacity: 0;
      }
      100% {
        opacity: 1;
      }
    }

    @keyframes bg-image {
      0% {
        width: 100vw;
        height: 100vh;
        opacity: 0.2;
      }

      100% {
        width: 50vw;
        height: 50vh;
        opacity: 1;
      }
    }
  }

  .data-container {
    height: 100vh;
  }
}
</style>
