import React from "react";
import { useOutletContext } from 'react-router-dom';


function Home() {
    const { userLogs } = useOutletContext();

    const user_names = (
        <ol>
            {userLogs.map((user) => (
                <li key={user.id}>{user.name}</li>
            ))}
        </ol>
    );


    if (userLogs){
        console.log(`true from Home.js`)
    }else{
        console.log(`false from Home.js`)
    }

    
    return (
        <>
            <header>Welcome</header>
            <div >
                users: {userLogs ? user_names :  <h1><br/>loading...</h1>}
            </div>
        </>
    );
}

export default Home;

