import React, { Component } from 'react'
import CryptoPrices from './CryptoPrices'

const cryptoPrices = new CryptoPrices()

class CryptoPricesList extends Component {
    constructor(props) {
        super(props)

        this.state = {
            prices: [],
        }
    }

    componentDidMount() {
        var self = this
        cryptoPrices.getPrices().then(function (result) {
            const { data } = result
            if (!data) {
                return
            }
            self.setState({ prices: data })
        })
    }

    render() {
        return (
            <div className="price__list">
                <table className="table">
                    <thead key="thead">
                        <tr>
                            <th>Name</th>
                            <th>Currency</th>
                            <th>Price</th>
                        </tr>
                    </thead>
                    <tbody>
                        {this.state.prices &&
                            this.state.prices.map((p, i) => (
                                <tr key={i}>
                                    <td>{p.base}</td>
                                    <td>{p.currency}</td>
                                    <td>
                                        ${' '}
                                        {String(
                                            parseFloat(p.amount).toFixed(2)
                                        ).replace(
                                            /\d{1,3}(?=(\d{3})+(?!\d))/g,
                                            '$&,'
                                        )}
                                    </td>
                                </tr>
                            ))}
                    </tbody>
                </table>
            </div>
        )
    }
}

export default CryptoPricesList
