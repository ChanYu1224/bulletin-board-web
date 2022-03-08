<template>
  <v-app>
    <NavigationBar></NavigationBar>
    <v-main app>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>
import NavigationBar from './components/NavigationBar.vue'
export default {
  components:{
    NavigationBar,
  }
}
</script>
