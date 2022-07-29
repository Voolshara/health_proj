<template>
  <div class="container-form">
    <p class="main-par">Заполните анкету</p>
    <div v-if="form_is_send" class="form-send">Форма отправлена</div>
    <div v-else>
      <el-form
        :model="form"
        label-width="200px"
        label-position="top"
        class="form"
        size="large"
        border
      >
        <el-carousel
          height="70vh"
          :autoplay="false"
          :arrow="'never'"
          indicator-position="none"
          ref="carousel"
          style="display: flex; justify-content: center"
        >
          <el-carousel-item class="quiz-el">
            <div>
              <p>Из каких вопросов вы хотите</p>
              <p>чтобы состояла данная методика?</p>
              <div class="quiz-buttons">
                <el-button
                  type="primary"
                  @click="
                    () => {
                      this.$refs['carousel'].next();
                    }
                  "
                  >Ответить на точные вопросы (85% эффективность , максимальное
                  количество вопросов , от 9 минут) - 1 и КАРТИНКА С ВЫБОРОМ
                </el-button>
                <el-button
                  type="primary"
                  @click="
                    () => {
                      this.$refs['carousel'].next();
                    }
                  "
                  >Ответить на общие вопросы (45% эффективность , минимальное
                  количество вопросов , до 9 минут) - 2 И КАРТИНКА С
                  ВЫБОРОМ</el-button
                >
              </div>
            </div>
          </el-carousel-item>
          <el-carousel-item class="quiz-el">
            <div class="quiz-2">
              <el-form-item
                label="Имеются ли у вас сопутствующие заболевания?"
                label-width="400px"
                class="animate__animated animate__fadeInUp animate__delay-2s"
              >
                <el-radio-group
                  v-model="form.is_have_add_ill"
                  @change="page2_next"
                >
                  <el-radio :label="true" size="large" border>Да</el-radio>
                  <el-radio :label="false" size="large" border>Нет</el-radio>
                </el-radio-group>
              </el-form-item>

              <el-form-item
                label="Принимаете ли вы лекарства?"
                label-width="400px"
                class="animate__animated animate__fadeInUp animate__delay-3s"
              >
                <el-radio-group
                  v-model="form.use_treatments"
                  @change="page2_next"
                >
                  <el-radio :label="true" size="large" border>Да</el-radio>
                  <el-radio :label="false" size="large" border>Нет</el-radio>
                </el-radio-group>
              </el-form-item>

              <el-form-item
                label="Владеете ли вы какой-либо информацией о инсульте?"
                label-width="400px"
                class="animate__animated animate__fadeInUp animate__delay-4s"
              >
                <el-radio-group
                  v-model="form.know_some_information"
                  @change="page2_next"
                >
                  <el-radio :label="true" size="large" border>Да</el-radio>
                  <el-radio :label="false" size="large" border>Нет</el-radio>
                </el-radio-group>
              </el-form-item>

              <el-form-item
                label="Владеете ли вы какой-либо информацией о инсульте пациента?"
                label-width="400px"
                class="animate__animated animate__fadeInUp animate__delay-5s"
              >
                <el-radio-group
                  v-model="form.information_about_patient"
                  @change="page2_next"
                >
                  <el-radio :label="true" size="large" border>Да</el-radio>
                  <el-radio :label="false" size="large" border>Нет</el-radio>
                </el-radio-group>
              </el-form-item>
              <el-button type="primary" @click="page2_prev">← Назад</el-button>
            </div>
          </el-carousel-item>

          <!-- # __________________________________________________________________________ -->

          <el-carousel-item class="quiz-el quiz-3">
            <div class="quiz-2">
              <el-form-item
                label="Была ли у вас уже реабилитация?"
                label-width="400px"
                class="animate__animated animate__fadeInUp animate__delay-2s"
              >
                <el-radio-group
                  v-model="form.reabilitation"
                  @change="page3_next"
                >
                  <el-radio :label="true" size="large" border>Да</el-radio>
                  <el-radio :label="false" size="large" border>Нет</el-radio>
                </el-radio-group>
              </el-form-item>

              <el-form-item
                label="Соблюдаете ли вы диету?"
                label-width="400px"
                class="animate__animated animate__fadeInUp animate__delay-3s"
              >
                <el-radio-group v-model="form.diete" @change="page3_next">
                  <el-radio :label="true" size="large" border>Да</el-radio>
                  <el-radio :label="false" size="large" border>Нет</el-radio>
                </el-radio-group>
              </el-form-item>

              <el-form-item
                label="Использовали ли вы ботулинотерапию?"
                label-width="400px"
                class="animate__animated animate__fadeInUp animate__delay-4s"
              >
                <el-radio-group
                  v-model="form.botuliniteraphy"
                  @change="page3_next"
                >
                  <el-radio :label="true" size="large" border>Да</el-radio>
                  <el-radio :label="false" size="large" border>Нет</el-radio>
                </el-radio-group>
              </el-form-item>

              <el-form-item
                label="Имеется ли у вас депрессия?"
                label-width="400px"
                class="animate__animated animate__fadeInUp animate__delay-5s"
              >
                <el-radio-group v-model="form.depression" @change="page3_next">
                  <el-radio :label="true" size="large" border>Да</el-radio>
                  <el-radio :label="false" size="large" border>Нет</el-radio>
                </el-radio-group>
              </el-form-item>
              <el-button type="primary" @click="page3_prev">← Назад</el-button>
            </div>
          </el-carousel-item>

          <!-- ____________________________________ -->

          <el-carousel-item class="quiz-el quiz-4">
            <el-form-item
              label="Были ли у вас судороги?"
              label-width="400px"
              class="animate__animated animate__fadeInUp animate__delay-2s"
            >
              <el-radio-group v-model="form.sydoragy" @change="page4_next">
                <el-radio :label="true" size="large" border>Да</el-radio>
                <el-radio :label="false" size="large" border>Нет</el-radio>
              </el-radio-group>
            </el-form-item>

            <el-form-item
              label="Нарушена ли у вас терморегуляция"
              label-width="400px"
              class="animate__animated animate__fadeInUp animate__delay-3s"
            >
              <el-radio-group v-model="form.termo" @change="page4_next">
                <el-radio :label="true" size="large" border>Да</el-radio>
                <el-radio :label="false" size="large" border>Нет</el-radio>
              </el-radio-group>
            </el-form-item>

            <el-form-item
              label="Нарушена ли у вас терморегуляция"
              label-width="400px"
              class="animate__animated animate__fadeInUp animate__delay-4s"
            >
              <el-radio-group v-model="form.headache" @change="page4_next">
                <el-radio :label="true" size="large" border>Да</el-radio>
                <el-radio :label="false" size="large" border>Нет</el-radio>
              </el-radio-group>
            </el-form-item>

            <el-button type="primary" @click="page_prev"
              >← Назад</el-button
            ></el-carousel-item
          >

          <!-- ____________________________________ -->

          <el-carousel-item class="quiz-el quiz-5">
            <el-form-item
              label="Имеется ли у вас страх от падений?"
              label-width="400px"
              class="animate__animated animate__fadeInUp animate__delay-2s"
            >
              <el-radio-group v-model="form.fear_of_high" @change="page5_next">
                <el-radio :label="true" size="large" border>Да</el-radio>
                <el-radio :label="false" size="large" border>Нет</el-radio>
              </el-radio-group>
            </el-form-item>

            <el-form-item
              label="Имеется ли у вас боль?"
              label-width="400px"
              class="animate__animated animate__fadeInUp animate__delay-3s"
            >
              <el-radio-group v-model="form.pain" @change="page5_next">
                <el-radio :label="true" size="large" border>Да</el-radio>
                <el-radio :label="false" size="large" border>Нет</el-radio>
              </el-radio-group>
            </el-form-item>

            <el-form-item
              label="В каком месте болит?"
              label-width="400px"
              class="animate__animated animate__fadeInUp animate__delay-0.25s"
              v-if="this.form.pain === true"
            >
              <el-radio-group v-model="form.type_of_pain" @change="page5_next">
                <el-radio label="Поясница" size="small" border
                  >Поясница</el-radio
                >
                <el-radio label="Стопа" size="small" border>Стопа</el-radio>
                <el-radio label="Плечо" size="small" border>Плечо</el-radio>
                <el-radio label="Колено" size="small" border>Колено</el-radio>
                <el-radio label="Бедро" size="small" border>Бедро</el-radio>
              </el-radio-group>
            </el-form-item>

            <el-form-item
              label="Разновидность боли:"
              label-width="400px"
              class="animate__animated animate__fadeInUp animate__delay-0.5s"
              v-if="this.form.pain === true"
            >
              <el-radio-group
                v-model="form.strength_of_pain"
                @change="page5_next"
              >
                <el-radio label="Поясница" size="small" border
                  >Поясница</el-radio
                >
                <el-radio label="Стопа" size="small" border>Стопа</el-radio>
                <el-radio label="Плечо" size="small" border>Плечо</el-radio>
                <el-radio label="Колено" size="small" border>Колено</el-radio>
                <el-radio label="Бедро" size="small" border>Бедро</el-radio>
              </el-radio-group>
            </el-form-item>

            <el-form-item
              label="Опишите свою боль:"
              label-width="400px"
              class="animate__animated animate__fadeInUp animate__delay-0.5s"
              v-if="this.form.pain === true"
            >
              <el-input
                @change="page5_next"
                v-model="form.pain_desc"
                placeholder="Опишите боль"
              />
            </el-form-item>
            <el-button type="primary" @click="page_prev">← Назад</el-button>
          </el-carousel-item>

          <!-- ____________________________________ -->

          <el-carousel-item class="quiz-el quiz-5">
            <el-form-item
              label="Пострадала ли у вас мимика?"
              label-width="400px"
              class="animate__animated animate__fadeInUp animate__delay-2s"
            >
              <el-radio-group v-model="form.mimika" @change="page6_next">
                <el-radio :label="true" size="large" border>Да</el-radio>
                <el-radio :label="false" size="large" border>Нет</el-radio>
              </el-radio-group>
            </el-form-item>

            <el-form-item
              label="Имеется ли у вас спастика?"
              label-width="400px"
              class="animate__animated animate__fadeInUp animate__delay-2s"
            >
              <el-radio-group v-model="form.spastick" @change="page6_next">
                <el-radio :label="true" size="large" border>Да</el-radio>
                <el-radio :label="false" size="large" border>Нет</el-radio>
              </el-radio-group>
            </el-form-item>

            <el-form-item
              label="Имеется ли у вас тонус?"
              label-width="400px"
              class="animate__animated animate__fadeInUp animate__delay-2s"
            >
              <el-radio-group v-model="form.tonus" @change="page6_next">
                <el-radio :label="true" size="large" border>Да</el-radio>
                <el-radio :label="false" size="large" border>Нет</el-radio>
              </el-radio-group>
            </el-form-item>

            <el-button type="primary" @click="page_prev">← Назад</el-button>
          </el-carousel-item>

          <el-carousel-item class="quiz-el quiz-6">
            <el-form-item
              label="Когда вы хотите провести следующий этап?"
              label-width="400px"
              class="animate__animated animate__fadeInUp animate__delay-2s"
            >
              <el-radio-group v-model="form.mess_day" @change="page7_next">
                <el-radio label="Сегодня" size="large" border>Сегодня</el-radio>
                <el-radio label="Завтра" size="large" border>Завтра</el-radio>
              </el-radio-group>
            </el-form-item>

            <el-form-item
              label="Выберете дату"
              label-width="400px"
              class="animate__animated animate__fadeInUp animate__delay-2s"
            >
              <el-date-picker
                @change="page7_next"
                v-model="form.date_of_next"
                type="date"
                placeholder="Выберете дату"
                style="width: 100%"
              />
            </el-form-item>
          </el-carousel-item>
        </el-carousel>
      </el-form>
    </div>
  </div>
