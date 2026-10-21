---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/ndb/QueryOptions/
title: google.appengine.ext.ndb.QueryOptions \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:11:52.048264+00:00
---

# google.appengine.ext.ndb.QueryOptions  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/ndb/QueryOptions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.ext.ndb.QueryOptions Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/query.py#L206-L207) Support both context options and query options (esp. use_cache). Inherits From: [`ContextOptions`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/ndb/ContextOptions), [`QueryOptions`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_query/QueryOptions), [`FetchOptions`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_query/FetchOptions), [`Configuration`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_rpc/Configuration), [`BaseConfiguration`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_rpc/BaseConfiguration), [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.ext.ndb.QueryOptions(
        config=None, **kwargs
    )
    

| 

## Args  
  
---  
  
`config` |  Optional base configuration providing default values for parameters not specified in the keyword arguments.   
`**kwargs` |  Configuration options to store on this object.   
  
## Methods

### `batch_size`
    
    
    batch_size(
        *args
    )
    

A descriptor for a Configuration option.

This class is used to create a configuration option on a class that inherits from BaseConfiguration. A validator function decorated with this class will be converted to a read-only descriptor and BaseConfiguration will implement constructor and merging logic for that configuration option. A validator function takes a single non-None value to validate and either throws an exception or returns that value (or an equivalent value). A validator is called once at construction time, but only if a non-None value for the configuration option is specified the constructor's keyword arguments.

### `deadline`
    
    
    deadline(
        *args
    )
    

A descriptor for a Configuration option.

This class is used to create a configuration option on a class that inherits from BaseConfiguration. A validator function decorated with this class will be converted to a read-only descriptor and BaseConfiguration will implement constructor and merging logic for that configuration option. A validator function takes a single non-None value to validate and either throws an exception or returns that value (or an equivalent value). A validator is called once at construction time, but only if a non-None value for the configuration option is specified the constructor's keyword arguments.

### `end_cursor`
    
    
    end_cursor(
        *args
    )
    

A descriptor for a Configuration option.

This class is used to create a configuration option on a class that inherits from BaseConfiguration. A validator function decorated with this class will be converted to a read-only descriptor and BaseConfiguration will implement constructor and merging logic for that configuration option. A validator function takes a single non-None value to validate and either throws an exception or returns that value (or an equivalent value). A validator is called once at construction time, but only if a non-None value for the configuration option is specified the constructor's keyword arguments.

### `force_writes`
    
    
    force_writes(
        *args
    )
    

A descriptor for a Configuration option.

This class is used to create a configuration option on a class that inherits from BaseConfiguration. A validator function decorated with this class will be converted to a read-only descriptor and BaseConfiguration will implement constructor and merging logic for that configuration option. A validator function takes a single non-None value to validate and either throws an exception or returns that value (or an equivalent value). A validator is called once at construction time, but only if a non-None value for the configuration option is specified the constructor's keyword arguments.

### `hint`
    
    
    hint(
        *args
    )
    

A descriptor for a Configuration option.

This class is used to create a configuration option on a class that inherits from BaseConfiguration. A validator function decorated with this class will be converted to a read-only descriptor and BaseConfiguration will implement constructor and merging logic for that configuration option. A validator function takes a single non-None value to validate and either throws an exception or returns that value (or an equivalent value). A validator is called once at construction time, but only if a non-None value for the configuration option is specified the constructor's keyword arguments.

### `is_configuration`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L449-L461)
    
    
    @classmethod
    is_configuration(
        obj
    )
    

True if configuration obj handles all options of this class.

Use this method rather than isinstance(obj, cls) to test if a configuration object handles the options of cls (is_configuration is handled specially for results of merge which may handle the options of unrelated configuration classes).

Args  
---  
  
`obj` |  the object to test.   
  
### `keys_only`
    
    
    keys_only(
        *args
    )
    

A descriptor for a Configuration option.

