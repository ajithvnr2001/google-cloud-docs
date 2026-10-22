---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/access-control-runtime-errors/
title: AccessControl policy runtime error troubleshooting \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:35:25.655413+00:00
---

# AccessControl policy runtime error troubleshooting  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/access-control-runtime-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  AccessControl policy runtime error troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/troubleshoot/policies/runtime/access-control-runtime-errors) documentation._

**Note:** Was this troubleshooting playbook helpful? Please let us know by clicking [ Send Feedback ](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/access-control-runtime-errors/).

## IPDeniedAccess

### Error code
    
    
    accesscontrol.IPDeniedAccess
    

### Error response body
    
    
    {
        "fault": {
            "faultstring": "Access Denied for client ip : client_IP",
            "detail": {
                "errorcode": "accesscontrol.IPDeniedAccess"
            }
        }
    }

### Example error message
    
    
    {
        "fault": {
            "faultstring": "Access Denied for client ip : 104.132.196.83",
            "detail": {
                "errorcode": "accesscontrol.IPDeniedAccess"
            }
        }
    }
    

### Cause

This error occurs if the client IP address, or any IP address passed as part of the API request, matches any IP address(es) specified in the `<SourceAddress>` element within the `<MatchRule>` element of the Access Control Policy, and the `action` attribute of the `<MatchRule>` element is set to `DENY`.

For example, let's say the `<SourceAddress>` is defined as shown below:
    
    
    <SourceAddress mask="32">104.132.196.83</SourceAddress>
    

If the above IP address matches the IP address of the client system (indicated by the variable `proxy.client.ip`), or any of the IP addresses passed as part of the API request, the error will occur.

### Diagnosis

  1. Identify the IP address(es) denied access for a specific API request. You can find this information in the `faultstring` element of the error response.

For example, in the following `faultstring`, the IP address is `104.132.196.83:`
         
         "faultstring": "Access Denied for client ip : 104.132.196.83"
         

  2. Examine all the Access Control policies in the failed API Proxy and determine the specific policy where the IP address(es) specified in the `<SourceAddress>` element matches the IP address(es) identified in the `faultstring` (Step 1 above).

For example, the following policy defines the `<SourceAddress>` IP as `104.132.196.83,` which matches what is in the `faultstring`:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
             <AccessControl async="false" continueOnError="false" enabled="true" name="Access-Control">
             <DisplayName>Access-Control</DisplayName>
             <Properties/>
             <IPRules noRuleMatchAction="ALLOW">
                 <MatchRule action="DENY">
                     <SourceAddress mask="32">104.132.196.83</SourceAddress>
                 </MatchRule>
             </IPRules>
             </AccessControl>
         

  3. Determine the IP address(es) from which the API request was made. This can be done in multiple ways:

     1. Using UI Trace

        1. Capture the trace for the failing API request.
        2. Select the specific Access Control Policy that has failed from the right hand panel.
        3. In the **Phase Details** pane, check the value of the variable `proxy.client.ip` as shown in the following screenshot of a sample trace.

![The Phase Details pane showing the IP address from which the API request was made.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/access-control-runtime-error.png)

        4. If the `proxy.client.ip` is not listed, then check the value of the X-Forwarded-For or True-Client-IP message headers.

     2. Using Custom Reports

You can create Custom Reports to determine whether a 403 status code was thrown during the execution of the Access Control policy within the API proxy and also determine the client IP address. This is particularly useful if the issue has occurred in the past or if the issue is intermittent and you are unable to capture the trace in UI.

Refer to [Creating and managing custom reports](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/create-custom-reports) to understand how to create custom reports. In the custom report, choose:

        1. **Sum of Traffic** as a Metric, and

        2. **Proxy** , **Response Status Code** , **Proxy Client IP** , and **X-Forwarded-For-IP** as Dimensions.

This should help you to determine the client IP or IP addresses passed that led to the error.

  4. If the client IP address (indicated by the variable `proxy.client.ip`), or any IP address passed as part of the API request, matches the IP address(es) specified in the `<SourceAddress>` element within the `<MatchRule>` element of Access Control Policy, where the `action` attribute is set to `DENY`, then that is the cause of the error.

In the example shown above, the value set in the reference variable `proxy.client.ip` (as seen in the screenshot of the trace above) matches the IP address defined in the `<SourceAddress>` element of the Access Control policy, thus triggering the error response:
         
         "faultstring": "Access Denied for client ip : 104.132.196.83"
         
         




### Resolution

If the Access Control policy is intended to deny access to API requests coming from the specific IP address(es) listed in the `faultstring`, then the error message is expected. In this case, there is no additional action is required.

However, if you determine that the specific IP address(es) can be given access to the API requests for the specific API Proxy, then modify the Access Control Policy to allow access to those IP address(es). Alternatively, you can remove the Access Control Policy from the API Proxy if you don't want to deny access to any IP address(es).

Here is an example that shows how to allow access to a specific IP Address `104.132.196.83` only and deny access for the rest:
    
    
    <AccessControl name="ACL">
      <IPRules noRuleMatchAction = "DENY">
        <MatchRule action = "ALLOW">
          <SourceAddress mask="32">104.132.196.83</SourceAddress>
        </MatchRule>
      </IPRules>
    </AccessControl>
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
