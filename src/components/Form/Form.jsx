import React from 'react'
import scss from './Form.module.scss'

const Form = () => {
  return (
    <form action="" className={scss.Form}>
      <input type="text" placeholder='Бишкек' />
      <button>Фильтры</button>
    </form>
  )
}

export default Form