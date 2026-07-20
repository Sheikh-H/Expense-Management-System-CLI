# 💷 Command-Line Expense Management System

<p align="center">
  <b>A structured, CSV-backed command-line finance tracker engineered for rapid expense logging, filtering, and lifecycle management.</b><br>
  Designed for local-first financial telemetry, persistent storage handling, and extensible multi-parameter query architecture.
</p>

---

<h2>📘 Project Overview</h2>

<p>
<b>LedgerFlow</b> is a fully interactive command-line expense tracking system developed as a native Python solution for the <b><a href="https://roadmap.sh/projects/expense-tracker" target="_blank">Expense Tracker</a></b> project challenge on <b>roadmap.sh</b>.
</p>

<p>
The application was engineered to simulate a lightweight personal finance management environment directly inside the terminal. Rather than relying on databases or third-party financial frameworks, LedgerFlow intentionally utilises structured CSV persistence to reinforce practical understanding of local file operations, record management, and transactional state handling.
</p>

<p>
Built with an extensible architecture and powered by Python's <code>argparse</code> module, the system supports dynamic expense creation, targeted querying, expense mutation, deletion workflows, CSV exporting, and temporal filtering by day, month, year, or exact date values.
</p>

---

<h2>🧠 Architectural Philosophy & Design Intent</h2>

<p>
LedgerFlow was intentionally designed around a <b>local-first persistence model</b>, meaning every financial transaction is stored directly inside a human-readable CSV datastore rather than abstracted behind external database engines.
</p>

<p>
This design philosophy was implemented for several deliberate technical and educational reasons:
</p>

<ol>
  <li>
    <b>Practical Reinforcement of File Handling:</b>  
    The project was engineered to provide repeated, hands-on exposure to Python file I/O operations, structured CSV manipulation, data serialisation, and runtime persistence management. Every expense insertion, modification, deletion, or export operation directly interacts with the filesystem.
  </li>

  <li>
    <b>Transparent Data Structures:</b>  
    Unlike hidden database layers, the application's storage system remains fully inspectable. Users can open <code>expenses.csv</code> directly and observe precisely how structured financial records are represented and manipulated programmatically.
  </li>

  <li>
    <b>CLI-Centric Workflow Optimisation:</b>  
    The application avoids graphical overhead entirely in favour of highly deterministic command execution. This creates an efficient workflow for users comfortable operating inside shell environments and allows for rapid data management through positional arguments and flags.
  </li>

  <li>
    <b>Scalable Query Foundations:</b>  
    While the current implementation processes one filtering parameter at a time during view operations, the internal architecture already introduces transitional list-based result handling designed to support future multi-filter querying systems.
  </li>
</ol>

---

<h2>⚡ Core Features & Project Enhancements</h2>

<p>
Although the application fulfils the baseline roadmap.sh requirements, LedgerFlow introduces a significantly expanded command architecture and multiple advanced behaviours:
</p>

| Capability          | Standard Requirements              | LedgerFlow Implementation                                                                                              |
| ------------------- | ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Expense Persistence | Store expenses locally             | Structured CSV-backed datastore with automatic file creation and persistent financial record indexing                  |
| Command Processing  | Basic terminal argument handling   | Full argparse integration with subcommands, validation pipelines, mutually exclusive groups, and structured help menus |
| Expense Querying    | Simple record viewing              | Granular temporal filtering by date, month, day, year, category, ID, or description                                    |
| Export Handling     | Display results to console         | Dynamic CSV export pipeline saving filtered results into structured reports                                            |
| Error Recovery      | Basic failures terminate execution | Structured terminal error sequencing with staged prompts and safe shutdowns                                            |
| Record Mutability   | Update expense values              | Dual-mode mutation engine via ID or description lookup                                                                 |

---

<h2>🧩 Folder Structure</h2>

<pre>
LedgerFlow/
│
├── expense-tracker.py   # Main CLI application and processing engine
├── expenses.csv         # Persistent expense datastore
├── filtered_expense.csv # Exported filtered query reports
└── README.md            # Project documentation
</pre>

