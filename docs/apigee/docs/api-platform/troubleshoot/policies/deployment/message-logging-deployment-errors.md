---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/message-logging-deployment-errors/
title: Message Logging policy deployment error troubleshooting \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:01:06.030944+00:00
---

# Message Logging policy deployment error troubleshooting  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/message-logging-deployment-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Message Logging policy deployment error troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/troubleshoot/policies/deployment/message-logging-deployment-errors) documentation._

Was this troubleshooting playbook helpful? Please let us know by clicking [ Send Feedback ](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/message-logging-deployment-errors/).

## InvalidProtocol

### Error message

Deployment of an API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision revision_number
    Invalid Protocol: invalid_protocol for Syslog handler in policy policy_name.
    

### Example error message
    
    
    Error Saving Revision 4
    Invalid Protocol: HTTP for Syslog handler in policy LogToSyslog.
    

### Example screenshot

![Error saving revision 4.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/messagelogging-error-2.png)

### **Cause**

The deployment of the [MessageLogging policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/message-logging-policy) policy can fail with this error if the protocol specified within the `<Protocol>` element is not valid. The valid protocols are TCP and UDP. For sending syslog messages over TLS/SSL, only TCP is supported.

For example, the deployment of the API Proxy fails with this error if you specify HTTP in the `<Protocol>` element of the MessageLogging Policy as shown below:
    
    
    <Protocol>HTTP</Protocol>
    

### **Diagnosis**

  1. Identify the MessageLogging policy where the error occurred. You can find this information in the error message. For example, in the following error, the policy name is `LogToSyslog:`
         
         Invalid Protocol: HTTP for Syslog handler in policy LogToSyslog.
         

  2. In the failed MessageLogging policy configuration check if the protocol specified within the `<Protocol>` element is valid. If there is an invalid protocol specified, then that's the cause of the error.

For example, the following policy specifies an invalid protocol.
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
         <MessageLogging name="LogToSyslog">
           <Syslog>
             <Message>[3f509b58 tag="{organization.name}.{apiproxy.name}.{environment.name}"] Weather request for WOEID {request.queryparam.w}.</Message>
             <Host>logs-01.loggly.com</Host>
             <Port>514</Port>
             <Protocol>HTTP</Protocol>
             <FormatMessage>true</FormatMessage>
           </Syslog>
           <logLevel>ALERT</logLevel>
         </MessageLogging>
         

Because the protocol defined within the `<Protocol>` element is invalid, the deployment of the API Proxy fails with the error:
         
         Invalid Protocol: HTTP for Syslog handler in policy LogToSyslog.
         




### Resolution

Ensure that the protocol defined within the `<Protocol>` element of the MessageLogging policy is valid. The `<Protocol>` element supports the following values:

  * TCP
  * UDP



To correct the example shown above, define a valid protocol within the `<Protocol>` element:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <MessageLogging name="LogToSyslog">
      <Syslog>
        <Message>[3f509b58 tag="{organization.name}.{apiproxy.name}.{environment.name}"] Weather request for WOEID {request.queryparam.w}.</Message>
        <Host>logs-01.loggly.com</Host>
        <Port>514</Port>
        <Protocol>TCP</Protocol>
        <FormatMessage>true</FormatMessage>
      </Syslog>
      <logLevel>ALERT</logLevel>
    </MessageLogging>
    

## InvalidPort

### Error message

Deployment of an API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision revision_number
    Invalid Port: 0 for Syslog handler in policy policy_name.
    

### Example error message
    
    
    Error Saving Revision 4
    Invalid Port: 0 for Syslog handler in policy LogToSyslog.
    

### Example screenshot

![Error saving revision 4.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/messagelogging-error-1.png)

### Cause

The deployment of the [MessageLogging policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/message-logging-policy) can fail with this error if the port number is not specified within the `<Port>` element or if it is not valid. The port number must be an integer greater than zero.

For example, if the `<Port>` element is declared as shown below, the deployment of the API proxy fails:
    
    
    <Port>0</Port>
    

### Diagnosis

  1. Identify the MessageLogging policy where the error occurred. You can find this information from the error message. For example, in the following error, the policy name is `LogToSyslog:`
         
         Invalid Port: 0 for Syslog handler in policy LogToSyslog.
         

  2. In the failed MessageLogging policy check if a valid port number is specified within the `<Port>` element. If the port number is not defined or is invalid, then that's the cause of the error.

For example, the following policy specifies an invalid port number:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
         <MessageLogging name="LogToSyslog">
           <Syslog>
             <Message>[3f509b58 tag="{organization.name}.{apiproxy.name}.{environment.name}"] Weather request for WOEID {request.queryparam.w}.</Message>
             <Host>logs-01.loggly.com</Host>
             <Port>0</Port>
             <Protocol>TCP</Protocol>
             <FormatMessage>true</FormatMessage>
           </Syslog>
           <logLevel>ALERT</logLevel>
         </MessageLogging>
         

Because the port number defined within the `<Port>` element is invalid, the deployment of the API Proxy fails with the error:
         
         Invalid Port: 0 for Syslog handler in policy LogToSyslog.
         




### Resolution

Ensure that a port number is defined within the `<Port>` element of the MessageLogging policy. It has to be an integer greater than zero.

To correct the example shown above, define a valid port number within the `<Protocol>` element.
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <MessageLogging name="LogToSyslog">
      <Syslog>
        <Message>[3f509b58 tag="{organization.name}.{apiproxy.name}.{environment.name}"] Weather request for WOEID {request.queryparam.w}.</Message>
        <Host>logs-01.loggly.com</Host>
        <Port>514</Port>
        <Protocol>TCP</Protocol>
        <FormatMessage>true</FormatMessage>
      </Syslog>
      <logLevel>ALERT</logLevel>
    </MessageLogging>
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
