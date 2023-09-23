<template>
  <div class="w-full">
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