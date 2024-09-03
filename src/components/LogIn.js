import React from "react";
import { NavLink } from "react-router-dom";

function LogIn(){

    return(
        <div className="hello-background">
        <form>
            <input id="glass"  type="text" placeholder="name"/>
            <input id="glass" type="email" placeholder="email"/>
            <br/>
            <NavLink to='/create-user'> create user</NavLink>
        </form>
        </div>
    )
}

export default LogIn

