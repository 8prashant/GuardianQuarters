# Guardian Quarters

## Introduction

**Guardian Quarters** is a welfare initiatives platform designed to help Armed Forces personnel find customized housing solutions. This platform bridges the gap for 30-50% of Army personnel in specific areas who opt for private housing. It provides a responsive, user-friendly platform that integrates modern technologies for efficient housing data management.

---

## Technology Stack

- **Frontend**: HTML, CSS, JavaScript  
- **Backend**: Django  
- **Database**: MySQL  

---

## Features

### 1. User-Friendly Interface
- The platform offers a clean and intuitive interface designed with HTML, CSS, and JavaScript.
- Ensures smooth navigation for users of all technical backgrounds.
- Fully responsive design for accessibility across desktops, tablets, and mobile devices.

### 2. Housing Data Management
- Efficient backend powered by Django ensures seamless data handling and retrieval.
- MySQL database used to store and manage housing information securely and efficiently.
- Admin panel for easy data updates and monitoring.

### 3. Personalized Recommendations
- Allows users to filter housing options based on preferences like location, budget, and amenities.
- Custom algorithms to rank housing options tailored for Armed Forces personnel.

### 4. Secure Authentication
- Login and registration functionality implemented using Django’s authentication system.
- Ensures user data privacy with robust encryption techniques.
- Role-based access control to protect sensitive features.

### 5. Dynamic Property Listings
- A dedicated properties page displaying dynamic property listings fetched from the database.
- Includes detailed information about each property, such as images, pricing, and contact details.
- Real-time updates to reflect new listings or changes.

### 6. Responsive Design
- Built with responsiveness in mind to cater to a variety of devices.
- Optimized for fast load times and smooth transitions, even on slower networks.
- Ensures a consistent user experience across browsers and platforms.

### 7. Scalability and Maintainability
- Modular code structure designed for easy updates and future feature integration.
- Supports scaling for additional functionalities, such as reviews and advanced search filters.
- Comprehensive documentation for developers to contribute seamlessly.

### 8. Accessibility Enhancements
- Complies with web accessibility standards to ensure usability for differently-abled users.
- Includes features like keyboard navigation and high-contrast mode for better visibility.

---

## Screenshots

### Home Page
![Home Page](https://github.com/8prashant/GuardianQuarters/blob/main/homePage.png)

### Properties Page
![Properties Page](https://github.com/8prashant/GuardianQuarters/blob/main/propertiesPage.png)

### Login Page
![Login Page](https://github.com/8prashant/GuardianQuarters/blob/main/Login.png)

---

## Installation

Follow the steps below to set up the project locally:

1. **Navigate to the project directory:**

    ```bash
    cd GuardianQuarters
    ```

2. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up the database:**
    - Configure the database settings in `settings.py`.

4. **Run migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Start the development server:**

    ```bash
    python manage.py runserver
    ```

6. **Access the application:**
    - Open your browser and navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## Usage

- **Home Page:** Explore the platform and access basic information.
- **Properties Page:** View detailed property listings with filtering options based on user preferences.
- **Login/Registration:** Access personalized features after logging into the platform.

---

## Contribution Guidelines

Contributions to the Guardian Quarters project are welcome! To contribute:

1. **Fork the repository.**
2. **Create a feature branch:**

    ```bash
    git checkout -b feature-name
    ```

3. **Commit your changes:**

    ```bash
    git commit -m "Feature description"
    ```

4. **Push to the branch:**

    ```bash
    git push origin feature-name
    ```

5. **Open a Pull Request** for review.

Please ensure your contributions follow the project’s coding standards and include relevant tests where applicable.

---

## License

This project is licensed under the terms of the MIT License.

---

## Contact

For further information or inquiries, feel free to contact the project maintainer:

- **Name:** Prashant Kumar Rai  
- **Email:** [prashantkumarrai8@gmail.com]  

---

Let me know if you need further modifications or additional sections.
