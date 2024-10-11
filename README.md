# Group_BSE25-34-Capstone
# Price Aggregator Web App
This web app allows users to search for products (e.g., laptops, phones, etc.) and retrieves prices from multiple online stores such as Amazon, Jumia, and eBay among others.

The app scrapes data from these stores in real-time and returns a list of the top-x cheapest products for the user’s search. 

This makes it easy for users to find the best deals across different platforms without manually browsing each one.

# Features:

Real-time data scraping: Fetches product data from various online stores.

Top-x results: Displays the cheapest options available.

Single-page frontend: Simple UI to display results and their details.
Installation

# Prerequisites:
Python installed (for running the frontend/backend)

Git installed (for cloning the repository)

Internet access (for scraping data from the online stores)

# Steps to Install:

# 1.Clone the Repository:
    git clone https://github.com/charlesrolandscr17/Group_BSE25-34-Capstone.git
# 2.Navigate to the Project Directory:
    cd Group_BSE25-34-Capstone

# 3.Create a Virtual Environment: Set up a virtual environment to manage your project dependencies.
    python -m venv venv

# 4.Activate the Virtual Environment: On macOS and Linux:
    source venv/bin/activate
# On Windows:
    venv\Scripts\activate

# 5.Install Dependencies: Install the required Python packages, including Django:
    pip install -r requirements.txt
# 6.Run Database Migrations: Apply Django migrations to set up the database.
    python manage.py migrate
# 7.Run the Development Server: Start the Django development server.
    python manage.py runserver
# 8.Access the App: Open your browser and go to [group-bse25-34-capstone - Aggregator](https://group-bse25-34-capstone-eaas.onrender.com) to view the app.
