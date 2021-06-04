<template>
  <div class="layer">
    <div class="row">
      <div class="col-md-6 offset-md-3 col-xl-4 offset-xl-4">
      <form @submit.prevent="onSubmit()">
        <div class="form-group">
          <input type="text" placeholder="username" v-model="username" name="" class="form-control">
        </div>
        <div class="form-group">
          <input type="password" placeholder="password" v-model="password" name="" class="form-control">
        </div>

        <button type="submit" class="btn btn-primary">Register</button>
      </form>

      <hr>

    




      </div>
    </div>

  </div>  
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: '',
      isEmployee: '',
      user_type: ''
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
    },
    onChange(event) {
      console.log(event.target.value);
    }
  },
  computed: {
    
  }
}
</script>

<style>
#identity-check {
  margin-left: 15px;
  margin-top: 25px;
}

.register__user-type {
  margin-top: 50px;
}
</style>  