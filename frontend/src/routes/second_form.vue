<template>
  <div class="container-form">
    <Dialog />
    <p class="main-par">Анкета 2</p>
    <p class="sub_information" style="font-size: 30px">
      В данном тесте вам необходимо замерить диаметр мышц
    </p>
    <p class="sub_information" style="font-size: 20px">Правила:</p>
    <el-row
      style="align-items: center; justify-content: center; padding-bottom: 50px"
    >
      <el-col
        v-for="(o, index) in rules"
        :key="o"
        :span="o[2]"
        :offset="index > 0 ? 1 : 0"
      >
        <el-card :body-style="{ padding: '2px' }">
          <img :src="o[0]" class="image" />
          <div style="padding: 14px">
            <div class="bottom">
              <span>{{ o[1] }}</span>
            </div>
          </div>
        </el-card>
      </el-col>
    </el-row>
    <el-form :model="form" label-width="200px" class="form">
      <el-form-item> Отличается ли у вас чувствительность ног? </el-form-item>
      <el-form-item label="">
        <el-radio-group v-model="form.differences_of_legs">
          <el-radio :label="true" size="large" border>Да</el-radio>
          <el-radio :label="false" size="large" border>Нет</el-radio>
        </el-radio-group>
      </el-form-item>

      <el-form-item> Отличается ли у вас чувствительность рук? </el-form-item>
      <el-form-item label="">
        <el-radio-group v-model="form.differences_of_arms">
          <el-radio :label="true" size="large" border>Да</el-radio>
          <el-radio :label="false" size="large" border>Нет</el-radio>
        </el-radio-group>
      </el-form-item>

      <el-form-item>Обхват талии (Ø \ см):</el-form-item>
      <el-form-item>
        <el-input-number
          v-model="form.waist"
          :controls="false"
          placeholder="Укажите число в см"
          size="large"
        />
      </el-form-item>

      <el-form-item
        >Диаметр выше колена на больной стороне (Ø \ см):</el-form-item
      >
      <el-form-item>
        <el-input-number
          v-model="form.above_the_knee"
          :controls="false"
          placeholder="Укажите число в см"
          size="large"
        />
      </el-form-item>

      <el-form-item>Обхват талии (Ø \ см):</el-form-item>
      <el-form-item>
        <el-input-number
          v-model="form.below_the_knee"
          :controls="false"
          placeholder="Укажите число в см"
          size="large"
        />
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import Dialog from "@/components/dialog.vue";
export default {
  name: "FormFirst",
  components: {
    Dialog,
  },
  data() {
    return {
      rules: [
        [
          "/img/form_2_p1.png",
          "Все измерения необходимо выполнять сидя, на расслабленное тело",
          8,
        ],
        ["/img/form_2_p2.jpg", "Все измерения должны быть точными", 5],
        [
          "/img/form_2_p3.jpg",
          "Все измерения должны быть производиться в системе СИ {см/кг}",
          5,
        ],
      ],
      form: {
        place_of_injure: "",
        differences_of_legs: "",
        differences_of_arms: "",
        waist: null,
        above_the_knee: null,
        below_the_knee: null,
      },
    };
  },
  methods: {
    onSubmit: function () {
      // fetch("http://localhost:5600/form2", {
      fetch("http://localhost:5600/article_data", {
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
          console.log(data);
        })
        .catch((error) => {
          console.error("Error:", error);
          return null;
        });
    },
  },
};
</script>

<style>
.container-form {
  align-items: center;
  text-align: center;
}

.sub_information {
  width: 70vw;
  margin: auto;
  margin-bottom: 15px;
}

.form {
  position: relative;
  align-self: center;
  padding: 0 3vw 0 0;
  width: 60vw;
  margin: auto;
}

.main-par {
  color: #0836b5;
  background-image: url("@/assets/bg_header.png");
  font-style: normal;
  font-weight: 900;
  font-size: 70px;
  line-height: 145px;
}

.image {
  width: 100%;
  height: 300px;
  display: block;
}

.bottom {
  height: 10vh;
  margin-top: 13px;
  line-height: 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
</style>
