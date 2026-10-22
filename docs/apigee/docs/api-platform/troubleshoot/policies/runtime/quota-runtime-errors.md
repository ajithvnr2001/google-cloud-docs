---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/quota-runtime-errors/
title: Quota runtime error troubleshooting \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:36:55.074191+00:00
---

# Quota runtime error troubleshooting  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/quota-runtime-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Quota runtime error troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/troubleshoot/policies/runtime/quota-runtime-errors) documentation._

**Note:** Was this troubleshooting playbook helpful? Please let us know by clicking [ Send Feedback ](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/quota-runtime-errors/).

## InvalidMessageWeight

### Error code
    
    
    policies.ratelimit.InvalidMessageWeight
    

### Error response body
    
    
    {
        "fault": {
            "faultstring": "Invalid message weight value [invalid_value]",
            "detail": {
                "errorcode": "policies.ratelimit.InvalidMessageWeight"
            }
        }
    }
    

**Example Error Message**
    
    
    {
        "fault": {
            "faultstring": "Invalid message weight value 1.5",
            "detail": {
                "errorcode": "policies.ratelimit.InvalidMessageWeight"
            }
        }
    }
    

### Cause

This error occurs if the value of the `<MessageWeight>` element specified through a flow variable is invalid (a non-integer value).

For example, this error will occur if the value of the flow variable specified for the `<MessageWeight>` element is 1.5 (a non-integer value).

### Diagnosis

  1. Identify the invalid value used for the `<MessageWeight>` element in the Quota policy. You can find this information in the `faultstring` element of the error response. For example, in the following error, the invalid value used for `<MessageWeight>` element is `1.5`:
         
         "faultstring": "Invalid message weight value 1.5"
         

  2. Examine all the Quota policies in the specific API Proxy where the failure has occurred. There could be one or more Quota policies in which the `<MessageWeight>` element is specified.

For example, the following policy specifies the `<MessageWeight>`through a flow variable`message_weight`:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
             <Quota async="false" continueOnError="false" enabled="true" name="Quota_with_weight" type="calendar">
             <DisplayName>Quota_with_weight</DisplayName>
             <Properties/>
             <Allow count="3"/>
             <Interval>1</Interval>
             <TimeUnit>minute</TimeUnit>
             <StartTime>2017-7-16 12:00:00</StartTime>
             <MessageWeight ref="message_weight"/>
         </Quota>
         

  3. Determine the value of the variable used for `<MessageWeight>` in the identified Quota Policy(ies). The value of the flow variable can be extracted from HTTP headers, query parameters, an XML or JSON request payload, or defined in another policy:

     1. Locate the code within the API Proxy bundle where the variable was defined first.
     2. Once you figure out the policy in which the variable is defined and populated first, then check how the value for the variable is set.
     3. If the value of the flow variable matches the value identified in Step #1 above, then that's the cause of the error.

For example, assume that a JavaScript policy used before the Quota Policy sets the variable `message_weight` based on the request type as shown below:
    
    var verb = context.getVariable("request.verb");
    context.setVariable("message_weight", "1.5");
    if (verb == 'POST') {
      context.setVariable("message_weight", "2");
    }
    

Notice that the value of the variable `message_weight` is `1.5` which is invalid (a non-integer) value.




### Resolution

Ensure that the value representing the `MessageWeight` specified by the flow variable is a valid value (integer value).

To correct the example shown above, you can modify the value of the variable `message_weight` in the JavaScript to be an integer.
    
    
    var verb = context.getVariable("request.verb");
    context.setVariable("message_weight", "1");
    if (verb == 'POST') {
      context.setVariable("message_weight", "2");
    }
    

## FailedToResolveQuotaIntervalReference

### Error code
    
    
    policies.ratelimit.FailedToResolveQuotaIntervalReference
    

### Error response body
    
    
    {
        "fault": {
            "faultstring": "Failed to resolve quota interval reference [reference] in quota policy {1}",
            "detail": {
                "errorcode": "policies.ratelimit.FailedToResolveQuotaIntervalReference"
            }
        }
    }
    

**Example Error Message**
    
    
    {
        "fault": {
            "faultstring": "Failed to resolve quota interval reference api.product.developer.quota.interval in quota policy {1}",
            "detail": {
                "errorcode": "policies.ratelimit.FailedToResolveQuotaIntervalReference"
            }
        }
    }
    

### Cause

