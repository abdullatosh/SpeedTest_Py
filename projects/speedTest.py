import speedtest
st = speedtest.Speedtest()
d = st.download()
u = st.upload()
print("Your download speed is ", d//1000000 , ' mbps/s')
print("Your upload speed is " , u//1000000 , ' mbps/s')