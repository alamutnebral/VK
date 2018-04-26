import vk
import top
from tools import Statistics
from ids import unid
from ids import kfu_facid
from indexes import Yee


app_id = 1337
login = '**'
password = '**'
session = vk.AuthSession(app_id=app_id, user_login=login, user_password=password, scope='audio')
vkapi = vk.API(session)


def main():
    users = vkapi.users.search(university=unid("КФУ"),
                              # university_faculty=kfu_facid("МЕХМАТ"),
                               age_from = 18,
                               age_to = 24,
                               count=10)[1:]
    #top.PublicManager(users, vkapi).top_publics(show=True)
    #top.PublicManager(vkapi, users).write_stats_to_file(max=300)
    #user_publics = vkapi.groups.get(user_id=1337, filter='publics', extended=1)[1:]
    #Yee(vkapi, "top300_KFU_1000.txt").show_user_portrait(1337)
    #Yee(vkapi, "top300_KFU_1000.txt").show_green_stats(users)
    #Statistics(vkapi).show_covering_stats(users)
    #Statistics(vkapi).show_covering(1337)

if __name__ == "__main__":
    main()