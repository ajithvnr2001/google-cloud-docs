---
url: https://docs.cloud.google.com/workflows/docs/use-secret-manager/
title: Secure and store sensitive data using the Secret Manager connector \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:01.831322+00:00
---

# Secure and store sensitive data using the Secret Manager connector  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/use-secret-manager/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Guides ](https://docs.cloud.google.com/workflows/docs/create-workflow-console)



Send feedback 

#  Secure and store sensitive data using the Secret Manager connector Stay organized with collections  Save and categorize content based on your preferences. 

Secret Manager is a secure and convenient storage system for API keys, passwords, certificates, and other sensitive data. Secret Manager provides a central place and single source of truth to manage, access, and audit secrets across Google Cloud.

You can use Workflows' [connector for the Secret Manager API](https://cloud.google.com/workflows/docs/reference/googleapis/secretmanager/Overview) to access Secret Manager within a workflow. This simplifies the integration for you, because the connector handles the formatting of requests, and provides methods and arguments so that you don't need to know the details of the Secret Manager API. The connector also has built-in behavior for handling retries and long-running operations. To learn more about using Workflows connectors, see [Understand connectors](https://docs.cloud.google.com/workflows/docs/connectors).

## Grant the Workflows service account access to Secret Manager

Secret Manager uses Identity and Access Management (IAM) for access control. To create, manage, list, or access a secret, the appropriate IAM permissions must be granted at the project level and at the individual resource level. For more information, see [Access control with IAM](https://docs.cloud.google.com/secret-manager/docs/access-control).

Workflows uses service accounts to give workflows access to Google Cloud resources. To [access a secret version](https://docs.cloud.google.com/secret-manager/docs/access-secret-version), you must grant the Secret Manager Secret Accessor role (`roles/secretmanager.secretAccessor`) on the secret, project, folder, or organization to the service account. Learn more about [deploying a workflow with a user-managed service account](https://docs.cloud.google.com/workflows/docs/authentication).

## Enable the APIs

Before using the Workflows' connector for the Secret Manager API, ensure that you enable the Secret Manager and Workflows APIs.

###  Console 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=secretmanager.googleapis.com,workflows.googleapis.com)

###  gcloud 
    
    
      gcloud services enable secretmanager.googleapis.com workflows.googleapis.com
    

## Invoke a connector call

Similar to invoking an HTTP endpoint, a connector call requires `call` and `args` fields. For more information, see [Invoke a connector call](https://docs.cloud.google.com/workflows/docs/reference/googleapis#invoke_a_connector_call).

In addition to using a call step, you can call the helper methods in an expression like this:
    
    
    ${googleapis.secretmanager.v1.projects.secrets.versions.accessString(secret_id, version, project_id)}

For example, you can use the helper method `accessString` to retrieve the secret data as a string. This is simpler than using the `access` API as the secret data is automatically decoded to a string format.

You can also use the helper method `addVersionString` to add a new secret value to an existing secret. This is simpler than using the `addVersion` API as the secret data is automatically encoded to a base-64 string, which is required by `addVersion`.

## Retrieve a secret using the Secret Manager connector

The following workflow demonstrates how to use the Secret Manager connector to retrieve a secret.

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

### JSON
    
    
    [
      {
        "init": {
          "assign": [
            {
              "project_id": "${sys.get_env(\"GOOGLE_CLOUD_PROJECT_ID\")}"
            },
            {
              "secret_id": "test-secret"
            },
            {
              "version": "1"
            }
          ]
        }
      },
      {
        "add_version_string": {
          "call": "googleapis.secretmanager.v1.projects.secrets.addVersionString",
          "args": {
            "secret_id": "${secret_id}",
            "project_id": "${project_id}",
            "data": "a new secret"
          }
        }
      },
      {
        "access_string_secret": {
          "call": "googleapis.secretmanager.v1.projects.secrets.versions.accessString",
          "args": {
            "secret_id": "${secret_id}",
            "version": "${version}",
            "project_id": "${project_id}"
          },
          "result": "str_secret"
        }
      },
      {
        "access_secret": {
          "call": "googleapis.secretmanager.v1.projects.secrets.versions.access",
          "args": {
            "name": "${\"projects/\" + project_id + \"/secrets/\" + secret_id + \"/versions/\" + version}"
          },
          "result": "base64_encoded_secret"
        }
      },
      {
        "expression": {
          "assign": [
            {
              "secret_str_from_exp": "${googleapis.secretmanager.v1.projects.secrets.versions.accessString(secret_id, version, project_id)}"
            }
          ]
        }
      },
      {
        "the_end": {
          "return": [
            "${str_secret}",
            "${text.decode(base64.decode(base64_encoded_secret.payload.data))}",
            "${secret_str_from_exp}"
          ]
        }
      }
    ]
    

## What's next

  * [Learn more about Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
