<template>
    <div>
        <h1>Test Page</h1>
        <span>{{this.USERS}}</span>
    </div>
</template>

<script>

import {mapActions, mapGetters} from 'vuex'

export default {
    name: 'Test',
    computed: {
        ...mapGetters([
            'USERS'
        ])
    },
    methods: {
        ...mapActions([
            'FETCH_USERS'
        ])
    },
    mounted() {
        this.FETCH_USERS()
    }
}
</script>