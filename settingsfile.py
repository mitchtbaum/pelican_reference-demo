SITENAME = "pelican_reference demo"
SITEURL = "http://mitchtbaum.github.io/pelican_reference-demo/"
#SITEURL = "http://localhost:8000"
DEFAULT_DATE = "fs"
CATEGORY_URL = "{slug}/"
CATEGORY_SAVE_AS = "{slug}/index.html"
ARTICLE_URL = "{category}/{slug}/"
ARTICLE_SAVE_AS = "{category}/{slug}/index.html"
PLUGIN_PATHS = 'plugins'
PLUGINS = ['pelican_reference']
SLUGIFY_SOURCE = 'basename'
PATH = "content"
THEME = "theme"
