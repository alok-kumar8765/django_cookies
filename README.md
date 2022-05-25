# django_cookies
using example to understand cookies
## Cookies

    Acookies is a small piece of text data set by Web Server that resided on the client's machine.
    Once it's been set, the client automatically returns the cookie to the web Server with each request that it makes.
    This allows the server to place value it wishes to 'remember' in the cookie, and have access to them when creating a response.

### Django Cookies

    HttpRequest.COOKIES - A dictionary containing all cookies. Keys and values are strings.


## Creating Cookies

    set_cookie() - set_cookie() is used to set/create/sent cookies.

    Syntax :- HttpRequest.set_cookie(key,value="",max_age=None,expires=None,path='/',domain=None,secure=False,httponly=False,samesite=None)

    when you omit the optional cookie fields, the browser fills them in automatically with resonable defaults.

    max_age = none means when browser closed the cookie get expired
    example : set_cookie('name','alok',max_age=60*60*24*10) // cookie workes for 10 day

    Expires = it describe the time when cookie will be expire.
    example = set_cookie('name','alok',expires = datetime.utcnow()+timedelta(days=2))

## Reading/Accessing Cookies

    HttpRequest.COOKIES- a dictionary all cookies. keys and values are strings
    Syntax : request.COOKIES['key']
    example : request.COOKIES['name']