import urllib2
import re

def main():
    
    # In last iteration, ix = 66831.

    ix = 66831 #12345
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}'

    print 'Start looping, type in "end" to terminate.'

    for i in range(400):
        res = urllib2.urlopen( url.format(ix) ).read()
        print res

        try:
            ix = re.search('and the next nothing is (\d+)', res).group(1)
        except:
            ix = raw_input()
            if ix == 'end':
                break

    print 'http://www.pythonchallenge.com/pc/def/{0}'.format(res)

if __name__ == '__main__':
    main()
