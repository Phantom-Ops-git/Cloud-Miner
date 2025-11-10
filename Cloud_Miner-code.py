>>> <!DOCTYPE html>
... <html lang="en">
... <head>
...   <meta charset="UTF-8" />
...   <meta name="viewport" content="width=device-width, initial-scale=1.0" />
...   <title>Cloud_Miner</title>
...   <style>
...     body {
...       font-family: "Poppins", sans-serif;
...       background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
...       color: #fff;
...       text-align: center;
...       margin: 0;
...       padding: 0;
...     }
...     header {
...       background: #111;
...       padding: 1rem;
...       font-size: 1.5rem;
...       font-weight: bold;
...       letter-spacing: 1px;
...     }
...     .container {
...       padding: 2rem;
...     }
...     select, button, input {
...       padding: 10px;
...       margin: 10px;
...       border-radius: 5px;
...       border: none;
...       font-size: 1rem;
...     }
...     button {
...       cursor: pointer;
...       background: #00c853;
...       color: white;
...       transition: 0.3s;
...     }
...     button:hover {
...       background: #009624;
    }
    .dashboard {
      display: none;
      margin-top: 2rem;
    }
    .balance {
      font-size: 2rem;
      margin: 1rem 0;
    }
    footer {
      margin-top: 3rem;
      background: #111;
      padding: 1rem;
      font-size: 0.9rem;
    }
  </style>
</head>
<body>
  <header>💎 Cloud_Miner</header>

  <div class="container">
    <h2>Welcome to Cloud_Miner</h2>
    <p>Select a mining option and start earning!</p>

    <div>
      <label for="coinSelect">Choose currency:</label>
      <select id="coinSelect">
        <option value="bitcoin">Bitcoin</option>
        <option value="ton">Ton</option>
        <option value="dollar">Dollar</option>
        <option value="gold">Gold</option>
        <option value="ethereum">Ethereum</option>
      </select>
    </div>

    <button id="startMining">Start Mining</button>

    <div class="dashboard" id="dashboard">
      <h3 id="miningTitle"></h3>
      <div class="balance" id="balance">0.00000000</div>
      <button id="stopMining">Stop Mining</button>
      <br />
      <button id="withdrawBtn">Withdraw</button>
    </div>
  </div>

  <footer>© 2025 Cloud_Miner. All rights reserved.</footer>

  <script>
    const startBtn = document.getElementById("startMining");
    const stopBtn = document.getElementById("stopMining");
    const withdrawBtn = document.getElementById("withdrawBtn");
    const dashboard = document.getElementById("dashboard");
    const title = document.getElementById("miningTitle");
    const balanceDisplay = document.getElementById("balance");
    const select = document.getElementById("coinSelect");

    let miningInterval;
    let balance = 0;

    startBtn.addEventListener("click", () => {
      const coin = select.value;
      title.textContent = `Mining ${coin.toUpperCase()}...`;
      dashboard.style.display = "block";
      balance = 0;
      balanceDisplay.textContent = "0.00000000";
      miningInterval = setInterval(() => {
        balance += Math.random() * 0.0001;
        balanceDisplay.textContent = balance.toFixed(8);
      }, 1000);
    });

    stopBtn.addEventListener("click", () => {
      clearInterval(miningInterval);
      alert("Mining stopped!");
    });

    withdrawBtn.addEventListener("click", () => {
      const wallet = prompt("Enter your wallet address:");
      if (wallet) {
        alert(`Withdrawal request sent to wallet: ${wallet}`);
        // Placeholder for backend call:
        // fetch(`${API_BASE}/withdraw`, { method: 'POST', body: JSON.stringify({ wallet, balance }) })
      } else {
        alert("Withdrawal cancelled.");
      }
    });
  </script>
</body>

