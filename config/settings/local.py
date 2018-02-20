from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY', default='&&88x$n$%-(viw=df$o314g5%tb!+7@3%v!half&@2r+x*hice')

DEBUG = env.bool('DJANGO_DEBUG', default=True)
