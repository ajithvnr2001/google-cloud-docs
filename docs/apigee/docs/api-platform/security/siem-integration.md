---
url: https://docs.cloud.google.com/apigee/docs/api-platform/security/siem-integration/
title: Integrate Apigee with your SIEM solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:44:52.340384+00:00
---

# Integrate Apigee with your SIEM solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/security/siem-integration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Integrate Apigee with your SIEM solution Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

Many organizations seek to integrate Apigee with their Security Information and Event Management (SIEM) solutions. This integration enables the valuable correlation of Apigee data with other network and security product logs, facilitating advanced threat detection, comprehensive logging, and compliance reporting. This document explores various integration approaches, catering to scenarios both with and without the [Advanced API Security](https://docs.cloud.google.com/apigee/docs/api-security) add-on. 

## Audience

The audience for this document includes:

  * **API administrators** responsible for ensuring API security, managing platform configurations, supporting operational efficiency, and adhering to security compliance requirements.
  * **Security analysts** focused on proactively detecting and investigating API-related security incidents to minimize risk and safeguard sensitive data.



## Configuration options

Apigee offers two primary methods for sending log information to a SIEM: 

Option | Description  
---|---  
[Google Cloud platform logs](https://docs.cloud.google.com/logging/docs/api/platform-logs) | Provides a foundational level of API log data, including service-specific logs helpful for debugging and troubleshooting. | Apigee Message Logging policy | The Message Logging policy offers greater flexibility and control, allowing you to send a wide range of Apigee log data, including specific flow variables, to your SIEM.   
  
## Integrating Apigee with your SIEM

Apigee's adaptability ensures smooth integration with your chosen SIEM solution. The general integration steps are:

**Note:** If you use Google Security Operations SIEM, see [Integrate Apigee with Google SecOps](https://docs.cloud.google.com/apigee/docs/api-platform/security/secops-integration) for more information. See also [Google Security Operations SIEM overview](https://docs.cloud.google.com/chronicle/docs/overview).

  1. **Choose your integration method.** Select either Google Cloud platform logs or the Apigee Message Logging policy based on your data requirements and SIEM capabilities.
  2. **Establish Data Forwarding.** To establish data forwarding, configure Apigee to send the desired log data to your SIEM. The basic steps for this configuration are as follows. The exact steps depend on your SIEM system's setup and configuration details: 
     1. Set up a connection or integration between Apigee and your SIEM.
     2. Specify in your SIEM configuration which Apigee logs or events to forward to your SIEM.
     3. Grant necessary permissions within your SIEM to receive and process the Apigee data.
  3. **Align Data Structures.** Map the Apigee log fields and [flow variables](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference) (like `client.ip`, `request.uri`, etc.) to the corresponding fields in your SIEM's data model. This alignment ensures that the SIEM can correctly interpret and categorize the Apigee data for effective analysis and correlation with other security events.



## Log Advanced API security data

If you wish to log data that was identified by Advanced API security [Abuse detection](https://docs.cloud.google.com/apigee/docs/api-security/abuse-detection), you can use [Actions](https://docs.cloud.google.com/apigee/docs/api-security/security-actions) with the Apigee Message Logging policy. 

Follow these steps:

  1. Use [Advanced API Security actions](https://docs.cloud.google.com/apigee/docs/api-security/security-actions) to flag a rule you want to log.
  2. Use the header added by the action to trigger the Message Logging policy to log the flagged request. For example, the following image shows the header `apisec` configured with the value `abuse` in the actions UI: 

![A screenshot showing
      the header apisec configured with value abuse in the API Security actions UI](https://docs.cloud.google.com/static/apigee/docs/api-monitoring/images/action-header.png)

Following this example, you could configure the Message Logging policy to trigger when it sees the header:
         
         <PostFlow name="PostFlow">
           <Request>
             <Step>
               <Condition>request.header.apisec="abuse"</Condition>
               <Name>LogMessagePolicy</Name>
             </Step>
           </Request>
         </PostFlow>




## Example: Use the Apigee Message Logging policy

This example shows how to configure the Apigee [Message Logging policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/message-logging-policy) to send Apigee log data to a SIEM. With this option, you specify in the Message Logging policy which Apigee [flow variables](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference) you wish to send to the SIEM. This option lets you send a richer set of log details to the SIEM than you get with the Cloud platform log option.

**Note:** To use this option, you must be familiar with configuring and using [Apigee policies](https://docs.cloud.google.com/apigee/docs/api-platform/develop/policy-attachment-and-enforcement).

  1. Enable ingestion of Apigee data into the SIEM. 
  2. Create a [Message Logging policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/message-logging-policy) with the following XML body. For help, see [Attaching and configuring policies in the UI](https://docs.cloud.google.com/apigee/docs/api-platform/develop/attaching-and-configuring-policies-management-ui). **Note** : Only the flow variables specified in the policy will be sent to the SIEM. If you do not wish to log certain variables, remove them from the policy body.
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
             <MessageLogging continueOnError="false" enabled="true" name="ML-SIEM-Integration">
               <CloudLogging>
                 <LogName>projects/{organization.name}/logs/Apigee-SIEM-Integration-{environment.name}</LogName>
                 <Message contentType="application/json" defaultVariableValue="unknown">
                 {
                   "apigee.metrics.policy.{policy_name}.timeTaken": "{apigee.metrics.policy.{policy_name}.timeTaken}",
                   "client.country": "{client.country}",
                   "client.host": "{client.host}",
                   "client.ip": "{client.ip}",
                   "client.locality": "{client.locality}",
                   "client.port": "{client.port}",
                  "client.state": "{client.state}",
                   "organization.name": "{organization.name}",
                 "proxy.client.ip": "{proxy.client.ip}",
                 "proxy.name": "{proxy.name}",
                 "proxy.pathsuffix": "{proxy.pathsuffix}",
                 "proxy.url": "{proxy.url}",
                 "request.uri": "{request.uri}",
                 "request.verb": "{request.verb}",
                 "response.content": "{response.content}",
                 "response.reason.phrase": "{response.reason.phrase}",
                 "response.status.code": "{response.status.code}",
                 "system.region.name": "{system.region.name}",
                 "system.timestamp": "{system.timestamp}",
                 "system.uuid": "{system.uuid}",
                 "target.country": "{target.country}",
                 "target.host": "{target.host}",
                 "target.ip": "{target.ip}",
                 "target.locality": "{target.locality}",
                 "target.organization": "{target.organization}",
                 "target.port": "{target.port}",
                 "target.scheme": "{target.scheme}",
                 "target.state": "{target.state}",
                 "target.url": "{target.url}"
                 }
                  </Message>
               </CloudLogging>
             </MessageLogging>

  3. Attach the policy to the Proxy Endpoint Post Flow. See [Attaching and configuring policies in the UI](https://docs.cloud.google.com/apigee/docs/api-platform/develop/attaching-and-configuring-policies-management-ui). 



As the API proxy processes traffic, the logging policy will capture the specified fields from the requests and responses and write them out to the log file for analysis and debugging.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
