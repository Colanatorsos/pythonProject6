import React from 'react'
import Header from '../components/Header/Header'
import { Link } from 'react-router-dom'
import { FaLongArrowAltLeft } from "react-icons/fa";
import { IoMdExit } from "react-icons/io";
import { FaArrowRightLong } from "react-icons/fa6";
import scss from './Settings.module.scss'

const Settings = () => {
  return (
    <>
      <Header />
      <div className={scss.Back}>
        <Link to='/'><FaLongArrowAltLeft color='#11828d' />My Rightmove home</Link>
      </div>
      <section className={scss.Settings__categories}>
        <div className={scss.Settings__categories__header}>
          <h1>Account details</h1>
          <Link><IoMdExit />Sign out</Link>
        </div>
        <ul className={scss.Settings__categories__list}>
          <li>Personal details <FaArrowRightLong /></li>
          <li>Profile <FaArrowRightLong /></li>
          <li>Contact preferences <FaArrowRightLong /></li>
          <li>Account settings <FaArrowRightLong /></li>
        </ul>
      </section>
      <section className={scss.Settings__subcategories}>

      </section>
    </>
  )
}

export default Settings