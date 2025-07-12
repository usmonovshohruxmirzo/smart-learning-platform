import axios, { Axios, AxiosError, type AxiosResponse } from 'axios'

const api: Axios = axios.create({
  baseURL: 'http://localhost:5173',
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
})

api.interceptors.request.use(
  (config) => {
    const token: string | null = localStorage.getItem('accessToken')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (error: AxiosError) => {
    return Promise.reject(error)
  },
)

api.interceptors.response.use(
  (response: AxiosResponse) => response,
  (error: AxiosError) => {
    if (error.response && error.response.status === 401) {
      console.error('Unauthorized! Redirecting...')
    }
    return Promise.reject()
  },
)

export default api
