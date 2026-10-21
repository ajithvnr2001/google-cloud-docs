---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/blobstore/BlobInfo/
title: google.appengine.ext.blobstore.BlobInfo \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:07:24.734486+00:00
---

# google.appengine.ext.blobstore.BlobInfo  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/blobstore/BlobInfo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.ext.blobstore.BlobInfo Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/blobstore/blobstore.py#L186-L477) Information about blobs in Blobstore. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)

#### View aliases

**Main aliases** `google.appengine.ext.blobstore.BlobReferenceProperty.data_type`, `google.appengine.ext.blobstore.blobstore.BlobInfo`, `google.appengine.ext.blobstore.blobstore.BlobReferenceProperty.data_type`
    
    
    google.appengine.ext.blobstore.BlobInfo(
        entity_or_blob_key, _values=None
    )
    

This is a [`db.Model`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/Model)-like class that contains information about blobs that are stored by an application. Like [`db.Model`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/Model), this class is backed by a Datastore entity; however, `BlobInfo` instances are read-only and have a much more limited interface. Each `BlobInfo` has a key of type `BlobKey` associated with it. This key is specific to the Blobstore API and is not compatible with [`db.get`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/get). The key can be used for quick lookup by passing it to [`BlobInfo.get`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/blobstore/BlobInfo#get). This key converts easily to a string, which is web safe and can be embedded in URLs.

#### Properties:

  * content_type: The content type of the blob.
  * creation: The creation date of the blob, or when it was uploaded.
  * filename: The file name that the user selected from their machine.
  * size: The size of the uncompressed blob.
  * md5_hash: The MD5 hash value of the uploaded blob.
  * **`gs_object_name`** : The name of the object, if the blob is stored in Google Cloud Storage, in the form /[bucket-name]/[object-name]

All properties are read-only. Attempting to assign a value to a property will raise a `NotImplementedError`. | 

## Args  
  
---  
  
`entity_or_blob_key` |  The datastore entity or blob key that represents the blob reference.   
`_values` |  Optional; not recommended. This argument passes the associated entity when `entity_or_blob_key` is a blob key.   
  
## Attributes  
  
---  
  
`content_type` |  Returns the content type of the blob.   
`creation` |  Returns the creation date or time of upload of the blob.   
`filename` |  Returns the file name that the user selected from their machine.   
`gs_object_name` |   
`md5_hash` |  Returns the MD5 hash value of the uncompressed blob.   
`size` |  Returns the size of the uncompressed blob.   
  
## Methods

### `all`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/blobstore/blobstore.py#L390-L397)
    
    
    @classmethod
    all()
    

Creates a query for all `BlobInfo` objects associated with the app.

Returns  
---  
A [`db.Query`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/db/Query) object that queries over `BlobInfo`'s datastore kind.   
  
### `delete`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/blobstore/blobstore.py#L346-L348)
    
    
    delete(
        _token=None
    )
    

Permanently deletes a blob from Blobstore.

### `from_entity`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/blobstore/blobstore.py#L289-L303)
    
    
    @classmethod
    from_entity(
        entity
    )
    

Converts an entity to `BlobInfo`.

#### Note:

This method is required for compatibility with the current `db.py` query mechanism but will be removed in the future. DO NOT USE.

Args  
---  
  
`entity` |  The entity that you are trying to convert.   
  
Returns  
---  
The `BlobInfo` that was converted from the entity.   
  
### `get`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/blobstore/blobstore.py#L361-L388)
    
    
    @classmethod
    get(
        blob_keys
    )
    

Retrieves a `BlobInfo` by key or by a list of keys.

Args  
---  
  
`blob_keys` |  A key or a list of keys. Keys can be in string, Unicode, or `BlobKey` format.   
  
Returns  
---  
A `BlobInfo` instance that is associated with the provided key or a list of `BlobInfo` instances if a list of keys was provided. Keys that are not found in Blobstore return `None`.   
  
### `gql`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/blobstore/blobstore.py#L405-L428)
    
    
    @classmethod
    gql(
        query_string, *args, **kwds
    )
    

Returns a query using a GQL query string.

See the `GQL source` for more information about GQL.

Args  
---  
  
`query_string` |  A properly formatted GQL query string that omits `SELECT * FROM <entity>`  
`*args` |  The remaining positional arguments that are used to bind numeric references in the query.   
`**kwds` |  The dictionary-based arguments for named parameters.   
  
Returns  
---  
A `gql.GqlQuery` object that queries over `BlobInfo`'s datastore kind.   
  
.. _GQL source: https://cloud.google.com/appengine/docs/python/refdocs/google.appengine.ext.gql

### `key`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/blobstore/blobstore.py#L338-L344)
    
    
    key()
    

Gets the key for a blob.

Returns  
---  
The `BlobKey` instance that identifies this blob.   
  
### `kind`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/blobstore/blobstore.py#L431-L442)
    
    
    @classmethod
    kind()
    

Gets the entity kind for the `BlobInfo`.

#### Note:

This method is required for compatibility with the current `db.py` query mechanism but will be removed in the future. DO NOT USE.

Returns  
---  
The entity kind for `BlobInfo`.   
  
### `open`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/blobstore/blobstore.py#L350-L359)
    
    
    open(
        *args, **kwargs
    )
    

Returns a `BlobReader` for this blob.

Args  
---  
  
`*args` |  Arguments to pass to the `BlobReader` constructor.   
`**kwargs` |  Keyword arguments to pass to the `BlobReader` constructor.   
  
Returns  
---  
A `BlobReader` instance.   
  
### `properties`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/blobstore/blobstore.py#L307-L318)
    
    
    @classmethod
    properties()
    

Defines the set of properties that belong to `BlobInfo`.

#### Note:

This method is required for compatibility with the current `db.py` query mechanism but will be removed in the future. DO NOT USE.

Returns  
---  
A set of all of the properties that belong to `BlobInfo`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
