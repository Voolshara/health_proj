<template>
  <div
    class="card-container"
    v-animate-onscroll="'animate__animated animate__fadeInUp'"
  >
    <el-image
      src="/main_page/heart.jpg"
      v-animate-onscroll="'animate__animated animate__fadeInRight'"
      class="img"
      fit="cover"
      ref="card-image"
    />
    <div v-animate-onscroll="'animate__animated animate__fadeInUp'">
      <p class="main-text">Lorem ipsum</p>
      <p class="sub-text">dolor sit amet</p>
      <p class="text">
        consectetur adipiscing elit. Duis metus justo, vehicula non urna quis,
        euismod viverra sem. Integer bibendum
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: "MPCard1",
};
</script>

<style lang="scss">
.card-container {
  display: flex;
  flex-direction: column;
  width: 100vw;
  margin-top: 40px;
  margin-bottom: 30px;

  .img {
    position: relative;
    left: 40%;
    width: 200px;
    height: 300px;
  }

  .main-text {
    font-family: "Microsoft YaHei";
    font-size: 40px;
    list-style: 41px;
    text-transform: capitalize;
    padding-left: 20px;
    margin-bottom: 0;
  }
  .sub-text {
    padding-left: 20px;
  }

  .text {
    width: 60vw;
    padding-left: 30px;
  }
}
</style>
