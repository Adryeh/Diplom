import VueRouter from "vue-router"
import Users from '@/components/Users'
import Main from '@/components/Main'
import Test from '@/components/Test'
import User from '@/components/User'
import Vacancies from '@/components/Vacancies'


export default new VueRouter({
	mode: 'history',
	routes: [
		{
            path: '/',
            name: 'main',
            component: Main
		},
        {
            path: '/users',
            name: 'users',
            component: Users
        },
        {
            path: '/test',
            name: 'test',
            component: Test
        },
        {
            path: '/users/:id',
            name: 'user',
            component: User
        },
        {
            path: '/vacancy',
            name: 'vacancy',
            component: Vacancies
        }
	]
})