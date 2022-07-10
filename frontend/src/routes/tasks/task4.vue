<template>
  <div class="container-form">
    <Dialog />
    <p class="main-par">Задание 4</p>
    <p class="sub_information" style="font-size: 20px">
      Данное движение необходимо совершить пациенту с максимальной силой (на
      столько быстро на сколько это возможно) как показано на видео ниже. Каждую
      мышцу следует проверять поочередно (с применением силы ассистента),
      регулируйте каждый ползунок для уточнения силы данной мышцы у пациента
    </p>
    <el-divider />

    <el-row class="task-container">
      <el-col :span="13">
        <p style="text-align: left; width: 30vw">
          Первоначальное состояние пациента - сидя на стуле / со спиной в 90°
        </p></el-col
      >
      <el-col :span="11">
        <el-image
          style="width: 200px; height: 200px"
          src="/img/task1/1.jpg"
          :fit="fit"
        />
      </el-col>
    </el-row>

    <el-row class="task-container">
      <el-col :span="13">
        <p style="text-align: left; width: 30vw">
          Первоначальное положение обеих сторон - согнутые ноги под углом 90°
        </p></el-col
      >
      <el-col :span="11">
        <el-image
          style="width: 200px; height: 200px"
          src="/img/task1/2.jpg"
          :fit="fit"
        />
      </el-col>
    </el-row>

    <el-row class="task-container">
      <el-col :span="13">
        <div style="text-align: left; width: 30vw">
          <p>
            Место проверки для обеих сторон от лица ассистента - положить ладонь
            на конец носка и приложить силу Сопротивление ассистента - 2/5
          </p>
          <p>Сила пациента - MAX ↑</p>
          <p>Скорость пациента - MAX ↑</p>
        </div></el-col
      >
      <el-col :span="11">
        <div style="display: flex">
          <el-image
            style="width: 200px; height: 200px"
            src="/img/task1/ruka_l.jpg"
            :fit="fit"
          />
          <div style="width: 30px"></div>
          <el-image
            style="width: 200px; height: 200px"
            src="/img/task1/ruka_r.jpg"
            :fit="fit"
          />
        </div>
      </el-col>
    </el-row>

    <el-row class="task-container">
      <el-col :span="13">
        <div style="text-align: left; width: 30vw">
          <p>Конечное положение обеих сторон - поднятие пятки пациента</p>
        </div></el-col
      >
      <el-col :span="11">
        <div style="display: flex">
          <el-image
            style="width: 200px; height: 200px"
            src="/img/task1/ruka_l.jpg"
            :fit="fit"
          />
          <div style="width: 30px"></div>
          <el-image
            style="width: 200px; height: 200px"
            src="/img/task1/ruka_r.jpg"
            :fit="fit"
          />
        </div>
      </el-col>
    </el-row>

    <el-row style="margin-top: 50px">
      <el-col :span="15">Левая нога</el-col>
      <el-col :span="4">Правая нога</el-col>
    </el-row>

    <el-row style="margin-top: 30px">
      <el-col :span="15">
        <video width="300" height="300" controls>
          <source src="/img/task1/koleno_1.mp4" type="video/mp4" /></video
      ></el-col>
      <el-col :span="3"
        ><video width="300" height="300" controls>
          <source src="/img/task1/koleno_2.mp4" type="video/mp4" />
        </video>
      </el-col>
    </el-row>

    <BottomSlider :task_num="'task4'" />
  </div>
</template>

<script>
import Dialog from "@/components/dialog.vue";
import BottomSlider from "@/components/bottom_slider.vue";
export default {
  name: "FormFirst",
  components: {
    Dialog,
    BottomSlider,
  },
  data() {
    return {
      form: {
        left: 1,
        right: 1,
      },
    };
  },
  methods: {
    onSubmit: function () {
      // fetch("http://localhost:5600/form1", {
      fetch("http://localhost:5600/form1", {
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
          data: this.form,
        }), // body data type must match "Content-Type" header
      })
        .then((response) => response.json())
        .then((data) => {
          (this.form_is_send = true), console.log(data);
        })
        .catch((error) => {
          console.error("Error:", error);
          return null;
        });
    },
  },
};
</script>

<style scoped>
.slider-demo-block {
  display: flex;
  align-items: center;
  justify-content: space-around;
}
.slider-demo-block .el-slider {
  margin-top: 0;
  margin-left: 12px;
  background-color: darkcyan;
}
</style>

<style>
.container-form {
  align-items: center;
  text-align: center;
}

.task-container {
  width: 60vw;
  margin: auto;
  margin-top: 40px;
  margin-bottom: 20px;
  align-items: center;
}

.sub_information {
  width: 70vw;
  margin: auto;
  margin-bottom: 15px;
}

.main-par {
  color: #0836b5;
  background-image: url("@/assets/bg_header.png");
  font-style: normal;
  font-weight: 900;
  font-size: 70px;
  line-height: 145px;
}
</style>
