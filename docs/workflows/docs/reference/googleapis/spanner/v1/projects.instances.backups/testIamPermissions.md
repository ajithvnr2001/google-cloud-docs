---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/spanner/v1/projects.instances.backups/testIamPermissions/
title: Method: googleapis.spanner.v1.projects.instances.backups.testIamPermissions \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:01:21.518308+00:00
---

# Method: googleapis.spanner.v1.projects.instances.backups.testIamPermissions  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/spanner/v1/projects.instances.backups/testIamPermissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Method: googleapis.spanner.v1.projects.instances.backups.testIamPermissions Stay organized with collections  Save and categorize content based on your preferences. 

Returns permissions that the caller has on the specified database or backup resource. Attempting this RPC on a non-existent Cloud Spanner database will result in a NOT_FOUND error if the user has `spanner.databases.list` permission on the containing Cloud Spanner instance. Otherwise returns an empty set of permissions. Calling this method on a backup that does not exist will result in a NOT_FOUND error if the user has `spanner.backups.list` permission on the containing instance. Calling this method on a backup schedule that does not exist will result in a NOT_FOUND error if the user has `spanner.backupSchedules.list` permission on the containing database.

For more information about retries and long-running operations, see [Understand connectors](https://docs.cloud.google.com/workflows/docs/reference/googleapis/spanner/v1/projects.instances.backups/testIamPermissions/).

## Arguments

Parameters  
---  
`resource` |  `string` REQUIRED: The Cloud Spanner resource for which permissions are being tested. The format is `projects//instances/` for instance resources and `projects//instances//databases/` for database resources.  
`body` |  `object ([TestIamPermissionsRequest](https://cloud.google.com/workflows/docs/reference/googleapis/spanner/v1/Overview#TestIamPermissionsRequest))` Required.  
  
## Raised exceptions

Exceptions  
---  
`ConnectionError` | In case of a network problem (such as DNS failure or refused connection).  
`HttpError` | If the response status is >= 400 (excluding 429 and 503).  
`TimeoutError` | If a long-running operation takes longer to finish than the specified timeout limit.  
`TypeError` | If an operation or function receives an argument of the wrong type.  
`ValueError` | If an operation or function receives an argument of the right type but an inappropriate value. For example, a negative timeout.  
  
## Response

If successful, the response contains an instance of [`TestIamPermissionsResponse`](https://cloud.google.com/workflows/docs/reference/googleapis/spanner/v1/Overview#TestIamPermissionsResponse).

## Subworkflow snippet

Some fields might be optional or required. To identify required fields, refer to the [API documentation](https://cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.backups/testIamPermissions).

### YAML
    
    
    - testIamPermissions:
        call: googleapis.spanner.v1.projects.instances.backups.testIamPermissions
        args:
            resource: ...
            body:
                permissions: ...
        result: testIamPermissionsResult

### JSON
    
    
    [
      {
        "testIamPermissions": {
          "call": "googleapis.spanner.v1.projects.instances.backups.testIamPermissions",
          "args": {
            "resource": "...",
            "body": {
              "permissions": "..."
            }
          },
          "result": "testIamPermissionsResult"
        }
      }
    ]

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
