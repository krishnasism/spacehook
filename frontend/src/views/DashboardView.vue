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
      <div class="fixed inset-0 flex items-center justify-center z-10 bg-black bg-gray-50 bg-opacity-50"
        v-if="showRequest">
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
      <div class="fixed inset-0 flex items-center justify-center z-10 bg-black bg-gray-50 bg-opacity-50"
        v-if="showHooksModal">
        <div class="relative bg-white rounded-lg shadow dark:bg-gray-700 p-8"
          style="max-height: 80vh; max-width: 100vh; overflow-y: auto;">
          <button class="absolute top-2 right-2 text-gray-500 hover:text-gray-700" @click="showHooksModal = false">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
              stroke="currentColor" class="w-6 h-6">
              <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
          <HooksList :hooks="hooks" v-if="hooks != null && showHooksModal" @hook-delete="deleteHook" @hook-edit="editHook"
            :hooksLoading="hooksLoading"></HooksList>
        </div>
      </div>
    </transition>
    <transition name="modal-fade" mode="out-in">
      <div class="fixed inset-0 flex items-center justify-center z-10 bg-gray-50 bg-opacity-50"
        v-if="showAddRequestModal">
        <div class="bg-white rounded-lg shadow-lg p-4">
          <AddRequest @close="showAddRequestModal = false; editingHook = null;" @submit="submitNewRequest"
            :hook="editingHook"></AddRequest>
        </div>
      </div>
    </transition>
    <transition name="modal-fade" mode="out-in">
      <div class="fixed inset-0 flex items-center justify-center z-10 bg-gray-50 bg-opacity-50" v-if="showSettingsForm">
        <div class="bg-white rounded-lg shadow-lg p-4">
          <SettingsForm @close="showSettingsForm = false;" @submit="updateSettings" :settings="settings"></SettingsForm>
        </div>
      </div>
    </transition>
    <transition name="modal-fade" mode="out-in">
      <div class="fixed inset-0 flex items-center justify-center z-10 bg-gray-50 bg-opacity-50"
        v-if="showSwaggerFileInput">
        <div class="bg-white rounded-lg shadow-lg p-4">
          <SwaggerFileInput @close="showSwaggerFileInput = false;" @submit="ingestSwaggerFile" :loading="swaggerFileIngesting"></SwaggerFileInput>
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

    <div class="fixed bottom-0 left-0 w-full p-4 flex justify-center items-center gap-4">
      <button type="button" @click="showAllHooks"
        class="flex justify-center items-center w-[52px] h-[52px] text-gray-500 hover:text-gray-900 bg-white rounded-full border border-gray-200 dark:border-gray-600 dark:hover:text-white shadow-sm dark:text-gray-400 hover:bg-gray-50 dark:bg-gray-700 dark:hover:bg-gray-600 focus:ring-4 focus:ring-gray-300 focus:outline-none dark:focus:ring-gray-400">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
          class="w-6 h-6">
          <path stroke-linecap="round" stroke-linejoin="round"
            d="M8.25 6.75h12M8.25 12h12m-12 5.25h12M3.75 6.75h.007v.008H3.75V6.75zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0zM3.75 12h.007v.008H3.75V12zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0zm-.375 5.25h.007v.008H3.75v-.008zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0z" />
        </svg>
        <span class="sr-only">All Hooks</span>
      </button>
      <button type="button" @click="openAddRequest"
        class="flex justify-center items-center w-[52px] h-[52px] text-gray-500 hover:text-gray-900 bg-white rounded-full border border-gray-200 dark:border-gray-600 dark:hover:text-white shadow-sm dark:text-gray-400 hover:bg-gray-50 dark:bg-gray-700 dark:hover:bg-gray-600 focus:ring-4 focus:ring-gray-300 focus:outline-none dark:focus:ring-gray-400">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
          class="w-6 h-6">
          <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v6m3-3H9m12 0a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
        <span class="sr-only">New Hook</span>
      </button>
      <button type="button" @click="showSettings"
        class="flex justify-center items-center w-[52px] h-[52px] text-gray-500 hover:text-gray-900 bg-white rounded-full border border-gray-200 dark:border-gray-600 dark:hover:text-white shadow-sm dark:text-gray-400 hover:bg-gray-50 dark:bg-gray-700 dark:hover:bg-gray-600 focus:ring-4 focus:ring-gray-300 focus:outline-none dark:focus:ring-gray-400">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
          class="w-6 h-6">
          <path stroke-linecap="round" stroke-linejoin="round"
            d="M9.594 3.94c.09-.542.56-.94 1.11-.94h2.593c.55 0 1.02.398 1.11.94l.213 1.281c.063.374.313.686.645.87.074.04.147.083.22.127.324.196.72.257 1.075.124l1.217-.456a1.125 1.125 0 011.37.49l1.296 2.247a1.125 1.125 0 01-.26 1.431l-1.003.827c-.293.24-.438.613-.431.992a6.759 6.759 0 010 .255c-.007.378.138.75.43.99l1.005.828c.424.35.534.954.26 1.43l-1.298 2.247a1.125 1.125 0 01-1.369.491l-1.217-.456c-.355-.133-.75-.072-1.076.124a6.57 6.57 0 01-.22.128c-.331.183-.581.495-.644.869l-.213 1.28c-.09.543-.56.941-1.11.941h-2.594c-.55 0-1.02-.398-1.11-.94l-.213-1.281c-.062-.374-.312-.686-.644-.87a6.52 6.52 0 01-.22-.127c-.325-.196-.72-.257-1.076-.124l-1.217.456a1.125 1.125 0 01-1.369-.49l-1.297-2.247a1.125 1.125 0 01.26-1.431l1.004-.827c.292-.24.437-.613.43-.992a6.932 6.932 0 010-.255c.007-.378-.138-.75-.43-.99l-1.004-.828a1.125 1.125 0 01-.26-1.43l1.297-2.247a1.125 1.125 0 011.37-.491l1.216.456c.356.133.751.072 1.076-.124.072-.044.146-.087.22-.128.332-.183.582-.495.644-.869l.214-1.281z" />
          <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
        </svg>
        <span class="sr-only">Settings</span>
      </button>
      <button type="button" @click="showSwaggerInput"
        class="flex justify-center items-center w-[52px] h-[52px] text-gray-500 hover:text-gray-900 bg-white rounded-full border border-gray-200 dark:border-gray-600 dark:hover:text-white shadow-sm dark:text-gray-400 hover:bg-gray-50 dark:bg-gray-700 dark:hover:bg-gray-600 focus:ring-4 focus:ring-gray-300 focus:outline-none dark:focus:ring-gray-400">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
          class="w-6 h-6">
          <path stroke-linecap="round" stroke-linejoin="round"
            d="M17.25 6.75L22.5 12l-5.25 5.25m-10.5 0L1.5 12l5.25-5.25m7.5-3l-4.5 16.5" />
        </svg>
        <span class="sr-only">Swagger File</span>
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
import SettingsForm from "@/components/SettingsForm.vue";
import SwaggerFileInput from "@/components/SwaggerFileInput.vue";

