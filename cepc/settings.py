"""
Django settings for Note_Cloud project.

Generated by 'django-admin startproject' using Django 2.2.27.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'rr83xcuh1)is*ok4^ai2dxgudcg!u1k!wvg^ush+-zg4_k=y%u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'all_user',
    'trip_card_records',
    'django_tctip',
    'abnormal_records',
    'import_export',


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
     'middleware.middleware.SimpleMiddleware',
    # 'middleware.middleware.IpMiddleware'
    #'middleware.middleware.ExceptionMW'

]
MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
'corsheaders.middleware.CorsMiddleware',

    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'middleware.middleware.SimpleMiddleware',
    # 'middleware.middleware.IpMiddleware'
    #'middleware.middleware.ExceptionMW'

]

ROOT_URLCONF = 'cepc.urls'

SESSION_COOKIE_AGE = 60*60*24
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],

        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'cepc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cepc',
        'USER':'root',
        'PASSWORD':'123456',
        'HOST':'localhost',
        'PORT':'3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/
LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/


STATIC_URL = '/static/'

STATICFILES_DIRS = ( os.path.join(BASE_DIR,'static'), )

STATIC_ROOT = os.path.join(BASE_DIR,'/static/')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# smtp 服务的邮箱服务器
EMAIL_HOST = 'smtp.qq.com'
# smtp服务固定的端口是25
EMAL_POST = 25
# 发送邮件的邮箱
EMAIL_HOST_USER = '352446506@qq.com'
# 在邮箱中设置的客户端授权密码
EMAIL_HOST_PASSWORD = 'avfivdkqkvcabibj'
# 收件人看到的发件人<此处要和发送邮件的邮箱相同>
EX_EMAIL = ['352446506@qq.com']

MEDIA_URL='/media/'
MEDIA_ROOT= os.path.join(BASE_DIR,'media')
# 隐藏右侧SimpleUI广告链接和使用分析
SIMPLEUI_HOME_INFO = False
SIMPLEUI_ANALYSIS = False

SIMPLEUI_CONFIG = {
    # 是否使用系统默认菜单，自定义菜单时建议关闭。
    'system_keep': False,

    # 用于菜单排序和过滤, 不填此字段为默认排序和全部显示。空列表[] 为全部不显示.
    'menu_display': ['用户明细维护','上报异常签到及维护','行程异常签到及维护','实时数据可视化大屏','公告栏','权限认证'],

    # 设置是否开启动态菜单, 默认为False. 如果开启, 则会在每次用户登陆时刷新展示菜单内容。
    # 一般建议关闭。
    'dynamic': False,
    'menus': [
        {
            'app': 'auth',
            'name': '权限认证',
            'icon': 'fas fa-user-shield',
            'models': [
                {
                    'name': '管理用户列表',
                    'icon': 'fa fa-user-secret',
                    'url': 'auth/user/'
                },
                {
                    'name': '用户组',
                    'icon': 'fa fa-th-list',
                    'url': 'auth/group/'
                },

            ]

        },

        {
            'name': '行程异常签到及维护',
            'icon': 'fa fa-exclamation-triangle',
            'url': '/admin/trip_card_records/tripcardrecords/'
        },
{
            'app': 'django_tctip',
            'name': '公告栏',

            'models': [
                {
                    'name': '公告栏',

                    'url': '/admin/django_tctip/tip/'
                },

            ]
        },
        {'name': '实时数据可视化大屏',
         'icon': 'fas fa-user-shield',
        'url': 'http://localhost:8075/webroot/decision/view/form?viewlet=%25E5%25AD%25A6%25E7%2594%259F%25E5%2581%25A5%25E5%25BA%25B7%25E7%258A%25B6%25E5%2586%25B5%25E5%2588%2586%25E6%259E%2590%25E5%25A4%25A7%25E5%25B1%258F%252F%25E5%25AD%25A6%25E7%2594%259F%25E5%2581%25A5%25E5%25BA%25B7%25E7%258A%25B6%25E5%2586%25B5%25E5%2588%2586%25E6%259E%2590%25E5%25A4%25A7%25E5%25B1%258F%252F%25E5%25AD%25A6%25E7%2594%259F%25E5%2581%25A5%25E5%25BA%25B7%25E7%258A%25B6%25E5%2586%25B5%25E5%2588%2586%25E6%259E%2590%25E5%25A4%25A7%25E5%25B1%258F.frm' ,
'newTab': True,
         },
{
            'name': '上报异常签到及维护',
            'icon': 'fa fa-exclamation-triangle',
            'url': '/admin/abnormal_records/abnormalrecords/'

        },
{
            'name': '用户明细维护',
            'icon': 'fa fa-user-md',
            'url': '/admin/all_user/alluser/'
        },



    ]
}
SIMPLEUI_LOGO='https://i.328888.xyz/2023/03/11/sPz8q.jpeg'
