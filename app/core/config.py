from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix='SOCIALPY',
    settings_file=['settings.toml', '.secrets.toml'],
    enviroments=['development', 'production', 'testing'],
    env_switcher='project_env',
    load_dotenv=False,
)
