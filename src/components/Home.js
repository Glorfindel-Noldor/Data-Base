import React from "react";
import { useOutletContext } from 'react-router-dom';

function Home(){
    const userLogs = useOutletContext()

    const user_names = userLogs.map((user)=>(<h6 key={user.id}>{user.name}</h6>))


    return(
        <>
            <header>welcome</header>
            <div>users: {user_names}</div>
        </>
    )
}
export default Home

