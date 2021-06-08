import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '@/router/index'
import createPersistedState from 'vuex-persistedstate'
import * as Cookies from 'js-cookie'

Vue.use(Vuex)

const token = localStorage.getItem('token')
const header = { 'Authorization': 'Bearer ' + token }

export default new Vuex.Store({
    plugins: [
        createPersistedState({
          getState: (key) => Cookies.getJSON(key),
          setState: (key, state) => Cookies.set(key, state, { expires: 3, secure: true })
        })],
    state: {
        status: '',
        users: [],
        vacancies: [],
        companies: [],
        username: null,
        token: localStorage.getItem('token') || '',
        user: {},
        currentUser_type: null,
        skills: []
    },
    getters: {
        USERS(state) {
            return state.users
        },
        VACANCIES(state) {
            return state.vacancies
        },
        COMPANIES(state) {
            return state.companies
        },
        SKILLS(state) {
            return state.skills
        },
        isAuthenticated: state => !!state.token,
        authStatus: state => state.status,
        currentUser: state => state.user,
        currentEmployee: state => state.user.employee_data,
        currentCompany: state => state.user.company_data,
        currentUser_type: state => state.currentUser_type
    },
    mutations: {
        SET_USERS_TO_STORE: (state, users) => {
            state.users = users;
        },
        SET_SKILLS_TO_STORE: (state, skills) => {
            state.skills = skills;
        },
        SET_VACANCY_TO_STORE: (state, vacancies) => {
            state.vacancies = vacancies;
        },
        SET_COMPANY_TO_STORE: (state, companies) => {
            state.companies = companies;
        },
        loginSuccess(state) {
            state.status = true
        },
        loginFailure(state) {
            state.status = false
        },
        logout(state) {
            state.status = false
        },
        registerSuccess(state) {
            state.status = false;
        },
        registerFailure(state) {
            state.status = false;
        },
        changeUserTypeToEmployee(state) {
            state.currentUser_type = 'employee'
        },
        changeUserTypeToCompany(state) {
            state.currentUser_type = 'company'
        },
        changeUserTypeToNone(state) {
            state.currentUser_type = ''
        },
        registerCompanySuccess(state) {
            state.currentUser_type = 'company'
        },
        registerEmployeeSuccess(state) {
            state.currentUser_type = 'employee'
        },
        // registerCompanyFailure(state) {
        //     state.currentUser_type = 'e'
        // },
        AUTH_REQUEST: (state) => {
            state.status = 'loading'
        },
        AUTH_SUCCESS: (state, user_data) => {
            console.log('MUTATION user', user_data);

            console.log('mutation token', user_data.access_token);
            state.status = 'success'
            state.token = user_data.access_token
            state.user = user_data
        },
        AUTH_ERROR: (state) => {
            state.status = 'error'
        },
        AUTH_LOGOUT: (state) => {
            state.token = ''
            state.user = ''
        }
    },
    actions: {
        FETCH_USERS({commit}) {
            console.log("i am here")
            return axios.get("employees")
                .then((users) => {
                    console.log(users);
                    commit('SET_USERS_TO_STORE', users.data);
                    return users;
                })
                .catch((error) => {
                    console.log(error);
                    return error;
                })
        },
        FETCH_SKILLS({commit}) {
            return axios.get("skill")
            .then((skills) => {
                commit('SET_SKILLS_TO_STORE', skills.data)
                return skills
            })
            .catch((error) => {
                console.log(error);
                return error
            })
        },
        FETCH_COMPANIES({commit}) {
            console.log('getting companies');
            return axios.get("company", { headers: header})
            .then((companies) => {
                console.log('COMPANIES', companies);
                commit('SET_COMPANY_TO_STORE', companies.data)
                return companies
            }).catch(error => {
                console.log(error);
                return error
            })
        },
        FETCH_VACANCIES({commit}) {
            console.log('here store');
            return axios.get("vacancy", { headers: header})
                .then((vacancies) => {
                    console.log('inside');
                    console.log(vacancies);
                    commit('SET_VACANCY_TO_STORE', vacancies.data);
                    return vacancies;
                })
                .catch((error) => {
                    console.log('err');
                    console.log(error);
                    return error
                })
        },
        login: ({commit}, authData) => {
            return new Promise((resolve, reject) => {
                commit('AUTH_REQUEST')
                axios.post('login', {
                    username: authData.username,
                    password: authData.password,
                    user_type: authData.user_type
                }).then(response => {
                    console.log('RESPONSE', response.data);
                    const user_data = response.data.user
                    console.log('login user', user_data);
                    localStorage.setItem('token', user_data.access_token)
                    commit('AUTH_SUCCESS', user_data)
                    resolve(response)
                    if (user_data.user_type == 'employee') {
                        commit('changeUserTypeToEmployee')
                        router.push('/')
                    } else if (user_data.user_type == 'company') {
                        commit('changeUserTypeToCompany')
                        router.push('/')
                    } else {
                        router.push('/register/user_type')
                        commit('changeUserTypeToNone')
                    }

                    // dispatch('USER_REQUEST')

                }).catch(err => {
                    
                    commit('AUTH_ERROR')
                    localStorage.removeItem('token')
                    reject(err)
                })
            })
        },
        logout: ({commit}) => {
            return new Promise((resolve) => {
                commit('AUTH_LOGOUT')
                localStorage.removeItem('token')
                resolve()
            })
        },
        register: ({commit}, registerData) => {
            console.log('debug action',registerData);
            axios.post('register', {
                username: registerData.username,
                password: registerData.password,
                user_type: registerData.userType
            })
            .then(response => {
                console.log(response);
                commit('registerSuccess')
            }).catch(error =>{
                console.log(error);
                commit('registerFailure')
            })
        },
        createVacancy: ({commit}, vacancyData) => {
            console.log('createVacancy');
            axios.post('vacancy', {
                company_id: vacancyData.company_id,
                name: vacancyData.name,
                requirements: vacancyData.requirements,
                salary: vacancyData.salary
            }, { headers: header})
            .then(response => {
                console.log('createVacancy response', response);
                commit('')
                
            }).catch(error => {
                console.log(error);
                commit('')
            })
        },
        createSkill: ({commit}, skillData) => {
            axios.post('skill', {
                skill_name: skillData.skill_name,
                skill_progress: skillData.skill_progress,
                employee_id: skillData.employee_id
            }, { headers: header})
            .then(resp => {
                commit('')
                return resp
            })
            .catch(err => {
                console.log(err);
                return err
            })
        },
        deleteSkill: ({commit}, id) => {
            axios.post('skill/delete', {
                id: id
            }, { headers: header})
            .then(resp => {
                commit('')
                return resp
            })
            .catch(err => {
                console.log(err);
                return err
            })
        },
        register_company: ({commit}, registerData) => {
            console.log('debug action',registerData);
            axios.post('company', {
                user_id: registerData.user_id,
                name: registerData.name,
                location: registerData.location,
                number_of_employees: registerData.number_of_employees
            })
            .then(response => {
                console.log(response);
                router.push('/profile')
                commit('')
            }).catch(error =>{
                console.log(error);
                console.log('Company register failed');
                // commit('registerCompanyFailure')
            })
        },
        register_employee: ({commit}, registerData) => {
            console.log('debug action',registerData);
            axios.post('register/employee', {
                user_id: registerData.user_id,
                first_name: registerData.first_name,
                last_name: registerData.last_name,
                education: registerData.education,
                gender: registerData.gender,
                age: registerData.age,
                citizenship: registerData.citizenship,
                position: registerData.position
            })
            .then(response => {
                console.log(response);
                router.push('/profile')
                commit('')
            }).catch(error =>{
                console.log(error);
                console.log('Employee register failed');
                // commit('registerCompanyFailure')
            })
        }        
    }
})