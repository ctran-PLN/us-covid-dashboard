import React from 'react'
import './../assets/Table.css'
import numeral from 'numeral'

function Table({states, caseType}) {
    return (
        <div className="table">
        {states.map((st)=>(
          <tr>
              <td>{st.state}</td>
              <td><strong>{numeral(st[caseType]).format()}</strong></td>
          </tr>
        ))}
        </div>
    )
}

export default Table
