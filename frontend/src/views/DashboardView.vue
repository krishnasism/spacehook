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
        You can start calling the /api/hook/ endpoint!
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
    <transition name="modal-fade" mode="out-in">
      <div class="fixed inset-0 flex items-center justify-center z-10 bg-black bg-opacity-50" v-if="showRequest">
        <div class="bg-white rounded-lg shadow-lg p-4"
          style="max-height: 80vh; max-width: 100vh; overflow-y: auto; position: relative;">
          <button class="absolute top-2 right-2 text-gray-500 hover:text-gray-700" @click="showRequest = false">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
              stroke="currentColor" class="w-6 h-6">
              <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
          <ViewRequest :request="request" v-if="request != null && showRequest"></ViewRequest>
        </div>
      </div>
    </transition>
    <transition name="modal-fade" mode="out-in">
      <div class="fixed inset-0 flex items-center justify-center z-10 bg-black bg-opacity-50" v-if="showHooksModal">
        <div class="relative bg-white rounded-lg shadow dark:bg-gray-700 p-8"
          style="max-height: 80vh; max-width: 100vh; overflow-y: auto;">
          <button class="absolute top-2 right-2 text-gray-500 hover:text-gray-700" @click="showHooksModal = false">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
              stroke="currentColor" class="w-6 h-6">
              <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
          <HooksList :hooks="hooks" v-if="hooks != null && showHooksModal" @hook-delete="deleteHook"
            :hooksLoading="hooksLoading"></HooksList>
        </div>
      </div>
    </transition>
    <transition name="modal-fade" mode="out-in">
      <div class="fixed inset-0 flex items-center justify-center z-10 bg-black bg-opacity-50" v-if="showAddRequestModal">
        <div class="bg-white rounded-lg shadow-lg p-4">
          <AddRequest @close="showAddRequestModal = false" @submit="submitNewRequest"></AddRequest>
        </div>
      </div>
    </transition>
    <div v-if="loading || loadingInner"
      style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: 9999; display: flex; justify-content: center; align-items: center;">
      <LoadingCircle />
    </div>

    <RequestsList v-if="!loading" :requests="requests" @request-clicked="showRequestModal"
      @request-delete="deleteRequest">
    </RequestsList>
    <Transition enter-active-class="duration-300 ease-out" enter-from-class="transform opacity-0"
      enter-to-class="opacity-100" leave-active-class="duration-200 ease-in" leave-from-class="opacity-100"
      leave-to-class="transform opacity-0">
      <FailureToast class="z-20" style="position: fixed; bottom: 0; right: 20;" v-if="showFailureToast"
        :message="failureToastMessage" @close-toast="showFailureToast = false"></FailureToast>
    </Transition>

    <div data-dial-init class="fixed right-6 bottom-6 group">
      <div id="speed-dial-menu-bottom-right" class="flex flex-col items-center hidden mb-4 space-y-2">
        <button type="button" data-tooltip-target="tooltip-all-hooks" data-tooltip-placement="left" @click="showAllHooks"
          class="flex justify-center items-center w-[52px] h-[52px] text-gray-500 hover:text-gray-900 bg-white rounded-full border border-gray-200 dark:border-gray-600 dark:hover:text-white shadow-sm dark:text-gray-400 hover:bg-gray-50 dark:bg-gray-700 dark:hover:bg-gray-600 focus:ring-4 focus:ring-gray-300 focus:outline-none dark:focus:ring-gray-400">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
            class="w-6 h-6">
            <path stroke-linecap="round" stroke-linejoin="round"
              d="M8.25 6.75h12M8.25 12h12m-12 5.25h12M3.75 6.75h.007v.008H3.75V6.75zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0zM3.75 12h.007v.008H3.75V12zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0zm-.375 5.25h.007v.008H3.75v-.008zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0z" />
          </svg>
          <span class="sr-only">All Hooks</span>
        </button>
        <div id="tooltip-all-hooks" role="tooltip"
          class="w-auto absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-sm opacity-0 tooltip dark:bg-gray-700">
          All Hooks
          <div class="tooltip-arrow" data-popper-arrow></div>
        </div>

        <button type="button" data-tooltip-target="tooltip-add-hook" data-tooltip-placement="left" @click="openAddRequest"
          class="flex justify-center items-center w-[52px] h-[52px] text-gray-500 hover:text-gray-900 bg-white rounded-full border border-gray-200 dark:border-gray-600 dark:hover:text-white shadow-sm dark:text-gray-400 hover:bg-gray-50 dark:bg-gray-700 dark:hover:bg-gray-600 focus:ring-4 focus:ring-gray-300 focus:outline-none dark:focus:ring-gray-400">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
            class="w-6 h-6">
            <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v6m3-3H9m12 0a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>

          <span class="sr-only">New Hook</span>
        </button>
        <div id="tooltip-add-hook" role="tooltip"
          class="w-auto absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-sm opacity-0 tooltip dark:bg-gray-700">
          New Hook
          <div class="tooltip-arrow" data-popper-arrow></div>
        </div>
      </div>
      <button type="button" data-dial-toggle="speed-dial-menu-bottom-right" aria-controls="speed-dial-menu-bottom-right"
        aria-expanded="false"
        class="flex items-center justify-center text-white bg-blue-700 rounded-full w-14 h-14 hover:bg-blue-800 dark:bg-blue-600 dark:hover:bg-blue-700 focus:ring-4 focus:ring-blue-300 focus:outline-none dark:focus:ring-blue-800">
        <svg class="w-5 h-5 transition-transform group-hover:rotate-45" aria-hidden="true"
          xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 18">
          <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
            d="M9 1v16M1 9h16" />
        </svg>
        <span class="sr-only">Open actions menu</span>
      </button>
    </div>

  </div>
