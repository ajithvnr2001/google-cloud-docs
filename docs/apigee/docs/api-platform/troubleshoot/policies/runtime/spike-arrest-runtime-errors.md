---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/spike-arrest-runtime-errors/
title: Spike Arrest policy runtime error troubleshooting \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:35:41.710834+00:00
---

# Spike Arrest policy runtime error troubleshooting  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/spike-arrest-runtime-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Spike Arrest policy runtime error troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/troubleshoot/policies/runtime/spike-arrest-runtime-errors) documentation._

**Note:** Was this troubleshooting playbook helpful? Please let us know by clicking [ Send Feedback ](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/spike-arrest-runtime-errors/).

## InvalidMessageWeight

### Error code
    
    
    policies.ratelimit.InvalidMessageWeight
    

### Error response body
    
    
    {
        "fault": {jdoe
            "faultstring": "Invalid message weight value [invalid_value]",
            "detail": {
                "errorcode": "policies.ratelimit.InvalidMessageWeight"
            }
        }
    }

**Example Error Message**
    
    
    {
        "fault": {
            "faultstring": "Invalid message weight value **1.5** ",
            "detail": {
                "errorcode": "policies.ratelimit.InvalidMessageWeight"
            }
        }
    }

### Cause

This error occurs if the value specified for the `<MessageWeight>` element through a flow variable is invalid (a non-integer value).

For example, if the value of the flow variable specified for the `<MessageWeight>` element is 1.5 (a non-integer value), then the error occurs.

### Diagnosis

  1. Identify the invalid value used for the `<MessageWeight>` element in the Spike Arrest policy. You can find this information in the `faultstring` element of the error response. For example, in the following error, the invalid value used for `<MessageWeight>` element is `1.5`:
         
         "faultstring": "Invalid message weight value 1.5"
         

  2. Examine all the Spike Arrest policies in the specific API Proxy where the failure has occurred. There could be one or more Spike Arrest policies in which the `<MessageWeight>` element is specified.

For example, the following policy specifies the value of `<MessageWeight>` through a flow variable called `message_weight:`
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
             <SpikeArrest async="false" continueOnError="false" enabled="true" name="SpikeArrest_AuthProxy">
             <DisplayName>SpikeArrest_AuthProxy</DisplayName>
             <Properties/>
             <Identifier ref="request.header.some-header-name"/>
             <Rate>100ps</Rate>
             <MessageWeight ref="message_weight"/>
         </SpikeArrest>
         

  3. Determine the value of the variable used in the `<MessageWeight>` element of the identified Spike Arrest Policy(ies). The value of the flow variable can be extracted from HTTP headers, query parameters, an XML or JSON request payload, or defined in another policy.

     1. Locate the code within the API proxy, where the variable was defined first.
     2. Once you figure out the policy in which the variable is defined and populated first, check how the value for the variable is set.
     3. If the value of the flow variable matches the value identified in Step #1 above, then that's the cause of the error.

For example, assume that a JavaScript policy is used before the Spike Arrest Policy to set the variable `message_weight` based on the request method as shown below:
    
    var verb = context.getVariable("request.verb");
    context.setVariable("message_weight", "1.5");
    if (verb == 'POST') {
      context.setVariable("message_weight", "2");
    }
    

Notice that the value of the variable `message_weight` is `1.5` which is invalid (a non-integer) value.




### Resolution

Ensure that the value of the `MessageWeight` element is a valid value (integer value).

To correct the example shown above, you can modify the value of the variable `message_weight` in the JavaScript to be an integer:
    
    
    var verb = context.getVariable("request.verb");
    context.setVariable("message_weight", "1");
    if (verb == 'POST') {
      context.setVariable("message_weight", "2");
    }
    

## FailedToResolveSpikeArrestRate

### Error code
    
    
    policies.ratelimit.FailedToResolveSpikeArrestRate
    

