<template>
  <div>
    <div v-if="place_order_flag == 0">
      <button
        type="submit"
        @click="toggle_place_order"
        class="btn btn-dark btn-lg btn-block"
      >
        Gimmy my number! Now!
      </button>
    </div>

    <div v-if="place_order_flag == 1">
      <b-form @submit="send_order">
        <b-form-group id="fname" label="First Name:" label-for="fname">
          <b-form-input
            id="fname"
            v-model="$store.state.fname"
            required
          ></b-form-input>
        </b-form-group>

        <b-form-group id="lname" label="Last name:" label-for="lname">
          <b-form-input
            id="lname"
            v-model="$store.state.lname"
            required
          ></b-form-input>
        </b-form-group>

        <b-form-group
          id="email"
          label="Email address:"
          label-for="email"
          description="We'll never share your email with anyone else."
        >
          <b-form-input
            id="email"
            v-model="$store.state.email"
            type="email"
            placeholder="user@example.com"
            required
          ></b-form-input>
        </b-form-group>

        <b-form-group
          id="fib_idx"
          label="Requested Fibonacci number(idx):"
          label-for="fib_idx"
        >
          <b-form-input
            id="fib_idx"
            v-model="fib_idx"
            type="number"
            required
          ></b-form-input>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
      <p />
      <button
        type="submit"
        @click="toggle_place_order"
        class="btn btn-dark btn-lg btn-block"
      >
        Hide this shit!
      </button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "PlaceOrder",
  data: function () {
    return {
      place_order_flag: 0,
      fib_idx: 0,
    };
  },
  methods: {
    toggle_place_order: function () {
      this.place_order_flag = this.place_order_flag == 1 ? 0 : 1;
    },

    send_order: function (event) {
      event.preventDefault();
      this.place_order_flag = this.place_order_flag == 1 ? 0 : 1;
      this.$store.commit("set_contact_params");

      const data = {
        e_mail: "cost@example.pl",
        fib_index: 4,
        firstname: "Jan",
        lastname: "Kowalski",
      };
      const headers = {
        "Content-Type": "application/json",
      };
      const url = this.$store.state.place_order_url;

      axios.post(url, data, { headers: headers }).then(
        (res) => {
          const body = JSON.parse(res.data.body);
          console.log(body);
          alert(
            "Request status: " +
              body.status +
              "\nRequested fibonacci number: " +
              this.fib_idx +
              "\nRequest id: " +
              body.id
          );
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

