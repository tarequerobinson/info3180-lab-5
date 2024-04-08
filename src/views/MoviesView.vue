<template>
    <div>
      <h1>All Movies</h1>
      <ul>
        <li v-for="movie in movies" :key="movie.id">{{ movie.title }} - {{ movie.year }}</li>
      </ul>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from "vue";
  
  // Define a ref to hold the movies data
  let movies = ref([]);
  
  // Fetch movies when the component is mounted
  onMounted(() => {
    fetchMovies();
  });
  
  async function fetchMovies() {
    try {
      // Make a GET request to fetch all movies
      const response = await fetch("/api/v1/movies");
      if (!response.ok) {
        throw new Error("Failed to fetch movies");
      }
      // Parse the response JSON
      const data = await response.json();
      // Update the movies ref with the fetched data
      movies.value = data;
    } catch (error) {
      console.error("Error fetching movies:", error.message);
    }
  }
  </script>
  