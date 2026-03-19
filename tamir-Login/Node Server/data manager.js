
const sqlite3 = require('sqlite3').verbose();
const db = new sqlite3.Database('./database.db');

// Function to get data based on user_ip and website
// Function to get data from the table
async function getData(user_ip, website) {
    const query = `SELECT data FROM your_table WHERE user_ip = ? AND website = ?`;
    try {
      const row = await db.get(query, [user_ip, website]);
      return row ? row.data : null;
    } catch (err) {
      console.error(err.message);
      throw err; // Re-throw the error for proper handling
    }
  }
  
  // Function to insert data into the table
async function insertData(user_ip, website, data) {
    const query = `INSERT INTO your_table (user_ip, website, data) VALUES (?, ?, ?)`;
    try {
      await db.run(query, [user_ip, website, data]);
    } catch (err) {
      console.error(err.message);
      throw err; // Re-throw the error for proper handling
    }
  }
  
  // Function to remove a line based on user_ip and website
async function removeData(user_ip, website) {
    const query = `DELETE FROM your_table WHERE user_ip = ? AND website = ?`;
    try {
      await db.run(query, [user_ip, website]);
    } catch (err) {
      console.error(err.message);
      throw err; // Re-throw the error for proper handling
    }
  }