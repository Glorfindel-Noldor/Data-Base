import React from "react";
import { useOutletContext } from 'react-router-dom';


function Home() {
    const { users, /*logs, setLogs, BASE_LINK*/ } = useOutletContext();

    
    const userList = users.map((user)=>(
        <h4 key={user.id}>{user.name}</h4>
    ))


    return (
        <>
            <p>our users:</p>
            <br/><hr/>
            {userList}
        </>
    );
}


export default Home;

