import streamlit as st
from PIL import Image
import wordcloud
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from cloud import ciyvn
from p_change import img_change
page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '词云生成小工具','我的智能词典', '我的留言区'])

def page_1(): 
    '''我的兴趣推荐'''
    st.image('slogan.png')
    st.write('点击侧边栏 发现更多')
    
def page_2():
    '''我的图片处理工具'''
    st.write(":sunglasses:图片处理小程序:sunglasses: " )
    uploaded_file = st.file_uploader("上传图片", type=[ 'png', 'jpeg', 'jpg'])
    if uploaded_file :
    #并获取图片文件的名称、类型和大小
        img = Image.open(uploaded_file)
        st.image(img)
        number1 = st.slider(':red[R]',1,255,0)
        number2 = st.slider(':green[G]',1,255,0)
        number3 = st.slider(':blue[B]',1,255,0)
        if number1 == 255 and number2 == 255 and number3 == 255:
            st.image("yuanshen.jpg")
            st.balloons()
            st.code('''# 恭喜你触发彩蛋，原神启动''')
        else:
            st.image(img_change(img,number1,number2,number3))
        
    

def page_3():
    st.write(':orange[词云生成小工具]')
    uploaded_file =st.file_uploader("Choose a file")
    if uploaded_file is not None:
        #将上传的文件转换成文本
        string_data=uploaded_file.read().decode("utf-8")
        st.image(ciyvn(string_data))
    else:
        pass


def page_4():
    '''我的智能词典'''
    st.write(':blue[智能词典]')
    # 从本地文件中将词典信息读取出来，并存储在列表中
    with open('words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    # 将列表中的每一项内容再进行分割，分为“编号、单词、解释”
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    # 将列表中的内容导入字典，方便查询，格式为“单词：编号、解释”
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]

    with open('check_out_times.txt', 'r', encoding='utf-8') as f:
        times_list = f.read().split('\n')
    # 将列表转为字典
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    # 创建输入框
    word = st.text_input('请输入要查询的单词')
    # 显示查询内容
    if word in words_dict:
        st.write(words_dict[word][1])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
    
        else:
            times_dict[n] = 1
        with open('check_out_times.txt', 'w', encoding='utf-8') as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        if word == "":
            st.write("")
        else:
            st.write('查询次数：', times_dict[n])
        if word == 'python':
            st.code('''
                # 恭喜你触发彩蛋，这是一行python代码
                print('hello world')''')
        if word == 'snow':
            st.snow()
        if word == 'birthday':
            st.balloons()
        if word == 'kind':
            st.image('kind.jpg')
            st.code('''# 恭喜你触发彩蛋，因为他善''')
            
        if word == 'genshin':
            st.image("yuanshen.jpg")
            st.code('''# 恭喜你触发彩蛋，原神启动''')
        if word == "":
            st.write("")
    elif word not in words_dict:
        st.write("对不起 未查询到此单词 请重新输入")
    
    

def page_5():
    st.write('我的留言区')
    # 从文件中加载内容，并处理成列表
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '阿短':
            with st.chat_message('🌞'):
                st.write(i[1],':',i[2])
        elif i[1] == '编程猫':
            with st.chat_message('🍥'):
                st.write(i[1],':',i[2])
        elif i[1] == 'Json':
            with st.chat_message('J'):
                st.write(i[1],':',i[2])
        elif i[1] == '匿名用户':
            with st.chat_message('?'):
                st.write(i[1],':',i[2])
        
    name = st.selectbox('我是……', ['阿短', '编程猫','Json','匿名用户'])
    new_message = st.text_input('想要说的话……')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f :
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)
    


if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '词云生成小工具':
    page_3()
elif page == '我的智能词典':
    page_4()
elif page == '我的留言区':
    page_5()