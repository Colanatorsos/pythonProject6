import React from "react";
import Header from '../components/Header/Header'
import Ramification from '../components/Ramification/Ramification'
import LogInBlock from '../components/LogInBlock/LogInBlock'
import DivRecentsearches from '../components/DivRecentsearches/DivRecentsearches'

const Home = () => {
  return (
    <>
      <Header />
      <Ramification />
      <LogInBlock />
      <DivRecentsearches />
    </>
  )
}

export default Home