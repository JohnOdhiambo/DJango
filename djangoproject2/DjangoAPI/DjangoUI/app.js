import Vue from 'vue';
import VueRouter from 'vue-router';

// Use VueRouter
Vue.use(VueRouter);

const routes=[
    {path:'/home', component:home},
    {path:'/department', component:department},
    {path:'/employee', component:employee}
]

//Vue router objects; then pass the routes array
const router = new VueRouter({
    routes
})

//Create a vue object and mount to the element with id app
const app = new Vue({
    router
}).$mount('#app')