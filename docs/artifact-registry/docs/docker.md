---
url: https://docs.cloud.google.com/artifact-registry/docs/docker/
title: Work with container images \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:21.709687+00:00
---

# Work with container images  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/docker/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Work with container images Stay organized with collections  Save and categorize content based on your preferences. 

Artifact Registry can store Docker and OCI [container images](https://docs.cloud.google.com/artifact-registry/docs/supported-formats#container) in a Docker repository.

To get familiar with container images in Artifact Registry, you can try the [quickstart](https://docs.cloud.google.com/artifact-registry/docs/docker/store-docker-container-images).

When you are ready to learn more, read the following information:

  * [Create a Docker repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos) for your images.
  * [Grant permissions](https://docs.cloud.google.com/artifact-registry/docs/access-control) to the account that will connect with the repository. 
    * The default service account for Compute Engine has permissions to pull from Artifact Registry repositories in the same Google Cloud project unless you have [disabled automatic role granting to default service accounts](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants). The Compute Engine service account is also the [default GKE node service account](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/service-accounts#default-gke-service-agent) and the default [Cloud Run service account](https://docs.cloud.google.com/run/docs/securing/service-identity#default_service_account).
    * The Cloud Build default service account has permissions to push to and pull from Artifact Registry repositories in the same Google Cloud project unless you have disabled automatic role granting to default service accounts.
  * If you are using a Docker client to push and pull images, configure [authentication](https://docs.cloud.google.com/artifact-registry/docs/docker/authentication) to Artifact Registry.
  * Learn about [pushing and pulling images](https://docs.cloud.google.com/artifact-registry/docs/docker/pushing-and-pulling).
  * Learn about [managing images](https://docs.cloud.google.com/artifact-registry/docs/docker/manage-images).
  * Learn how to [manage container metadata](https://docs.cloud.google.com/artifact-registry/docs/docker/manage-metadata) with attachments. Attachments are [OCI artifacts](https://github.com/opencontainers/image-spec/blob/main/manifest.md#guidelines-for-artifact-usage) that hold metadata about another container image.

Metadata can be any relevant information you want to store that is related to a container image, including files you can scan or generate with [Artifact Analysis](https://docs.cloud.google.com/artifact-registry/docs/analysis): 

    * [Software bill of materials (SBOM)](https://docs.cloud.google.com/artifact-analysis/docs/sbom-overview)
    * [Vulnerability scan results](https://docs.cloud.google.com/artifact-analysis/docs/container-scanning-overview)
    * [Other metadata such as build provenance](https://docs.cloud.google.com/artifact-analysis/docs/metadata-management-overview)
  * Set up [Pub/Sub notifications](https://docs.cloud.google.com/artifact-registry/docs/configure-notifications) for changes to your repository.
  * Set up [Artifact Analysis](https://docs.cloud.google.com/artifact-registry/docs/analysis) to manage image metadata and scan for vulnerabilities. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
