---
url: https://docs.cloud.google.com/artifact-registry/docs/repositories/virtual-overview/
title: Virtual repositories overview \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:20:12.674948+00:00
---

# Virtual repositories overview  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/repositories/virtual-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Virtual repositories overview Stay organized with collections  Save and categorize content based on your preferences. 

This document provides an overview of virtual repositories. For instructions on how to create a virtual repository, see [Create virtual repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/virtual-repo).

Artifact Registry [Quotas and limits](https://docs.cloud.google.com/artifact-registry/quotas) apply to virtual repositories.

## How virtual repositories work

Virtual repositories act as a single access point to download, install, or deploy artifacts in the same format from one or more _upstream repositories_. An upstream repository can be a Artifact Registry standard or remote repository.

## Use cases and benefits

Simpler client configuration
    

For task that only requires read access to repositories, you only need to configure a single Artifact Registry repository to access artifacts stored in multiple upstream repositories.

For example:

  * A virtual repository for Maven packages can serve private Java packages from a Artifact Registry standard repository and public Java packages from a remote repository that caches public packages from Maven Central.
  * A virtual repository can serve private Python packages from multiple upstream standard repositories owned by different teams. Each team has write access to their upstream repository, but downloads packages from other teams using the virtual repository.


Safer dependency resolution
    

You can assign a priority to upstream repositories to have more control over which repository Artifact Registry chooses when a requested artifact is in more than one upstream repository.

Some tools, such as the Python `pip` tool, do not provide a way to control search order when a mix of private and public repositories are configured in the client. This type of configuration is vulnerable to a _dependency confusion_ attack, where someone uploads a new version of a package with bad code to a public repository to trick clients into choosing the bad version.

You can use remote and virtual repositories together to mitigate this risk:

  1. Create a remote repository as a proxy for the public repository.
  2. Create a standard repository for your private packages.
  3. Create a virtual repository that is configured to prioritize your standard repository if a version of the same package exists in both repositories.
  4. Configure package managers and other tools to read from the virtual repository only, so that the client logic is not involved repository selection.



To learn about other dependency management best practices, see [Dependency management](https://docs.cloud.google.com/software-supply-chain-security/docs/dependencies).

## How virtual repositories select an upstream repository

Each upstream repository must have a configured _priority_. The priority is an integer that acts as a weight, not a ranking. This means that repositories with a higher numeric priority value are prioritized over repositories with lower priority values.

When you request an artifact that is in multiple upstream repositories, Artifact Registry uses the following prioritization logic:

  * The repository with the highest value is prioritized. For example, a value of `10` is treated as higher priority than a value of `1`.
  * If multiple upstream repositories have the same priority, the artifact can be served from any of those repositories.



We also recommend including the artifact version in your request. This way, the client returns the highest priority upstream repository that contains the requested artifact version. If you don't specify the artifact version, the client might return the latest version of the artifact, regardless of repository priority.

When you directly configure a client to search a virtual repository and additional repositories, the client might still download artifacts from repositories outside of Artifact Registry.For example, if you configure the Python `pip` tool to search PyPI and a virtual repository, your package might be downloaded directly from PyPI because `pip` will always choose the latest version of a package, regardless of which repository it comes from. If `pip` is configured to only search the virtual repository, you can then control the priority of all upstream repositories, including an upstream remote repository that acts as a proxy for PyPI.

## Supported repository formats

You can create virtual repositories for following Artifact Registry Artifact Registry repository formats:

Language packages:

  * [Docker](https://docs.cloud.google.com/artifact-registry/docs/docker)
  * [Go](https://docs.cloud.google.com/artifact-registry/docs/go)
  * [Maven](https://docs.cloud.google.com/artifact-registry/docs/java)
  * [npm](https://docs.cloud.google.com/artifact-registry/docs/nodejs)
  * [Python](https://docs.cloud.google.com/artifact-registry/docs/python)



OS packages:

**Private Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

  * [Apt](https://docs.cloud.google.com/artifact-registry/docs/os-packages/debian)
  * [Yum](https://docs.cloud.google.com/artifact-registry/docs/os-packages/rpm)



If you are new to Artifact Registry, you can use the quickstarts to learn about setting up standard repositories for these formats.

## Limitations

In addition to Artifact Registry quotas and limitations, virtual repositories have the following limitations:

  * Because virtual repositories don't store data, they will appear empty when running `gcloud artifacts docker images list` and when viewing the repository in the Google Cloud console.
  * Standard Artifact Registry upstream repositories must be in the same region or multi-region as the virtual repository, but can be in different Google Cloud projects.
  * Maven virtual repositories don't permit setting the version policy to snapshot or release.

  * Apt and Yum upstreams must be Artifact Registry standard repositories.

  * Apt and Yum standard repositories update the package index asynchronously after a package is imported, uploaded, or deleted. For small repositories, regenerating the index can take several seconds. For larger repositories, reindexing might take several minutes or longer. After reindexing is complete, the change to the repository is visible to Apt and Yum clients.




## Other repository modes

The other repository modes are the following:

  * [Standard](https://docs.cloud.google.com/artifact-registry/docs/repositories): the default repository mode. You upload or publish artifacts such as private packages directly to standard repositories. Although you can download directly from individual standard repositories, accessing groups of repositories with a virtual repository simplifies tool configuration.
  * [Remote](https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-overview): a repository that acts as a proxy for an upstream source by caching packages in Artifact Registry after they're downloaded from the upstream source for the first time. When you next request the same package version, Artifact Registry provides the cached copy.
  * [Connector](https://docs.cloud.google.com/artifact-registry/docs/repositories/connector-overview) (Preview): a repository that acts as a proxy for an upstream source but doesn't cache artifacts in Artifact Registry. Instead, all requests are made to the upstream source. Connector repositories are useful if you require full auditability of your upstream source or have policies preventing artifact caching.



## What's next

  * [Create virtual repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/virtual-repo).
  * Learn more about Artifact Registry repositories by reading the [Repository overview](https://docs.cloud.google.com/artifact-registry/docs/repositories).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
