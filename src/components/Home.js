import React, { useState, useEffect } from "react";
import { useOutletContext } from 'react-router-dom';

function Home() {
    const { userLogs, setUserLogs } = useOutletContext();
    const [logs, setLogs] = useState({});


    const fetchUserLogs = (userId) => {
        const userLogsApi = `http://127.0.0.1:5000/user/all-logs/${userId}`;
        
        fetch(userLogsApi)
            .then(res => res.json())
            .then(data => {
                setLogs((prevLogs) => ({
                    ...prevLogs,
                    [userId]: data
                }));
            })
            .catch(error => {
                console.error(`Error fetching logs for user ${typeof(userId)}:`, error);
            });
    };

    const handleDelete = (user) => {
        const deleteApi = `http://127.0.0.1:5000/user/delete/${user.id}/`;

        const DELETE = {
            method: 'DELETE',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
        };

        fetch(deleteApi, DELETE)
            .then((res) => {
                if (res.ok) {
                    return res.json();
                } else {
                    console.error(`Failed to delete user. Status: ${res.status}`);
                    throw new Error(`Failed to delete user with status ${res.status}`);
                }
            })
            .then(() => {
                setUserLogs((prevLogs) => prevLogs.filter(compareUsers => compareUsers.id !== user.id));
                setLogs((prevLogs) => {
                    const updatedLogs = { ...prevLogs };
                    delete updatedLogs[user.id]; // Remove logs for the deleted user
                    return updatedLogs;
                });
            })
            .catch((error) => console.error(`Error trying to delete: ${error}`))
            .finally(() => {
                alert(`User named: ${user.name} deleted!`);
            });
    };

    const user_names = (
        <ol>
            {userLogs.map((user) => (
                <li key={user.id}>
                    {user.name}
                    <button onClick={() => handleDelete(user)}> X</button>
                    <br />
                    {fetchUserLogs(user.id)}
                    <ul>
                        {logs[user.id] ? logs[user.id].map(log => (
                            <li key={log.id}>{log.log}</li>
                        )) : 'No logs loaded yet'}
                    </ul>
                    <hr />
                </li>
            ))}
        </ol>
    );

    return (
        <>
            <header>Welcome</header>
            <div>
                users: {userLogs ? user_names : <h1><br />loading...</h1>}
            </div>
        </>
    );
}

export default Home;