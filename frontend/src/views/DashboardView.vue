<template>
  <div class="w-full">
    <div id="alert-1" v-if="showTopTip && requests.length == 0"
      class="flex items-center p-4 mb-4 text-blue-800 rounded-lg bg-blue-50 dark:bg-gray-800 dark:text-blue-400"
      role="alert">
      <svg class="flex-shrink-0 w-4 h-4" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        viewBox="0 0 20 20">
        <path
          d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z" />
      </svg>
      <span class="sr-only">Info</span>
      <div class="ml-3 text-sm font-medium">
        You can start calling the /api endpoint!
      </div>
      <button type="button" @click="showTopTip = false"
        class="ml-auto -mx-1.5 -my-1.5 bg-blue-50 text-blue-500 rounded-lg focus:ring-2 focus:ring-blue-400 p-1.5 hover:bg-blue-200 inline-flex items-center justify-center h-8 w-8 dark:bg-gray-800 dark:text-blue-400 dark:hover:bg-gray-700"
        data-dismiss-target="#alert-1" aria-label="Close">
        <span class="sr-only">Close</span>
        <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
          <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
            d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6" />
        </svg>
      </button>
    </div>
    <button @click="openAddRequest" type="button"
      class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-2 py-2.5 mr-2 mb-2">
      <span class="flex">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="w-5 h-5">
          <path
            d="M10.75 4.75a.75.75 0 00-1.5 0v4.5h-4.5a.75.75 0 000 1.5h4.5v4.5a.75.75 0 001.5 0v-4.5h4.5a.75.75 0 000-1.5h-4.5v-4.5z" />
        </svg>
        <span class="mr-2">Hook</span>
      </span>
    </button>
    <button @click="showAllHooks" type="button"
      class="text-white bg-green-500 hover:bg-green-600 focus:ring-4 focus:ring-green-300 font-medium rounded-lg text-sm px-2 py-2.5 mr-2 mb-2">
      <span class="flex">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
          class="w-5 h-5 mr-16">
          <path stroke-linecap="round" stroke-linejoin="round"
            d="M15.75 15.75l-2.489-2.489m0 0a3.375 3.375 0 10-4.773-4.773 3.375 3.375 0 004.774 4.774zM21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
        <span class="mr-2">My Hooks</span>
      </span>
    </button>
    <div class="fixed inset-0 flex items-center justify-center z-50 bg-black bg-opacity-50" v-if="showRequest">
      <div class="bg-white rounded-lg shadow-lg p-4"
        style="max-height: 80vh; max-width: 100vh; overflow-y: auto; position: relative;">
        <button class="absolute top-2 right-2 text-gray-500 hover:text-gray-700" @click="showRequest = false">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
            class="w-6 h-6">
            <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
        <ViewRequest :request="request" v-if="request != null && showRequest"></ViewRequest>
      </div>
    </div>
    <div class="fixed inset-0 flex items-center justify-center z-50 bg-black bg-opacity-50" v-if="showHooksModal">
      <div class="bg-white rounded-lg shadow-lg p-4"
        style="max-height: 80vh; max-width: 100vh; overflow-y: auto; position: relative;">
        <button class="absolute top-2 right-2 text-gray-500 hover:text-gray-700" @click="showHooksModal = false">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
            class="w-6 h-6">
            <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
        <HooksList :hooks="hooks" v-if="hooks != null && showHooksModal" @hook-delete="deleteHook"></HooksList>
      </div>
    </div>

    <div class="fixed inset-0 flex items-center justify-center z-50 bg-black bg-opacity-50" v-if="showAddRequestModal">
      <div class="bg-white rounded-lg shadow-lg p-4">
        <AddRequest @close="showAddRequestModal = false" @submit="submitNewRequest"></AddRequest>
      </div>
    </div>
    <RequestsList :requests="requests" @request-clicked="showRequestModal" @request-delete="deleteRequest"></RequestsList>
  </div>
</template>

<script>
import RequestsList from "@/components/RequestsList.vue";
import AddRequest from "@/components/AddRequest.vue";
import ViewRequest from "@/components/ViewRequest.vue";
import HooksList from "@/components/HooksList.vue";
export default {
  components: {
    RequestsList,
    AddRequest,
    ViewRequest,
    HooksList,
  },
  data() {
    return {
      requests: [],
      sortedRequest: [],
      hooks: [],
      showAddRequestModal: false,
      showTopTip: true,
      showRequest: false,
      request: null,
      showHooksModal: false,
    }
  },
  setup() {
  },
  async mounted() {
    this.loading = true;
    this.loadRequests();
    setInterval(this.loadRequests, 5000);
  },
  computed: {
  },
  methods: {
    async openAddRequest(evt) {
      if (this.showAddRequestModal) {
        return;
      }
      this.showAddRequestModal = true;
    },
    async submitNewRequest(evt) {
      try {
        const apiUrl = '/api/settings/request';
        const response = await fetch(apiUrl, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json; charset=utf-8',
          },
          body: JSON.stringify(evt),
        });
        if (response.status != 200) {
          console.error('Request failed:', response.statusText);
        }
      } catch (error) {
        console.error('Error:', error);
      }
    },
    async loadRequests() {
      try {
        const response = await fetch('/api/all-requests');
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json();
        this.requests = data;
      } catch (error) {
        console.error('Error loading requests:', error);
      }
    },
    async loadHooks() {
      try {
        const response = await fetch('/api/settings/');
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json();
        this.hooks = data;
        console.log(this.hooks)
      } catch (error) {
        console.error('Error loading hooks:', error);
      }
    },
    async deleteRequest(requestId) {
      try {
        const apiUrl = '/api/settings/request?request_id=' + requestId;
        const response = await fetch(apiUrl, {
          method: 'DELETE',
          headers: {
            'Content-Type': 'application/json; charset=utf-8',
          },
        });
        if (response.status != 200) {
          console.error('Request failed:', response.statusText);
        } else {
          this.loadRequests();
        }
      } catch (error) {
        console.error('Error:', error);
      }
    },
    async deleteHook(hookId) {
      try {
        const apiUrl = '/api/settings/hook?hook_id=' + hookId;
        const response = await fetch(apiUrl, {
          method: 'DELETE',
          headers: {
            'Content-Type': 'application/json; charset=utf-8',
          },
        });
        if (response.status != 200) {
          console.error('Request failed:', response.statusText);
        } else {
          this.loadHooks();
        }
      } catch (error) {
        console.error('Error:', error);
      }
    },
    async showRequestModal(requestId) {
      try {
        const response = await fetch('/api/settings/request?request_id=' + requestId);
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json();
        this.request = data;
        this.showRequest = true;
      } catch (error) {
        console.error('Error loading request:', error);
      }
    },
    async showAllHooks(){
      this.loadHooks();
      this.showHooksModal = true;
    }
  }
};

</script>