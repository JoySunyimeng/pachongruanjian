all = []
userType = set(['陌生人','朋友'])
def newUser(name,age,utype,*tels,city='北京',des='这个家伙很懒',**kw):
    person = {}
    person['name'] = name #input('姓名：')
    person['age'] = age #int(input('年龄：'))
    person['type'] = utype
    person['city'] = city
    person['des'] = des
    person['tels'] = tels
    person['kw'] = kw
    all.append(person)
    print('用户信息已保存')
def listUser():
    i = 0
    for person in all:
        print(i,person['name'])
        i += 1
def userDetail():
    index = int(input('请输入要查看的用户序号：'))
    print(all[index])
def deleteUser():
    index = int(input('请输入要删除的用户序号：'))
    print(all.pop(index))
while True:
    cmd = input('请选择要进行的操作：\n n:新建,l:列出,v:详细,d:删除,q:退出')
    if cmd == 'q':
        break
    elif cmd == 'n':
        n = input('姓名：')
        a = int(input('年龄：'))
        tels = []
        while True:
            tel = input('电话（end结束）：')
            if tel == 'end':
                print('电话已保存')
                break
            tels.append(tel)
        kw = {}
        while True:
            k = input('key(end结束):')
            v = input('value:')
            if k == 'end':
                print('附加信息已保存')
                break
            kw[k] = v
        utype = ''
        while True:
            print(userType)
            utype = input('用户类型：')
            if utype in userType:
                break
        city = input('城市：')
        des = input('简介：')
        if city == '' and des == '':
            newUser(n,a,utype,*tels,**kw)
        elif des == '':
            newUser(n,a,utype,*tels,city,**kw)
        else:
            newUser(n,a,utype,*tels,city,des,**kw)
    elif cmd == 'l':
        listUser()
    elif cmd == 'v':
        userDetail()
    elif cmd == 'd':
        deleteUser()
    else:
        print('请输入正确的命令')
print('程序退出')