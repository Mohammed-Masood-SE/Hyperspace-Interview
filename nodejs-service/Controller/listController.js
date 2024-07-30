import listService from "../Services/listService.js"

let listController = {}

listController.getList = async(req,res)=>{
    try{

        let list = await listService.getList()
        if(list.length){
            res.status(200).json(list)
        }else{
            res.status(404).json({message:"List Not Found"})
        }

    }catch(error){
        res.status(500).json({message:"Internal Server Error"})
    }
}

export default listController