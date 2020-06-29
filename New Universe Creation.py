# This will get some inputs from the user, and then make a universe with the desired parameters.
# Universe creation rules are detailed out at the end of this code.

from math import *
from random import randint

min_thread_length = 0
max_thread_length = 0
min_cluster_size = 0
max_cluster_size = 0
cluster_connections = 0
add_ones = 0
dummy = 1
code_list = []
t_log = []
t_log.append(dummy)
a_sectors = []
b_sectors = []
c_sectors = []
t_sectors = []


while True:
    try:
        highway_size = int(input("Number of highway sectors (10-1000): "))
        assert 10 <= highway_size <= 1000
    except ValueError:
        print("Please use numbers only.")
    except AssertionError:
        print("Must be between 10 and 1000.")
    else:
        break

while True:
    try:
        thread_number = int(input("Number of threads (0 to " + str(highway_size) + "): "))
        assert 0 <= thread_number <= highway_size
    except ValueError:
        print("Please use numbers only.")
    except AssertionError:
        print("Must be between 0 and " + str(highway_size) + ".")
    else:
        break

if thread_number != 0:
    while True:
        try:
            min_thread_length = int(input("Minimum length of each thread (5-99): "))
            assert 5 <= min_thread_length <= 99
        except ValueError:
            print("Please use numbers only.")
        except AssertionError:
            print("Must be between 5 and 99.")
        else:
            break

    while True:
        try:
            max_thread_length = int(input("Maximum length of each thread (" + str(min_thread_length) + "-99): "))
            assert min_thread_length <= max_thread_length <= 99
        except ValueError:
            print("Please use numbers only.")
        except AssertionError:
            print("Must be between " + str(min_thread_length) + " and 99.")
        else:
            break

# Setting max clusters to an arbitrary proportion for now.
avg_thread_length = floor((min_thread_length + max_thread_length) / 2)
max_clusters = thread_number * avg_thread_length + highway_size
if max_clusters > 9000:
    max_clusters = 9000
while True:
    try:
        cluster_number = int(input("Number of clusters in the universe (0 to " + str(max_clusters) + "): "))
        assert 0 <= cluster_number <= max_clusters
    except ValueError:
        print("Please use numbers only.")
    except AssertionError:
        print("Must be between 0 and " + str(max_clusters) + ".")
    else:
        break

if cluster_number != 0:
    while True:
        try:
            min_cluster_size = int(input("Minimum size of clusters (5-99): "))
            assert 5 <= min_cluster_size <= 99
        except ValueError:
            print("Please use numbers only.")
        except AssertionError:
            print("Must be between 5 and 99.")
        else:
            break

    while True:
        try:
            max_cluster_size = int(input("Maximum size of clusters (" + str(min_cluster_size) + "-99): "))
            assert min_cluster_size <= max_cluster_size <= 99
        except ValueError:
            print("Please use numbers only.")
        except AssertionError:
            print("Must be between " + str(min_cluster_size) + " and 99.")
        else:
            break

    while True:
        try:
            cluster_connections = int(input("Min number of intracluster links (3 to " + str(max_cluster_size) + "): "))
            assert 3 <= cluster_connections <= max_cluster_size
        except ValueError:
            print("Please use numbers only.")
        except AssertionError:
            print("Must be between 3 and " + str(max_cluster_size) + ".")
        else:
            break

# Get the desired amount of additional one-way connections, set to an arbitrary maximum.
t_cluster = cluster_number * ((min_cluster_size + max_cluster_size) / 2)
approximation = floor((2 * highway_size) + (thread_number * avg_thread_length) + t_cluster)
print("This universe has approximately " + str(approximation) + " sectors.")
if cluster_number != 0 and thread_number != 0:
    while True:
        try:
            add_ones = int(input("Number of additional connections (up to " + str(floor(.1 * approximation)) + "): "))
            assert 0 <= add_ones <= floor(.1 * approximation)
        except ValueError:
            print("Please use numbers only.")
        except AssertionError:
            print("Must be between 0 and " + (str(floor(.1 * approximation))) + ".")
        else:
            break

