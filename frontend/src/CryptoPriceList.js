import React, { Component } from 'react'
import CryptoPrices from './CryptoPrices'
import Spinner from './components/Spinner'
import ErrorMessage from './components/ErrorMessage'

const cryptoPrices = new CryptoPrices()

class CryptoPricesList extends Component {
    constructor(props) {
        super(props)

        this.state = {
            prices: [],
            isLoading: true,
            errors: [],
        }
    }

    componentDidMount() {
        var self = this
        cryptoPrices
            .getPrices()
            .then(function (result) {
                const { data } = result
                if (!data) {
                    this.setState({
                        isLoading: false,
                        errors: ['Error: unable to get data'],
                    })
                    return
                }
                self.setState({ prices: data, isLoading: false })
            })
            .catch((e) => {
                this.setState({
                    errors: [e.message],
                    isLoading: false,
                })
            })
    }

    render() {
        const { isLoading, prices, errors } = this.state
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
                        {prices &&
                            prices.map((p, i) => (
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
                {isLoading ? <Spinner /> : null}
                {errors.map((e, i) => (
                    <ErrorMessage key={i} text={e} />
                ))}
            </div>
        )
    }
}

export default CryptoPricesList
