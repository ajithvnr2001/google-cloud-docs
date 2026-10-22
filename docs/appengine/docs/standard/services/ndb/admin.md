---
url: https://docs.cloud.google.com/appengine/docs/standard/services/ndb/admin/
title: NDB Administration \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:48.381613+00:00
---

# NDB Administration  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/ndb/admin/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  NDB Administration Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

There are tools and APIs to make it easier to administer an application's stored data.

## Google Cloud console

When using the [Google Cloud console](https://console.cloud.google.com/), remember that NDB is implemented by means of Datastore _and_ memcache. When NDB "reads" a value, it checks memcache first; it only reads from Datastore if it doesn't find the value in memcache.

Thus, if you use the Google Cloud console to edit an entity in Datastore, the application might still use the "old" value if that value is in memcache. You might work around this by purging memcache. This is rather disruptive, however; if you need to tweak values "by hand" often, you might want to set up a UI for this in your application that writes values via the NDB client library; writing via NDB keeps Datastore and memcache in sync.

## Metadata queries

NDB supports a metadata query API. This allows an application to get some general information about its use of Datastore. This API is in the [`google.appengine.ext.ndb.metadata`](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/metadata) module. It has functions:

  * `get_namespaces(start=None, end=None)`: return a list of namespace names
  * `get_kinds(start=None, end=None)`: return a list of kind names
  * `get_properties_of_kind(kind, start=None, end=None)`: return a list of property names for the given _kind_ name
  * `get_representations_of_kind(kind, start=None, end=None)`: return a dict mapping property names for the given kind name to lists of representation names such as `STRING`, `BOOLEAN` or `INT64`.



These functions have optional _start_ and _end_ arguments that can be used to restrict the query to a certain range. Here, _start_ is inclusive and _end_ is exclusive. Both default to `None`. For example, to get all namespaces starting with a lowercase letter you could call `get_namespaces('a', chr(ord('z') + 1))`. All of these except `get_namespaces()` are implicitly restricted to the current namespace. Metadata gets and queries are [billed in the same way as Datastore gets and queries](https://docs.cloud.google.com/appengine/docs/pricing).

## Statistics queries

Datastore maintains statistics about the data stored for an application, such as how many entities there are of a given kind, or how much space is used by property values of a given type. You can view these statistics in the Google Cloud console, in the [Dashboard](https://console.cloud.google.com/datastore/stats) page.

You can also access these values programmatically within the application by querying for specially named entities using the Datastore API. Each statistic is accessible as an entity whose kind name begins and ends with two underscores. For example, each app has exactly one entity of the kind `__Stat_Total__` that represents statistics about all of the entities in Datastore in total. Each statistic entity has the following properties:

  * `count`, the number of items considered by the statistic (a long integer)
  * `bytes`, the total size of the items for this statistic (a long integer)
  * `timestamp`, the time of the most recent update to the statistic (a date-time value)



Some statistic kinds also have additional properties, listed below.

An application can use model classes provided by the package `google.appengine.ext.ndb.stats` to access statistic entities.
    
    
    from google.appengine.ext.ndb import stats
    
    global_stat = stats.GlobalStat.query().get()
    print 'Total bytes stored: %d' % global_stat.bytes
    print 'Total entities stored: %d' % global_stat.count
    

When the statistics system creates new statistic entities, it does not delete the old ones right away. The best way to get a consistent view of the statistics is to query for the `GlobalStat` entity with the most recent `timestamp`, then use that timestamp value as a filter when fetching other statistic entities.

The statistic entities are included in the calculated statistic values. Statistic entities take up space relative to the number of unique kinds and property names used by the application.

The statistics system will also create statistics specific to each [namespace](https://docs.cloud.google.com/appengine/docs/standard/services/multitenancy/multitenancy). Note that if an application does not use Datastore namespaces then namespace specific statistics will not be created. Namespace specific stats are found in the namespace that they're specific to. The kind names for namespace specific stats are prefixed with `__Stat_Ns_` and have the same corresponding suffix as application wide statistics kinds.

Applications with thousands of namespaces, kinds, or property names require a very large number of statistics entities. To keep the overhead of storing and updating the statistics reasonable, Datastore progressively drops statistics entities, in the following order:

  * per-namespace, per-kind, and per-property statistics: `__Stat_Ns_PropertyName_Kind__`, `__Stat_Ns_PropertyType_PropertyName_Kind__`
  * per-kind and per-property statistics: `__Stat_PropertyName_Kind__`, `__Stat_PropertyType_PropertyName_Kind__`
  * per-namespace and per-kind statistics: `__Stat_Ns_Kind__`, `__Stat_Ns_Kind_IsRootEntity__`, `__Stat_Ns_Kind_NotRootEntity__`, `__Stat_Ns_PropertyType_Kind__`
  * per-kind statistics: `__Stat_Kind__`, `__Stat_Kind_IsRootEntity__`, `__Stat_Kind_NotRootEntity__`, `__Stat_PropertyType_Kind__`
  * per-namespace statistics: `__Stat_Namespace__`, `__Stat_Ns_Kind_CompositeIndex__`, `__Stat_Ns_PropertyType__`, `__Stat_Ns_Total__`



The summary statistics entities (`__Stat_Kind_CompositeIndex__`, `__Stat_PropertyType__`, `__Stat_Total__`) are never dropped.

The complete list of available statistics is as follows:

Statistic | Stat Entity Kind | Description  
---|---|---  
all entities | `__Stat_Total__`   
Namespace specific entry:  
`__Stat_Ns_Total__` | All entities. Additional properties:  
  
• `entity_bytes`: The storage in the entities table measured in bytes.  
• `builtin_index_bytes`: The storage in built-in index entries measured in bytes.  
• `builtin_index_count`: the count of built-in index entries.  
• `composite_index_bytes`: The storage in composite index entries measured in bytes.  
• `composite_index_count`: The count of composite index entries.  
all entities in a namespace | `__Stat_Namespace__`   
Note that `__Stat_Namespace__` entities are created for each namespace encountered and are only found in the empty string namespace. | All entities in a namespace.  
  
• `subject_namespace`, the namespace represented (a string)  
• `entity_bytes`: The storage in the entities table measured in bytes.  
• `builtin_index_bytes`: The storage in built-in index entries measured in bytes.  
• `builtin_index_count`: the count of built-in index entries.  
• `composite_index_bytes`: The storage in composite index entries measured in bytes.  
• `composite_index_count`: The count of composite index entries.  
all entries in application defined indexes | `__Stat_Kind_CompositeIndex__`  
Namespace specific entry: `__Stat_Ns_Kind_CompositeIndex__`  
| Information about the composite indexes in the database; one stat entity for each composite index. Additional properties:  
  
• `index_id`, the index id.  
• `kind_name`, the name of the kind represented (a string)  
entities of a kind | `__Stat_Kind__`   
Namespace specific entry:  
`__Stat_Ns_Kind__` | Entities of a kind; one stat entity for each kind of entity stored. Additional properties:  
  
• `kind_name`, the name of the kind represented (a string)  
• `entity_bytes`: The storage in the entities table measured in bytes.  
• `builtin_index_bytes`: The storage in built-in index entries measured in bytes.  
• `builtin_index_count`: the count of built-in index entries.  
• `composite_index_bytes`: The storage in composite index entries measured in bytes.  
• `composite_index_count`: The count of composite index entries.  
root entities of a kind | `__Stat_Kind_IsRootEntity__`   
Namespace specific entry:  
`__Stat_Ns_Kind_IsRootEntity__` | Entities of a kind that are entity group root entities (have no ancestor parent); one stat entity for each kind of entity stored. Additional properties:  
  
• `kind_name`, the name of the kind represented (a string)  
• `entity_bytes`: The storage in the entities table measured in bytes.  
non-root entities of a kind | `__Stat_Kind_NotRootEntity__`   
Namespace specific entry:  
`__Stat_Ns_Kind_NotRootEntity__` | Entities of a kind that are not entity group root entities (have an ancestor parent); one stat entity for each kind of entity stored. Additional properties:  
  
• `kind_name`, the name of the kind represented (a string)  
• `entity_bytes`: The storage in the entities table measured in bytes.  
properties of a type | `__Stat_PropertyType__`   
Namespace specific entry:  
`__Stat_Ns_PropertyType__` | Properties of a value type across all entities; one stat entity per value type. Additional properties:  
  
• `property_type`, the name of the value type (a string)  
• `entity_bytes`: The storage in the entities table measured in bytes.  
• `builtin_index_bytes`: The storage in built-in index entries measured in bytes.  
• `builtin_index_count`: the count of built-in index entries.  
properties of a type per kind | `__Stat_PropertyType_Kind__`   
Namespace specific entry:  
`__Stat_Ns_PropertyType_Kind__` | Properties of a value type across entities of a given kind; one stat entity per combination of property type and kind. Additional properties:  
  
• `property_type`, the name of the value type (a string)  
• `kind_name`, the name of the kind represented (a string)  
• `entity_bytes`: The storage in the entities table measured in bytes.  
• `builtin_index_bytes`: The storage in the built-in index measured in bytes.  
• `builtin_index_count`: the count of built-in index entries.  
properties with a name | `__Stat_PropertyName_Kind__`   
Namespace specific entry:  
`__Stat_Ns_PropertyName_Kind__` | Properties with a given name across entities of a given kind; one stat entity per combination of unique property name and kind. Additional properties:  
  
• `property_name`, the name of the property (a string)  
• `kind_name`, the name of the kind represented (a string)  
• `entity_bytes`: The storage in the entities table measured in bytes.  
• `builtin_index_bytes`: The storage in built-in index entries measured in bytes.  
• `builtin_index_count`: the count of built-in index entries.  
properties of a type and with a name | `__Stat_PropertyType_PropertyName_Kind__`   
Namespace specific entry:  
`__Stat_Ns_PropertyType_PropertyName_Kind__` | Properties with a given name and of a given value type across entities of a given kind; one stat entity per combination of property name, value type and kind that exists in Datastore. Additional properties:  
  
• `property_type`, the name of the value type (a string)  
• `property_name`, the name of the property (a string)  
• `kind_name`, the name of the kind represented (a string)  
• `entity_bytes`: The storage in the entities table measured in bytes.  
• `builtin_index_bytes`: The storage in built-in index entries measured in bytes.  
• `builtin_index_count`: the count of built-in index entries.  
  
Some statistics refer to Datastore property value types by name, as strings. These names are as follows:

  * `"Blob"`
  * `"BlobKey"`
  * `"Boolean"`
  * `"Category"`
  * `"Date/Time"`
  * `"Email"`
  * `"Float"`
  * `"GeoPt"`
  * `"IM"`
  * `"Integer"`
  * `"Key"`
  * `"Link"`
  * `"NULL"`
  * `"PhoneNumber"`
  * `"PostalAddress"`
  * `"Rating"`
  * `"ShortBlob"`
  * `"String"`
  * `"Text"`
  * `"User"`

**Note:** `__Stat_Namespace__` entities contain the same information found in `__Stat_Ns_Total__` records. `__Stat_Namespace__` entities are stored in the empty namespace and contain a `subject_namespace` field describing the namespace to which they belong. `__Stat_Ns_Total__` records are stored in the namespace to which they refer, and thus do not contain a `subject_namespace` field. Hence, a query on kind `__Stat_Namespace__` (from the empty string namespace) ordered descending by `bytes` will list the namespaces that consume the largest storage first. Because queries across namespaces are not possible, any query for `__Stat_Ns_Total__` entities will only ever produce at most a single record.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
