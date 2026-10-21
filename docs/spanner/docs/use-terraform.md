---
url: https://docs.cloud.google.com/spanner/docs/use-terraform/
title: Use Terraform with Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:38.553791+00:00
---

# Use Terraform with Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/use-terraform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Use Terraform with Spanner Stay organized with collections  Save and categorize content based on your preferences. 

[Terraform](https://www.terraform.io/) is a tool for building, changing, and versioning infrastructure. It uses configuration files to describe the components needed to run a single application or your entire infrastructure.

You can use the [Google Cloud Terraform Provider](https://www.terraform.io/docs/providers/google/index.html) to create Spanner instances and databases, and to modify or delete Spanner resources.

**PostgreSQL interface note:** For PostgreSQL-dialect databases, Terraform doesn't support submitting DDL while creating a database. You must submit DDL in a separate operation. 

The Google Cloud Terraform Provider offers the following Spanner resources:

  * [google_spanner_instance](https://www.terraform.io/docs/providers/google/r/spanner_instance)
  * [google_spanner_database](https://www.terraform.io/docs/providers/google/r/spanner_database)
  * [google_spanner_instance_iam](https://www.terraform.io/docs/providers/google/r/spanner_instance_iam)
  * [google_spanner_database_iam](https://www.terraform.io/docs/providers/google/r/spanner_database_iam)



For more information about using these resources to create and manage Spanner instances and databases, see [Using Terraform with Google Cloud](https://cloud.google.com/docs/terraform) or consult the Google Cloud Terraform Provider [reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs).

## What's next

  * Learn more about [Terraform](https://www.terraform.io/).
  * Try out [code examples](https://github.com/cloudspannerecosystem/spanner-terraform#examples) that use the Google Cloud Terraform Provider with Spanner.
  * For a step-by-step tutorial, try the Spanner with Terraform [codelab](https://codelabs.developers.google.com/codelabs/cloud-spanner-terraform#0).
  * View the Google Cloud Terraform Provider [repository on GitHub](https://github.com/hashicorp/terraform-provider-google).
  * [File a GitHub issue](https://github.com/hashicorp/terraform-provider-google/issues) to report a bug or ask a question about Terraform.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
