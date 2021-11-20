# Ex_1
Ex_1 - elevator - offline algo
Prof. Boaz Ben Moshe
harel giladi- 211576277
Oilon barashi - 322679713

# 1 
# -Literature review:
These are the links that have inspired us to execute the algorithm, given us knowledge regarding problem mapping, object properties, and optimization.
https://www.diva-portal.org/smash/get/diva2:668654/FULLTEXT01.pdf
https://studylib.net/doc/7878746/on-line-algorithms-versus-off-line-algorithms-for-the-ele...

The Elevator Problem - 
details: 
given N floors in a building, k elevator and a list of elevator-requests each request comes at a particular time. (source --> destination).
In the offline algorithm all the input is available to us, and we can use it to write an effecient algorithm.
Our goal is to set of a "call" to the elevator. we need to define the goodness of the offline algorithm and to find an algorithm that considerate and answers these problems - 
1. the average waiting time per person on any floor should be the minimum.
2. miss as little as possible from the given calls.

# 2
# Offline algorithm
first We'll find the max_path the longest call(path=abs(dest-src)).
then we will calculate a range (max_path\the building num of elevs) so we will have some measurement for "knowing when a call is over", then we will go trough the building elevs
and assigen for each one of them a diffrent range of operation.
and now we could work on each call and assign it to the best elev by considring the call path.

# 3 uml diagram

![2021-11-19 (2)](https://user-images.githubusercontent.com/93948749/142690263-4e561ce9-138d-4b0d-8343-8c4852b27d4f.png)


# 4
# Running the Algo and checker 

Run the Ex1_main.py with the relevant Building json and csv with calls.  <br>
The csv with the results (same calls but with an elevator in the column) will be created in the directory. 

Running the test code with this linev on cmd:
```
java -jar Ex1_checker_V1.2_obf.jar 1111,2222,3333 B2.json Ex1_Calls_case_2_b.csv out.log
```
