---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_rpc/BaseConfiguration/
title: google.appengine.datastore.datastore_rpc.BaseConfiguration \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T10:52:48.742667+00:00
---

# google.appengine.datastore.datastore_rpc.BaseConfiguration  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_rpc/BaseConfiguration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.datastore.datastore_rpc.BaseConfiguration Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L331-L527) A base class for a configuration object. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.datastore.datastore_rpc.BaseConfiguration(
        config=None, **kwargs
    )
    

Subclasses should provide validation functions for every configuration option they accept. Any public function decorated with ConfigOption is assumed to be a validation function for an option of the same name. All validation functions take a single non-None value to validate and must throw an exception or return the value to store. This class forces subclasses to be immutable and exposes a read-only property for every accepted configuration option. Configuration options set by passing keyword arguments to the constructor. The constructor and merge function are designed to avoid creating redundant copies and may return the configuration objects passed to them if appropriate. Setting an option to None is the same as not specifying the option except in the case where the 'config' argument is given. In this case the value on 'config' of the same name is ignored. Options that are not specified will return 'None' when accessed. | 

## Args  
  
---  
  
`config` |  Optional base configuration providing default values for parameters not specified in the keyword arguments.   
`**kwargs` |  Configuration options to store on this object.   
  
## Methods

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

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
