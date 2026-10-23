---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-cloudfunctions/
title: Connector for Cloud Functions \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:59.423497+00:00
---

# Connector for Cloud Functions  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-cloudfunctions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Connector for Cloud Functions Stay organized with collections  Save and categorize content based on your preferences. 

Workflows connector that defines the built-in function used to access Cloud Functions within a workflow.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Cloud Functions API Connector Overview](https://docs.cloud.google.com/workflows/docs/reference/googleapis/cloudfunctions/Overview)



## Code sample

### YAML
    
    
    # This workflow demonstrates how to use the Cloud Functions connector:
    # Create a function using source code stored as a zip archive in a
    # Cloud Storage bucket (gs://BUCKET_NAME/cloud-function-source.zip)
    # Source code must be a properly structured Cloud Function
    # Expected output: "SUCCESS"
    main:
      params: []
      steps:
        - init:
            assign:
              - project: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
              - location: "us-central1"
              - name: "example-function"
              - bucket: "BUCKET_NAME"  # replace BUCKET_NAME placeholder
              - sourceArchiveUrl: ${"gs://" + bucket + "/cloud-function-source.zip"}
              - service_account: ${project + "@appspot.gserviceaccount.com"}  # App Engine default service account
        - create_function:
            call: googleapis.cloudfunctions.v1.projects.locations.functions.create
            args:
              location: ${"projects/" + project + "/locations/" + location}
              body:
                name: ${"projects/" + project + "/locations/" + location + "/functions/" + name}
                description: "Cloud Function for Workflows connector testing"
                entryPoint: "helloWorld"
                runtime: "nodejs10"
                serviceAccountEmail: ${service_account}
                sourceArchiveUrl: ${sourceArchiveUrl}
                httpsTrigger:
                  securityLevel: "SECURE_OPTIONAL"
        - get_function:
            call: googleapis.cloudfunctions.v1.projects.locations.functions.get
            args:
              name: ${"projects/" + project + "/locations/" + location + "/functions/" + name}
            result: function
        - grant_permission_to_all:
            call: googleapis.cloudfunctions.v1.projects.locations.functions.setIamPolicy
            args:
              resource: ${"projects/" + project + "/locations/" + location + "/functions/" + name}
              body:
                policy:
                  bindings:
                    - members: ["allUsers"]
                      role: "roles/cloudfunctions.invoker"
        - call_function:
            call: http.get
            args:
              url: ${function.httpsTrigger.url}
            result: resp
        - verify_response:
            call: assert_response
            args:
              expected_response: "success"  # function must return "success" when triggered
              actual_response: ${resp.body}
        - delete_function:
            call: googleapis.cloudfunctions.v1.projects.locations.functions.delete
            args:
              name: ${"projects/" + project + "/locations/" + location + "/functions/" + name}
        - the_end:
            return: "SUCCESS"
    
    assert_response:
      params: [expected_response, actual_response]
      steps:
        - compare:
            switch:
              - condition: ${expected_response == actual_response}
                next: end
        - fail:
            raise: ${"Expected response is " + expected_response + ". Received " + actual_response + " instead."}

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
