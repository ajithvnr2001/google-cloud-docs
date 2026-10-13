---
url: https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.wireoutput.CommandCompleteResponse
title: Class CommandCompleteResponse (0.27.1) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:44:44.109881+00:00
---

# Class CommandCompleteResponse (0.27.1)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.wireoutput.CommandCompleteResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CommandCompleteResponse (0.27.1) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 0.27.1 (latest) ](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.wireoutput.CommandCompleteResponse)
  * [ 0.27.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.27.0/com.google.cloud.spanner.pgadapter.wireoutput.CommandCompleteResponse)
  * [ 0.26.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.26.0/com.google.cloud.spanner.pgadapter.wireoutput.CommandCompleteResponse)
  * [ 0.25.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.25.0/com.google.cloud.spanner.pgadapter.wireoutput.CommandCompleteResponse)
  * [ 0.24.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.24.0/com.google.cloud.spanner.pgadapter.wireoutput.CommandCompleteResponse)
  * [ 0.23.1 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.23.1/com.google.cloud.spanner.pgadapter.wireoutput.CommandCompleteResponse)
  * [ 0.22.1 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.22.1/com.google.cloud.spanner.pgadapter.wireoutput.CommandCompleteResponse)
  * [ 0.21.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.21.0/com.google.cloud.spanner.pgadapter.wireoutput.CommandCompleteResponse)
  * [ 0.20.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.20.0/com.google.cloud.spanner.pgadapter.wireoutput.CommandCompleteResponse)
  * [ 0.19.1 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.19.1/com.google.cloud.spanner.pgadapter.wireoutput.CommandCompleteResponse)
  * [ 0.18.4 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.18.4/com.google.cloud.spanner.pgadapter.wireoutput.CommandCompleteResponse)
  * [ 0.17.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.17.0/com.google.cloud.spanner.pgadapter.wireoutput.CommandCompleteResponse)
  * [ 0.16.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.16.0/com.google.cloud.spanner.pgadapter.wireoutput.CommandCompleteResponse)
  * [ 0.15.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.15.0/com.google.cloud.spanner.pgadapter.wireoutput.CommandCompleteResponse)
  * [ 0.14.1 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.14.1/com.google.cloud.spanner.pgadapter.wireoutput.CommandCompleteResponse)
  * [ 0.9.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.9.0/com.google.cloud.spanner.pgadapter.wireoutput.CommandCompleteResponse)
  * [ 0.8.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.8.0/com.google.cloud.spanner.pgadapter.wireoutput.CommandCompleteResponse)
  * [ 0.7.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.7.0/com.google.cloud.spanner.pgadapter.wireoutput.CommandCompleteResponse)
  * [ 0.6.1 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.6.1/com.google.cloud.spanner.pgadapter.wireoutput.CommandCompleteResponse)
  * [ 0.5.1 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.5.1/com.google.cloud.spanner.pgadapter.wireoutput.CommandCompleteResponse)


    
    
    public class CommandCompleteResponse extends WireOutput

Signals to a client that an issued query is complete.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [WireOutput](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.wireoutput.WireOutput) > CommandCompleteResponse

## Inherited Members

[WireOutput.getIdentifier()](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.wireoutput.WireOutput#com_google_cloud_spanner_pgadapter_wireoutput_WireOutput_getIdentifier__)

[WireOutput.getMessageName()](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.wireoutput.WireOutput#com_google_cloud_spanner_pgadapter_wireoutput_WireOutput_getMessageName__)

[WireOutput.getPayloadString()](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.wireoutput.WireOutput#com_google_cloud_spanner_pgadapter_wireoutput_WireOutput_getPayloadString__)

[WireOutput.isCompoundResponse()](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.wireoutput.WireOutput#com_google_cloud_spanner_pgadapter_wireoutput_WireOutput_isCompoundResponse__)

[WireOutput.send()](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.wireoutput.WireOutput#com_google_cloud_spanner_pgadapter_wireoutput_WireOutput_send__)

[WireOutput.send(boolean)](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.wireoutput.WireOutput#com_google_cloud_spanner_pgadapter_wireoutput_WireOutput_send_boolean_)

[WireOutput.sendPayload()](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.wireoutput.WireOutput#com_google_cloud_spanner_pgadapter_wireoutput_WireOutput_sendPayload__)

[WireOutput.toString()](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.wireoutput.WireOutput#com_google_cloud_spanner_pgadapter_wireoutput_WireOutput_toString__)

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Constructors 

### CommandCompleteResponse(DataOutputStream output, String command)
    
    
    public CommandCompleteResponse(DataOutputStream output, String command)

**Parameters**  
---  
**Name** | **Description**  
`output` | `[DataOutputStream](https://docs.oracle.com/javase/8/docs/api/java/io/DataOutputStream.html)`  
  
`command` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
## Methods 

### getIdentifier()
    
    
    public byte getIdentifier()

Override this to specify the byte which represents the protocol for the specific message. Used for logging and by send.

**Returns**  
---  
**Type** | **Description**  
`[byte](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[WireOutput.getIdentifier()](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.wireoutput.WireOutput#com_google_cloud_spanner_pgadapter_wireoutput_WireOutput_getIdentifier__)

### getMessageName()
    
    
    protected String getMessageName()

Used for logging.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Overrides**

[WireOutput.getMessageName()](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.wireoutput.WireOutput#com_google_cloud_spanner_pgadapter_wireoutput_WireOutput_getMessageName__)

### getPayloadString()
    
    
    protected String getPayloadString()

Used for logging.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Overrides**

[WireOutput.getPayloadString()](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.wireoutput.WireOutput#com_google_cloud_spanner_pgadapter_wireoutput_WireOutput_getPayloadString__)

### sendPayload()
    
    
    protected void sendPayload()

Override this method to include post-processing and metadata in the sending process. Template method for send.

**Overrides**

[WireOutput.sendPayload()](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.wireoutput.WireOutput#com_google_cloud_spanner_pgadapter_wireoutput_WireOutput_sendPayload__)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
