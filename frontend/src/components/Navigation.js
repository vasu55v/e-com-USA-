import React from 'react'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faBars ,faCartShopping } from '@fortawesome/free-solid-svg-icons';
import "../styles/navigation.css"

const Navigation = () => {

  const open=()=>{
    document.getElementById("main_nav_container").style.display="block";
    document.getElementById("main_nav_container").style.width="500px";
    document.getElementById("bar_icon").style.display="none";
  }

  
  const close=()=>{
    document.getElementById("main_nav_container").style.display="none";
    document.getElementById("bar_icon").style.display="block";
  }

  return (
    <div className="container">
    <h1 className="logo" id="logo"><a href="">Shop.me</a></h1>
    <div className="main_nav_container" id="main_nav_container">
    <span className='close_btn' onClick={close}>X</span>
     <nav className="nav_div">
        <ul className="ul_list">
            <li><a href=''>Home</a></li>
            <li><a href=''>Products</a></li>
            <li><a href=''>Cart</a></li>
            <li><a href=''>Logout</a></li>
            <li><a href=''>About Us</a></li>
        </ul>
     </nav>
     </div>
     <span className="open-nva-icon">
           <FontAwesomeIcon icon={faCartShopping} className='shopping_cart' />
           <FontAwesomeIcon icon={faBars} className="bar_icon" id="bar_icon" onClick={open} style={{fontSize:"35px"}} /> 
    </span>
    </div>
  )
}

export default Navigation;