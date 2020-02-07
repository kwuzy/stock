import React, { useState } from 'react';
import Button from '@material-ui/core/Button';
import Input from '@material-ui/core/Input';


export default function Stock() {
    const [ stock, setStock ] = useState(null);

    function handleStockChange(event) {
        setStock(event.target.value);
        console.log(stock);
    }

    function handleSearch(event) {
        console.log(`Stock is: ${stock}`);
    }

    return (
        <div>
            <div className="stock-input">
                <div><Input placeholder="Ticker Symbol" onChange={handleStockChange} /></div>
                <div className="submit-button"><Button onClick={handleSearch} color="primary" variant="outlined">Load</Button></div>
            </div>
        </div>
    )
}