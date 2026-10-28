const express = require('express');
const db = require('./db');

const app = express();
const PORT = 3000;

app.use(express.json());

// Root route
app.get('/', (req, res) => {
  res.send('Node.js backend is up and running!');
});

// Database test route
app.get('/db-test', async (req, res) => {
  try {
    const result = await db.query('SELECT NOW()');
    res.json({
      status: 'success',
      database_time: result.rows[0].now,
    });
  } catch (err) {
    console.error("Database error details:", err);
    res.status(500).json({ 
      error: 'Database connection failed', 
      details: err.message 
    });
  }
});

app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});