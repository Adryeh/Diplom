<template>
<!-- <nav class="navbar navbar-dark bg-dark">
  <li><a @click="$router.push('/users')">Users</a></li>
</nav> -->
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <a class="navbar-brand" href="" @click="$router.push('/')">FindJob</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarText">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link" href="" @click="$router.push('/')">Домой <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" v-if="isAuthenticated" href="" @click="$router.push('/users')">Кандидаты</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" v-if="isAuthenticated" href="" @click="$router.push('/vacancy')">Вакансии</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" v-if="isAuthenticated && currentUser_type=='employee'" href="" @click="$router.push({name: 'user', params: {'id': currentEmployee.id}})">Моё резюме</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" v-if="isAuthenticated && currentUser_type=='employee'" href="" @click="$router.push('/favorite')">Избранные вакансии</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="" v-if="!isAuthenticated" @click="$router.push('/login')">Авторизация</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="" v-if="!isAuthenticated" @click="$router.push('/register')">Регистрация</a>
      </li>
      <!-- <li class="nav-item">
        <a class="nav-link" href="" v-if="isAuthenticated" @click="$router.push('/profile')">Профиль</a>
      </li> -->
      <li class="nav-item">
        <a class="nav-link" v-if="isAuthenticated" href="" @click="logout">Выйти</a>
      </li>
    </ul>
    
    <span v-if="isAuthenticated" class="navbar-text">

      <span class="user-data">Пользователь: {{currentUser.user_object.username}}</span>
      <span class="user-data"><span v-if="currentUser_type=='employee'">Имя: {{currentEmployee.first_name}} </span><span v-if="currentUser_type=='company'">Компания: {{currentCompany.name}}</span> </span>
      <span class="user-data">Роль: <span v-if="currentUser_type=='employee'">Работник</span><span v-if="currentUser_type=='company'">Работодатель</span></span>
    </span>
  </div>
</nav>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'	
export default {
	name: 'Navigation',
  methods: {
    logout: function(){
      this.$store.dispatch('logout')
      .then(() => {
        this.$router.push('/login')
      })
    },
    ...mapActions([
      'FETCH_USERS',
      'FETCH_SKILLS',
      'FETCH_COMPANIES'
    ]),
  },
  mounted() {
    this.FETCH_COMPANIES(),
    this.FETCH_USERS()
  },
  computed: {
    ...mapGetters([
          'isAuthenticated',
          'currentUser_type',
          'currentUser',
          'USERS',
          'COMPANIES',
          'currentCompany',
          'currentEmployee'
    ]),
    getEmployeeData() {
      return this.USERS.filter(item => {
        console.log('ITEM', item);
        console.log('item.user_id', item.user_id, 'this.currentUser.user_object.id', this.currentUser.user_object.id);
          if (item.user_id == this.currentUser.user_object.id) {
            console.log('adfASFASF', item);
            return item
          }
      })
    },
    getCompanyData() {
      console.log(this.COMPANIES);
      return this.COMPANIES.filter(item => {
        console.log('item.user_id', item.user_id);
        console.log('this.currentUser.user_object.id', this.currentUser.user_object.id);
        if (item.user_id == this.currentUser.user_object.id) {
          return item
        }
      })
    }
  }
}

</script>

<style scoped>
.navbar {
  margin-bottom: 25px; 
}
.user-data {
  margin-right: 25px;
}
</style>