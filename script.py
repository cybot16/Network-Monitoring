import plotly
import plotly.plotly as py 
import plotly.tools as tls
import plotly.graph_objs as go
import datetime
import time
import numpy as np
import subprocess
from plotly.graph_objs import Scatter, Layout, Figure
from optparse import OptionParser


parser = OptionParser()
parser.add_option("-i","--ip", dest = "ip", type = "string" , help ="Enter the ip address of the host")
parser.add_option("-o","--oid", dest = "oid", type = "string" , help ="Enter the exact OID that you want to graph")
(options, args) = parser.parse_args()

ip = options.ip
oid = options.oid

print ip+oid
username = 'cybot16'
api_key = 'WaGAuN1U6aMJYswhxTZx'
stream_token = 'o5j88pkmyt'
power_limit = 50
py.sign_in(username, api_key)


trace1 = Scatter(
    x=[],
    y=[],
    fill='tonexty',
    mode='lines',
    line=dict(
        color='rgb(255,140,0)',
    ),
    stream=dict(
        token=stream_token,
        maxpoints=40
    )
)
layout = Layout(
    title='Power extraction'
)

fig = Figure(data=[trace1], layout=layout)

print py.plot(fig, filename='Streaming power levels')

i = 0    # a counter
k = 5    # some shape parameter

# We will provide the stream link object the same token that's associated with the trace we wish to stream to
s = py.Stream(stream_token)

# We then open a connection
s.open()

while True:

    # Current time on x-axis, random numbers on y-axis
    x = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    y = subprocess.call("snmpget -c public -v 1"+ip+" "+oid, shell=True) 
 #   if y<power_limit :
  #      import send.py
    # Send data to your plot
    s.write(dict(x=x, y=y))

    #     Write numbers to stream to append current data on plot,
    #     write lists to overwrite existing data on plot

    time.sleep(1)  # plot a point every second    
# Close the stream when done plotting
