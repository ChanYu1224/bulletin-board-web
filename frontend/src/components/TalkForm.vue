<template>
  <v-card width="700px" class="mx-auto mt-5">
    <v-card-title primary-title>
      <h3>投稿</h3>
    </v-card-title>
    <v-card-text>
      <v-form>
        <v-textarea
          label="本文"
          v-model="content"
          type="text"
          auto-grow
        ></v-textarea>
      </v-form>
    </v-card-text>
    <v-card-actions>
      <v-btn @click="sendMessage">送信</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import axios from '../axios-default'

export default {
  data(){
    return{
      content: "",
      loading: false,
    }
  },
  computed:{
    userInfo(){
      return this.$store.getters.userInfo
    },
    requestHeader(){
      return this.$store.getters.requestHeader
    }
  },
  methods:{
    sendMessage(){
      this.loading = true;
      const request = {
        send_by: this.userInfo.id,
        content: this.content,
      }
      axios.post('/api/talks/create/', request, this.requestHeader);
      this.content = "";
      this.loading = false;
    }
  }
}
</script>