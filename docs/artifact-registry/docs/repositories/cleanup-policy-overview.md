---
url: https://docs.cloud.google.com/artifact-registry/docs/repositories/cleanup-policy-overview/
title: Cleanup policy overview \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:46.494691+00:00
---

# Cleanup policy overview  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/repositories/cleanup-policy-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Cleanup policy overview Stay organized with collections  Save and categorize content based on your preferences. 

An Artifact Registry **cleanup policy** defines criteria for automatically deleting artifact versions that you no longer need or for keeping artifacts that you want to store indefinitely.

Cleanup policies are useful if you store many versions of your artifacts, but only need to keep specific versions that you release to production. You can define **delete policies** with criteria for deleting artifacts and **keep policies** with criteria for retaining artifacts.

Deletions triggered by delete policies count against your Artifact Registry [per project delete request quota](https://docs.cloud.google.com/artifact-registry/quotas#project-quota) and are limited to 600,000 deletions per repository, per day.

**Note:** When you use cleanup policies on [gcr.io repositories](https://docs.cloud.google.com/artifact-registry/docs/transition/setup-gcr-repo), the date the image was uploaded to Container Registry for each artifact is only preserved if you use the [automatic migration tool](https://docs.cloud.google.com/artifact-registry/docs/transition/auto-migrate-gcr-ar) to copy your images from Container Registry to Artifact Registry. If you use other tooling to copy your images, the creation time in Artifact Registry is the date the image was copied to Artifact Registry from Container Registry, not the date it was uploaded to Container Registry.

## Types of cleanup policies

A delete policy defines the minimum or maximum age for artifact deletion, with additional filtering criteria available to limit the policy to specific artifacts. When you have an active delete policy, you can also configure different types of keep policies so that Artifact Registry maintains specific artifacts:

  * **Conditional keep policy** : Defines criteria for retaining artifacts. You can configure conditional keep policies to maintain artifacts that your delete policies would otherwise remove. When an artifact matches the criteria for both a delete policy and a keep policy, the artifact is kept.
  * **Keep most recent versions** : Defines criteria for keeping a specific range of artifact versions. You can't use **Conditional keep** and **Keep most recent versions** criteria in the same cleanup policy.



## Priority of policies matching the same image

If an artifact version matches criteria in both a delete policy and a keep policy, Artifact Registry applies the keep policy.

If an artifact version matches multiple delete policies, Artifact Registry applies the delete policy with the shortest retention period. For example, you have two delete policies:

  * **Delete Policy 1** : Delete all images with tags that start with `commit-` after 24 hours.
  * **Delete Policy 2** : Delete all tagged images after seven days.



An image tagged as `commit-1234` matches both policies. Since Policy 1 has a shorter retention period, the image is deleted after 24 hours.

## Policy application order

If your repository has more than one cleanup policy, then Artifact Registry applies the policies in order unless a keep policy matches the same image as a delete policy. For example, your repository has cleanup policies with the following conditions:

  1. Delete images older than 100 days.
  2. Keep images with a version prefix of 2.0.6.
  3. Delete images with a `default` tag.



Your repository contains images with the following attributes:

Image | Age | Tag | Version  
---|---|---|---  
Image A | 120 Days | `default` | 2.0.1  
Image B | 150 Days | `default` | 2.0.6  
Image C | 20 Days | `patch` | 1.9.2  
  
In this example, Image A is deleted and Image C is kept. Image B is also kept due to the keep policy matching the image version, even though Image B also matches the deletion criteria for the first and third policies.

## Policy application schedule

Artifact Registry performs dry runs and active runs of cleanup policies using a background job that runs periodically. Changes take effect within approximately one day.

## Maximum number of cleanup policies per repository

You can apply a maximum of 10 cleanup policies to a repository.

## Supported formats

You can set a cleanup policy on standard and remote repositories for all repository [formats](https://docs.cloud.google.com/artifact-registry/docs/supported-formats).

**Note:** Repository [attachments](https://docs.cloud.google.com/artifact-registry/docs/store-artifact-metadata-in-attachments) aren't subject to cleanup policies. Instead, attachments are deleted when the image they are attached to is deleted. For more information, see [Manage attachments with cleanup policies](https://docs.cloud.google.com/artifact-registry/docs/store-artifact-metadata-in-attachments#attach-cleanup).

## What's next

  * For information about how to create and manage cleanup policies, see [Configure cleanup policies](https://docs.cloud.google.com/artifact-registry/docs/repositories/cleanup-policy).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
