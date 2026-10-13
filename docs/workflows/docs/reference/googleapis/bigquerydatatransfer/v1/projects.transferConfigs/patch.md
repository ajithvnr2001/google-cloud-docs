---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/bigquerydatatransfer/v1/projects.transferConfigs/patch/
title: Method: googleapis.bigquerydatatransfer.v1.projects.transferConfigs.patch \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:09:09.932350+00:00
---

# Method: googleapis.bigquerydatatransfer.v1.projects.transferConfigs.patch  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/bigquerydatatransfer/v1/projects.transferConfigs/patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Method: googleapis.bigquerydatatransfer.v1.projects.transferConfigs.patch Stay organized with collections  Save and categorize content based on your preferences. 

Updates a data transfer configuration. All fields must be set, even if they are not updated.

## Arguments

Parameters  
---  
`name` |  `string` The resource name of the transfer config. Transfer config names have the form `projects/{project_id}/locations/{region}/transferConfigs/{config_id}`. Where `config_id` is usually a uuid, even though it is not guaranteed or required. The name is ignored when creating a transfer config.  
`authorizationCode` |  `string` Optional OAuth2 authorization code to use with this transfer configuration. If it is provided, the transfer configuration will be associated with the authorizing user. In order to obtain authorization_code, please make a request to https://www.gstatic.com/bigquerydatatransfer/oauthz/auth?client_id=&scope=&redirect_uri= * client_id should be OAuth client_id of BigQuery DTS API for the given data source returned by ListDataSources method. * data_source_scopes are the scopes returned by ListDataSources method. * redirect_uri is an optional parameter. If not specified, then authorization code is posted to the opener of authorization flow window. Otherwise it will be sent to the redirect uri. A special value of urn:ietf:wg:oauth:2.0:oob means that authorization code should be returned in the title bar of the browser, with the page text prompting the user to copy the code and paste it in the application.  
`serviceAccountName` |  `string` Optional service account name. If this field is set and "service_account_name" is set in update_mask, transfer config will be updated to use this service account credentials. It requires that requesting user calling this API has permissions to act as this service account.  
`updateMask` |  `string ([FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask) format)` Required. Required list of fields to be updated in this request.  
`versionInfo` |  `string` Optional version info. If users want to find a very recent access token, that is, immediately after approving access, users have to set the version_info claim in the token request. To obtain the version_info, users must use the "none+gsession" response type. which be return a version_info back in the authorization response which be be put in a JWT claim in the token request.  
`body` |  `object ([TransferConfig](https://cloud.google.com/workflows/docs/reference/googleapis/bigquerydatatransfer/v1/Overview#TransferConfig))` Required.  
  
## Raised exceptions

Exceptions  
---  
`ConnectionError` | In case of a network problem (such as DNS failure or refused connection).  
`HttpError` | If the response status is >= 400 (excluding 429 and 503).  
`TimeoutError` | If a long-running operation takes longer to finish than the specified timeout limit.  
`TypeError` | If an operation or function receives an argument of the wrong type.  
`ValueError` | If an operation or function receives an argument of the right type but an inappropriate value. For example, a negative timeout.  
  
## Response

If successful, the response contains an instance of [`TransferConfig`](https://cloud.google.com/workflows/docs/reference/googleapis/bigquerydatatransfer/v1/Overview#TransferConfig).

## Subworkflow snippet

Some fields might be optional or required. To identify required fields, refer to the [API documentation](https://cloud.google.com/bigquery-transfer/docs/reference/datatransfer/rest/v1/projects.transferConfigs/patch).

### YAML
    
    
    - patch:
        call: googleapis.bigquerydatatransfer.v1.projects.transferConfigs.patch
        args:
            name: ...
            authorizationCode: ...
            serviceAccountName: ...
            updateMask: ...
            versionInfo: ...
            body:
                dataRefreshWindowDays: ...
                dataSourceId: ...
                destinationDatasetId: ...
                disabled: ...
                displayName: ...
                emailPreferences:
                    enableFailureEmail: ...
                name: ...
                notificationPubsubTopic: ...
                params: ...
                schedule: ...
                scheduleOptions:
                    disableAutoScheduling: ...
                    endTime: ...
                    startTime: ...
                userId: ...
        result: patchResult

### JSON
    
    
    [
      {
        "patch": {
          "call": "googleapis.bigquerydatatransfer.v1.projects.transferConfigs.patch",
          "args": {
            "name": "...",
            "authorizationCode": "...",
            "serviceAccountName": "...",
            "updateMask": "...",
            "versionInfo": "...",
            "body": {
              "dataRefreshWindowDays": "...",
              "dataSourceId": "...",
              "destinationDatasetId": "...",
              "disabled": "...",
              "displayName": "...",
              "emailPreferences": {
                "enableFailureEmail": "..."
              },
              "name": "...",
              "notificationPubsubTopic": "...",
              "params": "...",
              "schedule": "...",
              "scheduleOptions": {
                "disableAutoScheduling": "...",
                "endTime": "...",
                "startTime": "..."
              },
              "userId": "..."
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