# Get the name of the save file for the travel paths.
while True:
    try:
        f_name = input("Please enter a 6-16 character name for the galaxy: ")
        f_len = len(f_name)
        assert 6 <= f_len <= 16
    except ValueError:
        print("Please try again.")
    except AssertionError:
        print("Must be between 6 and 16 characters in length.")
    else:
        break

atemp = 1
while atemp <= highway_size:
    if len(str(atemp)) == 1:
        string = "A000" + str(atemp)
        code_list.append(string)
    elif len(str(atemp)) == 2:
        string = "A00" + str(atemp)
        code_list.append(string)
    elif len(str(atemp)) == 3:
        string = "A0" + str(atemp)
        code_list.append(string)
    elif len(str(atemp)) == 4:
        string = "A" + str(atemp)
        code_list.append(string)
    atemp += 1

btemp = 1
while btemp <= highway_size:
    if len(str(btemp)) == 1:
        string = "B000" + str(btemp)
        code_list.append(string)
    elif len(str(btemp)) == 2:
        string = "B00" + str(btemp)
        code_list.append(string)
    elif len(str(btemp)) == 3:
        string = "B0" + str(btemp)
        code_list.append(string)
    else:
        string = "B" + str(btemp)
        code_list.append(string)
    btemp += 1

if cluster_number != 0:
    ctemp = 1
    while ctemp <= cluster_number:
        csize = randint(min_cluster_size, max_cluster_size)
        cltemp = 1
        while cltemp <= csize:
            if len(str(ctemp)) == 1:
                if len(str(cltemp)) == 1:
                    string = "C000" + str(ctemp) + "S0" + str(cltemp)
                    code_list.append(string)
                elif len(str(cltemp)) == 2:
                    string = "C000" + str(ctemp) + "S" + str(cltemp)
                    code_list.append(string)
            elif len(str(ctemp)) == 2:
                if len(str(cltemp)) == 1:
                    string = "C00" + str(ctemp) + "S0" + str(cltemp)
                    code_list.append(string)
                elif len(str(cltemp)) == 2:
                    string = "C00" + str(ctemp) + "S" + str(cltemp)
                    code_list.append(string)
            elif len(str(ctemp)) == 3:
                if len(str(cltemp)) == 1:
                    string = "C0" + str(ctemp) + "S0" + str(cltemp)
                    code_list.append(string)
                elif len(str(cltemp)) == 2:
                    string = "C0" + str(ctemp) + "S" + str(cltemp)
                    code_list.append(string)
            elif len(str(ctemp)) == 4:
                if len(str(cltemp)) == 1:
                    string = "C" + str(ctemp) + "S0" + str(cltemp)
                    code_list.append(string)
                elif len(str(cltemp)) == 2:
                    string = "C" + str(ctemp) + "S" + str(cltemp)
                    code_list.append(string)
            cltemp += 1
        ctemp += 1

if thread_number != 0:
    ttemp = 1
    while ttemp <= thread_number:
        tlength = randint(min_thread_length, max_thread_length)
        t_log.append(tlength)
        tltemp = 1
        while tltemp <= tlength:
            if len(str(ttemp)) == 1:
                if len(str(tltemp)) == 1:
                    string = "T000" + str(ttemp) + "S0" + str(tltemp)
                    code_list.append(string)
                elif len(str(tltemp)) == 2:
                    string = "T000" + str(ttemp) + "S" + str(tltemp)
                    code_list.append(string)
            elif len(str(ttemp)) == 2:
                if len(str(tltemp)) == 1:
                    string = "T00" + str(ttemp) + "S0" + str(tltemp)
                    code_list.append(string)
                elif len(str(tltemp)) == 2:
                    string = "T00" + str(ttemp) + "S" + str(tltemp)
                    code_list.append(string)
            elif len(str(ttemp)) == 3:
                if len(str(tltemp)) == 1:
                    string = "T0" + str(ttemp) + "S0" + str(tltemp)
                    code_list.append(string)
                elif len(str(tltemp)) == 2:
                    string = "T0" + str(ttemp) + "S" + str(tltemp)
                    code_list.append(string)
            elif len(str(ttemp)) == 4:
                if len(str(tltemp)) == 1:
                    string = "T" + str(ttemp) + "S0" + str(tltemp)
                    code_list.append(string)
                elif len(str(tltemp)) == 2:
                    string = "T" + str(ttemp) + "S" + str(tltemp)
                    code_list.append(string)
            tltemp += 1
        ttemp += 1

