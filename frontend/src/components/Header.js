import React from 'react'
import '../styles/header.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faArrowRight } from '@fortawesome/free-solid-svg-icons'



const Header = () => {
  return (
    <div className='header_container'>
       <h1 className='header_text'>Explore our new products <br />and  antique thing.....</h1>
       <h4 className='header_text2'>Get the best deals on every product/Things.</h4>
       <div className='btn_container'>
        <button className='view_all_btn1'>New product</button>
        <button className='view_all_btn'>View all product<FontAwesomeIcon className='arrow' icon={faArrowRight} /></button>
       </div>      
    </div>
   
  )
}

export default Header;