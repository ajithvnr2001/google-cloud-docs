---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-build-config/
title: Deploy a workflow from Git using Cloud Build \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:54:49.027989+00:00
---

# Deploy a workflow from Git using Cloud Build  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-build-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Deploy a workflow from Git using Cloud Build Stay organized with collections  Save and categorize content based on your preferences. 

Create a Cloud Build configuration file that deploys and runs a workflow.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Deploy a workflow from a Git repository using Cloud Build](https://docs.cloud.google.com/workflows/docs/deploy-workflows-using-cloud-build)



## Code sample

### YAML
    
    
    steps:
    # Deploy the test workflow with the commit sha
    - id: 'deploy-test-workflow'
      name: 'gcr.io/cloud-builders/gcloud'
      args: ['workflows', 'deploy', '$_WORKFLOW_NAME-$BRANCH_NAME-$SHORT_SHA', '--source', 'gitops/workflow.yaml']
    
    # Run the test workflow and capture the output
    - id: 'run-test-workflow'
      name: 'gcr.io/cloud-builders/gcloud'
      entrypoint: 'bash'
      args: ['-c', 'gcloud workflows run $_WORKFLOW_NAME-$BRANCH_NAME-$SHORT_SHA > /workspace/testoutput.log']
    
    # Delete the test workflow
    - id: 'delete-test-workflow'
      name: 'gcr.io/cloud-builders/gcloud'
      args: ['workflows', 'delete', '$_WORKFLOW_NAME-$BRANCH_NAME-$SHORT_SHA', '--quiet']
    
    # Check the test output
    - id: 'check-test-workflow'
      name: 'gcr.io/cloud-builders/gcloud'
      entrypoint: 'bash'
      args: ['gitops/test-$BRANCH_NAME.sh']
    
    # Deploy the workflow
    - id: 'deploy-workflow'
      name: 'gcr.io/cloud-builders/gcloud'
      args: ['workflows', 'deploy', '$_WORKFLOW_NAME-$BRANCH_NAME', '--source', 'gitops/workflow.yaml']

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
