<template>
    <div class="card mb-3" style="max-width: 540px;" @click="$router.push({name:'users', query: {'id': user_data.id}})">
      <div class="row g-0">
        <div class="col-md-4">
          <img class="user-picture" src="@/assets/default.png" alt="...">
        </div>
        <div class="col-md-8">
          <div class="card-body">
            <h5 class="card-title">{{user_data.name}}</h5>
            <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
            <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
          </div>
        </div>
      </div>
      <UserInfo/>
    </div>
</template>

<script>
import UserInfo from '@/components/UserInfo'
	export default {
		name: 'User',
    components: {
      UserInfo
    },
		props: {
			user_data: {
				type: Object,
				default: () => {}
			}
		},
		methods: {
			toUserInfo() {
				this.$emit('to-user-info')
			}

		}
	}
</script>

<style scoped>
.users-wrapper {
    border: solid;
    width: 20%;
}
.user-picture {
    width: 100%;
    height: 15vw;
    object-fit: cover;
}
.card {
  border: solid red;
}
</style>