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
                <h2 class="text-xl font-bold text-gray-900 dark:text-white mb-10">Settings</h2>
                <div class="grid gap-4 mb-4">
                    <div class="sm:col-span-2">
                        <label class="relative inline-flex items-center cursor-pointer">
                            <input type="checkbox" v-model="unsetEndpointsEnabled" class="sr-only peer">
                            <div
                                class="w-11 h-6 bg-gray-200 rounded-full peer dark:bg-gray-700 peer-focus:ring-4 peer-focus:ring-purple-300 dark:peer-focus:ring-purple-800 peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-0.5 after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-purple-600">
                            </div>
                            <span class="ml-3 text-sm font-medium text-gray-900 dark:text-gray-300">Capture unset
                                endpoints</span>
                        </label>
                        <p class="mb-4 max-w-2xl text-sm leading-6 text-gray-500">Log requests to endpoints that haven't
                            been defined, instead of returning 404</p>
                    </div>
                </div>
                <div class="grid mb-10">
                    <div class="sm:col-span-2">
                        <label class="relative inline-flex items-center cursor-pointer">
                            <input type="checkbox" v-model="defaultEndpointsEnabled" class="sr-only peer">
                            <div
                                class="w-11 h-6 bg-gray-200 rounded-full peer dark:bg-gray-700 peer-focus:ring-4 peer-focus:ring-purple-300 dark:peer-focus:ring-purple-800 peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-0.5 after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-purple-600">
                            </div>
                            <span class="ml-3 text-sm font-medium text-gray-900 dark:text-gray-300">Enable default endpoint
                                (/api/hook/)</span>
                        </label>
                        <p class="mb-4 max-w-2xl text-sm leading-6 text-gray-500">Set whether default endpoint is enabled,
                            if not enabled, it will return 404</p>

                    </div>
                </div>
                <div class="flex items-center space-x-4">
                    <button type="submit" @click="saveSettings"
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
    name: 'SettingsForm',
    props: {
        settings: {
            type: Object,
            default: null,
            required: true,
        }
    },
    data() {
        return {
            unsetEndpointsEnabled: false,
            defaultEndpointsEnabled: true,
        };
    },
    mounted() {
        if (this.settings) {
            this.unsetEndpointsEnabled = this.settings.unset_endpoints_enabled;
            this.defaultEndpointsEnabled = this.settings.default_endpoints_enabled;
        }
    },
    methods: {
        closeModal() {
            this.$emit("close", true);
        },
        saveSettings() {
            const _settings = {};
            _settings.unset_endpoints_enabled = this.unsetEndpointsEnabled;
            _settings.default_endpoints_enabled = this.defaultEndpointsEnabled
            this.$emit('submit', _settings);
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