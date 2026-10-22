---
url: https://docs.cloud.google.com/marketplace/docs/partners/migrations/container-image-annotations/
title: Migrate to annotating container images with their service name \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:11:46.212139+00:00
---

# Migrate to annotating container images with their service name  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/migrations/container-image-annotations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Develop ](https://docs.cloud.google.com/marketplace/docs/partners/develop)



Send feedback 

#  Migrate to annotating container images with their service name Stay organized with collections  Save and categorize content based on your preferences. 

Starting January 20, 2025, Google Cloud Marketplace is requiring that all new or updated deployments of Google Kubernetes Engine app product listings or container image products contain an annotation in their image manifest that identifies the service name of the product. This annotation has the following format:
    
    
    com.googleapis.cloudmarketplace.product.service.name=services/SERVICE_NAME
    

Replace SERVICE_NAME with the name of your service (for example, `example.endpoints.example-project.cloud.goog`). You can find the service name for your product on the **Overview** page in Producer Portal, in the **Service name** column.

An annotation is a key-value pair that's added to the image manifest. For more information about annotations, see the Open Container Initiative's documentation of [annotations](https://github.com/opencontainers/image-spec/blob/main/annotations.md) on GitHub.

## Add the annotation to your container image manifest

To add the annotation to your container image manifest, use a tool like [Docker](https://docs.docker.com/engine/reference/builder/) or [Crane](https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane.md).

  * For steps to add an annotation with Docker, see [Add annotations](https://docs.docker.com/build/metadata/annotations/#add-annotations) in the Docker documentation.
  * For steps to add an annotation with Crane, see [crane mutate](https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_mutate.md) in the Crane documentation.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