This class is used to create a configuration option on a class that inherits from BaseConfiguration. A validator function decorated with this class will be converted to a read-only descriptor and BaseConfiguration will implement constructor and merging logic for that configuration option. A validator function takes a single non-None value to validate and either throws an exception or returns that value (or an equivalent value). A validator is called once at construction time, but only if a non-None value for the configuration option is specified the constructor's keyword arguments.

### `limit`
    
    
    limit(
        *args
    )
    

A descriptor for a Configuration option.

This class is used to create a configuration option on a class that inherits from BaseConfiguration. A validator function decorated with this class will be converted to a read-only descriptor and BaseConfiguration will implement constructor and merging logic for that configuration option. A validator function takes a single non-None value to validate and either throws an exception or returns that value (or an equivalent value). A validator is called once at construction time, but only if a non-None value for the configuration option is specified the constructor's keyword arguments.

### `max_allocate_ids_keys`
    
    
    max_allocate_ids_keys(
        *args
    )
    

A descriptor for a Configuration option.

This class is used to create a configuration option on a class that inherits from BaseConfiguration. A validator function decorated with this class will be converted to a read-only descriptor and BaseConfiguration will implement constructor and merging logic for that configuration option. A validator function takes a single non-None value to validate and either throws an exception or returns that value (or an equivalent value). A validator is called once at construction time, but only if a non-None value for the configuration option is specified the constructor's keyword arguments.

### `max_delete_keys`
    
    
    max_delete_keys(
        *args
    )
    

A descriptor for a Configuration option.

This class is used to create a configuration option on a class that inherits from BaseConfiguration. A validator function decorated with this class will be converted to a read-only descriptor and BaseConfiguration will implement constructor and merging logic for that configuration option. A validator function takes a single non-None value to validate and either throws an exception or returns that value (or an equivalent value). A validator is called once at construction time, but only if a non-None value for the configuration option is specified the constructor's keyword arguments.

### `max_entity_groups_per_rpc`
    
    
    max_entity_groups_per_rpc(
        *args
    )
    

A descriptor for a Configuration option.

This class is used to create a configuration option on a class that inherits from BaseConfiguration. A validator function decorated with this class will be converted to a read-only descriptor and BaseConfiguration will implement constructor and merging logic for that configuration option. A validator function takes a single non-None value to validate and either throws an exception or returns that value (or an equivalent value). A validator is called once at construction time, but only if a non-None value for the configuration option is specified the constructor's keyword arguments.

### `max_get_keys`
    
    
    max_get_keys(
        *args
    )
    

A descriptor for a Configuration option.

This class is used to create a configuration option on a class that inherits from BaseConfiguration. A validator function decorated with this class will be converted to a read-only descriptor and BaseConfiguration will implement constructor and merging logic for that configuration option. A validator function takes a single non-None value to validate and either throws an exception or returns that value (or an equivalent value). A validator is called once at construction time, but only if a non-None value for the configuration option is specified the constructor's keyword arguments.

### `max_memcache_items`
    
    
    max_memcache_items(
        *args
    )
    

A descriptor for a Configuration option.

This class is used to create a configuration option on a class that inherits from BaseConfiguration. A validator function decorated with this class will be converted to a read-only descriptor and BaseConfiguration will implement constructor and merging logic for that configuration option. A validator function takes a single non-None value to validate and either throws an exception or returns that value (or an equivalent value). A validator is called once at construction time, but only if a non-None value for the configuration option is specified the constructor's keyword arguments.

### `max_put_entities`
    
    
    max_put_entities(
        *args
    )
    

A descriptor for a Configuration option.

This class is used to create a configuration option on a class that inherits from BaseConfiguration. A validator function decorated with this class will be converted to a read-only descriptor and BaseConfiguration will implement constructor and merging logic for that configuration option. A validator function takes a single non-None value to validate and either throws an exception or returns that value (or an equivalent value). A validator is called once at construction time, but only if a non-None value for the configuration option is specified the constructor's keyword arguments.

