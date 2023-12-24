import React from 'react'
import LogIn from '../../assets/SVG.png'
import scss from './LogInBlock.module.scss'

const LogInBlock = () => {
  return (
    <div className={scss.section}>
      <img src={LogIn} alt="" className={scss.img}/>
      <div className={scss.button}>
        <p className={scss.text_wrapper}>Зарегистрируйтесь</p>
      </div>
    </div>
  )
}

export default LogInBlock