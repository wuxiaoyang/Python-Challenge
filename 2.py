import string

def main():
    fin = open('./data/2.txt','r').read()

    cnt = {}
    for i in fin:
        cnt[i] = cnt.get(i,0) + 1
    cnt.pop('\n')

    fin.close()

    print 'Letter Count'.center(80,'-')
    for c,n in cnt.iteritems():
        print 'Letter {0} occurs for {1} times.'.format(c,n) 
    print 'Letter Count'.center(80,'-')

    l = [ i for i in fin if i in string.ascii_lowercase]

    print 'http://www.pythonchallenge.com/pc/def/{0}.html'.format(''.join(l))

if __name__ == '__main__':
    main()
