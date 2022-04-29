# paradox_pay
<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="images/djesewa.png" alt="Logo" width="150" height="80">
  </a>

<h3 align="center">Integrate Esewa and Khalti for payment</h3>

  <p align="center">
    project_description
    <br />
    <!-- <a href="https://github.com/github_username/repo_name"><strong>Explore the docs Â»</strong></a>
    <br />
    <br />
    <a href="https://github.com/github_username/repo_name">View Demo</a>
    Â·
    <a href="https://github.com/github_username/repo_name/issues">Report Bug</a>
    Â·
    <a href="https://github.com/github_username/repo_name/issues">Request Feature</a> -->
    <a href="#"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="#">Report Bug</a>
    <a href="#">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#features">Features</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
     
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

 
This Reusable App is used for the esewa payment purposes. With the help of this project you can have lots of features 
such as create product,payment with esewa, Verify whether payment is successful or not, create recurrence subscription payment such as days, weeks, monthly and yearly basis.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Django](https://www.djangoproject.com/)
* [Bootstrap](https://getbootstrap.com)
* [Esewa](https://esewa.com.np/)
* [JQuery](https://jquery.com)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

You can setting up your project by  copy up and running follow these simple example steps.

### Features
* Inbuilt product model for adding product
* Esewa and Khalti are already implemented for Payment Purpose
* Inbuilt subscription model for adding and manage subscription like  weekly, monthly, yearly etc



### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* python
  ```sh
  pip install django==3.1
  pip install requests
  pip install django-rest-framework
  pip install Pillow
  ```

### Installation


1. Clone the repo
   ```sh
   https://github.com/PrinceSingh-123/paradox_pay.git
   ```
2. Install python packages
   ```sh
   pip install paradox-pay
   ```
 

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

### To use esewa and khalti for django
* Add app name in the settings.py file's INSTALLED_APPS
  ```sh
  'app',
  'shop',
  'rest-framework',
  ```
* Include these paths in the root urls of your Project
  ```sh
   path("",include("app.urls")),
   path("shop",include("shop.urls")),
   ```
* Don't forget to add media and static url in urlspatteerns of your root urls
  ```sh
    from django.conf import settings
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    ```


### Configuration

* List all these stuff in the settings.py file for redirect, login  and logout
  ```sh
  LOGIN_URL = 'login'
  LOGOUT_URL = 'logout'
  LOGIN_REDIRECT_URL = '/'
  LOGOUT_REDIRECT_URL = 'login'
  ```
* Add these configuration in the settings.py file
  ```sh

  AUTH_USER_MODEL = 'app.User'
  VERIFY_EXPIRE_DAYS = 3

  MEDIA_URL = '/media/'
  MEDIA_ROOT = BASE_DIR/ 'media'


  ```

* After listing all the configuration command following commands 
  ```sh
  python manage.py makemigrations app
  python manage.py migrate
  python manage.py makemigrations shop
  python manage.py migrate
  ```

* After that please create  Product and Subscription from Admin panel





<!-- _For more examples, please refer to the [Documentation](https://example.com)_ -->

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- Features -->
## Features

* Inbuilt product model for adding product
* Cart is already implemented for adding product to cart
* Esewa and Khalti are already implemented for Payment Purpose
* Inbuilt subscription model for adding and manage subscription like  weekly, monthly, yearly etc




     

See the [open issues](https://github.com/PrinceSingh-123/paradox_pay/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Developer - [@Purusottam Adhikari](https://www.linkedin.com/in/purusottam-adhikari/) - purusottamadhikari234@gmail.com

Project Link: [https://github.com/PrinceSingh-123/paradox_pay](https://github.com/PrinceSingh-123/paradox_pay)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/PrinceSingh-123/paradox_pay?style=for-the-badge
[contributors-url]: https://github.com/PrinceSingh-123/paradox_payment/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/PrinceSingh-123/paradox_pay?style=for-the-badge
[forks-url]: https://github.com/PrinceSingh-123/paradox_pay/network
[stars-shield]: https://img.shields.io/github/stars/PrinceSingh-123/paradox_pay?style=for-the-badge
[stars-url]: https://github.com/PrinceSingh-123/paradox_pay/stargazers
[issues-shield]: https://img.shields.io/github/issues/PrinceSingh-123/paradox_pay?style=for-the-badge
[issues-url]: https://github.com/PrinceSingh-123/paradox_pay/issues
[license-shield]: https://img.shields.io/github/license/PrinceSingh-123/paradox_pay?style=for-the-badge
[license-url]: https://github.com/PrinceSingh-123/paradox_pay/blob/main/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/purusottam-adhikari/
[product-screenshot]: images/admin.jpg



