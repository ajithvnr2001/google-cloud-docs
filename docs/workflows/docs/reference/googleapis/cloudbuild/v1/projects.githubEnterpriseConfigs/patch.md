---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/cloudbuild/v1/projects.githubEnterpriseConfigs/patch/
title: Method: googleapis.cloudbuild.v1.projects.githubEnterpriseConfigs.patch \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:02:03.308736+00:00
---

# Method: googleapis.cloudbuild.v1.projects.githubEnterpriseConfigs.patch  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/cloudbuild/v1/projects.githubEnterpriseConfigs/patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Method: googleapis.cloudbuild.v1.projects.githubEnterpriseConfigs.patch Stay organized with collections  Save and categorize content based on your preferences. 

Update an association between a GCP project and a GitHub Enterprise server. This API is experimental.

This method waits—the workflow execution is paused—until the operation is complete, fails, or times out. The default timeout value is `1800` seconds (30 minutes) and can be changed to a maximum value of `31536000` seconds (one year) for long-running operations using the `connector_params` field. See the [Connectors reference](https://docs.cloud.google.com/workflows/docs/reference/googleapis).

The connector uses polling to monitor the long-running operation, which might generate additional billable steps. For more information about retries and long-running operations, refer to [Understand connectors](https://docs.cloud.google.com/workflows/docs/connectors).

The polling policy for the long-running operation can be configured. To set the connector-specific parameters (`connector_params`), refer to [Invoke a connector call](https://docs.cloud.google.com/workflows/docs/reference/googleapis#invoke_a_connector_call).

## Arguments

Parameters  
---  
`name` |  `string` Required. Optional. The full resource name for the GitHubEnterpriseConfig For example: "projects/{$project_id}/githubEnterpriseConfigs/{$config_id}"  
`updateMask` |  `string ([FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask) format)` Update mask for the resource. If this is set, the server will only update the fields specified in the field mask. Otherwise, a full update of the mutable resource fields will be performed.  
`body` |  `object ([GitHubEnterpriseConfig](https://docs.cloud.google.com/workflows/docs/reference/googleapis/cloudbuild/v1/Overview#GitHubEnterpriseConfig))` Required.  
  
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

If successful, the response contains an instance of [`Operation`](https://docs.cloud.google.com/workflows/docs/reference/googleapis/cloudbuild/v1/Overview#Operation).

## Subworkflow snippet

Some fields might be optional or required. To identify required fields, refer to the [API documentation](https://cloud.google.com/build/docs/api/reference/rest/v1/projects.githubEnterpriseConfigs/patch).

### YAML
    
    
    - patch:
        call: googleapis.cloudbuild.v1.projects.githubEnterpriseConfigs.patch
        args:
            name: ...
            updateMask: ...
            body:
                appId: ...
                displayName: ...
                hostUrl: ...
                name: ...
                peeredNetwork: ...
                secrets:
                    oauthClientIdName: ...
                    oauthClientIdVersionName: ...
                    oauthSecretName: ...
                    oauthSecretVersionName: ...
                    privateKeyName: ...
                    privateKeyVersionName: ...
                    webhookSecretName: ...
                    webhookSecretVersionName: ...
                sslCa: ...
                webhookKey: ...
        result: patchResult

### JSON
    
    
    [
      {
        "patch": {
          "call": "googleapis.cloudbuild.v1.projects.githubEnterpriseConfigs.patch",
          "args": {
            "name": "...",
            "updateMask": "...",
            "body": {
              "appId": "...",
              "displayName": "...",
              "hostUrl": "...",
              "name": "...",
              "peeredNetwork": "...",
              "secrets": {
                "oauthClientIdName": "...",
                "oauthClientIdVersionName": "...",
                "oauthSecretName": "...",
                "oauthSecretVersionName": "...",
                "privateKeyName": "...",
                "privateKeyVersionName": "...",
                "webhookSecretName": "...",
                "webhookSecretVersionName": "..."
              },
              "sslCa": "...",
              "webhookKey": "..."
            }
          },
          "result": "patchResult"
        }
      }
    ]

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
