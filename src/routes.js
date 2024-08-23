import Main from "./components/Main"
import Home from "./components/Home"
import Readme from "./components/Readme"

const routes = [
    {
        path : "/",
        element : <Main/>,
        errorElement : <h1>Broken Page !</h1>,
        children : [
            {
                path : "home",
                element : <Home/>
            },
            {
                path : "readme",
                element : <Readme/>
            }
        ]
    },
]

export default routes
