<template>
  <div class="container-form">
    <p class="main-par">Заполните анкету</p>
    <div v-if="form_is_send" class="form-send"><ReadyForm /></div>
    <div v-else>
      <el-form
        :model="form"
        label-width="200px"
        label-position="top"
        size="large"
        border
      >
        <el-carousel
          height="70vh"
          :autoplay="false"
          :arrow="'never'"
          indicator-position="none"
          ref="carousel"
        >
          <el-carousel-item class="carousel-wrapper">
            <div class="carousel-el">
              <el-form-item
                label="Укажите свой рост (см)"
                label-width="400px"
                class="animate__animated animate__fadeInUp animate__delay-1s"
              >
                <el-input-number
                  v-model="form.tall"
                  :controls="false"
                  @change="page1"
                  placeholder="ваш рост"
                  size="large"
                />
              </el-form-item>

              <el-form-item
                label="Укажите свой вес (кг)"
                label-width="400px"
                class="animate__animated animate__fadeInUp animate__delay-2s"
              >
                <el-input-number
                  v-model="form.weight"
                  :controls="false"
                  @change="page1"
                  placeholder="ваш вес"
                  size="large"
                />
              </el-form-item>

              <el-form-item
                v-if="is_page_1"
                label="Обхват талии (Ø \ см)"
                label-width="400px"
                class="animate__animated animate__fadeInUp"
              >
                <el-input-number
                  v-model="form.talia"
                  :controls="false"
                  @change="page1"
                  placeholder="ваша талия"
                  size="large"
                  style="margin-right: 30px"
                />
                <el-image
                  style="width: 200px; height: 200px"
                  src="/img/task1/1.jpg"
                  :fit="fit"
                />
              </el-form-item>
              <el-button
                class="animate__animated animate__fadeInUp animate__delay-3s"
                type="primary"
                @click="page_prev"
                >← Назад</el-button
              >
            </div>
          </el-carousel-item>

          <!-- # _____________________________________________________________________________________________________ -->

          <el-carousel-item class="carousel-wrapper">
            <div class="carousel-el">
              <el-form-item
                label="Какая сторона у вас поражена?"
                label-width="400px"
                class="animate__animated animate__fadeInUp animate__delay-1s"
              >
                <el-radio-group v-model="form.side" @change="page2">
                  <el-radio :label="'Левая'" size="large" border
                    >Левая</el-radio
                  >
                  <el-radio :label="'Правая'" size="large" border
                    >Правая</el-radio
                  >

                  <el-radio :label="'Обе'" size="large" border>Обе</el-radio>
                  <el-radio :label="''" size="large" border>Другое</el-radio>
                  <el-input
                    v-if="
                      form.side !== 'Левая' &&
                      form.side !== 'Правая' &&
                      form.side !== 'Обе' &&
                      form.side !== null
                    "
                    @change="page2"
                    v-model="form.side"
                    placeholder="ваша сторона"
                  />
                </el-radio-group>
              </el-form-item>

              <!-- _____________________________________________________________________________________________________ -->

              <el-form-item
                v-if="form.side !== null"
                label="Отличается ли у вас чувствительность ног?"
                label-width="400px"
                class="animate__animated animate__fadeInUp"
              >
                <el-radio-group v-model="form.legs_sensitivity" @change="page2">
                  <el-radio :label="true" size="large" border>Да</el-radio>
                  <el-radio :label="false" size="large" border>Нет</el-radio>
                </el-radio-group>
              </el-form-item>

              <el-form-item
                v-if="form.side !== null"
                label="Отличается ли у вас чувствительность рук?"
                label-width="400px"
                class="animate__animated animate__fadeInUp"
              >
                <el-radio-group v-model="form.arms_sensitivity" @change="page2">
                  <el-radio :label="true" size="large" border>Да</el-radio>
                  <el-radio :label="false" size="large" border>Нет</el-radio>
                </el-radio-group>
              </el-form-item>

              <el-image
                v-if="form.side !== null"
                class="animate__animated animate__fadeInUp"
                style="width: 150px; height: 150px"
                src="/img/task1/1.jpg"
                :fit="fit"
              />

              <el-button
                class="animate__animated animate__fadeInUp animate__delay-3s"
                type="primary"
                @click="page_prev"
                >← Назад</el-button
              >
            </div>
          </el-carousel-item>

          <el-carousel-item class="carousel-wrapper">
            <div class="carousel-el">
              <p>Вехняя часть руки</p>
              <el-form-item
                label="Правая сторона (Ø \ см)"
                label-width="400px"
                class="animate__animated animate__fadeInUp animate__delay-1s"
              >
                <el-input-number
                  v-model="form.right_arm"
                  :controls="false"
                  @change="page3"
                  placeholder="Правая сторона"
                  size="large"
                />
              </el-form-item>
              <el-form-item
                label="Левая сторона (Ø \ см):"
                label-width="400px"
                class="animate__animated animate__fadeInUp animate__delay-2s"
              >
                <el-input-number
                  v-model="form.left_arm"
                  :controls="false"
                  @change="page3"
                  placeholder="Левая сторона"
                  size="large"
                />
              </el-form-item>

              <el-image
                class="animate__animated animate__fadeInUp animate__delay-2s"
                style="width: 150px; height: 150px"
                src="/img/task1/1.jpg"
                :fit="fit"
              />

              <el-button
                class="animate__animated animate__fadeInUp animate__delay-3s"
                type="primary"
                @click="page_prev"
                >← Назад</el-button
              >
            </div>
          </el-carousel-item>

          <!-- ______________________________________________________________________-- -->

          <el-carousel-item class="carousel-wrapper">
            <div class="carousel-el">
              <p>Нижняя часть руки</p>
              <el-form-item
                label="Правая сторона (Ø \ см)"
                label-width="400px"
                class="animate__animated animate__fadeInUp animate__delay-1s"
              >
                <el-input-number
                  v-model="form.bot_right_arm"
                  :controls="false"
                  @change="page4"
                  placeholder="Правая сторона"
                  size="large"
                />
              </el-form-item>
              <el-form-item
                label="Левая сторона (Ø \ см):"
                label-width="400px"
                class="animate__animated animate__fadeInUp animate__delay-2s"
              >
                <el-input-number
                  v-model="form.bot_left_arm"
                  :controls="false"
                  @change="page4"
                  placeholder="Левая сторона"
                  size="large"
                />
              </el-form-item>

              <el-form-item
                v-if="form.bot_right_arm != null && form.bot_left_arm != null"
                label="Имеются ли у вас вены на поврежденной руке? "
                label-width="400px"
                class="animate__animated animate__fadeInUp"
              >
                <el-radio-group v-model="form.vien_bot_arm" @change="page4">
                  <el-radio :label="true" size="large" border>Да</el-radio>
                  <el-radio :label="false" size="large" border>Нет</el-radio>
                </el-radio-group>
              </el-form-item>

              <el-image
                v-if="form.bot_right_arm != null && form.bot_left_arm != null"
                class="animate__animated animate__fadeInUp"
                style="width: 150px; height: 150px"
                src="/img/task1/1.jpg"
                :fit="fit"
              />

              <el-button
                class="animate__animated animate__fadeInUp animate__delay-3s"
                type="primary"
                @click="page_prev"
                >← Назад</el-button
              >
            </div>
          </el-carousel-item>

          <!-- ______________________________________________________________________-- -->

          <el-carousel-item class="carousel-wrapper">
            <div class="carousel-el">
              <p>Верхняя часть ноги</p>
              <el-form-item
                label="Правая сторона (Ø \ см)"
                label-width="400px"
                class="animate__animated animate__fadeInUp animate__delay-1s"
              >
                <el-input-number
                  v-model="form.right_leg"
                  :controls="false"
                  @change="page5"
                  placeholder="Правая сторона"
                  size="large"
                />
              </el-form-item>
              <el-form-item
                label="Левая сторона (Ø \ см):"
                label-width="400px"
                class="animate__animated animate__fadeInUp animate__delay-2s"
              >
                <el-input-number
                  v-model="form.left_leg"
                  :controls="false"
                  @change="page5"
                  placeholder="Левая сторона"
                  size="large"
                />
              </el-form-item>

              <el-image
                class="animate__animated animate__fadeInUp animate__delay-2s"
                style="width: 150px; height: 150px"
                src="/img/task1/1.jpg"
                :fit="fit"
              />

              <el-button
                class="animate__animated animate__fadeInUp animate__delay-3s"
                type="primary"
                @click="page_prev"
                >← Назад</el-button
              >
            </div>
          </el-carousel-item>

          <!-- ______________________________________________________________________-- -->

          <el-carousel-item class="carousel-wrapper">
            <div class="carousel-el">
              <p>Нижняя часть ноги</p>
              <el-form-item
                label="Правая сторона (Ø \ см)"
                label-width="400px"
                class="animate__animated animate__fadeInUp animate__delay-1s"
              >
                <el-input-number
                  v-model="form.bot_right_leg"
                  :controls="false"
                  @change="page6"
                  placeholder="Правая сторона"
                  size="large"
                />
              </el-form-item>
              <el-form-item
                label="Левая сторона (Ø \ см):"
                label-width="400px"
                class="animate__animated animate__fadeInUp animate__delay-2s"
              >
                <el-input-number
                  v-model="form.bot_left_leg"
                  :controls="false"
                  @change="page6"
                  placeholder="Левая сторона"
                  size="large"
                />
              </el-form-item>

              <el-form-item
                v-if="form.bot_right_leg != null && form.bot_left_leg != null"
                label="Имеются ли у вас вены на поврежденной руке? "
                label-width="400px"
                class="animate__animated animate__fadeInUp"
              >
                <el-radio-group v-model="form.vien_bot_leg" @change="page6">
                  <el-radio :label="true" size="large" border>Да</el-radio>
                  <el-radio :label="false" size="large" border>Нет</el-radio>
                </el-radio-group>
              </el-form-item>

              <el-image
                v-if="form.bot_right_leg != null && form.bot_left_leg != null"
                class="animate__animated animate__fadeInUp"
                style="width: 150px; height: 150px"
                src="/img/task1/1.jpg"
                :fit="fit"
              />

              <el-button
                class="animate__animated animate__fadeInUp animate__delay-3s"
                type="primary"
                @click="page_prev"
                >← Назад</el-button
              >
            </div>
          </el-carousel-item>
        </el-carousel>
      </el-form>
    </div>
  </div>