This error occurs if the `<Interval>`element is not defined within the Quota policy. This element is mandatory and used to specify the interval of time applicable to the quota. The time interval can be minutes, hours, days, weeks, or months as defined with the `<TimeUnit>` element.

### Diagnosis

  1. Examine each of the Quota policies in the API Proxy where the failure occurred. If there is any Quota policy where the mandatory element `<Interval>` is not defined, then that's the cause of the error.

For example, the following Quota policy does not have the mandatory element `<Interval>`:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
             <Quota async="false" continueOnError="false" enabled="true" name="CheckQuota" type="calendar">
             <DisplayName>CheckQuota</DisplayName>
             <Properties/>
             <Allow count="3"/>
                 <TimeUnit ref="verifyapikey.verify-api-key.apiproduct.developer.quota.timeunit">hour</TimeUnit>
             <StartTime>2017-7-16 12:00:00</StartTime>
         </Quota>
         

Because the mandatory element `<TimeUnit>` is not defined in the above Quota policy, you will receive the error code:
         
         policies.ratelimit.FailedToResolveQuotaIntervalReference
         




### Resolution

Ensure that all the Quota policies for a given API proxy have the mandatory element `<Interval>` defined properly.

To correct the example shown above, you can modify the policy to include the element `<Interval>` as shown below.``
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <Quota async="false" continueOnError="false" enabled="true" name="CheckQuota" type="calendar">
        <DisplayName>CheckQuota</DisplayName>
        <Properties/>
        <Allow count="3"/>
        <TimeUnit ref="verifyapikey.verify-api-key.apiproduct.developer.quota.timeunit">hour</TimeUnit>
        **< Interval ref="verifyapikey.verify-api-key.apiproduct.developer.quota.interval">1</Interval>**
        <StartTime>2017-7-16 12:00:00</StartTime>
    </Quota>

## FailedToResolveQuotaIntervalTimeUnitReference

### Error code
    
    
    policies.ratelimit.FailedToResolveQuotaIntervalTimeUnitReference
    

### Error response body
    
    
    {
        "fault": {
            "faultstring": "Failed to resolve quota time unit reference [reference] in quota policy {1}",
            "detail": {
                "errorcode": "policies.ratelimit.FailedToResolveQuotaIntervalTimeUnitReference"
            }
        }
    }
    

**Example Error Message**
    
    
    {
        "fault": {
            "faultstring": "Failed to resolve quota time unit reference apiproduct.developer.quota.timeunity in quota policy {1}",
            "detail": {
                "errorcode": "policies.ratelimit.FailedToResolveQuotaIntervalTimeUnitReference"
            }
        }
    }
    

### Cause

This error occurs if the `<TimeUnit>`element is not defined within the Quota policy. This element is mandatory and used to specify the unit of time applicable to the quota. The time interval can be in minutes, hours, days, weeks, or months.

### Diagnosis

  1. Examine each of the Quota policies in the API Proxy where the failure occurred. If there is any Quota policy where the mandatory element `<TimeUnit>` is not defined, then that's the cause of the error.

For example, the following Quota policy does not have the mandatory element `<TimeUnit>`:
         
         <Quota async="false" continueOnError="false" enabled="true" name="CheckQuota" type="calendar">
           <DisplayName>CheckQuota</DisplayName>
           <Properties/>
           <Allow count="3"/>
               <Interval ref="verifyapikey.verify-api-key.apiproduct.developer.quota.interval">1</Interval>
           <StartTime>2017-7-16 12:00:00</StartTime>
         </Quota>
         

Because the mandatory element `<TimeUnit>` is not defined in the above Quota policy, you will receive the error code:
         
         policies.ratelimit.FailedToResolveQuotaIntervalTimeUnitReference
         




### Resolution

Ensure that all the Quota policies for a given API proxy have the mandatory element `<TimeUnit>` defined.

To correct the example shown above, you can modify the policy to include the element `<TimeUnit>` as shown below.``
    
    
    <Quota async="false" continueOnError="false" enabled="true" name="CheckQuota" type="calendar">
        <DisplayName>CheckQuota</DisplayName>
        <Properties/>
        <Allow count="3"/>
        **< TimeUnit ref="verifyapikey.verify-api-key.apiproduct.developer.quota.timeunit">hour</TimeUnit>**
        <Interval ref="verifyapikey.verify-api-key.apiproduct.developer.quota.interval">1</Interval>
        <StartTime>2017-7-16 12:00:00</StartTime>
    </Quota>

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
