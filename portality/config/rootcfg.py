# absolute paths, or relative paths from root directory, to the desired config files (in the order you want them loaded)
CONFIG_FILES = [
    "portentious/portality/config/webapp.py",
    "portentious/portality/modules/sherpafact/settings.py",
    "portentious/portality/modules/es/settings.py",
    "portentious/portality/config/googlemap.py",
    "config/service.py",
    "local.cfg"
]

# absolute paths, or relative paths from root directory, to the template directories (in the order you want them looked at)
TEMPLATE_PATHS = [
    "service/templates",
    "portentious/portality/templates"
]

# absolute paths, or relative paths from the root directory, to the static file directories (in the order you want them looked at)
STATIC_PATHS = [
    "service/static",
    "portentious/portality/static"
]

# module import paths for the startup modules that need to run at application init type (in the order you want them run)
INITIALISE_MODULES = [
    "portality.modules.es.initialise"
]