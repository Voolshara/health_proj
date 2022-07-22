<template>
  <div class="card-container2">
    <div v-animate-onscroll="'animate__animated animate__fadeInUp'">
      <p class="main-text2">Lorem ipsum</p>
      <p class="sub-text2">dolor sit amet</p>
      <p class="text2">
        consectetur adipiscing elit. Duis metus justo, vehicula non urna quis,
        euismod viverra sem. Integer bibendum
      </p>
    </div>
    <el-image
      src="/main_page/heart.jpg"
      v-animate-onscroll="'animate__animated animate__fadeInRight'"
      class="img"
      fit="cover"
      ref="card-image"
    />
  </div>
</template>

<script>
export default {
  name: "MPCard1",
};
</script>

<style lang="scss">
.card-container2 {
  display: flex;
  flex-direction: column;
  width: 100vw;
  margin-top: 40px;
  margin-bottom: 30px;

  .img {
    position: relative;
    left: 10%;
    width: 200px;
    height: 300px;
  }

  .main-text2 {
    font-family: "Microsoft YaHei";
    position: relative;
    left: 25%;
    font-size: 40px;
    list-style: 41px;
    text-transform: capitalize;
    padding-right: 20px;
    margin-bottom: 0;
  }
  .sub-text2 {
    padding-left: 20px;
    position: relative;
    left: 55%;
  }

  .text2 {
    width: 80vw;
    padding-left: 30px;
  }
}
</style>
