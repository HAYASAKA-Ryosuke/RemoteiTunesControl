#coding:utf-8
import unittest
import csv
import sqlite3
import os.path

class MusicList(object):
    _musiclist=[]
    def album_musicnamesplit(self,musicnum,data):
        if(musicnum%2==0):
            self._musiclist.append(data)
        else:
            self._musiclist.append(data)

    def __init__(self,musictxt):
        f=open(musictxt)
        datalist=f.readline().split(',')
        indexnum=1
        musicnum=0
        for data in datalist:
            if(indexnum%2==0 and data=="\"" or data==" \""):
                indexnum+=1
            elif(data=='\"' or data==' \"'):
                indexnum+=1
            else:
                self.album_musicnamesplit(musicnum,data)
                musicnum+=1
    def writecsv(self,musiclistname):
        writer=open(musiclistname,'wb')
        for data in self._musiclist:
            writer.write(data)
        writer.close()
        return True
    def writeDatabase(self):
        con=musicDatabase('musicdatabase.sqlite')
        albumdata=''
        musicdata=''
        idnum=0
        for i,data in enumerate(self._musiclist):
            i+=1
            if i%2==1:
                albumdata=data.replace("'","''")
            if i%2==0:
                musicdata=data.replace("'","''")
                if(con.searchdata(musicdata)==False):
                    con.adddata(idnum,albumdata,musicdata)
                idnum+=1
        con.commitdata()

class musicDatabase(object):
    _con=sqlite3
    def __init__(self,databasename):
        if(os.path.exists(databasename)==False):
            self._con=sqlite3.connect(databasename)
            sql=u"""
            create table Music(
                Album varchat(300),
                Name varchat(300)
            );
            """
            self._con.execute(sql)
        else:
            self._con=sqlite3.connect(databasename)

    def adddata(self,idnum,albumname,musicname):
        if(albumname==' '):
            albumname='AlbumNameNone'
        else:
            pass
        sql="insert into Music values(\""+albumname+"\",\""+musicname+"\")"
        self._con.execute(sql)

    def searchdata(self,musicname):
        sql="select count(Name) from Music where Name like\"%"+musicname+"%\""
        kekka=self._con.execute(sql)
        self._con.commit()
        for row in kekka:
            if(row[0]>0):
                return True
            else:
                return False
        
    def commitdata(self):
        self._con.commit()
        self._con.close()
        
class RemoteiTunesControlTest(unittest.TestCase):
    def setUp(self):
        self.musictxtTestData="\", album1, \", \",music1, \", \", album2, \",\", music2, \""
        self.musicdatabasetest=" Branches (Japanese edition), Amber"
        self.musicdatabasetest2=" "

    def test_musiclist(self):
        getarray=MusicList('./music.txt')
        #self.assertTrue(getarray.writecsv('musiclist.csv'))
        self.assert_(getarray.writeDatabase())
        #self.assert_(getarray.searchdata(' 2013_04_23_13_18_49_0597'))
    #def test_database(self):
    #    con=musicDatabase('./musicdatabase.sql')
    #    self.assertTrue(con)
unittest.main()
#getarray=MusicList('./music.txt')
#getarray.writecsv('musiclist.csv')

