import requests
import tkinter as tk
import tkinter.messagebox

uuid = ''
count = 10000
url = 'https://lv.dingtalk.com/interaction/createLike?uuid=' + uuid + '&count=' + str(count)
print(url)

def upLoad():
    requests.get(url)
def upLoadLoop():
    times = int(line.get())
    if(times > 10000000 or times <= 0):
        tk.messagebox.showerror(title='Error!', message='Error! 0 < times <= 10000000')
    else:
        i=1
        while(i <= int(times)):
            upLoad()
            i += 1
        tk.messagebox.showinfo(message='完成！')

window = tk.Tk()
window.title('DingTalk Likes')
window.geometry('500x300')

lb_uuid = tk.Label(text='uuid = '+uuid)
# line_uuid = tk.Entry(width=35)
# line_uuid.insert(0, uuid)
line = tk.Entry()
btn_go = tk.Button(height=2, width=16, text='冲!', command=upLoad)
btn_loop = tk.Button(height=3, width=20, text='循环冲!', command=upLoadLoop)
lb = tk.Label(text='设置循环次数(单次循环点赞数 = '+str(count)+'次)：')
lb_tip = tk.Label(text='每次'+str(count)+'个点赞：')
lb_name = tk.Label(text='by RiceQuakes', fg='red')

lb_uuid.pack()
# line_uuid.pack()
lb_tip.pack()
btn_go.pack()
lb.pack()
line.pack()
btn_loop.pack()
lb_name.pack()

window.mainloop()
