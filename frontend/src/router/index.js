import Vue from 'vue'
import VueRouter from 'vue-router'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
import TalkView from '../views/TalkView.vue'

import store from '../store'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'talk',
    component: TalkView,
    beforeEnter(to, from, next){
      if(store.getters.isValid){
        next();
      }
      else{
        next('/login');
      }
    },
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView,
    beforeEnter(to, from, next){
      if(store.getters.isValid){
        next('/');
      }
      else{
        next();
      }
    },
  },
  {
    path: '/register',
    name: 'register',
    component: RegisterView,
    beforeEnter(to, from, next){
      if(store.getters.isValid){
        next('/');
      }
      else{
        next();
      }
    }
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
