import Main from "./components/Main"
import Home from "./components/Home"
import Readme from "./components/Readme"
import Broken from "./components/Broken"
import LogIn from "./components/LogIn"
import CreateUser from "./components/CreateUser"
import CreateLog from "./components/CreateLog"
import User from "./components/User"
import Log from "./components/Log"

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
            },
            {
                path : "new-log",
                element : <CreateLog/>
            },

        ]
    },
    {
        path : "user",
        element : <User/>,
        children : [
            {
                path: "log",
                element: <Log/>
            },
        ]
    }

]

export default routes
