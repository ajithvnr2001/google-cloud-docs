---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/reset-quota-runtime-errors/
title: Reset Quota runtime error troubleshooting \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:22:31.995731+00:00
---

# Reset Quota runtime error troubleshooting  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/reset-quota-runtime-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Reset Quota runtime error troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/troubleshoot/policies/runtime/reset-quota-runtime-errors) documentation._

**Note:** Was this troubleshooting playbook helpful? Please let us know by clicking [ Send Feedback ](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/reset-quota-runtime-errors/).

## InvalidRLPolicy

### Error code
    
    
    policies.resetquota.InvalidRLPolicy
    

### Error response body
    
    
    {
        "fault": {
            "faultstring": "Invalid rate limit policy quota_policy_name",
            "detail": {
                "errorcode": "policies.resetquota.InvalidRLPolicy"
            }
        }
    }

### Example error message
    
    
    {
        "fault": {
            "faultstring": "Invalid rate limit policy MyQuotaPolicy",
            "detail": {
                "errorcode": "policies.resetquota.InvalidRLPolicy"
            }
        }
    }
    

### Cause

This error occurs if the Quota policy specified in the `<Quota>` element of the Reset Quota policy is not defined in the API proxy. The `<Quota>` element is mandatory and it identifies the target Quota policy whose counter should be updated through the Reset Quota policy. This target Quota policy must be created and defined within the same API proxy and has to be available during the flow.

For example, let's say the`<Quota>` element is defined as seen below, but if `MyQuotaPolicy` is not defined in the API Proxy then you get the above error.
    
    
    <Quota name="MyQuotaPolicy">
    

### Diagnosis

  1. Identify the invalid Quota policy name specified in the Reset Quota policy. You can find the name of the Quota policy from the faultstring. For example, in the following faultstring, the Quota policy name is `MyQuotaPolicy:`
         
         "faultstring": "Invalid rate limit policy MyQuotaPolicy"
         

  2. Examine each of the Reset Quota policies in the API Proxy where the failure has occurred. Identify the specific Reset Quota policy where the Quota policy specified within the mandatory element `<Quota>` matches with the name identified in Step 1 above.

For example, the following Reset Quota policy specifies a Quota policy named `MyQuotaPolicy`, which matches what's in the faultstring:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
             <ResetQuota async="false" continueOnError="false" enabled="true" name="Reset_Quota_Demo">
             <DisplayName>Reset_Quota_Demo</DisplayName>
             <Properties/>
             <Quota name="MyQuotaPolicy">
                <Identifier name="identifierName" ref="request.header.identifier">
                     <Allow>100</Allow>
                 </Identifier>
             </Quota>
         </ResetQuota>
         
         

  3. Determine if this Quota policy is created and defined within the same API proxy. If the Quota policy doesn't exist within the same API proxy, then that's the cause of the error.

In the example shown above, the Quota policy `MyQuotaPolicy` is supposed to exist in the flow before the Reset Quota policy `Reset_Quota_Demo` executes.

Because the Quota Policy `MyQuotaPolicy` doesn't exist in the flow, you will receive the error code:



    
    
    "errorcode": "policies.resetquota.InvalidRLPolicy"
    

### Resolution

Ensure that the Quota Policy declared in the `<Quota>` element is defined in the API proxy. This target Quota policy has to be available when the Reset Quota policy executes.

## FailedToResolveAllowCountRef

### Error code
    
    
    policies.resetquota.FailedToResolveAllowCountRef
    

### Error response body
    
    
    Failed to resolve allow count reference reference_name for identifier identifier_name
    in ResetQuotaStepDefinition:policy_name;API Proxy:proxy_name;Revision:
    revision_number;Environment:env_name;Organization:org_name

### Example error message
    
    
    Failed to resolve allow count reference request.header.allowcount for identifier
    identifierName in ResetQuotaStepDefinition:ResetQuota;API Proxy:Reset_Quota;
    Revision:10;Environment:test;Organization:demo
    

**Note** : The above error message is not sent as a response to the client. It is seen only in the Trace tool as an error from the Reset Quota policy. A sample screenshot is shown below.

![Under Properties, the error row is populated with a message.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/reset-quota-runtime-error.png)

The error returned to the client will be simply: `policies.ratelimit.QuotaViolation`.

### Cause

This error occurs if the reference to the variable containing the allow count in the `<Allow>` element of the policy cannot be resolved to a value. This element is mandatory and specifies the amount to decrease the quota counter.

### Diagnosis

  1. Identify the Reset Quota policy where the error has occurred and the name of the reference variable that cannot be resolved. You can find both of these items in the error response.

For example, in the following faultstring, the policy name is `ResetQuota` and the reference is `request.header.allowcount`:
         
         Failed to resolve allow count reference request.header.allowcount for identifier
         identifierName in ResetQuotaStepDefinition:ResetQuota;API Proxy:Reset_Quota;
         Revision:10;Environment:test;Organization:demo
         

  2. In the failed Reset Quota policy XML, verify that the name of the reference variable used matches the reference name identified in the error response (Step 1 above).

For example, the following policy sets the element with the reference named `request.header.allowcount`, which matches what's in the error:
         
         <ResetQuota async="false" continueOnError="false" enabled="true" name="ResetQuota">
             <DisplayName>ResetQuota</DisplayName>
             <Properties/>
             <Quota name="MyQuotaPolicy">
                 <Identifier name="identifierName">
                     <Allow ref="request.header.allowcount"/>
                 </Identifier>
             </Quota>
         </ResetQuota>
         

  3. Determine if the reference variable is defined and available in the flow in which the Reset Quota policy executes.

  4. If the variable is either:

     1. out of scope (not available in the specific flow where the policy is being executed) or
     2. can't be resolved (is not defined)

