import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'


Vue.use(Vuex)


export default new Vuex.Store({
    state: {
        users: []
    },
    getters: {
        USERS(state) {
            return state.users
        }
    },
    mutations: {
        SET_USERS_TO_STORE: (state, users) => {
            state.users = users;
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
        }
    }
})