import './assets/main.css'

import { library } from '@fortawesome/fontawesome-svg-core'
import { faBookOpen, faCertificate, faStar, faDollarSign, faUsers, faCalendar, faEnvelope, faUserShield, faTasks, faCreditCard, faHeart, faComments, faTrophy, faChartBar } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(faBookOpen, faCertificate, faStar, faDollarSign, faUsers, faCalendar, faEnvelope, faUserShield, faTasks, faCreditCard, faHeart, faComments, faTrophy, faChartBar)

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

const app = createApp(App)
app.component('font-awesome-icon', FontAwesomeIcon)
app.use(createPinia())
app.use(router)

app.mount('#app')
