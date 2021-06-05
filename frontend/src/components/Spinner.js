import React from 'react'
import './Spinner.css'

const Spinner = () => (
    <div className="spinner__container">
        <div className="lds-ring">
            <div></div>
            <div></div>
            <div></div>
            <div></div>
        </div>
    </div>
)

export default Spinner
