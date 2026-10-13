---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.GqlQueryOrBuilder
title: Interface GqlQueryOrBuilder (3.7.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:20:21.560506+00:00
---

# Interface GqlQueryOrBuilder (3.7.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.GqlQueryOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface GqlQueryOrBuilder (3.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.7.0 (latest)  3.3.0  3.2.0  3.1.0  2.40.0  2.37.0  2.36.0  2.34.0  2.33.3  2.32.3  2.31.4  2.30.0  2.29.1  2.28.2  2.27.1  2.26.4  2.25.2  2.24.3  2.23.0  2.22.0  2.21.3  2.20.2  2.19.2  2.18.5  2.17.6 
    
    
    public interface GqlQueryOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsNamedBindings(String key)
    
    
    public abstract boolean containsNamedBindings(String key)

For each non-reserved named binding site in the query string, there must be a named parameter with that name, but not necessarily the inverse.

Key must match regex `A-Za-z_$__`, must not match regex`__.__`, and must not be `""`.

`map<string, .google.datastore.v1.GqlQueryParameter> named_bindings = 5;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAllowLiterals()
    
    
    public abstract boolean getAllowLiterals()

When false, the query string must not contain any literals and instead must bind all values. For example, `SELECT * FROM Kind WHERE a = 'string literal'` is not allowed, while `SELECT * FROM Kind WHERE a = @value` is.

`bool allow_literals = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The allowLiterals.  
  
### getNamedBindings() (deprecated)
    
    
    public abstract Map<String,GqlQueryParameter> getNamedBindings()

Use [#getNamedBindingsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.GqlQueryOrBuilder#com_google_datastore_v1_GqlQueryOrBuilder_getNamedBindingsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[GqlQueryParameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.GqlQueryParameter)>` |   
  
### getNamedBindingsCount()
    
    
    public abstract int getNamedBindingsCount()

For each non-reserved named binding site in the query string, there must be a named parameter with that name, but not necessarily the inverse.

Key must match regex `A-Za-z_$__`, must not match regex`__.__`, and must not be `""`.

`map<string, .google.datastore.v1.GqlQueryParameter> named_bindings = 5;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getNamedBindingsMap()
    
    
    public abstract Map<String,GqlQueryParameter> getNamedBindingsMap()

For each non-reserved named binding site in the query string, there must be a named parameter with that name, but not necessarily the inverse.

Key must match regex `A-Za-z_$__`, must not match regex`__.__`, and must not be `""`.

`map<string, .google.datastore.v1.GqlQueryParameter> named_bindings = 5;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[GqlQueryParameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.GqlQueryParameter)>` |   
  
### getNamedBindingsOrDefault(String key, GqlQueryParameter defaultValue)
    
    
    public abstract GqlQueryParameter getNamedBindingsOrDefault(String key, GqlQueryParameter defaultValue)

For each non-reserved named binding site in the query string, there must be a named parameter with that name, but not necessarily the inverse.

Key must match regex `A-Za-z_$__`, must not match regex`__.__`, and must not be `""`.

`map<string, .google.datastore.v1.GqlQueryParameter> named_bindings = 5;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[GqlQueryParameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.GqlQueryParameter)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GqlQueryParameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.GqlQueryParameter)` |   
  
### getNamedBindingsOrThrow(String key)
    
    
    public abstract GqlQueryParameter getNamedBindingsOrThrow(String key)

For each non-reserved named binding site in the query string, there must be a named parameter with that name, but not necessarily the inverse.

Key must match regex `A-Za-z_$__`, must not match regex`__.__`, and must not be `""`.

`map<string, .google.datastore.v1.GqlQueryParameter> named_bindings = 5;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GqlQueryParameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.GqlQueryParameter)` |   
  
### getPositionalBindings(int index)
    
    
    public abstract GqlQueryParameter getPositionalBindings(int index)

Numbered binding site @1 references the first numbered parameter, effectively using 1-based indexing, rather than the usual 0.

For each binding site numbered i in `query_string`, there must be an i-th numbered parameter. The inverse must also be true.

`repeated .google.datastore.v1.GqlQueryParameter positional_bindings = 4;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GqlQueryParameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.GqlQueryParameter)` |   
  
### getPositionalBindingsCount()
    
    
    public abstract int getPositionalBindingsCount()

Numbered binding site @1 references the first numbered parameter, effectively using 1-based indexing, rather than the usual 0.

For each binding site numbered i in `query_string`, there must be an i-th numbered parameter. The inverse must also be true.

`repeated .google.datastore.v1.GqlQueryParameter positional_bindings = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getPositionalBindingsList()
    
    
    public abstract List<GqlQueryParameter> getPositionalBindingsList()

Numbered binding site @1 references the first numbered parameter, effectively using 1-based indexing, rather than the usual 0.

For each binding site numbered i in `query_string`, there must be an i-th numbered parameter. The inverse must also be true.

`repeated .google.datastore.v1.GqlQueryParameter positional_bindings = 4;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[GqlQueryParameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.GqlQueryParameter)>` |   
  
### getPositionalBindingsOrBuilder(int index)
    
    
    public abstract GqlQueryParameterOrBuilder getPositionalBindingsOrBuilder(int index)

Numbered binding site @1 references the first numbered parameter, effectively using 1-based indexing, rather than the usual 0.

For each binding site numbered i in `query_string`, there must be an i-th numbered parameter. The inverse must also be true.

`repeated .google.datastore.v1.GqlQueryParameter positional_bindings = 4;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GqlQueryParameterOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.GqlQueryParameterOrBuilder)` |   
  
### getPositionalBindingsOrBuilderList()
    
    
    public abstract List<? extends GqlQueryParameterOrBuilder> getPositionalBindingsOrBuilderList()

Numbered binding site @1 references the first numbered parameter, effectively using 1-based indexing, rather than the usual 0.

For each binding site numbered i in `query_string`, there must be an i-th numbered parameter. The inverse must also be true.

`repeated .google.datastore.v1.GqlQueryParameter positional_bindings = 4;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.datastore.v1.GqlQueryParameterOrBuilder>` |   
  
### getQueryString()
    
    
    public abstract String getQueryString()

A string of the format described [here](https://cloud.google.com/datastore/docs/apis/gql/gql_reference).

`string query_string = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The queryString.  
  
### getQueryStringBytes()
    
    
    public abstract ByteString getQueryStringBytes()

A string of the format described [here](https://cloud.google.com/datastore/docs/apis/gql/gql_reference).

`string query_string = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for queryString.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
