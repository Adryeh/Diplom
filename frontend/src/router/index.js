import VueRouter from "vue-router"
import Users from '@/components/Users'
import Main from '@/components/Main'
import Test from '@/components/Test'
import UserInfo from '@/components/UserInfo'
// import Navigation from '@/components/Navigation'


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
            name: 'info',
            component: UserInfo
        }
	]
})