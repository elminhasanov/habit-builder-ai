import React, { useState } from 'react';

function App() {
    const [habit, setHabit] = useState("");
    const [motivation, setMotivation] = useState("");

    const addHabit = async () => {
        await fetch('http://localhost:5000/add_habit', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ user: "test_user", habit })
        });
        alert("Habit added!");
    };

    const getMotivation = async () => {
        const response = await fetch(`http://localhost:5000/motivation?habit=${habit}`);
        const data = await response.json();
        setMotivation(data.quote);
    };

    return (
        <div style={{ padding: '20px', textAlign: 'center' }}>
            <h1>Habit Builder with AI Motivation</h1>
            <input 
                type="text" 
                placeholder="Enter a habit" 
                value={habit} 
                onChange={(e) => setHabit(e.target.value)} 
            />
            <button onClick={addHabit} style={{ marginLeft: '10px' }}>Add Habit</button>
            <br /><br />
            <button onClick={getMotivation}>Get Motivation</button>
            <p>{motivation}</p>
        </div>
    );
}

export default App;
