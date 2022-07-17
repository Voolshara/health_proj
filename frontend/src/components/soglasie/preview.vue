<template>
  <div class="first-page">
    <div class="first-anim">
      <span class="dot left"></span>
      <p class="animate__animated animate__fadeInTopLeft">Здравствуйте!</p>
      <span class="dot right"></span>
    </div>
    <div class="second-anim"></div>
  </div>
</template>

<style lang="scss">
.first-page {
  .first-anim {
    z-index: 1;
    p {
      margin: auto;
      font-weight: 800;
      color: #202020;
    }

    .dot {
      background-color: #202020;
      border-radius: 50%;
    }
    .left {
      position: absolute;
      animation-name: left-dot;
      animation-duration: 1s;
      animation-fill-mode: forwards;
    }

    .right {
      position: absolute;
      animation-name: right-dot;
      animation-duration: 1s;
      animation-fill-mode: forwards;
    }
  }

  .second-anim {
    z-index: 2;

    animation-name: grey-bg-1, grey-bg-2;
    animation-delay: 0s, 2s;
    animation-duration: 0.5s;
    animation-fill-mode: forwards;

    background-color: #202020;
    color: white;
    position: absolute;
    width: 100vw;
    height: 100vh;
  }

  width: 100vw;
  height: 100vh;
  font-size: 80px;

  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

@keyframes grey-bg-1 {
  0% {
    top: 100%;
    opacity: 0;
  }

  100% {
    top: 100%;
    opacity: 0;
  }
}

@keyframes grey-bg-2 {
  0% {
    top: 100%;
    opacity: 0;
  }

  100% {
    top: 0%;
    opacity: 1;
  }
}

@keyframes left-dot {
  0% {
    bottom: 0;
    left: -10%;
    height: 300px;
    width: 300px;
    opacity: 0;
  }

  100% {
    bottom: 70%;
    left: -10%;
    height: 600px;
    width: 700px;
    opacity: 1;
  }
}

@keyframes right-dot {
  0% {
    top: -20%;
    right: -25%;
    height: 300px;
    width: 300px;
    opacity: 0;
  }

  100% {
    top: 40%;
    right: -20%;
    height: 600px;
    width: 700px;
    opacity: 1;
  }
}
</style>

<script>
export default {
  name: "PreviewMainPage",
};
</script>
