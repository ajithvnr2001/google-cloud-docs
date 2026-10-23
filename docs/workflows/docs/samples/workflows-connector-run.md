---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-run/
title: Connector for Cloud Run \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:46.591001+00:00
---

# Connector for Cloud Run  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-run/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Connector for Cloud Run Stay organized with collections  Save and categorize content based on your preferences. 

Workflows connector that defines the built-in function used to access Cloud Run within a workflow.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Cloud Run Admin API Connector Overview](https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/Overview)



## Code sample

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

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
