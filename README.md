# Library Management System

A web-based application for managing a library's collection, users, and transactions. Built using Django.

## Features

- User Authentication
- Book Management (CRUD)
- Borrowing and Returning Books
- User Management (Admin Interface)
- REST API for Integration
- Rate Limiting for API Endpoints

## Requirements

- Python 3.13.1
- Django 4.2
- Vercel CLI

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/YOUR_USERNAME/library_management.git
   cd library_management
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Collect static files:

   ```bash
   python manage.py collectstatic
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Deployment

### Vercel

1. Install Vercel CLI:

   ```bash
   npm install -g vercel
   ```

2. Initialize Vercel in your project:

   ```bash
   vercel
   ```

3. Follow the prompts to set up your project.

4. Configure your `vercel.json`:

   ```json
   {
     "version": 2,
     "builds": [
       {
         "src": "library_management/wsgi.py",
         "use": "@vercel/python",
         "config": {
           "distDir": "build"
         }
       }
     ],
     "routes": [
       {
         "src": "/(.*)",
         "dest": "library_management/wsgi.py"
       }
     ]
   }
   ```

5. Deploy your project:
   ```bash
   vercel --prod
   ```

## Environment Variables

Ensure the following environment variables are set for your project in Vercel:

- `DJANGO_SETTINGS_MODULE=library_management.settings`
- `SECRET_KEY=your_secret_key`
- `DEBUG=False`

## Troubleshooting

- **500: INTERNAL_SERVER_ERROR**: Check Vercel logs for detailed error messages and ensure all dependencies are correctly installed.
- **Static Files Not Loading**: Ensure `collectstatic` command is run and `STATIC_ROOT` is correctly set in `settings.py`.

## Acknowledgements

- **[Django](https://www.djangoproject.com/)** - The web framework used to build this application.
- **[Vercel](https://vercel.com/)** - For providing an excellent platform to deploy serverless functions.
- **[drf-yasg](https://github.com/axnsan12/drf-yasg)** - For the automatic generation of Swagger documentation.
- **[GitHub](https://github.com/)** - For hosting the project repository.

## Contributing

Feel free to contribute to the project by opening a pull request or filing an issue.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
