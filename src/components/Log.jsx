import React, { useState } from "react";

function Log(foreign_id){
    const [newLog, setNewLog] = useState('')

    const handleInput = (e) => {
        const { value, name } = e.target;
        setNewLog(value)
    };


    return(
        <>
            <p>create some logs!</p>
            <form >
                <input className="glass" name="newLog" value={newLog} onChange={handleInput} placeholder="whats on your mind ?"/>
                <input className="glass" type="submit" value={'enter'}/>
            </form>
        </>

    )
}
export default Log