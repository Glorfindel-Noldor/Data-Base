import React, { useState } from "react";
import { useOutletContext } from "react-router";
const API = 'http://127.0.0.1:5000/new-user'


function CreateUser(){
    const {users, setUsers} = useOutletContext()
    const [inputForm , setInputForm] = useState({
        stateName: '',
        stateEmail: ''
    })
    const {stateName, stateEmail} = inputForm ;

    const handleChange = (e)=>{
        const {name, value} = e.target
        setInputForm((prevState)=>({
            ...prevState,
            [name]:value
        }))
    }

    const handleSubmit = (e)=>{
        e.preventDefault();

        if ( stateName.length < 2 || !stateName){
            return alert(`name must be larger than 2 characters long`)
        }

        if (stateName.length > 15){
            return alert(`name ${stateName} cannot surpass 15 characters`)
        }

        if (stateEmail.length < 2 || !stateEmail){
            return alert(`email must fit format 'yourinfo@serviceprovider.com'`)
        }

        const newJsonPost = {
            "name" : stateName,
            "email": stateEmail
        }

        const POST = {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'},
                'body': JSON.stringify(newJsonPost)
        }

        
        fetch(API,POST)
        .then((res) => {
            if (!res.ok) {
                throw new Error(`Server error: ${res.statusText}`);
            }
            return res.json();
        })
        .then((newPush)=>(setUsers([newPush,...users])))
        .catch((error)=>(
            console.log(`POST ERROR : ${error}`)
        ))
        .finally(() => {
            setInputForm({
                stateName : "",
                stateEmail : ""
            })
            alert(`You have added user ${stateName}`)
        })
    }

    return(
        <div className="new-user" >
            <form onSubmit={handleSubmit}>
                <input
                    id="glass"
                    type="text"
                    value={stateName}
                    name="stateName"
                    onChange={handleChange}
                    placeholder="full name"
                /><br/>

                <input 
                    id="glass"
                    type="email"
                    value={stateEmail}
                    name="stateEmail"
                    onChange={handleChange}
                    placeholder="email"
                /><br/>
                <input type="submit" value="create!"/>
            </form>
        </div>
    )
}
export default CreateUser