### Error response body
    
    
    {
        "fault": {
            "faultstring": "Failed to resolve Spike Arrest Rate reference [reference] in SpikeArrest policy [api_policy]",
            "detail": {
                "errorcode": "policies.ratelimit.FailedToResolveSpikeArrestRate"
            }
        }
    }

**Example Error Message**
    
    
    {
        "fault": {
            "faultstring": "Failed to resolve Spike Arrest Rate reference **request.header.rate** in SpikeArrest policy **SpikeArrest_AuthProxy** ",
            "detail": {
                "errorcode": "policies.ratelimit.FailedToResolveSpikeArrestRate"
            }
        }
    }

### Cause

This error occurs if the reference to the variable containing the rate setting within the `<Rate>` element cannot be resolved to a value within the Spike Arrest policy. This element is mandatory and used to specify the spike arrest rate in the form of `{int}pm` or `{int}ps`. For example, `{int}pm` might be `500pm`, which means 500 calls per minute. Likewise, a value of `10ps` means 10 calls per second.

### Diagnosis

  1. Identify the Spike Arrest policy where the error occurred and the name of the reference that cannot be resolved properly. You can find both of these items in the faultstring element of the error response.

For example, in the following faultstring, the policy name is `SpikeArrest_AuthProxy` and the reference is `request.header.rate`:
         
         "faultstring": "Failed to resolve Spike Arrest Rate reference request.header.rate in SpikeArrest policy SpikeArrest_AuthProxy"
         

  2. In the failed Spike Arrest policy XML, verify that the name of the reference used matches the reference name identified in the fault string (step #1 above). ** **

For example, the following policy sets the `<Rate>` element with the reference named `request.header.rate`, which matches what's in the faultstring:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
             <SpikeArrest async="false" continueOnError="false" enabled="true" name="SpikeArrest_AuthProxy">
             <DisplayName>SpikeArrest_AuthProxy</DisplayName>
             <Properties/>
             <Identifier ref="request.header.some-header-name"/>
             <Rate ref="request.header.rate"/>
         </SpikeArrest>
         
         

  3. Determine if the variable is defined and available in the flow in which the Spike Arrest policy is being executed.

  4. If the variable is either:

     * out of scope (not available in the specific flow where the policy is being executed) or
     * can't be resolved (is not defined)

then that's the cause for the error.

In the example shown above, the value of the spike arrest rate in the `<Rate>` element is supposed to be retrieved from the request header named **rate**. However, Apigee is unable to resolve the **request.header.rate**. This happens if the header **rate** is not passed as part of the API request.

Here's a sample API request that does not pass the header **rate** as part of the request:
    
    curl -v http://your_host_alias/check_spikearrest -H "Content-Type: application/json"
    

Where your_host_alias is a publicly facing domain used to access your APIs, as configured in the `virtualhosts.hostAliases` property in your overrides file. See [Specify configuration overrides](https://docs.cloud.google.com/apigee/docs/hybrid/latest/2-6-install-configure-cluster#specify-configuration-overrides).

Since the header **rate** is not passed as part of the request, reference **request.header.rate** used in the element `<Rate>` in the above Spike Arrest policy is undefined and hence cannot be resolved. So you will receive the error code:
    
    policies.ratelimit.FailedToResolveSpikeArrestRate
    




### Resolution

Ensure that the variable referenced in the `<Rate>` element exists/is defined and available in the specific flow, where the Spike Arrest policy is being executed.

To correct the example shown above, you can modify the request to include the **rate** header as shown below:
    
    
    curl -v  http://your_host_alias/check_spikearrest -H "Content-Type: application/json" -H "rate:30ps"
    

Where your_host_alias is a publicly facing domain used to access your APIs, as configured in the `virtualhosts.hostAliases` property in your overrides file. See [Specify configuration overrides](https://docs.cloud.google.com/apigee/docs/hybrid/latest/2-6-install-configure-cluster#specify-configuration-overrides).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
