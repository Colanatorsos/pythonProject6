import React from 'react'
import scss from './SearchPanel.module.scss'

const SearchPanel = () => {
  return (
    <div className={scss.SearchPanel}>
      <h1>Недвижимость в <br /> Кыргызстане в аренду</h1>
      <h4>Введите название города</h4>
      <form>
        <input type="text" placeholder='Название города' />
      </form>
    </div>
  )
}

export default SearchPanel