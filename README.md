# serf-example
serf-example

## Try:
```
$ vagrant up
```

* node1 setting

```
$ vagrant ssh node1

# handler file permission
node1$ chmod +x -R /vagrant/serf

# serf agent run
node1$ serf agent -node=node1 -bind=172.20.20.10:7946 -event-handler=/vagrant/serf/handler.py &
```

* node2 setting

```
$ vagrant ssh node2

# handler file permission
node1$ chmod +x -R /vagrant/serf

# serf agent background run
node1$ serf agent -node=node2 -bind=172.20.20.11:7946 -event-handler=/vagrant/serf/handler.py &
```

* serf join

```
node1$ serf join 172.20.20.11:7946

or

node2$ serf join 172.20.20.10:7946
```

## watch event parameter

```
node1$ cat /tmp/serf.log

or

node2$ cat /tmp/serf.log
```

## event (add or fix)
add or fix python file undler the handers folder.
