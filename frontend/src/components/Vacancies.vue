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
    <h3 class="text-header">Список вакансий</h3>

    <div class="vacancy-list" v-for="vacancy in resultQuery"
    :key="vacancy.id">
    <div class="card">
      <div class="card-header">
        Вакансия от компании {{vacancy.company}}
      </div>
      <div class="card-body">
        <h5 class="card-title">Должность: {{vacancy.summary}}</h5>
        <p class="card-text">Требования: {{vacancy.skills}}</p>
        <p class="card-text">Зарплата: {{vacancy.price*1000}} {{vacancy.currency}}</p>
        <a href="#" class="btn btn-outline-primary">Подробнее о вакансии</a>
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
      searchQuery: null
    }
  },
  components: {
    
  },
  computed: {
      ...mapGetters([
          'VACANCIES'
      ]),
      resultQuery(){
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
    this.FETCH_VACANCIES()

  },
  methods: {
    ...mapActions([
        'FETCH_VACANCIES'
    ])
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
</style>