---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-secretmanager/
title: Connector for Secret Manager \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:12:23.129157+00:00
---

# Connector for Secret Manager  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-secretmanager/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Connector for Secret Manager Stay organized with collections  Save and categorize content based on your preferences. 

Workflows connector that defines the built-in function used to access Secret Manager within a workflow.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Secret Manager API Connector Overview](https://docs.cloud.google.com/workflows/docs/reference/googleapis/secretmanager/Overview)
  * [Secure and store sensitive data using the Secret Manager connector](https://docs.cloud.google.com/workflows/docs/use-secret-manager)



## Code sample

### YAML
    
    
    # This workflow demonstrates how to use the Secret Manager connector:
    # Retrieve a secret using three different methods
    # Expected output: the secret data (thrice)
    - init:
        assign:
          - project_id: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
          - secret_id: "test-secret"  # Make sure you have this secret and it has a version of 1.
          - version: "1"
    # Add data to an existing secret without base-64 encoding
    - add_version_string:
        call: googleapis.secretmanager.v1.projects.secrets.addVersionString
        args:
          secret_id: ${secret_id}
          project_id: ${project_id}
          data: "a new secret"
    # Retrieve the secret in string format without base-64 decoding and assume
    # that the secret data is a valid UTF-8 string; if not, raise an error
    - access_string_secret:
        call: googleapis.secretmanager.v1.projects.secrets.versions.accessString
        args:
          secret_id: ${secret_id}
          version: ${version}  # if not set, "latest" is used
          project_id: ${project_id}
        result: str_secret
    # Retrieve the secret in string format without base-64 decoding
    - access_secret:
        call: googleapis.secretmanager.v1.projects.secrets.versions.access
        args:
          name: ${"projects/" + project_id + "/secrets/" + secret_id + "/versions/" + version}
        result: base64_encoded_secret
    # Retrieve the secret using positional arguments in an expression
    - expression:
        assign:
          - secret_str_from_exp: ${googleapis.secretmanager.v1.projects.secrets.versions.accessString(secret_id, version, project_id)}
    - the_end:
        return:
          - ${str_secret}
          - ${text.decode(base64.decode(base64_encoded_secret.payload.data))}
          - ${secret_str_from_exp}

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
