import React, { Component } from 'react';

import CryptoPrices from './CryptoPrices';

const cryptoPrices = new CryptoPrices();

class CryptoPricesList extends Component {
    constructor(props) {
        super(props);

        this.state = {
            prices: []
        }
    }

    componentDidMount() {
        var  self  =  this;
        cryptoPrices.getPrices().then(function (result) {
            console.log(result);
            self.setState({ prices:  result.data })
        });
    }

    render() {

        return (
            <div  className="price--list">
                <table  className="table">
                <thead  key="thead">
                <tr>
                    <th>#</th>
                    <th>Coin</th>
                    <th>Price</th>
                    <th></th>
                    <th></th>
                    <th></th>
                </tr>
                </thead>
                <tbody>
                {this.state.prices.map( p  =>
                    <tr>
                    <td>{p}</td>
                    <td></td>
                    <td></td>
                    <td></td>
                </tr>)}
                </tbody>
                </table>
            </div>
            );
      }
}

export default CryptoPricesList;