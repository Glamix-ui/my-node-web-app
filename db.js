const { Pool } = require('pg');

const pool = new Pool({
  user: 'postgres',
  host: 'localhost',
  database: 'postgres', // <--- Use the default built-in 'postgres' database
  password: 'Glamix1!', // <--- Put your actual password inside single quotes
  port: 5432,
});

module.exports = {
  query: (text, params) => pool.query(text, params),
};