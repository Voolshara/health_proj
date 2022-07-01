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
    path: "/form1",
    component: () => import("@/routes/first_form.vue"),
  },
  {
    path: "/form2",
    component: () => import("@/routes/second_form.vue"),
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