</template>

<script>
import RequestsList from "@/components/RequestsList.vue";
import AddRequest from "@/components/AddRequest.vue";
import ViewRequest from "@/components/ViewRequest.vue";
import HooksList from "@/components/HooksList.vue";
import LoadingCircle from "@/components/LoadingCircle.vue";
import FailureToast from "@/components/FailureToast.vue";
export default {
  components: {
    RequestsList,
    AddRequest,
    ViewRequest,
    HooksList,
    LoadingCircle,
    FailureToast,
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
      loading: true,
      loadingInner: false,
      hooksLoading: false,
      failureToastMessage: '',
      showFailureToast: false,
    }
  },
  setup() {
  },
  async mounted() {
    this.loading = true;
    await this.loadRequests();
    setInterval(this.loadRequests, 3000);
    this.loading = false;
    document.addEventListener("keydown", this.handleKeyDown);
  },
  beforeUnmount() {
    document.removeEventListener("keydown", this.handleKeyDown);
  },
  computed: {
  },
  methods: {
    handleKeyDown(event) {
      if (event.key === "Escape") {
        this.onEscKeyPressed();
      }
    },
    onEscKeyPressed() {
      this.showAddRequestModal = false;
      this.showHooksModal = false;
      this.showRequest = false;

    },
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
          this.showFailureToast = true;
          this.failureToastMessage = 'Unable to add new request!';
        } else {
          this.showAddRequestModal = false;
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
      this.hooksLoading = true;
      try {
        const response = await fetch('/api/settings/');
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json();
        this.hooks = data;
      } catch (error) {
        console.error('Error loading hooks:', error);
      }
      this.hooksLoading = false;
    },
    async deleteRequest(requestId) {
      this.loadingInner = true;
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
      this.loadingInner = false;
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
      this.loadingInner = true;
      try {
        const response = await fetch('/api/settings/request?request_id=' + requestId);
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json();
        console.log(data);
        this.request = data;
        this.showRequest = true;
      } catch (error) {
        console.error('Error loading request:', error);
      }
      this.loadingInner = false;
    },
    async showAllHooks() {
      this.loadHooks();
      this.showHooksModal = true;
    }
  }
};

</script>
<style scoped>
/* Define CSS transitions for entering and leaving transitions */
.modal-fade-enter-active,
.modal-fade-leave-active {
  transition: opacity 0.5s;
}

.modal-fade-enter,
.modal-fade-leave-to {
  opacity: 0;
}

.tooltip {
  white-space: nowrap;
  display: inline-block;
}
</style>