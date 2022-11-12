import random

EMPTY = 0

class player:
    def __init__(self):
        self.step = 0
        self.mid = 0
        self.init_x = 0
        self.init_y = 0
        self.counter = 0
        self.counter1 = 0
        self.counter2 = 0
        self.counter3 = 0
        self.flag = False

    def move(self, B, N, cur_x, cur_y):
        if (self.step == 0):
            lis = []
            for i in range(N):
                lis.append(abs(i-cur_x)+abs(i-cur_y))
            self.mid = lis.index(min(lis))
            self.init_x = cur_x
            self.init_y = cur_y
            self.step += 1
            self.lis = [(0, 1), (0, 1)]

        if (self.init_x != self.mid):
            if (self.init_x > self.mid):
                self.init_x -= 1
                return (-1, 0)
            else:
                self.init_x += 1
                return (1, 0)

        if (self.init_y != self.mid):
            if (self.init_y > self.mid):
                self.init_y -= 1
                return (0, -1)
            else:
                self.init_y += 1
                return (0, 1)

        # if (self.flag == False):
        #     self.flag = True
        #     return (1,0)

        return self.move1(B, N, cur_x, cur_y)

    def move1(self, B, N, cur_x, cur_y):
        self.step += 1

        if (self.counter1 == 3):
            if (len(self.lis) != 0):
                a = self.lis[0]
                del self.lis[0]
                return a
            else:
                return self.move3(B, N, cur_x, cur_y)

        if (cur_x == self.init_x and cur_y == self.init_y):
            self.counter1 += 1
            print(self.counter1)

        lis = [(0, 1), (0, 1), (0, 1), (1, 0), (1, 0), (1, 0), (0, -1), (0, -1), (0, -1),
               (1, 0), (1, 0), (1, 0), (0, 1), (0, 1), (0, 1), (-1, 0), (-1, 0), (-1, 0)]
        while True:
            if self.counter == len(lis)-1:
                self.counter = 0
            else:
                self.counter += 1

            return lis[self.counter-1]

    def move2(self, B, N, cur_x, cur_y):

        if (self.counter3 == 2):
            return self.move3(B, N, cur_x, cur_y)

        if (cur_x == self.mid and cur_y == self.mid+3):
            self.counter3 += 1
            print(self.counter3)

        lis = [(0, 1), (0, 1), (0, 1), (1, 0), (1, 0), (1, 0)]
        while True:

            if self.counter2 == len(lis)-1:
                self.counter2 = 0
            else:
                self.counter2 += 1

            return lis[self.counter2-1]

    def move3(self, B, N, cur_x, cur_y):
        self.step += 1
        if B[cur_x][(cur_y+1) % N] == 0:
            return (0, 1)

        if B[cur_x][(cur_y+N-1) % N] == 0:
            return (0, -1)

        if B[(cur_x+1) % N][cur_y] == 0:
            return (1, 0)

        if B[(cur_x+N-1) % N][cur_y] == 0:
            return (-1, 0)

        # random.choice([(1,0),(0,1),(-1,0),(0,-1)])
        return self.closest_empty(B, N, cur_x, cur_y)

    def closest_empty(self, B, N, cur_x, cur_y):
        dis = 2*N+1
        best = {"x": cur_x, "y": cur_y}
        for i in range(N):
            for j in range(N):
                if B[i][j] == EMPTY:
                    dx = min(abs(cur_x - i), N - abs(cur_x - i))
                    dy = min(abs(cur_y - j), N - abs(cur_y - j))
                    cur_dis = dx+dy
                    if cur_dis < dis:
                        dis = cur_dis
                        best["x"] = i
                        best["y"] = j

        # Pick the direction to go in

        if best["y"] > cur_y:
            if best["y"]-cur_y < N/2:
                return (0, 1)
            else:
                return (0, -1)

        if best["y"] < cur_y:
            if cur_y-best["y"] < N/2:
                return (0, -1)
            else:
                return (0, 1)

        if best["x"] > cur_x:
            if best["x"]-cur_x < N/2:
                return (1, 0)
            else:
                return (-1, 0)

        if best["x"] < cur_x:
            if cur_x-best["x"] < N/2:
                return (-1, 0)
            else:
                return (1, 0)

        return (0, 0)


#p2 = player_two()
# for i in range(100):
#    p2.move()