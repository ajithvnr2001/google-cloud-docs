---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/Overview/
title: Cloud Run Admin API Connector Overview \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:33:43.081801+00:00
---

# Cloud Run Admin API Connector Overview  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/Overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Cloud Run Admin API Connector Overview Stay organized with collections  Save and categorize content based on your preferences. 

The Workflows connector defines the built-in functions that can be used to access other Google Cloud products within a workflow.

This page provides an overview of the individual connector. There is no need to import or load connector libraries in a workflow—connectors work out of the box when used in a call step.

## Cloud Run Admin API

Deploy and manage user provided container images that scale automatically based on incoming requests. The Cloud Run Admin API v1 follows the Knative Serving API specification, while v2 is aligned with Google Cloud AIP-based API standards, as described in https://google.aip.dev/. To learn more, see the [Cloud Run Admin API documentation](https://cloud.google.com/run/).

For the YAML representation of the [Service](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v1/Overview#service) and [Job](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v1/Overview#job) objects in the Cloud Run Admin API, see the [Cloud Run YAML reference](https://docs.cloud.google.com/run/docs/reference/yaml/v1). Note that the YAML maps exactly to the API, and you can modify the YAML specifications to configure your Cloud Run service.

## Authentication

All Cloud Run services are deployed privately by default, which means that they can't be accessed without providing authentication credentials in the request. Learn more about [invoking Cloud Run](https://docs.cloud.google.com/workflows/docs/calling-run-functions) and sending authenticated requests.

## Container image

Learn how to [build a container image](https://docs.cloud.google.com/run/docs/building/containers) like the one used in the following sample.

## Cloud Run Admin connector sample

### YAML
    
    
    # This workflow demonstrates how to use the Cloud Run connector:
    # Create a new service and then delete it
    # A location must be specified
    # Expected output is the `delete_service` response with a "Success" status
    - init:
        assign:
          - service_name: "test-service"
          - project: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
    - create_service:
        call: googleapis.run.v1.namespaces.services.create
        args:
          location: "us-central1"
          parent: ${"namespaces/" + project}
          body:
            apiVersion: "serving.knative.dev/v1"
            kind: "Service"
            metadata:
              name: ${service_name}
              namespace: ${project}
            spec:
              traffic:
                latest_revision: true
                percent: 100
              template:
                metadata:
                  labels:
                    serving.knative.dev/type: "container"
                spec:
                  containers:
                    - image: "us-docker.pkg.dev/cloudrun/container/hello:latest"
        result: create_response
    - get_service:
        call: googleapis.run.v1.namespaces.services.get
        args:
          name: ${"namespaces/" + project + "/services/" + service_name}
          location: "us-central1"
        result: get_response
    - delete_service:
        call: googleapis.run.v1.namespaces.services.delete
        args:
          location: "us-central1"
          name: ${"namespaces/" + project + "/services/" + service_name}
        result: delete_response
    - return:
        return: ${delete_response}

### JSON
    
    
    [
      {
        "init": {
          "assign": [
            {
              "service_name": "test-service"
            },
            {
              "project": "your-project-id"
            }
          ]
        }
      },
      {
        "create_service": {
          "call": "googleapis.run.v1.namespaces.services.create",
          "args": {
            "location": "us-central1",
            "parent": "${\"namespaces/\" + project}",
            "body": {
              "apiVersion": "serving.knative.dev/v1",
              "kind": "Service",
              "metadata": {
                "name": "${service_name}",
                "namespace": "${project}"
              },
              "spec": {
                "traffic": {
                  "latest_revision": true,
                  "percent": 100
                },
                "template": {
                  "metadata": {
                    "labels": {
                      "serving.knative.dev/type": "container"
                    }
                  },
                  "spec": {
                    "containers": [
                      {
                        "image": "us-docker.pkg.dev/cloudrun/container/hello:latest"
                      }
                    ]
                  }
                }
              }
            }
          },
          "result": "create_rsp"
        }
      },
      {
        "get_service": {
          "call": "googleapis.run.v1.namespaces.services.get",
          "args": {
            "name": "${\"namespaces/\" + project + \"/services/\" + service_name}",
            "location": "us-central1"
          },
          "result": "get_resp"
        }
      },
      {
        "delete_service": {
          "call": "googleapis.run.v1.namespaces.services.delete",
          "args": {
            "location": "us-central1",
            "name": "${\"namespaces/\" + project + \"/services/\" + service_name}"
          },
          "result": "delete_rsp"
        }
      },
      {
        "return": {
          "return": "${delete_rsp}"
        }
      }
    ]

## Module: googleapis.run.v1.namespaces.authorizeddomains

Functions  
---  
`[list](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v1/namespaces.authorizeddomains/list)` | List authorized domains.  
  
## Module: googleapis.run.v1.namespaces.configurations

Functions  
---  
`[get](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v1/namespaces.configurations/get)` | Get information about a configuration.  
`[list](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v1/namespaces.configurations/list)` | List configurations. Results are sorted by creation time, descending.  
  
## Module: googleapis.run.v1.namespaces.domainmappings

Functions  
---  
`[create](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v1/namespaces.domainmappings/create)` | Create a new domain mapping.  
`[delete](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v1/namespaces.domainmappings/delete)` | Delete a domain mapping.  
`[get](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v1/namespaces.domainmappings/get)` | Get information about a domain mapping.  
`[list](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v1/namespaces.domainmappings/list)` | List all domain mappings.  
  
## Module: googleapis.run.v1.namespaces.executions

Functions  
---  
`[cancel](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v1/namespaces.executions/cancel)` | Cancel an execution.  
`[delete](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v1/namespaces.executions/delete)` | Delete an execution.  
`[get](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v1/namespaces.executions/get)` | Get information about an execution.  
`[list](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v1/namespaces.executions/list)` | List executions. Results are sorted by creation time, descending.  
  
## Module: googleapis.run.v1.namespaces.jobs

Functions  
---  
`[create](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v1/namespaces.jobs/create)` | Create a job.  
`[delete](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v1/namespaces.jobs/delete)` | Delete a job.  
`[get](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v1/namespaces.jobs/get)` | Get information about a job.  
`[list](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v1/namespaces.jobs/list)` | List jobs. Results are sorted by creation time, descending.  
`[replaceJob](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v1/namespaces.jobs/replaceJob)` | Replace a job. Only the spec and metadata labels and annotations are modifiable. After the Replace request, Cloud Run will work to make the 'status' match the requested 'spec'. May provide metadata.resourceVersion to enforce update from last read for optimistic concurrency control.  
`[run](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v1/namespaces.jobs/run)` | Trigger creation of a new execution of this job.  
  
## Module: googleapis.run.v1.namespaces.revisions

Functions  
---  
`[delete](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v1/namespaces.revisions/delete)` | Delete a revision.  
`[get](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v1/namespaces.revisions/get)` | Get information about a revision.  
`[list](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v1/namespaces.revisions/list)` | List revisions. Results are sorted by creation time, descending.  
  
## Module: googleapis.run.v1.namespaces.routes

Functions  
---  
`[get](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v1/namespaces.routes/get)` | Get information about a route.  
`[list](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v1/namespaces.routes/list)` | List routes. Results are sorted by creation time, descending.  
  
## Module: googleapis.run.v1.namespaces.services

Functions  
---  
`[create](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v1/namespaces.services/create)` | Creates a new Service. Service creation will trigger a new deployment. Use GetService, and check service.status to determine if the Service is ready.  
`[delete](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v1/namespaces.services/delete)` | Deletes the provided service. This will cause the Service to stop serving traffic and will delete all associated Revisions.  
`[get](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v1/namespaces.services/get)` | Gets information about a service.  
`[list](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v1/namespaces.services/list)` | Lists services for the given project and region. Results are sorted by creation time, descending.  
`[replaceService](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v1/namespaces.services/replaceService)` | Replaces a service. Only the spec and metadata labels and annotations are modifiable. After the Update request, Cloud Run will work to make the 'status' match the requested 'spec'. May provide metadata.resourceVersion to enforce update from last read for optimistic concurrency control.  
  
## Module: googleapis.run.v1.namespaces.tasks

Functions  
---  
`[get](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v1/namespaces.tasks/get)` | Get information about a task.  
`[list](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v1/namespaces.tasks/list)` | List tasks.  
  
## Module: googleapis.run.v1.projects.locations

Functions  
---  
`[list](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v1/projects.locations/list)` | Lists information about the supported locations for this service.  
  
## Module: googleapis.run.v1.projects.locations.jobs

Functions  
---  
`[getIamPolicy](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v1/projects.locations.jobs/getIamPolicy)` | Get the IAM Access Control policy currently in effect for the given job. This result does not include any inherited policies.  
`[setIamPolicy](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v1/projects.locations.jobs/setIamPolicy)` | Sets the IAM Access control policy for the specified job. Overwrites any existing policy.  
`[testIamPermissions](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v1/projects.locations.jobs/testIamPermissions)` | Returns permissions that a caller has on the specified job. There are no permissions required for making this API call.  
  
## Module: googleapis.run.v1.projects.locations.services

Functions  
---  
`[getIamPolicy](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v1/projects.locations.services/getIamPolicy)` | Gets the IAM Access Control policy currently in effect for the given Cloud Run service. This result does not include any inherited policies.  
`[setIamPolicy](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v1/projects.locations.services/setIamPolicy)` | Sets the IAM Access control policy for the specified Service. Overwrites any existing policy.  
`[testIamPermissions](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v1/projects.locations.services/testIamPermissions)` | Returns permissions that a caller has on the specified Project. There are no permissions required for making this API call.  
  
## Module: googleapis.run.v2.projects.locations.jobs

Functions  
---  
`[create](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v2/projects.locations.jobs/create)` | Creates a Job.  
`[delete](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v2/projects.locations.jobs/delete)` | Deletes a Job.  
`[get](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v2/projects.locations.jobs/get)` | Gets information about a Job.  
`[getIamPolicy](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v2/projects.locations.jobs/getIamPolicy)` | Gets the IAM Access Control policy currently in effect for the given Job. This result does not include any inherited policies.  
`[list](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v2/projects.locations.jobs/list)` | Lists Jobs. Results are sorted by creation time, descending.  
`[patch](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v2/projects.locations.jobs/patch)` | Updates a Job.  
`[run](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v2/projects.locations.jobs/run)` | Triggers creation of a new Execution of this Job.  
`[setIamPolicy](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v2/projects.locations.jobs/setIamPolicy)` | Sets the IAM Access control policy for the specified Job. Overwrites any existing policy.  
`[testIamPermissions](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v2/projects.locations.jobs/testIamPermissions)` | Returns permissions that a caller has on the specified Project. There are no permissions required for making this API call.  
  
## Module: googleapis.run.v2.projects.locations.jobs.executions

Functions  
---  
`[cancel](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v2/projects.locations.jobs.executions/cancel)` | Cancels an Execution.  
`[delete](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v2/projects.locations.jobs.executions/delete)` | Deletes an Execution.  
`[get](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v2/projects.locations.jobs.executions/get)` | Gets information about an Execution.  
`[list](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v2/projects.locations.jobs.executions/list)` | Lists Executions from a Job. Results are sorted by creation time, descending.  
  
## Module: googleapis.run.v2.projects.locations.jobs.executions.tasks

Functions  
---  
`[get](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v2/projects.locations.jobs.executions.tasks/get)` | Gets information about a Task.  
`[list](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v2/projects.locations.jobs.executions.tasks/list)` | Lists Tasks from an Execution of a Job.  
  
## Module: googleapis.run.v2.projects.locations.operations

Functions  
---  
`[delete](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v2/projects.locations.operations/delete)` | Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.  
`[get](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v2/projects.locations.operations/get)` | Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.  
`[list](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v2/projects.locations.operations/list)` | Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`.  
  
## Module: googleapis.run.v2.projects.locations.services

Functions  
---  
`[create](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v2/projects.locations.services/create)` | Creates a new Service in a given project and location.  
`[delete](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v2/projects.locations.services/delete)` | Deletes a Service. This will cause the Service to stop serving traffic and will delete all revisions.  
`[get](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v2/projects.locations.services/get)` | Gets information about a Service.  
`[getIamPolicy](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v2/projects.locations.services/getIamPolicy)` | Gets the IAM Access Control policy currently in effect for the given Cloud Run Service. This result does not include any inherited policies.  
`[list](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v2/projects.locations.services/list)` | Lists Services. Results are sorted by creation time, descending.  
`[patch](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v2/projects.locations.services/patch)` | Updates a Service.  
`[setIamPolicy](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v2/projects.locations.services/setIamPolicy)` | Sets the IAM Access control policy for the specified Service. Overwrites any existing policy.  
`[testIamPermissions](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v2/projects.locations.services/testIamPermissions)` | Returns permissions that a caller has on the specified Project. There are no permissions required for making this API call.  
  
## Module: googleapis.run.v2.projects.locations.services.revisions

Functions  
---  
`[delete](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v2/projects.locations.services.revisions/delete)` | Deletes a Revision.  
`[get](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v2/projects.locations.services.revisions/get)` | Gets information about a Revision.  
`[list](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v2/projects.locations.services.revisions/list)` | Lists Revisions from a given Service, or from a given location. Results are sorted by creation time, descending.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
