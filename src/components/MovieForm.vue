<script setup>
import { ref, onMounted } from "vue";
let csrf_token = ref("");
let flashMessage = ref("");
let displayFlash = ref(false);
let isSuccess = ref(false);
let alertSuccessClass = ref("alert-success");
let alertErrorClass = ref("alert-danger");

onMounted(() => {
  getCsrfToken();
});

function saveMovie() {
  let movieForm = document.getElementById("movieForm");
  let form_data = new FormData(movieForm);

  fetch("/api/v1/movies", {
    method: "POST",
    body: form_data,
    headers: {
    "X-CSRFToken": csrf_token.value,
    },
  })
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      console.log(data);
      if ("errors" in data) {
        flashMessage.value = [...data.errors];
        isSuccess.value = false;
        displayFlash.value = true;
      } else {
        displayFlash.value = true;
        isSuccess.value = true;
        flashMessage.value = "Movie added successfully!";
        clearFormFields();
        console.log(data);
      }
    })
    .catch(function (error) {
      console.log(error);
    });
}

function getCsrfToken() {
  fetch("/api/v1/csrf-token")
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      csrf_token.value = data.csrf_token;
    });
}

function clearFormFields() {
  title.value = "";
  description.value = "";
  poster.value = "";
}
</script>

<template>
  <div class="container">
  <h1>Uploads</h1>
  <br/>
    <div
      v-if="displayFlash"
      v-bind:class="[isSuccess ? alertSuccessClass : alertErrorClass]"
      class="alert"
    >
      {{ flashMessage }}
    </div>
    <form id="movieForm" @submit.prevent="saveMovie">
      <div class="mb-3">
        <label for="exampleFormControlInput1" class="form-label">Title</label>
        <input type="text" class="form-control" id="exampleFormControlInput1" />
      </div>
      <div class="mb-3">
        <label for="exampleFormControlTextarea1" class="form-label"
          >Summary or Description</label
        >
        <textarea
          class="form-control"
          id="exampleFormControlTextarea1"
          rows="3"
        ></textarea>
      </div>
      <div class="mb-3">
        <label for="formFile" class="form-label">Poster</label>
        <input class="form-control" type="file" id="formFile" />
      </div>
      <div class="col-auto">
        <button type="submit" class="btn btn-primary mb-3">Submit</button>
      </div>
    </form>
  </div>
</template>