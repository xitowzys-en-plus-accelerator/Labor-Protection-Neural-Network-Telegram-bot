from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ID_ADMIN = env.str("ID_ADMIN", subcast=int)
