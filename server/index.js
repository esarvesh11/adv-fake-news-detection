const express = require("express");
const app = express();
const cors = require("cors");
require("dotenv").config();

const userRoutes = require("./routes/userRoutes");
const newsRoutes = require("./routes/newsRoutes");
const chartRoutes = require("./routes/chartRoutes");

const { default: mongoose } = require("mongoose");
mongoose
  .connect(process.env.MONGODB_URL)
  .then(() => {
    console.log("Connected to MONGODB successfully");
  })
  .catch((err) => {
    console.log("Couldn't connect to db");
    console.log(err);
  });

app.use(cors());
app.use(express.json());

app.use("/api/user", userRoutes);
app.use("/api/news/", newsRoutes);
app.use("/api/charts/", chartRoutes);

const server = app.listen("4000", () => {
  console.log("ON PORT 4000");
});
