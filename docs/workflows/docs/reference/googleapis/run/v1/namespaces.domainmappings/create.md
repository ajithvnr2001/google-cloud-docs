---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v1/namespaces.domainmappings/create/
title: Method: googleapis.run.v1.namespaces.domainmappings.create \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:01:27.826422+00:00
---

# Method: googleapis.run.v1.namespaces.domainmappings.create  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v1/namespaces.domainmappings/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Method: googleapis.run.v1.namespaces.domainmappings.create Stay organized with collections  Save and categorize content based on your preferences. 

Create a new domain mapping.

## Arguments

Parameters  
---  
`parent` |  `string` Required. The namespace in which the domain mapping should be created. For Cloud Run (fully managed), replace {namespace} with the project ID or number. It takes the form namespaces/{namespace}. For example: namespaces/PROJECT_ID  
`dryRun` |  `string` Indicates that the server should validate the request and populate default values without persisting the request. Supported values: `all`  
`location` |  `string` Location of the HTTP endpoint. For example, `us-central1` or `asia-southeast1`. If not set, the global endpoint https://run.googleapis.com will be used, which supports list methods only. See [service endpoints](https://cloud.google.com/run/docs/reference/rest#service-endpoint) for more location options.  
`body` |  `object ([DomainMapping](https://cloud.google.com/workflows/docs/reference/googleapis/run/v1/Overview#DomainMapping))` Required.  
  
## Raised exceptions

Exceptions  
---  
`ConnectionError` | In case of a network problem (such as DNS failure or refused connection).  
`HttpError` | If the response status is >= 400 (excluding 429 and 503).  
`TimeoutError` | If a long-running operation takes longer to finish than the specified timeout limit.  
`TypeError` | If an operation or function receives an argument of the wrong type.  
`ValueError` | If an operation or function receives an argument of the right type but an inappropriate value. For example, a negative timeout.  
  
## Response

If successful, the response contains an instance of [`DomainMapping`](https://cloud.google.com/workflows/docs/reference/googleapis/run/v1/Overview#DomainMapping).

## Subworkflow snippet

Some fields might be optional or required. To identify required fields, refer to the [API documentation](https://cloud.google.com/run/docs/reference/rest/v1/namespaces.domainmappings/create).

### YAML
    
    
    - create:
        call: googleapis.run.v1.namespaces.domainmappings.create
        args:
            parent: ...
            dryRun: ...
            body:
                apiVersion: ...
                kind: ...
                metadata:
                    annotations: ...
                    clusterName: ...
                    creationTimestamp: ...
                    deletionGracePeriodSeconds: ...
                    deletionTimestamp: ...
                    finalizers: ...
                    generateName: ...
                    generation: ...
                    labels: ...
                    name: ...
                    namespace: ...
                    ownerReferences: ...
                    resourceVersion: ...
                    selfLink: ...
                    uid: ...
                spec:
                    certificateMode: ...
                    forceOverride: ...
                    routeName: ...
                status:
                    conditions: ...
                    mappedRouteName: ...
                    observedGeneration: ...
                    resourceRecords: ...
                    url: ...
        result: createResult

### JSON
    
    
    [
      {
        "create": {
          "call": "googleapis.run.v1.namespaces.domainmappings.create",
          "args": {
            "parent": "...",
            "dryRun": "...",
            "body": {
              "apiVersion": "...",
              "kind": "...",
              "metadata": {
                "annotations": "...",
                "clusterName": "...",
                "creationTimestamp": "...",
                "deletionGracePeriodSeconds": "...",
                "deletionTimestamp": "...",
                "finalizers": "...",
                "generateName": "...",
                "generation": "...",
                "labels": "...",
                "name": "...",
                "namespace": "...",
                "ownerReferences": "...",
                "resourceVersion": "...",
                "selfLink": "...",
                "uid": "..."
              },
              "spec": {
                "certificateMode": "...",
                "forceOverride": "...",
                "routeName": "..."
              },
              "status": {
                "conditions": "...",
                "mappedRouteName": "...",
                "observedGeneration": "...",
                "resourceRecords": "...",
                "url": "..."
              }
            }
          },
          "result": "createResult"
        }
      }
    ]

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
