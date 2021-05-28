import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '@/router/index'

Vue.use(Vuex)


export default new Vuex.Store({
    state: {
        users: [],
        vacancies: [],
        username: null,
        token: null,
    },
    getters: {
        USERS(state) {
            return state.users
        },
        VACANCIES(state) {
            return state.vacancies
        },
        isAuthenticated(state) {
            return state.token != null
        }
    },
    mutations: {
        SET_USERS_TO_STORE: (state, users) => {
            state.users = users;
        },
        SET_VACANCY_TO_STORE: (state, vacancies) => {
            state.vacancies = vacancies;
        },
        authUser(state, userData) {
            state.username = userData.username;
            state.token = userData.token;
        },
        clearAuthData(state) {
            state.username = null;
            state.token = null;
        },        
    },
    actions: {
        FETCH_USERS({commit}) {
            console.log("i am here")
            return axios.get("http://localhost:5000/users")
                .then((users) => {
                    commit('SET_USERS_TO_STORE', users.data.message);
                    return users;
                })
                .catch((error) => {
                    console.log(error);
                    return error;
                })
        },
        FETCH_VACANCIES({commit}) {
            let token = localStorage.getItem('token')
            return axios.get("http://localhost:5000/vacancy",{ headers: {'Authorization': `Bearer ${token}`}})
                .then((vacancies) => {
                    commit('SET_VACANCY_TO_STORE', vacancies.data);
                    return vacancies;
                })
                .catch((error) => {
                    console.log(error);
                    return error
                })
        },
        login: ({commit}, authData) => {
            axios.post("http://localhost:5000/login", {
                username: authData.username,
                password: authData.password
            }).then(response => {
                console.log(response);
                let success = response.status;
                console.log(success);
                if (success === 200) {
                    commit('authUser', {username: authData.username, token: response.data.token})
                    localStorage.setItem('token', response.data.access_token)
                    localStorage.setItem('username', response.data.username)
                    router.replace('vacancy');
                } else {
                    console.log("Login error");
                }
            }).catch(error => {
                console.log(error);
            })
        },
        autoLogin({commit}) {
            let token = localStorage.getItem('token')
            let username = localStorage.getItem('username')

            if (!token || !username) {
                return
            }

            commit('authUser', {username: username, token: token})
        },
        logout: ({commit}) => {
            commit('clearAuthData')
            localStorage.removeItem('username');
            localStorage.removeItem('token');
            router.replace('login');            
        }
    }
})