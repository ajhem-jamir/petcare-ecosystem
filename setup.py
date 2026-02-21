#!/usr/bin/env python3
"""
Setup script for Pet Care Ecosystem
This script helps set up the development environment
"""

import os
import sys
import subprocess

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n{description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✓ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Error during {description}")
        print(f"Command: {command}")
        print(f"Error: {e.stderr}")
        return False

def main():
    print("🐾 Pet Care Ecosystem Setup")
    print("=" * 40)
    
    # Check if virtual environment exists
    if not os.path.exists('venv') and not os.path.exists('env'):
        print("\n📦 Creating virtual environment...")
        if not run_command("python -m venv venv", "Virtual environment creation"):
            print("Please ensure Python 3.8+ is installed")
            return False
    
    # Activate virtual environment and install requirements
    if os.name == 'nt':  # Windows
        activate_cmd = "venv\\Scripts\\activate && "
    else:  # Unix/Linux/Mac
        activate_cmd = "source venv/bin/activate && "
    
    # Install requirements
    if not run_command(f"{activate_cmd}pip install -r requirements.txt", "Installing Python packages"):
        return False
    
    # Create .env file if it doesn't exist
    if not os.path.exists('.env'):
        print("\n📝 Creating .env file...")
        import secrets
        secret_key = secrets.token_urlsafe(50)
        
        with open('.env', 'w') as f:
            f.write(f"""SECRET_KEY={secret_key}
DEBUG=True
DB_NAME=petcare_db
DB_USER=root
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=3306
""")
        print("✓ .env file created with random SECRET_KEY")
    
    print("\n🗄️  Database Setup Instructions:")
    print("1. Make sure MySQL is installed and running")
    print("2. Create a database named 'petcare_db':")
    print("   mysql -u root -p")
    print("   CREATE DATABASE petcare_db;")
    print("3. Update .env file with your MySQL credentials")
    print("4. Run migrations:")
    print(f"   {activate_cmd}python manage.py makemigrations")
    print(f"   {activate_cmd}python manage.py migrate")
    print("5. Create superuser:")
    print(f"   {activate_cmd}python manage.py createsuperuser")
    print("6. Run the development server:")
    print(f"   {activate_cmd}python manage.py runserver")
    
    print("\n🎉 Setup completed! Follow the database setup instructions above.")

if __name__ == "__main__":
    main()