import React from 'react'
import scss from './DivRecentsearches.module.scss'

const DivRecentsearches = () => {
  return (
    <div className={scss.div_recentsearches}>
      <div className={scss.heading}>
        <div className={scss.text_wrapper}>Последние просмотры</div>
      </div>
      <div className={scss.p_recentsearches}>
        <p className={scss.div}>У вас нету последних просмотров</p>
      </div>
    </div>
  )
}

export default DivRecentsearches