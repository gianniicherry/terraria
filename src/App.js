import './App.css';
import { useState, useEffect } from 'react';

function App() {
  const [characterName, setCharacterName] = useState('');
  const [classType, setClassType] = useState('');
  const [weapon, setWeaponType] = useState('');
  const [roles, setRoles] = useState([]);
  const [roleDescription, setRoleDescription] = useState('');
  const [characterSelected, setCharacterSelected] = useState(false)
  const [response, setResponse] = useState([]);
  const [loading, setLoading] = useState(false);
  const [region, setRegion] = useState(null)

  useEffect(() => {
    fetch('http://127.0.0.1:5000/api/roles')
      .then((response) => response.json())
      .then((data) => setRoles(data))
      .catch((error) => console.error('Error fetching roles:', error));
  }, []);

  const handleRoleChange = (e) => {
    const selectedRoleId = e.target.value;
    const selectedRole = roles.find((role) => role.id === parseInt(selectedRoleId));

    if (selectedRole) {
      setClassType(selectedRole.name);
      setRoleDescription(selectedRole.description);
    }
  };

  function onCharacterSelect(){
    setCharacterSelected(characterSelected => !characterSelected)
  }

  function findRegions() {
    setLoading(true);

    fetch('http://127.0.0.1:5000/api/regions')
      .then((response) => response.json())
      .then((data) => {
        console.log(data.regions)
        setResponse(data.regions);
        setLoading(false);
      })
      .catch((error) => {
        console.error('Error fetching regions:', error);
        setLoading(false);
      });
  }

  function handleRegionSelect(land){
    setRegion(land)
    console.log(region)
  }

  function startJourney(){
    console.log(characterName)
    console.log(classType)
    console.log(region)

    const newCharacter = {
      name: characterName,
      weapon: weapon,
      role_name: classType
    }
    {/*must add region to character model, 
    create weapon input on react, and create a 
    response script through OpenAi 
    to fetch newly created character and return response*/}
    fetch('http://127.0.0.1:5000/api/characters', {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(newCharacter)
    })
    .then(r => r.json())
    .then(data => console.log(data))

  }

  return (
    <div>
    { characterSelected ?
    <div className="App">
      <form>
        <label>Enter your Character Name:</label>
        <input
          type="text"
          value={characterName}
          onChange={(e) => setCharacterName(e.target.value)}
        ></input>
        <select
          id="classType"
          value={classType}
          onChange={handleRoleChange}
        >
          <option value="">Select a role</option>
          {roles.map((role) => (
            <option key={role.id} value={role.id}>
              {role.name}
            </option>
          ))}
        </select>
      </form>
          {classType}
      {roleDescription && (
        <p>Role Description: {roleDescription}</p>
      )}
      <button onClick={onCharacterSelect}>Next</button>
    </div>
    :
    <div>
      <p>Character Name: {characterName}</p>
      <p> Class: {classType}</p>
      <button onClick={onCharacterSelect}>Back</button>
     <button onClick={findRegions}>Submit</button> 
    </div>
    }
     <div>
        {loading ? (
          <p>Loading...</p>
        ) : (
          <ul>
            {response.map((r) => (
              <li key={r.name}
              onClick= {()=> handleRegionSelect(r)}
              style={{ cursor: 'pointer', backgroundColor: region === r ? 'lightblue' : 'white' }}
              >{r.name} <p key={r.description}>{r.description}</p></li>
            ))}
          </ul>
        )}
      </div>
      <div>
        { region === null ? <div></div> : ( <div>
        <h3>Ready to Start your Journey?</h3>
        <button>Start</button>
        </div>
        )
         }
      </div>
    </div>
  );
}

export default App;

