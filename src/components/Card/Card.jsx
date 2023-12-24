import React from 'react'
import scss from './Card.module.scss'
import photoOne from '../../assets/photo1.png'
import { FaPhoneAlt } from "react-icons/fa";
import { CiHeart } from "react-icons/ci";

const Card = () => {
  const data = {
    img: [],
    title: 'Бишкек, Парк Ататюрк, Масануева 58',
    desc: '3 комнаты',
    new: true,
    added: '11.12.2023'
  }
  return (
    <div className={scss.Card}>
      <div className={scss.Card__imgs}>
        <img src={photoOne} alt="" />
        <div>
          <img src={photoOne} alt="" />
          <img src={photoOne} alt="" />
          <img src={photoOne} alt="" />
        </div>
      </div>
      <div className={scss.Card__info}>
        <div className={scss.Card__info_price}>
          <div>
            <h3>4,000,000 COM</h3>
            <p>ЦЕНА</p>
          </div>
          <button>ОТКРЫТЬ</button>
        </div>
        <div className={scss.Card__info_desc}>
          <div className={scss.Card__info_desc_name}>
            <h5>{data.title}</h5>
            <p>{data.desc}</p>
            <p>{data.new ? 'новый' : null}</p>
          </div>
          <div className={scss.Card__info_desc_nav}>
            <p>Добавлено {data.added}</p>
            <div>
              <a href="/"><FaPhoneAlt />Позвонить</a>
              <a href="/"><CiHeart />Сохранить</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Card