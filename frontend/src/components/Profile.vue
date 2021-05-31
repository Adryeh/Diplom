<template>
  <div class="layout">
      <h1>{{currentUser.username}}'s profile</h1>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'

export default {
	computed: {
		...mapGetters([
			'isAuthenticated',
			'currentUser'
		])
    }
}
</script>

<style>

</style>