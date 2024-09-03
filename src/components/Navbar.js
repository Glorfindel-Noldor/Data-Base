import { NavLink } from "react-router-dom";

function Navbar(){

    return(
        <nav>
            <NavLink to='/home'     >Home </NavLink>
            <NavLink to='/log-in'>LogIn </NavLink>
            <NavLink className='right-float' to='/readme'>help</NavLink>
        </nav>
    )
}

export default Navbar

