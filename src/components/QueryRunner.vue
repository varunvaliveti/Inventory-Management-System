<template>
  <div class="query-runner">
    <form @submit.prevent="runQuery">
      <textarea
        v-model="query"
        placeholder="Write your SQL query here..."
        rows="5"
        cols="50"
      ></textarea>
      <br />
      <button type="submit">Run Query</button>
    </form>

    <div class="results" v-if="results.length">
      <h2>Query Results:</h2>
      <table>
        <thead>
          <tr>
            <th v-for="(value, key) in results[0]" :key="key">{{ key }}</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(row, index) in results" :key="index">
            <td v-for="value in row" :key="value">{{ value }}</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="error" v-if="error">
      <h2>Error:</h2>
      <p>{{ error }}</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      query: "",
      results: [],
      error: null,
    };
  },
  methods: {
    async runQuery() {
      this.error = null;
      this.results = [];

      try {
        const response = await axios.post("http://127.0.0.1:5000/run_query", {
          query: this.query,
        });
        if (response.data.success) {
          this.results = response.data.results || [];
        } else {
          this.error = response.data.error || "An unknown error occurred.";
        }
      } catch (err) {
        this.error = err.message;
      }
    },
  },
};
</script>

<style>
.query-runner {
  padding: 2rem;
}
textarea {
  width: 100%;
  font-family: monospace;
}
button {
  margin-top: 1rem;
  padding: 0.5rem 1rem;
  background-color: #007bff;
  color: white;
  border: none;
  cursor: pointer;
}
button:hover {
  background-color: #0056b3;
}
table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 1rem;
}
th,
td {
  border: 1px solid #ddd;
  padding: 8px;
}
th {
  background-color: #f4f4f4;
}
.error {
  color: red;
  margin-top: 1rem;
}
</style>

