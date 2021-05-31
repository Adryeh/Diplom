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
        <a class="nav-link" href="" @click="$router.push('/users')">Пользователи</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="" @click="$router.push('/vacancy')">Вакансии</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="" @click="$router.push('/login')">Авторизация</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="" @click="$router.push('/register')">Регистрация</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="" @click="$router.push('/profile')">Профиль</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="" @click="logout">Выйти</a>
      </li>
    </ul>
    <span class="navbar-text">
      Navbar text with an inline element
    </span>
  </div>
</nav>
</template>

<script>
	
export default {
	name: 'Navigation',
  methods: {
    logout: function(){
      this.$store.dispatch('logout')
      .then(() => {
        this.$router.push('/login')
      })
    }
  }
}

</script>

<style scoped>
.navbar {
  margin-bottom: 25px; 
}
</style>