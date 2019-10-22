# Tips and tricks

## PracticePython.org

#### Install `BeautifulSoup`

To install Beautiful Soup to the virtual machine you have to install two packages: 
`python3-bs4` and `python3-lxml`. 

Install the packages using the following commands in terminal:

```
sudo apt install python3-bs4
sudo apt install python3-lxml
```

You can test your installation of the BeautifulSoup with the following code:


```python

from bs4 import BeautifulSoup

html_doc = "<html><head><title>Test</title></head><body><h1>test</h1></body></html>"

soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())
```
