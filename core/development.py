import os
import sys

ENV = "development"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_DIR, "genproto"))

APPS = ["order"]

DATABASE = {
    "HOST": os.environ.get("DATABASE_HOST", "localhost"),
    "PORT": os.environ.get("DATABASE_PORT", "5432"),
    "USER": os.environ.get("DATABASE_USER", "bringo"),
    "PASSWORD": os.environ.get("DATABASE_PASSWORD", "bringo"),
    "NAME": os.environ.get("DATABASE_NAME", "bringo"),
    "CA_CERT": os.environ.get("DATABASE_CA_CERT"),
    "SSL": os.environ.get("DATABASE_SSL", False),
}

KAFKA = {
    "HOST": os.environ.get("KAFKA_HOST", "localhost"),
    "PORT": os.environ.get("KAFKA_PORT", "9092"),
    "GROUP_ID": "template",
    "EXCEPTION_TOPIC": "history.error.create",
}

CDN = {
    'BUCKET': os.environ.get('CDN_BUCKET', 'bringo-dev-cdn'),
    'REGION': os.environ.get('CDN_REGION', 'ams3'),
    'ENDPOINT_URL': os.environ.get('CDN_ENDPOINT_URL', 'https://ams3.digitaloceanspaces.com'),
    'SPACES_KEY': os.environ.get('CDN_SPACES_KEY', ''),
    'SPACES_SECRET': os.environ.get('CDN_SPACES_SECRET', ''),
}

REDIS_CACHE = {
    'HOST': os.environ.get('REDIS_HOST', 'localhost'),  # if not needed to set manually None
    'PORT': os.environ.get('REDIS_PORT', 6379),
    'USERNAME': os.environ.get('REDIS_USERNAME', None),
    'PASSWORD': os.environ.get('REDIS_PASSWORD', None),
    'EXPIRE_DURATION': os.environ.get('REDIS_EXPIRE_DURATION', 24 * 60 * 40),
    'DECODE_RESPONSES': True,  # to get results as string
    'DB': 0,
    'SSL': True,
    'SSL_CERT_REQS': None
}

SENTRY_CONFIG = {
    "DSN": os.environ.get("SENTRY_DSN"),
    "TRACES_SAMPLE_RATE": 1.0,
}

assert KAFKA.get("GROUP_ID"), "Add kafka GROUP_ID to kafka config"
