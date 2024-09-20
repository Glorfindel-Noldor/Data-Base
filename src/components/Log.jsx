import React, { useState } from "react";

function Log({ foreign_id, userName, setLogs }) {
    const [newLog, setNewLog] = useState({
        log: "",
        email: ""
    });
    const { log, email } = newLog;
    const [showEmailInput, setShowEmailInput] = useState(false);

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
                    log: ""
                });
            });
    };

    const handleEmailForm = (e) => {
        e.preventDefault();
        
        fetch(`http://127.0.0.1:5000/user/update/${foreign_id}`,
            {
                method: 'PUT',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    "id": foreign_id,
                    "name": userName,
                    "email": email
                }),
            }
        )
            .then(res => {
                if (!res.ok) {
                    throw new Error(`Error: ${res.status}`);
                }
                return res.json();
            })
            .then(() => {
                alert(`User updated email to:\n${email}`)
            })
            .catch(error => console.log(error))
            .finally(() => {
                setNewLog(prevState => ({
                    ...prevState,
                    email: ""
                }));
            });
    };

    return (
        <>
            <p>Create some logs!</p>
            <form onSubmit={handleForm}>
                <input className="glass" name="log" value={log} onChange={handleInput} placeholder="Add log" />
                <input className="glass" type="submit" value="Enter" />
            </form>
            <button className="to-bottom-center" onClick={() => setShowEmailInput(prevState => !prevState)}>
                {showEmailInput ? "Hide Email Update" : "Update Email"}
            </button>

            <div className="right-float">
                {showEmailInput && (
                    <form onSubmit={handleEmailForm}>
                        <input
                            className="glass"
                            type="email"
                            name="email"
                            value={email}
                            onChange={handleInput}
                            placeholder="Update email"
                        />
                        <input type="submit" value="Update" />
                    </form>
                )}
            </div>
        </>
    );
}

export default Log;

