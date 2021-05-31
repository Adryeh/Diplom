<template>
	<div class="">
		<h1>Main Page</h1>
		<h2 v-if="isAuthenticated">Hello, {{currentUser.username}}</h2>

	</div>
</template>

<script>
import {mapGetters} from 'vuex'


export default {
	computed: {
		...mapGetters([
			'isAuthenticated',
			'currentUser'
		]),
		user() {
			return this.$store.state.user
		}
	}
}
</script>