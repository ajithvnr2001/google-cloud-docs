---
url: https://docs.cloud.google.com/artifact-registry/docs/helm/
title: Work with Helm charts \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:36:16.931121+00:00
---

# Work with Helm charts  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/helm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Work with Helm charts Stay organized with collections  Save and categorize content based on your preferences. 

You can store Helm 3 charts saved as [OCI container images](https://helm.sh/docs/topics/registries/) in Artifact Registry Docker repositories.

  * To get familiar with Helm charts in Artifact Registry, try the [quickstart](https://docs.cloud.google.com/artifact-registry/docs/helm/store-helm-charts).
  * To learn about working with other container images, see the [Docker overview](https://docs.cloud.google.com/artifact-registry/docs/docker).

**Note:** Artifact Registry only supports OCI-packaged Helm charts. Native Helm charts aren't supported.

When you are ready to learn more about managing Helm charts, read the following information:

  1. [Create a Docker repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos) for your images.

If you are managing both container images and Helm charts in Artifact Registry, use one of these approaches to keep your charts organized:

     * Create separate repositories for your images and Helm charts.
     * Store images and charts under separate namespaces in the same repository. In the following example, the repository `my-repo` has separate namespaces for images and charts.
           
           us-west1-docker.pkg.dev/my-project/my-repo/images
           us-west1-docker.pkg.dev/my-project/my-repo/charts
           

  2. [Grant permissions](https://docs.cloud.google.com/artifact-registry/docs/access-control) to the account that will connect with the repository. Service accounts for common integrations with Artifact Registry have default [permissions](https://docs.cloud.google.com/artifact-registry/docs/access-control#gcp) for repositories in the same project.

  3. Configure Helm to [authenticate](https://docs.cloud.google.com/artifact-registry/docs/helm/authentication) with Artifact Registry.

  4. Learn about [managing charts](https://docs.cloud.google.com/artifact-registry/docs/helm/manage-charts).

  5. Set up [Pub/Sub notifications](https://docs.cloud.google.com/artifact-registry/docs/configure-notifications) for changes to your repository.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
