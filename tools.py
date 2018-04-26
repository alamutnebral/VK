import vk
import time


def intersection(f1, f2):
    s1 = set(f1)
    s2 = set(f2)
    return set.intersection(s1, s2)


def university_id(query):
    session = vk.Session()
    vkapi = vk.API(session)
    university = vkapi.database.getUniversities(q=query)
    print(university)


class Statistics():
    our_pids = []

    def __init__(self, vkapi):
        self.vkapi = vkapi
        with open("publics.txt", 'r', encoding="utf8") as data:
            for line in data:
                public_id = line.split(')')[0][1:]
                self.our_pids.append(int(public_id))

    def show_covering(self, user_id):
        user_publics = self.vkapi.groups.get(user_id=user_id, filter='publics', extended=1)[1:]
        time.sleep(0.3)
        total = len(user_publics)
        counter = 0
        for up in user_publics:
            pid = up['gid']
            if pid in self.our_pids:
                counter += 1

        print("{0:0.1f}% ({1} out of {2})".format(counter * 100 / total, counter, total))


    def show_covering_stats(self, users):
        for u in users:
            self.show_covering(u['uid'])