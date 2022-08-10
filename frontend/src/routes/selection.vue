<template>
  <div class="container-form">
    <p class="main-par">Заполните анкету</p>
    <div v-if="form_send_status == 1" class="form-w8"><div>Ждите...</div></div>
    <div v-else-if="form_send_status == 2" class="form-send">
      <div class="form-send-container">
        <ReadyForm />
        <p style="margin-bottom: 40px">Ваш пароль: {{ out_password }}</p>
      </div>
    </div>
    <div v-else>
      <el-form
        :model="form"
        label-width="400px"
        label-position="top"
        class="form"
        size="large"
        border
      >
        <el-carousel
          height="80vh"
          :autoplay="false"
          :arrow="'never'"
          indicator-position="none"
          ref="carousel"
        >
          <el-carousel-item class="carousel-wrapper">
            <div class="quiz-el quiz-1">
              <div>
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
                    @change="page1"
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
                  <el-input
                    v-model="form.name"
                    placeholder="Имя"
                    @change="page1"
                  />
                </el-form-item>
                <el-form-item label="Фамилия">
                  <el-input
                    v-model="form.last_name"
                    placeholder="Фамилия"
                    @change="page1"
                  />
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
                    @change="page1"
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
                    :on-success="() => {}"
                    :before-upload="
                      () => {
                        upload_success.page1_avatar = true;
                        page1();
                      }
                    "
                  >
                    <img src="/img/user.png" class="avatar" />
                  </el-upload>
                </el-form-item>
              </div>
            </div>
          </el-carousel-item>

          <!-- _____________________________________________________________ -->

          <el-carousel-item class="carousel-wrapper">
            <div class="quiz-el quiz-2">
              <div>
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
                  <el-input
                    v-model="form.phone"
                    placeholder="Телефон"
                    @change="page2"
                  />
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
                  <el-select
                    @change="page2"
                    v-model="form.region"
                    placeholder="Выберете страну"
                  >
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
                  <el-select
                    v-model="form.city"
                    placeholder="Выберете город"
                    @change="page2"
                  >
                    <el-option label="Москва" value="Москва" />
                    <el-option label="Вашингтон" value="Вашингтон" />
                  </el-select>
                </el-form-item>

                <el-form-item v-if="form.city != null">
                  <div style="text-align: left">
                    <p
                      style="
                        margin-bottom: 0;
                        line-height: 20px;
                        font-size: 10px;
                      "
                    >
                      Часовой пояс выбран
                    </p>
                  </div>
                </el-form-item>
                <el-form-item
                  style="margin-top: 20px"
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
                  <el-radio-group v-model="form.gender" @change="page2">
                    <el-radio label="Мужской" size="large" border
                      >Мужской</el-radio
                    >
                    <el-radio label="Женский" size="large" border
                      >Женский</el-radio
                    >
                    <el-radio label="Другое" size="large" border
                      >Другое</el-radio
                    >
                  </el-radio-group>
                </el-form-item>

                <div class="quiz-buttons">
                  <el-button type="primary" @click="prev">← Назад</el-button>
                </div>
              </div>
            </div>
          </el-carousel-item>

          <!-- _____________________________________________________________ -->

          <el-carousel-item class="carousel-wrapper">
            <div class="quiz-el">
              <div>
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
                  <el-radio-group v-model="form.stroke" @change="page3">
                    <el-radio :label="true" size="large" border>Да</el-radio>
                    <el-radio :label="false" size="large" border>Нет</el-radio>
                  </el-radio-group>
                </el-form-item>

                <div v-if="form.stroke == false">
                  <el-form-item
                    ><el-input
                      @change="page3"
                      label="Опишите вашу проблему"
                      v-model="form.problem_no_stroke"
                      autosize
                      type="textarea"
                      placeholder="Опишите проблему"
                    />
                  </el-form-item>
                </div>

                <div v-else-if="form.stroke == true">
                  <el-form-item label="Вид инсульта">
                    <el-radio-group
                      v-model="form.type_of_stroke"
                      @change="page3"
                    >
                      <el-radio label="Ишемический" size="large" border
                        >Ишемический</el-radio
                      >
                      <el-radio label="Геморрагический" size="large" border
                        >Геморрагический</el-radio
                      >
                      <el-radio label="Другое" size="large" border
                        >Другое</el-radio
                      >
                    </el-radio-group>
                  </el-form-item>

                  <el-form-item label="Когда у вас произошёл инсульт?">
                    <div style="display: flex; flex-direction: row">
                      <el-date-picker
                        v-model="form.date_of_stroke"
                        @change="page3"
                        type="date"
                        placeholder="Выберете дату"
                        style="width: 100%"
                      />
                      <el-radio-group
                        v-model="form.date_of_stroke"
                        style="padding-left: 20px"
                        @change="page3"
                      >
                        <el-radio label="none" size="large" border
                          >Не знаю</el-radio
                        >
                      </el-radio-group>
                    </div>
                  </el-form-item>

                  <el-form-item
                    label="Как пациент воспринимает какую-либо
                      информацию?"
                  >
                    <el-select
                      @change="page3"
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
                </div>
                <div class="quiz-buttons">
                  <el-button type="primary" @click="prev">← Назад</el-button>
                </div>
              </div>
            </div>
          </el-carousel-item>

          <!-- _____________________________________________________________ -->

          <el-carousel-item class="carousel-wrapper">
            <div class="quiz-el">
              <div>
                <el-form-item
                  label="Имеется ли у вас движения на поражённой ноге?"
                >
                  <el-radio-group
                    v-model="form.is_injured_leg_movemented"
                    @change="page4"
                  >
                    <el-radio :label="true" size="large" border>Да</el-radio>
                    <el-radio :label="false" size="large" border>Нет</el-radio>
                  </el-radio-group>
                </el-form-item>

                <div v-if="form.is_injured_leg_movemented">
                  <el-form-item label="На сколько % она работает?">
                    <el-select
                      @change="page4"
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
                    label="Имеется ли у вас движения в голеностопе?"
                  >
                    <el-radio-group
                      v-model="form.is_injured_ankle_movemented"
                      @change="page4"
                    >
                      <el-radio :label="true" size="large" border>Да</el-radio>
                      <el-radio :label="false" size="large" border
                        >Нет</el-radio
                      >
                    </el-radio-group>
                  </el-form-item>

                  <el-form-item
                    label="Может ли пациент сидеть без опоры под спину?"
                  >
                    <el-radio-group v-model="form.is_can_sit" @change="page4">
                      <el-radio :label="true" size="large" border>Да</el-radio>
                      <el-radio :label="false" size="large" border
                        >Нет</el-radio
                      >
                    </el-radio-group>
                  </el-form-item>
                </div>
                <div class="quiz-buttons">
                  <el-button type="primary" @click="prev">← Назад</el-button>
                </div>
              </div>
            </div>
          </el-carousel-item>

          <!-- _____________________________________________________________ -->

          <el-carousel-item class="carousel-wrapper">
            <div class="quiz-el">
              <div v-if="form.is_injured_leg_movemented === true">
                <el-form-item label="Может ли пациент самостоятельно стоять?">
                  <el-radio-group v-model="form.is_can_state" @change="page5">
                    <el-radio :label="true" size="large" border>Да</el-radio>
                    <el-radio :label="false" size="large" border>Нет</el-radio>
                  </el-radio-group>
                </el-form-item>

                <el-form-item label="Может ли пациент ходить с опорой?">
                  <el-radio-group
                    v-model="form.is_patient_walk_with_supports"
                    @change="page5"
                  >
                    <el-radio :label="true" size="large" border>Да</el-radio>
                    <el-radio :label="false" size="large" border>Нет</el-radio>
                  </el-radio-group>
                </el-form-item>

                <el-form-item label="Сгибается ли нога в колленом суставе?">
                  <el-radio-group v-model="form.is_knee_bend" @change="page5">
                    <el-radio :label="true" size="large" border>Да</el-radio>
                    <el-radio :label="false" size="large" border>Нет</el-radio>
                  </el-radio-group>
                </el-form-item>

                <el-form-item label="Разгибается ли нога в колленом суставе?">
                  <el-radio-group v-model="form.is_knee_unbend" @change="page5">
                    <el-radio :label="true" size="large" border>Да</el-radio>
                    <el-radio :label="false" size="large" border>Нет</el-radio>
                  </el-radio-group>
                </el-form-item>
                <div class="quiz-buttons">
                  <el-button type="primary" @click="prev">← Назад</el-button>
                </div>
              </div>
              <div v-else class="no-legs">
                <p>Это страница пустая</p>
                <div class="quiz-buttons">
                  <el-button type="primary" @click="prev">← Назад</el-button>
                  <el-button
                    type="primary"
                    class="button"
                    @click="
                      () => {
                        this.$refs['carousel'].next();
                      }
                    "
                    >Вперёд →</el-button
                  >
                </div>
              </div>
            </div>
          </el-carousel-item>

          <!-- _____________________________________________________________ -->

          <el-carousel-item class="carousel-wrapper"
            ><div class="quiz-el">
              <div v-if="form.is_injured_leg_movemented === true">
                <el-form-item label="Загрузите видео вашей ходьбы"
                  ><el-upload
                    class="upload-demo"
                    drag
                    action="https://run.mocky.io/v3/9d059bf9-4660-45f2-925d-ce80ad6c4d15"
                    multiple
                    :before-upload="
                      () => {
                        upload_success.page6_leg_video = true;
                        page6();
                      }
                    "
                  >
                    <el-icon class="el-icon--upload"><upload-filled /></el-icon>
                    <div class="el-upload__text">
                      Drop file here or <em>click to upload</em>
                    </div>
                  </el-upload></el-form-item
                >
                <div class="quiz-buttons">
                  <el-button type="primary" @click="prev">← Назад</el-button>
                </div>
              </div>
              <div v-else class="no-legs">
                <p>Это страница пустая</p>
                <div class="quiz-buttons">
                  <el-button type="primary" @click="prev">← Назад</el-button>
                  <el-button
                    type="primary"
                    class="button"
                    @click="
                      () => {
                        this.$refs['carousel'].next();
                      }
                    "
                    >Вперёд →</el-button
                  >
                </div>
              </div>
            </div>
          </el-carousel-item>

          <!-- _____________________________________________________________ -->

          <el-carousel-item class="carousel-wrapper">
            <div class="quiz-el">
              <div>
                <el-form-item
                  label="Имеются ли у вас движения на поражённой руке?"
                >
                  <el-radio-group
                    v-model="form.is_injured_arm_movemented"
                    @change="page7"
                  >
                    <el-radio :label="true" size="large" border>Да</el-radio>
                    <el-radio :label="false" size="large" border>Нет</el-radio>
                  </el-radio-group>
                </el-form-item>

                <div v-if="form.is_injured_arm_movemented">
                  <el-form-item label="На сколько % она работает?">
                    <el-select
                      @change="page7"
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

                  <el-form-item label="Сгибается ли рука в локтевом суставе?">
                    <el-radio-group
                      v-model="form.is_elbow_bend"
                      @change="page7"
                    >
                      <el-radio :label="true" size="large" border>Да</el-radio>
                      <el-radio :label="false" size="large" border
                        >Нет</el-radio
                      >
                    </el-radio-group>
                  </el-form-item>

                  <el-form-item label="Разгибается ли рука в локтевом суставе?">
                    <el-radio-group
                      v-model="form.is_elbow_unbend"
                      @change="page7"
                    >
                      <el-radio :label="true" size="large" border>Да</el-radio>
                      <el-radio :label="false" size="large" border
                        >Нет</el-radio
                      >
                    </el-radio-group>
                  </el-form-item>
                </div>

                <div class="quiz-buttons">
                  <el-button type="primary" @click="prev">← Назад</el-button>
                </div>
              </div>
            </div>
          </el-carousel-item>

          <!-- _____________________________________________________________ -->

          <el-carousel-item class="carousel-wrapper">
            <div class="quiz-el">
              <div v-if="form.is_injured_arm_movemented">
                <el-form-item label="Сгибается ли рука в предплечье?">
                  <el-radio-group
                    v-model="form.is_forearm_bend"
                    @change="page8"
                  >
                    <el-radio :label="true" size="large" border>Да</el-radio>
                    <el-radio :label="false" size="large" border>Нет</el-radio>
                  </el-radio-group>
                </el-form-item>

                <el-form-item label="Разгибается ли рука в предплечье?">
                  <el-radio-group
                    v-model="form.is_forearm_unbend"
                    @change="page8"
                  >
                    <el-radio :label="true" size="large" border>Да</el-radio>
                    <el-radio :label="false" size="large" border>Нет</el-radio>
                  </el-radio-group>
                </el-form-item>

                <el-form-item
                  label="Имеются ли у вас движения в пальцах на руке?"
                >
                  <el-radio-group
                    v-model="form.is_injured_finger_movemented"
                    @change="page8"
                  >
                    <el-radio :label="true" size="large" border>Да</el-radio>
                    <el-radio :label="false" size="large" border>Нет</el-radio>
                  </el-radio-group>
                </el-form-item>

                <div class="quiz-buttons">
                  <el-button type="primary" @click="prev">← Назад</el-button>
                </div>
              </div>
              <div v-else class="no-legs">
                <p>Это страница пустая</p>
                <div class="quiz-buttons">
                  <el-button type="primary" @click="prev">← Назад</el-button>
                  <el-button
                    type="primary"
                    class="button"
                    @click="
                      () => {
                        this.$refs['carousel'].next();
                      }
                    "
                    >Вперёд →</el-button
                  >
                </div>
              </div>
            </div>
          </el-carousel-item>

          <!-- _____________________________________________________________ -->

          <el-carousel-item class="carousel-wrapper">
            <div class="quiz-el">
              <div v-if="form.is_injured_arm_movemented">
                <el-form-item>Загрузите видео вашх рук</el-form-item>
                <el-form-item
                  ><el-upload
                    class="upload-demo"
                    drag
                    action="https://run.mocky.io/v3/9d059bf9-4660-45f2-925d-ce80ad6c4d15"
                    multiple
                    :before-upload="
                      () => {
                        upload_success.page9_arm_video = true;
                        page9();
                      }
                    "
                  >
                    <el-icon class="el-icon--upload"><upload-filled /></el-icon>
                    <div class="el-upload__text">
                      Drop file here or <em>click to upload</em>
                    </div>
                  </el-upload></el-form-item
                >
                <div class="quiz-buttons">
                  <el-button type="primary" @click="prev">← Назад</el-button>
                </div>
              </div>
              <div v-else class="no-legs">
                <p>Это страница пустая</p>
                <div class="quiz-buttons">
                  <el-button type="primary" @click="prev">← Назад</el-button>
                  <el-button
                    type="primary"
                    class="button"
                    @click="
                      () => {
                        this.$refs['carousel'].next();
                      }
                    "
                    >Вперёд →</el-button
                  >
                </div>
              </div>
            </div>
          </el-carousel-item>

          <!-- _____________________________________________________________ -->

          <el-carousel-item class="carousel-wrapper">
            <div class="quiz-el">
              <div>
                <el-form-item
                  label="В каком году вы планируете восстанавливаться?"
                  style="margin-bottom: 1px"
                >
                  <el-radio-group
                    v-model="form.now_year_to_repair"
                    @change="page10"
                  >
                    <el-radio label="now" size="large" border>В этом</el-radio>
                    <el-radio label="later" size="large" border
                      >В последующих</el-radio
                    >
                  </el-radio-group>
                </el-form-item>

                <el-form-item v-if="form.now_year_to_repair == 'later'">
                  <div style="text-align: left">
                    <p
                      style="
                        margin-bottom: 0;
                        line-height: 20px;
                        font-size: 11px;
                      "
                    >
                      Напоминание: чем дольше времени проходит с момента
                      инсульта , тем сложнее реабилитация
                    </p>
                  </div>
                </el-form-item>

                <el-form-item label="Где вы собираетесь восстанавливаться?">
                  <el-radio-group
                    v-model="form.where_to_repair"
                    @change="page10"
                  >
                    <el-radio label="outside" size="large" border
                      >За пределами страны
                    </el-radio>
                    <el-radio label="in_my_country" size="large" border
                      >В моей стране</el-radio
                    >
                    <el-radio label="home" size="large" border
                      >На дому</el-radio
                    >
                  </el-radio-group>
                </el-form-item>

                <div class="quiz-buttons">
                  <el-button type="primary" @click="prev">← Назад</el-button>
                </div>
              </div>
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
import ReadyForm from "@/components/form_is_send.vue";
export default {
  name: "FormSelection",
  components: { ReadyForm },
  data() {
    return {
      upload_filled: upload_filled,
      form_send_status: 0,
      out_password: "",

      upload_success: {
        page1_avatar: false,
        page6_leg_video: false,
        page9_arm_video: false,
      },

      form: {
        // 1
        email: null,
        name: null,
        last_name: null,
        date_of_birth: null,
        // 2
        phone: null,
        region: null,
        city: null,
        gender: null,
        // 3
        stroke: null,
        problem_no_stroke: null,
        type_of_stroke: null,
        date_of_stroke: null,
        percent_of_information: null,
        // 4
        is_injured_leg_movemented: null,
        percent_of_injured_leg_movemented: null,
        is_injured_ankle_movemented: null,
        is_can_sit: null,
        // 5
        is_can_state: null,
        is_patient_walk_with_supports: null,
        is_knee_bend: null,
        is_knee_unbend: null,
        //6
        video_leg_file: "",
        // 7
        is_injured_arm_movemented: null,
        percent_of_injured_arm_movemented: null,
        is_elbow_bend: null,
        is_elbow_unbend: null,
        // 8
        is_forearm_bend: null,
        is_forearm_unbend: null,
        is_injured_finger_movemented: null,
        // 9
        video_arm_file: "",
        // 10
        now_year_to_repair: null,
        where_to_repair: null,
      },
    };
  },
  methods: {
    prev() {
      this.$refs["carousel"].prev();
    },

    page1() {
      if (
        this.form.email !== null &&
        this.form.name !== null &&
        this.form.last_name !== null &&
        this.form.date_of_birth !== null &&
        this.upload_success.page1_avatar
      )
        this.$refs["carousel"].next();
    },

    page2() {
      if (
        this.form.phone !== null &&
        this.form.gender !== null &&
        this.form.region !== null &&
        this.form.city !== null
      )
        this.$refs["carousel"].next();
    },

    page3() {
      if (this.form.stroke !== null)
        if (this.form.stroke) {
          if (
            this.form.type_of_stroke !== null &&
            this.form.date_of_stroke !== null &&
            this.form.percent_of_information !== null
          )
            this.$refs["carousel"].next();
        } else {
          if (this.form.problem_no_stroke !== null) {
            this.form_is_send = true;
            this.onSubmit();
          }
        }
    },

    page4() {
      if (
        this.form.is_injured_leg_movemented !== null &&
        (!this.form.is_injured_leg_movemented ||
          (this.form.is_injured_leg_movemented &&
            this.form.percent_of_injured_leg_movemented !== null &&
            this.form.is_injured_ankle_movemented !== null &&
            this.form.is_can_sit !== null))
      ) {
        this.$refs["carousel"].next();
      }
    },

    page5() {
      if (
        this.form.is_can_state !== null &&
        this.form.is_patient_walk_with_supports !== null &&
        this.form.is_knee_bend !== null &&
        this.form.is_knee_unbend !== null
      )
        this.$refs["carousel"].next();
    },

    page6() {
      if (this.upload_success.page6_leg_video) this.$refs["carousel"].next();
    },

    page7() {
      if (
        this.form.is_injured_arm_movemented !== null &&
        (!this.form.is_injured_arm_movemented ||
          (this.form.is_injured_arm_movemented &&
            this.form.percent_of_injured_arm_movemented !== null &&
            this.form.is_elbow_bend !== null &&
            this.form.is_elbow_unbend !== null))
      ) {
        this.$refs["carousel"].next();
      }
    },

    page8() {
      if (
        this.form.is_forearm_bend !== null &&
        this.form.is_forearm_unbend !== null &&
        this.form.is_injured_finger_movemented !== null
      )
        this.$refs["carousel"].next();
    },

    page9() {
      if (this.upload_success.page9_arm_video) this.$refs["carousel"].next();
    },

    page10() {
      if (
        this.form.now_year_to_repair !== null &&
        this.form.where_to_repair !== null
      ) {
        this.form_is_send = true;
        this.onSubmit();
      }
    },

    onSubmit: function () {
      this.form_send_status = 1;
      fetch("http://localhost:5600/selection", {
        // fetch("http://45.91.8.150:5600/selection", {
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
          this.out_password = data["data"]["password"];
          this.form_send_status = 2;
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

.no-legs {
  display: flex;
  flex-direction: column;
}

.carousel-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;

  .quiz-el {
    width: 70vw;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
}

.form-w8 {
  height: 70vh;
  font-size: 40px;

  display: flex;
  align-items: center;
  justify-content: center;
}

.form-send-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.quiz-buttons {
  display: flex;
  flex-direction: row;
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
