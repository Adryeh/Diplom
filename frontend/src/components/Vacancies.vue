<template>
<div class="layout">

  <div class="sidebar">
    <h3 class="text-header">Параметры поиска</h3>

    <form action="" class="form_job-title">
      <input type="text" name="form_job-title" id="form_job-title" v-model="searchQuery" placeholder="Название вакансии">
    </form>
    
    <div class="employment-type">
      <h6 class="sidebar-title">Тип занятости</h6>
      <ul class="type-list-group">
        <li>Full-Time<span class="badge badge-primary badge-pill">1</span></li>
        <li>Part-Time<span class="badge badge-primary badge-pill">3</span></li>
        <li>Remote<span class="badge badge-primary badge-pill">11</span></li>
      </ul>
    </div>
  </div>
  <div class="content">
  <div class="vac">
    <h1>VACANCIES</h1>
    {{this.VACANCIES}}
  </div>
  <br>
  <div class="com">
    <h1>COMPANIES</h1>
    {{this.COMPANIES}}
  </div>
  data
  {{currentCompany}}
  user
  {{currentUser}}
    <form action="" class="vacancies-menu">
      <button class="btn btn-dark"  @click="$router.push('/vacancy/create')">Новая вакансия</button>
    </form>
    <h3 class="text-header">Список вакансий</h3>

    <div class="vacancy-list" v-for="vacancy in resultQuery"
    :key="vacancy.id">
    <div class="card">
       {{companyData(vacancy.company_id)}} 
      <div class="card-header">
        Вакансия от компании {{companyData(vacancy.company_id)[0].name}} 
      </div>
      <div class="card-body">
        <h5 class="card-title">Должность: {{vacancy.name}}</h5>
        <p class="card-text">Требования: {{vacancy.requirements}}</p>
        <p class="card-text">Зарплата: {{vacancy.salary}}</p>
        <a href="#" class="btn btn-outline-primary">Подробнее о вакансии</a>
        <button type="button" class="btn btn-danger" v-if="currentCompany.id==vacancy.company_id">Удалить</button>
      </div>
    </div>
    </div>
    
  </div>
 <!-- {{this.COMPANIES}} -->

</div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'


export default {
  name: 'Vacancies',
  data() {
    return {
      searchQuery: null
    }
  },
  components: {
    
  },
  computed: {
      ...mapGetters([
          'VACANCIES',
          'COMPANIES',
          'currentCompany',
          'currentUser'
      ]),
      // currentUserCompany() {
      //   console.log(currentUser);
      // },
      // companyData() {
      //   return this.COMPANIES.filter((item) => {
      //     return item.id == 4
      //   })
      // },
      resultQuery() {
        if (this.searchQuery) {
          return this.VACANCIES.filter((item)=>{
            return this.searchQuery.toLowerCase().split(' ').every(v => item.summary.toLowerCase().includes(v))

          })
        } else {
          return this.VACANCIES
        }
      }
  },
  mounted() {
    
    this.FETCH_COMPANIES(),
    this.FETCH_VACANCIES()


  },
  methods: {
    ...mapActions([
        'FETCH_VACANCIES',
        'FETCH_COMPANIES'
    ]),
    companyData(company_id) {
      return this.COMPANIES.filter( function(item) {
        console.log('company_id', company_id);
        console.log('ITEM', item);
        if (item.id == company_id) {
          console.log('item.company_id', item.company_id);
          return item
        }
      })
    },
    createVacancy() {
      const vacancy_data = {

      }
      console.log('vacancy_data', vacancy_data);
    }
  }
}
</script>

<style scoped>

.layout {
  display: flex;
  flex-direction: row;
}
.sidebar {
  width: 15%;
  margin-top: 3%;
  margin-left: 5%;
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
  transition: 0.3s;
  height: 80vh;
  position: fixed;
  z-index: 1;
  background-color: white;
}

.content {
  width: 60%;
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
  transition: 0.3s;
  margin-top: 3%;
  margin-left: 25%;
}

.card {
  margin-top: 15px;
}

.type-list-group {
  border: solid red;
  list-style: none;
  text-align: left;
}
.sidebar-title {
  margin: 15px 0px;
  border: solid red;

}
.vacancies-menu {
  display: flex;
  padding: 25px;
  justify-content: flex-end;
}
.vac{
  border: solid red;
}
.com {
  border: solid red;
}
.btn-danger {
  
}
</style>