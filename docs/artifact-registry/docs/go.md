---
url: https://docs.cloud.google.com/artifact-registry/docs/go/
title: Get started with Go modules \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:17.314669+00:00
---

# Get started with Go modules  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/go/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Get started with Go modules Stay organized with collections  Save and categorize content based on your preferences. 

Artifact Registry supports Go modules and semantic versioning independent of your version control system. Go modules stored in Artifact Registry can be used alongside other public or private modules in your Go projects.

## Overview

To get familiar with storing Go modules in Artifact Registry, you can try the [quickstart](https://docs.cloud.google.com/artifact-registry/docs/go/store-go).

When you're ready to learn more, read the following information:

  * [Create a Go module repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos) for your packages.
  * [Grant permissions](https://docs.cloud.google.com/artifact-registry/docs/access-control) to the account that will connect with the repository. Service accounts for common integrations with Artifact Registry have default [permissions](https://docs.cloud.google.com/artifact-registry/docs/access-control#gcp) for repositories in the same project.
  * [Set up authentication to Artifact Registry for Go](https://docs.cloud.google.com/artifact-registry/docs/go/authentication).
  * [Manage your Go modules](https://docs.cloud.google.com/artifact-registry/docs/go/manage-modules).
  * Learn about [semantic versioning in Go](https://go.dev/doc/modules/version-numbers).
  * Learn how to create [remote](https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-repo#go) and [virtual repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/virtual-repo).
  * Read about how remote and virtual repositories can be used in this [repository usage example](https://docs.cloud.google.com/artifact-registry/docs/repositories#example).



## Audit logging

To view Go log entries in Cloud Logging, you must [enable](https://docs.cloud.google.com/logging/docs/audit/configure-data-access#config-console-enable) `DATA_WRITE` logging.

When you upload a Go module to a repository, the operation is logged as `UploadGoModule`. Artifact Registry logs the following specific methods for Go repositories:

List versions in a module

  * `Go-ListVersions`



View module information

  * `Go-ViewModInfo`



Download the `go.mod` File

  * `Go-DownloadModFile`



Download the zip File

  * `Go-DownloadZipFile`



For information about other Artifact Registry log entries, see [View audit logs](https://docs.cloud.google.com/artifact-registry/docs/audit-logging).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
