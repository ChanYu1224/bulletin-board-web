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
              <v-btn
              color="grey"
              class="white--text"
              v-if="$store.getters.userInfo.id == talk.send_by.id || isStaff"
              >編集</v-btn>
              <v-btn
              color="red"
              class="white--text"
              v-if="$store.getters.userInfo.id == talk.send_by.id || isStaff"
              @click="deleteTalk(talk.id)"
              >削除</v-btn>
            </v-card-actions>
          </v-card>
        </v-item>
      </v-item-group>
    </v-row>
  </v-container>
</template>

<script>
import axios from '../axios-default'

export default {
  data(){
    return{
      talks:[],
    }
  },
  computed:{
    isStaff(){
      return this.$store.getters.userInfo.is_staff;
    }
  },
  methods:{
    getTalks(){
      axios.get('/api/talks/list/', this.$store.getters.requestHeader)
      .then(response => {
        this.talks = response.data;
      })
    },
    deleteTalk(talkId){
      axios.delete('api/talks/'+talkId+'/edit/', this.$store.getters.requestHeader)
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