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
body {
  background-color: #f39189;
}
#app {
  font-family: 'Fira Sans', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-color: #e9e9e9;
}
.users {
  width: 15%;
}
body {
  margin: 0;
  padding: 0;
}
</style>
