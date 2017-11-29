import win32com.client
import os

qinfo = win32com.client.Dispatch("MSMQ.MSMQQueueInfo")
computer_name = os.getenv('COMPUTERNAME')
qinfo.FormatName = "direct=os:"+computer_name+"\\PRIVATE$\\sreenu"
queue = qinfo.Open(2,0)   # Open a ref to queue
msg = win32com.client.Dispatch("MSMQ.MSMQMessage")
msg.Label = "TestMsg"
msg.Body = "This is a test message"
msg.Send(queue)

queue.Close()

