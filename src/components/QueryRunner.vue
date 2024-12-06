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

    <!-- Bar Chart for Sales by Month -->
    <div class="chart">
      <h2>Sales by Month</h2>
      <Bar
        :data="monthlySalesData"
        :options="chartOptions"
      />
    </div>

    <!-- Pie Chart for Sales by Vendor -->
    <div class="chart">
      <h2>Sales by Vendor</h2>
      <Pie
        :data="vendorSalesData"
        :options="chartOptions"
      />
    </div>

    <!-- Bar Chart for Customer Spending -->
    <div class="chart">
      <h2>Customer Spending</h2>
      <Bar
        :data="customerSpendingData"
        :options="chartOptions"
      />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { Bar, Pie } from "vue-chartjs";
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
  ArcElement,
} from "chart.js";

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale, ArcElement);

export default {
  components: {
    Bar,
    Pie,
  },
  data() {
    return {
      chartOptions: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          display: true,
          position: 'top'
        },
        title: {
          display: false
        }
      },
      scales: {
        y: {
          beginAtZero: true
        }
      }
    },
      query: "",
      results: [],
      error: null,
      monthlySalesData: {
        labels: ["October 2024", "November 2024"],
        datasets: [
          {
            label: "Sales ($)",
            data: [1448.97, 4109.95],
            backgroundColor: "rgba(75, 192, 192, 0.6)",
          },
        ],
      },
      vendorSalesData: {
        labels: ["NVIDIA", "AMD", "ASUS", "MSI"],
        datasets: [
          {
            label: "Sales by Vendor ($)",
            data: [4799.97, 1399.98, 499.99, 389.97],
            backgroundColor: ["#FF6384", "#36A2EB", "#FFCE56", "#4BC0C0"],
          },
        ],
      },
      customerSpendingData: {
        labels: ["Alice Johnson", "Bob Smith", "Charlie Davis", "Diana Carter", "Ethan Hunt"],
        datasets: [
          {
            label: "Customer Spending ($)",
            data: [3199.98, 699.99, 499.99, 389.97, 499.98],
            backgroundColor: "rgba(153, 102, 255, 0.6)",
          },
        ],
      },
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
          this.error = response.data.error;
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
  padding: 20px;
}

.chart {
  margin: 4rem auto; 
  width: 600px;
  height: 400px;
  position: relative;
  background: white;
  padding: 20px;
  box-shadow: 0 0 10px rgba(0,0,0,0.1);
}


.chart canvas {
  width: 100% !important;
  height: 100% !important;
}
</style>

