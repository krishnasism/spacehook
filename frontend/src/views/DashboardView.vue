<template>
  <div class="w-full">
    <RequestsList :requests="requests"></RequestsList>
  </div>
</template>

<script>
import RequestsList from "@/components/RequestsList.vue";

export default {
  components: {
    RequestsList,
  },
  data() {
    return {
      requests: [],
      sortedRequest: [],
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
    async loadRequests() {
      try {
        const response = await fetch('/api/all-requests'); // Make GET request to the API using fetch
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json(); // Parse response JSON
        console.log(data)
        this.requests = data; // Update the requests data with the parsed data
      } catch (error) {
        console.error('Error loading requests:', error);
      }
    },
  }
};

</script>