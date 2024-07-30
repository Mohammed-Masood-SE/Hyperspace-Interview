import dotenv from "dotenv"
dotenv.config()

import app from "./Util/server.js"

app.listen(process.env.PORT,()=>console.log(`Server Started On Port ${process.env.PORT}`))