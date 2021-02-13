<template>
  <div class>
    <div v-if="results_flag == 0">
      <button
        type="submit"
        @click="show_results"
        class="btn btn-dark btn-lg btn-block"
      >
        Show my orders, hurry, hurry!
      </button>
    </div>
    <div v-if="results_flag == 1">
      <div
        v-if="!$store.getters.results_are_available"
        class="text-center mb-3"
      >
        <p>LOADING</p>
        <b-spinner
          style="width: 3rem; height: 3rem"
          wariant="primary"
        ></b-spinner>
      </div>
      <p>
        <button
          type="submit"
          @click="hide_results"
          class="btn btn-dark btn-lg btn-block"
        >
          GO TO HELL, I'm Bored!
        </button>
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: "Results",
  data: function () {
    return {
      results_flag: 0,
      fib_idx: 0,
    };
  },
  methods: {
    show_results: function () {
      this.results_flag = 1;
    },
    hide_results: function () {
      this.results_flag = 0;
    },
  },
};
</script>
