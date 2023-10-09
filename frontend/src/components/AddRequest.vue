<template>
    <div>
        <section class="bg-white dark:bg-gray-900">
            <div class="relative max-w-2xl px-4 py-8 mx-auto lg:py-8">
                <button class="absolute right- text-gray-500 hover:text-gray-700 top-0 right-0" @click="closeModal">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                        stroke="currentColor" class="w-6 h-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
                    </svg>
                </button>
                <h2 class="text-xl font-bold text-gray-900 dark:text-white">{{ hook ? 'Edit' : 'Add' }} Hook</h2>
                <p class="mb-4 max-w-2xl text-sm leading-6 text-gray-500">All hooks are public by default</p>
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
                            <option value="options">OPTIONS</option>
                            <option value="head">HEAD</option>
                        </select>
                    </div>
                    <div>
                        <label for="category" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Response
                            Type</label>
                        <select id="responsetype" v-model="responsetype"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500">
                            <option value="plaintext" selected>Plain Text</option>
                            <option value="json">JSON</option>
                            <option value="html">HTML</option>
                        </select>
                    </div>
                    <div class="w-full">
                        <label for="brand" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Delay (in
                            seconds)</label>
                        <input type="text" name="delay" id="delay" v-model="delay"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            placeholder="0" required>
                    </div>
                    <div class="sm:col-span-2">
                        <label for="response"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Response</label>
                        <textarea id="response" rows="4" v-model="response"
                            class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            placeholder="Response"></textarea>
                    </div>
                    <div>
                        <label for="category" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Auth
                            Type</label>
                        <select id="responsetype" v-model="authtype"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500">
                            <option value="public" selected>No Auth (Public)</option>
                            <option value="basic">Basic Auth</option>
                            <option value="bearer">Bearer Token</option>
                        </select>
                    </div>
                    <div v-if="authtype == 'basic'">
                        <div class="w-full">
                            <label for="brand"
                                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Username</label>
                            <input type="text" name="basicAuthUsername" id="basicAuthUsername" v-model="basicAuthUsername"
                                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                                placeholder="Basic Auth Username">
                        </div>
                        <div class="w-full mt-2">
                            <label for="brand"
                                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Password</label>
                            <input type="text" name="basicAuthPassword" id="basicAuthPassword"
                                v-model="basicAuthPassword"
                                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                                placeholder="Basic Auth Password">
                        </div>
                    </div>
                    <div v-if="authtype == 'bearer'">
                        <div class="sm:col-span-2">
                        <label for="accessToken"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Bearer Token</label>
                        <textarea id="accessToken" rows="4" v-model="accessToken"
                            class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            placeholder="Bearer Token"></textarea>
                    </div>
                    </div>
                </div>
                <div id="alert-4" v-if="showAddRequestAlert"
                    class="flex items-center p-4 mb-4 text-yellow-800 rounded-lg bg-yellow-50 dark:bg-gray-800 dark:text-yellow-300"
                    role="alert">
                    <svg class="flex-shrink-0 w-4 h-4" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
                        fill="currentColor" viewBox="0 0 20 20">
                        <path
                            d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z" />
                    </svg>
                    <span class="sr-only">Warning</span>
                    <div class="ml-3 text-sm font-medium">
                        Please fill in all fields!
                    </div>
                    <button type="button" @click="showAddRequestAlert = false"
                        class="ml-auto -mx-1.5 -my-1.5 bg-yellow-50 text-yellow-500 rounded-lg focus:ring-2 focus:ring-yellow-400 p-1.5 hover:bg-yellow-200 inline-flex items-center justify-center h-8 w-8 dark:bg-gray-800 dark:text-yellow-300 dark:hover:bg-gray-700"
                        data-dismiss-target="#alert-4" aria-label="Close">
                        <span class="sr-only">Close</span>
                        <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none"
                            viewBox="0 0 14 14">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6" />
                        </svg>
                    </button>
                </div>
                <div class="flex items-center space-x-4">
                    <button type="submit" @click="saveRequest"
                        class="text-white purple-color focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-1 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800">
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
        hook: {
            type: Object,
            default: null,
            required: false,
        }
    },
    data() {
        return {
            endpoint: '',
            statuscode: '200',
            category: 'get',
            response: '',
            showAddRequestAlert: false,
            delay: '0',
            responsetype: 'plaintext',
            authtype: 'public',
            basicAuthUsername: '',
            basicAuthPassword: '',
            accessToken: '',
            hookId: '',
        };
    },
    mounted() {
      if (this.hook) {
            this.endpoint = this.hook.endpoint;
            this.statuscode = this.hook.statuscode;
            this.category = this.hook.category;
            this.response = this.hook.response;
            this.delay = this.hook.delay;
            this.responsetype =  this.hook.responsetype;
            this.authtype = this.hook.authtype;
            this.basicAuthUsername = this.hook.basic_auth_username;
            this.basicAuthPassword = this.hook.basic_auth_password;
            this.accessToken = this.hook.access_token;
            this.hookId = this.hook.key;
      }  
    },
    methods: {
        closeModal() {
            this.$emit("close", true);
        },
        saveRequest() {
            if (this.endpoint == '' || this.statuscode == '' || this.category == '' || this.response == '' || this.responsetype == '') {
                this.showAddRequestAlert = true;
                return;
            }
            this.showAddRequestAlert = false;
            const requestData = {
                endpoint: this.endpoint,
                statuscode: this.statuscode,
                category: this.category,
                response: this.response,
                delay: this.delay,
                responsetype: this.responsetype,
                authtype: this.authtype,
                basic_auth_username: this.basicAuthUsername,
                basic_auth_password: this.basicAuthPassword,
                access_token: this.accessToken,
                hook_id: this.hookId,
            };
            this.$emit('submit', requestData);
        },
    },
}
</script>

<style>
.purple-color {
    background-color: rgb(168 85 247);
}

.purple-color:hover {
    background-color: rgb(126 34 206);
}
</style>