print("This universe has " + str(len(code_list)) + " sectors.")
code_list.sort()
print("Codelist sorted.")

# Create sector lists by type
x = 0
while x < len(code_list):
    sector = code_list[x]
    if sector[0] == "A":
        a_sectors.append(sector)
    elif sector[0] == "B":
        b_sectors.append(sector)
    elif sector[0] == "C":
        c_sectors.append(sector)
    elif sector[0] == "T":
        t_sectors.append(sector)
    else:
        print("Put in some error handling here.")
    x += 1
print("Sectors grouped.")

# initialize two list of lists to aid in assigning connections to clusters and threads
# the index of each list contains the sectors in the cluster of that number. Zero is null.
if cluster_number != 0:
    clusplus = cluster_number + 1
    cluster_list = [[] for _ in range(clusplus)]
    x = 0
    while x < len(c_sectors):
        ccode = c_sectors[x]
        cnum = int(ccode[1:5])
        cluster_list[cnum].append(ccode)
        x += 1
if thread_number != 0:
    theplus = thread_number + 1
    thread_list = [[] for _ in range(theplus)]
    x = 0
    while x < len(t_sectors):
        tcode = t_sectors[x]
        tnum = int(tcode[1:5])
        if tnum <= thread_number:
            thread_list[tnum].append(tcode)
        x += 1

# initialize an empty list of lists of the size of the universe to be generated.
travel_paths = [[] for _ in range(len(code_list))]
print("Big bang baby.")

# Special case sets for one-way distribution and cluster/thread connections
at_sectors = a_sectors + t_sectors
if cluster_number != 0 and thread_number != 0:
    ct_sectors = c_sectors + t_sectors
    act_sectors = a_sectors + c_sectors + t_sectors
    print("Dummies arranged.")

# Generate two-way paths by pulling the codes for each pair and writing them to the index of the other in travel_paths.
x = 0
while x < len(code_list):
    sector = code_list[x]
    print("Working on sector " + str(x) + ", " + sector + ".")
    if sector[0] == "A":
        # Get the name of the sector one higher, one lower, and the name of the corresponding B sector, and one higher.
        sec_index = a_sectors.index(sector)
        if sec_index == 0:
            travel_paths[x].append(a_sectors[1])
            travel_paths[x].append(a_sectors[-1])
            travel_paths[x].append(b_sectors[0])
            travel_paths[x].append(b_sectors[1])
        elif sec_index == (len(a_sectors) - 1):
            travel_paths[x].append(a_sectors[0])
            travel_paths[x].append(a_sectors[-2])
            travel_paths[x].append(b_sectors[sec_index])
            travel_paths[x].append(b_sectors[0])
        elif sec_index != 0 and sec_index != (len(a_sectors) - 1):
            secplus = sec_index + 1
            secminus = sec_index - 1
            travel_paths[x].append(a_sectors[secplus])
            travel_paths[x].append(a_sectors[secminus])
            travel_paths[x].append(b_sectors[sec_index])
            travel_paths[x].append(b_sectors[secplus])
    elif sector[0] == "B":
        # Get the name of the sector one higher, one lower, and the name of the corresponding A sector.
        sec_index = b_sectors.index(sector)
        if sec_index == 0:
            travel_paths[x].append(b_sectors[1])
            travel_paths[x].append(b_sectors[-1])
            travel_paths[x].append(a_sectors[0])
        elif sec_index == (len(b_sectors) - 1):
            travel_paths[x].append(b_sectors[0])
            travel_paths[x].append(b_sectors[-2])
            travel_paths[x].append(a_sectors[sec_index])
        elif sec_index != 0 and sec_index != (len(b_sectors) - 1):
            secplus = sec_index + 1
            secminus = sec_index - 1
            travel_paths[x].append(b_sectors[secplus])
            travel_paths[x].append(b_sectors[secminus])
            travel_paths[x].append(a_sectors[sec_index])
    elif sector[0] == "C":
        cnum = int(sector[1:5])
        csec = int(sector[6:])
        if csec == 1:
            atminus = (len(at_sectors) - 1)
            ransec = randint(1, atminus)
            secode = at_sectors[ransec]
            secindex = code_list.index(secode)
            travel_paths[x].append(secode)
            travel_paths[secindex].append(sector)
        while len(travel_paths[x]) <= cluster_connections:
            c_size = len(cluster_list[cnum])
            perchance = cluster_connections / c_size * 50
            for sec in cluster_list[cnum]:
                secindex = code_list.index(sec)
                checker = randint(1, 100)
                if checker <= perchance:
                    if code_list[secindex] not in travel_paths[x] and sector not in travel_paths[secindex]:
                        travel_paths[x].append(code_list[secindex])
                        travel_paths[secindex].append(sector)
    elif sector[0] == "T":
        tnum = int(sector[1:5])
        tsec = int(sector[6:])
        tplus = x + 1
        tminus = x - 1
        if tsec == 1 or tsec == t_log[tnum]:
            ransec = randint(0, (highway_size - 1))
            secode = a_sectors[ransec]
            secindex = code_list.index(secode)
            travel_paths[x].append(secode)
            travel_paths[secindex].append(sector)
            if tsec == 1:
                travel_paths[x].append(code_list[tplus])
            elif tsec == t_log[tnum]:
                travel_paths[x].append(code_list[tminus])
        else:
            travel_paths[x].append(code_list[tplus])
            travel_paths[x].append(code_list[tminus])
    else:
        print("Put in some error handling here.")
    sector = ""
    x += 1