### `max_rpc_bytes`
    
    
    max_rpc_bytes(
        *args
    )
    

A descriptor for a Configuration option.

This class is used to create a configuration option on a class that inherits from BaseConfiguration. A validator function decorated with this class will be converted to a read-only descriptor and BaseConfiguration will implement constructor and merging logic for that configuration option. A validator function takes a single non-None value to validate and either throws an exception or returns that value (or an equivalent value). A validator is called once at construction time, but only if a non-None value for the configuration option is specified the constructor's keyword arguments.

### `memcache_deadline`
    
    
    memcache_deadline(
        *args
    )
    

A descriptor for a Configuration option.

This class is used to create a configuration option on a class that inherits from BaseConfiguration. A validator function decorated with this class will be converted to a read-only descriptor and BaseConfiguration will implement constructor and merging logic for that configuration option. A validator function takes a single non-None value to validate and either throws an exception or returns that value (or an equivalent value). A validator is called once at construction time, but only if a non-None value for the configuration option is specified the constructor's keyword arguments.

### `memcache_timeout`
    
    
    memcache_timeout(
        *args
    )
    

A descriptor for a Configuration option.

This class is used to create a configuration option on a class that inherits from BaseConfiguration. A validator function decorated with this class will be converted to a read-only descriptor and BaseConfiguration will implement constructor and merging logic for that configuration option. A validator function takes a single non-None value to validate and either throws an exception or returns that value (or an equivalent value). A validator is called once at construction time, but only if a non-None value for the configuration option is specified the constructor's keyword arguments.

### `merge`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L466-L518)
    
    
    merge(
        config
    )
    

Merge two configurations.

The configuration given as an argument (if any) takes priority; defaults are filled in from the current configuration.

Args  
---  
  
`config` |  Configuration providing overrides, or None (but cannot be omitted).   
  
Returns  
---  
Either a new configuration object or (if it would be equivalent) self or the config argument unchanged, but never None.   
  
Raises  
---  
BadArgumentError if self or config are of configurations classes with conflicting options (i.e. the same option name defined in two different configuration classes).   
  
### `offset`
    
    
    offset(
        *args
    )
    

A descriptor for a Configuration option.

This class is used to create a configuration option on a class that inherits from BaseConfiguration. A validator function decorated with this class will be converted to a read-only descriptor and BaseConfiguration will implement constructor and merging logic for that configuration option. A validator function takes a single non-None value to validate and either throws an exception or returns that value (or an equivalent value). A validator is called once at construction time, but only if a non-None value for the configuration option is specified the constructor's keyword arguments.

### `on_completion`
    
    
    on_completion(
        *args
    )
    

A descriptor for a Configuration option.

This class is used to create a configuration option on a class that inherits from BaseConfiguration. A validator function decorated with this class will be converted to a read-only descriptor and BaseConfiguration will implement constructor and merging logic for that configuration option. A validator function takes a single non-None value to validate and either throws an exception or returns that value (or an equivalent value). A validator is called once at construction time, but only if a non-None value for the configuration option is specified the constructor's keyword arguments.

### `prefetch_size`
    
    
    prefetch_size(
        *args
    )
    

A descriptor for a Configuration option.

This class is used to create a configuration option on a class that inherits from BaseConfiguration. A validator function decorated with this class will be converted to a read-only descriptor and BaseConfiguration will implement constructor and merging logic for that configuration option. A validator function takes a single non-None value to validate and either throws an exception or returns that value (or an equivalent value). A validator is called once at construction time, but only if a non-None value for the configuration option is specified the constructor's keyword arguments.

### `produce_cursors`
    
    
    produce_cursors(
        *args
    )
    

A descriptor for a Configuration option.

