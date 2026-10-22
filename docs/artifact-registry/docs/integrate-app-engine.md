---
url: https://docs.cloud.google.com/artifact-registry/docs/integrate-app-engine/
title: Deploying to App Engine \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:09.520045+00:00
---

# Deploying to App Engine  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/integrate-app-engine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Deploying to App Engine Stay organized with collections  Save and categorize content based on your preferences. 

Artifact Registry lets you store private container images and language packages for your App Engine applications. You can declare Node.js and Python dependencies in Artifact Registry and deploy your applications using Cloud Build.

**Note:** App Engine and Cloud Build create [Pub/Sub](https://docs.cloud.google.com/pubsub/docs) topics and subscriptions in your project for use in Google's internal analysis and maintenance of your container images. These Pub/Sub push subscriptions have `rpc://` URL targets.

## Required permissions

App Engine flexible environment
    If App Engine flexible environment and Artifact Registry are in the same project, the App Engine [default service account](https://docs.cloud.google.com/appengine/docs/standard/python/service-account) has permissions to pull containers from repositories.
    If you also use Cloud Build to containerize your applications and store them in Artifact Registry, [grant](https://docs.cloud.google.com/artifact-registry/docs/access-control#grant) the Artifact Registry Writer role to the Cloud Build service account.
App Engine standard environment:
    App Engine standard environment uses the [Cloud Build service account](https://docs.cloud.google.com/build/docs/cloud-build-service-account) to build and deploy your applications, including integration of dependencies stored in Artifact Registry. 

  * If App Engine and Artifact Registry are in the same Google Cloud project, the service account has the necessary permissions to download from repositories.
  * If App Engine and Artifact Registry are in different projects, you must grant repository access to the service account.
  * To provide read-only access for downloading dependencies, [grant](https://docs.cloud.google.com/artifact-registry/docs/access-control#grant) the Artifact Registry Reader role to the Cloud Build service account.
  * If you also use Cloud Build to upload artifacts to repositories, [grant](https://docs.cloud.google.com/artifact-registry/docs/access-control#grant) the Artifact Registry Writer role to the Cloud Build service account.



## Configure access to dependencies

For standard environment applications, see the App Engine standard environment documentation for [npm](https://docs.cloud.google.com/appengine/docs/standard/nodejs/specifying-dependencies#private_dependencies_with_artifact_registry) and [Python](https://docs.cloud.google.com/appengine/docs/standard/python3/specifying-dependencies#private_dependencies_with_artifact_registry) configuration instructions.

To include dependencies in builds you run with Cloud Build, see [Integrating with Cloud Build](https://docs.cloud.google.com/artifact-registry/docs/configure-cloud-build).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
