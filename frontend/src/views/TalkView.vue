<template>
  <div>
  <TalkPanel></TalkPanel>
  <TalkForm></TalkForm>
  </div>
</template>

<script>
import TalkPanel from '../components/TalkPanel.vue'
import TalkForm from '../components/TalkForm.vue'

export default {
  components:{
    TalkPanel,
    TalkForm,
  }
}
</script>