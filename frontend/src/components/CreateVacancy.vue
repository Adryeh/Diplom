<template>
  <div class="layout">
      <h2>Новая вакансия</h2>
    <div class="row">
        <div class="col-md-6 offset-md-3 col-xl-4 offset-xl-4">
            <form @submit.prevent="createVacancy()">
            <div class="form-group">
                <label>Название</label>
                <input class="form-control" v-model="name">
            </div>
            <div class="form-group">
                <label>Требования</label>
                <input class="form-control" v-model="requirements">
            </div>
            <div class="form-group">
                <label>Зарплата</label>
                <input class="form-control" v-model="salary">
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
            </form>
        </div>
    </div>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'

export default {
    data() {
        return {
            name: '',
            requirements: '',
            salary: ''     
        }
    },
    computed: {
      ...mapGetters([
          'VACANCIES',
          'COMPANIES',
          'currentCompany',
          'currentUser'
      ]),
  },
  methods: {
      createVacancy() {
          const vacancyData = {
              company_id: this.$store.getters.currentCompany.id,
              name: this.name,
              requirements: this.requirements,
              salary: this.salary
          }
          console.log('VACANCY CREATION FORM', vacancyData);
          this.$store.dispatch('createVacancy', vacancyData)
      }
  }
}
</script>

<style>

</style>