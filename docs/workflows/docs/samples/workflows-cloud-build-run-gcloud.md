---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-cloud-build-run-gcloud/
title: Run gcloud commands in a workflow \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:54:45.430786+00:00
---

# Run gcloud commands in a workflow  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-cloud-build-run-gcloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Run gcloud commands in a workflow Stay organized with collections  Save and categorize content based on your preferences. 

You can run gcloud CLI commands from a Cloud Build step, and you can create that step in Workflows using the Cloud Build connector.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Best practices for Workflows](https://docs.cloud.google.com/workflows/docs/best-practice)



## Code sample

### YAML
    
    
    # This example shows how to execute gcloud commands from Workflows
    # using Cloud Build and returns the output
    
    main:
      steps:
      - execute_command:
          call: gcloud
          args:
              args: "workflows list"
          result: result
      - return_result:
          return: ${result}
    
    gcloud:
      params: [args]
      steps:
      - create_build:
          call: googleapis.cloudbuild.v1.projects.builds.create
          args:
            projectId: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
            parent: ${"projects/" + sys.get_env("GOOGLE_CLOUD_PROJECT_ID") + "/locations/global"}
            body:
              serviceAccount: ${sys.get_env("GOOGLE_CLOUD_SERVICE_ACCOUNT_NAME")}
              options:
                logging: CLOUD_LOGGING_ONLY
              steps:
              - name: gcr.io/google.com/cloudsdktool/cloud-sdk
                entrypoint: /bin/bash
                args: ${["-c", "gcloud " + args + " > $$BUILDER_OUTPUT/output"]}
          result: result_builds_create
      - return_build_result:
          return: ${text.split(text.decode(base64.decode(result_builds_create.metadata.build.results.buildStepOutputs[0])), "\n")}

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
