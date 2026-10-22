---
url: https://docs.cloud.google.com/artifact-registry/docs/repositories/connector-overview/
title: Connector repositories overview \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:20.447763+00:00
---

# Connector repositories overview  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/repositories/connector-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Connector repositories overview Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Artifact Registry connector repositories act as proxies for upstream sources. All requests to the repository are proxied to the upstream source and no artifacts are cached in Artifact Registry. This configuration allows for full auditability of upstream sources and supports cases where third-party policies prevent artifact caching.

This document describes how connector repositories work and provides several use cases. For instructions on how to create a connector repository, see [Create connector repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/connector-repo).

**Note:** Artifact Registry [Quotas and limits](https://docs.cloud.google.com/artifact-registry/quotas) apply to connector repositories.

## Supported connector formats

Artifact Registry supports only Docker-format connector repositories.

## Upstream authentication

Artifact Registry connector repositories require [basic authentication](https://datatracker.ietf.org/doc/html/rfc7617) to upstream sources. For more information about how to authenticate to connector repository upstream sources, see [Configure authentication to connector repository upstreams](https://docs.cloud.google.com/artifact-registry/docs/repositories/configure-connector-authentication).

If you request an artifact from an upstream source that doesn't exist, or doesn't contain the version you specified, the request will fail.

## Use cases and benefits

Full upstream auditability
    Connector repositories don't cache any packages in Artifact Registry, so all repository requests are made directly to your upstream source. This process is helpful if your repository configuration requires full auditability of upstream sources or if you must comply with third-party policies that prevent artifact caching.
Safer dependency resolution
    

Use connector repositories together with virtual repositories to mitigate risks associated with public dependencies. Some tools don't provide a way to control search order when a mix of private and public repositories are configured in the client. This type of configuration is vulnerable to a _dependency confusion_ attack, where an attacker uploads a new version of a package with bad code to a public repository to trick clients into choosing the malicious version.

Instead of configuring clients directly to search multiple repositories, you can configure virtual repositories to prioritize your private repositories over connector repositories.

If Artifact Registry is in a [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) service perimeter, Artifact Registry denies access to upstream sources outside the perimeter by default. You can allow connector repositories in a specific location to access their configured external sources outside the perimeter. For instructions, see [VPC Service Controls configuration](https://docs.cloud.google.com/artifact-registry/docs/repositories/connector-repo#vpc).

To learn about other dependency management best practices, see [Dependency management](https://docs.cloud.google.com/software-supply-chain-security/docs/dependencies).

### Updates to package indexes and metadata

Mutable files such as package indexes and metadata are updated from the upstream source when they become more than the default age. Defaults for specific file types are listed in the following table:

Format | File type | Default update age  
---|---|---  
Docker | List/Get tags cache | 1 hour  
  
## Artifact Registry connector repository upstreams

You can use Docker Hub as your connector repository source or enter a custom repository URL. The following table shows a partial list of some common upstream Docker URIs:

**Format** | **Upstream URI** | **Registry Name**  
---|---|---  
Docker | `https://MY_ARTIFACTORY_INSTANCE.jfrog.io/OPTIONAL_REPO` | JFrog Artifactory  
Docker | `https://ghcr.io` | GitHub Container Registry  
Docker | `https://registry-1.docker.io` | Docker Hub  
Docker | `https://public.ecr.aws` | AWS ECR Public Gallery  
Docker | `https://registry.k8s.io` | Kubernetes Container Registry  
Docker | `https://MY_NEXUS_IP` | Nexus  
  
## Limitations

In addition to Artifact Registry quotas and limitations, connector repositories have the following limitations:

  * Upstream sources must be internet accessible. Connector repositories don't support on-premise or Virtual Private Cloud (VPC) network upstream sources without a public IP address.



## Other repository modes

The other repository modes are the following:

  * [Standard](https://docs.cloud.google.com/artifact-registry/docs/repositories): the default repository mode. You upload or publish artifacts such as private packages directly to standard repositories. Although you can download directly from individual standard repositories, accessing groups of repositories with a virtual repository simplifies tool configuration.
  * [Remote](https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-overview): a repository that acts as a proxy for an upstream source by caching packages in Artifact Registry after they're downloaded from the upstream source for the first time. When you next request the same package version, Artifact Registry provides the cached copy.
  * [Virtual](https://docs.cloud.google.com/artifact-registry/docs/repositories/virtual-overview): a repository that acts as a single access point for multiple upstream repositories, including connector and standard repositories.



## What's next

  * [Create connector repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/connector-repo).
  * Learn more about Artifact Registry repositories by reading the [Repository overview](https://docs.cloud.google.com/artifact-registry/docs/repositories).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
