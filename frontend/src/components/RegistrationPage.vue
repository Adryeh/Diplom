<template>
  <div class="row">
    <div class="col-md-6 offset-md-3 col-xl-4 offset-xl-4">
    <form @submit.prevent="onSubmit()">
      <div class="form-group">
        <input type="text" placeholder="username" v-model="username" name="" class="form-control">
      </div>
      <div class="form-group">
        <input type="password" placeholder="password" v-model="password" name="" class="form-control">
      </div>
      <select class="form-control" v-model="userType" aria-label="Default select example">
        <option value="1">Работадатель</option>
        <option value="2">Работник</option>
      </select>
      <button type="submit" class="btn btn-primary">Register</button>
    </form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: '',
      userType: ''
    }
  },
  methods: {
    onSubmit() {
      const registerData = {
        username: this.username,
        password: this.password,
        userType: this.userType
      }
      console.log(registerData);
      this.$store.dispatch('register', registerData).then(() => {
        this.$router.push('/login');
      });
    }
  }
}
</script>

<style>

</style>  