---

<h2>🚀 How to Run</h2>

<ol>
  <li>Ensure you have <b>Python 3.8 or above</b> installed locally.</li>

  <li>Clone or download this repository:
    <pre>git clone https://github.com/Sheikh-H/LedgerFlow.git</pre>
  </li>

  <li>Navigate into the project directory:
    <pre>cd LedgerFlow</pre>
  </li>

  <li>No external dependencies are required — the project operates entirely using Python standard libraries.</li>

  <li>Run commands directly through the integrated CLI interface.</li>
</ol>

---

<h2>🖥️ Detailed Usage & Command Manual</h2>

<p>
LedgerFlow operates through a modular subcommand architecture powered by <code>argparse</code>.
</p>

---

<h3>1. Adding New Expenses</h3>

<p>
Create a brand-new financial transaction entry:
</p>

<pre>
python expense-tracker.py add --description "Coffee" --amount 4.50 --category "Food" --date 23-05-2026
</pre>

---

<h3>2. Viewing All Expenses</h3>

<p>
Display every stored expense record:
</p>

<pre>
python expense-tracker.py view
</pre>

---

<h3>3. Filtering Expenses</h3>

<p>
Query expenses using targeted filtering parameters:
</p>

<h4>Filter By Category</h4>

<pre>
python expense-tracker.py view --category Food
</pre>

<h4>Filter By Date</h4>

<pre>
python expense-tracker.py view --date 23-05-2026
</pre>

<h4>Filter By Month</h4>

<pre>
python expense-tracker.py view --month May
</pre>

<h4>Filter By Year</h4>

<pre>
python expense-tracker.py view --year 2026
</pre>

<h4>Filter By Description</h4>

<pre>
python expense-tracker.py view --description Coffee
</pre>

---

<h3>4. Updating Existing Expenses</h3>

<p>
Modify existing expense records using either an ID or description lookup:
</p>

<pre>
python expense-tracker.py update --id 3 --amount 12.99
</pre>

<i>Example updating multiple fields simultaneously:</i>

<pre>
python expense-tracker.py update --description Coffee --newdescription "Costa Coffee" --amount 5.20 --category Drinks
</pre>

---

<h3>5. Deleting Expenses</h3>

<p>
Delete records by ID:
</p>

<pre>
python expense-tracker.py delete --id 5
</pre>

<p>
Or by description:
</p>

<pre>
python expense-tracker.py delete --description Coffee
</pre>

---

<h2>⚙️ Code Architecture & Function Breakdown</h2>

<p>
The application is separated into modular operational blocks responsible for command parsing, data persistence, record transformation, and user interaction workflows.
</p>

---

<h3>CLI Bootloader & Argument Engine</h3>

<ul>
  <li>
    <code>on_load()</code>:  
    Initialises the command-line interface, configures all argparse subcommands, builds validation rules, and dynamically parses runtime user arguments.
  </li>
</ul>

---

<h3>Persistence & File Management</h3>

<ul>
  <li>
    <code>load_file()</code>:  
    Automatically creates the expense datastore if missing, loads structured CSV rows into memory, and returns a manipulatable list structure.
  </li>

  <li>
    <code>save_data(DATA)</code>:  
    Serialises active runtime expense records directly back into the CSV datastore while preserving field consistency.
  </li>
</ul>

---

<h3>Expense Lifecycle Controllers</h3>

<ul>
  <li>
    <code>add_expense()</code>:  
    Generates unique IDs, validates date structures, normalises category formatting, and appends new expenses into persistent storage.
  </li>

  <li>
    <code>update_expense()</code>:  
    Handles selective record mutation using either unique IDs or description references while preserving untouched fields.
  </li>

  <li>
    <code>delete_expense()</code>:  
    Removes expense records safely while handling duplicate description conflicts through guided user feedback.
  </li>
</ul>

---

<h3>Query & Filtering System</h3>

