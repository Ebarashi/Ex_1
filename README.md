# Ex_1
Ex_1 - elevator - offline algo

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





# Running the simulation 
Run the Ex1.py file in a directory containing 'Brain', 'Ex1Objects', relevant Building json and csv with calls.  <br>
Use the following code template to run Ex1:  <br>
```
python Ex1.py <Building json> <Calls csv> <output name>
```
The csv with the results (same calls but allocated to elevators) will be created in the directory.   <br>

Running the algorithm example:
```
python Ex1.py B1.json C2.csv out.csv
```
Running the test code example:
```
java -jar Ex1_checker_V1.2_obf.jar 1111,2222,3333 B2.json Ex1_Calls_case_2_b.csv out.log
```
