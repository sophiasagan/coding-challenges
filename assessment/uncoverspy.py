def uncover_spy(n, trust):
    # trusts no one
    # trusted by everyone
    # works alone

    # all all_people
    all_people = []
    # list of all_people who trust others
    trusting_people = []
    # list of all_people who are trusted
    trusted_people = []

    # add n all_people to the all_people list
    for person in range(1, n + 1):
        all_people.append(person)
    # for each arr in trust input
    for arr in trust:
        # put the first element in the trusting_people list
        trusting_people.append(arr[0])
        # put the second element in the trusted list
        trusted_people.append(arr[1])
    # iterate through the all_people
    for person in all_people:
        # if the person trusts no one and is trusted by everyone (but themselves)
        if person not in trusting_people and trusted_people.count(person) == (n - 1):
            # that person is the spy
            return person
    # otherwise there is no spy
    return -1