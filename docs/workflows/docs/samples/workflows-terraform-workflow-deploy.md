---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-terraform-workflow-deploy/
title: Create and deploy a workflow using Terraform \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:25.934612+00:00
---

# Create and deploy a workflow using Terraform  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-terraform-workflow-deploy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Create and deploy a workflow using Terraform Stay organized with collections  Save and categorize content based on your preferences. 

Creates and deploys a sample workflow using Terraform.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Quickstart: Create a workflow by using Terraform](https://docs.cloud.google.com/workflows/docs/create-workflow-terraform)



## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    # Create a workflow
    resource "google_workflows_workflow" "default" {
      name            = "sample-workflow"
      region          = "us-central1"
      description     = "A sample workflow"
      service_account = google_service_account.default.id
    
      deletion_protection = false # set to "true" in production
    
      labels = {
        env = "test"
      }
      user_env_vars = {
        url = "https://timeapi.io/api/Time/current/zone?timeZone=Europe/Amsterdam"
      }
      source_contents = <<-EOF
      # This is a sample workflow that you can replace with your source code
      #
      # The workflow does the following:
      # - Retrieves the current date from a public API and stores the
      #   response in `currentDate`
      # - Retrieves a list of Wikipedia articles from a public API related
      #   to the day of the week stored in `currentDate`
      # - Returns the list of articles in the workflow output
      #
      # Note that when you define workflows in Terraform, variables must be
      # escaped with two dollar signs ($$) and not a single sign ($)
    
      - getCurrentDate:
          call: http.get
          args:
              url: $${sys.get_env("url")}
          result: currentDate
      - readWikipedia:
          call: http.get
          args:
              url: https://en.wikipedia.org/w/api.php
              query:
                  action: opensearch
                  search: $${currentDate.body.dayOfWeek}
          result: wikiResult
      - returnOutput:
          return: $${wikiResult.body[1]}
    EOF
    
      depends_on = [google_project_service.default]
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
