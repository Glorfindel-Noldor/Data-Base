import { NavLink } from "react-router-dom";

function Navbar(){

    return(
        <nav>
            <NavLink to='/home'     >Home </NavLink>
            <NavLink to='/readme'   >README.md</NavLink>
            {/* <NavLink></NavLink> */}
        </nav>
    )
}

export default Navbar
