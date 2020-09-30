friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

local_friends = {"Rolf"}

local_friends= friends.difference(abroad)  #{'Rolf'}
#local_friends= abroad.difference(friends)   #set()
print(local_friends)

local = {"Mika"}
kz= {"Doni", "Ulpi"}


dostar = local.union(kz)
print(dostar)

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}


both = art.intersection(science)
print(both)