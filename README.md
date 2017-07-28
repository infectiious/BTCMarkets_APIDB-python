# Python Docker container pulling data from BTCMarkets.net

A couple of Python3 scripts I made to pull data from BTCMarkets.net and log the results into a MySQL database for graphical visualisation through [Grafana](https://github.com/grafana/grafana).

## Getting Started

Get started by cloning the repository and adding your database details connections.py. Your database will need tables created (BTCMarkets_btc, BTCMarkets_etc, BTCMarkets_eth, BTCMarkets_ltc, BTCMarkets_xrp). You can either create these tables yourself or name your own and change them in each relevant script.

### Prerequisites

As this is running in a docker container the only requirement is that you have Docker installed. If you do not want to run this in a container you will have to use Pip to install the 'Requests' and 'Pymysql' modules.

```
pip install requests
pip install pymysql
```

### Installation

To run in a container clone the repository, update your server details in 'connections.py' and run the 'runcontainer.sh' script to build the image and start the container.

```
git clone https://github.com/infectiious/BTCMarkets_APIDB-python.git
cd BTCMarkets_APIDB-python/
vim connections.py
```

Add your MySQL server details

Then start the container. You may have to run this with elevated privelages if your current user is not added to the [Docker group](https://askubuntu.com/questions/477551/how-can-i-use-docker-without-sudo).

```
sh ./runcontainer.sh
```

### Test if working

To test if the container is working run

```
docker ps
```

You should see Infectiious_APICollect running if the container has started correctly. You can with the logs with docker logs. By default the API is contacted every 150 seconds. The time is logged when the collection has run the latest update is logged to the Database.

This could be improved upon by checking if the data has changed before adding a new record as the update time is logged.

## Roadmap

- Add further scripts to collect data from alternative markets.
- Add better logging.
- General clean up of directory and code.
- Add function to consolidate older records into longer timeframes. i.e data from 6 months or older would be stored on a hourly/daily basis rather then every 2 minutes for optimisation.

## Built With...

- [Official Python Docker Container](https://hub.docker.com/_/python/) - The Docker container built on.
- [Python Requests Module](http://docs.python-requests.org/en/master/) - For interacting with the API.
- [Python3](https://www.python.org/) - Language for scripts.
- [Pymysql](http://docs.python-requests.org/en/master/) - For writing to the MySQL database.
- [Mysql](https://www.mysql.com/) - Database backend.

## Acknowledgements

- [For inspiration with using Python to interact with the API's](https://github.com/adversary-org/python-btcmarkets)
