---
url: https://docs.cloud.google.com/artifact-registry/docs/repositories/delete-repos/
title: Delete repositories \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:44:34.810350+00:00
---

# Delete repositories  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/repositories/delete-repos/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Delete repositories Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to delete Artifact Registry repositories.

## Before you begin

You must have the Artifact Registry Administrator role or a role with equivalent [permissions](https://docs.cloud.google.com/artifact-registry/docs/access-control#permissions).

## Deleting repositories

Before you remove a repository, ensure that any packages that you want to keep are available in another location.

**Warning:** If you disable the Artifact Registry API or [delete the project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#shutting_down_projects), Artifact Registry services become unavailable. Artifact Registry deletes repository data after 7 days. [Learn more about data deletion on Google Cloud](https://docs.cloud.google.com/security/deletion). If you want to recover deleted repositories, then [Google Cloud Support](https://console.cloud.google.com/support) might be able to help recover deleted Artifact Registry repositories. However, Google Cloud Support can't restore individual images. Data recovery isn't a feature of Artifact Registry and is only performed as a good-will gesture. Google Cloud Support tries to recover Artifact Registry repositories on a best-effort basis. During the process of restoring Artifact Registry repositories, don't try to re-create the repository or push images to it.

When you delete a repository, make sure all references to the repository are replaced in your build and configuration files.

To delete a repository:

###  Console 

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. In the repository list, select the repository to delete.

  3. Click **Delete**.




###  gcloud 

To delete the a repository, run the following command:
    
    
    gcloud artifacts repositories delete REPOSITORY \
    [--location=LOCATION] [--async]

Where

  * REPOSITORY is the name of the repository.
  * `LOCATION` is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository. You can omit this flag if you set a [default](https://docs.cloud.google.com/artifact-registry/docs/repositories/gcloud-defaults#set).
  * `--async` returns immediately, without waiting for the operation in progress to complete.



For more information about the command, run the following command:
    
    
     gcloud artifacts repositories delete --help
     ```
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
