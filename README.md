# Goodmil Construction - Django Business Website

Goodmil Construction is a comprehensive Django-based website for a Nepal-based construction company established in 2013. The platform specializes in architecture, construction, building, interior design, and real estate services.

## 🏗️ About Goodmil Construction

**Company**: Goodmil Amrit Nirman Sewa Pvt. Ltd.  
**Established**: 2013  
**Services**: Architecture, Construction, Building, Interior Design, Real Estate  

## 🌟 Features

### Business Showcase
- **Homepage**: Professional company introduction and services overview
- **About Us**: Company history, founder information, and mission
- **Services**: Detailed construction and architectural services
- **Projects**: Portfolio of completed construction projects
- **Gallery**: Visual showcase of work and capabilities
- **Real Estate**: Property listings and development projects

### Interactive Features
- **Property Search**: Advanced search functionality for real estate listings
- **Blog System**: Industry insights, company updates, and news
- **Contact Forms**: Multiple inquiry channels for different services
- **Newsletter Subscription**: Email marketing and updates
- **Apply Now**: Job applications and service inquiry system
- **Social Media Integration**: Multiple platform connectivity

### User Experience
- **Responsive Design**: Mobile-first design approach
- **Professional UI/UX**: Modern construction industry aesthetics
- **Loading Animations**: Smooth preloader and transitions
- **Interactive Navigation**: Responsive menu system
- **Search Functionality**: Site-wide search capabilities

## 🛠️ Technology Stack

- **Backend**: Django 4.1.6
- **Database**: SQLite (development), easily configurable for PostgreSQL/MySQL
- **Frontend**: HTML5, CSS3, JavaScript, jQuery
- **Animation Libraries**: 
  - GSAP 3.11.4 (animations and effects)
  - AOS (Animate On Scroll)
  - Swiper (touch slider)
  - Slick Carousel
- **Image Processing**: Pillow 9.4.0
- **Icons**: Font Awesome
- **Timezone**: Asia/Kathmandu

## 📁 Project Structure

```
goodmil/
├── goodmil/                   # Main project directory
│   ├── settings.py           # Django settings
│   ├── urls.py              # Main URL configuration
│   ├── wsgi.py              # WSGI configuration
│   ├── asgi.py              # ASGI configuration
│   └── sitemaps.py          # SEO sitemaps
├── home/                    # Main application
│   ├── models.py           # Database models
│   ├── views.py            # Business logic
│   ├── urls.py             # App URL patterns
│   ├── admin.py            # Admin interface
│   ├── context_processors.py  # Global context
│   └── migrations/         # Database migrations
├── templates/              # HTML templates
│   ├── base.html          # Base template
│   ├── home/              # Home app templates
│   └── components/        # Reusable components
├── static/                # Static files
│   ├── css/              # Stylesheets
│   ├── js/               # JavaScript files
│   └── img/              # Static images
├── media/                 # User uploaded files
│   ├── Gallery/          # Gallery images
│   ├── Projects/         # Project images
│   ├── Properties/       # Real estate images
│   ├── NewsAndArticles/  # Blog images
│   ├── Resume/           # Resume uploads
│   └── CoverLetter/      # Cover letter uploads
├── requirements.txt       # Python dependencies
└── manage.py             # Django management script
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd GoodmilConstruction

   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure settings**
   - Update `SECRET_KEY` in `settings.py` for production
   - Configure database settings if not using SQLite
   - Update `SITE_URL` for production domain
   - Set `DEBUG = False` for production

5. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Collect static files** (for production)
   ```bash
   python manage.py collectstatic
   ```

8. **Run the development server**
   ```bash
   python manage.py runserver
   ```

Visit `http://127.0.0.1:8000` to view the website.

## 📋 Usage

### Admin Panel
Access the admin panel at `http://127.0.0.1:8000/admin/` to:
- Manage construction projects and portfolio
- Add/edit real estate properties
- Create blog posts and news articles
- Manage gallery images
- Handle contact form submissions
- Manage newsletter subscribers

### Content Management
1. **Projects**: Add construction projects with images and details
2. **Real Estate**: List properties with search functionality
3. **Blog**: Publish industry insights and company news
4. **Gallery**: Showcase visual portfolio
5. **Services**: Update service offerings and descriptions

## 🔧 Configuration

### Social Media Links
Configure social media URLs in the footer and header sections:
- Facebook
- Instagram
- WhatsApp
- YouTube
- TikTok
- Twitter

## 🌐 Production Deployment

### Environment Variables
Set the following for production:
- `SECRET_KEY`: Django secret key
- `DEBUG`: Set to `False`
- `ALLOWED_HOSTS`: Your domain names
- `SITE_URL`: Production domain URL
- Database credentials
- Email configuration

### Security Considerations
- Use HTTPS in production
- Configure proper ALLOWED_HOSTS
- Set up database backups
- Enable Django security middleware
- Use environment variables for sensitive data

## 📱 Key Pages & Features

### Main Navigation
- **Home**: Company showcase and hero section
- **About Us**: Company history and team information
- **Services**: Construction and architectural services
- **Projects**: Portfolio of completed work
- **Real Estate**: Property search and listings
- **Blog**: Industry news and company updates
- **Gallery**: Visual portfolio and project images
- **Apply Now**: Career and service applications
- **Contact**: Business contact and inquiry forms

### Real Estate Features
- Advanced property search functionality
- Property listings with detailed information
- Image galleries for properties
- Contact forms for property inquiries

### Blog System
- Dynamic blog content management
- Category-based organization
- Image support for articles
- SEO-friendly URLs

## 🎨 Customization

### Styling
- Modify CSS files in `static/css/`
- Update templates in `templates/`
- Customize animations in JavaScript files
- Update color schemes and branding

### Adding Features
- Extend models in `home/models.py`
- Add views in `home/views.py`
- Create URL patterns in `home/urls.py`
- Update templates as needed

## 📊 Business Impact

### Digital Presence
- **Professional Website**: Establishes credibility in construction industry
- **Portfolio Showcase**: Visual demonstration of capabilities
- **Lead Generation**: Multiple contact and inquiry channels
- **Client Engagement**: Blog and newsletter for ongoing communication

### Technical Benefits
- **SEO Optimized**: Search engine friendly structure
- **Mobile Responsive**: Accessible on all devices
- **Fast Loading**: Optimized performance
- **Easy Management**: Django admin for content updates

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## 📄 License

This project is proprietary software for Goodmil Amrit Nirman Sewa Pvt. Ltd. All rights reserved.

## 🔄 Version History

- **v1.0**: Initial release with complete business website functionality
- Current version includes full project portfolio, real estate listings, blog system, and client engagement tools

---

**Note**: This is a production business website. Ensure proper testing and security measures before deploying to a live environment.

## 🏆 Company Services

**Goodmil Construction** provides comprehensive construction and design services:

1. **Architecture**: Design and planning services
2. **Construction**: Building and construction management
3. **Interior Design**: Interior decoration and design
4. **Real Estate**: Property development and sales
5. **Building Services**: Complete building solutions

*Trust us to bring your vision to life with exceptional customer service and attention to detail.*
