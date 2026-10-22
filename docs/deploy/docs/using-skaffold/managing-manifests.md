---
url: https://docs.cloud.google.com/deploy/docs/using-skaffold/managing-manifests/
title: Manage manifests in Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:06.044834+00:00
---

# Manage manifests in Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/using-skaffold/managing-manifests/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback 

#  Manage manifests in Cloud Deploy Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure Cloud Deploy to render the configuration for each target in a delivery pipeline.

**Caution** : Skaffold [will be removed](https://groups.google.com/g/skaffold-users/c/FTR3xLJpePY) from gcloud CLI releases after January 15, 2027. Going forward, Skaffold can be installed following the instructions in the [Installing Skaffold documentation](https://skaffold.dev/docs/install/). On January 29, 2027 the Skaffold GitHub repository will be archived. All existing releases will remain available to users.

Cloud Deploy uses [Skaffold](https://cloud.google.com/skaffold) to render your Kubernetes manifests. The service supports rendering of raw manifests and more advanced manifest-management tools, such as [Helm](https://helm.sh), [Kustomize](https://kustomize.io), and [kpt](https://github.com/GoogleContainerTools/kpt).

The rendering process has two stages:

  1. The manifest-management tool generates the manifest.

  2. Skaffold substitutes the image references in the manifest with the images you want to deploy in your release.




This page includes configuration examples using Helm and Kustomize.

## Using Skaffold to generate your configuration

If you don't already have a Skaffold configuration file (`skaffold.yaml`), you can use Skaffold to generate one for you, based on what's in your repository.

  1. Install Skaffold using Google Cloud CLI:

`gcloud components install skaffold`

  2. Run `skaffold init` in the repository that contains your manifests:

`skaffold init --skip-build`




This command creates a `skaffold.yaml` file in your repository. That file references the manifests in that repository. The contents look like this:
    
    
    apiVersion: skaffold/v4beta7
    kind: Config
    metadata:
      name: sample-app
    manifests:
      rawYaml:
        - k8s-manifests/deployment.yaml
        - k8s-manifests/rbac.yaml
        - k8s-manifests/redis.yaml
        - k8s-manifests/service.yaml
    

## Rendering raw manifests

Raw manifests are manifests that aren't managed by a tool like Helm or Kustomize, and therefore don't need any pre-processing before being hydrated and deployed to a cluster.

By default, Cloud Deploy uses [`skaffold render`](https://skaffold.dev/docs/workflows/ci-cd/#separation-of-rendering-and-deployment) to render your Kubernetes manifests, replacing untagged image names with the tagged image names of the container images you're deploying. Then when you promote the release, Cloud Deploy uses [`skaffold apply`](https://skaffold.dev/docs/workflows/ci-cd/#separation-of-rendering-and-deployment) to apply the manifests and deploy the images to your Google Kubernetes Engine cluster.

**Note:** When you first create the release, deployment happens automatically. Cloud Deploy creates the rollout and deploys into the first target.

A `manifests` stanza from a basic configuration looks like this:
    
    
    manifests:
      rawYaml:
        - PATH_TO_MANIFEST
    

See the [Skaffold documentation](https://skaffold.dev/docs) for more information on what values can be passed here.

## Rendering using Helm

You can use Cloud Deploy to render your [Helm](https://helm.sh) charts. To do so, you include Helm chart details in a `deploy` stanza in a Skaffold profile.

Each such definition looks like this:
    
    
    apiVersion: skaffold/v4beta7
    kind: Config
    manifests:
      helm:
        releases:
          - name: RELEASE_NAME
            chartPath: PATH_TO_HELM_CHART
    

Where:

RELEASE_NAME is the name of the Helm chart instance for this release.

PATH_TO_HELM_CHART is the local path to a packaged Helm chart or an unpacked Helm chart directory.

You can use additional Helm configuration options, as described in the [Skaffold documentation](https://skaffold.dev/docs/deployers/helm/)

## Rendering using Kustomize

You can use [Kustomize](https://kustomize.io) with Cloud Deploy. To do so, you point to the Kustomization files from within the `deploy` stanza in your `skaffold.yaml` profile configuration.

You include a separate Kustomize configuration for each target for which you're using Kustomize, under each corresponding `profile` in your `skaffold.yaml`.

Each such definition looks like this:
    
    
    apiVersion: skaffold/v4beta7
    kind: Config
    manifests:
      kustomize:
        paths:
          - PATH_TO_KUSTOMIZE
    

Where:

PATH_TO_KUSTOMIZE points to your Kustomization files. The default is `["."]`

You can use additional Kustomize configuration options, as described in the [Skaffold documentation](https://skaffold.dev/docs/renderers/kustomize/)

## Configuring different manifests per target

Often each target needs a slightly different configuration. For example, you might have more replicas in your production deployments than in your staging deployments.

You can render a different set of manifests for each target by providing each variation as a different [Skaffold profile](https://skaffold.dev/docs/environment/profiles/).

### Profiles with Raw manifests

When working with raw manifests you can point Cloud Deploy at a different file, depending on the target. You could configure that as follows:
    
    
    apiVersion: skaffold/v4beta7
    kind: Config
    profiles:
      - name: prod
        manifests:
          rawYaml:
            - prod.yaml
      - name: staging
        manifests:
          rawYaml:
            - staging.yaml
    

### Profiles with Kustomize

Here's an example `skaffold.yaml` that has different profiles for staging and production using Kustomize, where each profile points to a different Kustomization:
    
    
    apiVersion: skaffold/v4beta7
    kind: Config
    profiles:
      - name: prod
        manifests:
          kustomize:
            paths:
              - environments/prod
      - name: staging
        manifests:
          kustomize:
            paths:
              - environments/staging
    

### Profiles referenced in the delivery pipeline

These profiles, defined in `skaffold.yaml`, are referenced in the [delivery pipeline config](https://docs.cloud.google.com/deploy/docs/config-files), per target:
    
    
    serialPipeline:
      stages:
      - targetId: staging-target
        profiles:
        - staging
      - targetId: prod-target
        profiles:
        - prod
    

## Substitute a specific image when you create the release

Your manifest can use a placeholder for the image name, which you can substitute when you create your release.

Here's an example of a manifest with a placeholder for the image:
    
    
    apiVersion: v1
    kind: Deployment
    metadata:
      name: getting-started
      labels:
        app: nginx
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: nginx
      template:
        metadata:
          labels:
            app: nginx
        spec:
          containers:
          - name: nginx
            image: **my-app-image**
    

When you create your release, you can use the `--images=` flag to identify the specific image to deploy. For example, the following command creates a release and substitutes a SHA-qualified image name for the placeholder name:
    
    
    gcloud deploy releases create test-release-001 \
      --project=test-gke-using-deployment \
      --region=us-central1 \
      --delivery-pipeline=my-gke-demo-app-1 \
      --images=my-app-image=gcr.io/google-containers/nginx@sha256:f49a843c290594dcf4d193535d1f4ba8af7d56cea2cf79d1e9554f077f1e7aaa
    

The resulting rendered manifest now has a reference to the specified image instead of `my-app-image`.

## What's next

  * Learn more about [Cloud Deploy delivery pipeline configuration](https://docs.cloud.google.com/deploy/docs/config-files).
  * Try the [Cloud Deploy Skaffold profiles walkthrough](https://shell.cloud.google.com/?show=ide%2Cterminal&walkthrough_id=deploy--cloud-deploy-profiles-gke)
  * Learn more about [Kustomize](https://kustomize.io).
  * Learn more about [Helm](https://helm.sh).
  * Learn more about [Kpt](https://googlecontainertools.github.io/kpt)
  * Consider using [Artifact Registry](https://cloud.google.com/artifact-registry) to store artifacts such as Helm charts or Kustomizations.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
