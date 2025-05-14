When browsing a mapped network drive on windows and you find the path of a directory you are interested in, you cannot
copy and paste this path to the linux server system. This is due to the windows path names having forward slashes (\)
to sperate directories while linux uses backslashes (/).

This is possible to do manually but there are 2 cons:
(1) Time taken to manually remove forward slashes and add backslashes
(2) Human error which could result in wrong path names

--HOW TO RUN--

(1) Press shift+enter in directory and open a powershell window
(2) Run command : python path_converter.py
(3) Paste the windows path in the powershell
(4) Copy the output linux path and paste in server
(5) Double check the path before running any analysis

-- V1 of this program does not account for error handling please provide a clear windows path