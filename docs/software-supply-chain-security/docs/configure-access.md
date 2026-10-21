---
url: https://docs.cloud.google.com/software-supply-chain-security/docs/configure-access/
title: Configure access \u00a0|\u00a0 Software supply chain security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:04.785359+00:00
---

# Configure access  |  Software supply chain security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/software-supply-chain-security/docs/configure-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Software supply chain security ](https://docs.cloud.google.com/software-supply-chain-security/docs)
  * [ Guides ](https://docs.cloud.google.com/software-supply-chain-security/docs/overview)



Send feedback 

#  Configure access Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the IAM permissions that are required to view software supply chain security insights in Google Cloud console. 

## Required roles

To view software supply chain security insights in Google Cloud console, you must have the following roles, or a role with equivalent permissions:

  * [Cloud Build Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.viewer) (`roles/cloudbuild.builds.viewer`): View insights for a build.
  * [Artifact Analysis Occurrences Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.occurrences.viewer) (`roles/containeranalysis.occurrences.viewer`): View vulnerabilities, build provenance, and other dependency information.
  * [Cloud Run Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.viewer) (`roles/run.viewer`): View insights for a Cloud Run revision.
  * [Kubernetes Engine Cluster Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.clusterViewer) (`roles/container.clusterViewer`): View insights for a GKE cluster.



These permissions provide access to insights, but they don't provide permissions to perform other actions such as running builds in Cloud Build.

  * For details about required permissions for a specific service, refer to the documentation for that service.
  * To learn about granting permissions, see the Identity and Access Management documentation on [granting permissions to projects](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).



By default, many services have default permissions for other services in the same project but cannot access resources in another project. If you are running services in different Google Cloud projects or if you are using custom IAM roles or custom service accounts, you must grant the appropriate permissions yourself.

## Granting permissions when services are in the same project

If Cloud Build, Artifact Registry, Artifact Analysis, and Cloud Run are all running in the same project, each service uses the default service account to act on behalf of the service, and the default permissions are unchanged. The services can all work together without changes to permissions, but you do need to grant permissions to users that need to see insights in the project.

Permissions between services
    

No changes are required:

  * The default [Cloud Build service account](https://docs.cloud.google.com/build/docs/cloud-build-service-account#default_permissions_of_service_account) has permissions to upload and download with Artifact Registry and read insight data from Artifact Analysis, so the service can sign container images with build provenance and push them to Artifact Registry.
  * Cloud Run revisions use the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) for deployments, which has permissions to download images from Artifact Registry and read insight data from Artifact Analysis.


User permissions to view insights
    

You must grant users of Cloud Build and Cloud Run with the required roles to view insights.

## Granting permissions when services are in different projects

When Artifact Registry and Artifact Analysis are running in separate project from other Google Cloud services, you must explicitly grant permissions for all cross-project activity. Consider the following project setup:

  * Cloud Build runs in project A
  * Artifact Registry and Artifact Analysis run in project B
  * Cloud Run runs in project C



Permissions between services
    

Cloud Build and Cloud Run cannot access resources in other projects without explicitly granting access to the service accounts that act on behalf of these services. You must grant appropriate [Artifact Registry permissions](https://docs.cloud.google.com/artifact-registry/docs/access-control#permissions) and [Artifact Analysis permissions](https://docs.cloud.google.com/artifact-analysis/docs/ca-access-control) in project B where the artifacts and artifact metadata are stored.

    

For Cloud Build, you must grant these roles in project B:

  * Artifact Registry Writer (`roles/artifactregistry.writer`) grants permissions to upload and download.
  * Artifact Analysis Occurrences Viewer (`roles/containeranalysis.occurrences.viewer`) grants permissions to display insights.


    

For Cloud Run, you must grant these roles in project B:

  * Artifact Registry Reader (`roles/artifactregistry.reader`) grants permissions to download for deployments.
  * Artifact Analysis Occurrences Viewer (`roles/containeranalysis.occurrences.viewer`) grants permissions to display insights.


User permissions to view insights
    

In project B, you must grant users of Cloud Build and Cloud Run with the required roles view insights.

## What's next

  * Learn more about how Google Cloud services protect your software supply chain in the [overview](https://docs.cloud.google.com/software-supply-chain-security/docs/overview)
  * Learn about [software supply chain security practices](https://docs.cloud.google.com/software-supply-chain-security/docs/practices) and how Google Cloud services can help you to implement them.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
