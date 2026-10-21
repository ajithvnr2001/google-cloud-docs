---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/app_identity/app_identity_stub/AppIdentityServiceStub/
title: google.appengine.api.app_identity.app_identity_stub.AppIdentityServiceStub \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:53:08.026885+00:00
---

# google.appengine.api.app_identity.app_identity_stub.AppIdentityServiceStub  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/app_identity/app_identity_stub/AppIdentityServiceStub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.app_identity.app_identity_stub.AppIdentityServiceStub Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/app_identity/app_identity_stub.py#L43-L75) A stub for the AppIdentityService API for offline development. Inherits From: [`AppIdentityServiceStubBase`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/app_identity/app_identity_stub_base/AppIdentityServiceStubBase), [`APIProxyStub`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/apiproxy_stub/APIProxyStub), [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.api.app_identity.app_identity_stub.AppIdentityServiceStub(
        service_name='app_identity_service'
    )
    

Provides stub functions which allow a developer to test integration before deployment. Automatically creates appropriate stub (default credentials or key based) using `Create()`.

## Methods

### `Clear`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/app_identity/app_identity_stub_base.py#L197-L199)
    
    
    Clear()
    

Resets the state on the App Identity stub.

### `Create`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/app_identity/app_identity_stub.py#L54-L75)
    
    
    @staticmethod
    Create(
        email_address=None, private_key_path=None, oauth_url=None
    )
    

### `CreateRPC`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/apiproxy_stub.py#L87-L93)
    
    
    CreateRPC()
    

Creates RPC object instance. | Returns  
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
  
### `SetDefaultGcsBucketName`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/app_identity/app_identity_stub_base.py#L160-L164)
    
    
    SetDefaultGcsBucketName(
        default_gcs_bucket_name
    )
    

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
  
### `get_service_account_name`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/app_identity/app_identity_stub_base.py#L188-L189)
    
    
    get_service_account_name()
    

### `get_service_account_token`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/app_identity/app_identity_stub_base.py#L166-L186)
    
    
    get_service_account_token(
        scopes, service_account=None
    )
    

test implementation for _metadata_server.get_service_account_token.

This API returns an invalid token, as the `dev_appserver` does not have access to an actual service account. Subclasses override this function with more useful implementations.

Args  
---  
  
`scopes` |  a list of oauth2 scopes.   
`service_account` |  the service account to get the token for   
  
Returns  
---  
Tuple of access token and expiration time in epoch   
  
## Class Variables  
  
---  
  
THREADSAFE |  `True`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
