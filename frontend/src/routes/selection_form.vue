<template>
  <div class="container-form">
    <p class="main-par">Заполните анкету</p>
    <div v-if="form_is_send" class="form-send">Форма отправлена</div>
    <div v-else>
      <el-form
        :model="form"
        label-width="200px"
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
        >
          <el-carousel-item class="quiz-el quiz-1">
            <p>Введите свои личные данные</p>
            <el-form-item
              prop="email"
              label="Эл почта"
              :rules="[
                {
                  required: true,
                  message: 'Пожалуйста введите почту',
                  trigger: 'blur',
                },
                {
                  type: 'email',
                  message: 'Укажите верную почту',
                  trigger: ['blur', 'change'],
                },
              ]"
              :validate="() => {}"
            >
              <el-input
                v-model="form.email"
                :blur="page1"
                placeholder="Ваша почта"
              />
            </el-form-item>
            <el-form-item
              label="Имя"
              prop="name"
              :rules="[
                {
                  required: true,
                  message: 'Пожалуйста укажите имя',
                  trigger: 'blur',
                },
              ]"
              :validate="() => {}"
            >
              <el-input v-model="form.name" placeholder="Имя" />
            </el-form-item>
            <el-form-item label="Фамилия">
              <el-input v-model="form.last_name" placeholder="Фамилия" />
            </el-form-item>
            <el-form-item
              label="Дата Рождения"
              prop="date_of_birth"
              :rules="[
                {
                  required: true,
                  message: 'Укажите дату',
                  trigger: 'blur',
                },
              ]"
              :validate="() => {}"
            >
              <el-date-picker
                v-model="form.date_of_birth"
                type="date"
                placeholder="Выберете дату"
                style="width: 100%"
              />
            </el-form-item>

            <el-form-item label="Фото:">
              <el-upload
                class="avatar-uploader"
                action="https://run.mocky.io/v3/9d059bf9-4660-45f2-925d-ce80ad6c4d15"
                :show-file-list="false"
                :on-success="handleAvatarSuccess"
                :before-upload="beforeAvatarUpload"
              >
                <img src="/img/user.png" class="avatar" />
              </el-upload>
            </el-form-item>

            <el-button type="primary" @click="page1">Дальше →</el-button>
          </el-carousel-item>
          <el-carousel-item class="quiz-el quiz-2">
            <el-form-item
              label="Телефон"
              prop="phone"
              :rules="[
                {
                  required: true,
                  message: 'Укажите телефон',
                  trigger: 'blur',
                },
              ]"
              :validate="() => {}"
            >
              <el-input v-model="form.phone" placeholder="Телефон" />
            </el-form-item>
            <el-form-item
              label="Страна"
              style="margin-bottom: 1px"
              prop="region"
              :rules="[
                {
                  required: true,
                  message: 'Выберите страну',
                  trigger: 'blur',
                },
              ]"
              :validate="() => {}"
            >
              <el-select v-model="form.region" placeholder="Выберете страну">
                <el-option label="США" value="США" />
                <el-option label="Россия" value="Россия" />
              </el-select>
            </el-form-item>

            <el-form-item
              label="Город"
              v-if="form.region"
              style="margin-bottom: 1px"
              prop="region"
              :rules="[
                {
                  required: true,
                  message: 'Выберите город',
                  trigger: 'blur',
                },
              ]"
              :validate="() => {}"
            >
              <el-select v-model="form.city" placeholder="Выберете город">
                <el-option label="Москва" value="Москва" />
                <el-option label="Вашингтон" value="Вашингтон" />
              </el-select>
            </el-form-item>
            <el-form-item v-if="form.city != ''">
              <div style="text-align: left">
                <p style="margin-bottom: 0; line-height: 20px; font-size: 10px">
                  Часовой пояс выбран
                </p>
              </div>
            </el-form-item>
            <el-form-item
              label="Укажите пол"
              prop="gender"
              :rules="[
                {
                  required: true,
                  message: 'Укажите пол',
                  trigger: 'blur',
                },
              ]"
              :validate="() => {}"
            >
              <el-radio-group v-model="form.gender">
                <el-radio label="Мужской" size="large" border>Мужской</el-radio>
                <el-radio label="Женский" size="large" border>Женский</el-radio>
                <el-radio label="Другое" size="large" border>Другое</el-radio>
              </el-radio-group>
            </el-form-item>
            <div class="quiz-buttons">
              <el-button type="primary" @click="page2_prev">← Назад</el-button>
              <el-button type="primary" @click="page2_next">Дальше →</el-button>
            </div>
          </el-carousel-item>
          <el-carousel-item class="quiz-el">
            <el-form-item
              label="У вас был инсульт ?"
              prop="stroke"
              :rules="[
                {
                  required: true,
                  message: 'Ответьте на вопрос',
                  trigger: 'blur',
                },
              ]"
              :validate="() => {}"
            >
              <el-radio-group v-model="form.stroke">
                <el-radio :label="true" size="large" border>Да</el-radio>
                <el-radio :label="false" size="large" border>Нет</el-radio>
              </el-radio-group>
            </el-form-item>
            <div v-if="form.stroke == false">
              <el-form-item>
                <p>Опишите вашу проблему</p>
              </el-form-item>
              <el-form-item
                ><el-input
                  v-model="form.problem_no_stroke"
                  autosize
                  type="textarea"
                  placeholder="Please input"
                />
              </el-form-item>
            </div>
            <div v-else-if="form.stroke == true">
              <el-form-item label="Вид инсульта">
                <el-radio-group v-model="form.type_of_stroke">
                  <el-radio label="Ишемический" size="large" border
                    >Ишемический</el-radio
                  >
                  <el-radio label="Геморрагический" size="large" border
                    >Геморрагический</el-radio
                  >
                  <el-radio label="Другое" size="large" border>Другое</el-radio>
                </el-radio-group>
              </el-form-item>

              <el-form-item> Когда у вас произошёл инсульт? </el-form-item>
              <el-form-item label="Дата">
                <div style="display: flex; flex-direction: row">
                  <el-date-picker
                    v-model="form.date_of_stroke"
                    type="date"
                    placeholder="Выберете дату"
                    style="width: 100%"
                  />
                  <el-radio-group
                    v-model="form.date_of_stroke"
                    style="padding-left: 20px"
                  >
                    <el-radio label="none" size="large" border
                      >Не знаю</el-radio
                    >
                  </el-radio-group>
                </div>

                <el-form-item
                  >Как пациент воспринимает какую-либо информацию?</el-form-item
                >
                <el-form-item label="Уровень">
                  <el-select
                    v-model="form.percent_of_information"
                    placeholder="Укажите уровень"
                  >
                    <el-option label="10%" value="10%" />
                    <el-option label="20%" value="20%" />
                    <el-option label="30%" value="30%" />
                    <el-option label="40%" value="40%" />
                    <el-option label="50%" value="50%" />
                    <el-option label="60%" value="60%" />
                    <el-option label="70%" value="70%" />
                    <el-option label="80%" value="80%" />
                    <el-option label="90%" value="90%" />
                    <el-option label="100%" value="100%" />
                  </el-select>
                </el-form-item>
              </el-form-item>
            </div>
            <div class="quiz-buttons">
              <el-button type="primary" @click="page3_prev">← Назад</el-button>
              <el-button type="primary" @click="page3_next">Дальше →</el-button>
            </div>
          </el-carousel-item>
          <el-carousel-item class="quiz-el">
            <el-form-item
              >Имеется ли у вас движения на поражённой ноге?</el-form-item
            >
            <el-form-item label="">
              <el-radio-group v-model="form.is_injured_leg_movemented">
                <el-radio :label="true" size="large" border>Да</el-radio>
                <el-radio :label="false" size="large" border>Нет</el-radio>
              </el-radio-group>
            </el-form-item>

            <div v-if="form.is_injured_leg_movemented">
              <el-form-item>На сколько % она работает?</el-form-item>
              <el-form-item label="Укажите %">
                <el-select
                  v-model="form.percent_of_injured_leg_movemented"
                  placeholder="Укажите уровень"
                >
                  <el-option label="10%" value="10%" />
                  <el-option label="20%" value="20%" />
                  <el-option label="30%" value="30%" />
                  <el-option label="40%" value="40%" />
                  <el-option label="50%" value="50%" />
                  <el-option label="60%" value="60%" />
                  <el-option label="70%" value="70%" />
                  <el-option label="80%" value="80%" />
                  <el-option label="90%" value="90%" />
                  <el-option label="100%" value="100%" />
                </el-select>
              </el-form-item>

              <el-form-item
                >Имеется ли у вас движения в голеностопе?</el-form-item
              >
              <el-form-item label="">
                <el-radio-group v-model="form.is_injured_ankle_movemented">
                  <el-radio :label="true" size="large" border>Да</el-radio>
                  <el-radio :label="false" size="large" border>Нет</el-radio>
                </el-radio-group>
              </el-form-item>

              <el-form-item
                >Может ли пациент сидеть без опоры под спину?</el-form-item
              >
              <el-form-item label="">
                <el-radio-group v-model="form.is_can_sit">
                  <el-radio :label="true" size="large" border>Да</el-radio>
                  <el-radio :label="false" size="large" border>Нет</el-radio>
                </el-radio-group>
              </el-form-item>
            </div>
            <div class="quiz-buttons">
              <el-button type="primary" @click="page4_prev">← Назад</el-button>
              <el-button type="primary" @click="page4_next">Дальше →</el-button>
            </div>
          </el-carousel-item>

          <el-carousel-item
            class="quiz-el"
            v-if="form.is_injured_leg_movemented"
          >
            <el-form-item>Может ли пациент самостоятельно стоять?</el-form-item>
            <el-form-item label="">
              <el-radio-group v-model="form.is_can_state">
                <el-radio :label="true" size="large" border>Да</el-radio>
                <el-radio :label="false" size="large" border>Нет</el-radio>
              </el-radio-group>
            </el-form-item>

            <el-form-item>Может ли пациент ходить с опорой?</el-form-item>
            <el-form-item label="">
              <el-radio-group v-model="form.is_patient_walk_with_supports">
                <el-radio :label="true" size="large" border>Да</el-radio>
                <el-radio :label="false" size="large" border>Нет</el-radio>
              </el-radio-group>
            </el-form-item>

            <el-form-item>Сгибается ли нога в колленом суставе?</el-form-item>
            <el-form-item label="">
              <el-radio-group v-model="form.is_knee_bend">
                <el-radio :label="true" size="large" border>Да</el-radio>
                <el-radio :label="false" size="large" border>Нет</el-radio>
              </el-radio-group>
            </el-form-item>

            <el-form-item>Разгибается ли нога в колленом суставе?</el-form-item>
            <el-form-item label="">
              <el-radio-group v-model="form.is_knee_unbend">
                <el-radio :label="true" size="large" border>Да</el-radio>
                <el-radio :label="false" size="large" border>Нет</el-radio>
              </el-radio-group>
            </el-form-item>
            <div class="quiz-buttons">
              <el-button type="primary" @click="page5_prev">← Назад</el-button>
              <el-button type="primary" @click="page5_next">Дальше →</el-button>
            </div>
          </el-carousel-item>

          <el-carousel-item
            class="quiz-el"
            v-if="form.is_injured_leg_movemented"
          >
            <el-form-item>Загрузите видео вашей ходьбы</el-form-item>
            <el-form-item
              ><el-upload
                class="upload-demo"
                drag
                action="https://run.mocky.io/v3/9d059bf9-4660-45f2-925d-ce80ad6c4d15"
                multiple
              >
                <el-icon class="el-icon--upload"><upload-filled /></el-icon>
                <div class="el-upload__text">
                  Drop file here or <em>click to upload</em>
                </div>
              </el-upload></el-form-item
            >
            <div class="quiz-buttons">
              <el-button type="primary" @click="page6_prev">← Назад</el-button>
              <el-button type="primary" @click="page6_next">Дальше →</el-button>
            </div>
          </el-carousel-item>

          <el-carousel-item class="quiz-el">
            <el-form-item
              >Имеются ли у вас движения на поражённой руке?</el-form-item
            >
            <el-form-item label="">
              <el-radio-group v-model="form.is_injured_arm_movemented">
                <el-radio :label="true" size="large" border>Да</el-radio>
                <el-radio :label="false" size="large" border>Нет</el-radio>
              </el-radio-group>
            </el-form-item>

            <div v-if="form.is_injured_arm_movemented">
              <el-form-item>На сколько % она работает?</el-form-item>
              <el-form-item label="Уровень">
                <el-select
                  v-model="form.percent_of_injured_arm_movemented"
                  placeholder="Укажите уровень"
                >
                  <el-option label="10%" value="10%" />
                  <el-option label="20%" value="20%" />
                  <el-option label="30%" value="30%" />
                  <el-option label="40%" value="40%" />
                  <el-option label="50%" value="50%" />
                  <el-option label="60%" value="60%" />
                  <el-option label="70%" value="70%" />
                  <el-option label="80%" value="80%" />
                  <el-option label="90%" value="90%" />
                  <el-option label="100%" value="100%" />
                </el-select>
              </el-form-item>

              <el-form-item>Сгибается ли рука в локтевом суставе?</el-form-item>
              <el-form-item label="">
                <el-radio-group v-model="form.is_elbow_bend">
                  <el-radio :label="true" size="large" border>Да</el-radio>
                  <el-radio :label="false" size="large" border>Нет</el-radio>
                </el-radio-group>
              </el-form-item>

              <el-form-item
                >Разгибается ли рука в локтевом суставе?</el-form-item
              >
              <el-form-item label="">
                <el-radio-group v-model="form.is_elbow_unbend">
                  <el-radio :label="true" size="large" border>Да</el-radio>
                  <el-radio :label="false" size="large" border>Нет</el-radio>
                </el-radio-group>
              </el-form-item>
            </div>

            <div class="quiz-buttons">
              <el-button type="primary" @click="page7_prev">← Назад</el-button>
              <el-button type="primary" @click="page7_next">Дальше →</el-button>
            </div>
          </el-carousel-item>

          <el-carousel-item v-if="form.is_injured_arm_movemented">
            <el-form-item>Сгибается ли рука в предплечье?</el-form-item>
            <el-form-item label="">
              <el-radio-group v-model="form.is_forearm_bend">
                <el-radio :label="true" size="large" border>Да</el-radio>
                <el-radio :label="false" size="large" border>Нет</el-radio>
              </el-radio-group>
            </el-form-item>

            <el-form-item>Разгибается ли рука в предплечье?</el-form-item>
            <el-form-item label="">
              <el-radio-group v-model="form.is_forearm_unbend">
                <el-radio :label="true" size="large" border>Да</el-radio>
                <el-radio :label="false" size="large" border>Нет</el-radio>
              </el-radio-group>
            </el-form-item>

            <el-form-item
              >Имеются ли у вас движения в пальцах на руке?</el-form-item
            >
            <el-form-item label="">
              <el-radio-group v-model="form.is_injured_finger_movemented">
                <el-radio :label="true" size="large" border>Да</el-radio>
                <el-radio :label="false" size="large" border>Нет</el-radio>
              </el-radio-group>
            </el-form-item>

            <div class="quiz-buttons">
              <el-button type="primary" @click="page8_prev">← Назад</el-button>
              <el-button type="primary" @click="page8_next">Дальше →</el-button>
            </div>
          </el-carousel-item>

          <el-carousel-item
            class="quiz-el"
            v-if="form.is_injured_arm_movemented"
          >
            <el-form-item>Загрузите видео вашх рук</el-form-item>
            <el-form-item
              ><el-upload
                class="upload-demo"
                drag
                action="https://run.mocky.io/v3/9d059bf9-4660-45f2-925d-ce80ad6c4d15"
                multiple
              >
                <el-icon class="el-icon--upload"><upload-filled /></el-icon>
                <div class="el-upload__text">
                  Drop file here or <em>click to upload</em>
                </div>
              </el-upload></el-form-item
            >
            <div class="quiz-buttons">
              <el-button type="primary" @click="page9_prev">← Назад</el-button>
              <el-button type="primary" @click="page9_next">Дальше →</el-button>
            </div>
          </el-carousel-item>

          <el-carousel-item class="quiz-el">
            <el-form-item
              >В каком году вы планируете восстанавливаться?</el-form-item
            >
            <el-form-item label="" style="margin-bottom: 1px">
              <el-radio-group v-model="form.now_year_to_repair">
                <el-radio label="now" size="large" border>В этом</el-radio>
                <el-radio label="later" size="large" border
                  >В последующих</el-radio
                >
              </el-radio-group>
            </el-form-item>
            <el-form-item v-if="form.now_year_to_repair == 'later'">
              <div style="text-align: left">
                <p style="margin-bottom: 0; line-height: 20px; font-size: 11px">
                  Напоминание: чем дольше времени проходит с момента инсульта ,
                  тем сложнее реабилитация
                </p>
              </div>
            </el-form-item>

            <el-form-item>Где вы собираетесь восстанавливаться?</el-form-item>
            <el-form-item label="">
              <el-radio-group v-model="form.where_to_repair">
                <el-radio label="outside" size="large" border
                  >За пределами страны
                </el-radio>
                <el-radio label="in_my_country" size="large" border
                  >В моей стране</el-radio
                >
                <el-radio label="home" size="large" border>На дому</el-radio>
              </el-radio-group>
            </el-form-item>

            <div class="quiz-buttons">
              <el-button type="primary" @click="page10_prev">← Назад</el-button>
              <el-button type="primary" @click="page10_next"
                >Отправить запрос</el-button
              >
            </div>
          </el-carousel-item>
        </el-carousel>
      </el-form>
      <!-- <div style="width: 100%; height: 500px"></div> -->
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
        email: "",
        name: "",
        last_name: "",
        date_of_birth: "",
        gender: "",
        region: "",
        city: "",
        phone: "",
        stroke: null,
        problem_no_stroke: "",
        type_of_stroke: "",
        date_of_stroke: "",
        know_reason: "",
        percent_of_information: "",
        is_injured_leg_movemented: "",
        percent_of_injured_leg_movemented: "",
        is_injured_ankle_movemented: "",
        is_can_sit: "",
        is_can_state: "",
        is_patient_walk_with_supports: "",
        is_knee_bend: "",
        is_knee_unbend: "",
        is_injured_arm_movemented: "",
        percent_of_injured_arm_movemented: "",
        is_elbow_bend: "",
        is_elbow_unbend: "",
        is_forearm_bend: "",
        is_forearm_unbend: "",
        is_injured_finger_movemented: "",
        now_year_to_repair: "",
        where_to_repair: "",
      },
    };
  },
  methods: {
    page1() {
      // console.log(ev);
      this.$refs["carousel"].next();
    },
    page2_prev() {
      this.$refs["carousel"].prev();
    },
    page2_next() {
      this.steps_active += 1;
      this.$refs["carousel"].next();
    },

    page3_prev() {
      this.steps_active -= 1;
      this.$refs["carousel"].prev();
    },
    page3_next() {
      if (this.form.stroke) {
        this.steps_active += 1;
        this.$refs["carousel"].next();
      } else this.onSubmit();
    },
    page4_prev() {
      this.steps_active -= 1;
      this.$refs["carousel"].prev();
    },
    page4_next() {
      this.steps_active += 1;
      this.$refs["carousel"].next();
    },

    page5_prev() {
      this.$refs["carousel"].prev();
    },
    page5_next() {
      this.$refs["carousel"].next();
    },
    page6_prev() {
      this.$refs["carousel"].prev();
    },
    page6_next() {
      this.steps_active += 1;
      this.$refs["carousel"].next();
    },

    page7_prev() {
      this.steps_active -= 1;
      this.$refs["carousel"].prev();
    },
    page7_next() {
      this.$refs["carousel"].next();
    },

    page8_prev() {
      this.$refs["carousel"].prev();
    },
    page8_next() {
      this.$refs["carousel"].next();
    },

    page9_prev() {
      this.$refs["carousel"].prev();
    },
    page9_next() {
      this.$refs["carousel"].next();
    },

    page10_prev() {
      this.$refs["carousel"].prev();
    },
    page10_next() {
      this.$refs["carousel"].next();
      this.onSubmit();
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

.quiz-el {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.quiz-buttons {
  display: flex;
  flex-direction: row;
}

.container-form {
  align-items: center;
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
  text-align: center;
}
</style>
