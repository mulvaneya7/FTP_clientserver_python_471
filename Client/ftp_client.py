from ftplib import FTP
import subprocess

ftp = FTP('')
ftp.connect('localhost',5000)
ftp.login()
ftp.cwd('/') #replace with your directory
ftp.retrlines('LIST')

def uploadFile(filename_):
    filename = filename_
    ftp.cwd('/Stories/')
    ftp.storbinary('STOR '+filename, open(filename, 'rb'))
    ftp.cwd('/')
    # ftp.pwd()
    # ftp.quit()

def downloadFile(filename_):
    filename = filename_  #replace with your file in the directory ('directory_name')
    localfile = open(filename, 'wb')
    ftp.cwd('/Stories/')
    ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
    ftp.cwd('/')
    # ftp.quit()
    localfile.close()

todownload = input(str("Upload a story to our folder? (Y/n): "))
if todownload.upper() == 'Y':
    for line in subprocess.getstatusoutput('ls -l'):
        print(line)
    fileto = input(str("Please enter a filename to upload: "))
    uploadFile(fileto)
todownload = input(str("Download our stories folder? (Y/n): "))
if todownload.upper() == 'Y':
    todownload = input(str("Which story would you like to download: "))
    downloadFile(todownload)
print("Thank you for visiting!")
ftp.quit()
#uploadFile()
#downloadFile()