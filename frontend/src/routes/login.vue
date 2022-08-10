<template>
  <div class="panel-container">
    <p class="join join-left">Личный кабинет</p>
    <el-form :model="user" label-width="180px" class="form-enter join-left">
      <el-form-item
        label="Почта:"
        prop="email"
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
      >
        <el-input v-model="user.email" />
      </el-form-item>
      <el-form-item
        label="Пароль для доступа:"
        prop="passwrd"
        :rules="[
          {
            required: true,
            message: 'Пожалуйста введите пароль',
            trigger: 'blur',
          },
        ]"
      >
        <el-input v-model="user.password" type="password" />
      </el-form-item>

      <el-form-item style="margin-top: 30px">
        <el-button type="primary" v-on:click="onSubmit">Войти</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  name: "LoginPage",
  data() {
    return {
      is_can_enter: false,
      user: {
        email: "",
        password: "",
      },
    };
  },
  computed: {
    loggedIn() {
      return this.$store.state.auth.status.loggedIn;
    },
  },
  created() {
    if (this.loggedIn) {
      this.$router.push("/profile");
    }
  },
  methods: {
    onSubmit() {
      this.loading = true;
      this.$store.dispatch("auth/login", this.user).then(
        () => {
          this.$router.push("/profile");
        },
        (error) => {
          this.loading = false;
          this.message =
            (error.response &&
              error.response.data &&
              error.response.data.message) ||
            error.message ||
            error.toString();
        }
      );
    },
  },
};
</script>

<style>
.form-enter {
  width: 30vw;
}

.join {
  font-size: 70px;
  margin-bottom: 50px;
  margin-left: 170px;
}

.join-left {
  position: relative;
  left: -70px;
}

.panel-container {
  align-items: center;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  height: 65vh;
  align-items: center;
}
</style>
