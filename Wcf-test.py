from wcferry import Wcf

wcf = Wcf()
res = wcf.is_login()
print(res)

info = wcf.get_user_info()

print(info)


dinfo = wcf.get_info_by_wxid('wxid_iwia62utkg0022')

print(dinfo)

get_contacts = wcf.get_contacts()

print(get_contacts)