import { useState, useEffect } from 'react'
import {BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, LineChart, Line} from "recharts"

import './App.css'

function App() {
  const [champions, setChampions] = useState([])
  const [roles, setRoles] = useState([])
    const [rolling, setRolling] = useState([])
    
    const rollingWithNo = rolling.map((row, i ) => ({...row, game: i + 1}))

  useEffect(() => {
    fetch("http://localhost:8000/stats/champion").then (r => r.json()).then(setChampions)},

  [])
   useEffect(() => {
    fetch("http://localhost:8000/stats/role").then (r => r.json()).then(setRoles)},

  [])
   useEffect(() => {
    fetch("http://localhost:8000/stats/rolling").then (r => r.json()).then(setRolling)},

  [])
  return (
    <>
    <section className='card'>
    <table>
      <thead>
        <tr><th>Champion</th><th>Games</th><th>Wins</th><th>Winrate</th></tr>
      </thead>
      <tbody>
        {champions.map(row => (
          <tr key={row.champion}>
            <td>{row.champion}</td>
            <td>{row.games}</td>
            <td>{row.wins}</td>
            <td>{row.winrate} %</td>
          </tr>
        ))}
      </tbody>
    </table>

        <h2>Winrate per champion</h2>
    <ResponsiveContainer width="100%" height={300}>
      <BarChart data={champions.filter(row => row.games >= 2).slice(0, 10)}>
        <XAxis dataKey="champion"/>
            <Tooltip/>
            <Bar dataKey="winrate" fill='#4f7cff'/>
            <Bar dataKey="games" fill='#4f7cff'/>
      </BarChart>
    </ResponsiveContainer>
</section>

    <section className='card'>
 <h2>Winrate changing throughout games</h2>
        <ResponsiveContainer width="100%" height={300}>
      <LineChart data={rollingWithNo}>
        <XAxis dataKey="game"/>
          <YAxis domain={[0, 100]}/>
            <Tooltip/>
            <Line dataKey="rolling_winrate"/>
      </LineChart>
    </ResponsiveContainer>
    <p>Amount of matches</p>
</section>

    <section className='card'>

        <h2>Winrate per role</h2>
        <ResponsiveContainer width="100%" height={300}>
      <BarChart data={roles}>
        <XAxis dataKey="role"/>
          <YAxis />
            <Tooltip/>
            <Bar dataKey="winrate"/>
            <Bar dataKey="wins"/>
      </BarChart>
    </ResponsiveContainer>

</section>

    </>
  )
}

export default App
