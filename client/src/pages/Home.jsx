import React from "react";
import { Link } from "react-router-dom";

const Home = () => {
  return (
    <div>
      <h1>Hello world!</h1>
      <Link to="/signup">Signup</Link>
    </div>
  );
};

export default Home;
