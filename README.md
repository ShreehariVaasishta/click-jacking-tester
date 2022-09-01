# Test Clickjacking

A python script to check if the website is vulnerable of clickjacking and creates a simple html file as a proof of concept.

### Usage

```
python click-jacking-tester.py <file_name>
```

### Example
![demo](https://github.com/ShreehariVaasishta/click-jacking-tester/blob/main/image.png)


##### Input

```
python click-jacking-tester.py sites.txt
```

##### sites.txt

```
www.google.com
```

##### Output

```
Testing Site - www.google.com
                 Website is not vulnerable! ✓

Testing Site - youtube.com
                 Website is not vulnerable! ✓

Testing Site - github.com
                 Website is not vulnerable! ✓
```
