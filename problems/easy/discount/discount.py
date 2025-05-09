
# p =original price
#  d = percentage discount

def getdiscountedPS(p,d):
    pd = p * d/100
    pd = p - pd
    return pd
