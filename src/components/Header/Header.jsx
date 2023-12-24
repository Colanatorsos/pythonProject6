import React, { useState } from 'react'
import scss from './Header.module.scss'

import LogoSVG from '../../assets/logo.svg'
import Profile from '../../assets/Profile'
import { Link } from 'react-router-dom'


const Header = () => {
  const [active, setActive] = useState(false)
  return (
    <header className={scss.header}>
      <div className={scss.div_seo_header}>
        <span className={scss.div_seo_header_button} onClick={() => setActive(!active)}></span>
        {/*<Logo className={scss.div_seo_header_logo} />*/}
        <img src={LogoSVG} alt="" />
        <Profile className={scss.div_seo_header_profile} />
      </div>
      <div className={active ? scss.demo_active : scss.demo}>
        <Link to='/'>Главная</Link>
        <Link to='/filter'>Поиск</Link>
        <Link to='/signin'>Войти</Link>
        <Link to='/product'>Продукт</Link>
        <Link to='/settings'>Настройки</Link>
      </div>
    </header>
  )
}

export default Header