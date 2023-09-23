<template>
    <div>
        <section class="bg-white dark:bg-gray-900">
            <div class="max-w-2xl px-4 py-8 mx-auto lg:py-8">
                <h2 class="mb-4 text-xl font-bold text-gray-900 dark:text-white">Add Request</h2>
                <div class="grid gap-4 mb-4 sm:grid-cols-2 sm:gap-6 sm:mb-5">
                    <div class="sm:col-span-2">
                        <label for="name"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Endpoint</label>
                        <div class="flex">
                            <span class="text-xs p-3 pl-0">/api/hook/</span>
                            <input type="text" name="endpoint" id="endpoint" v-model="endpoint"
                                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                                placeholder="test" required>
                        </div>
                    </div>
                    <div class="w-full">
                        <label for="brand" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Status
                            Code</label>
                        <input type="text" name="statuscode" id="statuscode" v-model="statuscode"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            placeholder="200" required>
                    </div>
                    <div>
                        <label for="category"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Type</label>
                        <select id="category" v-model="category"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500">
                            <option value="get" selected>GET</option>
                            <option value="post">POST</option>
                            <option value="put">PUT</option>
                            <option value="patch">PATCH</option>
                            <option value="delete">DELETE</option>
                        </select>
                    </div>
                    <div class="sm:col-span-2">
                        <label for="response"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Response</label>
                        <textarea id="response" rows="8" v-model="response"
                            class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            placeholder="Response"></textarea>
                    </div>
                </div>
                <div class="flex items-center space-x-4">
                    <button type="submit" @click="saveRequest"
                        class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800">
                        Save
                    </button>
                    <button type="button" @click="closeModal"
                        class="focus:outline-none text-white bg-red-700 hover:bg-red-800 focus:ring-4 focus:ring-red-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-red-600 dark:hover:bg-red-700 dark:focus:ring-red-900">
                        Cancel
                    </button>
                </div>
            </div>
        </section>
    </div>
</template>
<script>
export default {
    name: 'AddRequest',
    props: {
    },
    data() {
        return {
            endpoint: '',
            statuscode: '200',
            category: 'get',
            response: '',
        };
    },
    methods: {
        closeModal() {
            this.$emit("close", true);
        },
        saveRequest() {
            const requestData = {
                endpoint: this.endpoint,
                statuscode: this.statuscode,
                category: this.category,
                response: this.response,
            };
            this.$emit('submit', requestData);
            this.closeModal();
        },
    },
}
</script>
  