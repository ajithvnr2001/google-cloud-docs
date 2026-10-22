---
url: https://docs.cloud.google.com/artifact-registry/docs/repositories/
title: Repository overview \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:27:31.878435+00:00
---

# Repository overview  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/repositories/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Repository overview Stay organized with collections  Save and categorize content based on your preferences. 

Artifact Registry enables you to store different artifact types, create multiple repositories in a single project, and associate a specific regional or multi-regional location with each repository. This page describes considerations to help you plan the locations and organization of your repositories. 

Consider both internal processes for creating your artifacts and the usage by consumers of your artifacts when you create your repositories.

## Repository formats

Each repository is associated with a specific artifact [format](https://docs.cloud.google.com/artifact-registry/docs/supported-formats). For example, a Docker repository stores Docker images. You can create multiple repositories for each format in the same Google Cloud project.

## Repository modes

There are multiple repository modes. Each mode serves a different purpose, so you cannot change the repository mode after you have created a repository.

### Standard repository

Standard repositories are regular Artifact Registry repositories for your private artifacts. You upload and download artifacts directly with these repositories and use Artifact Analysis to scan for vulnerabilities and other metadata.

To create standard repositories, follow the steps in [Create standard repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos).

### Remote repository

Remote repositories are read-only repositories that act as proxies to store artifacts from the following upstream sources:

  * Standard Artifact Registry repositories.
  * External sources such as Docker Hub, Maven Central, the Python Package Index (PyPI), Debian or CentOS.



The first time you request an artifact version, the repository downloads it from the upstream source and caches a copy of it. The remote repository serves the cached copy when the same version is requested again.

Remote repositories reduce latency and improve availability for builds and deployments on Google Cloud. You can also use Artifact Analysis to scan cached packages for vulnerabilities and other metadata.

To learn more about remote repositories, read [Remote repository overview](https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-overview). To create remote repositories, follow the steps in [Create remote repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-repo). 

### Connector repository (Preview)

Connector repositories act as proxies to upstream sources while helping to ensure that all requests are handled by the upstream source. Unlike remote repositories, connector repositories don't cache artifacts. As a result, connector repositories are useful if you require full auditability of upstream sources or if you must comply with third-party policies that prevent artifact caching.

To learn more about connector repositories, read [Connector repository overview](https://docs.cloud.google.com/artifact-registry/docs/repositories/connector-overview). To create connector repositories, follow the steps in [Create connector repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/connector-repo). 

### Virtual repository

A read-only repository that acts as a single access point to download, install, or deploy artifacts of the same format from one or more _upstream repositories_. An upstream repository can be a standard, remote, or virtual repository.

Virtual repositories simplify client configuration for consumers of your artifacts. You can also mitigate [dependency confusion attacks](https://docs.cloud.google.com/software-supply-chain-security/docs/dependencies#public-dependencies) by configuring your upstream policy to prioritize repositories with your private artifacts over remote repositories that cache public artifacts.

To learn more about virtual repositories, read [Virtual repository overview](https://docs.cloud.google.com/artifact-registry/docs/repositories/virtual-overview). To create virtual repositories, follow the steps in [Create virtual repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/virtual-repo). 

### Repository usage example

The following diagram shows one of many possible ways you can use repositories in different modes together. The diagram shows a workflow across two Google Cloud projects. In a development project, developers build a Java application. In a separate runtime project, another build creates a container image with the application for deployment to Google Kubernetes Engine.

![Standard, virtual, and remote repositories used across two projects.](https://docs.cloud.google.com/artifact-registry/docs/images/repo-types.svg)

  1. In the development project, a Java development team uses Cloud Build to build a Java application.

     * The build can request public Java dependencies using the virtual repository. The virtual repository serves the dependencies from the remote repository, which is a caching proxy for Maven Central.
     * Cloud Build uploads the package to the standard Maven repository in the component project.
  2. In the runtime project, Cloud Build containerizes the Java application.

The build uses the Maven virtual repository to download the application. The virtual repository serves the package from the standard repository in the development project. The build can also download public Java dependencies from the same virtual repository.

  3. In the runtime project, Cloud Build uploads the built container image to a standard Docker repository.

  4. GKE pulls images from the Docker virtual repository.

     * The upstream standard Docker repository provides private images, such as the containerized Java application.
     * The upstream remote repository provides images that GKE requests from Docker Hub.



In this example, all repositories, builds, and GKE clusters are in the same region. Using the same location for Google Cloud services has benefits which are described in Repository location.

## Repository location

You can create one or more repositories in a supported [region or multi-region](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations). A good repository location balances latency, availability, and bandwidth costs for data consumers. Your organization might also have specific compliance requirements. 

### Location considerations

This section describes why you might want to create a repository in the same region as other Google Cloud services.

You can reduce latency and [network egress](https://docs.cloud.google.com/artifact-registry/pricing#network-egress) costs by creating repositories in the same region where you run GKE, Cloud Run, Cloud Build, and other Google Cloud services that interact with the repository. There is no charge for egress from Artifact Registry to other Google Cloud services in the same region. 

Although there is no charge for egress from a multi-region to a Google Cloud service in a corresponding region, this pricing only applies to a limited set of regions.

  * For the `us` multi-region, egress to a region in the United States such as `us-central` is not charged, to any region in Canada or South America is charged.
  * For the `asia` multi-region, egress to regions in Asia such as `asia-northeast1` are not charged, but egress to regions in Australia are charged.

You can only use image streaming in [GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/image-streaming) and [Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc-serverless/docs/guides/custom-containers#image_streaming) if your container images are stored in Artifact Registry repositories in the same region as your workloads or a multi-region that corresponds to the region with your workloads. Image streaming can reduce workload initialization time significantly when you are using larger container images because workloads can start before the entire image is downloaded. 

Consider the location of consumers outside of Google Cloud. For example, if you developers team in Australia need to download artifacts from Artifact Registry to their local workstations, a repository in an Australian region will reduce latency and incur lower egress charges than a repository located on another continent.

### Restricting repository locations

If you need to comply with regulations or policies that require you to store data in specific regions, you can include a [resource locations constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations) in your Google Cloud organization policy that only allows repository creation in compliant regions. Artifact Registry only enforces the constraint after you include it in your organization policy. If you have existing repositories in non-compliant locations, you must move your artifacts to a repository in a compliant location yourself and then delete the non-compliant repository.

## Cleanup policies

An Artifact Registry _cleanup policy_ defines criteria for automatically deleting artifact versions that you no longer need or keeping artifacts that you want to store indefinitely.

Cleanup policies are useful if you store many versions of your artifacts, but only need to keep specific versions that you release to production. You can define _delete policies_ with criteria for deleting artifacts and _keep policies_ with criteria for retaining artifacts.

If an artifact version matches criteria in both a delete policy and a keep policy, Artifact Registry applies the keep policy.

### Use delete policies

Delete policies delete artifacts matching the following required criteria:

  * **Tag state** : indicates if the policy should check for tagged artifacts or untagged artifacts. Artifacts are tagged when pushing or pulling an image to or from a repository. For more on Docker tags, see [Container concepts](https://docs.cloud.google.com/artifact-registry/docs/container-concepts#tags).

    * **Any tag state** : ignores tag state and applies to both tagged and untagged artifacts.
    * **Tagged** : only applies to tagged artifacts.
    * **Untagged** : only applies to untagged artifacts.

Formats that don't support tags are treated as `untagged`. Tagged artifacts in repositories with immutable tags enabled cannot be deleted.

For more information on tag state as it applies to cleanup policies, see the [TagState reference](https://docs.cloud.google.com/artifact-registry/docs/reference/rest/v1/projects.locations.repositories#tagstate).




You can use any of the following settings to configure your delete policy:

  * **Tag prefixes** : is a comma-separated list of tag prefixes. For example, the prefixes `test`, and `staging` would match images with tags `testenv` and `staging-1.5`. `tagState` must be set to `TAGGED` to use tag prefixes. 
    * **Version prefixes** : - is a comma-separated list of artifact version prefixes. For example `v1`, `v2` would match versions `v1.5`, `v2.0alpha`, and `v10.2`.
  * **Package prefixes** : is a list of artifact name prefixes. You can enter multiple prefixes by pressing `Enter` or `,` between the prefixes. For example `red, blue` would create two prefixes, `red` and `blue` and would match artifact names `red-team`, `redis`, and `bluebird`.
  * **Older than** : is a minimum time since an artifact version was uploaded to the repository, specified as a duration. For example, `30d` is 30 days. You can specify durations of seconds, minutes, hours, or days by appending `s`, `m`, `h`, or `d` respectively.
  * **Newer than** : is a maximum time since an artifact version was uploaded to the repository, specified as a duration. For example, `30d` is 30 days.



### Use keep policies

Keep policies keep artifacts matching the same conditions as delete policies, or a set number of most recent versions.

**Caution:** if you define **Package prefixes** in a **Keep most recent versions** keep policy, only packages matching the package prefixes you define are kept.

For example, given a repository containing the following artifacts:
    
    
    IMAGE: us-west1-docker.pkg.dev/my-project/release-xyz-v1
    DIGEST: sha256:1b0a26bd07a3d17473d8d8468bea84015e27f87124b2831234581bce13f61370
    TAGS:
    CREATE_TIME: 2023-06-19T18:59:09
    UPDATE_TIME: 2023-06-19T18:59:10
    
    IMAGE: us-west1-docker.pkg.dev/my-project/release-xyz-v2
    DIGEST: sha256:6e494387c901caf429c1bf77bd92fb82b33a68c0e19f123456a3ac8d27a7049d
    TAGS: latest
    CREATE_TIME: 2023-06-19T18:59:09
    UPDATE_TIME: 2023-06-19T18:59:09
    
    IMAGE: us-west1-docker.pkg.dev/my-project/release-v2
    DIGEST: sha256:6e494387c901caf429c1bf77bd92fb82b33a68c0e19f123456a3ac8d27a7049d
    TAGS: latest
    CREATE_TIME: 2023-06-19T18:59:09
    UPDATE_TIME: 2023-06-19T18:59:09
    

If your **Keep most recent versions** policy is set to keep 3 versions of packages matching the **Package prefixes** : `{release-xyz}`, only `release-xyz-v1`, and `release-xyz-v2` are kept.

Deletions triggered by delete policies count against your Artifact Registry [per project delete request quota](https://docs.cloud.google.com/artifact-registry/quotas#project-quota).

To create and apply cleanup policies to your repository, see [Configure cleanup policies](https://docs.cloud.google.com/artifact-registry/docs/repositories/cleanup-policy).

## gcr.io domain support

Artifact Registry supports hosting of images on the `gcr.io` domain. If you are transitioning from Container Registry to Artifact Registry, you can set up gcr.io repositories Artifact Registry to minimize changes to your existing automation and workflows. These repositories provide:

  * Redirection of requests to the `gcr.io` domain.
  * Creation of gcr.io repositories when the first image is pushed to a gcr.io hostname for compatibility with Container Registry behavior.



For more information, see [Transition to repositories with gcr.io domain support](https://docs.cloud.google.com/artifact-registry/docs/transition/setup-gcr-repo)

## Project structure

Your [resource hierarchy](https://docs.cloud.google.com/architecture/landing-zones/decide-resource-hierarchy) is the way that you organize your resources across Google Cloud projects. The structure that you choose depends on factors such as data governance requirements, trust boundaries, and team structure. 

There are two general approaches for setting up your repositories in multi-project organizations.

Centralize repositories
    

Create all repositories in a single project and then grant access to principals from other projects at the repository level. This approach can be more effective when a single person or team handles repository administration and repository access across your organization.

    

It can also simplify setup of virtual repositories since you only need to enable and manage a single instance of Artifact Registry.

Project-specific repositories
    

Create repositories in projects that store and download artifacts. This approach might be required when you have data governance policies or trust boundaries that require more project-level separation and control of resources.

## Access control

Repositories are only accessible with appropriate permissions unless you configure the repository for [public access](https://docs.cloud.google.com/artifact-registry/docs/access-control#public). You can grant permissions at the project or repository level.

Some Google Cloud services use default service accounts with default permissions to repositories in the same Google Cloud project. However, these default might not be suitable for your software development process or might not comply with security or policy requirements in your organization. Your repository administrator must explicitly grant these services access to repositories if:

  * Artifact Registry is in a different project than the service that is interacting with it.
  * You are using custom IAM roles with the default service accounts instead of the predefined role.
  * You are not using the default service account for the Google Cloud service. 
  * You are setting up virtual repositories. You must explicitly grant the Artifact Registry service account access to upstream repositories. 



For other principals that require access to repositories, your repository administrator must grant access. Following the security principle of least privilege, grant the minimum required permissions. For example:

  * You deploy container images in Artifact Registry to GKE clusters in several different projects. The service account for nodes in these clusters only require read access to repositories.
  * You have a development repository for applications that are in development and production repository for applications that are released. Developers require read and write access to the development repository and read-only access to the production repository.
  * You have a demo repository with sample applications. Your sales team only requires read-only access to download the demos.



## Restrict artifact downloads

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can [restrict artifact downloads with download rules](https://docs.cloud.google.com/artifact-registry/docs/restrict-artifact-downloads). Download rules let you allow or deny artifact downloads from your repositories and packages. You can also set conditions so the rule applies to specific tags or versions.

For details on how downloads rules work, see the [Restrict artifact downloads](https://docs.cloud.google.com/artifact-registry/docs/protect-artifacts#restrict_artifact_downloads) section of the Control access and protect artifacts overview.

## Data encryption

By default, Google Cloud automatically [encrypts data when it is at rest](https://docs.cloud.google.com/docs/security/encryption/default-encryption) using Google-owned and Google-managed encryption keys. If you have specific compliance or regulatory requirements related to the keys that protect your data, you can create repositories encrypted with [customer-managed encryption keys](https://docs.cloud.google.com/artifact-registry/docs/cmek) (CMEK). 

Artifact Registry also supports [organization policy constraints](https://docs.cloud.google.com/artifact-registry/docs/cmek#org-policy) that can require CMEK to protect resources.

## Labels and tags

Labels provide a way to organize resources specific to a Google Cloud service. In Artifact Registry, you can add labels to repositories so that you can group them together or filter repository lists by label. For example, you can use labels to group repositories by development stage or by team for automation or billing purposes. For more information about creating and using repository labels, see [Labelling repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/label-repos).

You can also apply _tags_ to repositories. While labels are primarily for organizing and filtering service-specific resources, tags are for programmatic control of policies across a Google Cloud organization. For more information, see [Tagging repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/tag-repos).

## What's Next

  * [Create standard repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos)
  * Learn more about [remote repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-overview)
  * Learn more about [virtual repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/virtual-overview)
  * [Create remote repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-repo)
  * [Create virtual repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/virtual-repo)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