then that's the cause of the error.

In the example shown above, the value of the allowed count in the `<Allow>`element is supposed to be retrieved from the request header named **allowcount**. However, Apigee is unable to resolve the **request.header.allowcount**. This happens if the header **allowcount** is not passed as part of the API request.

Here's a sample API request that does not pass the header **allowcount** as part of the request:
    
    curl -v http://your_host_alias/v1/reset_quota -H "Content-Type: application/json"
    

Where your_host_alias is a publicly facing domain used to access your APIs, as configured in the `virtualhosts.hostAliases` property in your overrides file. See [Specify configuration overrides](https://docs.cloud.google.com/apigee/docs/hybrid/latest/2-6-install-configure-cluster#specify-configuration-overrides).

Because the header **allowcount** is not passed as part of the request, the variable **request.header.allowcount** used in the element `<Allow>` in the above Reset Quota policy is undefined and therefore cannot be resolved. So you will receive the error response:
    
    Failed to resolve allow count reference request.header.allowcount for identifier
    identifierName in ResetQuotaStepDefinition:ResetQuota;API Proxy:Reset_Quota;
    Revision:10;Environment:test;Organization:demo
    




### Resolution

Ensure that the variable referenced in the `<Allow>` element exists/is defined and available in the specific flow, where the Reset Quota policy executes.

To correct the example shown above, you can modify the request to include the **allowcount** header as shown below:
    
    
    curl -v http://your_host_alias/v1/reset_quota -H "Content-Type: application/json" -H "allowcount:30"
    

Where your_host_alias is a publicly facing domain used to access your APIs, as configured in the `virtualhosts.hostAliases` property in your overrides file. See [Specify configuration overrides](https://docs.cloud.google.com/apigee/docs/hybrid/latest/2-6-install-configure-cluster#specify-configuration-overrides).

## FailedToResolveRLPolicy

### Error code
    
    
    policies.resetquota.FailedToResolveRLPolicy
    

### Error response body
    
    
    {
        "fault": {
            "faultstring": "Failed to resolve rate limit policy",
            "detail": {
                "errorcode": "policies.resetquota.FailedToResolveRLPolicy"
            }
        }
    }
    

### Example error message
    
    
    {
        "fault": {
            "faultstring": "Failed to resolve rate limit policy",
            "detail": {
                "errorcode": "policies.resetquota.FailedToResolveRLPolicy"
            }
        }
    }
    

### Cause

This error occurs if the variable referenced by the `ref` attribute in the `<Quota>` element cannot be resolved.

For example, if the `ref` attribute is set as `request.header.quotapolicy` in the `<Quota>` element but is not available in the API proxy flow, then you get the above error.
    
    
    <Quota ref="request.header.quotapolicy">
    

### Diagnosis

  1. Examine each of the Reset Quota policies in the API Proxy where the failure occurred and identify the Reset Quota policy where the name of the reference variable specified in `<Quota>` element cannot be resolved properly.

**Note:** You could determine the specific Reset Quota policy that is failing by capturing the trace for the failing API request.
  2. Determine if the variable is defined and available in the flow in which the Reset Quota policy executes.

  3. If the variable is either:

     1. out of scope (not available in the specific flow where the policy executes) or
     2. can't be resolved (is not defined)

then that's the cause of the error.

In the example shown below, the name of the target Quota policy is supposed to be retrieved from the request header named **quotapolicy**. However, Apigee is unable to resolve the **request.header.quotapolicy**. This happens if the header **quotapolicy** is not passed as part of the API request.
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <ResetQuota async="false" continueOnError="false" enabled="true" name="Reset_Quota_Demo">
        <DisplayName>Reset_Quota_Demo</DisplayName>
        <Properties/>
        <Quota ref="request.header.quotapolicy">
            <Identifier name="identifierName" ref="request.header.identifier">
                <Allow>100</Allow>
            </Identifier>
        </Quota>
    </ResetQuota>
    

Here's a sample API request that does not pass the header **quotapolicy** as part of the request:
    
    curl -v http://your_host_alias/v1/reset_quota -H "Content-Type: application/json"
    

Where your_host_alias is a publicly facing domain used to access your APIs, as configured in the `virtualhosts.hostAliases` property in your overrides file. See [Specify configuration overrides](https://docs.cloud.google.com/apigee/docs/hybrid/latest/2-6-install-configure-cluster#specify-configuration-overrides).

Because the header **quotapolicy** is not passed as part of the request, the reference **request.header.quotapolicy** used in the element `<Quota>` in the above Reset Quota policy is undefined and cannot be resolved. As a result, you receive the error response:
    
    "errorcode": "policies.resetquota.FailedToResolveRLPolicy"
    




### Resolution

Ensure that the attribute `ref` referenced in the `<Quota>` element resolves at runtime and is available in the specific flow, where the Reset Quota policy executes.

To correct the example shown above, you can modify the request to include the **quotapolicy** header as shown below:
    
    
    curl -v http://your_host_alias/v1/reset_quota -H "Content-Type: application/json" -H "quotapolicy:MyQuotaPolicy"
    

Where your_host_alias is a publicly facing domain used to access your APIs, as configured in the `virtualhosts.hostAliases` property in your overrides file. See [Specify configuration overrides](https://docs.cloud.google.com/apigee/docs/hybrid/latest/2-6-install-configure-cluster#specify-configuration-overrides).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
