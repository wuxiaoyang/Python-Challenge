import string

s = r"g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

def main():

    global s
    frm = string.ascii_lowercase
    to = string.ascii_lowercase[2:] + string.ascii_lowercase[:2] 
    dic = string.maketrans(frm, to)

    print 'HINT'.center(80,'-')
    print string.translate(s,dic)
    print 'HINT'.center(80,'-')

    print 'http://www.pythonchallenge.com/pc/def/{0}.html'.format(string.translate('map',dic))

if __name__ == '__main__':

    main()
