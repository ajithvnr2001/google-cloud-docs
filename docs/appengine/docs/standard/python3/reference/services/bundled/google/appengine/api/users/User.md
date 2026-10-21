---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/users/User/
title: google.appengine.api.users.User \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:16:34.432302+00:00
---

# google.appengine.api.users.User  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/users/User/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.users.User Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/users.py#L61-L239) Provides the email address, nickname, and `ID` for a user. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)

#### View aliases

**Main aliases** `google.appengine.ext.db.UserProperty.data_type`
    
    
    google.appengine.api.users.User(
        email=None,
        _auth_domain=None,
        _user_id=None,
        federated_identity=None,
        federated_provider=None,
        _strict_mode=True
    )
    

A nickname is a human-readable string that uniquely identifies a Google user, akin to a username. For some users, this nickname is an email address, but for other users, a different nickname is used. A user is a Google Accounts user. `federated_identity` and `federated_provider` are decommissioned and should not be used. | 

## Args  
  
---  
  
`email` |  An optional string of the user's email address. It defaults to the current user's email address.   
`federated_identity` |  Decommissioned, don't use.   
`federated_provider` |  Decommissioned, don't use.   
  
## Raises  
  
---  
  
`UserNotFoundError` |  If the user is not logged in and both `email` and `federated_identity` are empty.   
  
## Methods

### `auth_domain`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/users.py#L168-L175)
    
    
    auth_domain()
    

Obtains the user's authentication domain.

Returns  
---  
A string containing the authentication domain. This method is internal and should not be used by client applications.   
  
### `email`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/users.py#L155-L157)
    
    
    email()
    

Returns the user's email address.

### `federated_identity`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/users.py#L177-L184)
    
    
    federated_identity()
    

Decommissioned, don't use.

Returns  
---  
A string containing the federated identity of the user. If the user is not a federated user, `None` is returned.   
  
### `federated_provider`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/users.py#L186-L193)
    
    
    federated_provider()
    

Decommissioned, don't use.

Returns  
---  
A string containing the federated provider. If the user is not a federated user, `None` is returned.   
  
### `nickname`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/users.py#L136-L153)
    
    
    nickname()
    

Returns the user's nickname.

The nickname will be a unique, human readable identifier for this user with respect to this application. It will be an email address for some users, and part of the email address for some users.

Returns  
---  
The nickname of the user as a string.   
  
### `user_id`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/users.py#L159-L166)
    
    
    user_id()
    

Obtains the user `ID` of the user.

Returns  
---  
A permanent unique identifying string or `None`. If the email address was set explicitly, this will return `None`.   
  
### `__eq__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/users.py#L217-L227)
    
    
    __eq__(
        other
    )
    

Return self==value.

### `__ge__`
    
    
    __ge__(
        other, NotImplemented=NotImplemented
    )
    

Return a >= b. Computed by @total_ordering from (not a < b).

### `__gt__`
    
    
    __gt__(
        other, NotImplemented=NotImplemented
    )
    

Return a > b. Computed by @total_ordering from (not a < b) and (a != b).

### `__le__`
    
    
    __le__(
        other, NotImplemented=NotImplemented
    )
    

Return a <= b. Computed by @total_ordering from (a < b) or (a == b).

### `__lt__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/users.py#L232-L239)
    
    
    __lt__(
        other
    )
    

Return self<value.

### `__ne__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/users.py#L229-L230)
    
    
    __ne__(
        other
    )
    

Return self!=value.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