This class is used to create a configuration option on a class that inherits from BaseConfiguration. A validator function decorated with this class will be converted to a read-only descriptor and BaseConfiguration will implement constructor and merging logic for that configuration option. A validator function takes a single non-None value to validate and either throws an exception or returns that value (or an equivalent value). A validator is called once at construction time, but only if a non-None value for the configuration option is specified the constructor's keyword arguments.

### `projection`
    
    
    projection(
        *args
    )
    

A descriptor for a Configuration option.

This class is used to create a configuration option on a class that inherits from BaseConfiguration. A validator function decorated with this class will be converted to a read-only descriptor and BaseConfiguration will implement constructor and merging logic for that configuration option. A validator function takes a single non-None value to validate and either throws an exception or returns that value (or an equivalent value). A validator is called once at construction time, but only if a non-None value for the configuration option is specified the constructor's keyword arguments.

### `read_policy`
    
    
    read_policy(
        *args
    )
    

A descriptor for a Configuration option.

This class is used to create a configuration option on a class that inherits from BaseConfiguration. A validator function decorated with this class will be converted to a read-only descriptor and BaseConfiguration will implement constructor and merging logic for that configuration option. A validator function takes a single non-None value to validate and either throws an exception or returns that value (or an equivalent value). A validator is called once at construction time, but only if a non-None value for the configuration option is specified the constructor's keyword arguments.

### `start_cursor`
    
    
    start_cursor(
        *args
    )
    

A descriptor for a Configuration option.

This class is used to create a configuration option on a class that inherits from BaseConfiguration. A validator function decorated with this class will be converted to a read-only descriptor and BaseConfiguration will implement constructor and merging logic for that configuration option. A validator function takes a single non-None value to validate and either throws an exception or returns that value (or an equivalent value). A validator is called once at construction time, but only if a non-None value for the configuration option is specified the constructor's keyword arguments.

### `use_cache`
    
    
    use_cache(
        *args
    )
    

A descriptor for a Configuration option.

This class is used to create a configuration option on a class that inherits from BaseConfiguration. A validator function decorated with this class will be converted to a read-only descriptor and BaseConfiguration will implement constructor and merging logic for that configuration option. A validator function takes a single non-None value to validate and either throws an exception or returns that value (or an equivalent value). A validator is called once at construction time, but only if a non-None value for the configuration option is specified the constructor's keyword arguments.

### `use_datastore`
    
    
    use_datastore(
        *args
    )
    

A descriptor for a Configuration option.

This class is used to create a configuration option on a class that inherits from BaseConfiguration. A validator function decorated with this class will be converted to a read-only descriptor and BaseConfiguration will implement constructor and merging logic for that configuration option. A validator function takes a single non-None value to validate and either throws an exception or returns that value (or an equivalent value). A validator is called once at construction time, but only if a non-None value for the configuration option is specified the constructor's keyword arguments.

### `use_memcache`
    
    
    use_memcache(
        *args
    )
    

A descriptor for a Configuration option.

This class is used to create a configuration option on a class that inherits from BaseConfiguration. A validator function decorated with this class will be converted to a read-only descriptor and BaseConfiguration will implement constructor and merging logic for that configuration option. A validator function takes a single non-None value to validate and either throws an exception or returns that value (or an equivalent value). A validator is called once at construction time, but only if a non-None value for the configuration option is specified the constructor's keyword arguments.

### `__eq__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L398-L403)
    
    
    __eq__(
        other
    )
    

Return self==value.

### `__ne__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L405-L409)
    
    
    __ne__(
        other
    )
    

Return self!=value.

## Class Variables  
  
---  
  
ALL_READ_POLICIES | 
    
    
    {
     0,
     1,
     2
    }
      
  
ANCESTOR_FIRST |  `2`  
APPLY_ALL_JOBS_CONSISTENCY |  `2`  
EVENTUAL_CONSISTENCY |  `1`  
FILTER_FIRST |  `3`  
ORDER_FIRST |  `1`  
STRONG_CONSISTENCY |  `0`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
