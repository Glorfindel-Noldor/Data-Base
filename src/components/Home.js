import React from "react";
import { useOutletContext } from 'react-router-dom';

function Home(){
    const text = useOutletContext()

    return(
        <>
            <h1>{text}</h1>
        </>
    )
}
export default Home

