---
url: https://docs.cloud.google.com/artifact-registry/docs/ar-service-account/
title: Artifact Registry Service Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:48:26.767289+00:00
---

# Artifact Registry Service Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/ar-service-account/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Artifact Registry Service Agent Stay organized with collections  Save and categorize content based on your preferences. 

Artifact Registry uses a Google-managed service account, called the Artifact Registry Service Agent, to act on your behalf when connecting to other Google Cloud services. You can grant IAM roles to the service agent so that it can integrate with services such as customer-managed encryption keys (CMEK) in Cloud Key Management Service and repository event notifications in Pub/Sub.

Artifact Registry creates the Artifact Registry Service Agent when you create the first Artifact Registry repository in a Google Cloud project. The service agent identifier is:

`service-PROJECT-NUMBER@gcp-sa-artifactregistry.iam.gserviceaccount.com`

PROJECT-NUMBER is the [project number](https://docs.cloud.google.com/resource-manager/docs/view-update-projects#identifying_projects) of the Google Cloud project where Artifact Registry is running.

You can manually create the service agent in a project without any repositories with the command:
    
    
    gcloud beta services identity create \
        --service=artifactregistry.googleapis.com \
        --project=PROJECT-ID
    

Replace `PROJECT-ID` with the Google Cloud project ID.

The Artifact Registry Service Agent is granted the Artifact Registry Service Agent role (`roles/artifactregistry.serviceAgent`) for resources in the project. To enforce the security principle of least privilege, the role only has the minimum required permissions:

  * Publish Pub/Sub topics: `pubsub.topics.publish`
  * Download artifacts from Artifact Registry repositories: `artifactregistry.repositories.downloadArtifacts`
  * Read repository metadata: `artifactregistry.repositories.get`
  * Read artifacts using virtual repositories: `artifactregistry.repositories.readViaVirtualRepository`
  * Delete artifacts: `artifactregistry.versions.delete`



## What's next

Learn about [Artifact Registry roles and configuring access to repositories](https://docs.cloud.google.com/artifact-registry/docs/access-control).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
