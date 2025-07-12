import './assets/main.css'

import { library } from '@fortawesome/fontawesome-svg-core'
import {
  faBookOpen,
  faCertificate,
  faStar,
  faDollarSign,
  faUsers,
  faCalendar,
  faEnvelope,
  faUserShield,
  faTasks,
  faCreditCard,
  faHeart,
  faComments,
  faTrophy,
  faChartBar,
  faListUl,
} from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(
  faBookOpen,
  faCertificate,
  faStar,
  faDollarSign,
  faUsers,
  faCalendar,
  faEnvelope,
  faUserShield,
  faTasks,
  faCreditCard,
  faHeart,
  faComments,
  faTrophy,
  faChartBar,
  faListUl,
)

import { createApp } from 'vue'

import App from './App.vue'
import router from './router'
import pinia from './stores'

const app = createApp(App)
app.component('font-awesome-icon', FontAwesomeIcon)
app.use(pinia)
app.use(router)

app.mount('#app')
