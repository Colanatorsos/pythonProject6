import React from 'react'
import Header from '../components/Header/Header'
import FilterComp from '../components/Filter/Filter'
import SearchPanel from '../components/SearchPanel/SearchPanel'
import scss from './Filter.module.scss'

const Filter = () => {
  return (
    <>
      <Header />
      <section style={{display: 'flex', flexDirection: 'column', alignItems: 'center'}}>
        <SearchPanel/>
        <FilterComp/>
        
      </section>
    </>
  )
}

export default Filter