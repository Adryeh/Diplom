import Vue from 'vue'
import App from './App.vue'
import router from '@/router/index'
import VueRouter from 'vue-router'
import BootstrapVue from "bootstrap-vue"
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap-vue/dist/bootstrap-vue.css"
import store from '@/store/index'
import '@/assets/css/main.css'
import './axios'


Vue.config.productionTip = false
Vue.use(VueRouter)
Vue.use(BootstrapVue)


new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
