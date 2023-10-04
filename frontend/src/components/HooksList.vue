<template>
    <div v-if="hooksLoading">
        <LoadingCircle></LoadingCircle>
    </div>
    <div v-else>
        <div v-if="hooks.length == 0" class="m-4">No hooks added..</div>
        <div v-else class="relative overflow-x-auto">
            <h3 class="text-base font-semibold leading-7 text-gray-900">Hooks</h3>
            <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400 h-full">
                <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                    <tr>
                        <th></th>
                        <th scope="col" class="w-52 p-8">
                            <div class="flex items-center">
                                Type
                            </div>
                        </th>
                        <th scope="col" class="w-52 p-8">
                            <div class="flex items-center">
                                Endpoint
                            </div>
                        </th>
                        <th scope="col" class="w-52 p-8">
                            <div class="flex items-center">
                                Code
                            </div>
                        </th>
                        <th scope="col" class="w-52 p-8">
                            <div class="flex items-center">
                                Response
                            </div>
                        </th>
                        <th>
                        </th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="hook in hooks" :key="hook.id"
                        class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                        <td>
                            <button class="pr-2 cursor-pointer" @click="editHook(hook.key)">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                    stroke="currentColor" class="w-6 h-6">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M16.862 4.487l1.687-1.688a1.875 1.875 0 112.652 2.652L10.582 16.07a4.5 4.5 0 01-1.897 1.13L6 18l.8-2.685a4.5 4.5 0 011.13-1.897l8.932-8.931zm0 0L19.5 7.125M18 14v4.75A2.25 2.25 0 0115.75 21H5.25A2.25 2.25 0 013 18.75V8.25A2.25 2.25 0 015.25 6H10" />
                                </svg>
                            </button>
                        </td>
                        <td>{{ hook.category }}</td>
                        <td>/api/hook/{{ hook.endpoint }}</td>
                        <td>{{ hook.statuscode }}</td>
                        <td class="max-h-3 h-3 max-w-xs" style="overflow: hidden; max-width: 50px; max-height: 50px;">{{
                            hook.response }}</td>
                        <td>
                            <button @click="deleteHook(hook.key)">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                    stroke="red" class="w-6 h-6">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M14.74 9l-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 01-2.244 2.077H8.084a2.25 2.25 0 01-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 00-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 013.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 00-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 00-7.5 0" />
                                </svg>
                            </button>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>
  
<script>
import LoadingCircle from './LoadingCircle.vue';

export default {
    name: 'HooksList',
    components: {
        LoadingCircle,
    },
    props: {
        hooks: {
            type: Array,
            required: true,
        },
        hooksLoading: {
            type: Boolean,
            required: false,
            default: false,
        }
    },
    data() {
        return {
        }
    },
    methods: {
        deleteHook(hookId) {
            this.$emit("hook-delete", hookId);
        },
        editHook(hookId) {
            this.$emit("hook-edit", hookId);
        },
    },
}
</script>
  