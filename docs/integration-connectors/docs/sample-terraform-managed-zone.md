---
url: https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-managed-zone/
title: Sample terraform template for managed zone creation \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:36.860946+00:00
---

# Sample terraform template for managed zone creation  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-managed-zone/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Reference ](https://docs.cloud.google.com/integration-connectors/docs/reference/rest)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Sample terraform template for managed zone creation

The following is a sample terraform template for managed zone creation.

**Note:** This sample is not specific to any connector. It just shows how a managed zone creation terraform template looks like. You must repurpose this sample based on your requirements.
    
    
    resource "google_integration_connectors_managed_zone" "test_managed_zone" {
      name        = "test-managed-zone"
      description = "tf created resource"
      labels = {
        intent = "example"
      }
      target_project = data.google_project.target_project.project_id
      target_vpc     = "test"
      dns            = google_dns_managed_zone.default.dns_name
      depends_on     = [google_project_iam_member.default]
    }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
