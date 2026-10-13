---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.OSPolicy.Resource.ExecResource.ExecOrBuilder
title: Interface OSPolicy.Resource.ExecResource.ExecOrBuilder (2.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:49:27.889443+00:00
---

# Interface OSPolicy.Resource.ExecResource.ExecOrBuilder (2.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.OSPolicy.Resource.ExecResource.ExecOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface OSPolicy.Resource.ExecResource.ExecOrBuilder (2.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.101.0 (latest)  2.97.0  2.96.0  2.95.0  2.93.0  2.90.0  2.89.0  2.87.0  2.85.0  2.84.0  2.82.0  2.80.0  2.78.0  2.77.0  2.76.0  2.75.0  2.74.0  2.72.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.6  2.4.3  2.3.2 
    
    
    public static interface OSPolicy.Resource.ExecResource.ExecOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getArgs(int index)
    
    
    public abstract String getArgs(int index)

Optional arguments to pass to the source during execution.

`repeated string args = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The args at the given index.  
  
### getArgsBytes(int index)
    
    
    public abstract ByteString getArgsBytes(int index)

Optional arguments to pass to the source during execution.

`repeated string args = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the args at the given index.  
  
### getArgsCount()
    
    
    public abstract int getArgsCount()

Optional arguments to pass to the source during execution.

`repeated string args = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of args.  
  
### getArgsList()
    
    
    public abstract List<String> getArgsList()

Optional arguments to pass to the source during execution.

`repeated string args = 3;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the args.  
  
### getFile()
    
    
    public abstract OSPolicy.Resource.File getFile()

A remote or local file.

`.google.cloud.osconfig.v1alpha.OSPolicy.Resource.File file = 1;`

**Returns**  
---  
**Type** | **Description**  
`[OSPolicy.Resource.File](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.OSPolicy.Resource.File)` | The file.  
  
### getFileOrBuilder()
    
    
    public abstract OSPolicy.Resource.FileOrBuilder getFileOrBuilder()

A remote or local file.

`.google.cloud.osconfig.v1alpha.OSPolicy.Resource.File file = 1;`

**Returns**  
---  
**Type** | **Description**  
`[OSPolicy.Resource.FileOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.OSPolicy.Resource.FileOrBuilder)` |   
  
### getInterpreter()
    
    
    public abstract OSPolicy.Resource.ExecResource.Exec.Interpreter getInterpreter()

Required. The script interpreter to use.

` .google.cloud.osconfig.v1alpha.OSPolicy.Resource.ExecResource.Exec.Interpreter interpreter = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[OSPolicy.Resource.ExecResource.Exec.Interpreter](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.OSPolicy.Resource.ExecResource.Exec.Interpreter)` | The interpreter.  
  
### getInterpreterValue()
    
    
    public abstract int getInterpreterValue()

Required. The script interpreter to use.

` .google.cloud.osconfig.v1alpha.OSPolicy.Resource.ExecResource.Exec.Interpreter interpreter = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for interpreter.  
  
### getOutputFilePath()
    
    
    public abstract String getOutputFilePath()

Only recorded for enforce Exec. Path to an output file (that is created by this Exec) whose content will be recorded in OSPolicyResourceCompliance after a successful run. Absence or failure to read this file will result in this ExecResource being non-compliant. Output file size is limited to 100K bytes.

`string output_file_path = 5;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The outputFilePath.  
  
### getOutputFilePathBytes()
    
    
    public abstract ByteString getOutputFilePathBytes()

Only recorded for enforce Exec. Path to an output file (that is created by this Exec) whose content will be recorded in OSPolicyResourceCompliance after a successful run. Absence or failure to read this file will result in this ExecResource being non-compliant. Output file size is limited to 100K bytes.

`string output_file_path = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for outputFilePath.  
  
### getScript()
    
    
    public abstract String getScript()

An inline script. The size of the script is limited to 1024 characters.

`string script = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The script.  
  
### getScriptBytes()
    
    
    public abstract ByteString getScriptBytes()

An inline script. The size of the script is limited to 1024 characters.

`string script = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for script.  
  
### getSourceCase()
    
    
    public abstract OSPolicy.Resource.ExecResource.Exec.SourceCase getSourceCase()

**Returns**  
---  
**Type** | **Description**  
`[OSPolicy.Resource.ExecResource.Exec.SourceCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.OSPolicy.Resource.ExecResource.Exec.SourceCase)` |   
  
### hasFile()
    
    
    public abstract boolean hasFile()

A remote or local file.

`.google.cloud.osconfig.v1alpha.OSPolicy.Resource.File file = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the file field is set.  
  
### hasScript()
    
    
    public abstract boolean hasScript()

An inline script. The size of the script is limited to 1024 characters.

`string script = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the script field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
