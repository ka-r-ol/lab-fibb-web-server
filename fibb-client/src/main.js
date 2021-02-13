import Vue from 'vue'
import Vuex from 'vuex'
import App from './App.vue'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import Cookies from 'js-cookie'

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(Vuex)

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
//import axios from "axios";

Vue.config.productionTip = false

const store = new Vuex.Store({
  state: {},
  mutations: {
    // store.commit('set_contact_params', {fname:"?", lname:"?", email:"?"})
    set_contact_params(state) {
      Cookies.set('fib_fname', state.fname)
      Cookies.set('fib_lname', state.lname)
      Cookies.set('fib_email', state.email)
    }
  }
}
)

new Vue({
  store,
  mounted() {
    //Cookies.set("test", "to jest testowe ciasteczko")

    store.state.BASE_API_URL = "http://127.0.0.1:8000/api/v1/"
    store.state.fname = Cookies.get('fib_fname')
    store.state.lname = Cookies.get('fib_lname')
    store.state.email = Cookies.get('fib_email')
    console.log("Ciasteczka = ", Cookies.get())
    console.log("Store = ", store.state)
  },

  render: h => h(App),
}).$mount('#app')
