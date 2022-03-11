<template>
  <v-card width="400px" class="mx-auto mt-5">
    <v-card-title primary-title>
      <h3>ログイン</h3>
    </v-card-title>
    <v-card-text>
      <v-form v-model="isValid">
        <v-text-field
          label="メールアドレス"
          v-model="email"
          type="email"
          :rules="[rules.required, rules.isMailAddress]"
          prepend-icon="mdi-email"
        ></v-text-field>
        <v-text-field
          label="パスワード"
          v-model="password"
          :type="passwordVisible? 'text':'password'"
          :rules="[rules.required, rules.lengthMoreThan6]"
          @keypress.enter="login"
          prepend-icon="mdi-lock"
          :append-icon="passwordVisible? 'mdi-eye':'mdi-eye-off'"
          @click:append="passwordVisible = !passwordVisible"
        ></v-text-field>
      </v-form>
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn 
        @click="login"
        color="blue-grey darken-2"
        class="blue-grey--text text--lighten-5"
        :disabled="!isValid || loading"
      >ログイン</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import sweetAlert from 'sweetalert2'

export default {
  data(){
    return {
      email: "",
      password: "",
      passwordVisible: false,
      rules:{
        required: input => !!input || "必須です。",
        lengthMoreThan6: input => input.length >= 6 || "6文字以上でなければいけません。",
        isMailAddress: input => input.includes('@') || "メールアドレスを入力してください。",
      },
      isValid: false,
      loading: false,
    }
  },
  methods:{
    async login(){
      this.loading = true;
      const authData = {
        email: this.email,
        password: this.password,
      };
      await this.$store.dispatch('login', authData);
      if(!this.$store.getters.isValid){
        sweetAlert.fire({
          title: 'ログインできませんでした',
          text: 'メールアドレスもしくはパスワード、又は両方が間違っています。',
          showConfirmButton: true,
        });
      }
      this.loading = false;
    }
  },
}
</script>