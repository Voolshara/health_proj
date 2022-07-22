<template>
  <div class="block-container">
    <div><p>RE</p></div>
    <div class="special-block">
      <div class="bg-text" style="color: white">COV</div>
      <div class="special-element">sdf</div>
    </div>
    <div><p>ER</p></div>
  </div>
</template>

<script>
export default {
  name: "MainPageElement",
};
</script>

<style lang="scss">
.block-container {
  width: 90vw;
  height: 120vh;
  opacity: 0.9;

  p {
    font-family: "Microsoft YaHei";
    z-index: 1;
  }

  color: white;
  font-size: 400px;
  line-height: 400px;
  -webkit-text-stroke: 5pt #0836b5;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-items: center;
}

.special-block {
  opacity: 0.9;
  color: white;
  -webkit-text-stroke: 5pt #34000000;
  background-color: black;

  .bg-text {
    z-index: 1;
    position: relative;
    top: -15%;
    color: rgba(255, 255, 255, 0.327);
  }

  .special-element {
    z-index: 2;
    position: relative;
  }
}
</style>
