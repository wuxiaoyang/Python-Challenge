import re

def main():
    fin = open('./data/3.txt','r').read()
    text = fin.replace('\n','')

    pat = r'[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]'

    data = re.findall(pat,text)
    ans = ''.join( i[4] for i in data)

    print 'http://www.pythonchallenge.com/pc/def/{0}.html'.format(ans)

if __name__ == '__main__':
    main()