if cluster_number != 0:
    cluster_list.clear()
if thread_number != 0:
    thread_list.clear()
    t_log.clear()
a_sectors.clear()
b_sectors.clear()
c_sectors.clear()
t_sectors.clear()
if cluster_number != 0 and thread_number != 0:
    at_sectors.clear()

if add_ones != 0:
    print("Rolling some dice.")
    x = 1
    while x <= add_ones:
        ct = (len(ct_sectors) - 1)
        act = (len(act_sectors) - 1)
        ran1 = randint(1, ct)
        ran2 = randint(1, act)
        if ct_sectors[ran1] != act_sectors[ran2]:
            ransec = ct_sectors[ran1]
            sec1 = code_list.index(ransec)
            travel_paths[sec1].append(act_sectors[ran2])
        x += 1

# Sort and de-dupe the sublists, then write to files.
travel_paths = [sorted(set(a), key=a.index) for a in travel_paths]
tempnum = 0
while tempnum < len(travel_paths):
    travel_paths[tempnum].sort()
    print(travel_paths[tempnum])
    tempnum += 1
with open(f_name + "_paths.txt", "w") as out_file:
    for x in travel_paths:
        out_file.write(", ".join(map(str, x)))
        out_file.write("\n")
with open(f_name + "_sec.txt", "w") as out_file:
    for x in code_list:
        out_file.write(str(x) + "\n")

# For each sector in A (exchange sectors)
#   connect that sector to the similarly named sector in B, and the one just above, wrapping.
#   connect that sector to the ones above and below in A, wrapping.
# For each sector in B (highway sectors)
#   connect that sector to the similarly named sector in A.
#   connect that sector to the ones above and below in B, wrapping.
# For each sector in C (clusters)
#   if it is a cluster sector 01, connect it to a random A or T sector.
#     ensure that this random sector connects to this 01 sector.
#   connect the sector to a number of other sectors in its cluster, according to cluster_connections.
#     ensure that each sector has at least 2 or 3 connections, repeat assignment if necessary.
# For each sector in T (threads)
#   if it is a thread sector 01, or the final sector in a thread, connect it to a random A sector.
#     ensure that this random sector connects to this 01 sector.
#   connect that sector to the ones above and/or below, but not wrapping.
# Add in one-ways
#   source can be any C or T, destination can be any A, C, or T.
#   generate purposeful lists for each of these and select randomly.
# Sort each list in travel_paths.
# Clear all unnecessary lists.
# Create a dictionary to convert the codenames in travel_paths into sector numbers.
#
# sector_paths = [tuple(x) for x in travel_paths]