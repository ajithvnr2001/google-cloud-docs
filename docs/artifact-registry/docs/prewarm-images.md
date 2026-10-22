---
url: https://docs.cloud.google.com/artifact-registry/docs/prewarm-images/
title: Reduce latency with image prewarming \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:43.215389+00:00
---

# Reduce latency with image prewarming  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/prewarm-images/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Reduce latency with image prewarming Stay organized with collections  Save and categorize content based on your preferences. 

Prewarming images lets you explicitly trigger the downloading of container images into the **Image Streaming** cache before a runtime client requests them. This effectively eliminates the "cold start" latency associated with the first pull of a new image version for workloads using [image streaming](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/image-streaming).

## Overview

When you push an image to Artifact Registry, it's stored in an underlying storage system. For low-latency access, Artifact Registry also uses an **Image Streaming** cache, which typically populates on the first pull from a client that has image streaming enabled. For latency-sensitive workloads, like scaling up a Google Kubernetes Engine cluster, waiting for this cache to warm up can cause delays. Prewarming helps get images into the Image streaming cache in advance.

The **Prewarm Artifact** API lets you manually request that a specific image version or tag is precached. You also specify a retention period to ensure the image remains in the cache for a specified duration.

## Limitations

  * API only: prewarming is available only using the Artifact Registry REST API. Prewarming is not available using the Google Cloud console.
  * GKE only: Prewarming is only effective for GKE clusters with [Image Streaming](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/image-streaming) enabled. Image streaming requires specific software running on the client node.
  * Single artifact: you can prewarm only one artifact (version or tag) per API request.
  * Multi-architecture images: Not supported. Use the specific version for an architecture image.
  * Project limit: There is an overall limit of 100 GB per consumer project for prewarmed images. When the limit is reached, older images are evicted to make space for new images.



## Before you begin

  1. Enable the Artifact Registry API. For more information, see [Enable Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/enable-service).
  2. Install the gcloud CLI to obtain authentication tokens for REST API requests.



### Required roles

To get the permissions that you need to manage prewarmed images, ask your administrator to grant you the following IAM roles on the repository: 

  * Prewarm or remove artifacts from cache (`artifactregistry.repositories.prewarmArtifact`, `artifactregistry.repositories.removePrewarmedArtifact`): [Artifact Registry Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.writer) (`roles/artifactregistry.writer`) 
  * Check or list prewarmed artifacts (`artifactregistry.repositories.checkPrewarmedArtifact`, `artifactregistry.repositories.listPrewarmedArtifacts`): [Artifact Registry Reader ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.reader) (`roles/artifactregistry.reader`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

This permission model ensures that only users with write access can manage the cache state, preventing unauthorized users from overfilling the cache. Meanwhile, users with read access can verify which artifacts are available for streaming.

## Prewarm an image

To prewarm an image, you make a `POST` request to the `:prewarmArtifact` method of your repository.

### REST API

Reference: [`projects.locations.repositories.prewarmArtifact`](https://docs.cloud.google.com/artifact-registry/docs/reference/rest/v1/projects.locations.repositories/prewarmArtifact)

The request body has the following structure:
    
    
    {
      "version": "projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY/packages/PACKAGE/versions/VERSION",
      "retention_days": 3
    }
    

Alternatively, use a tag:
    
    
    {
      "tag": "projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY/packages/PACKAGE/tags/TAG",
      "retention_days": 3,
      "force": true
    }
    

Field | Description  
---|---  
`tag` | **Optional**. The specific artifact tag to prewarm. You must specify either a `version` or a `tag`.  
`version` | **Optional**. The specific artifact version to prewarm. You must specify either a `version` or a `tag`.  
`retention_days` | **Optional**. The number of days to keep the artifact in the cache. If you don't specify this field, the default is 3 days.  
`force` | **Optional**. If `true`, the system might evict older artifacts to make space for this one.  
`stream_location` | **Optional**. The specific region where the image will be prewarmed. By default, this matches the image location. Note that multi-region configurations are not supported. If a broad region is specified, the defaults are us-central1 (US), europe-north1 (EU), and asia-east1 (Asia).  
  
#### Example: Prewarm a specific version

The following example prewarms the version `sha256:52e...` of the `nginx` package in the `my-repo` repository in "us-east1" region.
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{
        "version": "projects/my-project/locations/us-central1/repositories/my-repo/packages/nginx/versions/sha256:52e85304675567b5e656f5e997576a9d20c57176",
        "retention_days": 7,
        "stream_location": "us-east1",
      }' \
      "https://artifactregistry.googleapis.com/v1/projects/my-project/locations/us-central1/repositories/my-repo:prewarmArtifact"
    
    

#### Example: Prewarm a tag

The following example prewarms the image tagged `production` of the `my-app` package.
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{
        "tag": "projects/my-project/locations/us-central1/repositories/my-repo/packages/my-app/tags/production",
        "force": true
      }' \
      "https://artifactregistry.googleapis.com/v1/projects/my-project/locations/us-central1/repositories/my-repo:prewarmArtifact"
    

## Check prewarm status

To check if an artifact is prewarmed, use the `:checkPrewarmedArtifact` method.
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{
        "version": "projects/my-project/locations/us-central1/repositories/my-repo/packages/nginx/versions/sha256:52e85304675567b5e656f5e997576a9d20c57176"
      }' \
      "https://artifactregistry.googleapis.com/v1/projects/my-project/locations/us-central1/repositories/my-repo:checkPrewarmedArtifact"
    

## List prewarmed artifacts

To list all prewarmed artifacts in a repository, use the `GET` method on the `prewarmedArtifacts` collection. The following example lists all the prewarmed images under `my-repo` in `us-east1`. `stream_location` filter is required.
    
    
    curl -X GET \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      "https://artifactregistry.googleapis.com/v1/projects/my-project/locations/us-central1/repositories/my-repo/prewarmedArtifacts?filter=stream_location=us-east1"/
    

## Remove from cache

To explicitly remove an artifact from the prewarm cache, use the `:removePrewarmedArtifact` method. Use this method to free up space or when a specific image version is no longer needed in the cache.
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{
        "version": "projects/my-project/locations/us-central1/repositories/my-repo/packages/nginx/versions/sha256:52e85304675567b5e656f5e997576a9d20c57176"
      }' \
      "https://artifactregistry.googleapis.com/v1/projects/my-project/locations/us-central1/repositories/my-repo:removePrewarmedArtifact"
    

## What's next

  * [Push and pull container images](https://docs.cloud.google.com/artifact-registry/docs/docker/pushing-and-pulling)
  * [Manage container images](https://docs.cloud.google.com/artifact-registry/docs/docker/manage-images)
  * Learn more about [Image Streaming in Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/image-streaming)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
