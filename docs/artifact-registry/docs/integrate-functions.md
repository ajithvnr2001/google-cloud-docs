---
url: https://docs.cloud.google.com/artifact-registry/docs/integrate-functions/
title: Using private dependencies with Cloud Run functions \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:29:57.337413+00:00
---

# Using private dependencies with Cloud Run functions  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/integrate-functions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Using private dependencies with Cloud Run functions Stay organized with collections  Save and categorize content based on your preferences. 

Artifact Registry lets you store private npm and Python packages that you can include as dependencies in a Cloud Run function. You can use default permissions in the same project or grant roles to the Cloud Build service account for cross-project builds.

## Required permissions

Cloud Run functions uses the [Cloud Build service account](https://docs.cloud.google.com/build/docs/cloud-build-service-account) in the same Google Cloud project to build and deploy your function.

  * If Cloud Run functions and Artifact Registry are in the same Google Cloud project, the service account has the necessary permissions to download from repositories.
  * If Cloud Run functions and Artifact Registry are in different projects, you must grant repository access to the Cloud Build service account. 
    * To provide read-only access for downloading dependencies, [grant](https://docs.cloud.google.com/artifact-registry/docs/access-control#grant) the Artifact Registry Reader role.
    * If you also use Cloud Build to upload artifacts to repositories, [grant](https://docs.cloud.google.com/artifact-registry/docs/access-control#grant) the Artifact Registry Writer role.



## Configuring access to dependencies

See the Cloud Run functions documentation for [npm](https://docs.cloud.google.com/functions/docs/writing/specifying-dependencies-nodejs#using_private_modules) and [Python](https://docs.cloud.google.com/functions/docs/writing/specifying-dependencies-python#using_private_dependencies) configuration instructions.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
