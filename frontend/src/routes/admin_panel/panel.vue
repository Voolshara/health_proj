<template>
  <div class="panel-container">
    <p class="panel-name">Список пользователей</p>
    <div class="users animate__animated animate__backInUp animate__delay-1s">
      <el-table :data="user_data" size="large" @row-click="click_to_row">
        <el-table-column prop="[0]" label="Имя" />
        <el-table-column prop="[1]" label="Фамилия" />
        <el-table-column prop="[2]" label="Пол">
          <template #default="scope">
            <el-tag
              class="ml-2"
              type=""
              size="large"
              effect="dark"
              v-if="scope.row[2] == 'М'"
              >{{ scope.row[2] }}</el-tag
            >
            <el-tag
              class="ml-2"
              type="danger"
              size="large"
              effect="dark"
              v-else
              >{{ scope.row[2] }}</el-tag
            >
          </template>
        </el-table-column>
        <el-table-column prop="[3]" label="Страна">
          <template #default="scope">
            <el-tag type="info" size="large" effect="dark">{{
              scope.row[3]
            }}</el-tag>
          </template>
        </el-table-column>
        <el-table-column label="Дата рождения">
          <template #header>
            <el-input
              v-model="search"
              size="small"
              placeholder="Type to search"
              @input="new_filters"
            />
          </template>
          <template #default="scope">
            {{
              scope.row[6].split(" ")[1] +
              " " +
              scope.row[6].split(" ")[2] +
              " " +
              scope.row[6].split(" ")[3]
            }}
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
export default {
  name: "AdminPanel",
  data() {
    return {
      original_user_data: [],
      user_data: [],
      search: "",
    };
  },
  methods: {
    click_to_row: function (row) {
      this.$router.push("/admin_panel/user/" + row[5]);
    },
    new_filters: function () {
      this.user_data = this.original_user_data.filter(
        (data) =>
          !this.search ||
          data[1].toLowerCase().includes(this.search.toLowerCase()) ||
          data[0].toLowerCase().includes(this.search.toLowerCase()) ||
          data[6].toLowerCase().includes(this.search.toLowerCase())
      );
    },
  },
  mounted() {
    //fetch("http://localhost:5600/panel/get_users", {
    fetch("http://45.91.8.150:5600/panel/get_users", {
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
        this.original_user_data = data["data"];
        this.user_data = this.original_user_data;
      })
      .catch(() => {
        this.user_data = "Ошибка 500";
      });
  },
};
</script>

<style lang="scss">
.users {
  width: 80vw;
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin: auto;

  .image {
    width: 50px;
    height: 50px;
  }
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
  font-size: 40px;
  margin-bottom: 40px;
}

.panel-container {
  align-items: center;
  text-align: center;
  justify-content: center;
  padding-top: 40px;
  padding-bottom: 80px;
}

.cont {
  display: none;
}
</style>
