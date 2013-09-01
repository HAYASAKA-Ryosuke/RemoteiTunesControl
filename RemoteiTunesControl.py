#coding:utf-8
import unittest
import csv
import sqlite3

class MusicList(object):
    def __init__(self,musictxt):
        f=open(musictxt)
        datalist=f.readline().split(',')
        self.musiclist=[]
        indexnum=1
        musicnum=0
        for data in datalist:
            if(indexnum%2==0 and data=="\"" or data==" \""):
                indexnum+=1
            elif(data=='\"' or data==' \"'):
                indexnum+=1
            elif(data!="\"" or data!=" \""):
                if(musicnum%2==0):
                    self.musiclist.append(data)
                else:
                    self.musiclist.append(','+data+'\n')
                musicnum+=1
    def writecsv(self,musiclistname):
        writer=open(musiclistname,'wb')
        for data in self.musiclist:
            writer.write(data)
        writer.close()
        return True

class RemoteiTunesControlTest(unittest.TestCase):
    def setUp(self):
        self.musictxtTestData="\", album1, \", \",music1, \", \", album2, \",\", music2, \""
    def test_musiclist(self):
        getarray=MusicList('./music.txt')
        self.assertTrue(getarray.writecsv('musiclist.csv'))
unittest.main()
#getarray=MusicList('./music.txt')
#getarray.writecsv('musiclist.csv')

