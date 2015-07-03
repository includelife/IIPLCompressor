# -*- coding: utf-8 -*-
from Tkinter import *
import tkFileDialog
import tkMessageBox
from FileDialog import *
import zip_no_crop
import unzip_no_crop

def resource_path(relative_path):
	if hasattr(sys,'_MEIPASS'):
		base_path = sys._MEIPASS
	else:
		base_path = os.abspath('.')
	return os.path.join(base_path,relative_path)


#中文路径问题
reload(sys)
sys.setdefaultencoding('utf-8')

# main window
window = Tk()
# window.geometry('600x400')
window.minsize(650,350)
# window.maxsize(800,450)
window.iconbitmap(resource_path('res\\iipl.ico'))
print resource_path('res\\iipl.ico')
window.title("IIPL简历压缩器")
#menu
menubar = Menu(window)
level=StringVar(None)
level.set('-o1')

def select_file():
	returned_values=tkFileDialog.askopenfilename(
									filetypes=[('Image files','*.bmp;*.dib;*.jpeg;*.jpg;*.jpe;*.jp2;*.png;*.pbm;*.pgm;*.ppm;*.sr;*.ras;*.tiff;*.tif'),
												('Windows bitmaps','*.bmp;*.dib'),
												('JPEG files','*.jpeg;*.jpg;*.jpe'),
												('JPEG 2000 files','*.jp2'),
												('Portable Network Graphics','*.png'),
												('Portable image format','*.pbm;*.pgm;*.ppm'),
												('Sun rasters','*.sr;*.ras'),
												('TIFF files','*.tiff;*.tif')
											  ])
	file_name.set(returned_values)
	return

def select_dir():
	returned_values=tkFileDialog.askdirectory()
	file_dir.set(returned_values)
	# print returned_values
	return

def select_decom_file():
	returned_values=tkFileDialog.askopenfilename(
									filetypes=[('IIPL files','*.iipl'),
									          ])
	decom_file_in_name.set(returned_values)
	# print returned_values
	return

def select_decom_dir():
	returned_values=tkFileDialog.askdirectory()
	decom_file_out_dir.set(returned_values)
	return

def get_comfile_name():
	name = com_file_in_path.get().split('/')[-1]
	return name

def get_decomfile_name():
	name = 'resrore_'+decom_file_in_path.get().split('/')[-1].rstrip('.iipl')
	return name

def clear():
	file_name.set('')
	return

def sel():
	level = level_var.get()
	# print level
	return

def compress():	
	com_file_path = com_file_in_path.get()
	com_folder_path = com_file_out_path.get()+'/'+get_comfile_name()
	# print com_file_path,com_folder_path
	# print com_file_in_path.get()
	level = level_var.get()
	zip_no_crop.compress_cv_with_image(com_file_path,com_folder_path,level)

def decompress():
	decom_file_path = decom_file_in_name.get()
	decom_folder_path = decom_file_out_dir.get()+'/'+get_decomfile_name()
	unzip_no_crop.recover_cv_from_iipl(decom_file_path,decom_folder_path)

def about():
	tkMessageBox.showinfo('关于','created by huzhp & David liu \n If you have any question or advices,you can cantact us with the email:\n 262548467@qq.com \n 244252585@qq.com')

def help():
	tkMessageBox.showinfo('帮助','这是一个简单的简历压缩工具，支持.jpg,.png,.tif等格式的输入(不支持.gif),为了尽可能的减小压缩后的文件大小，压缩后的文件将会是黑白的。压缩后的文件后缀为.iipl，该文件必须要在解压后才可以打开,解压后的文件名会加上前缀"restore_"。\n\n使用方法:首先选择您要压缩的文件，然后选择您需要存放压缩文件的地址，然后点击压缩即可。压缩的时候可以选择压缩比，越高的压缩比将会消耗更多的时间，建议选择"中"。如果您需要解压文件，选择要解压的.iipl文件和解压后存放文件的地址即可。')

#file menu
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label="添加图片", command = select_file)
filemenu.add_command(label="解压图片", command = select_decom_file)
filemenu.add_command(label="移除选中的图片", command = clear)
# filemenu.add_command(label="Save as...", command = None)
# filemenu.add_command(label="Close", command = None)       
filemenu.add_command(label="退出", command=window.quit)
menubar.add_cascade(label="文件", menu = filemenu)

#opti menu 	
# optimenu = Menu(menubar,tearoff = 0)
# optimenu.add_command(label='选项',command = None)
# menubar.add_cascade(label='选项',menu = optimenu)

#help menu
helpmenu = Menu(menubar,tearoff = 0)
helpmenu.add_command(label='帮助',command = help)
helpmenu.add_command(label='关于',command = about)
menubar.add_cascade(label='帮助',menu = helpmenu)

