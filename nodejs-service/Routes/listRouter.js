import express from "express"
import listController from "../Controller/listController.js"

let listRouter = express.Router()

listRouter.get("/get-list",listController.getList)

export default listRouter