---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/cloudbuild/v1/projects.locations.triggers/create/
title: Method: googleapis.cloudbuild.v1.projects.locations.triggers.create \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:56:29.007803+00:00
---

# Method: googleapis.cloudbuild.v1.projects.locations.triggers.create  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/cloudbuild/v1/projects.locations.triggers/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Method: googleapis.cloudbuild.v1.projects.locations.triggers.create Stay organized with collections  Save and categorize content based on your preferences. 

Creates a new `BuildTrigger`. This API is experimental.

## Arguments

Parameters  
---  
`parent` |  `string` Required. The parent resource where this trigger will be created. Format: `projects/{project}/locations/{location}`  
`projectId` |  `string` Required. ID of the project for which to configure automatic builds.  
`body` |  `object ([BuildTrigger](https://docs.cloud.google.com/workflows/docs/reference/googleapis/cloudbuild/v1/Overview#BuildTrigger))` Required.  
  
## Raised exceptions

Exceptions  
---  
`ConnectionError` | In case of a network problem (such as DNS failure or refused connection).  
`HttpError` | If the response status is >= 400 (excluding 429 and 503).  
`TimeoutError` | If a long-running operation takes longer to finish than the specified timeout limit.  
`TypeError` | If an operation or function receives an argument of the wrong type.  
`ValueError` | If an operation or function receives an argument of the right type but an inappropriate value. For example, a negative timeout.  
  
## Response

If successful, the response contains an instance of [`BuildTrigger`](https://docs.cloud.google.com/workflows/docs/reference/googleapis/cloudbuild/v1/Overview#BuildTrigger).

## Subworkflow snippet

Some fields might be optional or required. To identify required fields, refer to the [API documentation](https://cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers/create).

### YAML
    
    
    - create:
        call: googleapis.cloudbuild.v1.projects.locations.triggers.create
        args:
            parent: ...
            projectId: ...
            body:
                approvalConfig:
                    approvalRequired: ...
                autodetect: ...
                build:
                    artifacts:
                        images: ...
                        objects:
                            location: ...
                            paths: ...
                    availableSecrets:
                        inline: ...
                        secretManager: ...
                    images: ...
                    logsBucket: ...
                    options:
                        diskSizeGb: ...
                        dynamicSubstitutions: ...
                        env: ...
                        logStreamingOption: ...
                        logging: ...
                        machineType: ...
                        pool:
                            name: ...
                        requestedVerifyOption: ...
                        secretEnv: ...
                        sourceProvenanceHash: ...
                        substitutionOption: ...
                        volumes: ...
                        workerPool: ...
                    queueTtl: ...
                    secrets: ...
                    serviceAccount: ...
                    source:
                        repoSource:
                            branchName: ...
                            commitSha: ...
                            dir: ...
                            invertRegex: ...
                            projectId: ...
                            repoName: ...
                            substitutions: ...
                            tagName: ...
                        storageSource:
                            bucket: ...
                            generation: ...
                            object: ...
                        storageSourceManifest:
                            bucket: ...
                            generation: ...
                            object: ...
                    steps: ...
                    substitutions: ...
                    tags: ...
                    timeout: ...
                description: ...
                disabled: ...
                filename: ...
                filter: ...
                gitFileSource:
                    path: ...
                    repoType: ...
                    revision: ...
                    uri: ...
                github:
                    enterpriseConfigResourceName: ...
                    installationId: ...
                    name: ...
                    owner: ...
                    pullRequest:
                        branch: ...
                        commentControl: ...
                        invertRegex: ...
                    push:
                        branch: ...
                        invertRegex: ...
                        tag: ...
                ignoredFiles: ...
                includedFiles: ...
                name: ...
                pubsubConfig:
                    serviceAccountEmail: ...
                    state: ...
                    topic: ...
                resourceName: ...
                serviceAccount: ...
                sourceToBuild:
                    ref: ...
                    repoType: ...
                    uri: ...
                substitutions: ...
                tags: ...
                triggerTemplate: ...
                webhookConfig:
                    secret: ...
                    state: ...
        result: createResult

### JSON
    
    
    [
      {
        "create": {
          "call": "googleapis.cloudbuild.v1.projects.locations.triggers.create",
          "args": {
            "parent": "...",
            "projectId": "...",
            "body": {
              "approvalConfig": {
                "approvalRequired": "..."
              },
              "autodetect": "...",
              "build": {
                "artifacts": {
                  "images": "...",
                  "objects": {
                    "location": "...",
                    "paths": "..."
                  }
                },
                "availableSecrets": {
                  "inline": "...",
                  "secretManager": "..."
                },
                "images": "...",
                "logsBucket": "...",
                "options": {
                  "diskSizeGb": "...",
                  "dynamicSubstitutions": "...",
                  "env": "...",
                  "logStreamingOption": "...",
                  "logging": "...",
                  "machineType": "...",
                  "pool": {
                    "name": "..."
                  },
                  "requestedVerifyOption": "...",
                  "secretEnv": "...",
                  "sourceProvenanceHash": "...",
                  "substitutionOption": "...",
                  "volumes": "...",
                  "workerPool": "..."
                },
                "queueTtl": "...",
                "secrets": "...",
                "serviceAccount": "...",
                "source": {
                  "repoSource": {
                    "branchName": "...",
                    "commitSha": "...",
                    "dir": "...",
                    "invertRegex": "...",
                    "projectId": "...",
                    "repoName": "...",
                    "substitutions": "...",
                    "tagName": "..."
                  },
                  "storageSource": {
                    "bucket": "...",
                    "generation": "...",
                    "object": "..."
                  },
                  "storageSourceManifest": {
                    "bucket": "...",
                    "generation": "...",
                    "object": "..."
                  }
                },
                "steps": "...",
                "substitutions": "...",
                "tags": "...",
                "timeout": "..."
              },
              "description": "...",
              "disabled": "...",
              "filename": "...",
              "filter": "...",
              "gitFileSource": {
                "path": "...",
                "repoType": "...",
                "revision": "...",
                "uri": "..."
              },
              "github": {
                "enterpriseConfigResourceName": "...",
                "installationId": "...",
                "name": "...",
                "owner": "...",
                "pullRequest": {
                  "branch": "...",
                  "commentControl": "...",
                  "invertRegex": "..."
                },
                "push": {
                  "branch": "...",
                  "invertRegex": "...",
                  "tag": "..."
                }
              },
              "ignoredFiles": "...",
              "includedFiles": "...",
              "name": "...",
              "pubsubConfig": {
                "serviceAccountEmail": "...",
                "state": "...",
                "topic": "..."
              },
              "resourceName": "...",
              "serviceAccount": "...",
              "sourceToBuild": {
                "ref": "...",
                "repoType": "...",
                "uri": "..."
              },
              "substitutions": "...",
              "tags": "...",
              "triggerTemplate": "...",
              "webhookConfig": {
                "secret": "...",
                "state": "..."
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
