---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/decode-JWT-deployment-errors/
title: DecodeJWT policy deployment error troubleshooting \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:59:00.706351+00:00
---

# DecodeJWT policy deployment error troubleshooting  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/decode-JWT-deployment-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  DecodeJWT policy deployment error troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/troubleshoot/policies/deployment/decode-JWT-deployment-errors) documentation._

Was this troubleshooting playbook helpful? Please let us know by clicking [ Send Feedback ](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/decode-JWT-deployment-errors/).

## InvalidEmptyElement

### Error message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision
    Invalid empty element : policy(policy_name) element(Source)

### Example error message
    
    
    Error Saving Revision
    Invalid empty element : policy(Decode_JWT) element(Source).
    

### Example screenshot

In the Apigee UI, you will see a dialog box with an error:

![Error saving revision.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/decodeJWT-deploy-error.png)

### Cause

This error occurs if the flow variable containing JWT that is to be decoded is not specified in the `<Source>` element of the DecodeJWT policy.

For example, the error will occur if the `<Source>` element does not contain a value, as shown below:
    
    
    <Source></Source>
    

### Diagnosis

  1. Identify the name of the DecodeJWT policy and name of the element that is empty from the error message. For example, in the following error message, the name of DecodeJWT policy is `Decode_JWT` and the element name is `Source`.
         
         Invalid empty element : policy(Decode_JWT) element(Source).

  2. Examine the DecodeJWT policy and verify if the element identified in Step 1 is empty. If the element is empty, then that's the cause of the error.

Here's a sample DecodeJWT policy:
         
         <DecodeJWT name="Decode_JWT">
             <DisplayName>JWT Decode HS256</DisplayName>
             <Source></Source>
             <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
         </DecodeJWT>
         

Because the `<Source>` element is empty, you get the error:
         
         Invalid empty element : policy(Decode_JWT) element(Source).
         




### Resolution

Ensure that the `<Source>` element specifies a valid JWT in a flow variable.

To fix the issue with the sample DecodeJWT policy, you can specify the flow variable containing a valid JWT in the `<Source>` element.
    
    
    <DecodeJWT name="Decode_JWT">
        <DisplayName>JWT Decode HS256</DisplayName>
        <Source>var.jwt</Source>
        <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
    </DecodeJWT>
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
