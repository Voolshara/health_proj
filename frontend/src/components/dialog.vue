<template>
  <el-dialog
    v-model="dialogVisible"
    title="Войдите"
    width="40%"
    :show-close="false"
    :before-close="() => {}"
  >
    <el-form
      :model="user"
      label-width="100px"
      style="margin: 40px; margin-bottom: 0; margin-left: 10px"
    >
      <el-form-item label="Ваша почта">
        <el-input v-model="user.email" autocomplete="off" />
      </el-form-item>

      <el-form-item label="Пароль">
        <el-input v-model="user.password" autocomplete="off" />
      </el-form-item>

      <el-form-item>
        <el-button type="primary" v-on:click="onSubmit">Отправить</el-button>
      </el-form-item>
    </el-form>
    <div v-if="form_is_send">
      <p v-if="data === null">Такой почты нет</p>
    </div>
    {{ data }}
  </el-dialog>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
export default {
  name: "DialogForm2",
  data() {
    return {
      dialogVisible: true,
      user: {
        email: "",
        password: "",
        errorMsg: "",
      },
      data: null,
    };
  },

  methods: {
    onSubmit() {
      alert("HI");
      this.loginUser(this.user).then(() => {
        if (this.authUser.authenticated) {
          this.$router.push("/secure");
        } else {
          // Handle error
          this.user = {
            email: null,
            password: null,
          };
        }
      });
    },
    ...mapActions({
      loginUser: "auth/loginUser",
    }),
  },
  computed: {
    ...mapGetters({
      authUser: "auth/user",
    }),
  },
  // onSubmit: function () {
  //   //fetch("http://localhost:5600/form_selection", {
  //   fetch("http://45.91.8.150:5600/form_selection", {
  //     method: "POST", // *GET, POST, PUT, DELETE, etc.
  //     mode: "cors", // no-cors, *cors, same-origin
  //     cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
  //     credentials: "same-origin", // include, *same-origin, omit
  //     headers: {
  //       "Content-Type": "application/json",
  //       "Access-Control-Allow-Private-Network": true,
  //     },
  //     redirect: "follow", // manual, *follow, error
  //     referrerPolicy: "no-referrer", // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
  //     body: JSON.stringify({
  //       data: this.form,
  //     }), // body data type must match "Content-Type" header
  //   })
  //     .then((response) => response.json())
  //     .then((data) => {
  //       this.form_is_send = true;
  //       console.log(data);
  //     })
  //     .catch((error) => {
  //       console.error("Error:", error);
  //       return null;
  //     });
  // },
};
</script>

<style scoped>
.dialog-footer button:first-child {
  margin-right: 10px;
}
</style>
