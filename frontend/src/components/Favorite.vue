<template>
    <div class="">
        <h1>Избранные вакансии</h1>
            <div class="" v-for="f in this.myFAVS" :key="f.id">
                <div class="card">
                    <div class="card-header">
                        Вакансия от компании {{companyData(getVacancyData(f)[0].company_id)[0].name}} 
                    </div>
                    <div class="card-body">
                        <h5 class="card-title">Должность: {{getVacancyData(f)[0].name}}</h5>
                        <p class="card-text">Требования: {{getVacancyData(f)[0].requirements}}</p>
                        <p class="card-text">Зарплата: {{getVacancyData(f)[0].salary}} RUB</p>
                    </div>
                    <a class="btn btn-outline-primary" @click="$router.push({name: 'vacancy', params: {'id': getVacancyData(f)[0].id}})">Подробнее</a>
                </div>
                    
            </div>
            
        </div>

</template>

<script>
import {mapActions, mapGetters} from 'vuex'	
export default {
    name: 'Favorite',
    methods: {
        ...mapActions([
        'FETCH_USERS',
        'FETCH_SKILLS',
        'FETCH_COMPANIES',
        'FETCH_FAVORITE'
        ]),
        getVacancyData(id) {
            return this.VACANCIES.filter(item => {
                if (item.id == id) {
                    return item
                }
            })
        },
        companyData(company_id) {
            return this.COMPANIES.filter( function(item) {
                if (item.id == company_id) {

                return item
                }
            })
        }
    },
    mounted() {
        this.FETCH_COMPANIES(),
        this.FETCH_USERS(),
        this.FETCH_FAVORITE()
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
        ])
    }
}

</script>

<style>

</style>