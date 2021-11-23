import html2jira

h = html2jira.HTML2Jira()
h.ignore_links = True
h.ignore_images = True
print(h.handle("<p>Hello, <a href='http://earth.google.com/'>world</a>!"))
