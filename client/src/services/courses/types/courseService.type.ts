export interface Course {
  id: string | number
  title: string
  description: string
  instructor: string
}

export interface CourseCreateRequest {
  title: string
  description?: string
}

export type CourseUpdateRequest = Partial<CourseCreateRequest>
