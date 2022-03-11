<template>
  <v-container>
    <v-row justify="space-around">
      <v-item-group>
        <v-item v-for="talk in talks" :key="talk.id">
          <v-card
          width="700px"
          class="my-4 pa-2"
          >
            <v-card-title primary-title>
              <h5>{{talk.send_by.name}}</h5>
            </v-card-title>
            <v-card-text>
              <p>{{talk.content}}</p>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <!-- <v-btn
              color="grey"
              class="white--text"
              v-if="userInfo.id == talk.send_by.id || userInfo.is_staff"
              >編集</v-btn> -->
              <v-btn
              color="red"
              class="white--text"
              v-if="userInfo.id == talk.send_by.id || userInfo.is_staff"
              @click="deleteTalk(talk.id)"
              >削除</v-btn>
            </v-card-actions>
          </v-card>
        </v-item>
      </v-item-group>
    </v-row>
    <v-card width="700px" class="mx-auto mt-5">
      <v-card-title primary-title>
        <h3>投稿フォーム</h3>
      </v-card-title>
      <v-card-text>
        <v-form>
          <v-textarea
            label="本文"
            v-model="content"
            type="text"
            auto-grow
            @keypress.enter="postTalk"
          ></v-textarea>
        </v-form>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn
        @click="postTalk"
        color="blue-grey darken-2"
        class="blue-grey--text text--lighten-5"
        :disabled="!contentExists"
        >送信</v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script>
import axios from '../axios-default'

export default {
  data(){
    return{
      talks:[],
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
    },
    contentExists(){
      return this.content !== ""
    }
  },
  methods:{
    getTalks(){
      axios.get('/api/talks/list/', this.requestHeader)
      .then(response => {
        this.talks = response.data;
      })
    },
    postTalk(){
      this.loading = true;
      const request = {
        send_by: this.userInfo.id,
        content: this.content,
      }
      axios.post('/api/talks/create/', request, this.requestHeader)
      .then(() => {
        this.getTalks();
      });
      this.content = "";
      this.loading = false;
    },
    deleteTalk(talkId){
      axios.delete('api/talks/'+talkId+'/edit/', this.requestHeader)
      .then(() => {
        this.getTalks();
      });
    }
  },
  created(){
    this.getTalks();
  }
}
</script>