<template>
<div class="layout">

  <!-- <div class="sidebar">
    <h3 class="text-header">Параметры поиска</h3>

    <form action="" class="form_job-title">
      <input type="text" name="form_job-title" id="form_job-title" v-model="searchQuery" placeholder="Название вакансии">
    </form>
    
  </div> -->
  <form action="" class="vacancies-menu">
    <button class="btn_new-vacancy btn btn-dark" v-if="currentUser_type=='company'" @click="$router.push('/vacancy/create')">Новая вакансия</button>
    <input type="text" class="inp_find-vacancy form-control" v-model="searchQuery" placeholder="Название вакансии">
  </form>
  <div class="content">
    
    <h3 class="text-header">Список вакансий</h3>
    <div class="vacancy-list" v-for="vacancy in resultQuery"
    :key="vacancy.id">
    <div class="card">
      <div class="card-header">
        Вакансия от компании {{companyData(vacancy.company_id)[0].name}} 
      </div>
      <div class="card-body">
        <h5 class="card-title">Должность: {{vacancy.name}}</h5>
        <p class="card-text">Требования: {{vacancy.requirements}}</p>
        <p class="card-text">Зарплата: {{vacancy.salary}} RUB</p>
        <!-- <form @submit.prevent="addToFav(vacancy.id)">
          <button  class="btn btn-outline-primary" v-if="currentUser_type=='employee' && !vacancyInFavs(vacancy.id) ">Откликнуться</button>
        </form>
        <form @submit.prevent="removeFromFav(vacancy.id)">
          <button class="btn btn-outline-danger" v-if="currentUser_type=='employee' && vacancyInFavs(vacancy.id) ">Удалить отклик</button>
        </form> -->
        <a class="btn btn-outline-primary" @click="$router.push({name: 'vacancy', params: {'id': vacancy.id}})">Подробнее</a>
      </div>
    </div>
    </div>
    
  </div>


</div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'


export default {
  name: 'Vacancies',
  data() {
    return {
      searchQuery: null,
      IDs: []
    }
  },
  components: {
    
  },
  computed: {
      ...mapGetters([
          'VACANCIES',
          'COMPANIES',
          'currentCompany',
          'currentUser',
          'currentEmployee',
          'currentUser_type',
          'FAVS',
          'myFAVS'
      ]),
      myFavs() {
        console.log('myFavs', this.FAVS);
        return this.FAVS.filter((item) => {
            console.log('ITEM', item.employee_id, this.currentEmployee.id);
            if (item.employee_id == this.currentEmployee.id) {
                return item
            }
        })
      },
      myFavsIDS() {
        console.log('here');
        let arr = this.myFavs
        console.log('arr', this.myFavs);
        let ids = []
        for (let i = 0; i < arr.length; i++) {
          console.log('arr[i]', arr[i])
          ids.push(arr[i].vacancy_id)
          
        }
        return ids
      },
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
            return this.searchQuery.toLowerCase().split(' ').every(v => item.name.toLowerCase().includes(v))

          })
        } else {
          return this.VACANCIES
        }
      }
  },
  mounted() {
    
    this.FETCH_COMPANIES(),
    this.FETCH_VACANCIES(),
    this.FETCH_FAVORITE()


  },
  methods: {
    ...mapActions([
        'FETCH_VACANCIES',
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
    // createVacancy() {
    //   const vacancy_data = {

    //   }

    // },
  }
}
</script>

<style scoped>

.layout {

}
/* .sidebar {
  width: 15%;
  margin-top: 3%;
  margin-left: 5%;
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
  transition: 0.3s;
  height: 80vh;
  position: fixed;
  z-index: 1;
  background-color: white;
} */

.content {
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
  transition: 0.3s;

  margin: 0 auto;
  margin-top: 50px;
}

.card {
  margin-top: 15px;
}
.inp_find-vacancy {
  width: 500px;
  margin-left: 15px;
}

.btn_new-vacancy{
  align-self: flex-start;
}

.sidebar-title {
  margin: 15px 0px;
  border: solid red;

}
.vacancies-menu {
  display: flex;
  /* border: solid 1px; */
  padding: 15px;
  border-radius: 5px;
  margin: 5px;
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
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