export default {
  components: {
    RequestsList,
    AddRequest,
    ViewRequest,
    HooksList,
    LoadingCircle,
    FailureToast,
    SettingsForm,
    SwaggerFileInput,
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
      editingHook: null,
      showSettingsForm: false,
      settings: null,
      showSwaggerFileInput: false,
      swaggerFileIngesting: false,
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
      this.editingHook = null;
      this.showSettingsForm = false;
      this.showSwaggerFileInput = false;
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
          if (this.editingHook) {
            this.editingHook = null;
            this.loadHooks();
          }
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
    async editHook(hookId) {
      try {
        const apiUrl = '/api/settings/hook?hook_id=' + hookId;
        const response = await fetch(apiUrl, {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json; charset=utf-8',
          },
        });
        if (response.status != 200) {
          console.error('Request failed:', response.statusText);
        } else {
          this.editingHook = await response.json();
          this.showAddRequestModal = true;
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
    },
    async showSettings() {
      try {
        const apiUrl = '/api/settings/user-settings';
        const response = await fetch(apiUrl, {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json; charset=utf-8',
          },
        });
        if (response.status != 200) {
          console.error('Request failed:', response.statusText);
        } else {
          this.settings = await response.json();
          this.showSettingsForm = true;
        }
      } catch (error) {
        console.error('Error:', error);
      }
    },
    async updateSettings(_settings) {
      try {
        const apiUrl = '/api/settings/user-settings';
        const response = await fetch(apiUrl, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json; charset=utf-8',
          },
          body: JSON.stringify(_settings),
        });
        if (response.status != 200) {
          console.error('Request failed:', response.statusText);
          this.showFailureToast = true;
          this.failureToastMessage = 'Unable to update user settings!';
        } else {
          this.showSettingsForm = false;
        }
      } catch (error) {
        console.error('Error:', error);
      }
    },
    async showSwaggerInput() {
      this.showSwaggerFileInput = true;
    },
    async ingestSwaggerFile(swaggerYaml) {
      try {
        this.swaggerFileIngesting = true;
        const apiUrl = '/api/settings/swagger';
        const response = await fetch(apiUrl, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json; charset=utf-8',
          },
          body: JSON.stringify({
            swagger_yaml: swaggerYaml,
          }),
        });
        if (response.status != 200) {
          const response_data = await response.json();
          this.showFailureToast = true;
          this.failureToastMessage = 'Unable to ingest swagger file: ' + response_data['error'].slice(0, 50) + '!';
        } else {
          this.showSwaggerFileInput = false;
          this.showAllHooks();
        }
      } catch (error) {
        console.error('Error:', error);
      } finally {
        this.swaggerFileIngesting = false;
      }
    },
  }
}

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

.purple-color {
  background-color: rgb(168 85 247);
}

.purple-color:hover {
  background-color: rgb(126 34 206);
}
</style>