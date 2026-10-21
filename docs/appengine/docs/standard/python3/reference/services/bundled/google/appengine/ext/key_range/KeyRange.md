---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/key_range/KeyRange/
title: google.appengine.ext.key_range.KeyRange \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:21:17.818226+00:00
---

# google.appengine.ext.key_range.KeyRange  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/key_range/KeyRange/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.ext.key_range.KeyRange Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/key_range/__init__.py#L51-L882) Represents a range of keys in the datastore. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.ext.key_range.KeyRange(
        key_start=None,
        key_end=None,
        direction=None,
        include_start=True,
        include_end=True,
        namespace=None,
        _app=None
    )
    

A KeyRange object represents a key range (key_start, include_start, key_end, include_end) and a scan direction (KeyRange.DESC or KeyRange.ASC). | 

## Args  
  
---  
  
`key_start` |  The starting key for this range (db.Key or ndb.Key).   
`key_end` |  The ending key for this range (db.Key or ndb.Key).   
`direction` |  The direction of the query for this range.   
`include_start` |  Whether the start key should be included in the range.   
`include_end` |  Whether the end key should be included in the range.   
`namespace` |  The namespace for this range. If None then the current namespace is used.   
  
## Methods

### `advance`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/key_range/__init__.py#L133-L143)
    
    
    advance(
        key
    )
    

Updates the start of the range immediately past the specified key.

Args  
---  
  
`key` |  A db.Key or ndb.Key.   
  
### `bisect_string_range`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/key_range/__init__.py#L520-L577)
    
    
    @staticmethod
    bisect_string_range(
        start, end
    )
    

Returns a string that is approximately in the middle of the range.

(start, end) is treated as a string range, and it is assumed start <= end in the usual lexicographic string ordering. The output key mid is guaranteed to satisfy start <= mid <= end.

The method proceeds by comparing initial characters of start and end. When the characters are equal, they are appended to the mid string. In the first place that the characters differ, the difference characters are averaged and this average is appended to the mid string. If averaging resulted in rounding down, and additional character is added to the mid string to make up for the rounding down. This extra step is necessary for correctness in the case that the average of the two characters is equal to the character in the start string.

This method makes the assumption that most keys are ascii and it attempts to perform splitting within the ascii range when that results in a valid split.

Args  
---  
  
`start` |  A string.   
`end` |  A string such that start <= end.   
  
Returns  
---  
A string mid such that start <= mid <= end.   
  
### `compute_split_points`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/key_range/__init__.py#L778-L829)
    
    
    @classmethod
    compute_split_points(
        kind, count
    )
    

Computes a set of KeyRanges that are split points for a kind.

Args  
---  
  
`kind` |  String with the entity kind to split.   
`count` |  Number of non-overlapping KeyRanges to generate.   
  
Returns  
---  
A list of KeyRange objects that are non-overlapping. At most "count" + 1 KeyRange objects will be returned. At least one will be returned.   
  
### `filter_datastore_query`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/key_range/__init__.py#L218-L248)
    
    
    filter_datastore_query(
        query, filters=None
    )
    

Add query filter to restrict to this key range.

Args  
---  
  
`query` |  A datastore.Query instance.   
`filters` |  optional list of filters to apply to the query. Each filter is a tuple: (, , ). User filters are applied first.   
  
Returns  
---  
The input query restricted to this key range.   
  
### `filter_ndb_query`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/key_range/__init__.py#L181-L216)
    
    
    filter_ndb_query(
        query, filters=None
    )
    

Add query filter to restrict to this key range.

Args  
---  
  
`query` |  An ndb.Query instance.   
`filters` |  optional list of filters to apply to the query. Each filter is a tuple: (, , ). User filters are applied first.   
  
Returns  
---  
The input query restricted to this key range.   
  
### `filter_query`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/key_range/__init__.py#L145-L179)
    
    
    filter_query(
        query, filters=None
    )
    

Add query filter to restrict to this key range.

Args  
---  
  
`query` |  A db.Query or ndb.Query instance.   
`filters` |  optional list of filters to apply to the query. Each filter is a tuple: (, , ). User filters are applied first.   
  
Returns  
---  
The input query restricted to this key range.   
  
### `from_json`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/key_range/__init__.py#L858-L882)
    
    
    @staticmethod
    from_json(
        json_str
    )
    

Deserialize KeyRange from its json representation.

Args  
---  
  
`json_str` |  string with json representation created by key_range_to_json.   
  
Returns  
---  
deserialized KeyRange instance.   
  
### `guess_end_key`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/key_range/__init__.py#L691-L776)
    
    
    @staticmethod
    guess_end_key(
        kind, key_start, probe_count=30, split_rate=5
    )
    

Guess the end of a key range with a binary search of probe queries.

When the 'key_start' parameter has a key hierarchy, this function will only determine the key range for keys in a similar hierarchy. That means if the keys are in the form:

kind=Foo, name=bar/kind=Stuff, name=meep

only this range will be probed:

kind=Foo, name=_/kind=Stuff, name=_

That means other entities of kind 'Stuff' that are children of another parent entity kind will be skipped:

kind=Other, name=cookie/kind=Stuff, name=meep

Args  
---  
  
`key_start` |  The starting key of the search range. In most cases this should be id = 0 or name = ''. May be db.Key or ndb.Key.   
`kind` |  String name of the entity kind.   
`probe_count` |  Optional, how many probe queries to run.   
`split_rate` |  Exponential rate to use for splitting the range on the way down from the full key space. For smaller ranges this should be higher so more of the keyspace is skipped on initial descent.   
  
