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
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=KoHo');

#app {
  font-family: 'KoHo', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  
}
.users {
  width: 15%;
}
body {
  margin: 0;
  padding: 0;
  border: solid red;
  height: 100%;
  background-color: #7e0f0f;
}
.text-header {
  padding: 25px 0px;
  background-color: #343a40;
  color: white;
}
</style>
