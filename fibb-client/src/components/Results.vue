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
        v-if="!$store.getters.check_results_are_available"
        class="text-center mb-3"
      >
        <p>LOADING</p>
        <b-spinner
          style="width: 3rem; height: 3rem"
          wariant="primary"
        ></b-spinner>
      </div>
      <div v-else>
        {{ $store.state.results }}
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
import axios from "axios";
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
      this.fetch_results();
    },
    hide_results: function () {
      this.results_flag = 0;
    },

    fetch_results: function () {
      //event.preventDefault();
      this.$store.commit("declare_results_are_unavailable");

      const data = {
        e_mail: this.$store.state.email,
      };
      const headers = {
        "Content-Type": "application/json",
      };
      const url = this.$store.state.results_url;

      axios.post(url, data, { headers: headers }).then(
        (res) => {
          this.$store.state.results = JSON.parse(res.data.body);
          console.log(this.$store.state.results);
          this.$store.commit("declare_results_are_available");
        },
        (err) => {
          alert("Place Order API Error response: " + err);
          console.log("Place Order API response: ", err);
        }
      );
    },
  },
};
</script>
