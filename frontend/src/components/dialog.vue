<template>
  <el-dialog
    v-model="dialogVisible"
    title="Введите номер своего личного кабинета"
    width="40%"
    :show-close="false"
    :before-close="() => {}"
  >
    <el-form
      :model="form"
      label-width="100px"
      style="margin: 40px; margin-bottom: 0; margin-left: 10px"
    >
      <el-form-item label="Ваша почта" :label-width="formLabelWidth">
        <el-input v-model="form.email" autocomplete="off" />
      </el-form-item>

      <el-form-item label="Код" :label-width="formLabelWidth">
        <el-input v-model="form.password" autocomplete="off" />
      </el-form-item>

      <el-form-item>
        <el-button type="primary" @click="onSubmit">Отправить</el-button>
      </el-form-item>
    </el-form>
    <div v-if="form_is_send">
      <p v-if="data === null">Такой почты нет</p>
    </div>
    {{ data }}
  </el-dialog>
</template>

<script>
export default {
  name: "DialogForm2",
  data() {
    return {
      dialogVisible: true,
      form: {
        email: "",
        password: "",
      },
      data: null,
      form_is_send: false,
    };
  },
  methods: {
    onSubmit: function () {
      this.form_is_send = false;
      //fetch("http://localhost:5600/check_email", {
      fetch("http://45.91.8.150:5600/check_email", {
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
          this.data = data["data"];
          this.form_is_send = true;
          this.$emit("data", this.data);
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
.dialog-footer button:first-child {
  margin-right: 10px;
}
</style>
