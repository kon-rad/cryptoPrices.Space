import axios from 'axios';
let API_URL = '';
if (!process.env.NODE_ENV || process.env.NODE_ENV === 'development') {
    API_URL = 'http://localhost:8085';
}
console.log(API_URL, process.env.NODE_ENV);

export default class CryptoPrices{

    constructor(){}
    
    getPrices() {
        console.log('API_URL -> ', API_URL);
        const url = `${API_URL}/api/prices/`;
        return axios.get(url).then(response => response.data);
    }
}