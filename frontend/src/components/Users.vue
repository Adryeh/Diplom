<template>

  <div id="users-component">
  <h1 class="text-header">Список пользователей</h1>
  {{this.USERS}}
  <div class="user-sorting-menu">
    <label for="sort-select">Sort by: </label>
    <select id="sort-select">
      <option>Alphabetic</option>
      <option>Other</option>
    </select>
  </div>
    <div class="user-list" 
    v-for="user in this.USERS"
    :key="user.id">
    
    <div class="flex-container">
    <div class="card">
      <img v-if="user.gender == 'М'" src="@/assets/avatar.png" alt="Avatar" style="width:100%">
      <img v-else src="@/assets/female.png" alt="Avatar" style="width:100%">
      <div class="container">
        <h4><b>{{user.first_name}}</b></h4> 
        <p></p> 
        
      </div>
    </div>

    <div class="description-container">
      <span class="user-description_item"><b>Полное имя:</b> {{user.first_name}}</span>
      <span class="user-description_item"><b>Пол:</b> {{user.gender}}</span>
      <span class="user-description_item"><b>Должность: </b> {{user.position}}</span>
      <span class="user-description_item"><b>Гражданство:</b> {{user.citizenship}}</span>
      <hr>
      <span class="user-description_item"><b>Краткая информация:</b> </span>
    </div>
    <button type="button" class="check-more_link btn btn-outline-primary" @click="$router.push({name: 'user', params: {'id': user.id}})">Резюме</button>
    </div>
    </div>
    
  </div>
</template>


<script>
import {mapActions, mapGetters} from 'vuex'

export default {
  name: 'Users',
  components: {
    
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
    ...mapActions([
        'FETCH_USERS'
    ])
  }
}
</script>


<style scoped>
#checkboxes {
  border: solid red;
  display: flex;
  justify-content: center;
  align-content: center;
}

#checkboxes ul {
  display: flex;
  list-style: none;
}

#checkboxes ul li {
  margin: 0px 25px;
}

a {
  text-decoration: none;
}
.check-more_link {
  align-self: flex-end;
  width: 10%;
  margin: 25px;
}
.card {
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
  transition: 0.3s;
  width: 15%;
}

.card:hover {
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
}

.container {
  padding: 2px 16px;
  
}
.user-list {
  display: flex;
  flex-direction:row;
  align-items: flex-start;
  width: 80%;
  margin: 0 auto;

}
.flex-container {
  display: flex;
  width: 100%;
  margin: 10px 0px;
  background-color: white;
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
}
.description-container {
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  text-align: left;
  padding: 15px;
  width: 75%;
}
.user-description_item{
  
}
#sort-select {
  margin-left: 10px;
}
#users-component {
  margin-top: 3%;
}
.user-sorting-menu{
  margin-top: 3%;
}
</style>
