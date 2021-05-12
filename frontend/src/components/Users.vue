<template>
  <div>
    <User 
    v-for="(user) in this.USERS" 
    :key="user.id"
    :user_data="user"
    @to-user-info="toUserInfo(user)"/>

  </div>
</template>


<script>
import {mapActions, mapGetters} from 'vuex'
import User from '@/components/User'

export default {
  name: 'Users',
  components: {
    User
  },
  computed: {
      ...mapGetters([
          'USERS'
      ])
  },  
  data: () => ({
    users: null
  }),
  mounted() {

    this.FETCH_USERS()

  },
  methods: {
    toUserInfo(user) {
        this.$router.push({
          name: 'users',
          query: {'id': user.id}
        })
      },
    ...mapActions([
        'FETCH_USERS'
    ])
  }
}
</script>


<style scoped>

</style>