Returns  
---  
db.Key that is guaranteed to be as high or higher than the highest key existing for this Kind. Doing a query between 'key_start' and this returned Key (inclusive) will contain all entities of this Kind.   
  
NOTE: Even though an ndb.Key instance is accepted as argument, the return value is always a db.Key instance.

### `make_ascending_datastore_query`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/key_range/__init__.py#L391-L411)
    
    
    make_ascending_datastore_query(
        kind, keys_only=False, filters=None
    )
    

Construct a query for this key range without setting the scan direction.

Args  
---  
  
`kind` |  A string.   
`keys_only` |  bool, default False, use keys_only on Query?   
`filters` |  optional list of filters to apply to the query. Each filter is a tuple: (, , ). User filters are applied first.   
  
Returns  
---  
A datastore.Query instance.   
  
### `make_ascending_ndb_query`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/key_range/__init__.py#L369-L389)
    
    
    make_ascending_ndb_query(
        kind_class, keys_only=False, filters=None
    )
    

Construct an NDB query for this key range, without the scan direction.

Args  
---  
  
`kind_class` |  An ndb.Model subclass.   
`keys_only` |  bool, default False, query only for keys.   
  
Returns  
---  
An ndb.Query instance.   
  
### `make_ascending_query`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/key_range/__init__.py#L344-L367)
    
    
    make_ascending_query(
        kind_class, keys_only=False, filters=None
    )
    

Construct a query for this key range without setting the scan direction.

Args  
---  
  
`kind_class` |  A kind implementation class (a subclass of either db.Model or ndb.Model).   
`keys_only` |  bool, default False, query only for keys.   
`filters` |  optional list of filters to apply to the query. Each filter is a tuple: (, , ). User filters are applied first.   
  
Returns  
---  
A db.Query or ndb.Query instance (corresponding to kind_class).   
  
### `make_directed_datastore_query`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/key_range/__init__.py#L323-L342)
    
    
    make_directed_datastore_query(
        kind, keys_only=False
    )
    

Construct a query for this key range, including the scan direction.

Args  
---  
  
`kind` |  A string.   
`keys_only` |  bool, default False, use keys_only on Query?   
  
Returns  
---  
A datastore.Query instance.   
  
Raises  
---  
  
`KeyRangeError` |  if self.direction is not in (KeyRange.ASC, KeyRange.DESC).   
  
### `make_directed_ndb_query`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/key_range/__init__.py#L295-L321)
    
    
    make_directed_ndb_query(
        kind_class, keys_only=False
    )
    

Construct an NDB query for this key range, including the scan direction.

Args  
---  
  
`kind_class` |  An ndb.Model subclass.   
`keys_only` |  bool, default False, use keys_only on Query?   
  
Returns  
---  
An ndb.Query instance.   
  
Raises  
---  
  
`KeyRangeError` |  if self.direction is not in (KeyRange.ASC, KeyRange.DESC).   
  
### `make_directed_query`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/key_range/__init__.py#L270-L293)
    
    
    make_directed_query(
        kind_class, keys_only=False
    )
    

Construct a query for this key range, including the scan direction.

Args  
---  
  
`kind_class` |  A kind implementation class (a subclass of either db.Model or ndb.Model).   
`keys_only` |  bool, default False, use keys_only on Query?   
  
Returns  
---  
A db.Query or ndb.Query instance (corresponding to kind_class).   
  
Raises  
---  
  
`KeyRangeError` |  if self.direction is not in (KeyRange.ASC, KeyRange.DESC).   
  
### `split_keys`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/key_range/__init__.py#L579-L651)
    
    
    @staticmethod
    split_keys(
        key_start, key_end, batch_size
    )
    

Return a key that is between key_start and key_end inclusive.

This method compares components of the ancestor paths of key_start and key_end. The first place in the path that differs is approximately split in half. If the kind components differ, a new non-existent kind halfway between the two is used to split the space. If the id_or_name components differ, then a new id_or_name that is halfway between the two is selected. If the lower id_or_name is numeric and the upper id_or_name is a string, then the minumum string key u'' is used as the split id_or_name. The key that is returned is the shared portion of the ancestor path followed by the generated split component.

Args  
---  
  
`key_start` |  A db.Key or ndb.Key instance for the lower end of a range.   
`key_end` |  A db.Key or ndb.Key instance for the upper end of a range.   
`batch_size` |  The maximum size of a range that should not be split.   
  
Returns  
---  
A db.Key instance, k, such that key_start <= k <= key_end.   
  
NOTE: Even though ndb.Key instances are accepted as arguments, the return value is always a db.Key instance.

### `split_range`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/key_range/__init__.py#L413-L473)
    
    
    split_range(
        batch_size=0
    )
    

Split this key range into a list of at most two ranges.

This method attempts to split the key range approximately in half. Numeric ranges are split in the middle into two equal ranges and string ranges are split lexicographically in the middle. If the key range is smaller than batch_size it is left unsplit.

Note that splitting is done without knowledge of the distribution of actual entities in the key range, so there is no guarantee (nor any particular reason to believe) that the entities of the range are evenly split.

Args  
---  
  
`batch_size` |  The maximum size of a key range that should not be split.   
  
Returns  
---  
A list of one or two key ranges covering the same space as this range.   
  
### `to_json`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/key_range/__init__.py#L831-L855)
    
    
    to_json()
    

Serialize KeyRange to json.

Returns  
---  
string with KeyRange json representation.   
  
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
    

Return self!=value.

## Class Variables  
  
---  
  
ASC |  `'ASC'`  
DESC |  `'DESC'`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
