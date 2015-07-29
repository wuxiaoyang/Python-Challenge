import pickle
import urllib2

def main():

    res = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/banner.p')
    res = res.read()
    content = pickle.loads(res)

    with open('./data/5.out','w') as fout: 
        for line in content:
            for c,n in line:
                fout.write(c*n)
            fout.write('\n')

if __name__ == '__main__':
    main()
