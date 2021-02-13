<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/fib.png" width="30%" />
    <FibWorld msg="Welcome to Fibonacci World!" />
  </div>
</template>

<script>
import FibWorld from "./components/FibWorld.vue";

export default {
  name: "Fibb.Math",
  components: {
    FibWorld,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
