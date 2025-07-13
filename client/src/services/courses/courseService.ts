import type { AxiosInstance, AxiosResponse } from 'axios'
import type { Course, CourseCreateRequest, CourseUpdateRequest } from './types/courseService.type'
import axios from 'axios'

const API_BASE = '/api/courses/'

interface HttpClient {
  get<T>(url: string, config?: unknown): Promise<AxiosResponse<T>>
  post<T>(url: string, data: unknown, config?: unknown): Promise<AxiosResponse<T>>
  put<T>(url: string, data: unknown, config?: unknown): Promise<AxiosResponse<T>>
  delete<T>(url: string, config?: unknown): Promise<AxiosResponse<T>>
}

class CourseService {
  private readonly http: HttpClient

  constructor(httpClient: HttpClient) {
    this.http = httpClient
  }

  async getCourses(params?: Record<string, string | number>): Promise<Course[]> {
    try {
      const res = await this.http.get<Course[]>(API_BASE, { params })
      return res.data
    } catch (error) {
      throw this.handleError(error, 'Failed to fetch courses')
    }
  }

  async getCourse(id: string): Promise<Course> {
    try {
      const res = await this.http.get<Course>(`${API_BASE}/${id}`)
      return res.data
    } catch (error) {
      throw this.handleError(error, `Failed to fetch course with ID ${id}`)
    }
  }

  async createCourse(data: CourseCreateRequest): Promise<Course> {
    try {
      const res = await this.http.post<Course>(API_BASE, data)
      return res.data
    } catch (error) {
      throw this.handleError(error, 'Failed to create course')
    }
  }

  async updateCourse(id: string, data: CourseUpdateRequest): Promise<Course> {
    try {
      const res = await this.http.put<Course>(`${API_BASE}/${id}`, data)
      return res.data
    } catch (error) {
      throw this.handleError(error, `Failed to update course with ID ${id}`)
    }
  }

  async deleteCourse(id: string): Promise<void> {
    try {
      await this.http.delete(`${API_BASE}/${id}`)
    } catch (error) {
      throw this.handleError(error, `Failed to delete course with ID ${id}`)
    }
  }

  private handleError(error: unknown, message: string): Error {
    if (error instanceof Error && 'response' in error) {
      if (axios.isAxiosError(error)) {
        return new Error(
          `${message}: ${error.response?.status} - ${error.response?.data?.message || error.message}`,
        )
      }
    }
    return new Error(`${message}: ${error instanceof Error ? error.message : 'Unknown error'}`)
  }
}

export const createCourseService = (httpClient: AxiosInstance) => new CourseService(httpClient)
