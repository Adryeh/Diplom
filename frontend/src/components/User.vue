<template>
<div>
    {{currentUser}}
</div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'


export default {
    name: 'User',
    data() {
        return {
            user_info: null,
            id: null
        }
    },
    computed: {
        ...mapGetters([
            'USERS'
         ]),
         currentUser: {
             get: function() {
                 console.log("lo");
                 return this.USERS.filter(user => user.id === parseInt(this.id))[0]
             }
         }
    },
    methods: {
        ...mapActions([
            'FETCH_USERS'
        ])
    },
    mounted() {
        this.FETCH_USERS()
    },
    created() {
        this.id = this.$route.params.id;
    }
}
</script>
<style scoped>

</style>