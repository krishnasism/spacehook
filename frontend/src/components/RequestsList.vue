<template>
    <div>
        <div class="relative overflow-x-auto">
            <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400 h-full">
                <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                    <tr>
                        <th scope="col" class="py-4">
                            <div class="flex items-center">
                                    Key
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
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="request in requests" :key="request.id"
                        class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                        <td class="">{{ request.key }}</td>
                        <td class="">{{ request.method }}</td>
                        <td class="">{{ request.endpoint }}</td>
                        <td class="py-4">{{ request.timestamp }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
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
    },
}
</script>
  