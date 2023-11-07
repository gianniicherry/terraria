import './App.css';
import { useState, useEffect } from 'react';

function App() {
  const [characterName, setCharacterName] = useState('');
  const [classType, setClassType] = useState('');
  const [weapon, setWeaponType] = useState('');
  const [roles, setRoles] = useState([]);
  const [roleDescription, setRoleDescription] = useState('');

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

  return (
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
        <p>Selected Role Description: {roleDescription}</p>
      )}
    </div>
  );
}

export default App;

