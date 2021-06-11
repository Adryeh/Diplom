<template>
	<div class="">
		<h2>Это мой диплом</h2>
		
	</div>
</template>

<script>
import {mapGetters} from 'vuex'


export default {
	computed: {
		...mapGetters([
			'isAuthenticated',
			'currentUser',
			'currentUser_type',
			'currentCompany'
		]),
		user() {
			return this.$store.state.user
		}
	}
}
</script>