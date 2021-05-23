<template>
  <div class="layer">
    <h1>Login Page</h1>
    <form action="" @submit.prevent="login">
        <input type="text" name="" id="" v-model="username">
        <input type="text" name="" id="" v-model="password">
    </form>
  </div>
</template>

<script>
export default {
  name: 'login',
  data() {
      return {
          username: '',
          password: ''
      }
  },
  methods: {
      login() {
          this.$store.dispatch('retrieveToken', {
              username: this.username,
              password: this.password
          })
      }
  }
}
</script>

<style>

</style>