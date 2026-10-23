---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-terraform-create-workflow/
title: Create a workflow that executes a Cloud Run job using Terraform \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:56:58.537051+00:00
---

# Create a workflow that executes a Cloud Run job using Terraform  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-terraform-create-workflow/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Create a workflow that executes a Cloud Run job using Terraform Stay organized with collections  Save and categorize content based on your preferences. 

Deploys a sample workflow using Terraform.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Execute a Cloud Run job using Workflows](https://docs.cloud.google.com/workflows/docs/tutorials/execute-cloud-run-jobs)



## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    # Create a workflow
    resource "google_workflows_workflow" "default" {
      name        = "cloud-run-job-workflow"
      region      = "us-central1"
      description = "Workflow that routes a Cloud Storage event and executes a Cloud Run job"
    
      deletion_protection = false # set to "true" in production
    
      # Note that $$ is needed for Terraform
      source_contents = <<EOF
      main:
          params: [event]
          steps:
              - init:
                  assign:
                      - project_id: $${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
                      - event_bucket: $${event.data.bucket}
                      - event_file: $${event.data.name}
                      - target_bucket: "${google_storage_bucket.default.name}"
                      - job_name: parallel-job
                      - job_location: us-central1
              - check_input_file:
                  switch:
                      - condition: $${event_bucket == target_bucket}
                        next: run_job
                      - condition: true
                        next: end
              - run_job:
                  call: googleapis.run.v1.namespaces.jobs.run
                  args:
                      name: $${"namespaces/" + project_id + "/jobs/" + job_name}
                      location: $${job_location}
                      body:
                          overrides:
                              containerOverrides:
                                  env:
                                      - name: INPUT_BUCKET
                                        value: $${event_bucket}
                                      - name: INPUT_FILE
                                        value: $${event_file}
                  result: job_execution
              - finish:
                  return: $${job_execution}
      EOF
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
