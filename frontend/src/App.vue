<template>
  <div id="app">
      <Navigation/>
      <router-view></router-view>
  </div>
</template>

<script>

import Navigation from '@/components/Navigation'

export default {
  name: 'App',
  components: {
    Navigation
  },
  data () {
    return {
      authenticated: false
    }
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=KoHo');
@font-face {
  font-family: "Literata";
  src: local("Literata"),
       url("./fonts/Literata/Literata-Regular.ttf");
}
#app {
  font-family: 'Literata', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
/* .users {
  width: 15%;
} */
h1 {
  font-weight: 400;
}
.text-header {
  padding: 25px 0px;
  background-color: #343a40;
  color: white;
}
</style>
