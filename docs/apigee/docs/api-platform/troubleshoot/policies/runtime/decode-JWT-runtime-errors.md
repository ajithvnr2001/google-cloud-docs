---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/decode-JWT-runtime-errors/
title: Decode JWT runtime error troubleshooting \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:59:54.553747+00:00
---

# Decode JWT runtime error troubleshooting  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/decode-JWT-runtime-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Decode JWT runtime error troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/troubleshoot/policies/runtime/decode-JWT-runtime-errors) documentation._

**Note:** Was this troubleshooting playbook helpful? Please let us know by clicking [ Send Feedback ](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/decode-JWT-runtime-errors/).

## FailedToDecode

### Error code
    
    
    steps.jwt.FailedToDecode
    

### Error response body
    
    
    {
      "fault": {
        "faultstring": "Failed to Decode Token: policy({0})",
        "detail": {
           "errorcode": "steps.jwt.FailedToDecode"
         }
      }
    }
    

### Cause

This error occurs if the [JSON Web Token](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/jwt-policies-overview) (JWT) specified in the `<Source>` element of the Decode JWT policy is malformed, invalid or otherwise not decodable.

A properly structured JWT should contain a header, payload and signature in the following format: `header.payload.signature`. If the JWT passed to the DecodeJWT policy is missing a component part, then you will get the error. For example, if the JWT has only `payload.signature`, but is missing its `header`, the error will occur.

### Diagnosis

  1. Identify the variable specified in the `<Source>` element of the Decode JWT policy. This variable should contain the JWT.

Here's a sample Decode JWT policy:
         
         <DecodeJWT name="JWT-Decode-HS256">
             <DisplayName>JWT Verify HS256</DisplayName>
             <Source>request.header.authorization</Source>
             <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
         </DecodeJWT>
         

In the above example, the JWT should be contained in the Authorization request header.

  2. Examine the variable identified in Step 1 and check to see if the JWT it contains is valid. If the input JWT is not valid, then that's the cause for the error.

In the example API request below, the input JWT is passed in the Authorization request header:
         
         curl -v "http://**$EXTERNAL_IP** /v1/decodeJWT" -H "Authorization: Bearer eyJ1c2VySWQiOiJiMDhmODZhZi0zNWRhLTQ4ZjItOGZhYi1jZWYzOTA0NjYwYmQifQ.-xN_h82PHVTCMA9vdoHrcZxH-x5mb11y1537t3rGzcM"
         

Where `**$EXTERNAL_IP**` is the IP address of the external load balancer. This IP address is exposed to the internet. For more information, see [Customize access routing](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/configure-routing#external-access). 

Close examination of the JWT shows that it has the format `payload.signature` which is invalid. The expected format of the JWT is `header.payload.signature`. As a result, the Decode JWT policy fails with the error :
         
         "faultstring": "Failed to Decode Token: policy({0})"
         




### Resolution

Ensure that the JWT passed to the Decode JWT policy contains all three elements, is correctly formatted and is decodable.

To correct the example shown above, you can pass in a valid JWT with the format `header.payload.signature`. This can be done by making the API call using the cURL command as follows:
    
    
    curl -v "http://**$EXTERNAL_IP** /v1/decodeJWT" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOiJiMDhmODZhZi0zNWRhLTQ4ZjItOGZhYi1jZWYzOTA0NjYwYmQifQ.-xN_h82PHVTCMA9vdoHrcZxH-x5mb11y1537t3rGzcM"
    

Where `**$EXTERNAL_IP**` is the IP address of the external load balancer. This IP address is exposed to the internet. For more information, see [Customize access routing](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/configure-routing#external-access). 

## InvalidToken

### Error code
    
    
    steps.jwt.InvalidToken
    

### Error response body
    
    
    {
      "fault": {
        "faultstring": "Invalid token: policy({0})",
        "detail": {
          "errorcode": "steps.jwt.InvalidToken"
         }
      }
    }
    

### Cause

This error occurs if the flow variable specified in the `<Source>` element of the Decode JWT policy is:

  * out of scope (not available in the specific flow where the policy is being executed) or
  * can't be resolved (is not defined)



### Diagnosis

  1. Identify the variable specified in the `<Source>` element of the Decode JWT policy. This variable should contain the JWT.

Here's a sample Decode JWT policy:
         
         <DecodeJWT name="JWT-Decode-HS256">
             <DisplayName>JWT Verify HS256</DisplayName>
             <Source>request.header.authorization</Source>
             <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>
         </DecodeJWT>
         

In the example above, the Authorization request header should contain the JWT.

  2. Determine if the variable identified in Step 1 is defined and available in the flow in which the Decode JWT policy is executed.

  3. If the variable is either:

     * out of scope (not available in the specific flow where the policy is being executed) or
     * can't be resolved (is not defined)

then that's the cause for the error.

In the example API request below, the JWT is not passed in the authorization request header by the user.
    
    curl -v "http://**$EXTERNAL_IP** /v1/decodeJWT"
    




Where `**$EXTERNAL_IP**` is the IP address of the external load balancer. This IP address is exposed to the internet. For more information, see [Customize access routing](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/configure-routing#external-access). 
    
    
    Because the authorization request header is not passed, the Decode JWT policy fails with the error:
    
    ```
    "faultstring": "Invalid token: policy({0})"
    ```
    

### Resolution

Ensure that the variable referenced in the `<Source>` element of the Decode JWT policy is defined, contains a valid (decodable) JWT and is available in the specific flow where the Decode JWT policy is being executed.

To correct the example shown above, you can pass a valid JWT in the request authorization header. This can be done by making the API call using the cURL command as follows:
    
    
    curl -v "http://**$EXTERNAL_IP** /v1/decodeJWT" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOiJiMDhmODZhZi0zNWRhLTQ4ZjItOGZhYi1jZWYzOTA0NjYwYmQifQ.-xN_h82PHVTCMA9vdoHrcZxH-x5mb11y1537t3rGzcM"
    

Where `**$EXTERNAL_IP**` is the IP address of the external load balancer. This IP address is exposed to the internet. For more information, see [Customize access routing](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/configure-routing#external-access). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
