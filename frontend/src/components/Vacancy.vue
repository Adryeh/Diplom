<template>
    <div class="wrap">
        <div class="vacancy_card">
            
            <h1>{{currentPageVacancy.name}}</h1>
            <p>Вакансия от компании {{companyData(currentPageVacancy.company_id)[0].name}} </p>
            <hr>
            <div class="vac-item salary">
                <h3>Зарплата:</h3>
                <span>{{currentPageVacancy.salary}} RUB</span>
            </div>
            <div class="vac-item req">
                <h3>Требования:</h3>
                <span>{{currentPageVacancy.requirements}}</span>
            </div>

            <div class="btn-list">
                <form @submit.prevent="addToFav(currentPageVacancy.id)">
                    <button  class="btn btn-outline-primary" v-if="currentUser_type=='employee' && !vacancyInFavs(currentPageVacancy.id) ">Откликнуться</button>
                </form>
                <form @submit.prevent="removeFromFav(currentPageVacancy.id)">
                    <button class="btn btn-outline-danger" v-if="currentUser_type=='employee' && vacancyInFavs(currentPageVacancy.id) ">Удалить отклик</button>
                </form>
            </div>

        </div>
    </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'

export default {
    data () {
        return {
            id: ''
        }
    },
    computed: {
        ...mapGetters([
            'isAuthenticated',
            'currentUser_type',
            'currentUser',
            'USERS',
            'COMPANIES',
            'VACANCIES',
            'currentCompany',
            'currentEmployee',
            'myFAVS'
        ]),
        currentPageVacancy: {
            get: function() {
                return this.VACANCIES.filter(v => v.id === parseInt(this.id))[0]
            }
        }
    },
    methods: {
        ...mapActions([
            'FETCH_USERS',
            'FETCH_SKILLS',
            'FETCH_COMPANIES',
            'FETCH_FAVORITE'
        ]),
        companyData(company_id) {
            return this.COMPANIES.filter( function(item) {
                if (item.id == company_id) {

                return item
                }
            })
        },
        addToFav(id) {
            console.log('ADD');
            const data = {
                vacancy_id: id,
                employee_id: this.currentEmployee.id
            }
            console.log('addToFav', data);
            this.$store.dispatch('addToFav', data)
        },
        removeFromFav(id) {
            console.log('DELETING', id);
            this.$store.dispatch('removeFromFav', id)
        },
        vacancyInFavs(id) {
            return this.myFAVS.includes(id)
        }
    },

    created() {
        this.id = this.$route.params.id;
    }
}
</script>

<style>
.vacancy_card {
    background-color: white;
    border: solid;
}
.vac-item {
    margin: 25px;
}
</style>