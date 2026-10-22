---
url: https://docs.cloud.google.com/deploy/docs/select-tool-version/
title: Manage tool versions \u00a0|\u00a0 Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:00.096616+00:00
---

# Manage tool versions  |  Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/select-tool-version/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback 

#  Manage tool versions Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Deploy performs its operations using a custom image, which includes default tool versions. Cloud Deploy provides you with flexibility and control over your deployment process by allowing you to specify tool versions to use in operations to render, deploy, and verify your manifests.

This page describes how Cloud Deploy tool versions are selected and the maintenance and support time for each tool version.

**Note:** By default, Cloud Deploy now uses Kustomize through [kubectl kustomize](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_kustomize/). You can still use kustomize directly (not through kubectl) by specifying the kustomize version when you create a release.

## Supported Cloud Deploy Tool Versions

Cloud Deploy lets you select the versions for the following tools:

  * [`Docker`](https://console.cloud.google.com/artifacts/generic/cd-image-prod/us-central1/tools/docker?project=cd-image-prod)
  * [`Kubectl`](https://console.cloud.google.com/artifacts/generic/cd-image-prod/us-central1/tools/kubectl?project=cd-image-prod)
  * [`Kpt`](https://console.cloud.google.com/artifacts/generic/cd-image-prod/us-central1/tools/kpt?project=cd-image-prod)
  * [`Helm`](https://console.cloud.google.com/artifacts/generic/cd-image-prod/us-central1/tools/helm?project=cd-image-prod)
  * [`Kustomize`](https://console.cloud.google.com/artifacts/generic/cd-image-prod/us-central1/tools/kustomize?project=cd-image-prod)
  * [`Skaffold`](https://console.cloud.google.com/artifacts/generic/cd-image-prod/us-central1/tools/skaffold?project=cd-image-prod)



**Caution** : Skaffold [will be removed](https://groups.google.com/g/skaffold-users/c/FTR3xLJpePY) from gcloud CLI releases after January 15, 2027. Going forward, Skaffold can be installed following the instructions in the [Installing Skaffold documentation](https://skaffold.dev/docs/install/). On January 29, 2027 the Skaffold GitHub repository will be archived. All existing releases will remain available to users.

Cloud Deploy provides a [repository](https://console.cloud.google.com/artifacts/generic/cd-image-prod/us-central1/tools?project=cd-image-prod) of available tool versions that you can use for your operations. All of these versions are subject to the maintenance and deprecation policy.

### Default tool versions

If no user-specified tool versions are supplied, default tool versions are used during release creation.

A new Cloud Deploy image is released every week containing the latest tool versions available at the time the image is built. Based on the timing of different release schedules of the tools, a new tool version may take up to two weeks to become the default.

You can view the default versions by running the following command:
    
    
    gcloud deploy get-config \
          --project=PROJECT \
          --region=REGION \
          --format 'yaml(defaultToolVersions)'
    

### Fixed Tool Versioning

All tool versions are saved onto the release resource by default. The tool versions are associated with a release at release creation and are used for the entire lifecycle of that release, and cannot be changed during that lifetime. The release lifecycle consists of all render, deploy, and other jobs on that release. This includes up to deployment into the final target in the progression, and beyond (rollbacks or redeployments). You can find the tool versions associated with a release by running the following command:
    
    
    gcloud deploy releases describe RELEASE_NAME \
           --delivery-pipeline=PIPELINE_NAME \
           --project=PROJECT \
           --region=REGION \
           --format='yaml(toolVersions)'
    

Releases created before the tool versioning feature won't have toolVersions listed in their output. Instead you can see their Skaffold version with the `--format 'yaml(skaffoldVersion)'` flag.

#### Disable fixed tool versioning

If you want to disable fixed tool versioning and use the latest tools for a given release, you can do so by specifying the special keyword `latest` for each tool. Here's an example of creating a release that uses the latest versions for all tools:
    
    
    gcloud deploy releases create RELEASE_NAME \
           --delivery-pipeline=PIPELINE_NAME \
           --project=PROJECT \
           --region=REGION \
           --docker-version=latest \
           --helm-version=latest \
           --kpt-version=latest \
           --kubectl-version=latest \
           --kustomize-version=latest \
           --skaffold-version=latest
    

### How to specify a particular tool version to use

You can use any of the supported tool versions. To specify the version that you want to use, include the appropriate flag for specific tool:
    
    
    gcloud deploy releases create RELEASE_NAME \
           --delivery-pipeline=PIPELINE_NAME \
           --project=PROJECT \
           --region=REGION \
           --docker-version=DOCKER_VERSION \
           --helm-version=HELM_VERSION \
           --kpt-version=KPT_VERSION \
           --kubectl-version=KUBECTL_VERSION \
           --kustomize-version=KUSTOMIZE_VERSION \
           --skaffold-version=SKAFFOLD_VERSION
    

For any tools where you want to use the default version, you can omit the corresponding version flag.

For example, the following command uses Skaffold `2.16.1` and Helm `3.18.3`:
    
    
    gcloud deploy releases create release-001 \
                                  --delivery-pipeline=PIPELINE_NAME \
                                  --skaffold-version=2.16.1 \
                                  --helm-version=3.18.3 \
                                  --project=PROJECT \
                                  --region=REGION
    

### Tool version compatibility

Cloud Deploy takes responsibility for ensuring that the tool versions are compatible on the Cloud Deploy image. If you use the tool version replacement feature to replace tool versions on the Cloud Deploy image, then you're responsible for choosing compatible tool versions.

## Tool version deprecation and maintenance policy

Tool versions are supported for 12 months with a 60-day maintenance period, from the day they are imported. This maintenance period means that releases tied to a tool version are still supported for 60 days after support for that tool version has expired. You can still create rollouts from those releases, but you can't create _releases_ using a tool version that's in the maintenance period.

After the 60-day maintenance period, the tool version is no longer supported for any operations. You can no longer create rollouts from a release that uses the unsupported version. However, all data associated with the release remains.

You can view the maintenance and expiration dates on the release by running the following command:
    
    
    gcloud deploy releases describe RELEASE_NAME \
           --delivery-pipeline=PIPELINE_NAME \
           --project=PROJECT \
           --region=REGION \
           --format 'yaml(condition)'
    

You can also view the maintenance and expiration date of a specific tool by running the command:
    
    
    gcloud artifacts versions list \
           --package TOOL_NAME \
           --repository tools \
           --project cd-image-prod \
           --location=REGION
    

The maintenance and expiration dates are available as annotations on the respective versions.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
