import React, { useEffect, useState } from "react";
import { Outlet } from "react-router";
import Navbar from "./Navbar";
const BASE_LINK = 'http://127.0.0.1:5000'; 


function Main() {
    const [users, setUsers] = useState([])
    const [logs, setLogs] = useState([])


    useEffect(() => {

        const GET = {
            method: 'GET',
            headers: {
              'Accept': 'application/json',
              'Content-Type': 'application/json'
            }
        }
        
        fetch(BASE_LINK + '/all-users',GET)
            .then((res) => {
                if (!res.ok) {
                    throw Error(`Server responded with status ${res.status}`);
                }
                return res.json(); 
            })
            .then((data) => (
                setUsers(data)
            ))
            .catch((error) => {
                console.error(`Fetch error: ${error.message}`);
            });
    }, []);


    return (
        <>
            <Navbar />
            <Outlet context={{ users, logs, setLogs, BASE_LINK }} />
        </>
    );

    
}


export default Main;

















    // const PUT = (edit)=> {
    //     method: 'PUT',
    //     headers: {
    //       'Accept': 'application/json',
    //       'Content-Type': 'application/json'
    //     },
    //     body: JSON.stringify(edit)
    // }