<template>
	<div class="">
		<h1>Main Page</h1>
		<h2 v-if="isAuthenticated">Hello, {{currentUser.user_object.username}}, {{currentUser_type}}, {{currentUser.company_data}}</h2>

	</div>
</template>

<script>
import {mapGetters} from 'vuex'


export default {
	computed: {
		...mapGetters([
			'isAuthenticated',
			'currentUser',
			'currentUser_type'
		]),
		user() {
			return this.$store.state.user
		}
	}
}
</script>