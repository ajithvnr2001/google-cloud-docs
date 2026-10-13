---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.WindowsScheduledTask.TaskActionOrBuilder
title: Interface WindowsScheduledTask.TaskActionOrBuilder (0.7.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:35:57.183279+00:00
---

# Interface WindowsScheduledTask.TaskActionOrBuilder (0.7.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.WindowsScheduledTask.TaskActionOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface WindowsScheduledTask.TaskActionOrBuilder (0.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.0 (latest)  0.3.0  0.2.0  0.1.0 
    
    
    public static interface WindowsScheduledTask.TaskActionOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getActionType()
    
    
    public abstract WindowsScheduledTask.TaskAction.ActionType getActionType()

The action type of the task.

`.google.backstory.WindowsScheduledTask.TaskAction.ActionType action_type = 1;`

**Returns**  
---  
**Type** | **Description**  
`[WindowsScheduledTask.TaskAction.ActionType](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.WindowsScheduledTask.TaskAction.ActionType)` | The actionType.  
  
### getActionTypeValue()
    
    
    public abstract int getActionTypeValue()

The action type of the task.

`.google.backstory.WindowsScheduledTask.TaskAction.ActionType action_type = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for actionType.  
  
### getComClassId()
    
    
    public abstract String getComClassId()

The COM class IF the action is COM handler. This field is only populated if the task action type is COM_HANDLER.

`string com_class_id = 4;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The comClassId.  
  
### getComClassIdBytes()
    
    
    public abstract ByteString getComClassIdBytes()

The COM class IF the action is COM handler. This field is only populated if the task action type is COM_HANDLER.

`string com_class_id = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for comClassId.  
  
### getComData()
    
    
    public abstract String getComData()

The data of the task. This field is only populated if the task action type is COM_HANDLER.

`string com_data = 5;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The comData.  
  
### getComDataBytes()
    
    
    public abstract ByteString getComDataBytes()

The data of the task. This field is only populated if the task action type is COM_HANDLER.

`string com_data = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for comData.  
  
### getExecArguments(int index)
    
    
    public abstract String getExecArguments(int index)

The arguments of the task. This field is only populated if the task action type is EXEC.

`repeated string exec_arguments = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The execArguments at the given index.  
  
### getExecArgumentsBytes(int index)
    
    
    public abstract ByteString getExecArgumentsBytes(int index)

The arguments of the task. This field is only populated if the task action type is EXEC.

`repeated string exec_arguments = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the execArguments at the given index.  
  
### getExecArgumentsCount()
    
    
    public abstract int getExecArgumentsCount()

The arguments of the task. This field is only populated if the task action type is EXEC.

`repeated string exec_arguments = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of execArguments.  
  
### getExecArgumentsList()
    
    
    public abstract List<String> getExecArgumentsList()

The arguments of the task. This field is only populated if the task action type is EXEC.

`repeated string exec_arguments = 2;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the execArguments.  
  
### getExecWorkingDirectory()
    
    
    public abstract String getExecWorkingDirectory()

The executable working directory of the task. This field is only populated if the task action type is EXEC.

`string exec_working_directory = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The execWorkingDirectory.  
  
### getExecWorkingDirectoryBytes()
    
    
    public abstract ByteString getExecWorkingDirectoryBytes()

The executable working directory of the task. This field is only populated if the task action type is EXEC.

`string exec_working_directory = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for execWorkingDirectory.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
