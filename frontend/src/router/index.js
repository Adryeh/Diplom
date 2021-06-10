import VueRouter from "vue-router"
import Users from '@/components/Users'
import Main from '@/components/Main'
import Test from '@/components/Test'
import User from '@/components/User'
import Vacancies from '@/components/Vacancies'
import LoginPage from '@/components/LoginPage'
import RegistrationPage from '@/components/RegistrationPage'
import Profile from '@/components/Profile'
import UserTypeRegister from '@/components/UserTypeRegister'
import CreateVacancy from '@/components/CreateVacancy'
import Favorite from '@/components/Favorite'
import Vacancy from '@/components/Vacancy'

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
            name: 'vacancies',
            component: Vacancies
        },
        {
            path: '/vacancy/:id',
            name: 'vacancy',
            component: Vacancy
        },
        {
            path: '/login',
            name: 'login',
            component: LoginPage

        },
        {
            path: '/register',
            name: 'register',
            component: RegistrationPage
        },
        {
            path: '/profile',
            name: 'profile',
            component: Profile
        },
        {
            path: '/register/user_type',
            name: 'registerType',
            component: UserTypeRegister
        },
        {
            path: '/vacancy/create',
            name: 'createVacancy',
            component: CreateVacancy
        },
        {
            path: '/favorite',
            name: 'favorite',
            component: Favorite
        }
	]
})