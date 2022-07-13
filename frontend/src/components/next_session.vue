<template>
  <div class="w8-form">
    <p>Через сколько часов вы хотите начать следующий этап?</p>

    <el-select
      v-model="next_stage"
      placeholder="Выберите"
      @change="change_session()"
    >
      <el-option label="Через 24ч" value="24" />
      <el-option label="Через 48ч" value="48" />
      <el-option label="Через 72ч" value="72" />
    </el-select>
  </div>
</template>

<script>
export default {
  name: "W8-form",

  data() {
    return {
      next_stage: "",
    };
  },
  methods: {
    change_session() {
      this.$emit("value", this.next_stage);
    },
  },
};
</script>

<style>
.w8-form {
  margin: 70px;
}
</style>
