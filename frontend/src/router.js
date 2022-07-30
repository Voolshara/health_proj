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
    path: "/form1",
    component: () => import("@/routes/first_form.vue"),
  },

  {
    path: "/form2",
    component: () => import("@/routes/second_form.vue"),
  },

  {
    path: "/task1",
    component: () => import("@/routes/tasks/task1.vue"),
  },
  {
    path: "/task2",
    component: () => import("@/routes/tasks/task2.vue"),
  },
  {
    path: "/task3",
    component: () => import("@/routes/tasks/task3.vue"),
  },
  {
    path: "/task4",
    component: () => import("@/routes/tasks/task4.vue"),
  },
  {
    path: "/task5",
    component: () => import("@/routes/tasks/task5.vue"),
  },
  {
    path: "/task6",
    component: () => import("@/routes/tasks/task6.vue"),
  },
  {
    path: "/task7",
    component: () => import("@/routes/tasks/task7.vue"),
  },
  {
    path: "/task8",
    component: () => import("@/routes/tasks/task8.vue"),
  },
  {
    path: "/login",
    component: () => import("@/routes/login.vue"),
  },
  {
    path: "/admin_panel",
    component: () => import("@/routes/admin_panel/panel.vue"),
    /*beforeEnter: (to, from, next) => {
      const isLoggedIn = !!Userfront.tokens.accessToken;
      if (to.name === "Dashboard" && !isLoggedIn) {
        return next({ path: "/login" });
      }

      next();
    },*/
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

export default router;
