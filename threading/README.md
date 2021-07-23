# When to use threading?

Use the threading to speed up the IO bound operations.<br>
Eg. Downloading images from internet<br>
    Reading data from files<br>

Threading should not be use for CPU bound operations like processing images.<br>
Using Threading for CPU bound operations will slow down the process because of
the threading overhead.