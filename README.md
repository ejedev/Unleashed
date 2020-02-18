# Unleashed
A Python library to interact with the Unleashed API. This is based off of Jonathan Sokolowski's original module but intended to be maintained and updated for future versions of Python.

# Documentation
As it stands, the module is currently quite basic. It currently only allows you to pull data from an endpoint (but allows for specifications.)

**Install the module**

`pip install Unleashed`

**Import the module**

`from Unleashed import Unleashed`

**Set up a client**

`Client = Unleashed.Client(api_key, api_id)`

**Request data**

This will return JSON data. It can be iterated through like a Python dictionary.

`data = Client.request_endpoint("SalesOrders")`

**Request data with specifications**

`data = Client.request_endpoint("SalesOrders", "pageSize=50&startDate=2019-11-20")`

# Acknowledgements
[Jonathan Sokolowski](https://github.com/jsok/) for the original Unleashed module. You can view it [here.](https://github.com/jsok/unleashed)
