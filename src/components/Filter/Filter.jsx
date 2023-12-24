import React from 'react'
import scss from './Filter.module.scss'
import Arrow from '../../assets/arrow.svg'

const Filter = () => {
  return (
    <form className={scss.Filter}>
      <div>
        <div className={scss.Filter__block}>
          <p>Радиус</p>
          <input type="text" placeholder='Укажите радиус в метрах' />
        </div>
        <div className={scss.Filter__block}>
          <p>Тип недвижимости</p>
          <select name="" id="">
            <option value="любое">любое</option>
          </select>
        </div>
        <div className={scss.Filter__block}>
          <p>Комнаты</p>
          <div>
            <select name="" id="">
              <option value="любое">любое</option>
            </select>
            <select name="" id="">
              <option value="любое">любое</option>
            </select>
          </div>
        </div>
        <div className={scss.Filter__block}>
          <p>Цена</p>
          <div>
            <select name="" id="">
              <option value="любое">любое</option>
            </select>
            <select name="" id="">
              <option value="любое">любое</option>
            </select>
          </div>
        </div>
        <div className={scss.Filter__block}>
          <p>По дате добавления</p>
          <select name="" id="">
            <option value="любое">любое</option>
          </select>
        </div>
        <div className={scss.Filter__checkbox}>
          <input type="checkbox" />
          <p>Включая арендованные жилье</p>
        </div>
      </div>
      <div className={scss.buttons}>
        <button>Очистить</button>
        <button>Найти жилье</button>
      </div>
    </form>
  )
}

export default Filter