<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h3>Wanna something, huh?</h3>
    <PlaceOrder />
    <p />
    <Results />
  </div>
</template>

<script>
import PlaceOrder from "./PlaceOrder.vue";
import Results from "./Results.vue";

export default {
  name: "FibWorld",
  components: {
    PlaceOrder,
    Results,
  },
  props: {
    msg: String,
  },
  data: function () {
    return {
      place_order_flag: 0,
      results_flag: 0,
      fib_idx: 0,
    };
  },
  methods: {
    toggle_place_order: function () {
      this.place_order_flag = this.place_order_flag == 1 ? 0 : 1;
    },

    toggle_results: function () {
      this.results_flag = this.results_flag == 1 ? 0 : 1;
    },

    send_order: function (event) {
      event.preventDefault();
      this.place_order_flag = this.place_order_flag == 1 ? 0 : 1;
      this.$store.commit("set_contact_params");
      alert(
        "I wish I know how to send your order, sir for #" +
          this.fib_idx +
          " Fibonacci number."
      );
    },
  },
};
</script>
