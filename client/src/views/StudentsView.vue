<template>
  <div class="w-full">
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-2xl font-bold text-gray-800">Students</h1>
      <button
        @click="showAddModal = true"
        class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors"
      >
        Add Student
      </button>
    </div>

    <div v-if="loading" class="text-center py-8">
      <div class="text-gray-500">Loading students...</div>
    </div>
    
    <div v-else-if="error" class="text-center py-8">
      <div class="text-red-500">{{ error }}</div>
    </div>

    <div v-else class="bg-white rounded-lg shadow overflow-hidden">
      <div class="overflow-x-auto">
        <table class="min-w-full divide-y divide-gray-200">
          <thead class="bg-gray-50">
            <tr>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Name
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Email
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Phone
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Enrollment Date
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Status
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Actions
              </th>
            </tr>
          </thead>
          <tbody class="bg-white divide-y divide-gray-200">
            <tr v-for="student in students" :key="student.id" class="hover:bg-gray-50">
              <td class="px-6 py-4 whitespace-nowrap">
                <div class="flex items-center">
                  <div class="flex-shrink-0 h-10 w-10">
                    <div class="h-10 w-10 rounded-full bg-blue-100 flex items-center justify-center">
                      <span class="text-blue-600 font-semibold text-sm">
                        {{ student.first_name.charAt(0) }}{{ student.last_name.charAt(0) }}
                      </span>
                    </div>
                  </div>
                  <div class="ml-4">
                    <div class="text-sm font-medium text-gray-900">
                      {{ student.first_name }} {{ student.last_name }}
                    </div>
                    <div class="text-sm text-gray-500">
                      ID: {{ student.id }}
                    </div>
                  </div>
                </div>
              </td>
              <td class="px-6 py-4 whitespace-nowrap">
                <div class="text-sm text-gray-900">{{ student.email }}</div>
              </td>
              <td class="px-6 py-4 whitespace-nowrap">
                <div class="text-sm text-gray-900">{{ student.phone_number || 'N/A' }}</div>
              </td>
              <td class="px-6 py-4 whitespace-nowrap">
                <div class="text-sm text-gray-900">
                  {{ formatDate(student.enrollment_date) }}
                </div>
              </td>
              <td class="px-6 py-4 whitespace-nowrap">
                <span
                  :class="[
                    'inline-flex px-2 py-1 text-xs font-semibold rounded-full',
                    student.is_active
                      ? 'bg-green-100 text-green-800'
                      : 'bg-red-100 text-red-800'
                  ]"
                >
                  {{ student.is_active ? 'Active' : 'Inactive' }}
                </span>
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm font-medium">
                <button
                  @click="editStudent(student)"
                  class="text-blue-600 hover:text-blue-900 mr-3"
                >
                  Edit
                </button>
                <button
                  @click="deleteStudent(student.id)"
                  class="text-red-600 hover:text-red-900"
                >
                  Delete
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      
      <div v-if="students.length === 0" class="text-center py-12">
        <div class="text-gray-500 text-lg">No students found</div>
        <div class="text-gray-400 text-sm mt-2">Add your first student to get started</div>
      </div>
    </div>

    <div v-if="showAddModal || editingStudent" class="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto h-full w-full z-50">
      <div class="relative top-20 mx-auto p-5 border w-96 shadow-lg rounded-md bg-white">
        <div class="mt-3">
          <h3 class="text-lg font-medium text-gray-900 mb-4">
            {{ editingStudent ? 'Edit Student' : 'Add New Student' }}
          </h3>
          <form @submit.prevent="saveStudent">
            <div class="space-y-4">
              <div>
                <label class="block text-sm font-medium text-gray-700">First Name</label>
                <input
                  v-model="form.first_name"
                  type="text"
                  required
                  class="mt-1 block w-full border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:ring-blue-500 focus:border-blue-500"
                />
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700">Last Name</label>
                <input
                  v-model="form.last_name"
                  type="text"
                  required
                  class="mt-1 block w-full border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:ring-blue-500 focus:border-blue-500"
                />
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700">Email</label>
                <input
                  v-model="form.email"
                  type="email"
                  required
                  class="mt-1 block w-full border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:ring-blue-500 focus:border-blue-500"
                />
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700">Phone Number</label>
                <input
                  v-model="form.phone_number"
                  type="tel"
                  class="mt-1 block w-full border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:ring-blue-500 focus:border-blue-500"
                />
              </div>
              <div v-if="editingStudent">
                <label class="flex items-center">
                  <input
                    v-model="form.is_active"
                    type="checkbox"
                    class="rounded border-gray-300 text-blue-600 focus:ring-blue-500"
                  />
                  <span class="ml-2 text-sm text-gray-700">Active</span>
                </label>
              </div>
            </div>
            <div class="flex justify-end space-x-3 mt-6">
              <button
                type="button"
                @click="closeModal"
                class="px-4 py-2 text-sm font-medium text-gray-700 bg-gray-100 rounded-md hover:bg-gray-200"
              >
                Cancel
              </button>
              <button
                type="submit"
                class="px-4 py-2 text-sm font-medium text-white bg-blue-600 rounded-md hover:bg-blue-700"
              >
                {{ editingStudent ? 'Update' : 'Add' }}
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, reactive } from 'vue'

