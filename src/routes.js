import Main from "./components/Main"
import Home from "./components/Home"
import Readme from "./components/Readme"
import Broken from "./components/Broken"
import LogIn from "./components/LogIn"
import CreateUser from "./components/CreateUser"

const routes = [
    {
        path : "/",
        element : <Main/>,
        errorElement : <Broken/>,
        children : [
            {
                path : "home",
                element : <Home/>
            },
            {
                path : "readme",
                element : <Readme/>
            },
            {
                path : "log-in",
                element : <LogIn/>
            },
            {
                path : "create-user",
                element : <CreateUser/>
            }
        ]
    },
]

export default routes
