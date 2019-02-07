from __future__ import print_function
__copyright__ = """

    Copyright 2019 Samapriya Roy

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

"""
__license__ = "Apache 2.0"


from bs4 import BeautifulSoup
import requests,csv,zipfile,os,platform
from pathlib import Path
from pySmartDL import SmartDL
sysinfo=platform.machine()[-2:]
comb="win"+str(sysinfo)+".zip"
directory=os.path.dirname(os.path.realpath(__file__))
os.chdir(os.path.dirname(os.path.realpath(__file__)))
def geckodown(directory):
    source=requests.get("https://github.com/mozilla/geckodriver/releases").text
    soup=BeautifulSoup(source,'lxml')
    match=soup.find('ul',class_='release-downloads')
    i=0
    for article in soup.find_all('strong'):
        if str(comb) not in article.text:
            pass
        else:
            while i<1:
                vr=str(article.text).split("-")[1].split("-")[0]
                container="https://github.com/mozilla/geckodriver/releases/download/"+vr+"/"+str(article.text)
                print("Downloading from: "+str(container))
                try:
                    url = container
                    dest = directory
                    obj = SmartDL(url, dest)
                    obj.start()
                    path=obj.get_dest()
                    #print(article.text)
                    archive=zipfile.ZipFile(os.path.join(directory,article.text))
                    for files in archive.namelist():
                        archive.extractall(directory)
                    print("Use selenium driver path as "+str(directory))
                except Exception as e:
                    print(e)
                    
                i=i+1
    
geckodown(directory=directory)
#print(match.li.strong)

#print(match.find('li',class_='strong'))