select_frame = LabelFrame(window,text='压缩选项')
select_frame.pack(fill='x',side='top',expand='no')
level_var = StringVar()
level_var.set('-o4')
R1 = Radiobutton(select_frame, text="低", variable=level_var, value='-o1',command=sel)
R1.pack(side='left')
R2 = Radiobutton(select_frame, text="中", variable=level_var, value='-o4',command=sel)
R2.pack(side='left')
R3 = Radiobutton(select_frame, text="高", variable=level_var, value='-o7',command=sel)
R3.pack(side='left')



compress_frame = LabelFrame(window,text='压缩：')
compress_frame.pack(fill='x',side='top',expand='yes')

#compress label
com_var = StringVar()         
com_label = Label(compress_frame,textvariable = com_var)
com_var.set('请选择要压缩的.jpg文件')
com_label.pack(fill='x',side='top')
# com_label.place(bordermode=INSIDE,height=20,width=200,x=10,y=0)

#compress file in path
entry_frame1 = Frame(compress_frame)
entry_frame1.pack(fill='x',expand='yes',side='top')

file_name = StringVar(None)
com_file_in_path = Entry(entry_frame1,textvariable=file_name)
# com_file_in_path.place(height=20,width=500,x=10,y=25)
com_file_in_path.pack(fill=X,expand=1,side=LEFT)

#select button
select_button1 = Button(entry_frame1,text = '浏览',command = select_file)
# select_button1.place(height=20,width=40,x=520,y=25)
select_button1.pack(fill=X,expand=0,side=RIGHT,padx=5)



com_out_var = StringVar(None)
com_out_label = Label(compress_frame,textvariable = com_out_var)
com_out_var.set('请选择要输出的目录')
# com_out_label.place(height=20,width=200,x=10,y=50)
com_out_label.pack(fill='x',side='top')

entry_frame2 = Frame(compress_frame)
entry_frame2.pack(fill='x',expand='yes',side='top')

#compress fiel out path
file_dir = StringVar(None)
com_file_out_path = Entry(entry_frame2,textvariable=file_dir)
# com_file_out_path.place(height=20,width=500,x=10,y=75)
com_file_out_path.pack(fill='x',expand='yes',side='left')

#select button
select_button2 = Button(entry_frame2,text = '浏览',command = select_dir)
# select_button2.place(height=20,width=40,x=520,y=75)
select_button2.pack(fill='x',side='left',padx=5)

compress_button = Button(entry_frame2, text = '压缩', command = compress)
# compress_button.place(height=20,width=50,x=580,y=75)
compress_button.pack(fill='x',side='right')


decompress_frame = LabelFrame(window,text='解压：')
decompress_frame.pack(fill='x',side='top',expand='yes')

#decompress label
decom_var = StringVar()         
decom_label = Label(decompress_frame,textvariable = decom_var)
decom_var.set('请选择要解压的.iipl文件')
decom_label.pack(fill='x',side='top')
# decom_label.place(bordermode=INSIDE,height=20,width=200,x=10,y=150)


entry_frame3 = Frame(decompress_frame)
entry_frame3.pack(fill='x',side='top')

#compress file in path
decom_file_in_name = StringVar(None)
decom_file_in_path = Entry(entry_frame3,textvariable=decom_file_in_name)
decom_file_in_path.pack(fill='x',expand='yes',side='left')
# decom_file_in_path.place(height=20,width=500,x=10,y=175)

#select button
select_button3 = Button(entry_frame3,text = '浏览',command = select_decom_file)
select_button3.pack(fill='x',side='right',padx=5)
# select_button3.place(height=20,width=40,x=520,y=175)

decom_out_var = StringVar()
decom_out_label = Label(decompress_frame,textvariable = decom_out_var)
decom_out_var.set('请选择要输出的目录')
decom_out_label.pack(fill='x',side='top')
# decom_out_label.place(height=20,width=200,x=10,y=200)

entry_frame4 = Frame(decompress_frame)
entry_frame4.pack(fill='x',side='top')

#compress fiel out path
decom_file_out_dir = StringVar(None)
decom_file_out_path = Entry(entry_frame4,textvariable=decom_file_out_dir)
decom_file_out_path.pack(fill='x',expand='yes',side='left')
# decom_file_out_path.place(height=20,width=500,x=10,y=225)

#select button
select_button4 = Button(entry_frame4,text = '浏览',command = select_decom_dir)
select_button4.pack(fill='x',side='left',padx=5)
# select_button4.place(height=20,width=40,x=520,y=225)


decompress_button = Button(entry_frame4,text = '解压',command = decompress)
decompress_button.pack(fill='x',side='right')
# decompress_button.place(height=20,width=50,x=580,y=225)


window.config(menu = menubar)
window.mainloop()
