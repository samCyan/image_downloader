# image_downloader
Given a list of image urls this utility downloads them to your local


Steps to use image_downloader-
1. Clone it to your machine
    git clone https://github.com/samCyan/image_downloader.git
2. create a virtual environment
    2.1     virtual venv
    2.2     source venv/bin/activate
3. Open the project using one of the IDE's or may be shell
4. add <path to the downloaded source code>/image_downloader/src to $PYTHONPATH/sys.path
    4.1     import os.path
    4.2     import sys
    4.3     sys.path.append(<path to the downloaed source code>/image_downloader/src)
5. call following lines of code:
    5.1     from src.fetch import FetchImages  
    5.2     fetchimages = FetchImages()
    5.3     source = <text file containing list of image urls>
    5.4     dest = <output directory>
    5.5     fetchimages.fromFile(source).saveTo(dest)


To run unit test cases, execute the following command in your shell-
    python -m unittest discover . 
    or
    python -m unittest discover -s <directory> -p '*_test.py'


Future book of work-
add more functionalities for multi thread/ process support
    support byte range header in requests
    support seeking files to a position
add feature for handling same file download
streamline handlers
    let one interface hold contracts for functionalities
make it compatible with Redis Queue and workers architecture
dockerize the whole thing 