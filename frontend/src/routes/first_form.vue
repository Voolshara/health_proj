<template>
  <div class="container">
    <p>Заполните анкету</p>
    <el-form :model="form" label-width="200px">
      <el-form-item> Введите данные </el-form-item>
      <el-form-item label="ФИО">
        <el-input v-model="form.fio" />
      </el-form-item>
      <el-form-item label="Дата Рождения">
        <el-date-picker
          v-model="form.date_of_birth"
          type="date"
          placeholder="Pick a date"
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
            После выбора страны автоматически включится ночной режим
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
        <el-input v-model="form.phone" />
      </el-form-item>
      <el-form-item label="Телефон">
        <el-input v-model="form.phone" />
      </el-form-item>
      <el-form-item label="У вас был инсульт">
        <el-radio-group v-model="form.stroke">
          <el-radio label="1" size="large" border>Да</el-radio>
          <el-radio label="0" size="large" border>Нет</el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item label="Вид инсульта" v-if="form.stroke[0] == '1'">
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
    </el-form>
    {{ form }}
    <div></div>
  </div>
</template>

<script>
export default {
  name: "FormFirst",
  data() {
    return {
      form: {
        fio: "",
        date_of_birth: "",
        gender: [],
        region: [],
        phone: "",
        stroke: [],
        type_of_stroke: [],
      },
    };
  },
  methods: {
    onSubmit: function () {
      console.log("submit!");
    },
  },
};
</script>

<style>
.container {
  align-items: center;
  text-align: center;
  margin-top: 30px;
  position: relative;
  left: -5%;
}
</style>
