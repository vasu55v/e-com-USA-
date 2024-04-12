import Home from './pages/Home';
import {BrowserRouter,Routes,Route,Navigate} from "react-router-dom";
// import Register from './pages/Register';
import NotFound from './pages/NotFound';



function App() {
  return (
    <div>
   <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />




        {/* <Route path="/login" element={<Login />} />
        <Route path="/logout" element={<Logout />} /> */}
        <Route path="/NotFound" element={<NotFound />} />
        {/* <Route path="/register" element={<Register />} /> */}

      </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