<ul>
  <li>
    <code>view_all()</code>:  
    Renders the complete expense ledger to the terminal.
  </li>

  <li>
    <code>view_by()</code>:  
    Processes dynamic expense filtering across multiple financial dimensions including temporal queries, categories, IDs, and textual descriptions.
  </li>

  <li>
    <code>export_to_csv()</code>:  
    Exports filtered query results into a standalone CSV report for external analysis or archival storage.
  </li>
</ul>

---

<h3>System Utilities</h3>

<ul>
  <li>
    <code>clear_screen()</code>:  
    Performs operating-system aware terminal clearing for cleaner UI presentation.
  </li>

  <li>
    <code>error_messages()</code>:  
    Displays staged runtime alerts with timed delays before safely terminating the application.
  </li>
</ul>

---

<h2>📂 Local Data Architecture</h2>

<p>
All financial records are stored inside <code>expenses.csv</code> using a structured column-based format:
</p>

<h3>Sample Datastore Layout</h3>

<pre>
ID,Date,Description,Amount,Category
1,2026-05-23,Coffee,4.50,FOOD
2,2026-05-24,Train Ticket,18.20,TRANSPORT
3,2026-05-25,Netflix,10.99,ENTERTAINMENT
</pre>

---

<h2>🧪 Current Limitations & Future Improvements</h2>

<p>
The current query engine processes one filter parameter at a time. A future architectural redesign is planned to support <b>multi-condition filtering</b>.
</p>

<p>
The intended future implementation involves generating a temporary in-memory results list containing all expense records before progressively eliminating entries that fail to match layered filter conditions.
</p>

<p>
This would allow advanced query combinations such as:
</p>

<pre>
python expense-tracker.py view --category Food --month May --year 2026
</pre>

<p>
Additional planned improvements include:
</p>

<ul>
  <li>Multi-parameter query chaining</li>
  <li>Summary statistics and spending analytics</li>
  <li>Budget threshold monitoring</li>
  <li>Coloured terminal rendering</li>
  <li>SQLite backend migration</li>
  <li>Advanced report generation</li>
</ul>

---

<h2>🧰 Requirements & Dependencies</h2>

<ul>
  <li><b>Python Runtime:</b> version 3.8 or above.</li>

  <li>
    <b>Internal Standard Modules:</b>
    <code>os</code>,
    <code>sys</code>,
    <code>csv</code>,
    <code>time</code>,
    <code>argparse</code>,
    <code>datetime</code>.
  </li>

  <li><b>External Libraries:</b> None.</li>
</ul>

---

<h2>📄 Licence</h2>

<p>
  This project is licensed under the <b>MIT Licence</b> — see the <a href="./LICENCE">LICENCE</a> file for details.
</p>

<pre>
MIT Licence

Copyright (c) 2026 Sheikh Hussain

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
</pre>

---

## Footnote

<div align="center" style="border: 1px solid green; padding: 10px; border-radius: 5px;">
  <p>🗣️ Feel free to follow, connect, and chat!</p>
  <a class="header-badge" target="_blank" href="https://github.com/Sheikh-H"><img src="https://img.shields.io/badge/GitHub-376e00?style=flat&logo=github&logoColor=white" alt="GitHub">
  </a><a class="header-badge" target="_blank" href="https://www.linkedin.com/in/sheikh-hussain/"><img src="https://img.shields.io/badge/LinkedIn-376e00?style=flat&logo=LinkedIn&logoColor=white" alt="LinkedIn">
  </a><a class="header-badge" target="_blank" href="mailto:sheikh.hussain1155@gmail.com"><img src="https://img.shields.io/badge/Gmail-376e00?style=flat&logo=gmail&logoColor=white" alt="Gmail">
  </a><a class="header-badge" target="_blank" href="https://sheikh-hussain.onrender.com/"><img src="https://img.shields.io/badge/Portfolio-376e00?style=flat&logo=github&logoColor=white" alt="Portfolio">
  </a>
</div>

<div align="center">
  <a href="https://sheikh-hussain.onrender.com/" target="_blank">By Sheikh Hussain 💚</a>  
</div>

---

<h2 align="center">⭐ If you like this project, please give it a star on GitHub!</h2>
