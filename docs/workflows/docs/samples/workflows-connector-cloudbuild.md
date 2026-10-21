---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-cloudbuild/
title: Connector for Cloud Build \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:12:25.659735+00:00
---

# Connector for Cloud Build  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-cloudbuild/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Connector for Cloud Build Stay organized with collections  Save and categorize content based on your preferences. 

Workflows connector that defines the built-in function used to access Cloud Build within a workflow.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Cloud Build API Connector Overview](https://docs.cloud.google.com/workflows/docs/reference/googleapis/cloudbuild/Overview)



## Code sample

### YAML
    
    
    # This workflow demonstrates how to use the Cloud Build connector.
    # The workflow creates a simple build and the image is stored to an Artifact Registry repo.
    # The workflow assumes a properly defined source tgz file already
    # exists in a Cloud Storage bucket: gs://your-project-id_cloudbuild/source/placeholder_src.tgz
    # and a repository "your-project-id-docker-repo" already
    # exists in Artifact Registry where the image will be stored.
    # The new table and dataset are both deleted in the following steps.
    # Expected successful output: "SUCCESS"
    
    - init:
        assign:
          - project_id: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
          - location_id: "global"
          - repo: ${project_id + "-docker-repo"}
          - image_path: ${"us-central1-docker.pkg.dev/" + project_id + "/" + repo + "/quickstart-image:tag1"}
    - create_build:
        call: googleapis.cloudbuild.v1.projects.builds.create
        args:
          projectId: ${project_id}
          parent: ${"projects/" + project_id + "/locations/" + location_id}
          body:
            source:
              storageSource:
                bucket: ${project_id + "_cloudbuild"}
                object: "source/placeholder_src.tgz"
            steps:
              - name: "gcr.io/cloud-builders/docker"
                args:
                  - "build"
                  - "-t"
                  - ${image_path}
                  - "."
            images:
              - ${image_path}
    - the_end:
        return: "SUCCESS"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
