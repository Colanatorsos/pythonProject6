import { Route, Routes } from "react-router-dom";
import Home from "./Pages/Home";
import SignIn from "./Pages/SignIn";
import Filter from "./Pages/Filter";
import './global.css'
import Product from './Pages/Product';
import Settings from "./Pages/Settings";

const App = () => {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/signin" element={<SignIn />} />
      <Route path="/filter" element={<Filter />} />
      <Route path="/product" element={<Product />} />
      <Route path="/settings" element={<Settings />} />
    </Routes>
  );
};

export default App;
