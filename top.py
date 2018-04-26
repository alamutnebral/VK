import time
from collections import Counter


class PublicManager:
    public_names = {}
    sorted_publics = []

    def __init__(self, vkapi, users):
        self.vkapi = vkapi
        self.users = users
        self.n = len(users)


    def update_public_names(self, publics):
        for p in publics:
            self.public_names.update({p['gid'] : p['name']})


    def public_ids(self, publics):
        pbnames = []
        for p in publics:
            pbnames.append(p['gid'])
        return pbnames


    def update_stats(self, stats):
        for i in range(len(stats)):
            self.sorted_publics.append(stats.popitem())
        self.sorted_publics.sort(key=lambda x: -x[1])


    def show_stats(self):
        print("\nLadder (users analyzed: " + str(self.n) + ")")
        for i in range(10):
            print("{0}: {1} ({2})".format(i + 1,
                                          self.sorted_publics[i][1],
                                          self.public_names[self.sorted_publics[i][0]]))

    def top_publics(self, show=False):
        stats = Counter()
        i = 1
        for u in self.users:
            print("decomposing: " + str(i) + " of " + str(self.n))
            try:
                publics = self.vkapi.groups.get(user_id=u['uid'], filter='publics', fields='name', extended=1)[1:]
                time.sleep(0.3)  # RPS control
            except Exception:
                continue
            self.update_public_names(publics)

            gids = self.public_ids(publics)
            for gid in gids:
                stats[gid] += 1


            i += 1
        self.update_stats(stats)
        if show:
            self.show_stats()


    def write_stats_to_file(self, max=100):
        self.top_publics()
        i = 1
        print("Trying to rewrite publics data. Proceed? y/n")
        if (input() == "y"):
            with open("publics.txt", 'w', encoding="utf8") as publics_file:
                for i in range(max):
                    unit = self.sorted_publics[i][0]
                    output = "({0})__[{1}]__[]\n".format(unit, self.public_names[unit])
                    publics_file.write(output)
                    i += 1
                    if (i > max):
                        break