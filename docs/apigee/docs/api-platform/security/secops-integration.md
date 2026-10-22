---
url: https://docs.cloud.google.com/apigee/docs/api-platform/security/secops-integration/
title: Integrate Apigee with Google SecOps \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:57:52.518788+00:00
---

# Integrate Apigee with Google SecOps  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/security/secops-integration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Integrate Apigee with Google SecOps Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

This document explains how to integrate Apigee with [Google Security Operations](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview) (Google SecOps). If you use Google SecOps as your SIEM solution, follow the steps in this document to configure Apigee to send log data to SecOps.

To facilitate this integration, Google SecOps supports an Apigee parser for ingesting Apigee log data. See also [Ingest Google Cloud data to Google Security Operations](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ingest-gcp-logs). After you complete the configuration steps in this document, your Apigee log data will flow to Google SecOps.

For information about how to integrate SecOps with other SIEM solutions, see [Integrate Apigee with your SIEM solution](https://docs.cloud.google.com/apigee/docs/api-platform/security/siem-integration).

## Audience

The audience for this document includes:

  * **API administrators** responsible for ensuring API security, managing platform configurations, supporting operational efficiency, and adhering to security compliance requirements.
  * **Security analysts** focused on proactively detecting and investigating API-related security incidents to minimize risk and safeguard sensitive data.



## Configuration overview

The configuration discussed in this document uses the Apigee [MessageLogging policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/message-logging-policy) to send a wide range of Apigee log data, including specific flow variables, to SecOps. 

Google SecOps provides a special Cloud Logging filter that can send specific log types, including Apigee logs, to Google SecOps in real time. Google SecOps supports an Apigee parser for ingesting Apigee log data into Google SecOps. See also [Ingest Google Cloud data to Google Security Operations](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-gcp-apigee-x).

## Prerequisites

Once these prerequisites are met, follow the instructions in this document to integrate Apigee with your SecOps instance. Before beginning the integration, ensure you have the following: 

  * An Apigee or Apigee hybrid account with administrative privileges to develop and deploy API proxies 
  * A Google SecOps account 
  * [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview) enabled and experience configuring and using Cloud Logging 
  * An understanding of Apigee [flow variables](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/introduction-flow-variables)
  * An understanding of the Apigee MessageLogging policy and general [policy use and configuration](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-policies)
  * (Optional) An understanding of how [Google SecOps parsers](https://docs.cloud.google.com/chronicle/docs/event-processing/parsing-overview) are used to interpret ingested logs. SecOps parsers are by default built in to parse and understand Apigee logs ingested by the MessageLogging policy. 
  * Google Cloud IAM permissions to use the Cloud Logging API and grant IAM roles to the SecOps service account



## Integrating Apigee with SecOps

If you are using Google SecOps as your SIEM solution, follow these steps to send Apigee log data to SecOps. There are two basic steps: 

  * Configure a MessageLogging policy to send Apigee log data to Cloud Logging
  * Attach the MessageLogging policy to an Apigee proxy



When the MessageLogging policy configuration described in this section is completed, Apigee log data sent to Cloud Logging will be parsed by SecOps. For detailed information about the parser and how Apigee flow variable data is mapped to SecOps data fields, see Integrate Apigee with Google SecOps SIEM. See also [Collect Apigee logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-gcp-apigee-x).

Follow these steps to integrate Apigee with SecOps using the MessageLogging policy: 

  1. Configure a new MessageLogging policy. See [Attaching and configuring policies in the UI](https://docs.cloud.google.com/apigee/docs/api-platform/develop/attaching-and-configuring-policies-management-ui).

**Note:** You can add or remove flow variables in the policy as you wish, depending on the fields you determine are important for your SecOps analysis. The following policy is an example only.

The following is an example MessageLogging policy that sends data to Cloud Logging. The policy specifies a large number of flow variables to be sent to Cloud Logging. You can add or remove flow variables as you wish, depending on the fields you determine are important for your SecOps analysis. For information about how Apigee flow variable data is mapped to SecOps data fields, see Integrate Apigee with Google SecOps SIEM.
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
           <MessageLogging continueOnError="false" enabled="true" name="ML-CloudLoggingSecOps">
            <DisplayName>ML-CloudLoggingSecOps</DisplayName>
            <CloudLogging>
              <LogName>projects/{organization.name}/logs/apigee-secops-integration-{environment.name}</LogName>
              <Message contentType="application/json">{
            "apiproduct.name": "{apiproduct.name}",
            "app.name": "{developer.app.name}",
            "cachehit":"{cachehit}",
            "client.country": "{client.country}",
            "client.cn": "{client.cn}",
            "client.ip": "{proxy.client.ip}",
            "client.locality": "{client.locality}",
            "client.port": "{client.port}",
            "client.scheme": "{client.scheme}",
            "client.state": "{client.state}",
            "developer.email": "{developer.email}",
            "environment.name": "{environment.name}",
            "error":"{is.error}",
            "error.state":"{error.state}",
            "error.message":"{escapeJSON(error.message)}",
            "fault.name":"{fault.name}",
            "messageid":"{messageid}",
            "organization.name": "{organization.name}",
            "proxy.name": "{apiproxy.name}",
            "proxy.basepath": "{proxy.basepath}",
            "proxy.pathsuffix": "{proxy.pathsuffix}",
            "proxy.proxyendpoint.name": "{proxy.name}",
            "proxy.revision":"{apiproxy.revision}",
            "request.content-length":"{request_msg.header.content-length}",
            "request.content-type":"{request_msg.header.content-type}",
            "request.host":"{request_msg.header.host}",
            "request.httpversion": "{request.version}",
            "request.url": "{client.scheme}://{request_msg.header.host}{request_msg.uri}",
            "request.user-agent":"{request.header.user-agent}",
            "request.verb": "{request.verb}",
            "request.x-b3-traceid": "{request.header.x-b3-traceid}",
            "request.x-cloud-trace-context": "{request.header.x-cloud-trace-context}",
            "response.content-length":"{response.header.content-length}",
            "response.content-type":"{response.header.content-type}",
            "response.status.code": "{message.status.code}",
            "system.region.name": "{system.region.name}",
            "system.timestamp": "{system.timestamp}",
            "system.uuid": "{system.uuid}",
            "target.cn": "{target.cn}",
            "target.country": "{target.country}",
            "target.host": "{target.host}",
            "target.ip": "{target.ip}",
            "target.locality": "{target.locality}",
            "target.organization": "{target.organization}",
            "target.port": "{target.port}",
            "target.scheme": "{target.scheme}",
            "target.state": "{target.state}",
            "target.url": "{request.url}"
           }
              </Message>
              <ResourceType>api</ResourceType>
            </CloudLogging>
           </MessageLogging>

  2. [Attach the policy as a conditional step](https://docs.cloud.google.com/apigee/docs/api-platform/develop/attaching-and-configuring-policies-management-ui) in an API proxy. One option is to attach the policy in a FaultRule in the PostFlow, where security related faults are typically raised. For example:
         
         <PostFlow name="PostFlow">
           <Request>
             <Step>
               <Condition>flow.isError == true)</Condition>
               <Name>ML-CloudLoggingSecOps</Name>
             </Step>
           </Request>
         </PostFlow>

Now when the API proxy that uses this policy executes, Apigee log data will flow to Google SecOps.

Another [common practice](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/message-logging-policy#usage) is to place the MessageLogging policy in the PostClientFlow of the ProxyEndpoint response.

Consider the following advice when attaching the MessageLogging policy to your API proxy:

     * Place the policy in a [FaultRule](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling#creatingfaultrules). FaultRule is the recommended location to log security security exceptions and policy violations. 
     * Place the policy in the PostFlow. PostFlow is another suitable location to log security issues. 
     * Avoid logging successful requests. For security monitoring focused on threats, you typically log details when something goes wrong (a fault is raised). Logging every successful request with full message content can generate excessive logs and increase costs. 
     * Consider custom variables for certain use cases. For example, if you need to capture the original request URI in a fault flow, you can use the AssignMessage policy in the request PreFlow to copy it to a custom variable (such as `original.request.uri`), and then log that variable in the MessageLogging policy.



## Best practices

Consider these best practices when configuring Apigee with Google SecOps: 

  * **Focus on the security context:** Log only the flow variables that provide valuable context for security monitoring and threat detection. Avoid excessive logging of non-security-related data. 
  * **Use a consistent logging format:** Maintain a consistent logging format across your API proxies that use SecOps. 
  * **Use secure service accounts:** Adhere to security best practices for managing and securing the Google Cloud service account used for SecOps ingestion. If possible, limit permission to Logs Viewer. 
  * **Monitor the SecOps feed:** Regularly monitor the health and status of your SecOps feed to ensure logs are being ingested successfully and without errors. 
  * **Use SecOps rules and dashboards:** Once security-relevant logs are in SecOps, develop specific rules and dashboards to detect and visualize security threats based on the detailed information you are logging. 



##  **Troubleshooting**

This section describes several possible issues that you may encounter when configuring Apigee with SecOps and things to check for. 

### Issue: Security event logs do not appear in Cloud Logging

Things to check: 

  * Double-check that your MessageLogging Policy is correctly configured with the `Condition` to trigger when a security event occurs. 
  * Ensure the MessageLogging policy is attached to the appropriate flow context, such as a FaultRule or PostFlow. 
  * Verify that Cloud Logging is enabled in your Google Cloud project. 
  * Review any error messages in your Apigee proxy logs related to the MessageLogging Policy.



### Issue: Security event logs do not appear in SecOps

  * Verify that your SecOps feed is configured correctly with the correct project ID, log filter (ensuring it captures the logs from your security logging policy), and service account credentials. 
  * Check the status of your SecOps feed in the SecOps UI for any error messages or ingestion issues. 
  * Ensure the service account used by SecOps has the Logs Viewer role on your Google Cloud project.



### Security-Related Fields Not Parsed Correctly in SecOps

  * Review the JSON structure of your logs in Cloud Logging to ensure they are well-formed and contain the expected field names.
  * Confirm that the appropriate Google Cloud parser is enabled.
  * If you suspect a parsing issue, examine a sample log entry in the SecOps raw data to see how it was ingested before parsing. If specific fields are not being extracted as expected, you might need to review the SecOps parser documentation or consider if a custom parser is necessary.



## Integrate Apigee with Google SecOps SIEM

The following table maps Apigee flow variable names to equivalent Google SecOps SIEM field names. For example, when viewing Apigee log data in Cloud Logging, the `client.id` flow variable maps to the SecOps SIEM field called `principle_ip`. See also [Collect Apigee logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-gcp-apigee-x).

Apigee flow variable | SecOps SIEM field name | Description  
---|---|---  
client.country | principal.hostname | The HTTP host IP associated with the request received by the ProxyEndpoint.  
client.host | principal.location.country_or_region | The country in the TLS/SSL certificate presented by the client app. Proxy request `principal.location.country_or_region`.  
client.ip | principle.ip | The IP address of the client or system sending the message to the load balancer. For example, this could be the original client IP or a load balancer IP.  
client.locality | principal.location.city | The locality (City) in the TLS/SSL certificate presented by the client.  
client.port | principal.port | The HTTP port associated with the originating client request to the ProxyEndpoint.  
client.state | principal.location.state | The state in the TLS/SSL certificate presented by the client.  
organization.name | intermediary.cloud.project.name | Name of the Apigee organization.  
proxy.client.ip | src.ip | The `X-Forwarded-For` address of the inbound call, which is the IP address Apigee received from the last external TCP handshake. This could be the calling client or a load balancer.  
proxy.name | intermediary.resource.name | The name attribute configured for the ProxyEndpoint.  
proxy.pathsuffix | intermediary.resource.attribute.labels[pathsuffix] | "The value of the path suffix in the URL that is sent from the client and received at the ProxyEndpoint. The basepath is the left-most path component that uniquely identifies an API proxy within an Environment Group. Suppose that you have an API Proxy endpoint configured with a basepath of /v2/weatherapi. In that case, a request sent to https://myhost.example.net/v2/weatherapi/forecastrss?w=12797282, the proxy.pathsuffix variable will hold the string /forecastrss."  
proxy.url | intermediary.url | "Gets the complete URL associated with the proxy request received by the ProxyEndpoint, including any query parameters present. For an example that constructs a request URL using the original request host (rather than the router host used in proxy.url), see Access request messages."  
request.uri | target.resource.name | The domain name of the target service that returns the response to the API proxy.  
request.verb | network.http.method | The HTTP verb used for the request. For example, GET, PUT, and DELETE.  
response.content | security_result.description  | Payload content of the response message returned by the target.  
response.status.code | network.http.response_code | The response code returned for a request. You can use this variable to override the response status code, which is stored in message.status.code. For more, see message.  
system.region.name | intermediary.location.name | The name of the data center region where the proxy is running.  
system.timestamp | additional.fields[jsonPayload_system_timestamp] | The 64-bit (long) integer representing the time that this variable was read. The value is the number of milliseconds elapsed since midnight, on January 1, 1970 UTC. For example, 1534783015000.  
system.uuid | intermediary.process.pid or intermediary.process.product_specific_process_id | The UUID of the message processor handling the proxy.  
target.country | target.location.country_or_region | Country of the TLS/SSL certificate presented by the target server  
target.host | target.hostname | The domain name of the target service that returns the response to the API proxy.  
target.ip | target.ip | The IP address of the target service that returns the response to the API proxy.  
target.locality | target.location.city | Locality (city) of the TLS/SSL certificate presented by the target server  
target.organization | target.resource_ancestors.name | Organization of the TLS/SSL certificate presented by the target server.  
target.port | target.port | The port number of the target service that returns the response to the API proxy.  
target.scheme | target.network.application_protocol | Returns HTTP or HTTPS depending on the request message.   
target.state | target.location.state | State of the TLS/SSL certificate presented by the target server.   
target.url | target.url | The URL configured in the TargetEndpoint XML file or the dynamic target URL (if target.url is set during the message flow). The variable does not include any additional path elements or query parameters. Returns null if called out of scope or otherwise unset.  
  
Note: Use a JavaScript policy attached to the TargetEndpoint to set this variable.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
