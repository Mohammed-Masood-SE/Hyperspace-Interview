import express from "express"
import cors from 'cors';

const app = express()

app.use(cors());
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

// Setting up routes
import listRouter from "../Routes/listRouter.js";
app.use("/api/list",listRouter)


export default app