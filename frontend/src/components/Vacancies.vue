<template>
<div class="layout">
  <div class="sidebar">
    <h3>Параметры поиска</h3>
    <hr>
  </div>
  <div class="content">
    <h3>Результаты поиска</h3>
    <hr>
    <div class="vacancy-list" v-for="vacancy in this.VACANCIES"
    :key="vacancy.id">
    <div class="card">
      <div class="card-header">
        Вакансия от компании {{vacancy.company}}
      </div>
      <div class="card-body">
        <h5 class="card-title">{{vacancy.summary}}</h5>
        <p class="card-text">Требования: {{vacancy.skills}}</p>
        <p class="card-text">Зарплата {{vacancy.price*1000}} {{vacancy.currency}}</p>
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
  components: {
    
  },
  computed: {
      ...mapGetters([
          'VACANCIES'
      ])
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
</style>