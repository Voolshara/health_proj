import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    component: () => import("@/routes/main.vue"),
  },
  {
    path: "/:lang/terms",
    component: () => import("@/routes/terms.vue"),
  },
  {
    path: "/start",
    component: () => import("@/routes/selection.vue"),
  },
  {
    path: "/profile",
    component: () => import("@/routes/profile.vue"),
    beforeEnter(to, from, next) {
      if (!localStorage.getItem("user")) {
        next("/login");
      } else {
        next();
      }
    },
  },
  {
    path: "/form1",
    component: () => import("@/routes/first_form.vue"),
    beforeEnter(to, from, next) {
      if (!localStorage.getItem("user")) {
        next("/login");
      } else {
        next();
      }
    },
  },

  {
    path: "/form2",
    component: () => import("@/routes/second_form.vue"),
    meta: { requiredAuth: true },
    beforeEnter(to, from, next) {
      if (!localStorage.getItem("user")) {
        next("/login");
      } else {
        next();
      }
    },
  },

  {
    path: "/task1",
    component: () => import("@/routes/tasks/task1.vue"),
    meta: { requiredAuth: true },
    beforeEnter(to, from, next) {
      if (!localStorage.getItem("user")) {
        next("/login");
      } else {
        next();
      }
    },
  },
  {
    path: "/task2",
    component: () => import("@/routes/tasks/task2.vue"),
    meta: { requiredAuth: true },
    beforeEnter(to, from, next) {
      if (!localStorage.getItem("user")) {
        next("/login");
      } else {
        next();
      }
    },
  },
  {
    path: "/task3",
    component: () => import("@/routes/tasks/task3.vue"),
    meta: { requiredAuth: true },
    beforeEnter(to, from, next) {
      if (!localStorage.getItem("user")) {
        next("/login");
      } else {
        next();
      }
    },
  },
  {
    path: "/task4",
    component: () => import("@/routes/tasks/task4.vue"),
    meta: { requiredAuth: true },
    beforeEnter(to, from, next) {
      if (!localStorage.getItem("user")) {
        next("/login");
      } else {
        next();
      }
    },
  },
  {
    path: "/task5",
    component: () => import("@/routes/tasks/task5.vue"),
    meta: { requiredAuth: true },
    beforeEnter(to, from, next) {
      if (!localStorage.getItem("user")) {
        next("/login");
      } else {
        next();
      }
    },
  },
  {
    path: "/task6",
    component: () => import("@/routes/tasks/task6.vue"),
    meta: { requiredAuth: true },
    beforeEnter(to, from, next) {
      if (!localStorage.getItem("user")) {
        next("/login");
      } else {
        next();
      }
    },
  },
  {
    path: "/task7",
    component: () => import("@/routes/tasks/task7.vue"),
    meta: { requiredAuth: true },
    beforeEnter(to, from, next) {
      if (!localStorage.getItem("user")) {
        next("/login");
      } else {
        next();
      }
    },
  },
  {
    path: "/task8",
    component: () => import("@/routes/tasks/task8.vue"),
    meta: { requiredAuth: true },
    beforeEnter(to, from, next) {
      if (!localStorage.getItem("user")) {
        next("/login");
      } else {
        next();
      }
    },
  },
  {
    path: "/login",
    component: () => import("@/routes/login.vue"),
    meta: { requiredAuth: true },
  },
  {
    path: "/admin_panel",
    component: () => import("@/routes/admin_panel/panel.vue"),
  },
  {
    path: "/admin_panel/user/:id",
    component: () => import("@/routes/admin_panel/user.vue"),
  },
];

// 3. Create the router instance and pass the `routes` option
// You can pass in additional options here, but let's
// keep it simple for now.
const router = createRouter({
  // 4. Provide the history implementation to use. We are using the hash history for simplicity here.
  history: createWebHistory(),
  routes, // short for `routes: routes`
});

// routeConfig.beforeEach(async (to, from, next) => {
//   if (to.meta.requiredAuth) {
//     var userProfile = store.getters["auth/getUserProfile"];
//     if (userProfile.id === 0) {
//       await store.dispatch("auth/userProfile");
//       userProfile = store.getters["auth/getUserProfile"];
//       if (userProfile.id === 0) {
//         return next({ path: "/login" });
//       } else {
//         return next();
//       }
//     }
//   }
//   return next();
// });

export default router;
