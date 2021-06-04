<template>
<div class="layout">
      <h1>{{currentUser.username}}'s profile</h1>
	{{currentUser.user_object.id}}
	<div class="register__user-type">
		<div class="row">
		<div class="col-md-6 offset-md-3 col-xl-4 offset-xl-4">
			<label>Выберите тип пользователя</label><br>
			<select class="select-type" v-model="user_type" @change="onChange($event)">
				<option>Работодатель</option>
				<option>Работник</option>
			</select>
			<form class="form-layout" v-if="user_type=='Работодатель'" @submit.prevent="registerCompany()">
				<div class="form-group">
					<label >Название компании</label>
					<input type="text" class="form-control" v-model="company.name">
				</div>
				<div class="form-group">
					<label>Адрес</label>
					<input type="text" class="form-control" v-model="company.location">
				</div>
				<div class="form-group">
					<label >Количество сотрудников</label>
					<input type="text" class="form-control" v-model="company.number_of_employees">
				</div>
				<button class="btn btn-primary">Submit</button>
			</form>

			<!-- else -->

			<form class="form-layout" v-if="user_type=='Работник'" @submit.prevent="registerCompany()">
				<div class="form-group">
					<label >Имя</label>
					<input type="text" class="form-control" v-model="employee.first_name">
				</div>
				<div class="form-group">
					<label>Фамилия</label>
					<input type="text" class="form-control" v-model="employee.last_name">
				</div>
				<div class="form-group">
					<label >Образование</label>
					<input type="text" class="form-control" v-model="employee.education">
				</div>
				<div class="form-group">
					<label >Пол</label>
					<input type="text" class="form-control" v-model="employee.gender">
				</div>
				<div class="form-group">
					<label >Возраст</label>
					<input type="text" class="form-control" v-model="employee.age">
				</div>
				<div class="form-group">
					<label >Гражданство</label>
					<input type="text" class="form-control" v-model="employee.citizenship">
				</div>
				<button class="btn btn-primary">Submit</button>
			</form>

			<!-- else end -->
			</div>
		</div>
	</div>
</div>
</template>

<script>
import {mapGetters} from 'vuex'

export default {
	data () {
		return {
			user_type: '',
			company: {
				number_of_employees: '',
				location: '',
				name: ''
			},
			employee: {
				first_name: '',
				last_name: '',
				education: '',
				gender: '',
				age: '',
				citizenship: ''

			}

		}
	},
	methods: {
		onChange(event) {
			console.log(event.target.value);
			
		},
		registerCompany() {
			const companyData = {
				user_id: this.currentUser.user_object.id,
				name: this.company.name,
				location: this.company.location,
				number_of_employees: this.company.number_of_employees
			}
			console.log(companyData);
			this.$store.dispatch('register_company', companyData).then(() => {
			// this.$router.push('/login');
			});
		}
	},
	computed: {
		...mapGetters([
			'isAuthenticated',
			'currentUser'
		])
    }
}
</script>

<style>
.form-layout {
	padding: 50px;
	box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
}
.select-type {
	margin: 15px;
}
</style>