<template>
  <el-form :model="form" class="container-form">
    <div class="two-sliders">
      <el-form-item style="margin-left: 0">
        <div style="display: flex; flex-direction: column">
          <p>Укажите силу</p>
          <div class="slider-demo-block">
            <el-slider
              v-model="form.left"
              vertical
              height="400px"
              :min="0"
              :max="5"
              :step="0.1"
              size="large"
              :marks="marks"
            />
          </div></div
      ></el-form-item>
      <el-form-item>
        <div style="display: flex; flex-direction: column">
          <p>Укажите силу</p>
          <div class="slider-demo-block">
            <el-slider
              v-model="form.right"
              vertical
              height="400px"
              :min="0"
              :max="5"
              :step="0.1"
              size="large"
              :marks="marks"
            />
          </div>
        </div>
      </el-form-item>
    </div>
    <el-form-item>
      <el-button type="primary" @click="onSubmit"
        >Отправить запрос на восстановление</el-button
      >
    </el-form-item>
  </el-form>
</template>

<script>
export default {
  name: "BottomSlider",
  data() {
    return {
      form: {
        left: 1,
        right: 1,
      },
      marks: { 0: "0x", 1: "1x", 2: "2x", 3: "3x", 4: "4x", 5: "5x" },
    };
  },
  props: {
    task_num: String,
  },
  onSubmit: function () {
    const send_data = this.form;
    send_data["task_num"] = this.task_num;
    // fetch("http://localhost:5600/new_user", {
    fetch("http://45.91.8.150:5600/tasks", {
      method: "POST", // *GET, POST, PUT, DELETE, etc.
      mode: "cors", // no-cors, *cors, same-origin
      cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
      credentials: "same-origin", // include, *same-origin, omit
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Private-Network": true,
      },
      redirect: "follow", // manual, *follow, error
      referrerPolicy: "no-referrer", // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
      body: JSON.stringify({
        data: send_data,
      }), // body data type must match "Content-Type" header
    })
      .then((response) => response.json())
      .then((data) => {
        this.form_is_send = true;
        console.log(data);
      })
      .catch((error) => {
        console.error("Error:", error);
        return null;
      });
  },
};
</script>

<style scoped>
.slider-demo-block {
  display: flex;
  align-items: center;
}
.slider-demo-block .el-slider {
  margin-top: 0;
  margin-left: 12px;
}

.container-form {
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin-top: 100px;
}

.two-sliders {
  display: flex;
  justify-content: space-evenly;
  width: 100vw;
}
</style>
