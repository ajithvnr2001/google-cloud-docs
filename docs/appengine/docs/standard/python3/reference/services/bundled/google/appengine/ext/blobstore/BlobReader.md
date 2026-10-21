---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/blobstore/BlobReader/
title: google.appengine.ext.blobstore.BlobReader \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:24:59.793324+00:00
---

# google.appengine.ext.blobstore.BlobReader  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/blobstore/BlobReader/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.ext.blobstore.BlobReader Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/blobstore/blobstore.py#L866-L1191) Provides a read-only file-like interface to a blobstore blob. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)

#### View aliases

**Main aliases** `google.appengine.ext.blobstore.blobstore.BlobReader`
    
    
    google.appengine.ext.blobstore.BlobReader(
        blob, buffer_size=131072, position=0
    )
    

| 

## Args  
  
---  
  
`blob` |  The blob key, blob info, or string blob key to read from.   
`buffer_size` |  The minimum size to fetch chunks of data from blobstore.   
`position` |  The initial position in the file.   
  
## Raises  
  
---  
  
`ValueError` |  If a `BlobKey`, `BlobInfo`, or string blob key is not supplied.   
  
## Attributes  
  
---  
  
`blob_info` |  Returns the `BlobInfo` for this file.   
`closed` |  Determines whether a file is closed.   
  
## Methods

### `close`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/blobstore/blobstore.py#L920-L927)
    
    
    close()
    

Closes the file.

A closed file cannot be read or written to anymore. An operation that requires that the file to be open will raise a `ValueError` after the file has been closed. Calling `close()` more than once is allowed.

### `flush`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/blobstore/blobstore.py#L929-L930)
    
    
    flush()
    

### `next`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/blobstore/blobstore.py#L932-L945)
    
    
    next()
    

Returns the next line from the file.

Returns  
---  
A string, terminated by `\\n`. The last line cannot end with `\\n`. If the end of the file is reached, an empty string will be returned.   
  
Raises  
---  
  
`StopIteration` |  If there are no further lines to read.   
  
### `read`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/blobstore/blobstore.py#L1004-L1029)
    
    
    read(
        size=-1
    )
    

Reads at most `size` bytes from the file.

Fewer bytes are read if the read hits the end of the file before obtaining `size` bytes. If the `size` argument is negative or omitted, all data is read until the end of the file is reached. The bytes are returned as a string object. An empty string is returned immediately when the end of the file is reached.

Calling `read()` without specifying a `size` is likely to be dangerous, as it might read excessive amounts of data.

Args  
---  
  
`size` |  Optional. The maximum number of bytes to read. When omitted, `read()` returns all remaining data in the file.   
  
Returns  
---  
The read data, as a string.   
  
### `readline`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/blobstore/blobstore.py#L1031-L1066)
    
    
    readline(
        size=-1
    )
    

Reads one entire line from the file.

A trailing newline character is kept in the string but can be absent when a file ends with an incomplete line. If the `size` argument is present and non-negative, it represents a maximum byte count, including the trailing newline and an incomplete line might be returned. An empty string is returned immediately only when the end of the file is reached.

Args  
---  
  
`size` |  Optional. The maximum number of bytes to read.   
  
Returns  
---  
The read data, as a string.   
  
### `readlines`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/blobstore/blobstore.py#L1068-L1092)
    
    
    readlines(
        sizehint=None
    )
    

Reads until the end of the file using `readline()`.

A list of lines read is returned.

If the optional `sizehint` argument is present, instead of reading up to the end of the file, whole lines totalling approximately `sizehint` bytes are read, possibly after rounding up to an internal buffer size.

Args  
---  
  
`sizehint` |  A hint as to the maximum number of bytes to read.   
  
Returns  
---  
A list of strings, each being a single line from the file.   
  
### `seek`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/blobstore/blobstore.py#L1094-L1115)
    
    
    seek(
        offset, whence=SEEK_SET
    )
    

Sets the file's current position, like stdio's `fseek()`_.

Args  
---  
  
`offset` |  The relative offset to seek to.   
`whence` |  Optional; defines to what value the offset is relative. This argument defaults to `os.SEEK_SET` or `0` to use absolute file positioning; other valid values are `os.SEEK_CUR` or `1` to seek relative to the current position and `os.SEEK_END` or `2` to seek relative to the end of the file.   
  
.. _fseek(): http://www.cplusplus.com/reference/cstdio/fseek/

### `tell`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/blobstore/blobstore.py#L1117-L1126)
    
    
    tell()
    

Retrieves the file's current position, like stdio's `ftell()`_.

Returns  
---  
The file's current position.   
  
.. _ftell(): http://www.cplusplus.com/reference/cstdio/ftell/

### `truncate`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/blobstore/blobstore.py#L1128-L1137)
    
    
    truncate(
        size
    )
    

Raises an error if you attempt to truncate the file.

Args  
---  
  
`size` |  The size that you are attempting to truncate to.   
  
Raises  
---  
  
`IOError` |  If you attempt to truncate a file in `BlobReader`.   
  
### `write`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/blobstore/blobstore.py#L1139-L1148)
    
    
    write(
        str
    )
    

Raises an error if you attempt to write to the file.

Args  
---  
  
`str` |  The string that you are attempting to write.   
  
Raises  
---  
  
`IOError` |  If you attempt to write to a file in `BlobReader`.   
  
### `writelines`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/blobstore/blobstore.py#L1150-L1159)
    
    
    writelines(
        sequence
    )
    

Raises an error if you attempt to write to the file.

Args  
---  
  
`sequence` |  The sequence of strings that you are attempting to write.   
  
Raises  
---  
  
`IOError` |  If you attempt to write lines to a file in `BlobReader`.   
  
### `__enter__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/blobstore/blobstore.py#L1181-L1187)
    
    
    __enter__()
    

Attempts to open the file.

Returns  
---  
The open file.   
  
### `__exit__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/blobstore/blobstore.py#L1189-L1191)
    
    
    __exit__(
        exc_type, exc_value, traceback
    )
    

Closes the file.

### `__iter__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/blobstore/blobstore.py#L899-L906)
    
    
    __iter__()
    

Retrieves a file iterator for this `BlobReader`.

Returns  
---  
The file iterator for the `BlobReader`.   
  
## Class Variables  
  
---  
  
SEEK_CUR |  `1`  
SEEK_END |  `2`  
SEEK_SET |  `0`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
