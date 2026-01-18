# From the Deep

In this problem, you'll write freeform responses to the questions provided in the specification.

## Random Partitioning

Reasons to adopt: easy to distribute data across the boats, load distributed evenly across servers; lower risk of single point failure.
Reasons not to adopt: harder to index data, slower to search for data.

## Partitioning by Hour

Reasons to adopt: easy to index data and search for it quickly.
Reasons not to adopt: risk of single point failure; data isnt evenly distributed across servers.

## Partitioning by Hash Value

Reasons to adopt: easy to index data, and easy to search for it if we know the timestamp. And it also distribute data evenly across servers, so there is lower risk of single point failure.
Reasons not to adopt: hard to search for data if we dont know the timestamp.


'''
Random partitioning (each observation goes to a random boat)

Why you’d adopt it:

- It spreads data and traffic evenly across boats almost automatically. If most sightings happen at midnight–1am, random assignment still keeps all boats busy instead of melting one.

- It’s simple operationally: writes don’t need any “routing logic” beyond “pick a boat”.

Why you might avoid it:

- Any time-range query (e.g., “give me everything from 00:00 to 01:00”) will usually need to query every boat, because that hour’s data is scattered everywhere. That means more network calls, more coordination, and higher latency for analytics-style questions.

- You can index locally on each boat, but you still pay the “fan-out cost” because the matching rows live everywhere.


Mental model

- Great for load balancing.

- Bad for range scans by time.



Partitioning by hour (boat A = 00:00–00:59, boat B = 01:00–01:59, …)

Why you’d adopt it:

- It’s excellent for time-window queries. If you ask for “midnight–1am”, you hit exactly one boat (boat A), not all of them.
This is “partition pruning”: you know where the data must live based on time, so queries get targeted and cheap.

Why you might avoid it:

- If data is not evenly distributed across hours (and it often isn’t), you get a hot partition. Midnight–1am might be huge, so boat A becomes:

a CPU bottleneck,

a storage bottleneck,

and a single point of pain for that specific hour’s queries/writes.

It’s not “single point of failure” for the whole system, but it is a point of failure for that hour’s slice: if boat A is down, you lose access to that hour’s data.


Mental model

- Great when queries are time-based and load is roughly uniform across time.

- Dangerous when one time bucket dominates.




Partitioning by hash (hash(timestamp) → boat)

Why you’d adopt it:

- It gives you even distribution like random partitioning, but with determinism: the same timestamp always maps to the same boat.

- It’s great for point lookups: “Do we have an observation at timestamp T?” → compute hash(T) → go to exactly one boat.

Why you might avoid it:

- Hashing destroys time order. So range queries (midnight–1am) still usually require hitting all boats, because that hour’s timestamps are spread across boats by the hash.

In other words: good for “find this exact record”, not good for “find everything in this time interval”.

Operational nuance: if you change the number of boats, the mapping can change and you may need rebalancing (unless you use consistent hashing / virtual nodes).


Mental model

- Great for even load + targeted point reads.

- Still bad for time ranges.




A clean one-liner comparison

- Random: evenly balanced, but time queries fan out to all boats.

- By hour: time queries are targeted, but you can get a hot boat if one hour dominates.

- Hash: evenly balanced and targeted for exact timestamps, but time-range queries still fan out.


'''
