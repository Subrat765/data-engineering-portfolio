# Data Engineering Portfolio

🚀 **Professional Data Engineering Portfolio website built with Flask to showcase projects, skills, and expertise in data engineering.**

## 📋 Project Overview

This portfolio website serves as a comprehensive platform to display data engineering projects, technical skills, and professional experience. Built with modern web technologies and designed with a clean, professional interface to highlight data engineering capabilities.

## 🛠️ Tech Stack

### Backend
- **Flask** - Python web framework for backend development
- **Python** - Core programming language
- **Jinja2** - Template engine for dynamic content rendering

### Frontend
- **HTML5** - Markup language for web structure
- **CSS3** - Styling and responsive design
- **JavaScript** - Interactive frontend functionality
- **Bootstrap** (if applicable) - CSS framework for responsive design

### Deployment & DevOps
- **Heroku** - Cloud platform deployment (Procfile included)
- **Git** - Version control
- **GitHub** - Code repository hosting

### Configuration & Environment
- **Environment Variables** - Secure configuration management
- **Requirements.txt** - Python dependency management

## 📁 Repository Structure

```
data-engineering-portfolio/
│
├── static/                 # Static files (CSS, JS, images)
│   ├── css/               # Stylesheets
│   ├── js/                # JavaScript files
│   └── images/            # Image assets
│
├── templates/             # Jinja2 HTML templates
│   ├── base.html          # Base template layout
│   ├── index.html         # Homepage template
│   └── [other templates]  # Additional page templates
│
├── app.py                 # Main Flask application
├── config.py              # Application configuration
├── requirements.txt       # Python dependencies
├── Procfile              # Heroku deployment configuration
├── .env.example          # Environment variables template
├── .gitignore            # Git ignore rules
└── README.md             # Project documentation
```

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- pip (Python package manager)
- Git

### Local Development Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Subrat765/data-engineering-portfolio.git
   cd data-engineering-portfolio
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env file with your configuration
   ```

5. **Run the application:**
   ```bash
   python app.py
   ```

6. **Access the application:**
   Open your browser and navigate to `http://localhost:5000`

## 🌐 Deployment

This application is configured for Heroku deployment:

1. **Install Heroku CLI**
2. **Login to Heroku:**
   ```bash
   heroku login
   ```

3. **Create Heroku app:**
   ```bash
   heroku create your-portfolio-name
   ```

4. **Deploy:**
   ```bash
   git push heroku main
   ```

## 📊 Features

- **Responsive Design** - Works seamlessly across devices
- **Project Showcase** - Highlight data engineering projects
- **Skills Display** - Technical competencies and tools
- **Professional Experience** - Career timeline and achievements
- **Contact Integration** - Easy way for employers to connect
- **SEO Optimized** - Better search engine visibility

## 🔧 Configuration

### Environment Variables
Create a `.env` file based on `.env.example`:

```env
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your-secret-key
# Add other configuration variables as needed
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 📞 Contact

**Subrat Kumar** - Data Engineer

- GitHub: [@Subrat765](https://github.com/Subrat765)
- LinkedIn: [Connect with me](https://linkedin.com/in/your-profile)
- Email: your.email@example.com

---

⭐ **If you like this project, please give it a star on GitHub!** ⭐

*Built with ❤️ by Subrat Kumar*
