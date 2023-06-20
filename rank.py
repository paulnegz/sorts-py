from heapq import heappop, heappush

prefix, race, finished_race = {1:"st",2:"nd",3:"rd"}, [], []

def print_ranking():
    if not finished_race: print("not ranked yet")
    print(f"Comparing {len(finished_race)} algorithms")
    for my_rank in finished_race:
        rank, name, time = my_rank.position, my_rank.name, my_rank.exec_time
        print(f"{name}\t took {time:.4f} seconds\t &\t placed {rank}{prefix.get(rank,'th')}")

class rank_sort:
    def __init__(self, name: str):
        self.name, self.position = name, None 

    def __lt__(self, other):
        return self.exec_time < other.exec_time
    
    def __repr__(self) -> str:
        position, name = self.position, self.name
        if not position: return f"{name} still racing..."
        return f"{name} ranked {position}{prefix.get(position,'th')}"


    def report_time(self, time: float):
        self.exec_time = time
        heappush(race, self)
    

    @staticmethod
    def end_ranking():
        for position in range(len(race)):
            my_rank, rank = heappop(race), position+1
            my_rank.position = rank
            finished_race.append(my_rank)
        print_ranking() 