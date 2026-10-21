---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/user_service_stub/UserServiceStub/
title: google.appengine.api.user_service_stub.UserServiceStub \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:21:50.953205+00:00
---

# google.appengine.api.user_service_stub.UserServiceStub  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/user_service_stub/UserServiceStub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.user_service_stub.UserServiceStub Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/user_service_stub.py#L55-L221) Trivial implementation of the `UserService`. Inherits From: [`APIProxyStub`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/apiproxy_stub/APIProxyStub), [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.api.user_service_stub.UserServiceStub(
        login_url=_DEFAULT_LOGIN_URL,
        logout_url=_DEFAULT_LOGOUT_URL,
        service_name='user',
        auth_domain=_DEFAULT_AUTH_DOMAIN,
        request_data=None
    )
    

| 

## Args  
  
---  
  
`login_url` |  String containing the URL to use for logging in.   
`logout_url` |  String containing the URL to use for logging out.   
`service_name` |  Service name expected for all calls.   
`auth_domain` |  The authentication domain for the service (e.g. "gmail.com").   
`request_data` |  A `apiproxy_stub.RequestData` instance used to look up state associated with the request that generated an API call.   
  
## Methods

### `CreateRPC`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/apiproxy_stub.py#L87-L93)
    
    
    CreateRPC()
    

Creates RPC object instance.

Returns  
---  
An instance of RPC.   
  
### `MakeSyncCall`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/apiproxy_stub.py#L112-L143)
    
    
    MakeSyncCall(
        service, call, request, response, request_id=None
    )
    

The main RPC entry point.

Args  
---  
  
`service` |  Must be name as provided to `service_name` of constructor.   
`call` |  A string representing the rpc to make. Must be part of the underlying services methods and impemented by `_Dynamic_<call>`.   
`request` |  A protocol buffer of the type corresponding to `call`.   
`response` |  A protocol buffer of the type corresponding to `call`.   
`request_id` |  A unique string identifying the request associated with the API call.   
  
### `SetError`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/apiproxy_stub.py#L145-L163)
    
    
    SetError(
        error, method=None, error_rate=1
    )
    

Set an error condition that may be raised when calls made to stub.

If a method is specified, the error will only apply to that call. The error rate is applied to the method specified or all calls if method is not set.

Args  
---  
  
`error` |  An instance of [`apiproxy_errors.Error`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/runtime/apiproxy_errors/Error) or `None` for no error.   
`method` |  A string representing the method that the error will affect.   
`error_rate` |  a number from `[0, 1]` that sets the chance of the error, defaults to `1`.   
  
### `SetOAuthUser`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/user_service_stub.py#L95-L120)
    
    
    SetOAuthUser(
        email=_OAUTH_EMAIL,
        domain=_OAUTH_AUTH_DOMAIN,
        user_id=_OAUTH_USER_ID,
        is_admin=False,
        scopes=None,
        client_id=_OAUTH_CLIENT_ID
    )
    

Set test OAuth user.

Determines what user is returned by requests to `GetOAuthUser`.

Args  
---  
  
`email` |  Email address of OAuth user. None indicates that no oauth user is authenticated.   
`domain` |  Domain of OAuth user.   
`user_id` |  User ID of OAuth user.   
`is_admin` |  Whether the user is an admin.   
`scopes` |  List of scopes that user is authenticated against.   
`client_id` |  Client ID of the OAuth2 request   
  
## Class Variables  
  
---  
  
THREADSAFE |  `True`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
