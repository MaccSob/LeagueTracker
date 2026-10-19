import { useState, useEffect } from 'react'

import './App.css'

function App() {
  const [data, setData] = useState([])

  useEffect(() => {
    fetch("http://localhost:8000/stats/champion").then (r => r.json()).then(setData)},

  [])
  return (
    <>
    <table>
      <tbody>
        {data.map(row => (
          <tr key={row.champion}>
            <td>{row.champion}</td>
            <td>{row.games}</td>
            <td>{row.wins}</td>
            <td>{row.winrate} %</td>
          </tr>
        ))}
      </tbody>
    </table>

    </>
  )
}

export default App
