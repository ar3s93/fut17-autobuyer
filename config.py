import fut

email = raw_input('Insert your email\n')
pwd = raw_input('Insert your password\n')
sec_ans = raw_input('Insert your security answer\n')
sec_code= raw_input('Insert your security code (SMS or email)\n')
plt = raw_input('Insert your platform (please use: ps4 or ps3 or xbox360 or pc or xbox)\n')

#Connection to EA
#Code= for two factor
#Platform: ps4 - ps3 - xbox360 - pc -xbox
def connect():
    return fut.Core(email=email, passwd=pwd, secret_answer=sec_ans, platform=plt, code=sec_code, debug=True)