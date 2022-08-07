// store/index.js
import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export function isValidJwt(jwt) {
  if (!jwt || jwt.split(".").length < 3) {
    return false;
  }
  const data = JSON.parse(atob(jwt.split(".")[1]));
  const exp = new Date(data.exp * 1000); // JS deals with dates in milliseconds since epoch
  const now = new Date();
  return now < exp;
}

const actions = {
  // asynchronous operations

  login(context, userData) {
    context.commit("setUserData", { userData });
    return authenticate(userData)
      .then((response) => context.commit("setJwtToken", { jwt: response.data }))
      .catch((error) => {
        console.log("Error Authenticating: ", error);
      });
  },
  register(context, userData) {
    context.commit("setUserData", { userData });
    return register(userData)
      .then(context.dispatch("login", userData))
      .catch((error) => {
        console.log("Error Registering: ", error);
      });
  },
};

const mutations = {
  // isolated data mutations
  setUserData(state, payload) {
    console.log("setUserData payload = ", payload);
    state.userData = payload.userData;
  },
  setJwtToken(state, payload) {
    console.log("setJwtToken payload = ", payload);
    localStorage.token = payload.jwt.token;
    state.jwt = payload.jwt;
  },
};

const getters = {
  // reusable data accessors
  isAuthenticated(state) {
    return isValidJwt(state.jwt.token);
  },
};

const store = new Vuex.Store({
  state,
  actions,
  mutations,
  getters,
});

export default store;
