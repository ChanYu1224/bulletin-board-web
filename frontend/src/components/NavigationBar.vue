<template>
  <v-app-bar color="blue-grey darken-2"
  elevate-on-scroll
  app
  >
    <v-toolbar-title
    class="blue-grey--text text--lighten-5"
    >かなりふつうの掲示板</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-btn
    class="mx-2"
    text
    color="blue-grey lighten-5"
    v-if="isAuthenticated"
    >{{userName}}</v-btn>
    <v-btn
    class="mx-2"
    text
    color="blue-grey lighten-5"
    v-if="isAuthenticated"
    @click="logout"
    >ログアウト</v-btn>
    <v-btn
    class="mx-2"
    text
    color="blue-grey lighten-5"
    v-if="!isAuthenticated"
    @click="toRegisterView"
    >会員登録</v-btn>
    <v-btn
    class="mx-2"
    text
    color="blue-grey lighten-5"
    v-if="!isAuthenticated"
    @click="toLoginView"
    >ログイン</v-btn>
  </v-app-bar>
</template>

<script>
import router from '../router'

export default {
  computed:{
    isAuthenticated(){
      return this.$store.getters.isValid;
    },
    userName(){
      return this.$store.getters.userInfo.name;
    }
  },
  methods:{
    logout(){
      this.$store.dispatch('logout');
    },
    toLoginView(){
      if(this.$route.path !== '/login'){
        router.push('/login');
      }
    },
    toRegisterView(){
      if(this.$route.path !== '/register'){
        router.push('/register');
      }
    }
  }
}
</script>