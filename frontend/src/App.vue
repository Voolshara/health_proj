<template>
  <router-view class="wrapper" />
  <Footer />
</template>

<script>
import Footer from "@/components/footer.vue";
export default {
  name: "App",
  components: {
    Footer,
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&display=swap");

* {
  font-family: Montserrat;
  font-weight: 500;
}
</style>
