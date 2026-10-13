---
url: https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.wireprotocol.TerminateMessage
title: Class TerminateMessage (0.27.1) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:31:09.234117+00:00
---

# Class TerminateMessage (0.27.1)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.wireprotocol.TerminateMessage

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class TerminateMessage (0.27.1) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 0.27.1 (latest) ](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.wireprotocol.TerminateMessage)
  * [ 0.27.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.27.0/com.google.cloud.spanner.pgadapter.wireprotocol.TerminateMessage)
  * [ 0.26.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.26.0/com.google.cloud.spanner.pgadapter.wireprotocol.TerminateMessage)
  * [ 0.25.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.25.0/com.google.cloud.spanner.pgadapter.wireprotocol.TerminateMessage)
  * [ 0.24.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.24.0/com.google.cloud.spanner.pgadapter.wireprotocol.TerminateMessage)
  * [ 0.23.1 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.23.1/com.google.cloud.spanner.pgadapter.wireprotocol.TerminateMessage)
  * [ 0.22.1 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.22.1/com.google.cloud.spanner.pgadapter.wireprotocol.TerminateMessage)
  * [ 0.21.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.21.0/com.google.cloud.spanner.pgadapter.wireprotocol.TerminateMessage)
  * [ 0.20.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.20.0/com.google.cloud.spanner.pgadapter.wireprotocol.TerminateMessage)
  * [ 0.19.1 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.19.1/com.google.cloud.spanner.pgadapter.wireprotocol.TerminateMessage)
  * [ 0.18.4 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.18.4/com.google.cloud.spanner.pgadapter.wireprotocol.TerminateMessage)
  * [ 0.17.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.17.0/com.google.cloud.spanner.pgadapter.wireprotocol.TerminateMessage)
  * [ 0.16.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.16.0/com.google.cloud.spanner.pgadapter.wireprotocol.TerminateMessage)
  * [ 0.15.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.15.0/com.google.cloud.spanner.pgadapter.wireprotocol.TerminateMessage)
  * [ 0.14.1 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.14.1/com.google.cloud.spanner.pgadapter.wireprotocol.TerminateMessage)
  * [ 0.9.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.9.0/com.google.cloud.spanner.pgadapter.wireprotocol.TerminateMessage)
  * [ 0.8.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.8.0/com.google.cloud.spanner.pgadapter.wireprotocol.TerminateMessage)
  * [ 0.7.0 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.7.0/com.google.cloud.spanner.pgadapter.wireprotocol.TerminateMessage)
  * [ 0.6.1 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.6.1/com.google.cloud.spanner.pgadapter.wireprotocol.TerminateMessage)
  * [ 0.5.1 ](https://docs.cloud.google.com/java/docs/reference/pgadapter/0.5.1/com.google.cloud.spanner.pgadapter.wireprotocol.TerminateMessage)


    
    
    public class TerminateMessage extends ControlMessage

Closes a connection.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [WireMessage](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.wireprotocol.WireMessage) > [ControlMessage](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.wireprotocol.ControlMessage) > TerminateMessage

## Inherited Members

[ControlMessage.create(ConnectionHandler)](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.wireprotocol.ControlMessage#com_google_cloud_spanner_pgadapter_wireprotocol_ControlMessage_create_com_google_cloud_spanner_pgadapter_ConnectionHandler_)

[ControlMessage.getFormatCodes(DataInputStream)](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.wireprotocol.ControlMessage#com_google_cloud_spanner_pgadapter_wireprotocol_ControlMessage_getFormatCodes_java_io_DataInputStream_)

[ControlMessage.handleError(Exception)](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.wireprotocol.ControlMessage#com_google_cloud_spanner_pgadapter_wireprotocol_ControlMessage_handleError_java_lang_Exception_)

[ControlMessage.isExtendedProtocol()](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.wireprotocol.ControlMessage#com_google_cloud_spanner_pgadapter_wireprotocol_ControlMessage_isExtendedProtocol__)

[WireMessage.getHeaderLength()](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.wireprotocol.WireMessage#com_google_cloud_spanner_pgadapter_wireprotocol_WireMessage_getHeaderLength__)

[WireMessage.getIdentifier()](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.wireprotocol.WireMessage#com_google_cloud_spanner_pgadapter_wireprotocol_WireMessage_getIdentifier__)

[WireMessage.getMessageName()](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.wireprotocol.WireMessage#com_google_cloud_spanner_pgadapter_wireprotocol_WireMessage_getMessageName__)

[WireMessage.getParameters(DataInputStream)](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.wireprotocol.WireMessage#com_google_cloud_spanner_pgadapter_wireprotocol_WireMessage_getParameters_java_io_DataInputStream_)

[WireMessage.getPayloadString()](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.wireprotocol.WireMessage#com_google_cloud_spanner_pgadapter_wireprotocol_WireMessage_getPayloadString__)

[WireMessage.nextHandler()](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.wireprotocol.WireMessage#com_google_cloud_spanner_pgadapter_wireprotocol_WireMessage_nextHandler__)

[WireMessage.read(int)](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.wireprotocol.WireMessage#com_google_cloud_spanner_pgadapter_wireprotocol_WireMessage_read_int_)

[WireMessage.readAll()](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.wireprotocol.WireMessage#com_google_cloud_spanner_pgadapter_wireprotocol_WireMessage_readAll__)

[WireMessage.readString()](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.wireprotocol.WireMessage#com_google_cloud_spanner_pgadapter_wireprotocol_WireMessage_readString__)

[WireMessage.send()](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.wireprotocol.WireMessage#com_google_cloud_spanner_pgadapter_wireprotocol_WireMessage_send__)

[WireMessage.sendPayload()](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.wireprotocol.WireMessage#com_google_cloud_spanner_pgadapter_wireprotocol_WireMessage_sendPayload__)

[WireMessage.toString()](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.wireprotocol.WireMessage#com_google_cloud_spanner_pgadapter_wireprotocol_WireMessage_toString__)

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

## Static Fields 

### IDENTIFIER
    
    
    protected static final char IDENTIFIER

**Field Value**  
---  
**Type** | **Description**  
`[char](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
## Constructors 

### TerminateMessage(ConnectionHandler connection)
    
    
    public TerminateMessage(ConnectionHandler connection)

**Parameter**  
---  
**Name** | **Description**  
`connection` | `[ConnectionHandler](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.ConnectionHandler)`  
  
  
## Methods 

### getIdentifier()
    
    
    public String getIdentifier()

Used for logging.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Overrides**

[WireMessage.getIdentifier()](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.wireprotocol.WireMessage#com_google_cloud_spanner_pgadapter_wireprotocol_WireMessage_getIdentifier__)

### getMessageName()
    
    
    protected String getMessageName()

Used for logging.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Overrides**

[WireMessage.getMessageName()](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.wireprotocol.WireMessage#com_google_cloud_spanner_pgadapter_wireprotocol_WireMessage_getMessageName__)

### getPayloadString()
    
    
    protected String getPayloadString()

Used for logging.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Overrides**

[WireMessage.getPayloadString()](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.wireprotocol.WireMessage#com_google_cloud_spanner_pgadapter_wireprotocol_WireMessage_getPayloadString__)

### sendPayload()
    
    
    protected void sendPayload()

Override this method to include post-processing and metadata in the sending process. Template method for send.

**Overrides**

[WireMessage.sendPayload()](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.wireprotocol.WireMessage#com_google_cloud_spanner_pgadapter_wireprotocol_WireMessage_sendPayload__)

**Exceptions**  
---  
**Type** | **Description**  
`[Exception](https://docs.oracle.com/javase/8/docs/api/java/lang/Exception.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
