<template>
  <div class="main-container">
    <Preview />
    <div class="data-container" v-on:scroll="go_scroll">
      <Card1 />
      <Card2 />
      <!--
        <el-image
        class="main-bg"
        v-animate-onscroll="'main-bg-fix'"
        src="/main_page/bg_header.png"
        :fit="'cover'"
      />
      -->
      <!-- <div class="data-inf">
        <div
          class="stroke-text"
          ref="horizontalbox"
          id="sticky"
          v-on="onScroll"
          :class="classes"
        >
          <Element />
        </div>
        <div style="height: 2000vh">some information</div>
      </div> -->
      <!-- <el-steps :active="now_menu" class="steps">
        <el-step title="Step 1" />
        <el-step title="Step 2" />
        <el-step title="Step 3" />
      </el-steps> -->
    </div>
  </div>
</template>
<script>
import Preview from "@/components/first_page/preview.vue";
import Card1 from "@/components/first_page/card1.vue";
import Card2 from "@/components/first_page/card2.vue";
// import Element from "@/components/first_page/element.vue";
export default {
  components: {
    Preview,
    Card1,
    Card2,
  },
  data() {
    return {
      isScrolling: false, // initially false,
      scrollTimeout: null,
      lastScrollTop: 0,
      classes: "stroke-text",
      now_menu: 1,
    };
  },
  created() {
    window.addEventListener("scroll", this.onScroll);
  },
  unmounted() {
    window.removeEventListener("scroll", this.onScroll);
  },
  methods: {
    go_sckull() {
      console.log("qi");
    },
    onScroll() {
      // const vm = this;
      // vm.isScrolling = true; //as soon as scroll event is dispatched, set isScrolling as true
      // clearTimeout(vm.scrollTimeout); // clea
      // vm.scrollTimeout = setTimeout(function () {
      //   vm.isScrolling = false;
      //   vm.$refs.video.pause();
      // }, 100); //300ms after the last event isScrolling will be set false.
      // this.$refs.video.play();
      // var st = window.pageYOffset || document.documentElement.scrollTop; // Credits: "https://github.com/qeremy/so/blob/master/so.dom.js#L426"
      // if (st > this.lastScrollTop) {
      //   this.$refs["horizontalbox"].scrollLeft += 10;
      // } else {
      //   this.$refs["horizontalbox"].scrollLeft -= 10;
      // }
      // this.lastScrollTop = st <= 0 ? 0 : st; // For Mobile or negative scrolling
      // if (
      //   this.lastScrollTop < window.scrollY &&
      //   0 * window.screen.height <= window.scrollY &&
      //   10 * window.screen.height >= window.scrollY
      // ) {
      //   this.now_menu = 1;
      //   // move up!
      // } else if (
      //   this.lastScrollTop < window.scrollY &&
      //   10 * window.screen.height <= window.scrollY &&
      //   20 * window.screen.height >= window.scrollY
      // ) {
      //   this.now_menu = 2;
      //   // move down
      // } else {
      //   this.now_menu = 3;
      // }
      // this.lastScrollTop = window.scrollY;
      // this.scrolled = window.scrollY > 250;
    },
  },
};
</script>

<style lang="scss">
.data-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  position: absolute;
  margin-top: 120vh;

  .data-inf {
    position: relative;
    z-index: 2;

    .stroke-text {
      width: 100vw;
      // overflow: hidden;
    }

    .stroke-text-fixed {
    }
  }
}

.steps {
  width: 70vw;
}

.main-bg-fix {
  position: fixed;
  z-index: 1;
}

.global-footer {
  display: none;
}

body {
  padding: 0;
}

.wrapper {
  align-items: center;
}
</style>
