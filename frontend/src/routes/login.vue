<template>
  <div class="panel-container">
    <p class="join join-left">Личный кабинет</p>
    <el-form
      :model="form_enter"
      label-width="180px"
      class="form-enter join-left"
    >
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
        <el-input v-model="form_enter.email" />
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
        <el-input v-model="form_enter.passwrd" type="password" />
      </el-form-item>

      <el-form-item style="margin-top: 30px">
        <el-button type="primary" @click="onSubmit">Войти</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  name: "AdminPanel",
  data() {
    return {
      is_can_enter: false,
      form_enter: {
        email: "",
        passwrd: "",
      },
    };
  },
  onSubmit: function () {
    fetch("http://45.91.8.150:5600/login", {
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
        data: this.form_enter,
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
