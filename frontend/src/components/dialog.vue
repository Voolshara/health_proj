<template>
  <el-dialog
    v-model="dialogVisible"
    title="Введите номер своего личного кабинета"
    width="40%"
    :show-close="false"
  >
    <el-form :model="form" style="margin: 40px; margin-bottom: 0">
      <el-form-item label="Номер" :label-width="formLabelWidth">
        <el-input v-model="form.id" autocomplete="off" />
      </el-form-item>

      <el-form-item>
        <el-button type="primary" @click="onSubmit">Отправить</el-button>
      </el-form-item>
    </el-form>
    <p>*Это окно свёрстано, но ещё не подключено!!!*</p>
    <p>*Нажмите куда либо за пределы окна*</p>
  </el-dialog>
</template>

<script>
export default {
  name: "DialogForm2",
  data() {
    return {
      dialogVisible: true,
      form: {
        id: "",
      },
    };
  },
  methods: {},
};
</script>

<style scoped>
.dialog-footer button:first-child {
  margin-right: 10px;
}
</style>
