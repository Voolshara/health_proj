<template>
  <div class="container-form">
    <p class="main-par">Анкета 2</p>
    <el-image
      style="width: 300px; height: 200px"
      src="@/assets/fast_recover.png"
      :fit="'fit'"
    />
    <el-form :model="form" label-width="200px" class="form">
      <el-form-item label="Имя">
        <el-input v-model="form.name" placeholder="Имя" />
      </el-form-item>
      <el-form-item label="Фамилия">
        <el-input v-model="form.last_name" placeholder="Фамилия" />
      </el-form-item>
      <el-form-item label="Дата Рождения">
        <el-date-picker
          v-model="form.date_of_birth"
          type="date"
          placeholder="Выберете дату"
          style="width: 100%"
        />
      </el-form-item>
      <el-form-item label="Укажите пол">
        <el-radio-group v-model="form.gender">
          <el-radio label="Мужской" size="large" border>Мужской</el-radio>
          <el-radio label="Женский" size="large" border>Женский</el-radio>
          <el-radio label="Другое" size="large" border>Другое</el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item>
        <div style="text-align: left">
          <p style="margin-bottom: 0">Укажите страну</p>
          <p style="margin-bottom: 0; font-size: 10px; line-height: 5px">
            После выбора страны мы автоматически подстроимся под ваш часовой
            пояс и не буреем вас беспокоить в ночное время
          </p>
        </div>
      </el-form-item>
      <el-form-item label="Страна">
        <el-select v-model="form.region" placeholder="Выберете страну">
          <el-option label="США" value="США" />
          <el-option label="Россия" value="Россия" />
        </el-select>
      </el-form-item>
      <el-form-item>Введите номер телефона</el-form-item>
      <el-form-item label="Телефон">
        <el-input v-model="form.phone" placeholder="Телефон" />
      </el-form-item>
      <el-form-item label="У вас был инсульт ?">
        <el-radio-group v-model="form.stroke">
          <el-radio :label="true" size="large" border>Да</el-radio>
          <el-radio :label="false" size="large" border>Нет</el-radio>
        </el-radio-group>
      </el-form-item>
      <div v-if="form.stroke">
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
          <el-date-picker
            v-model="form.date_of_stroke"
            type="date"
            placeholder="Выберете дату"
            style="width: 100%"
          />
        </el-form-item>
        <el-form-item label="Вы знаете причину?">
          <el-radio-group v-model="form.know_reason">
            <el-radio :label="true" size="large" border>Да</el-radio>
            <el-radio :label="false" size="large" border>Нет</el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item
          >Как пациент воспринимает какую-либо информацию?</el-form-item
        >
        <el-form-item label="Укажите %">
          <el-select
            v-model="form.percent_of_information"
            placeholder="Указананный уровень"
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
          >Имеется ли у вас движения на поражённой ноге?</el-form-item
        >
        <el-form-item label="">
          <el-radio-group v-model="form.is_injured_leg_movemented">
            <el-radio :label="true" size="large" border>Да</el-radio>
            <el-radio :label="false" size="large" border>Нет</el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item v-if="form.is_injured_leg_movemented"
          >На сколько % она работает?</el-form-item
        >
        <el-form-item v-if="form.is_injured_leg_movemented" label="Укажите %">
          <el-select
            v-model="form.percent_of_injured_leg_movemented"
            placeholder="Указананный уровень"
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

        <el-form-item v-if="form.is_injured_leg_movemented"
          >Имеется ли у вас движения в голеностопе?</el-form-item
        >
        <el-form-item label="" v-if="form.is_injured_leg_movemented">
          <el-radio-group v-model="form.is_injured_ankle_movemented">
            <el-radio :label="true" size="large" border>Да</el-radio>
            <el-radio :label="false" size="large" border>Нет</el-radio>
          </el-radio-group>
        </el-form-item>

        <el-form-item v-if="form.is_injured_leg_movemented"
          >Может ли пациент сидеть без опоры под спину?</el-form-item
        >
        <el-form-item label="" v-if="form.is_injured_leg_movemented">
          <el-radio-group v-model="form.is_can_sit">
            <el-radio :label="true" size="large" border>Да</el-radio>
            <el-radio :label="false" size="large" border>Нет</el-radio>
          </el-radio-group>
        </el-form-item>

        <el-form-item v-if="form.is_injured_leg_movemented"
          >Может ли пациент самостоятельно стоять?</el-form-item
        >
        <el-form-item label="" v-if="form.is_injured_leg_movemented">
          <el-radio-group v-model="form.is_can_state">
            <el-radio :label="true" size="large" border>Да</el-radio>
            <el-radio :label="false" size="large" border>Нет</el-radio>
          </el-radio-group>
        </el-form-item>

        <el-form-item v-if="form.is_injured_leg_movemented"
          >Может ли пациент ходить с опорой?</el-form-item
        >
        <el-form-item label="" v-if="form.is_injured_leg_movemented">
          <el-radio-group v-model="form.is_patient_walk_with_supports">
            <el-radio :label="true" size="large" border>Да</el-radio>
            <el-radio :label="false" size="large" border>Нет</el-radio>
          </el-radio-group>
        </el-form-item>

        <el-form-item v-if="form.is_injured_leg_movemented"
          >Сгибается / Разгибается нога в колленом суставе?</el-form-item
        >
        <el-form-item label="" v-if="form.is_injured_leg_movemented">
          <el-radio-group v-model="form.is_knee_work">
            <el-radio :label="true" size="large" border>Да</el-radio>
            <el-radio :label="false" size="large" border>Нет</el-radio>
          </el-radio-group>
        </el-form-item>

        <el-form-item
          >Имеются ли у вас движения на поражённой руке?</el-form-item
        >
        <el-form-item label="">
          <el-radio-group v-model="form.is_injured_arm_movemented">
            <el-radio :label="true" size="large" border>Да</el-radio>
            <el-radio :label="false" size="large" border>Нет</el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item v-if="form.is_injured_arm_movemented"
          >На сколько % она работает?</el-form-item
        >
        <el-form-item v-if="form.is_injured_arm_movemented" label="Укажите %">
          <el-select
            v-model="form.percent_of_injured_arm_movemented"
            placeholder="Указананный уровень"
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

        <el-form-item v-if="form.is_injured_arm_movemented"
          >Сгибается / Разгибается рукав локтевом суставе?</el-form-item
        >
        <el-form-item label="" v-if="form.is_injured_arm_movemented">
          <el-radio-group v-model="form.is_elbow_work">
            <el-radio :label="true" size="large" border>Да</el-radio>
            <el-radio :label="false" size="large" border>Нет</el-radio>
          </el-radio-group>
        </el-form-item>

        <el-form-item v-if="form.is_injured_arm_movemented"
          >Сгибается / Разгибается рука в предплечье?</el-form-item
        >
        <el-form-item label="" v-if="form.is_injured_arm_movemented">
          <el-radio-group v-model="form.is_forearm_work">
            <el-radio :label="true" size="large" border>Да</el-radio>
            <el-radio :label="false" size="large" border>Нет</el-radio>
          </el-radio-group>
        </el-form-item>

        <el-form-item v-if="form.is_injured_arm_movemented"
          >Имеются ли у вас движения в пальцах на руке?</el-form-item
        >
        <el-form-item label="" v-if="form.is_injured_arm_movemented">
          <el-radio-group v-model="form.is_injured_finger_movemented">
            <el-radio :label="true" size="large" border>Да</el-radio>
            <el-radio :label="false" size="large" border>Нет</el-radio>
          </el-radio-group>
        </el-form-item>
      </div>
      <el-form-item>
        <el-button type="primary" @click="onSubmit"
          >Отправить запрос на восстановление</el-button
        >
      </el-form-item>
    </el-form>
    <!-- <div style="width: 100%; height: 500px"></div> -->
  </div>
</template>

<script>
export default {
  name: "FormFirst",
  data() {
    return {
      form: {
        name: "",
        last_name: "",
        date_of_birth: "",
        gender: "",
        region: "",
        phone: "",
        stroke: null,
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
        is_knee_work: "",
        is_injured_arm_movemented: "",
        percent_of_injured_arm_movemented: "",
        is_elbow_work: "",
        is_forearm_work: "",
        is_injured_finger_movemented: "",
      },
    };
  },
  methods: {
    onSubmit: function () {
      fetch("http://localhost:5600/new_user", {
        // fetch("http://localhost:4600/article_data", {
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
</style>
