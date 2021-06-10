
<template>
	<div class="row">
		<div class="col-md-6 offset-md-3 col-xl-4 offset-xl-4">
			<form>
				<div class="form-group">
					<label>Username</label>
					<input v-model="username" type="text" class="form-control" placeholder="Username">
				</div>
				<div class="form-group">
					<label>Password</label>
					<input v-model="password" type="password" class="form-control" placeholder="Password">
				</div>
				<label>Тип пользователя</label>
				<select v-model="user_type" class="custom-select" aria-label=".form-select-sm example">
					<option value="Работодатель" selected>Работодатель</option>
					<option value="Работник">Работник</option>
				</select>	
				<div v-if="invalidCredentials" class="form-group">
					<small class="text-danger">Invalid credentials</small>
				</div>
				<button type="submit" @click.prevent="onSubmit" class="btn btn-primary">Login</button>
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
				user_type: '',
				invalidCredentials: false,
			}
		},
		methods: {
			onSubmit() {
				let formData = {
					username: this.username,
					password: this.password,
					user_type: this.user_type
				}
				console.log('form', formData);
				this.$store.dispatch('login', formData).then((response) => {
					const user_data = response.data.user
					if (user_data.user_type == 'employee') {	
                        this.$store.commit('changeUserTypeToEmployee')
						this.$store.commit('SET_EMPLOYEE_DATA', user_data.employee_data)
                        this.$router.push('/')
                    } else if (user_data.user_type == 'company') {
                        this.$store.commit('changeUserTypeToCompany')
						this.$store.commit('SET_COMPANY_DATA', user_data.company_data)
                        this.$router.push('/')
                    } else {
                        this.$router.push('/register/user_type')
                        this.$store.commit('changeUserTypeToNone')
                    }
				}).catch(err => {
					console.log(err);
					this.$router.push('/register');
				})
			}
		}
	}
</script>
