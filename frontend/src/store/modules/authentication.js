import axios from '../../axios-default'
import router from '../../router'

const state = {
  JWT: null,
  isValid: false,
  userInfo:{}
};

const getters = {
  JWT: state => state.JWT,
  requestHeader(state){
    return {
      headers:{
        Authorization: "JWT "+ state.JWT
      }
    }
  },
  isValid: state => state.isValid,
  userInfo: state => state.userInfo
};

const mutations = {
  setJWT(state, JWT){
    state.JWT = JWT;
  },
  setIsValid(state, isValid){
    state.isValid = isValid;
  },
  setUserInfo(state, userInfo){
    state.userInfo = userInfo;
  },
};

const actions = {
  //localStrageとstoreにJWTを保存
  setJWT({commit}, JWT){
    localStorage.setItem('JWT', JWT);
    commit('setJWT', JWT);
  },

  //localStrageとstoreからJWTを除去
  removeJWT({commit}){
    localStorage.removeItem('JWT');
    commit('setJWT', null);
    commit('setIsValid', false);
  },
  
  //emailとパスワードを送信することで、JWTを入手する。
  async obtainJWT({commit, dispatch}, authData){
    await axios.post('/api-token-obtain/', authData)
    .then(response => {
      if(response.status == 200){
        dispatch('setJWT', response.data.token);
        commit('setIsValid', true);
      }
      else{
        commit('setIsValid', false);
      }
    })
    .catch(error => {
      console.log(error);
    });
  },

  //JWTをリフレッシュ
  async refreshJWT({commit, dispatch}){
    const request = {
      token: localStorage.getItem('JWT'),
    }
    await axios.post('/api-token-refresh/', request)
    .then(response => {
      if(response.status == 200){
        dispatch('setJWT', response.data.token);
        commit('setIsValid', true);
      }
      else{
        commit('setIsValid', false);
      }
    })
    .catch(error => {
      console.log(error);
    });
  },

  //JWTを認証し、有効であるかをisValid内に格納
  async verifyJWT({commit}){
    const request = {
      token: localStorage.getItem('JWT'),
    }
    await axios.post('/api-token-verify/', request)
    .then(response => {
      if(response.status == 200){
        commit('setIsValid', true);
      }
      else{
        commit('setIsValid', false);
      }
    });
  },

  //ユーザ情報の取得
  obtainUserInfo({getters, commit}){
    axios.get('/api/users/myinfo/', getters.requestHeader)
    .then(response => {
      const userInfo = response.data
      commit('setUserInfo', userInfo);
    })
    .catch(error => {
      console.log(error);
    });
  },

  //ログイン時の処理
  async login({dispatch}, authData){
    await dispatch('obtainJWT', authData);
    dispatch('obtainUserInfo');
    router.push('/')
    .catch(()=>{});
  },

  //自動ログイン処理
  async autoLogin({getters, commit, dispatch}){
    if(!localStorage.getItem('JWT')){
      return;
    }
    else{
      commit('setJWT', localStorage.getItem('JWT'));
    }
    
    await dispatch('verifyJWT');
    if(getters.isValid){
      await dispatch('refreshJWT');
      dispatch('obtainUserInfo');
      router.push('/')
      .catch(()=>{});
    }
    else{
      router.push('/login')
      .catch(()=>{});
    }
  },

  //ログアウト処理
  async logout({commit, dispatch}){
    await dispatch('removeJWT');
    commit('setUserInfo', {});
    router.push('/login')
    .catch(()=>{});
  },

  //会員登録処理
  async register({dispatch}, registerData){
    await axios.post('/api/users/register/', registerData)
    .then(() => {
      const loginRequest = {
        email: registerData.email,
        password: registerData.password,
      }
      dispatch('login', loginRequest);
    });
  }
}

export default {
  state,
  getters,
  mutations,
  actions,
}