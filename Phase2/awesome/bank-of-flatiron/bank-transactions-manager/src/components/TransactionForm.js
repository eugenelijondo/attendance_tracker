import React from 'react'

function TransactionForm({handleChange, formData, handleSubmit, handleNewData}){
    
    return (
        <form onSubmit={handleSubmit}>
        <label for="date">Date:
            <input id="date" name='date' type='text' value={formData.date} onChange={handleChange} placeholder='Date' />
        </label>
        <label for="description">Description:
            <input id="description" name='description' type='text' value={formData.description} onChange={handleChange} placeholder='Description' />
        </label>
        <label for="amount">Amount:
            <input id="amount" name='amount' type='text' value={formData.amount} onChange={handleChange} placeholder='Amount' />
        </label>
        <button type='submit'>Add Transaction</button>
    </form>
    
    )
}

export default TransactionForm;