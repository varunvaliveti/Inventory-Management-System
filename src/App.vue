<template>
  <div id="app">
    <header>
      <h1>SQL Query Runner</h1>
    </header>
    <QueryRunner />
  </div>
</template>

<script>
import QueryRunner from "./components/QueryRunner.vue";

export default {
  components: {
    QueryRunner,
  },
};
</script>

<style>
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
}
header {
  background-color: #007bff;
  color: white;
  text-align: center;
  padding: 1rem 0;
}
</style>
 