</template>

<script>
import { upload_filled } from "@element-plus/icons-vue";
export default {
  name: "FormFirst",
  data() {
    return {
      upload_filled: upload_filled,
      form_is_send: false,
      steps_active: 0,
      form: {
        is_have_add_ill: "",
        use_treatments: "",
        know_some_information: "",
        information_about_patient: "",

        reabilitation: "",
        diete: "",
        botuliniteraphy: "",
        depression: "",

        sydoragy: "",
        termo: "",
        headache: "",

        fear_of_high: "",
        pain: "",
        type_of_pain: "",
        strength_of_pain: "",
        pain_desc: "",

        mimika: "",
        spastick: "",
        tonus: "",

        mess_day: "",
        date_of_next: "",
      },
    };
  },
  methods: {
    page2_prev() {
      this.$refs["carousel"].prev();
    },
    page2_next() {
      if (
        this.form.is_have_add_ill !== "" &&
        this.form.use_treatments !== "" &&
        this.form.know_some_information !== "" &&
        this.form.information_about_patient !== ""
      )
        this.$refs["carousel"].next();
    },

    page3_prev() {
      this.$refs["carousel"].prev();
    },
    page_prev() {
      this.$refs["carousel"].prev();
    },
    page3_next() {
      if (
        this.form.reabilitation !== "" &&
        this.form.diete !== "" &&
        this.form.botuliniteraphy !== "" &&
        this.form.depression !== ""
      )
        this.$refs["carousel"].next();
    },
    page4_next() {
      if (
        this.form.sydoragy !== "" &&
        this.form.termo !== "" &&
        this.form.headache !== ""
      )
        this.$refs["carousel"].next();
    },
    page5_next() {
      if (
        this.form.fear_of_high !== "" &&
        ((this.form.pain == false && this.form.pain != "") ||
          (this.form.type_of_pain !== "" &&
            this.form.strength_of_pain !== "" &&
            this.form.pain_desc !== ""))
      )
        this.$refs["carousel"].next();
    },
    page6_next() {
      if (
        this.form.spastick !== "" &&
        this.form.tonus !== "" &&
        this.form.mimika !== ""
      )
        this.$refs["carousel"].next();
    },

    page7_next() {
      if (this.form.mess_day !== "" && this.form.date_of_next !== "")
        this.form_is_send = true;
    },

    onSubmit: function () {
      //fetch("http://localhost:5600/form_selection", {
      fetch("http://45.91.8.150:5600/form_selection", {
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
          this.form_is_send = true;
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

<style lang="scss">
.steps {
  margin: auto;
  margin-top: 30px;
  margin-bottom: 30px;
}

.quiz-1 {
  p {
    font-size: 4vh;
    margin-top: 30px;
    margin-bottom: 30px;
  }
  .avatar-uploader .avatar {
    width: 70px;
    height: 70px;
    display: block;
  }
}

.quiz-2 {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: center;
}

.quiz-el {
  width: 100vw;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.quiz-buttons {
}

.quiz-first {
  width: 100vw;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.container-form {
  align-items: center;
}

.form {
  position: relative;
  align-self: center;
  align-items: center;
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
  text-align: center;
}
</style>