</template>

<script>
import ReadyForm from "@/components/form_is_send.vue";
export default {
  name: "FormFirst",
  components: { ReadyForm },
  data() {
    return {
      form_is_send: false,
      is_page_1: false,
      form: {
        tall: null,
        weight: null,
        talia: null,

        side: null,
        legs_sensitivity: null,
        arms_sensitivity: null,

        right_arm: null,
        left_arm: null,

        bot_right_arm: null,
        bot_left_arm: null,
        vien_bot_arm: null,

        right_leg: null,
        left_leg: null,

        bot_right_leg: null,
        bot_left_leg: null,
        vien_bot_leg: null,
      },
    };
  },
  methods: {
    page1() {
      if (this.form.tail !== null && this.form.weight !== null) {
        if (this.form.talia !== null) this.$refs["carousel"].next();
        else this.is_page_1 = true;
      }
    },

    page2() {
      if (
        this.form.side !== null &&
        this.form.legs_sensitivity !== null &&
        this.form.arms_sensitivity !== null
      ) {
        this.$refs["carousel"].next();
      }
    },

    page3() {
      if (this.form.right_arm !== null && this.form.left_arm !== null) {
        this.$refs["carousel"].next();
      }
    },

    page4() {
      if (
        this.form.bot_right_arm !== null &&
        this.form.bot_left_arm !== null &&
        this.form.vien_bot_arm !== null
      ) {
        this.$refs["carousel"].next();
      }
    },

    page5() {
      if (this.form.right_leg !== null && this.form.left_leg !== null) {
        this.$refs["carousel"].next();
      }
    },

    page6() {
      if (
        this.form.bot_right_leg !== null &&
        this.form.bot_left_leg !== null &&
        this.form.vien_bot_leg !== null
      ) {
        this.form_is_send = true;
      }
    },

    page_prev() {
      this.$refs["carousel"].prev();
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
.carousel-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;

  .carousel-el {
    width: 70vw;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
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
