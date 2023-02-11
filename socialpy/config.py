from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix='socialpy',
    settings_files=['settings.toml', '.secrets.toml'],
    environments=['development', 'production', 'testing'],
    env_switcher='socialpy_env',
    load_dotenv=False,
)
