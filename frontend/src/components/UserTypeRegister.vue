<template>
  <div class="layout">
    <select v-model="user_type" class="custom-select" aria-label=".form-select-sm example">
        <option value="" selected disabled>Выберите тип пользователя</option>
        <option value="Работодатель" selected>Работодатель</option>
        <option value="Работник">Работник</option>
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
        <form class="form-layout" v-if="user_type=='Работник'" @submit.prevent="registerEmployee()">
            <div class="form-group">
                <label >Имя</label>
                <input type="text" class="form-control" v-model="employee.first_name">
            </div>
            <div class="form-group">
                <label>Фамилия</label>
                <input type="text" class="form-control" v-model="employee.last_name">
            </div>
            <div class="form-group">
                <label>Специальность</label>
                <input type="text" class="form-control" v-model="employee.position">
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
				citizenship: '',
                position: ''

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
		},
		registerEmployee() {
			const employeeData = {
                user_id: this.currentUser.user_object.id,
                first_name: this.employee.first_name,
                last_name: this.employee.last_name,
                education: this.employee.education,
                gender: this.employee.gender,
                age: this.employee.age,
                citizenship: this.employee.citizenship,
                position: this.employee.position
			}
			console.log(employeeData);
			this.$store.dispatch('register_employee', employeeData).then(() => {
			// this.$router.push('/login');
			});
		}
	},
	computed: {
		...mapGetters([
			'isAuthenticated',
			'currentUser',
			'currentUser_type'
		])
    }
}
</script>

<style>
.form-layout {
	padding: 50px;

}
.select-type {
	margin: 15px;
}
</style>