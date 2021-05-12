<template>
	<div>
		{{user_info}}
		<button @click="checkUsers"></button>
	</div>
</template>
<script>
import {mapActions, mapGetters} from 'vuex'
export default {
name: 'UserInfo',
data(){
	return {
		user_info: {}
	}
},
computed: {
	...mapGetters([
		'USERS'
	])
},
methods: {
	...mapActions([
		'FETCH_USERS'
	]),
	checkUsers() {
		console.log("len", this.USERS.length)
		if (!this.USERS.length) {
			this.FETCH_USERS()
			.then(() => {
				this.toUserInfo()
			})
		} else {
			this.toUserInfo()
		}
	},
	toUserInfo() {
		this.USERS.map((user) => {
			if (user.id === this.user_info.id) {
				this.$router.push({
					name: 'user',
					params: {'user': user.name},
					query: {'id': this.user_info.id}
				}).catch(()=>{});
			}
		})
	}
},
mounted() {
	
	this.USERS.find((user) => {
		console.log("mounted", user)
		if (user.id === this.$route.query.id) {
			console.log("mounted user id", user.id)
			console.log("mounted query id", this.$route.query.id)
			this.user_info = user
			console.log("mounted user_info", this.user_info)
		} else {
			console.log("kik")
		}
	})
	
}
}
</script>
