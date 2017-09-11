domain = "https://api.btcmarkets.net"
apiroot = "market"
coin = "ETH"
currancy =  "AUD"
tick = "tick"
slash = "/"

uri = str(slash + apiroot + slash + coin + slash + currancy + slash + tick)
url = str(domain + uri)

print domain
print uri
print url
