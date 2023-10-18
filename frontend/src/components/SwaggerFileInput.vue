<template>
    <div>
        <section class="bg-white dark:bg-gray-900">
            <div class="max-w-2xl px-4 py-8 mx-auto lg:py-8 relative">
                <button class="absolute right- text-gray-500 hover:text-gray-700 top-0 right-0" @click="closeModal">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                        stroke="currentColor" class="w-6 h-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
                    </svg>
                </button>
                <h2 class="text-xl font-bold text-gray-900 dark:text-white mb-4">Swagger File</h2>
                <p class="mb-4 max-w-2xl text-sm leading-6 text-gray-500">Convert a swagger file to mock endpoints</p>
                <textarea id="swaggerInput" rows="8" v-model="swaggerYaml"
                    class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                    placeholder="Paste your swagger file here..."></textarea>
                <div v-if="loading">
                    <LoadingCircle class="mt-6"></LoadingCircle>
                </div>
                <div v-else class="flex items-center space-x-4 mt-6">
                    <button type="submit" @click="ingestSwagger"
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
import LoadingCircle from './LoadingCircle.vue';
export default {
    name: 'SwaggerFileInput',
    components: {
        LoadingCircle,
    },
    props: {
        loading: {
            type: Boolean,
            default: false,
        },
    },
    data() {
        return {
            swaggerYaml: "",
        };
    },
    mounted() {
    },
    methods: {
        closeModal() {
            this.$emit("close", true);
        },
        ingestSwagger() {
            if (this.swaggerYaml.trim().length > 0) {
                this.$emit("submit", this.swaggerYaml);
            }
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