<template>
  <div class="w-full">
    <div id="alert-1" v-if="showTopTip"
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
      class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2">Add
      Request</button>
    <div class="fixed inset-0 flex items-center justify-center z-50 bg-black bg-opacity-50" v-if="showAddRequestModal">
      <!-- The modal dialog -->
      <div class="bg-white rounded-lg shadow-lg p-4">
        <button @click="closeAddRequestModal"
          class="absolute top-2 right-2 text-gray-500 hover:text-gray-700 focus:outline-none">
          <i class="fa fa-times"></i> <!-- You can use a close icon here -->
        </button>
        <AddRequest @close="showAddRequestModal = false" @submit="submitNewRequest"></AddRequest>
      </div>
    </div>
    <RequestsList :requests="requests"></RequestsList>
  </div>
</template>

<script>
import RequestsList from "@/components/RequestsList.vue";
import AddRequest from "@/components/AddRequest.vue";
export default {
  components: {
    RequestsList,
    AddRequest,
  },
  data() {
    return {
      requests: [],
      sortedRequest: [],
      showAddRequestModal: false,
      showTopTip: true,
    }
  },
  setup() {
  },
  async mounted() {
    this.loading = true;
    this.loadRequests();
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
        console.log(JSON.stringify(evt))
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
  }
};

</script>