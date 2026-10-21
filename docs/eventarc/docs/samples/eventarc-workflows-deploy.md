---
url: https://docs.cloud.google.com/eventarc/docs/samples/eventarc-workflows-deploy/
title: Create a trigger using Terraform (workflow) \u00a0|\u00a0 Eventarc \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:25:44.111864+00:00
---

# Create a trigger using Terraform (workflow)  |  Eventarc  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/docs/samples/eventarc-workflows-deploy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Samples ](https://docs.cloud.google.com/eventarc/docs/samples)



#  Create a trigger using Terraform (workflow) Stay organized with collections  Save and categorize content based on your preferences. 

Creates a workflow that returns information about Google Cloud Storage events.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create a trigger using Terraform](https://docs.cloud.google.com/eventarc/docs/creating-triggers-terraform)



## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    # Create a workflow
    resource "google_workflows_workflow" "default" {
      name            = "storage-workflow-tf"
      region          = "us-central1"
      description     = "Workflow that returns information about storage events"
      service_account = google_service_account.eventarc.email
    
      deletion_protection = false # set to "true" in production
    
      # Note that $$ is needed for Terraform
      source_contents = <<EOF
      main:
        params: [event]
        steps:
          - log_event:
              call: sys.log
              args:
                text: $${event}
                severity: INFO
          - gather_data:
              assign:
                - bucket: $${event.data.bucket}
                - name: $${event.data.name}
                - message: $${"Received event " + event.type + " - " + bucket + ", " + name}
          - return_data:
              return: $${message}
      EOF
    
      depends_on = [
        google_project_service.workflows
      ]
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=eventarc). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
