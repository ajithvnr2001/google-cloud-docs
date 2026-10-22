---
url: https://docs.cloud.google.com/appengine/docs/standard/services/ndb/metadata/
title: NDB Metadata Reference \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:43:53.586767+00:00
---

# NDB Metadata Reference  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/ndb/metadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  NDB Metadata Reference Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

This API is in the `google.appengine.ext.ndb.metadata` module, typically used via `from google.appengine.ext.ndb import metadata`. 

## Functions

get_entity_group_version(key) 
    Return the version of the entity group containing key. This version is guaranteed to increase on every change to the entity group. The version may increase even in the absence of user-visible changes to the entity group. May return `None` if the entity group was never written to. 

**Warning** : The behavior of entity group metadata is now different. The entity group version can increase independently of user updates. Previously, the entity group version increased only on user update. To maintain legacy behavior, use the [entity group version workaround](https://support.google.com/cloud/answer/9133787#zippy=python-ndb). 

**Arguments**

key
    key for an entity group. 
get_namespaces(start=None, end=None) 
    Returns a list of namespace names. 

**Arguments**

start
    Don't return namespace names before this in alphabetical order. 
end
    Don't return namespace names after this in alphabetical order. 
get_kinds(start=None, end=None): 
    Returns a list of kind names in the current namespace. 

**Arguments**

start
    Don't return kind names before this in alphabetical order. 
end
    Don't return kind names after this in alphabetical order. 
get_properties_of_kind(kind, start=None, end=None): 
    Returns a list of property names for the given kind name in the current namespace. 

**Arguments**

kind
    Which kind's properties to list. 
start
    Don't return property names before this in alphabetical order. 
end
    Don't return property names after this in alphabetical order. 
get_representations_of_kind(kind, start=None, end=None) 
    Returns a `dict` mapping property names for the given kind name to lists of representation names such as 'STRING', 'BOOLEAN' or 'INT64'. Only looks in the current namespace. For a complete list of these types, see Representation Types     Returns a list of property names for the given kind name. 

**Arguments**

kind
    Which kind's properties to list. 
start
    Don't return property names before this in alphabetical order. 
end
    Don't return property names after this in alphabetical order. 

## Representation Types

Property Class  |  Representation   
---|---  
StringProperty  |  STRING   
BooleanProperty  |  BOOLEAN   
IntegerProperty  |  INT64   
FloatProperty  |  DOUBLE   
DateTimeProperty  
DateProperty  
TimeProperty  |  INT64   
UserProperty  |  USER   
BlobProperty  |  STRING   
BlobKeyProperty  |  STRING   
TextProperty  |  STRING   
GeoPtProperty  |  POINT   
GenericProperty  |  (Depends on what value is stored.)   
ComputedProperty  |  (Depends on what value is stored.)   
JsonProperty  |  STRING   
PickleProperty  |  STRING   
StructuredProperty  |  (When you get representation types, `StructuredProperty` properties won't be returned. Instead, it shows values for the subproperties corresponding to _their_ property types.)   
LocalStructuredProperty  |  STRING   
KeyProperty  |  REFERENCE   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
