import './assets/main.css'

import { library } from '@fortawesome/fontawesome-svg-core'
import { faBookOpen, faCertificate, faStar, faDollarSign, faUsers } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(faBookOpen, faCertificate, faStar, faDollarSign, faUsers)

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

const app = createApp(App)
app.component('font-awesome-icon', FontAwesomeIcon)
app.use(createPinia())
app.use(router)

app.mount('#app')
