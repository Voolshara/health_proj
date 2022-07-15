<template>
  <div class="container-user">
    <el-row class="top-bunner">
      <el-col :span="9"><img src="/img/user.png" class="image" /></el-col>
      <el-col :span="12">
        <div class="info-cont">
          <el-descriptions title="Информация о пользователе" :column="1" border>
            <el-descriptions-item
              label="ID пользователя"
              label-align="left"
              align="center"
              label-class-name="my-label"
              class-name="my-content"
              width="0"
              >{{ data["id"] }}</el-descriptions-item
            >

            <el-descriptions-item
              label="Имя"
              label-align="left"
              align="center"
              label-class-name="my-label"
              class-name="my-content"
              width="0"
              >{{ data["name"] }}</el-descriptions-item
            >

            <el-descriptions-item
              label="Фамилия"
              label-align="left"
              align="center"
              label-class-name="my-label"
              class-name="my-content"
              width="0"
              >{{ data["last_name"] }}</el-descriptions-item
            >

            <el-descriptions-item
              label="Пол"
              label-align="left"
              align="center"
              label-class-name="my-label"
              class-name="my-content"
              width="0"
              >{{ data["gender"] }}</el-descriptions-item
            >

            <el-descriptions-item
              label="Страна"
              label-align="left"
              align="center"
              label-class-name="my-label"
              class-name="my-content"
              width="0"
              >{{ data["Country"] }}</el-descriptions-item
            >

            <el-descriptions-item
              label="Телефон"
              label-align="left"
              align="center"
              label-class-name="my-label"
              class-name="my-content"
              width="0"
              >{{ data["Phone"] }}</el-descriptions-item
            >

            <el-descriptions-item
              label="Был ли у вас инсульт?"
              label-align="left"
              align="center"
              label-class-name="my-label"
              class-name="my-content"
              width="0"
              >{{ is_been_stroke }}</el-descriptions-item
            >
          </el-descriptions>
        </div></el-col
      >
    </el-row>
    <div style="display: flex; justify-content: center">
      <div class="main-container">
        <p style="margin-top: 70px; font-size: 50px; margin-bottom: 30px">
          Заполнение пациента
        </p>

        <el-tabs v-model="activeTab" class="demo-tabs" @tab-click="handleClick">
          <el-tab-pane label="Отборная анкета" :name="1" class="selection">
            <Selection :data="data" />
          </el-tab-pane>
          <el-tab-pane label="Первая форма" :name="2"
            >Пока ещё не готово (</el-tab-pane
          >
          <el-tab-pane label="Вторая форма" :name="3"
            >Пока ещё не готово (</el-tab-pane
          >
          <el-tab-pane label="Задание 1 - 8" :name="4"
            >Пока ещё не готово (</el-tab-pane
          >
        </el-tabs>
      </div>
    </div>
  </div>
</template>

<script>
import Selection from "@/components/admin_panel/selection_form.vue";
export default {
  name: "UserInPanel",
  components: {
    Selection,
  },
  data() {
    return {
      data: {},
      is_been_stroke: "",
      activeTab: 1,
    };
  },
  mounted() {
    // fetch("http://localhost:5600/panel/get_user_data", {
    fetch("http://45.91.8.150:5600/panel/get_user_data", {
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
        user_id: this.$route.params.id,
      }), // body data type must match "Content-Type" header
    })
      .then((response) => response.json())
      .then((data) => {
        this.data = data["data"];
        if (data["data"]["Selection"]) {
          this.is_been_stroke = "Да";
        } else {
          this.is_been_stroke = "Нет";
        }
      })
      .catch(() => {});
  },
};
</script>

<style lang="scss">
.selection {
  width: 50vw;
}

.top-bunner {
  padding-left: 10vw;
  padding-right: 10vw;
  padding-bottom: 50px;

  .info-cont {
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: left;
    padding-left: 5vw;
    padding-top: 70px;
  }
}

.main-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: left;
  width: 70vw;

  .progress-recovery {
    width: 30vw;
    margin-bottom: 30px;
  }
}

.image {
  width: 100%;
  display: block;
}
.container-user {
  align-items: center;
  text-align: center;

  .main-par {
    text-align: left;
    background-image: url("@/assets/bg_header.png");

    p {
      margin-left: 15vw;
      color: #0836b5;

      font-style: normal;
      font-weight: 900;
      font-size: 70px;
      line-height: 145px;
    }

    name {
      display: block;
      font-size: 20px;
    }

    name:first-letter {
      text-transform: uppercase;
    }
  }
}

.global-footer {
  display: none;
}
</style>
