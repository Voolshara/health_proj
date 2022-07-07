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
    path: "/form_selection",
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
    component: () => import("@/routes/task1.vue"),
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
