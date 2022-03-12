<template>
  <v-card width="400px" class="mx-auto mt-5">
    <v-card-title primary-title>
      <h3>会員登録</h3>
    </v-card-title>
    <v-card-text>
      <v-form v-model="isValid">
        <v-text-field
        label="ユーザー名"
        v-model="name"
        :rules="[rules.required]"
        prepend-icon="mdi-account-circle"
        ></v-text-field>
        <v-text-field
        label="登録メールアドレス"
        v-model="email"
        type="email"
        :rules="[rules.required, rules.isMailAddress]"
        prepend-icon="mdi-email"
        
        ></v-text-field>
        <v-text-field
        label="パスワード"
        v-model="password"
        type="password"
        :rules="[rules.required, rules.lengthMoreThan6]"
        prepend-icon="mdi-lock"
        ></v-text-field>
        <v-text-field
        label="パスワード（確認）"
        v-model="passwordForCheck"
        type="password"
        :rules="[rules.required, rules.lengthMoreThan6, rules.isSamePassword]"
        prepend-icon="mdi-lock"
        ></v-text-field>
        <v-textarea
        label="プロフィール"
        v-model="profile"
        type="text"
        :rules="[rules.lengthLessThan200]"
        counter="200"
        outlined
        auto-grow
        ></v-textarea>
      </v-form>
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn 
      @click="register"
      color="blue-grey darken-2"
      class="blue-grey--text text--lighten-5"
      :disabled="!isValid || loading"
      >会員登録</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import sweetAlert from 'sweetalert2'

export default {
  data(){
    return {
      name: "",
      email: "",
      password: "",
      passwordForCheck: "",
      profile: "",
      rules:{
        required: input => !!input || "必須です。",
        lengthMoreThan6: input => input.length >= 6 || "6文字以上でなければいけません。",
        isMailAddress: input => input.includes('@') || "メールアドレスを入力してください。",
        isSamePassword: input => input === this.password || "パスワードが一致していません。",
        lengthLessThan200: input => input.length <= 200 || "200文字以内で入力してください。"
      },
      isValid: false,
      loading: false,
    }
  },
  computed:{
    registerRequest(){
      return {
        name: this.name,
        email: this.email,
        password: this.password,
        profile: this.profile,
      }
    },
    loginRequest(){
      return {
        email: this.email,
        password: this.password,
      }
    },
  },
  methods:{
    register(){
      this.loading = true;
      this.$store.dispatch('register', this.registerRequest)
      .then(() => {
        if(!this.$store.getters.isValid){
          sweetAlert.fire({
            title: '会員登録に失敗しました。',
            text: '正しく情報が入力されていないか、既に登録されているメールアドレスです。',
            showConfirmButton: true,
          });
        }
      });
      this.loading = false;
    }
  },
}
</script>