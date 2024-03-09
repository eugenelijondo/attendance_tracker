import React, {useState, useEffect} from 'react'
import TransactionForm from './TransactionForm';

function TransactionTableList(){
    const [formData, setFormData]= useState({});
    const [transactions, setTransactions] = useState([])
    useEffect(() => {
        fetch("http://localhost:8001/transactions")
            .then((response) => response.json())
            .then((data) => {
                if (Array.isArray(data) && data.length > 0) {
                    const {
                        date,
                        description,
                        amount,
                    } = data[0];
                    setFormData({ date, description, amount });
                }
                setTransactions(data);
            })
            .catch(error => {
                console.error('Error fetching transactions!: ', error);
            });
    }, []);
    function handleNewData(newData){
        setTransactions([...transactions, newData]);
    }
    function handleChange(e){
        const name = e.target.value;
        let value = e.target.value;
        if(name === "amount"){
           value = parseFloat(value);
        }
        setFormData({
            ...formData,
            [name]: value,
        })
    }
    function handleSubmit(e){
        e.preventDefault();
        handleNewData(formData)
    }
    return (
        <div className='transactions'>
            <h3>Bank Transactions</h3>
            <table className='transaction'>
                <thead>
                    <tr>
                        <th>Date</th>
                        <th>Description</th>
                        <th>Amount</th>
                    </tr>
                </thead>
                <tbody>
                    {transactions.map((transaction)=>(
                    <tr key={transaction.id}>
                        <td>{transaction.date}</td>
                        <td>{transaction.description}</td>
                        <td>{transaction.amount}</td>
                        </tr>))}
                </tbody>
            </table>
            <TransactionForm handleNewData={handleNewData} handleChange={handleChange} handleSubmit={handleSubmit}/>
        </div>
    )
}

export default TransactionTableList;