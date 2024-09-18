import { toBeEmptyDOMElement } from "@testing-library/jest-dom/matchers";
import React, { useEffect } from "react";
import { json, useOutletContext } from 'react-router-dom';

function Home() {
    const { users, logs, setLogs, BASE_LINK } = useOutletContext();

    




    return (
        <>
            <header>Welcome</header>
            <div>
            </div>
        </>
    );
}

export default Home;


