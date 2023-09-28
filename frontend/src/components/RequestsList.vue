<template>
    <div>
        <div class="w-full mr-28 ml-28" v-if="requests.length > 0">
            <div v-for="request in requests" :key="request.id"
                class="relative w-full grid grid-cols-12 bg-white shadow p-3 gap-2 items-center cursor-pointer p-6 rounded-xl mt-2 mb-6 request-item"
                @click="viewRequest(request.key)">
                <div class="col-span-6 xl:-ml-5">
                    <p class="purple-text font-semibold">{{ request.method }}</p>
                </div>
                <div class="md:col-start-2 col-span-6 xl:-ml-5">
                    <p class="text-sm text-gray-800 font-light">{{ ("/api/hook/" + request.endpoint).replace("//", "/") }}
                    </p>
                </div>
                <div class="md:col-start-2 col-span-11 xl:-ml-5">
                    <p class="text-sm text-gray-500 font-light">{{ request.timestamp }}</p>
                </div>
                <button @click.stop="deleteRequest(request.key)"
                    class="absolute top-1/2 right-2 transform -translate-y-1/2 mr-4">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="red"
                        class="w-6 h-6">
                        <path stroke-linecap="round" stroke-linejoin="round"
                            d="M14.74 9l-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 01-2.244 2.077H8.084a2.25 2.25 0 01-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 00-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 013.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 00-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 00-7.5 0" />
                    </svg>
                </button>
            </div>
        </div>
        <p class="p-4" v-if="requests.length == 0">It's a bit lonely in here... try calling <a href="/api/hook/"
                target="_blank" class="underline text-blue-600">/api/hook/</a></p>
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
  
<style>
.request-item:hover {
    transform: scale(1.005);
    transition: transform 0.2s ease;
}

.purple-text {
    color: rgb(168 85 247);
}
</style>