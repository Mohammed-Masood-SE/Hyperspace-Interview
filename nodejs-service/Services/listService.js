import axios from "axios"

let listService = {}

listService.getList = async()=>{
    try{

        let response =await axios.get(`${process.env.PYTHON_SERVICE_URL}/languages`)
        return response.data

    }catch(error){
        throw error
    }
}

export default listService