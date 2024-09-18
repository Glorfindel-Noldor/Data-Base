import React, { useState } from "react";

function Log({ foreign_id, logs, setLogs }) {
    const [newLog, setNewLog] = useState({
        log: "",
    });
    const { log } = newLog;

    const handleInput = (e) => {
        const { value, name } = e.target;
        setNewLog(prevState => ({
            ...prevState,
            [name]: value,
        }));
    };

    const handleForm = (e) => {
        e.preventDefault();

        const newPost = {
            log: log,
            foreign_id: foreign_id,
        };

        const POST = {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(newPost),
        };

        fetch(`http://127.0.0.1:5000/user/${foreign_id}/new-log`, POST)
            .then(res => {
                if (!res.ok) {
                    throw new Error(`Error: ${res.status}`);
                }
                return res.json();
            })
            .then(data => {

                setLogs(prevLogs => [...prevLogs, data]);
            })
            .catch((error) => {
                console.error("Post error, nothing posted:", error);
            })
            .finally(() => {
                setNewLog({
                    log: "",
                });
            });
    };

    return (
        <>
            <p>Create some logs!</p>
            <form onSubmit={handleForm}>
                <input className="glass" name="log" value={log} onChange={handleInput} placeholder="Add log" />
                <input className="glass" type="submit" value="Enter" />
            </form>
        </>
    );
}

export default Log;

