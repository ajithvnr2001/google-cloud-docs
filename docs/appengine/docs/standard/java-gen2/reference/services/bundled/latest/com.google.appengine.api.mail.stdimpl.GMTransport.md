---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.stdimpl.GMTransport
title: Class GMTransport (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T01:45:36.136126+00:00
---

# Class GMTransport (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.stdimpl.GMTransport

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class GMTransport (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public class GMTransport extends Transport

Implementation of the 'Google Message Transport' which really just connects to the exposed MailService and uses it to deliver a message. 

The special destination address "admins" results in a delivery of the message to the owners of the application. 

Note that most RFC822 headers are silently ignored.

## Inheritance

[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > javax.mail.Service > [Transport](https://docs.oracle.com/javase/8/docs/api/javax/mail/Transport.html) > GMTransport

## Inherited Members

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

[Service.addConnectionListener(ConnectionListener)](https://docs.oracle.com/javase/8/docs/api/javax/mail/Service.html#addConnectionListener-javax.mail.event.ConnectionListener-)

[Service.close()](https://docs.oracle.com/javase/8/docs/api/javax/mail/Service.html#close--)

[Service.connect()](https://docs.oracle.com/javase/8/docs/api/javax/mail/Service.html#connect--)

[Service.connect(String,int,String,String)](https://docs.oracle.com/javase/8/docs/api/javax/mail/Service.html#connect-java.lang.String-int-java.lang.String-java.lang.String-)

[Service.connect(String,String)](https://docs.oracle.com/javase/8/docs/api/javax/mail/Service.html#connect-java.lang.String-java.lang.String-)

[Service.connect(String,String,String)](https://docs.oracle.com/javase/8/docs/api/javax/mail/Service.html#connect-java.lang.String-java.lang.String-java.lang.String-)

[Service.finalize()](https://docs.oracle.com/javase/8/docs/api/javax/mail/Service.html#finalize--)

[Service.getURLName()](https://docs.oracle.com/javase/8/docs/api/javax/mail/Service.html#getURLName--)

[Service.isConnected()](https://docs.oracle.com/javase/8/docs/api/javax/mail/Service.html#isConnected--)

[Service.notifyConnectionListeners(int)](https://docs.oracle.com/javase/8/docs/api/javax/mail/Service.html#notifyConnectionListeners-int-)

[Service.protocolConnect(String,int,String,String)](https://docs.oracle.com/javase/8/docs/api/javax/mail/Service.html#protocolConnect-java.lang.String-int-java.lang.String-java.lang.String-)

[Service.queueEvent(MailEvent,Vector)](https://docs.oracle.com/javase/8/docs/api/javax/mail/Service.html#queueEvent-javax.mail.event.MailEvent-java.util.Vector-)

[Service.removeConnectionListener(ConnectionListener)](https://docs.oracle.com/javase/8/docs/api/javax/mail/Service.html#removeConnectionListener-javax.mail.event.ConnectionListener-)

[Service.setConnected(boolean)](https://docs.oracle.com/javase/8/docs/api/javax/mail/Service.html#setConnected-boolean-)

[Service.setURLName(URLName)](https://docs.oracle.com/javase/8/docs/api/javax/mail/Service.html#setURLName-javax.mail.URLName-)

[Service.toString()](https://docs.oracle.com/javase/8/docs/api/javax/mail/Service.html#toString--)

[Transport.addTransportListener(TransportListener)](https://docs.oracle.com/javase/8/docs/api/javax/mail/Transport.html#addTransportListener-javax.mail.event.TransportListener-)

[Transport.notifyTransportListeners(int,Address[],Address[],Address[],Message)](https://docs.oracle.com/javase/8/docs/api/javax/mail/Transport.html#notifyTransportListeners-int-javax.mail.Address\[\]-javax.mail.Address\[\]-javax.mail.Address\[\]-javax.mail.Message-)

[Transport.removeTransportListener(TransportListener)](https://docs.oracle.com/javase/8/docs/api/javax/mail/Transport.html#removeTransportListener-javax.mail.event.TransportListener-)

[Transport.send(Message)](https://docs.oracle.com/javase/8/docs/api/javax/mail/Transport.html#send-javax.mail.Message-)

[Transport.send(Message,Address[])](https://docs.oracle.com/javase/8/docs/api/javax/mail/Transport.html#send-javax.mail.Message-javax.mail.Address\[\]-)

[Transport.sendMessage(Message,Address[])](https://docs.oracle.com/javase/8/docs/api/javax/mail/Transport.html#sendMessage-javax.mail.Message-javax.mail.Address\[\]-)

## Constructors 

### GMTransport(Session session, URLName urlName)
    
    
    public GMTransport(Session session, URLName urlName)

**Parameters**  
---  
**Name** | **Description**  
`session` | `[Session](https://docs.oracle.com/javase/8/docs/api/javax/mail/Session.html)`  
  
`urlName` | `[URLName](https://docs.oracle.com/javase/8/docs/api/javax/mail/URLName.html)`  
  
  
## Methods 

### equals(Object obj)
    
    
    public boolean equals(Object obj)

**Parameter**  
---  
**Name** | **Description**  
`obj` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

### hashCode()
    
    
    public int hashCode()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

### protocolConnect(String host, int port, String user, String password)
    
    
    protected boolean protocolConnect(String host, int port, String user, String password)

**Parameters**  
---  
**Name** | **Description**  
`host` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`port` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`user` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`password` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Service.protocolConnect(String,int,String,String)](https://docs.oracle.com/javase/8/docs/api/javax/mail/Service.html#protocolConnect-java.lang.String-int-java.lang.String-java.lang.String-)

### sendMessage(Message message, Address[] addresses)
    
    
    public void sendMessage(Message message, Address[] addresses)

**Parameters**  
---  
**Name** | **Description**  
`message` | `[Message](https://docs.oracle.com/javase/8/docs/api/javax/mail/Message.html)`  
  
`addresses` | `javax.mail.Address[]`  
  
**Overrides**

[Transport.sendMessage(Message,Address[])](https://docs.oracle.com/javase/8/docs/api/javax/mail/Transport.html#sendMessage-javax.mail.Message-javax.mail.Address\[\]-)

**Exceptions**  
---  
**Type** | **Description**  
`[MessagingException](https://docs.oracle.com/javase/8/docs/api/javax/mail/MessagingException.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
