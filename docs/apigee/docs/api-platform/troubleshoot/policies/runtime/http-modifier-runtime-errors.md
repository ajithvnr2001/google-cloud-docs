---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/http-modifier-runtime-errors/
title: HTTPModifier runtime error troubleshooting \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:35:24.455253+00:00
---

# HTTPModifier runtime error troubleshooting  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/http-modifier-runtime-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)



Send feedback 

#  HTTPModifier runtime error troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_There is no equivalent[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/get-started) documentation for this topic._

**Note:** Was this troubleshooting playbook helpful? Please let us know by clicking [ Send Feedback ](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/http-modifier-runtime-errors/).

## UnresolvedVariable

### Error code
    
    
    steps.httpmodifier.UnresolvedVariable
    

### Error response body
    
    
    {
        "fault": {
            "faultstring": "HTTPModifier[policy_name]: unable to resolve variable [variable_name]",
            "detail": {
                "errorcode": "steps.httpmodifier.UnresolvedVariable"
            }
        }
    }

### Cause

This error occurs if a variable specified in the [HTTPModifier policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy) is either:

  * out of scope (not available in the specific flow where the policy is being executed) or
  * can't be resolved (is not defined)



### Diagnosis

  1. Identify the HTTPModifier policy where the error occurred and the name of the variable that is not available. You can find both of these items in the `faultstring` element of the error response.

For example, in the following `faultstring`, the policy name is `googleBook` and the variable is `var`:
         
         "faultstring": "HTTPModifier[googleBook]: unable to resolve variable var"
         

  2. In the failed HTTPModifier policy XML, verify that the name of the variable used matches the variable name identified in the fault string (step #1 above). 

  3. Determine if the variable is defined and available in the flow in which the HTTPModifier policy is being executed.

  4. If the variable is either:

     1. out of scope (not available in the specific flow where the policy is being executed) or
     2. can't be resolved (is not defined)

then that's the cause for the error.

Check if the variable is defined in any of the policies that are executed before the HTTPModifier policy in the request flow. If the variable has not been defined, then you will receive the error code:
    
    steps.httpmodifier.UnresolvedVariable
    




### Resolution

Ensure that the variable referenced in the policy exists and is available in the specific flow, where the HTTPModifier policy is being executed.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
