import React from 'react'
import scss from './LogIn.module.scss'

const LogIn = () => {
  return (
    <form className={scss.Form}>
      <h1>Зарегистрируйте аккаунт</h1>
      <div>
        <div>
          <p>Адрес электронной почты</p>
          <input type="email" />
        </div>
        <div>
          <p>Пароль</p>
          <input type="password" />
        </div>
      </div>
      <button>Продолжить</button>
    </form>
  )
}

export default LogIn