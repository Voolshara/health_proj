<template>
  <div class="profile-container">
    <div class="description">
      Это будущее лк пользователя. Пока здесь будут отображаться текущие ссылки
    </div>
    <div class="all-links">
      <router-link to="/form1">Первая форма</router-link>
      <router-link to="/form2">Вторая форма</router-link>
      <router-link to="/task1">Задание 1</router-link>
      <router-link to="/task2">Задание 2</router-link>
      <router-link to="/task3">Задание 3</router-link>
      <router-link to="/task4">Задание 4</router-link>
      <router-link to="/task5">Задание 5</router-link>
      <router-link to="/task6">Задание 6</router-link>
      <router-link to="/task7">Задание 7</router-link>
      <router-link to="/task8">Задание 8</router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: "ProfilePage",
};
</script>

<style lang="scss">
.profile-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.description {
  font-size: 50px;
  text-align: center;
  margin: 30px;
}

.all-links {
  display: flex;
  flex-direction: column;
  margin: 30px;

  a {
    margin: 10px;
  }
}
</style>
