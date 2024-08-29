import React, { useEffect, useState } from "react";
import { Outlet } from "react-router";
import Navbar from "./Navbar";
const API_ALL_USERS = '/user/all-users'

function Main(){

    const [ userLogs , setUserLogs ] = useState([])

    useEffect(()=>{ //default GET
        fetch(API_ALL_USERS)
        .then((res)=>(res.json()))
        .then((data)=>(setUserLogs(data)))
        .catch((error)=>(
            console.log(`sorry error fetch in...\n'${API_ALL_USERS}'\t:\t${error}`)
        ))

    },[])


    return(
        <>
            <Navbar/>
            <Outlet context={userLogs}/>
        </>
    )
}
export default Main

