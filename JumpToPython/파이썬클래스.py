name = "Kakao"
email = "kaka0@naver.com"
addr = "seoul"

def business_card(name, email, addr):
    print("----------------")
    print("Name : %s" % name)
    print("E-mail : %s" % email)
    print("Office Adress : %s " % addr)
    print("-----------------")


business_card(name, email, addr)

name2 = "German"
email2 = "German2@naver.com"
addr2 = "Berlin"

business_card(name2, email2, addr2)

def foo():
    pass

print(type(foo))
