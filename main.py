from random import randrange


def lottery():
    balls = list(range(1, 51))

    # unit test : test container that contains 50 balls
    assert len(balls) == 50

    # unit test : test container that contains balls numbered 1 to 50
    assert all(0 < i <= 50 for i in balls)

    picked_list = []

    for i in range(10):
        pick = balls[randrange(len(balls))]
        picked_list.append(pick)
    picked_list.sort()

    return picked_list


if __name__ == '__main__':

    picked = lottery()

    # unit test : test a function picked 10 balls
    assert 10 == len(picked)

    # unit test : test a function picked ball
    assert 10 == len(list(set(picked)))

    # unit test : test a picked balls are ascending order
    assert all(picked[i] <= picked[i+1] for i in range(len(picked)-1))

    # unit test : test a function balls picked balls that numbered 1 to 50
    assert all(0 < i <= 50 for i in picked)
