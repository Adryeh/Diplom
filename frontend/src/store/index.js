import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'


Vue.use(Vuex)


export default new Vuex.Store({
    state: {
        users: [],
        vacancies: []
    },
    getters: {
        USERS(state) {
            return state.users
        },
        VACANCIES(state) {
            return state.vacancies
        }
    },
    mutations: {
        SET_USERS_TO_STORE: (state, users) => {
            state.users = users;
        },
        SET_VACANCY_TO_STORE: (state, vacancies) => {
            state.vacancies = vacancies;
        }
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
            return axios.get("http://localhost:5000/vacancy")
                .then((vacancies) => {
                    commit('SET_VACANCY_TO_STORE', vacancies.data);
                    return vacancies;
                })
                .catch((error) => {
                    console.log(error);
                    return error
                })
        }
    }
})