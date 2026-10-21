---
url: https://docs.cloud.google.com/artifact-registry/docs/troubleshooting/
title: General troubleshooting \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:11:16.313129+00:00
---

# General troubleshooting  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  General troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

Learn about troubleshooting steps that apply to all artifact formats when working with Artifact Registry. For issues specific to an artifact format, refer to the format-specific page.

  * Container images: [Container images](https://docs.cloud.google.com/artifact-registry/docs/docker/troubleshoot), [Helm charts](https://docs.cloud.google.com/artifact-registry/docs/helm/troubleshoot)
  * Language packages: [Java](https://docs.cloud.google.com/artifact-registry/docs/java/troubleshoot), [Node.js](https://docs.cloud.google.com/artifact-registry/docs/nodejs/troubleshoot), [Python](https://docs.cloud.google.com/artifact-registry/docs/python/troubleshoot)
  * [OS packages](https://docs.cloud.google.com/artifact-registry/docs/os-packages/troubleshoot)



## Vulnerability scanning for Red Hat Enterprise Linux minor versions

Artifact Analysis delivers vulnerability scanning results for Red Hat Enterprise Linux (RHEL) based on the latest minor version of each major version released. If you scan an older minor version, then you may get inaccurate results.

## Invalid repository or location in commands

Use the following information to help you diagnose invalid repository location or invalid repository name errors.

### Location and repository defaults for gcloud

If you set a default [repository and location](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults) in the Google Cloud CLI so that you can omit `--location` and `--repository` flags from `gcloud artifacts` commands, try running the command that failed with the flags and corresponding values. For details about the syntax for a particular command, run the command with the `--help` flag.

The default repository setting does not apply to `gcloud artifacts` commands where you specify a repository name without the `--repository` flag. For example, you must specify the repository name in a [gcloud artifacts repositories describe](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/repositories/describe) command like the following example:
    
    
    gcloud artifacts repositories describe my-repo --location=us-west1
    

If your command still fails, you might need to verify that you specified valid values for the repository or location.

### Repository location

To list all supported Artifact Registry locations, run the command:
    
    
    gcloud artifacts locations list
    

Your organization policy might include [location restrictions](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services#artifact-registry). Artifact Registry enforces these restrictions at repository creation time. Artifact Registry does not enforce policy retroactively on repositories that predate the location restrictions.

### Repository names in gcloud commands

You can list repositories to view the repository names in a specified project or location.

To list all repositories in a project, run the command:
    
    
    gcloud artifacts repositories list --project=PROJECT-ID \
        --location=all
    

To list all repositories in a location, run the command:
    
    
    gcloud artifacts repositories list --project=PROJECT-ID \
        --location=LOCATION
    

Replace PROJECT-ID with your Google Cloud project ID and LOCATION with the repository location.

The command returns information for each repository similar to the following example:
    
    
    REPOSITORY: my-repo
    FORMAT: DOCKER
    DESCRIPTION:
    LOCATION: us-west1
    LABELS:
    ENCRYPTION: Google-owned and Google-managed encryption key
    CREATE_TIME: 2021-09-23T19:39:10
    UPDATE_TIME: 2021-09-23T19:39:10
    

The value for `REPOSITORY` is the value you use with `gcloud artifacts` commands that include the repository name as a parameter.

For example, this command uses the `--repository` flag:
    
    
    gcloud artifacts packages list --location=us-west1 --repository=my-repo
    

This command uses the repository name only without a flag:
    
    
    gcloud artifacts repositories describe my-repo --location=us-west1
    

### Repository names with third-party clients

For third-party clients, you generally use a full repository path when configuring clients, such as `us-west1-docker.pkg.dev/my-project/my-repo`. You then follow the conventions of the client for uploading and downloading packages. For client configuration and usage details, refer to the documentation for the format you are working with.

  * Container images: [Docker](https://docs.cloud.google.com/artifact-registry/docs/docker), [Helm](https://docs.cloud.google.com/artifact-registry/docs/helm)
  * Language packages: [Java](https://docs.cloud.google.com/artifact-registry/docs/java), [Node.js](https://docs.cloud.google.com/artifact-registry/docs/nodejs), [Python](https://docs.cloud.google.com/artifact-registry/docs/python), [Go](https://docs.cloud.google.com/artifact-registry/docs/go)
  * OS packages: [Debian](https://docs.cloud.google.com/artifact-registry/docs/os-packages/debian), [RPM](https://docs.cloud.google.com/artifact-registry/docs/os-packages/rpm)

If you are transitioning from Container Registry, note that all image paths must include an Artifact Registry repository name. You cannot specify an image path that only includes a project ID. 
  * **Invalid path** : `us-east1-docker.pkg.dev/my-project/my-image`
  * **Valid path** : `us-east1-docker.pkg.dev/my-project/my-repo/my-image`



## Cannot push or pull from undeleted repositories

Repositories no longer work properly after you undelete a Google Cloud project or enable the Artifact Registry API after disabling it.

If you disable the Artifact Registry API or [delete the project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#shutting_down_projects), Artifact Registry services become unavailable. Artifact Registry deletes repository data after 7 days.

[Learn more about data deletion on Google Cloud](https://cloud.google.com/docs/security/deletion).

## Error pulling the Prometheus sidecar for Cloud Run in a service perimeter

You're [using Artifact Registry with VPC Service Controls](https://docs.cloud.google.com/artifact-registry/docs/securing-with-vpc-sc#ar-vpc) and you try to pull the image of the [Prometheus sidecar for Cloud Run](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/cloudrun-sidecar) within a service perimeter. You receive a `403 permission denied` error.

To address this issue, allow egress to the `cloud-ops-agents-artifacts` project in the egress rule you configured to use `mirror.gcr.io` in your service perimeter. To do so, add `projects/1042947621568` as a resource in your egress rule.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
