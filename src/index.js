import React from 'react';
import ReactDOM from 'react-dom/client';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import routes from './routes';

const rout = createBrowserRouter(routes);

const root = ReactDOM.createRoot(document.getElementById('root'));

root.render(<RouterProvider router={rout} />);
