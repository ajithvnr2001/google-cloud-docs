---
url: https://docs.cloud.google.com/artifact-registry/docs/docker/troubleshoot/
title: Troubleshoot container image issues \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:39:47.161907+00:00
---

# Troubleshoot container image issues  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/docker/troubleshoot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Troubleshoot container image issues Stay organized with collections  Save and categorize content based on your preferences. 

Learn about troubleshooting steps that you might find helpful if you run into problems managing container images in Artifact Registry.

### Project ID syntax in the Docker CLI

Because of how Docker treats colons, when you use the Docker CLI, you must replace colons (`:`) in your project ID with a forward slash (`/`). For more information, see [Domain-scoped projects](https://docs.cloud.google.com/artifact-registry/docs/docker/names#domain). 

### Cannot pull an image or deploy to a Google Cloud runtime environment

Check the following:

  1. Verify that the full path of the image that you are pushing is correct. The path must include the registry hostname, Google Cloud, project ID, repository, and image. For example: 
         
         us-west1-docker.pkg.dev/my-project/my-repo/my-image:v1

For more information, see [Repository and image names](https://docs.cloud.google.com/artifact-registry/docs/docker/names).
  2. Verify that the account that is pulling the image has the correct [permissions](https://docs.cloud.google.com/artifact-registry/docs/access-control) to read from the repository. If you have [disabled automatic role granting to service accounts](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants), then you must grant Artifact Registry roles to the runtime service accounts.
     * For Compute Engine, Cloud Run, and Google Kubernetes Engine service accounts, you must grant the Artifact Registry Reader role (`roles/artifactregistry.reader`) to the runtime service account.
     * For your Cloud Build service account, you must grant the Artifact Registry Writer role (`roles/artifactregistry.writer`) to the service account that runs builds.
     * If you are using Docker or another third-party tool, you must: 
       * [Grant permissions](https://docs.cloud.google.com/artifact-registry/docs/access-control#grant) to the account that interacts with the repository.
       * Configure the client to authenticate to the repository. 
         * [Docker authentication](https://docs.cloud.google.com/artifact-registry/docs/docker/authentication) instructions
         * [Troubleshooting containerd node images on Google Kubernetes Engine](https://docs.cloud.google.com/artifact-registry/docs/integrate-gke#troubleshooting_containerd_node_images)



### Cannot push an image to Artifact Registry

Try the following:

  1. Verify that the repository exists. Unlike Container Registry, repository creation is a separate operation from pushing the first image. If the repository does not exist, then [create](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos) it.
  2. Verify that the full path of the image that you are pushing is correct. The path must include the registry hostname, Google Cloud project ID, repository, and image. For example: 
         
         us-west1-docker.pkg.dev/my-project/my-repo/my-image:v1
           

Each Artifact Registry repository is a separate resource, so you cannot push an image to a path without a repository. For example, `us-west1-docker.pkg.dev/my-project/my-image:v1` is an invalid image path.

For more information, see [Repository and image names](https://docs.cloud.google.com/artifact-registry/docs/docker/names).

  3. Verify that the account that is pushing the image has [permissions](https://docs.cloud.google.com/artifact-registry/docs/access-control) to write to the repository. If you have [disabled automatic role granting to service accounts](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants), then you must grant Artifact Registry roles to the runtime service accounts.
     * For Compute Engine, Cloud Run, and Google Kubernetes Engine service accounts, you must grant the Artifact Registry Writer role (`roles/artifactregistry.writer`) to the runtime service account.
     * For your Cloud Build service account, you must grant the Artifact Registry Writer role (`roles/artifactregistry.writer`) to the service account that runs builds.
  4. If Artifact Registry returned the message `The repository has enabled tag immutability`, then tag immutability is configured for the repository. You cannot push an image with a tag that is already used for another version of the same image in the repository. Try to push the image again with a tag that is not used by other stored versions of the image. 

To verify that the a repository is configured for immutable image tags, check the **Immutable image tags** column in the list of repositories in Google Cloud console or run the following command:
         
         gcloud artifacts repositories describe REPOSITORY \
               --project=PROJECT-ID \
               --location=LOCATION
           




### ImagePullBackOff and ErrImagePull messages

Messages with `ImagePullBackOff` and `ErrImagePull` indicate that an image cannot be pulled from the registry by GKE.

  * Verify the [requirements](https://docs.cloud.google.com/artifact-registry/docs/integrate-gke#permissions) to pull from Artifact Registry.
  * Review [Troubleshoot image pulls](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/image-pulls) in the GKE documentation.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
