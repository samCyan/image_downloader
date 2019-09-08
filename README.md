### image_downloader  
Given a list of image urls this utility downloads them to your local  


**Steps to use image_downloader-**  
1. Clone it to your machine-  
    git clone https://github.com/samCyan/image_downloader.git  
2. create a virtual environment-  
```
virtual venv  
source venv/bin/activate  
```
3. Open the project using one of the IDE's or may be shell  
4. add <path to the downloaded source code>/image_downloader/src to $PYTHONPATH/sys.path-  
```
import os.path  
import sys  
sys.path.append(<path to the downloaed source code>/image_downloader/src)  
```
5. call following lines of code-  
```
from src.fetch import FetchImages   
fetchimages = FetchImages()  
source = <text file containing list of image urls>  
dest = <output directory>  
fetchimages.fromFile(source).saveTo(dest)  
```

**To run unit test cases, execute the following command in your shell-**  
```
python -m unittest discover .  
or  
python -m unittest discover -s <directory> -p '*_tests.py'  
```

**Future book of work-**  
add more functionalities for multi thread/ process support  
&nbsp;&nbsp;&nbsp;&nbsp;-support byte range header in requests  
&nbsp;&nbsp;&nbsp;&nbsp;-support seeking files to a position  
add feature for handling same file download  
streamline handlers  
&nbsp;&nbsp;&nbsp;&nbsp;-let one interface hold contracts for functionalities  
make it compatible with Redis Queue and workers architecture  
dockerize the whole thing  

