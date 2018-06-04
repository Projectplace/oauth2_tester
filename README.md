# Test Oauth2

## Installation

### 1. Clone this repo
Open test_oauth2.py in an editor and modify the following attributes to point to the service you want to test:

```
authorization_base_url = 'https://api.projectplace.com/oauth2/authorize'
token_url = 'https://api.projectplace.com/oauth2/access_token'
api_endpoint = 'https://api.projectplace.com'
```

Or leave the Projectplace endpoints if you are testing towards Projectplace.

### 2. (optional) Start up a python virtualenv
(`https://blog.dbrgn.ch/2012/9/18/virtualenv-quickstart/)

```
$ virtualenv VIRTUAL
$ source VIRTUAL/bin/activate
```

Your prompt should now include the word (VIRTUAL) before the prompt such as:

`(VIRTUAL) $`

### 3. Install required python packages
If you did step 2 simply run:

```
$ pip install -r requirements.txt
```

If you didn't set up a virtualenv: run pip with sudo or admin-privileges.

### 4 Run the script

Invoke the script by calling `test_oauth2.py` with the client's client key, secret and redirect URI, 
separated by space. Such as:

```
$ python test_oauth2.py CLIENT_ID CLIENT_SECRET REDIRECT_URI
```

For example

```
$ python test_oauth2.py af3019238391238af fbcd739dddeedacba3829349 https://www.example.com/myredirect
```

The script will open a browser and ask you to authenticate your application - once done the redirect will be
opened. From the address bar copy the "code" parameter and paste it into the terminal.

```
Opening webrowser to https://api.projectplace.com/oauth2/authorize?...etc
Enter Code: ENTER_CODE_HERE
```

Once the code has been entered - you should get the following response:

```
User successfully authorized, with token: {u'access_token': u'La2pcx1SRwe-CigfnDbkTw', u'token_type': u'Bearer',u'expires': 2592000, u'expires_in': 2592000, u'refresh_token': u'ThuFVkA0SsOz8GbiWXLBJg'}
Calling with token {u'access_token': u'La2pcx1SRwe-CigfnDbkTw', u'token_type': u'Bearer', u'expires': 2592000, u'expires_in': 2592000, u'refresh_token': u'ThuFVkA0SsOz8GbiWXLBJg'}
200 OK Successfully fetched profile belonging to My Name
```

The access token gets saved to `access_token.json` and if you rerun the script it will automatically retry with the
stored access token.

### 5. Force refresh
If you want to test that refreshing works - simply add the parameter `--force_refresh` to your invokation of the script, such as:

```
$ python test_oauth2.py CLIENT_ID CLIENT_SECRET REDIRECT_URI --force_refresh
```

### 6. Start from the beginning
Either delete the access_token.json file, OR call the script with the `--reauthenticate` flag. This will render a completely
new access token, without refreshing any existing one.



