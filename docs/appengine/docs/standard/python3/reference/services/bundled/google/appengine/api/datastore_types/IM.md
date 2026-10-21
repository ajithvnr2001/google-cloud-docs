---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/datastore_types/IM/
title: google.appengine.api.datastore_types.IM \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:22:58.317342+00:00
---

# google.appengine.api.datastore_types.IM  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/datastore_types/IM/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.datastore_types.IM Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore_types.py#L985-L1075) An instant messaging handle. Includes both an address and its protocol. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)

#### View aliases

**Main aliases** `google.appengine.api.datastore.datastore_types.IM`, `google.appengine.ext.db.IMProperty.data_type`
    
    
    google.appengine.api.datastore_types.IM(
        protocol, address=None
    )
    

The protocol value is either a standard IM scheme or a URL identifying the IM network for the protocol. Possible values include: Value Description sip SIP/SIMPLE unknown Unknown or unspecified xmpp XMPP/Jabber http://aim.com/ AIM http://icq.com/ ICQ http://talk.google.com/ Google Talk http://messenger.msn.com/ MSN Messenger http://messenger.yahoo.com/ Yahoo Messenger http://sametime.com/ Lotus Sametime http://gadu-gadu.pl/ Gadu-Gadu This is the gd:im element. In XML output, the address and protocol are provided as the address and protocol attributes, respectively. See: https://developers.google.com/gdata/docs/1.0/elements#gdIm Serializes to `<protocol> <address>`. Raises `BadValueError` if tag is not a standard IM scheme or a URL.

## Methods

### `ToXml`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore_types.py#L1069-L1072)
    
    
    ToXml()
    

### `__eq__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/cmp_compat.py#L55-L55)
    
    
    __eq__(
        other
    )
    

Return self==value.

### `__ge__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/cmp_compat.py#L57-L57)
    
    
    __ge__(
        other
    )
    

Return self>=value.

### `__gt__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/cmp_compat.py#L52-L57)
    
    
    __gt__(
        other
    )
    

Return self>value.

### `__le__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/cmp_compat.py#L54-L54)
    
    
    __le__(
        other
    )
    

Return self<=value.

### `__len__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore_types.py#L1074-L1075)
    
    
    __len__()
    

### `__lt__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/cmp_compat.py#L53-L53)
    
    
    __lt__(
        other
    )
    

Return self<value.

### `__ne__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/cmp_compat.py#L56-L56)
    
    
    __ne__(
        other
    )
    

Return self!=value. | 

## Class Variables  
  
---  
  
PROTOCOLS |  `['sip', 'unknown', 'xmpp']`  
address |  `None`  
protocol |  `None`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
