---
url: https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.KeyRange
title: Class KeyRange (3.71.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:39:37.000309+00:00
---

# Class KeyRange (3.71.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.KeyRange

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class KeyRange (3.71.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.71.0 (latest)  3.70.0  3.69.1  3.68.0  3.67.0  3.66.0  3.65.0  3.64.0  3.63.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.51.0  3.50.1  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.1  3.39.0  3.38.0  3.37.0  3.36.0  3.35.1  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.1  3.26.0  3.25.0  3.24.0  3.23.0  3.22.2  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.1  3.14.1  3.13.0  3.12.1  3.11.1  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.1.1  2.0.0  1.19.3  1.18.0  1.17.1  1.16.0  1.15.1  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0 
    
    
    KeyRange(mapping=None, *, ignore_unknown_fields=False, **kwargs)

KeyRange represents a range of rows in a table or index.

A range has a start key and an end key. These keys can be open or closed, indicating if the range includes rows with that key.

Keys are represented by lists, where the ith value in the list corresponds to the ith component of the table or index primary key. Individual values are encoded as described `here][google.spanner.v1.TypeCode]`.

For example, consider the following table definition:

::
    
    
    CREATE TABLE UserEvents (
      UserName STRING(MAX),
      EventDate STRING(10)
    ) PRIMARY KEY(UserName, EventDate);
    

The following keys name rows in this table:

::
    
    
    ["Bob", "2014-09-23"]
    ["Alfred", "2015-06-12"]
    

Since the `UserEvents` table's `PRIMARY KEY` clause names two columns, each `UserEvents` key has two elements; the first is the `UserName`, and the second is the `EventDate`.

Key ranges with multiple components are interpreted lexicographically by component using the table or index key's declared sort order. For example, the following range returns all events for user `"Bob"` that occurred in the year 2015:

::
    
    
    "start_closed": ["Bob", "2015-01-01"]
    "end_closed": ["Bob", "2015-12-31"]
    

Start and end keys can omit trailing key components. This affects the inclusion and exclusion of rows that exactly match the provided key components: if the key is closed, then rows that exactly match the provided components are included; if the key is open, then rows that exactly match are not included.

For example, the following range includes all events for `"Bob"` that occurred during and after the year 2000:

::
    
    
    "start_closed": ["Bob", "2000-01-01"]
    "end_closed": ["Bob"]
    

The next example retrieves all events for `"Bob"`:

::
    
    
    "start_closed": ["Bob"]
    "end_closed": ["Bob"]
    

To retrieve events before the year 2000:

::
    
    
    "start_closed": ["Bob"]
    "end_open": ["Bob", "2000-01-01"]
    

The following range includes all rows in the table:

::
    
    
    "start_closed": []
    "end_closed": []
    

This range returns all users whose `UserName` begins with any character from A to C:

::
    
    
    "start_closed": ["A"]
    "end_open": ["D"]
    

This range returns all users whose `UserName` begins with B:

::
    
    
    "start_closed": ["B"]
    "end_open": ["C"]
    

Key ranges honor column sort order. For example, suppose a table is defined as follows:

::
    
    
    CREATE TABLE DescendingSortedTable {
      Key INT64,
      ...
    ) PRIMARY KEY(Key DESC);
    

The following range retrieves all rows with key values between 1 and 100 inclusive:

::
    
    
    "start_closed": ["100"]
    "end_closed": ["1"]
    

Note that 100 is passed as the start, and 1 is passed as the end, because `Key` is a descending column in the schema.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`start_closed` |  `google.protobuf.struct_pb2.ListValue`   
If the start is closed, then the range includes all rows whose first `len(start_closed)` key columns exactly match `start_closed`. This field is a member of `oneof`_ `start_key_type`.   
`start_open` |  `google.protobuf.struct_pb2.ListValue`   
If the start is open, then the range excludes rows whose first `len(start_open)` key columns exactly match `start_open`. This field is a member of `oneof`_ `start_key_type`.   
`end_closed` |  `google.protobuf.struct_pb2.ListValue`   
If the end is closed, then the range includes all rows whose first `len(end_closed)` key columns exactly match `end_closed`. This field is a member of `oneof`_ `end_key_type`.   
`end_open` |  `google.protobuf.struct_pb2.ListValue`   
If the end is open, then the range excludes rows whose first `len(end_open)` key columns exactly match `end_open`. This field is a member of `oneof`_ `end_key_type`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
