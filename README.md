# Warbler – A Twitter Clone Project

## Project Overview

This project involves working on a somewhat-functioning Twitter clone called Warbler. The primary objective is to extend the application by fixing bugs, writing tests, and adding new features.

## Technologies Used

- **Programming Language:** Python
- **Web Framework:** Flask
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Authentication:** Flask-Bcrypt for secure password hashing
- **Debugging Tools:**
  - Flask-DebugToolbar for an in-browser debugger.
  - `pdb` for Python's interactive debugging environment.
- **Form Handling:** Flask-WTF for form validation and rendering

## Notes

- My role involves understanding, debugging, enhancing, and testing the code.
- The project reflects my ability to work with existing codebases and implement industry-standard practices.
- This initial push to GitHub consists of the starter code provided by Springboard's Software Engineering Bootcamp. The only modifications that have been made are:
  - **Secret Data Management:**
    - I created a `secret_data.py` file with associated variables (named `SECRET_KEY_FALLBACK` and `DATABASE_URI_FALLBACK`) and imported them into `app.py` for secure handling of sensitive configuration data.
    - This ensures that sensitive information is not hardcoded into the main codebase and is kept out of the public repository.
    - If utilizing this code, you should create your own `secret_data.py` file and import the necessary variables (such as secret keys and database URIs) as needed.
    - Example `secret_data.py`:
      ```python
      SECRET_KEY_FALLBACK = "your_secret_key_goes_here"
      DATABASE_URI_FALLBACK = "your_database_uri_goes_here"
      ```
  - A `.gitignore` file was added by me to ensure that unnecessary files/directories and/or sensitive information are not tracked by Git, preventing them from being pushed to public repositories.
  - This README was made by me in order to outline the project's structure, goals, and my tasks.

### Goals

- **Understand and Extend Existing Codebase:** The project offers an opportunity to work with an existing codebase, requiring me to refactor, document, and commit changes as I progress.
- **Bug Fixing:** Identify and fix bugs, maintaining a log of all the fixes.
- **Testing:** Develop tests for different aspects of the application.
- **Feature Enhancement:** Add new features and functionalities to the existing application.

### Key Responsibilities

- Regularly commit changes to GitHub, demonstrating the ability to work with version control systems.
- Debug and fix existing features.
- Enhance user profiles, authentication mechanisms, and other functionalities.
- Implement a new 'likes' feature without AJAX/JavaScript.
- Write comprehensive tests for models and routes/view-functions.

## Part One: Fix Current Features

### Steps

1. **Understand the Model:** Read `models.py` and create a diagram of the four tables.
2. **Fix Logout:** Implement a working logout route with a success message and redirection.
3. **Fix User Profile:** Add missing elements like location, bio, and header image.
4. **Fix User Cards:** Show user bios on various pages.
5. **Profile Edit:** Implement profile editing functionality.
6. **Fix Homepage:** Modify the homepage to show specific content based on user followings.
7. **Understand Login Strategy:** Analyze the existing authentication mechanism.

## Part Two: Add Likes

### Objective

- Implement a feature to allow users to like and unlike warbles (Warbler's version of tweets).
- Display liked warbles on the user's profile.

## Part Three: Add Tests

### Objective

- Test models and routes/view-functions.
- Ensure authentication and authorization functionalities are working as expected.
- Verify model attributes and methods.
- Ensure the correct functioning of endpoints and response codes.

---

_This project is part of my journey and transition from a Physical Therapist to a Software Engineer, and demonstrates my ability to work with and enhance existing codebases._
