# Census

**Census** is a personal CRM and networking platform that merges the simplicity of a contact book with the functionality of professional networking sites. It helps you manage your contacts, capture key interactions, and organize your network with a flexible, version-controlled approach.

## Overview

Census enables you to build rich contact profiles by adding customizable information blocks. Capture details about work, education, family, and the context of your interactions—all within an intuitive interface. Whether you're managing a personal network or connecting with professional organizations, Census is designed to make networking easier and more efficient.

## Key Features

- **Flexible Information Blocks:**  
  Create, edit, and organize contact data in a modular way. Future enhancements will support custom and nested blocks for even greater flexibility.

- **Interactions as Tags:**  
  Easily tag interactions with metadata (such as title, date, and an optional location) to keep track of the context and updates made during each encounter.

- **Version History:**  
  Maintain a revision history for your contact information, ensuring you can track and revert changes as needed.

- **Dual Profiles:**  
  Build both a private contact page and a public profile. The public profile serves as a baseline for discovery and connection, while the private page allows for detailed personal notes.

- **Organizations:**  
  Join or create organizations to manage professional or community-based networks. Role-based access ensures that you control who can view or edit organization details.

- **Calendar and Notifications:**  
  Integrate event tracking and reminders to manage important dates, meetings, and follow-ups, keeping your networking efforts on schedule.

- **API Ready:**  
  The backend is built with a RESTful API to facilitate seamless integration with a React frontend (currently in development).

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/census.git
   cd census
   ```

2. **Create and Activate a Virtual Environment:**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # For Linux/macOS
   .venv\Scripts\activate     # For Windows
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser:**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server:**

   ```bash
   python manage.py runserver
   ```

7. **Access the Backend:**

   Open your browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## API & Frontend Integration

This repository contains the backend API for Census, built using Django. The API endpoints are organized by functionality (users, organizations, contacts) to ensure a clear separation of concerns and scalability as the project grows. The React frontend is currently under development and will integrate with this backend via RESTful endpoints.

## Roadmap

### MVP Phase
- **User Management & Organizations:**  
  Implement core user authentication and organization management using Django’s built-in auth system and custom views.

- **Minimal Contacts Model:**  
  Introduce a basic contacts model with a simple text field for contact details, serving as a placeholder for future expansion.

### Future Enhancements
- Expand the contacts model to support customizable information blocks.
- Implement detailed interaction tagging and editing sessions.
- Integrate a calendar and notification system for tracking important dates and follow-ups.
- Add external integrations (e.g., LinkedIn import, external calendar sync).
- Develop comprehensive API endpoints to support an interactive React frontend.

## License

[LICENSE PLACEHOLDER]
