<template>
    <form action="" >
      <input type="text" v-model="searchQuery" placeholder="Название вакансии">
    </form>
</template>

<script>
export default {
    data() {
        return {
            searchQuery: ''
        }
    }
}
</script>

<style>
.body {
    border: solid;
}
</style>