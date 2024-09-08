import React from "react";
import { useOutletContext } from 'react-router-dom';

function Home() {
    const { userLogs, setUserLogs } = useOutletContext();

    if (userLogs) {
        console.log(`true from Home.js`);
    } else {
        console.log(`false from Home.js`);
    }

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
                    {user.name} <button onClick={() => handleDelete(user)}>x</button>
                </li>
            ))}
        </ol>
    );

    return (
        <>
            <header>Welcome</header>
            <div>
                users: {userLogs ? user_names : <h1><br/>loading...</h1>}
            </div>
        </>
    );
}

export default Home;

