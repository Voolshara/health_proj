<template>
  <div class="container-form">
    <p class="main-par">Задание 1</p>
    <p class="sub_information" style="font-size: 20px">
      Индивидуальная подборка мышц Данное движение необходимо совершить пациенту
      с максимальной силой (на столько быстро на сколько это возможно) как
      показано на видео ниже. Каждую мышцу следует проверять поочередно (с
      применением силы ассистента), регулируйте каждый ползунок для уточнения
      силы данной мышцы у пациента
    </p>
    <el-divider />
    <div
      style="display: flex; flex-direction: row; justify-content: space-around"
    >
      <UserBar :data="panel_data" />
      <div style="width: 70vw">
        <el-row class="task-container">
          <el-col :span="13">
            <p style="text-align: left; width: 30vw">
              Первоначальное состояние пациента - сидя на стуле / со спиной в
              90°
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
              Первоначальное положение обеих сторон - нога слегка вытянута ,
              носок слегка вытянут вперед
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
                Место проверки для обеих сторон от лица ассистента - обхват
                щиколотки с передней стороны Сопротивление ассистента к силе
                пациента - 4/5
              </p>
              <p>Сила пациента - MAX ↑</p>
              <p>Скорость пациента - MAX ↑</p>
            </div></el-col
          >
          <el-col :span="11">
            <div style="display: flex">
              <el-image
                style="width: 200px; height: 200px"
                src="/img/task1/3.1.jpg"
                :fit="fit"
              />
              <div style="width: 30px"></div>
              <el-image
                style="width: 200px; height: 200px"
                src="/img/task1/3.2.jpg"
                :fit="fit"
              />
            </div>
          </el-col>
        </el-row>

        <el-row class="task-container">
          <el-col :span="13">
            <div style="text-align: left; width: 30vw">
              <p>
                Конечное состояние для обеих мышц - разогнутая нога оставаясь
                при правильном угле
              </p>
            </div></el-col
          >
          <el-col :span="11">
            <div style="display: flex">
              <el-image
                style="width: 200px; height: 200px"
                src="/img/task1/4.1.jpg"
                :fit="fit"
              />
              <div style="width: 30px"></div>
              <el-image
                style="width: 200px; height: 200px"
                src="/img/task1/4.2.jpg"
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
              <source src="/img/task1/1.mp4" type="video/mp4" /></video
          ></el-col>
          <el-col :span="3"
            ><video width="300" height="300" controls>
              <source src="/img/task1/2.mp4" type="video/mp4" />
            </video>
          </el-col>
        </el-row>

        <BottomSlider :task_num="'task1'" />
      </div>
    </div>
  </div>
</template>

<script>
import UserBar from "@/components/user_bar.vue";
import BottomSlider from "@/components/bottom_slider.vue";
export default {
  name: "FormFirst",
  components: {
    BottomSlider,
    UserBar,
  },
  data() {
    return {
      form: {
        left: 1,
        right: 1,
      },
      panel_data: null,
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
    write_data(val) {
      this.panel_data = val;
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
