---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_index/CompositeIndexForQuery/
title: google.appengine.datastore.datastore_index.CompositeIndexForQuery \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:52:22.596212+00:00
---

# google.appengine.datastore.datastore_index.CompositeIndexForQuery  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_index/CompositeIndexForQuery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.datastore.datastore_index.CompositeIndexForQuery Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_index.py#L552-L733) Returns the composite index needed for a query.
    
    
    google.appengine.datastore.datastore_index.CompositeIndexForQuery(
        query
    )
    

A query is translated into a tuple, as follows:

  * The first item is the kind string, or `None` if we're not filtering on kind (see below).
  * The second item is a bool giving whether the query specifies an ancestor.
  * After that come `(property, ASCENDING)` pairs for those Filter entries whose operator is `EQUAL` or `IN`. Since the order of these doesn't matter, they are sorted by property name to normalize them in order to avoid duplicates.
  * After that comes at most one `(property, ASCENDING)` pair for a Filter entry whose operator is on of the four inequalities. There can be at most one of these.
  * After that come all the `(property, direction)` pairs for the Order entries, in the order given in the query. Exceptions:
    * (a) If there is a Filter entry with an inequality operator that matches the first Order entry, the first order pair is omitted (or, equivalently, in this case the inequality pair is omitted).
    * (b) If an Order entry corresponds to an equality filter, it is ignored (since there will only ever be one value returned).
    * (c) If there is an equality filter on `__key__` all orders are dropped (since there will be at most one result returned).
    * (d) If there is an order on `__key__` all further orders are dropped (since keys are unique).
    * (e) Orders on `__key__` `ASCENDING` are dropped (since this is supported natively by the datastore).
  * Finally, if there are Filter entries whose operator is `EXISTS`, and whose property names are not already listed, they are added, with the direction set to `ASCENDING`.

This algorithm should consume all Filter and Order entries.

#### Additional notes:

  * The low-level implementation allows queries that don't specify a kind; but the Python `API` doesn't support this yet.
  * If there's an inequality filter and one or more sort orders, the first sort order _must_ match the inequality filter.
  * The following indexes are always built in and should be suppressed:
    * Query on kind only;
    * Query on kind and one filter _or_ one order;
    * Query on ancestor only, without kind (not exposed in Python yet);
    * Query on kind and equality filters only, no order (with or without ancestor).
  * While the protocol buffer allows a Filter to contain multiple properties, we don't use this. It is only needed for the `IN` operator but this is (currently) handled on the client side, so in practice each Filter is expected to have exactly one property.

| 

## Args  
  
---  
  
`query` |  A `datastore_pb.Query` instance.   
  
## Returns  
  
---  
A tuple of the form `(required, kind, ancestor, properties)`. `required`: Boolean, whether the index is required; `kind`: The kind or None; `ancestor`: True if this is an ancestor query; `properties`: A tuple consisting of: 

  * The prefix, represented by a set of property names.
  * The postfix, represented by a tuple consisting of any number of: 
    * Sets of property names or `PropertySpec` objects: these properties can appear in any order.
    * Sequences of `PropertySpec` objects: Indicates the properties must appear in the given order, with the specified direction (if specified in the `PropertySpec`). 

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
