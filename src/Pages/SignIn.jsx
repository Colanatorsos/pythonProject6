import React from 'react'
import Header from '../components/Header/Header'
import LogIn from '../components/LogIn/LogIn'
import SignSvg from '../assets/signin.svg'

const SignIn = () => {
  return (
    <>
      <Header />
      <section style={{height: '94dvh', background: '#FFF'}}>
        <LogIn />
        <div style={{ width: '100%', display: 'flex', justifyContent: 'center', marginTop: '27px' }}>
          <img src={SignSvg} alt="" />
        </div>
      </section>
    </>
  )
}

export default SignIn