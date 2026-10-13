---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Task.SparkTaskConfigOrBuilder
title: Interface Task.SparkTaskConfigOrBuilder (1.97.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:25:37.936330+00:00
---

# Interface Task.SparkTaskConfigOrBuilder (1.97.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Task.SparkTaskConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface Task.SparkTaskConfigOrBuilder (1.97.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.97.0 (latest)  1.93.0  1.92.0  1.91.0  1.89.0  1.86.0  1.85.0  1.83.0  1.81.0  1.80.0  1.79.0  1.78.0  1.76.0  1.74.0  1.73.0  1.72.0  1.71.0  1.70.0  1.68.0  1.66.0  1.65.0  1.62.0  1.61.0  1.60.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.2  1.0.1  0.2.2 
    
    
    public static interface Task.SparkTaskConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getArchiveUris(int index)
    
    
    public abstract String getArchiveUris(int index)

Optional. Cloud Storage URIs of archives to be extracted into the working directory of each executor. Supported file types: .jar, .tar, .tar.gz, .tgz, and .zip.

`repeated string archive_uris = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The archiveUris at the given index.  
  
### getArchiveUrisBytes(int index)
    
    
    public abstract ByteString getArchiveUrisBytes(int index)

Optional. Cloud Storage URIs of archives to be extracted into the working directory of each executor. Supported file types: .jar, .tar, .tar.gz, .tgz, and .zip.

`repeated string archive_uris = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the archiveUris at the given index.  
  
### getArchiveUrisCount()
    
    
    public abstract int getArchiveUrisCount()

Optional. Cloud Storage URIs of archives to be extracted into the working directory of each executor. Supported file types: .jar, .tar, .tar.gz, .tgz, and .zip.

`repeated string archive_uris = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of archiveUris.  
  
### getArchiveUrisList()
    
    
    public abstract List<String> getArchiveUrisList()

Optional. Cloud Storage URIs of archives to be extracted into the working directory of each executor. Supported file types: .jar, .tar, .tar.gz, .tgz, and .zip.

`repeated string archive_uris = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the archiveUris.  
  
### getDriverCase()
    
    
    public abstract Task.SparkTaskConfig.DriverCase getDriverCase()

**Returns**  
---  
**Type** | **Description**  
`[Task.SparkTaskConfig.DriverCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Task.SparkTaskConfig.DriverCase)` |   
  
### getFileUris(int index)
    
    
    public abstract String getFileUris(int index)

Optional. Cloud Storage URIs of files to be placed in the working directory of each executor.

`repeated string file_uris = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The fileUris at the given index.  
  
### getFileUrisBytes(int index)
    
    
    public abstract ByteString getFileUrisBytes(int index)

Optional. Cloud Storage URIs of files to be placed in the working directory of each executor.

`repeated string file_uris = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the fileUris at the given index.  
  
### getFileUrisCount()
    
    
    public abstract int getFileUrisCount()

Optional. Cloud Storage URIs of files to be placed in the working directory of each executor.

`repeated string file_uris = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of fileUris.  
  
### getFileUrisList()
    
    
    public abstract List<String> getFileUrisList()

Optional. Cloud Storage URIs of files to be placed in the working directory of each executor.

`repeated string file_uris = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the fileUris.  
  
### getInfrastructureSpec()
    
    
    public abstract Task.InfrastructureSpec getInfrastructureSpec()

Optional. Infrastructure specification for the execution.

` .google.cloud.dataplex.v1.Task.InfrastructureSpec infrastructure_spec = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Task.InfrastructureSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Task.InfrastructureSpec)` | The infrastructureSpec.  
  
### getInfrastructureSpecOrBuilder()
    
    
    public abstract Task.InfrastructureSpecOrBuilder getInfrastructureSpecOrBuilder()

Optional. Infrastructure specification for the execution.

` .google.cloud.dataplex.v1.Task.InfrastructureSpec infrastructure_spec = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Task.InfrastructureSpecOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Task.InfrastructureSpecOrBuilder)` |   
  
### getMainClass()
    
    
    public abstract String getMainClass()

The name of the driver's main class. The jar file that contains the class must be in the default CLASSPATH or specified in `jar_file_uris`. The execution args are passed in as a sequence of named process arguments (`--key=value`).

`string main_class = 101;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The mainClass.  
  
### getMainClassBytes()
    
    
    public abstract ByteString getMainClassBytes()

The name of the driver's main class. The jar file that contains the class must be in the default CLASSPATH or specified in `jar_file_uris`. The execution args are passed in as a sequence of named process arguments (`--key=value`).

`string main_class = 101;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for mainClass.  
  
### getMainJarFileUri()
    
    
    public abstract String getMainJarFileUri()

The Cloud Storage URI of the jar file that contains the main class. The execution args are passed in as a sequence of named process arguments (`--key=value`).

`string main_jar_file_uri = 100;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The mainJarFileUri.  
  
### getMainJarFileUriBytes()
    
    
    public abstract ByteString getMainJarFileUriBytes()

The Cloud Storage URI of the jar file that contains the main class. The execution args are passed in as a sequence of named process arguments (`--key=value`).

`string main_jar_file_uri = 100;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for mainJarFileUri.  
  
### getPythonScriptFile()
    
    
    public abstract String getPythonScriptFile()

The Gcloud Storage URI of the main Python file to use as the driver. Must be a .py file. The execution args are passed in as a sequence of named process arguments (`--key=value`).

`string python_script_file = 102;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The pythonScriptFile.  
  
### getPythonScriptFileBytes()
    
    
    public abstract ByteString getPythonScriptFileBytes()

The Gcloud Storage URI of the main Python file to use as the driver. Must be a .py file. The execution args are passed in as a sequence of named process arguments (`--key=value`).

`string python_script_file = 102;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for pythonScriptFile.  
  
### getSqlScript()
    
    
    public abstract String getSqlScript()

The query text. The execution args are used to declare a set of script variables (`set key="value";`).

`string sql_script = 105;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The sqlScript.  
  
### getSqlScriptBytes()
    
    
    public abstract ByteString getSqlScriptBytes()

The query text. The execution args are used to declare a set of script variables (`set key="value";`).

`string sql_script = 105;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for sqlScript.  
  
### getSqlScriptFile()
    
    
    public abstract String getSqlScriptFile()

A reference to a query file. This should be the Cloud Storage URI of the query file. The execution args are used to declare a set of script variables (`set key="value";`).

`string sql_script_file = 104;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The sqlScriptFile.  
  
### getSqlScriptFileBytes()
    
    
    public abstract ByteString getSqlScriptFileBytes()

A reference to a query file. This should be the Cloud Storage URI of the query file. The execution args are used to declare a set of script variables (`set key="value";`).

`string sql_script_file = 104;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for sqlScriptFile.  
  
### hasInfrastructureSpec()
    
    
    public abstract boolean hasInfrastructureSpec()

Optional. Infrastructure specification for the execution.

` .google.cloud.dataplex.v1.Task.InfrastructureSpec infrastructure_spec = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the infrastructureSpec field is set.  
  
### hasMainClass()
    
    
    public abstract boolean hasMainClass()

The name of the driver's main class. The jar file that contains the class must be in the default CLASSPATH or specified in `jar_file_uris`. The execution args are passed in as a sequence of named process arguments (`--key=value`).

`string main_class = 101;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the mainClass field is set.  
  
### hasMainJarFileUri()
    
    
    public abstract boolean hasMainJarFileUri()

The Cloud Storage URI of the jar file that contains the main class. The execution args are passed in as a sequence of named process arguments (`--key=value`).

`string main_jar_file_uri = 100;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the mainJarFileUri field is set.  
  
### hasPythonScriptFile()
    
    
    public abstract boolean hasPythonScriptFile()

The Gcloud Storage URI of the main Python file to use as the driver. Must be a .py file. The execution args are passed in as a sequence of named process arguments (`--key=value`).

`string python_script_file = 102;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the pythonScriptFile field is set.  
  
### hasSqlScript()
    
    
    public abstract boolean hasSqlScript()

The query text. The execution args are used to declare a set of script variables (`set key="value";`).

`string sql_script = 105;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the sqlScript field is set.  
  
### hasSqlScriptFile()
    
    
    public abstract boolean hasSqlScriptFile()

A reference to a query file. This should be the Cloud Storage URI of the query file. The execution args are used to declare a set of script variables (`set key="value";`).

`string sql_script_file = 104;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the sqlScriptFile field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
