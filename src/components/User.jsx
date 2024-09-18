import React, { useEffect, useState } from "react";
import Log from "./Log";
import { NavLink, useLocation } from "react-router-dom";


function User() {
    const location = useLocation();
    const { userInfo } = location.state || {}; 
    const { name, email, id } = userInfo || {};
    const [logs, setLogs] = useState([]);


    useEffect(() => {
        if (id) { 
            const fetchLogs = async () => {
                try {
                    const response = await fetch(`http://127.0.0.1:5000/user/all-logs/${id}`);
                    if (!response.ok) {
                        throw new Error(`Error: ${response.status}`);
                    }
                    const data = await response.json();
                    setLogs(data);
                } catch (error) {
                    console.error("Error fetching logs:", error);
                }
            };

            fetchLogs();
        }
    }, [id]);  


    if (!userInfo) {
        return <h6>No user information found. Please log in.</h6>;
    }


    return (
        <>
            <NavLink to='/home'>Log out</NavLink>
            <h6>Welcome
                <strong>
                <hr/>
                    {name}                    
                <hr/>
                </strong>
            </h6>
            
            <h3>Your Logs:</h3>
            <ul>
                {logs.length > 0 ? (
                    logs.map((log) => (
                        <li key={log.id}>
                            {log.log}
                        </li>
                    ))
                ) : (
                    <p>No logs found</p>
                )}
            </ul>
            <Log foreign_id={id} logs={logs} setLogs={setLogs} />
        </>
    );
}

export default User;

