import React from 'react'
import scss from './Ramification.module.scss'

const Ramification = () => {
  return (
    <div className={scss.section}>
      <div className={scss.heading}>
        <div className={scss.text_wrapper}>Верь в то, чтобы найти это.</div>
      </div>
      <div className={scss.wrapper}>
        <p className={scss.div}>Ищите недвижимость на продажу и в аренду <br /> в Кыргызстане</p>
      </div>
      <div className={scss.link}>
        <button className={scss.text_wrapper_2}>Продажа</button>
        <button className={scss.text_wrapper_3}>Покупка</button>
      </div>
    </div>
  )
}

export default Ramification