interface Student {
  id: number
  first_name: string
  last_name: string
  email: string
  phone_number?: string
  enrollment_date: string
  is_active: boolean
}

const students = ref<Student[]>([])
const loading = ref(false)
const error = ref('')
const showAddModal = ref(false)
const editingStudent = ref<Student | null>(null)

const form = reactive({
  first_name: '',
  last_name: '',
  email: '',
  phone_number: '',
  is_active: true
})

const mockStudents: Student[] = [
  {
    id: 1,
    first_name: 'John',
    last_name: 'Doe',
    email: 'john.doe@example.com',
    phone_number: '+1 (555) 123-4567',
    enrollment_date: '2024-01-15T10:30:00Z',
    is_active: true
  },
  {
    id: 2,
    first_name: 'Jane',
    last_name: 'Smith',
    email: 'jane.smith@example.com',
    phone_number: '+1 (555) 987-6543',
    enrollment_date: '2024-02-20T14:45:00Z',
    is_active: true
  },
  {
    id: 3,
    first_name: 'Mike',
    last_name: 'Johnson',
    email: 'mike.johnson@example.com',
    phone_number: '+1 (555) 456-7890',
    enrollment_date: '2024-03-10T09:15:00Z',
    is_active: false
  }
]

const fetchStudents = async () => {
  loading.value = true
  error.value = ''
  
  try {
    await new Promise(resolve => setTimeout(resolve, 1000))
    students.value = mockStudents
  } catch (err) {
    error.value = 'Failed to load students'
    console.error('Error fetching students:', err)
  } finally {
    loading.value = false
  }
}

const formatDate = (dateString: string) => {
  return new Date(dateString).toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric'
  })
}

const editStudent = (student: Student) => {
  editingStudent.value = student
  form.first_name = student.first_name
  form.last_name = student.last_name
  form.email = student.email
  form.phone_number = student.phone_number || ''
  form.is_active = student.is_active
}

const deleteStudent = async (id: number) => {
  if (confirm('Are you sure you want to delete this student?')) {
    try {
      await new Promise(resolve => setTimeout(resolve, 500))
      students.value = students.value.filter(student => student.id !== id)
    } catch (err) {
      console.error('Error deleting student:', err)
    }
  }
}

const saveStudent = async () => {
  try {
    if (editingStudent.value) {
      const index = students.value.findIndex(s => s.id === editingStudent.value!.id)
      if (index !== -1) {
        students.value[index] = {
          ...editingStudent.value,
          ...form
        }
      }
    } else {
      const newStudent: Student = {
        id: Math.max(...students.value.map(s => s.id)) + 1,
        first_name: form.first_name,
        last_name: form.last_name,
        email: form.email,
        phone_number: form.phone_number,
        enrollment_date: new Date().toISOString(),
        is_active: true
      }
      students.value.push(newStudent)
    }
    
    closeModal()
  } catch (err) {
    console.error('Error saving student:', err)
  }
}

const closeModal = () => {
  showAddModal.value = false
  editingStudent.value = null
  form.first_name = ''
  form.last_name = ''
  form.email = ''
  form.phone_number = ''
  form.is_active = true
}

onMounted(() => {
  fetchStudents()
})
</script> 