---
url: https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-overview/
title: Remote repositories overview \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:52.402826+00:00
---

# Remote repositories overview  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Remote repositories overview Stay organized with collections  Save and categorize content based on your preferences. 

Remote repositories act as proxies for upstream sources, such as Docker Hub and Maven Central, and provide more control over your dependencies in Google Cloud. This document describes how remote repositories work and provides several use cases.

For instructions on how to create a remote repository, see [Create remote repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-repo).

**Note:** Artifact Registry [Quotas and limits](https://docs.cloud.google.com/artifact-registry/quotas) apply to remote repositories.

## How remote repositories work

Remote repositories store artifacts from standard Artifact Registry repositories and external sources. The first time that you request a version of a package, Artifact Registry downloads and caches the package in the remote repository. The next time you request the same package version, Artifact Registry serves the cached copy.

If you request an artifact from an upstream source that doesn't exist, or doesn't contain the version you specified, the request will fail.

## Upstream authentication

Artifact Registry remote repositories support [basic authentication](https://datatracker.ietf.org/doc/html/rfc7617) to upstream sources for supported formats. For more information on how to authenticate to remote repository upstream sources, see [Configure authentication to remote repository upstreams](https://docs.cloud.google.com/artifact-registry/docs/repositories/configure-remote-authentication).

## Use cases and benefits

Faster, more reliable access to artifacts
    Storing cached copies of your public dependencies in Artifact Registry reduces latency when other Google Cloud services retrieve images. Cached artifacts are also still available if the external public repository is offline due to an outage or other issue.
Safer dependency resolution
    

Use remote repositories together with virtual repositories to mitigate risks associated with public dependencies. Some tools do not provide a way to control search order when a mix of private and public repositories are configured in the client. This type of configuration is vulnerable to a _dependency confusion_ attack, where someone uploads a new version of a package with bad code to a public repository to trick clients into choosing the bad version.

Instead of configuring clients directly to search multiple repositories, you can configure virtual repositories to prioritize your private repositories over remote repositories.

Reduce data transfer cost
    

Use remote repositories to cache artifacts in the same region or multi-region as your runtimes to reduce [data transfer costs](https://docs.cloud.google.com/artifact-registry/pricing#data-transfer).

If Artifact Registry is in a [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) service perimeter, Artifact Registry denies access to upstream sources outside the perimeter by default. To allow remote repositories in a specific location to access their configured external sources outside the perimeter, see the instructions for [VPC Service Controls configuration](https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-repo#vpc).

To learn about other dependency management best practices, see [Dependency management](https://docs.cloud.google.com/software-supply-chain-security/docs/dependencies).

### Updates to package indexes and metadata

Mutable files such as package indexes and metadata are updated from the upstream source when they become more than the default age. Defaults for specific file types are listed in the following table:

Format | File type | Default update age  
---|---|---  
Maven | `maven-metadata.xml` | 5 minutes  
`archetype-catalog.xml` | 1 hour  
Npm | Manifest files | 5 minutes  
Python | Index files | 1 hour  
Docker | List/Get tags cache | 1 hour  
Apt/Yum (preview) | Index files | 2 minutes  
Package files | 72 hours  
  
## Supported formats

See the following sections for the formats available for preset and user-defined remote repositories.

### Preset upstream URLs

A number of common upstream repository URLs are available as preset selections for convenience in the following formats.

Format | package types | Upstream URL | Upstream preset name  
---|---|---|---  
Docker | Public or private | `https://registry-1.docker.io` | `DOCKER-HUB`  
Go | Public | `https://proxy.golang.org` | `https://proxy.golang.org`  
Maven | Public or private | `https://repo.maven.apache.org/maven2` | `MAVEN-CENTRAL`  
npm | Public or private | `https://registry.npmjs.org` | `NPMJS`  
Python | Public | `https://pypi.io` | `PYPI`  
OS packages ([preview](https://cloud.google.com/products#product-launch-stages)) | Public | See OS packages supported upstreams | See OS packages supported upstreams  
  
### OS packages preset upstreams

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can create an OS package remote repository by choosing from one of the common preset upstream repository base URLs and customizing the remainder of the URL to the specific repository. The following repository bases are supported:

**Apt**

**Repository** | **URL Prefix** | **Repository Base Name**  
---|---|---  
Archived Debian | `https://snapshot.debian.org` | `DEBIAN_SNAPSHOT`  
Debian | `http://deb.debian.org` | `DEBIAN`  
Ubuntu LTS or Pro  | `http://archive.ubuntu.com` | `UBUNTU`  
  
**Yum**

**Repository** | **URL Prefix** | **Repository Base Name**  
---|---|---  
CentOS  | `http://mirror.centos.org` | `CENTOS`  
| `http://debuginfo.centos.org` | `CENTOS_DEBUG`  
| `https://vault.centos.org` | `CENTOS_VAULT`  
| `https://mirror.stream.centos.org` | `CENTOS_STREAM`  
Rocky  | `http://dl.rockylinux.org` | `ROCKY`  
Fedora Extra Packages for Enterprise Linux (EPEL) | `https://dl.fedoraproject.org/pub/epel` | `EPEL`  
  
### Artifact Registry repository upstreams

You can create remote repositories with Artifact Registry standard format repositories as upstreams for the following formats:

  * Docker
  * npm
  * Maven
  * Python



### Custom URLs

You can enter the URL for your remote repository directly, without using one of the preset upstream sources for the following formats. Custom remote repository upstream URIs must use HTTPS. Unencrypted HTTP upstream URIs are not supported.

  * Docker
  * npm
  * Maven
  * Python



The following non-exhaustive table lists some common upstream URIs.

**Format** | **Upstream URI** | **Registry Name**  
---|---|---  
Docker | `https://ghcr.io` | GitHub Container Registry  
Docker | `https://registry-1.docker.io` | Docker Hub  
Docker | `https://public.ecr.aws` | AWS ECR Public Gallery  
Docker | `https://registry.k8s.io` | Kubernetes Container Registry  
Docker | `https://MY_NEXUS_IP` | Nexus  
npm | `https://registry.npmjs.org` | npm  
npm | `https://npm.pkg.github.com` | GitHub Npm Registry  
npm | `https://MY_NEXUS_IP/repository/MY_UPSTREAM_REPOSITORY` | Nexus  
Maven | `https://repo.maven.apache.org/maven2` | Maven Central  
Maven | `https://MY_NEXUS_IP/repository/MY_UPSTREAM_REPOSITORY` | Nexus  
Python | `https://pypi.io` | Python Package Index (PyPI)  
Python | `https://MY_NEXUS_IP/repository/MY_UPSTREAM_REPOSITORY` | Nexus  
  
Where

  * MY_NEXUS_IP is the IP address and port of your Nexus upstream instance. The upstream endpoint must use HTTPS.
  * MY_UPSTREAM_REPOSITORY is the name of your upstream repository; used in the Nexus examples.



## Limitations

In addition to Artifact Registry quotas and limitations, remote repositories have the following limitations:

  * Maven remote repositories don't permit setting the version policy to snapshot or release.
  * Upstream sources must be internet accessible. Remote repositories don't support on-premise or Virtual Private Cloud (VPC) network upstream sources without a public IP address.
  * Custom remote repository upstream URIs must use HTTPS. Unencrypted HTTP upstream URIs are not supported.



## Other repository modes

The other repository modes are the following:

  * [Standard](https://docs.cloud.google.com/artifact-registry/docs/repositories): the default repository mode. You upload or publish artifacts such as private packages directly to standard repositories. Although you can download directly from individual standard repositories, accessing groups of repositories with a virtual repository simplifies tool configuration.
  * [Connector](https://docs.cloud.google.com/artifact-registry/docs/repositories/connector-overview) (Preview): a repository that acts as a proxy for an upstream source but doesn't cache artifacts in Artifact Registry. Instead, all requests are made to the upstream source. Connector repositories are useful if you require full auditability of your upstream source or have policies preventing artifact caching.
  * [Virtual](https://docs.cloud.google.com/artifact-registry/docs/repositories/virtual-overview): a repository that acts as a single access point for multiple upstream repositories, including remote and standard repositories.



## What's next

  * [Create remote repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-repo).
  * Learn more about Artifact Registry repositories by reading the [Repository overview](https://docs.cloud.google.com/artifact-registry/docs/repositories).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
