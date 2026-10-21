---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_query/Cursor/
title: google.appengine.datastore.datastore_query.Cursor \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:27:46.924772+00:00
---

# google.appengine.datastore.datastore_query.Cursor  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_query/Cursor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.datastore.datastore_query.Cursor Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_query.py#L1554-L1693) An immutable class that represents a relative position in a query. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.datastore.datastore_query.Cursor(
        urlsafe=None, _cursor_bytes=None
    )
    

The position denoted by a Cursor is relative to a result in a query even if the result has been removed from the given query. Usually to position immediately after the last result returned by a batch. A cursor should only be used on a query with an identical signature to the one that produced it or on a query with its sort order reversed.

## Methods

### `advance`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_query.py#L1665-L1686)
    
    
    advance(
        offset, query, conn
    )
    

Advances a Cursor by the given offset. | Args  
---  
  
`offset` |  The amount to advance the current query.   
`query` |  A Query identical to the one this cursor was created from.   
`conn` |  The datastore_rpc.Connection to use.   
  
Returns  
---  
A new cursor that is advanced by offset using the given query.   
  
### `from_bytes`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_query.py#L1602-L1619)
    
    
    @staticmethod
    from_bytes(
        cursor
    )
    

Gets a Cursor given its byte string serialized form.

The serialized form of a cursor may change in a non-backwards compatible way. In this case cursors must be regenerated from a new Query request.

Args  
---  
  
`cursor` |  A serialized cursor as returned by .to_bytes.   
  
Returns  
---  
A Cursor.   
  
Raises  
---  
datastore_errors.BadValueError if the cursor argument does not represent a serialized cursor.   
  
### `from_websafe_string`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_query.py#L1630-L1648)
    
    
    @staticmethod
    from_websafe_string(
        cursor
    )
    

Gets a Cursor given its websafe serialized form.

The serialized form of a cursor may change in a non-backwards compatible way. In this case cursors must be regenerated from a new Query request.

Args  
---  
  
`cursor` |  A serialized cursor as returned by .to_websafe_string.   
  
Returns  
---  
A Cursor.   
  
Raises  
---  
datastore_errors.BadValueError if the cursor argument is not a string type of does not represent a serialized cursor.   
  
### `reversed`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_query.py#L1590-L1596)
    
    
    reversed()
    

DEPRECATED. It is no longer necessary to call reversed() on cursors.

A cursor returned by a query may also be used in a query whose sort order has been reversed. This method returns a copy of the original cursor.

### `to_bytes`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_query.py#L1598-L1600)
    
    
    to_bytes()
    

Serialize cursor as a byte string.

### `to_websafe_string`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_query.py#L1621-L1627)
    
    
    to_websafe_string()
    

Serialize cursor as a websafe string.

Returns  
---  
A base64-encoded serialized cursor.   
  
### `urlsafe`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_query.py#L1621-L1627)
    
    
    urlsafe()
    

Serialize cursor as a websafe string.

Returns  
---  
A base64-encoded serialized cursor.   
  
### `__eq__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_query.py#L81-L84)
    
    
    __eq__(
        other
    )
    

Return self==value.

### `__ne__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_query.py#L86-L90)
    
    
    __ne__(
        other
    )
    

Return self!=value.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
