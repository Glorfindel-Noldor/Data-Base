import React from "react";
import { Outlet } from "react-router";
import Navbar from "./Navbar";

function Main(){

    const text = "Hello, World!"

    return(
        <>
            <Navbar/>
            <Outlet context={text}/>
        </>
    )
}
export default Main

