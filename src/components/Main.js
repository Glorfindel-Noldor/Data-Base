import React, { useEffect, useState } from "react";
import { Outlet } from "react-router";
import Navbar from "./Navbar";
const API_ALL_USERS = 'http://127.0.0.1:5000/all-users'; 


function Main() {
    const [userLogs, setUserLogs] = useState([]);


    useEffect(() => {
        fetch(API_ALL_USERS)
            .then((res) => {
                if (!res.ok) {
                    throw Error(`Server responded with status ${res.status}`);
                }
                return res.json(); 
            })
            .then((data) => {
                console.log('Fetched users:', data);
                setUserLogs(data);
            })
            .catch((error) => {
                console.error(`Fetch error: ${error.message}`);
            });
    }, []);


    return (
        <>
            <Navbar />
            <Outlet context={{ userLogs, setUserLogs }} />
        </>
    );
}

export default Main;

