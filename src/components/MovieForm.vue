<template>
  <div>
    <h2>Add New Movie</h2>
    <form @submit.prevent="saveMovie">
      <div>
        <label for="title">Title:</label>
        <input type="text" id="title" v-model="formData.title" required>
      </div>
      <div>
        <label for="description" class="form-label">Description:</label>
        <textarea id="description" v-model="formData.description" required></textarea>
      </div>
      <div>
        <label for="poster" class="form-label">Poster Image:</label>
        <input type="file" id="poster" @change="handleFileChange" required>
      </div>
      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

let csrf_token = ref("");

function getCsrfToken() {
  fetch('/api/v1/csrf-token')
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      csrf_token.value = data.csrf_token;
    })
}

const formData = ref({
  title: '',
  description: '',
  poster: null
});

const saveMovie = () => {
  const data = new FormData();
  data.append('title', formData.value.title);
  data.append('description', formData.value.description);
  data.append('poster', formData.value.poster);

  fetch('/api/v1/movies', {
    method: 'POST',
    body: data,
    headers: {
      'X-CSRFToken': csrf_token.value
    }
  })
    .then(response => {
      if (!response.ok) {
        throw new Error('Failed to upload movie.');
      }
      return response.json();
    })
    .then(data => {
      console.log(data.message); // Success message
    })
    .catch(error => {
      console.error(error.message); // Error message
    });
};

const handleFileChange = (event) => {
  formData.value.poster = event.target.files[0];
};

onMounted(() => {
  getCsrfToken();
});
</script>

<style scoped>
/* Add your styles here */
</style>