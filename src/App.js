import './App.css';
import {useState} from 'react'


function App() {
  const [characterName, setCharacterName] = useState("")
  const [classType, setClassType] = useState("Warrior")
  const [weapon, setWeaponType] = useState("")

  return (
    <div className="App">
      <form>
        <label>Enter your Character Name.</label>
        <input type="text" value={characterName} onChange={(e) => setCharacterName(e.target.value)}></input>
        <select id="classType" value={classType} onChange={(e)=> setClassType(e.target.value)}>
          <option value="Warrior">Warrior</option>
          <option value="Wizard">Wizard</option>
          <option value="Assassin">Assassin</option>
          <option value="Ranger">Ranger</option>
          <option value="Templar">Templar</option>
          <option value="Wicken">Wicken</option>
        </select>
      </form>
    </div>
  );
}

export default App;
