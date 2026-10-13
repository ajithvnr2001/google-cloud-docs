---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/compute/beta/organizationSecurityPolicies/insert/
title: Method: googleapis.compute.beta.organizationSecurityPolicies.insert \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:37:13.660593+00:00
---

# Method: googleapis.compute.beta.organizationSecurityPolicies.insert  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/compute/beta/organizationSecurityPolicies/insert/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Method: googleapis.compute.beta.organizationSecurityPolicies.insert Stay organized with collections  Save and categorize content based on your preferences. 

Creates a new policy in the specified project using the data included in the request.

This method waits—the workflow execution is paused—until the operation is complete, fails, or times out. The default timeout value is `1800` seconds (30 minutes) and can be changed to a maximum value of `31536000` seconds (one year) for long-running operations using the `connector_params` field. See the [Connectors reference](https://docs.cloud.google.com/workflows/docs/reference/googleapis).

The connector uses polling to monitor the long-running operation, which might generate additional billable steps. For more information about retries and long-running operations, refer to [Understand connectors](https://docs.cloud.google.com/workflows/docs/connectors).

The polling policy for the long-running operation can be configured. To set the connector-specific parameters (`connector_params`), refer to [Invoke a connector call](https://docs.cloud.google.com/workflows/docs/reference/googleapis#invoke_a_connector_call).

## Arguments

Parameters  
---  
`parentId` |  `string` Parent ID for this request. The ID can be either be "folders/[FOLDER_ID]" if the parent is a folder or "organizations/[ORGANIZATION_ID]" if the parent is an organization.  
`requestId` |  `string` An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported ( 00000000-0000-0000-0000-000000000000).  
`body` |  `object ([SecurityPolicy](https://docs.cloud.google.com/workflows/docs/reference/googleapis/compute/beta/Overview#SecurityPolicy))` Required.  
  
## Raised exceptions

Exceptions  
---  
`ConnectionError` | In case of a network problem (such as DNS failure or refused connection).  
`HttpError` | If the response status is >= 400 (excluding 429 and 503).  
`TimeoutError` | If a long-running operation takes longer to finish than the specified timeout limit.  
`TypeError` | If an operation or function receives an argument of the wrong type.  
`ValueError` | If an operation or function receives an argument of the right type but an inappropriate value. For example, a negative timeout.  
`OperationError` | If the long-running operation finished unsuccessfully.  
`ResponseTypeError` | If the long-running operation returned a response of the wrong type.  
  
## Response

If successful, the response contains an instance of [`Operation`](https://docs.cloud.google.com/workflows/docs/reference/googleapis/compute/beta/Overview#Operation).

## Subworkflow snippet

Some fields might be optional or required. To identify required fields, refer to the [API documentation](https://cloud.google.com/compute/docs/reference/rest/beta/organizationSecurityPolicies/insert).

### YAML
    
    
    - insert:
        call: googleapis.compute.beta.organizationSecurityPolicies.insert
        args:
            parentId: ...
            requestId: ...
            body:
                adaptiveProtectionConfig:
                    autoDeployConfig:
                        confidenceThreshold: ...
                        expirationSec: ...
                        impactedBaselineThreshold: ...
                        loadThreshold: ...
                    layer7DdosDefenseConfig:
                        enable: ...
                        ruleVisibility: ...
                        thresholdConfigs: ...
                advancedOptionsConfig:
                    jsonCustomConfig:
                        contentTypes: ...
                    jsonParsing: ...
                    logLevel: ...
                    userIpRequestHeaders: ...
                associations: ...
                ddosProtectionConfig:
                    ddosProtection: ...
                description: ...
                displayName: ...
                fingerprint: ...
                labelFingerprint: ...
                labels: ...
                name: ...
                recaptchaOptionsConfig:
                    redirectSiteKey: ...
                rules: ...
                type: ...
                userDefinedFields: ...
        result: insertResult

### JSON
    
    
    [
      {
        "insert": {
          "call": "googleapis.compute.beta.organizationSecurityPolicies.insert",
          "args": {
            "parentId": "...",
            "requestId": "...",
            "body": {
              "adaptiveProtectionConfig": {
                "autoDeployConfig": {
                  "confidenceThreshold": "...",
                  "expirationSec": "...",
                  "impactedBaselineThreshold": "...",
                  "loadThreshold": "..."
                },
                "layer7DdosDefenseConfig": {
                  "enable": "...",
                  "ruleVisibility": "...",
                  "thresholdConfigs": "..."
                }
              },
              "advancedOptionsConfig": {
                "jsonCustomConfig": {
                  "contentTypes": "..."
                },
                "jsonParsing": "...",
                "logLevel": "...",
                "userIpRequestHeaders": "..."
              },
              "associations": "...",
              "ddosProtectionConfig": {
                "ddosProtection": "..."
              },
              "description": "...",
              "displayName": "...",
              "fingerprint": "...",
              "labelFingerprint": "...",
              "labels": "...",
              "name": "...",
              "recaptchaOptionsConfig": {
                "redirectSiteKey": "..."
              },
              "rules": "...",
              "type": "...",
              "userDefinedFields": "..."
            }
          },
          "result": "insertResult"
        }
      }
    ]

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
