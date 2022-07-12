<template>
  <div class="panel-container">
    <p class="panel-name">Список пользователей</p>
    <div
      class="users-cards animate__animated animate__backInUp animate__delay-1s"
    >
      <div v-for="(item, index) in user_data" :key="index">
        <router-link
          :to="'/admin_panel/user/' + item[5]"
          style="text-decoration: none"
        >
          <el-card
            class="card good"
            :body-style="{ padding: '0' }"
            :shadow="'hover'"
            v-if="item[4]"
          >
            <img src="/img/user.png" class="image" />
            <div style="padding-top: 14px">
              <div class="top">
                <span class="card-name" style="padding-right: 14px">{{
                  item[0]
                }}</span
                ><span class="card-name"> {{ item[1] }}</span>
              </div>
              <div class="bottom">
                <el-tag
                  class="ml-2"
                  type=""
                  size="large"
                  effect="dark"
                  v-if="item[2] == 'М'"
                  >{{ item[2] }}</el-tag
                >
                <el-tag
                  class="ml-2"
                  type="error"
                  size="large"
                  effect="dark"
                  v-else
                  >{{ item[2] }}</el-tag
                >
                <el-tag class="ml-2" type="info" size="large" effect="dark">{{
                  item[3]
                }}</el-tag>
              </div>
            </div>
          </el-card>

          <el-card
            class="card bad"
            :body-style="{ padding: '0' }"
            :shadow="'hover'"
            v-else
          >
            <img src="/img/user.png" class="image" />
            <div style="padding-top: 14px">
              <div class="top">
                <span class="card-name" style="padding-right: 14px">{{
                  item[0]
                }}</span
                ><span class="card-name"> {{ item[1] }}</span>
              </div>
              <div class="bottom">
                <el-tag
                  class="ml-2"
                  type=""
                  size="large"
                  effect="dark"
                  v-if="item[2] == 'М'"
                  >{{ item[2] }}</el-tag
                >
                <el-tag
                  class="ml-2"
                  type="error"
                  size="large"
                  effect="dark"
                  v-else
                  >{{ item[2] }}</el-tag
                >
                <el-tag class="ml-2" type="info" size="large" effect="dark">{{
                  item[3]
                }}</el-tag>
              </div>
            </div>
          </el-card>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AdminPanel",
  data() {
    return {
      user_data: [],
    };
  },
  mounted() {
    //fetch("http://localhost:5600/panel/get_users", {
    fetch("http://45.91.8.150:5600/get_users", {
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
      body: JSON.stringify({}), // body data type must match "Content-Type" header
    })
      .then((response) => response.json())
      .then((data) => {
        this.user_data = data["data"];
      })
      .catch(() => {
        this.user_data = "Ошибка 500";
      });
  },
};
</script>

<style lang="scss">
.users-cards {
  display: grid;
  column-gap: 100px;
  row-gap: 50px;
  grid-template-columns: 300px 300px 300px;
  justify-content: center;

  .card {
    width: 300px;

    .card-name {
      display: block;
      font-size: 20px;
    }

    .card-name:first-letter {
      text-transform: uppercase;
    }

    .image {
      width: 100%;
      display: block;
    }
  }
}

.good {
  background: rgb(55, 255, 81);
  background: linear-gradient(
    205deg,
    rgba(55, 255, 81, 0.29485297536983546) 0%,
    rgba(9, 51, 121, 0) 36%,
    rgba(202, 234, 255, 0.5161414907759979) 100%
  );
}

.bad {
  background: rgb(255, 55, 55);
  background: linear-gradient(
    205deg,
    rgba(255, 55, 55, 0.29485297536983546) 0%,
    rgba(9, 51, 121, 0) 36%,
    rgba(202, 234, 255, 0.5161414907759979) 100%
  );
}

.top {
  display: flex;
  flex-direction: row;
  justify-content: center;
}

.bottom {
  margin-top: 8px;
  margin-bottom: 20px;
}

.panel-name {
  font-size: 70px;
  margin-bottom: 40px;
}

.panel-container {
  align-items: center;
  text-align: center;
  justify-content: center;
  padding-top: 40px;
  padding-bottom: 80px;
}
</style>
