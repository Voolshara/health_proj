<template>
  <p v-if="data === null">Такого пользователя нет</p>
  <el-descriptions v-else :column="1" border style="width: 30vw">
    <el-descriptions-item
      label="Фото"
      label-align="left"
      align="center"
      label-class-name="my-label"
      class-name="my-content"
      width="0"
    >
      <el-image
        style="width: 100px; height: 100px"
        src="/img/user.png"
        :fit="fit"
      />
    </el-descriptions-item>
    <el-descriptions-item
      label="Имя"
      label-align="left"
      align="center"
      label-class-name="my-label"
      class-name="my-content"
      width="0"
      >{{ data[0] }}</el-descriptions-item
    >
    <el-descriptions-item
      label="Фамилия"
      label-align="left"
      align="center"
      label-class-name="my-label"
      class-name="my-content"
      width="0"
      >{{ data[1] }}</el-descriptions-item
    >
    <el-descriptions-item
      label="Дата Рождения"
      label-align="left"
      align="center"
      label-class-name="my-label"
      class-name="my-content"
      width="0"
      >{{
        this.data[2].split(" ")[1] +
        " " +
        this.data[2].split(" ")[2] +
        " " +
        this.data[2].split(" ")[3]
      }}</el-descriptions-item
    >
    <el-descriptions-item
      label="Вид Инсульта"
      label-align="left"
      align="center"
      label-class-name="my-label"
      class-name="my-content"
      width="0"
      >{{ data[5] }}</el-descriptions-item
    >
  </el-descriptions>
</template>

<script>
export default {
  name: "UserBar",
  props: {
    data: Array,
  },
};
</script>
