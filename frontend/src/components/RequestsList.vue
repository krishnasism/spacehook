<template>
    <div>
        <div class="relative overflow-x-auto">
            <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400 h-full">
                <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                    <tr>
                        <th scope="col" class="py-4">
                            <div class="flex items-center">
                            </div>
                        </th>
                        <th scope="col" class="py-4">
                            <div class="flex items-center">
                                Method
                            </div>
                        </th>
                        <th scope="col" class="py-4">
                            <div class="flex items-center">
                                Endpoint
                            </div>
                        </th>
                        <th scope="col" class="py-4">
                            <div class="flex items-center">
                                Created (UTC)
                            </div>
                        </th>
                        <th></th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="request in requests" :key="request.id"
                        class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                        <td class="ml-2 p-2"><button class="text-blue-700" @click="viewRequest(request.key)"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
  <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 6H5.25A2.25 2.25 0 003 8.25v10.5A2.25 2.25 0 005.25 21h10.5A2.25 2.25 0 0018 18.75V10.5m-10.5 6L21 3m0 0h-5.25M21 3v5.25" />
</svg>


                            </button></td>
                        <td class="">{{ request.method }}</td>
                        <td class="">{{ request.endpoint }}</td>
                        <td class="py-4">{{ request.timestamp }}</td>
                        <td>
                            <button @click="deleteRequest(request.key)">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                    stroke="currentColor" class="w-6 h-6">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M14.74 9l-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 01-2.244 2.077H8.084a2.25 2.25 0 01-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 00-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 013.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 00-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 00-7.5 0" />
                                </svg>
                            </button>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
        <p v-if="requests.length == 0">Its a bit lonely here... try calling /api!</p>
    </div>
</template>
  
<script>
export default {
    name: 'RequestsList',
    props: {
        requests: {
            type: Array,
            required: true,
        },
    },
    data() {
        return {
        }
    },
    methods: {
        viewRequest(requestId) {
            this.$emit("request-clicked", requestId);
        },
        deleteRequest(requestId) {
            this.$emit("request-delete", requestId);
        }
    },
}
</script>
  