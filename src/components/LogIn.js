import React, { useState } from "react";
import { NavLink, useNavigate } from "react-router-dom";

const API = 'http://127.0.0.1:5000/all-users';

function LogIn() {
    const [inputForm, setInputForm] = useState({
        name: "",
        email: ""
    });
    const { name, email } = inputForm;
    const navigate = useNavigate();

    const eventInput = (e) => {
        const { value, name } = e.target;
        setInputForm(prevState => ({
            ...prevState,
            [name]: value
        }));
    };

    const eventSubmit = (e) => {
        e.preventDefault();

        fetch(API)
            .then(res => res.json())
            .then(data => {
                try {
                    // Find the user where both email and name match
                    const matchedUser = data.find(user => user.email.toLowerCase() === email.toLowerCase() && user.name.toLowerCase() === name.toLowerCase());
                    
                    if (matchedUser) {
                        setInputForm({
                            name: "",
                            email: ""
                        });


                        navigate('/user', {
                            state: {
                                userInfo: {
                                    "id": matchedUser.id,
                                    "name": matchedUser.name,
                                    "email": matchedUser.email
                                }
                            }
                        });
                    } else {

                        setInputForm({
                            name: "",
                            email: ""
                        });
                        alert(`User ${name} NOT found!`);
                    }
                } catch (error) {
                    console.log(`Error: ${error.toString()}`);
                }
            })
            .catch(error => console.log(`Fetch error: ${error.toString()}`));
    };

    return (
        <div className="hello-background">
            <form onSubmit={eventSubmit}>
                <input id="glass" type="text" value={name} onChange={eventInput} name="name" placeholder="name" />
                <input id="glass" type="email" value={email} onChange={eventInput} name="email" placeholder="email" />
                <input id="glass" type="submit" value="enter" />
                <br />
                <NavLink to='/create-user'>Create user</NavLink>
            </form>
        </div>
    );
}

export default LogIn;