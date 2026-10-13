---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.TrinoJobOrBuilder
title: Interface TrinoJobOrBuilder (4.96.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:00:57.061730+00:00
---

# Interface TrinoJobOrBuilder (4.96.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.TrinoJobOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface TrinoJobOrBuilder (4.96.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.96.0 (latest)  4.92.0  4.91.1  4.90.0  4.88.0  4.85.0  4.84.0  4.82.0  4.80.0  4.79.0  4.78.0  4.77.0  4.75.0  4.73.0  4.72.0  4.71.0  4.70.0  4.69.0  4.67.0  4.65.0  4.64.0  4.61.0  4.60.0  4.59.0  4.57.0  4.56.0  4.55.0  4.54.0  4.53.0  4.52.0  4.51.0  4.50.0  4.49.0  4.48.0  4.46.0  4.45.0  4.44.0  4.43.0  4.42.0  4.41.0  4.40.0  4.39.0  4.38.0  4.37.0  4.36.0  4.34.0  4.33.0  4.32.0  4.31.0  4.30.0  4.29.0  4.28.0  4.27.0  4.26.0  4.25.0  4.24.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.16.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.0  4.8.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.8  3.1.2  3.0.3  2.3.1 
    
    
    public interface TrinoJobOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsProperties(String key)
    
    
    public abstract boolean containsProperties(String key)

Optional. A mapping of property names to values. Used to set Trino [session properties](https://trino.io/docs/current/sql/set-session.html) Equivalent to using the --session flag in the Trino CLI

`map<string, string> properties = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getClientTags(int index)
    
    
    public abstract String getClientTags(int index)

Optional. Trino client tags to attach to this query

`repeated string client_tags = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The clientTags at the given index.  
  
### getClientTagsBytes(int index)
    
    
    public abstract ByteString getClientTagsBytes(int index)

Optional. Trino client tags to attach to this query

`repeated string client_tags = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the clientTags at the given index.  
  
### getClientTagsCount()
    
    
    public abstract int getClientTagsCount()

Optional. Trino client tags to attach to this query

`repeated string client_tags = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of clientTags.  
  
### getClientTagsList()
    
    
    public abstract List<String> getClientTagsList()

Optional. Trino client tags to attach to this query

`repeated string client_tags = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the clientTags.  
  
### getContinueOnFailure()
    
    
    public abstract boolean getContinueOnFailure()

Optional. Whether to continue executing queries if a query fails. The default value is `false`. Setting to `true` can be useful when executing independent parallel queries.

`bool continue_on_failure = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The continueOnFailure.  
  
### getLoggingConfig()
    
    
    public abstract LoggingConfig getLoggingConfig()

Optional. The runtime log config for job execution.

` .google.cloud.dataproc.v1.LoggingConfig logging_config = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[LoggingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.LoggingConfig)` | The loggingConfig.  
  
### getLoggingConfigOrBuilder()
    
    
    public abstract LoggingConfigOrBuilder getLoggingConfigOrBuilder()

Optional. The runtime log config for job execution.

` .google.cloud.dataproc.v1.LoggingConfig logging_config = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[LoggingConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.LoggingConfigOrBuilder)` |   
  
### getOutputFormat()
    
    
    public abstract String getOutputFormat()

Optional. The format in which query output will be displayed. See the Trino documentation for supported output formats

`string output_format = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The outputFormat.  
  
### getOutputFormatBytes()
    
    
    public abstract ByteString getOutputFormatBytes()

Optional. The format in which query output will be displayed. See the Trino documentation for supported output formats

`string output_format = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for outputFormat.  
  
### getProperties() (deprecated)
    
    
    public abstract Map<String,String> getProperties()

Use [#getPropertiesMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.TrinoJobOrBuilder#com_google_cloud_dataproc_v1_TrinoJobOrBuilder_getPropertiesMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getPropertiesCount()
    
    
    public abstract int getPropertiesCount()

Optional. A mapping of property names to values. Used to set Trino [session properties](https://trino.io/docs/current/sql/set-session.html) Equivalent to using the --session flag in the Trino CLI

`map<string, string> properties = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getPropertiesMap()
    
    
    public abstract Map<String,String> getPropertiesMap()

Optional. A mapping of property names to values. Used to set Trino [session properties](https://trino.io/docs/current/sql/set-session.html) Equivalent to using the --session flag in the Trino CLI

`map<string, string> properties = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getPropertiesOrDefault(String key, String defaultValue)
    
    
    public abstract String getPropertiesOrDefault(String key, String defaultValue)

Optional. A mapping of property names to values. Used to set Trino [session properties](https://trino.io/docs/current/sql/set-session.html) Equivalent to using the --session flag in the Trino CLI

`map<string, string> properties = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getPropertiesOrThrow(String key)
    
    
    public abstract String getPropertiesOrThrow(String key)

Optional. A mapping of property names to values. Used to set Trino [session properties](https://trino.io/docs/current/sql/set-session.html) Equivalent to using the --session flag in the Trino CLI

`map<string, string> properties = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getQueriesCase()
    
    
    public abstract TrinoJob.QueriesCase getQueriesCase()

**Returns**  
---  
**Type** | **Description**  
`[TrinoJob.QueriesCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.TrinoJob.QueriesCase)` |   
  
### getQueryFileUri()
    
    
    public abstract String getQueryFileUri()

The HCFS URI of the script that contains SQL queries.

`string query_file_uri = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The queryFileUri.  
  
### getQueryFileUriBytes()
    
    
    public abstract ByteString getQueryFileUriBytes()

The HCFS URI of the script that contains SQL queries.

`string query_file_uri = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for queryFileUri.  
  
### getQueryList()
    
    
    public abstract QueryList getQueryList()

A list of queries.

`.google.cloud.dataproc.v1.QueryList query_list = 2;`

**Returns**  
---  
**Type** | **Description**  
`[QueryList](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.QueryList)` | The queryList.  
  
### getQueryListOrBuilder()
    
    
    public abstract QueryListOrBuilder getQueryListOrBuilder()

A list of queries.

`.google.cloud.dataproc.v1.QueryList query_list = 2;`

**Returns**  
---  
**Type** | **Description**  
`[QueryListOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.QueryListOrBuilder)` |   
  
### hasLoggingConfig()
    
    
    public abstract boolean hasLoggingConfig()

Optional. The runtime log config for job execution.

` .google.cloud.dataproc.v1.LoggingConfig logging_config = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the loggingConfig field is set.  
  
### hasQueryFileUri()
    
    
    public abstract boolean hasQueryFileUri()

The HCFS URI of the script that contains SQL queries.

`string query_file_uri = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the queryFileUri field is set.  
  
### hasQueryList()
    
    
    public abstract boolean hasQueryList()

A list of queries.

`.google.cloud.dataproc.v1.QueryList query_list = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the queryList field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
