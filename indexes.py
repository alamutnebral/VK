import time
import math


class Yee():

    our_pids = []

    def __init__(self, vkapi, publics_file):
        self.vkapi = vkapi
        self.publics_file = publics_file
        with open(self.publics_file, 'r', encoding="utf8") as data:
            for line in data:
                public_id = line.split(')')[0][1:]
                self.our_pids.append(int(public_id))

    def show_user_portrait(self, user_id):
        user_publics = self.vkapi.groups.get(user_id=user_id, filter='publics', extended=1)[1:]
        time.sleep(0.3)

        print("user_id: " + str(user_id))
        print("green: " + str(self.green(user_publics)))

    def green(self, user_publics):
        M = len(user_publics)
        if M < 5:
            return 228
        counter = 0
        for up in user_publics:
            pid = up['gid']
            if pid in self.our_pids:
                counter += 1
        return round((10.0 * counter / M), 1)
        #return round((10.0 * counter / M) / math.sqrt(math.log(M, 5)), 1)

    def show_green_stats(self, users):
        stats = {}
        for u in users:
            user_id = u['uid']
            user_publics = self.vkapi.groups.get(user_id=user_id, filter='publics', extended=1)[1:]
            time.sleep(0.3)
            stats[user_id] = self.green(user_publics)
        stats = sorted(stats.items(), key=lambda x: x[1], reverse=False)
        for user in stats:
            print("g = {} (user: {})".format(user[1], user[0]))