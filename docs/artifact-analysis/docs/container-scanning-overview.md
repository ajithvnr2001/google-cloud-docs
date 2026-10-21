---
url: https://docs.cloud.google.com/artifact-analysis/docs/container-scanning-overview/
title: Container scanning overview \u00a0|\u00a0 Artifact Analysis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:44:40.671168+00:00
---

# Container scanning overview  |  Artifact Analysis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-analysis/docs/container-scanning-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Analysis ](https://docs.cloud.google.com/artifact-analysis/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-analysis/docs/ods-quickstart)



Send feedback 

#  Container scanning overview Stay organized with collections  Save and categorize content based on your preferences. 

Container scanning identifies new and existing vulnerabilities and malicious packages in the open-source dependencies for container images in your Artifact Registry repositories. Artifact Analysis provides two ways to scan your packages: _automatic scanning_ and _on-demand scanning_. This document describes both types of scanning.

Artifact Analysis also provides metadata management. To learn more about how you can use scanning and metadata storage together to secure your CI/CD pipeline from end to end, see the [Artifact Analysis overview](https://docs.cloud.google.com/artifact-analysis/docs/artifact-analysis).

See [pricing](https://cloud.google.com/artifact-analysis/pricing) to learn more about the costs associated with scanning container images.

This overview assumes you are already familiar with using Docker repositories in [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/overview).

## Scan images for vulnerabilities

Artifact Analysis performs vulnerability and malicious package scans on your artifacts in Artifact Registry. Artifact Analysis also identifies dependencies and licenses to help you understand your software composition.

Automatic scanning comprises two main tasks: automatic scanning and continuous analysis.

### Automatic scanning

Artifact Analysis scans new images when they're uploaded to Artifact Registry. This scan extracts information about the packages in the container. The images are scanned only once, based on the image's digest. This means that adding or modifying tags won't trigger new scans.

Artifact Analysis only detects vulnerabilities and malicious software in packages that are publicly monitored. Vulnerability data is sourced from various upstream providers, and malicious package data is sourced from the [OpenSSF Malicious Packages Repository](https://github.com/ossf/malicious-packages). Malicious packages are reported as **CRITICAL** severity vulnerabilities.

When the scan of an image is completed, the produced **vulnerability result** is the collection of vulnerability occurrences for that image.

Automatic vulnerability scans also detect secrets, such as API keys and service account keys, so that you can prevent sensitive data from exposure. This feature is in [public preview](https://cloud.google.com/products/#product-launch-stages). For more information, see [Scan for secrets](https://docs.cloud.google.com/artifact-analysis/docs/secret-scanning).

**Important:** When you enable the Artifact Analysis API, Artifact Analysis automatically begins scanning each new image as they are pushed to Artifact Registry repositories in your project. However, scanning is disabled by default for packages pushed to Artifact Registry repositories. To enable scanning in a repository, see [Control scanning settings for an individual repository](https://docs.cloud.google.com/artifact-analysis/docs/enable-automatic-scanning#disable-repo).

### Continuous analysis

Artifact Analysis creates occurrences for vulnerabilities and malicious packages found when you upload the image. After the initial scan, it continuously monitors the metadata for scanned images in Artifact Registry for new vulnerabilities and malicious packages.

Artifact Analysis receives new and updated vulnerability and malicious package information from [vulnerability sources](https://docs.cloud.google.com/artifact-analysis/docs/container-scanning-overview#sources) multiple times each day. When new vulnerability or malicious package data arrives, Artifact Analysis updates the metadata of the scanned images to keep it up-to-date. Artifact Analysis updates existing occurrences, creates new occurrences for new notes, and deletes occurrences that are no longer valid.

Artifact Analysis continues to scan images and packages as long as they have been pulled within the last 30 days. After 30 days, metadata for scanned images and packages will no longer be updated, and the results will be stale.

Artifact Analysis archives metadata that has been stale for more than 90 days. This archived metadata can be evaluated only by using the API. You can re-scan an image with stale or archived metadata by pulling that image. Refreshing metadata can take up to 24 hours. Packages with stale or archived metadata can't be rescanned.

### Architectures

Artifact Analysis can scan images on any Linux-based architecture.

You can also use vulnerability scanning with manifest lists. A [manifest list](https://docs.docker.com/registry/spec/manifest-v2-2/#manifest-list) is a list of pointers to manifests for several platforms. They allow a single image to work with multiple architectures or variations of an operating system.

If your manifest list contains a Linux amd64 image, Artifact Analysis will scan that image. Otherwise, Artifact Analysis selects a different image from the list.

## On-demand scanning

On-demand scanning lets you scan container images locally on your computer or in your registry, using the gcloud CLI. This gives you the flexibility to customize your CI/CD pipeline, depending on when you need to access the vulnerability results.

## Supported package types

When you push container images to Docker repositories in Artifact Registry, Artifact Analysis can scan for vulnerabilities in several types of OS packages and application language packages.

The following tables compare the types of packages that Artifact Analysis can scan with each scanning service:

### Supported OS packages

| Automatic scanning with Artifact Registry | On-demand scanning  
---|---|---  
AlmaLinux OS |  |   
Alpine |  |   
CentOS |  |   
Chainguard |  |   
Debian |  |   
Google Distroless |  |  | MinimOS |  |   
Red Hat Enterprise Linux (RHEL) |  |   
Red Hat Universal Base Image (UBI) |  |   
Rocky Linux |  |   
SUSE Linux Enterprise Server (SLES) |  |   
Ubuntu |  |   
Wolfi |  |   
  
### Supported application language packages

| Automatic scanning with Artifact Registry | On-demand scanning  
---|---|---  
Go packages |  |   
Java packages |  |   
Node.js packages |  |   
PHP packages |  |   
Python packages |  |   
Ruby packages |  |   
Rust packages |  |   
.NET packages |  |   
  
For more information on the features available for each registry product, view the [comparison chart](https://docs.cloud.google.com/artifact-registry/docs/transition/setup-repo#analysis).

Artifact Analysis is not supported on Windows Server containers.

## Artifact Analysis interfaces

In the Google Cloud console, you can view image vulnerabilities and image metadata for containers in [Artifact Registry](https://console.cloud.google.com/artifacts).

You can use the gcloud CLI to [view vulnerabilities and image metadata](https://docs.cloud.google.com/artifact-analysis/docs/scan-os-automatically#view-gcloud).

You can also use the [Artifact Analysis REST API](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest) to perform any of these actions. As with other Cloud Platform APIs, you must authenticate access using [OAuth2](https://cloud.google.com/docs/authentication). After you have authenticated, you can use also the API to create custom notes and occurrences and view vulnerability occurrences.

The Artifact Analysis API supports both gRPC and REST/JSON. You can make calls to the API either using the [client libraries](https://docs.cloud.google.com/artifact-analysis/docs/reference/libraries) or using cURL for REST/JSON.

### Finding package file paths

When Artifact Analysis finds a vulnerability, you might not recognize the vulnerable package as a dependency in your artifact. This can happen if the package manager introduces it, or if the package is a transitive dependency — a dependency of one of your dependencies.

To find the path to the file that caused a vulnerability finding, follow these steps:

  1. In the Google Cloud console, go to the list of vulnerabilities for an artifact in [Go to Artifact Registry](https://console.cloud.google.com/artifacts).
  2. For the vulnerability you want to investigate, click **VIEW FIX**.
  3. In the details pane, click **SHOW MORE INFO**.

The **File location** field shows the path to the vulnerable package




## Control deployment of vulnerable images

You can integrate Artifact Analysis with Binary Authorization to [create attestations](https://docs.cloud.google.com/binary-authorization/docs/making-attestations), which can prevent container images with known security issues from running in your deployment environment.

You can use also use Binary Authorization to create a vulnerability allowlist based on the [vulnerability information](https://docs.cloud.google.com/binary-authorization/docs/cv-vulnerability-check) provided by Artifact Analysis as part of your deployment. If the vulnerabilities violate the policy in the allowlist, you will be alerted.

Finally, you can use On Demand Scanning to [block and fail builds](https://docs.cloud.google.com/artifact-analysis/docs/ods-cloudbuild) based on the severity of the vulnerabilities found.

## Vulnerability sources

The following section lists the vulnerability sources that Artifact Analysis uses to obtain [CVE](https://cve.mitre.org/) data.

### OS package scans

Artifact Analysis uses the following sources:

  * [AlmaLinux OS](https://errata.almalinux.org/)
  * [Alpine](https://secdb.alpinelinux.org/)
  * [CentOS](https://www.redhat.com/security/data/metrics/) \- Red Hat and CentOS share the same source of vulnerability data. Because CentOS packages are published after Red Hat packages, a fix available for a vulnerability in Red Hat may take some time to also be available for CentOS.
  * [Chainguard](https://images.chainguard.dev/security)
  * [Debian](https://security-tracker.debian.org/tracker)
  * Google Distroless is based on Debian and uses the [Debian](https://security-tracker.debian.org/tracker) vulnerability data.
  * [National Vulnerability Database](https://nvd.nist.gov/)
  * [Minimus](https://docs.minimus.io/remediate/advisories)
  * [Red Hat Enterprise Linux (RHEL)](https://www.redhat.com/security/data/metrics/)
  * [Red Hat Universal Base Image (UBI)](https://www.redhat.com/security/data/metrics/)
  * [Rocky Linux](https://errata.rockylinux.org/)
  * [SUSE Linux Enterprise Server (SLES)](https://www.suse.com/support/update/)
  * [Ubuntu](https://security-metadata.canonical.com/oval/)
  * [Wolfi](https://images.chainguard.dev/security)



### Language package scans

Artifact Analysis supports vulnerability and malicious package scanning for language packages within a container image.

  * Vulnerability data is obtained from the [GitHub Advisory Database](https://github.com/advisories).
  * Malicious package data is obtained from the [OpenSSF Malicious Packages Repository](https://github.com/ossf/malicious-packages). Malicious packages are reported as **CRITICAL** severity findings. Artifact Analysis detects malicious packages that fall into the following categories:

    * **Typosquatting or dependency confusion** : Packages published with names similar to popular packages to trick users into installing them.
    * **Account takeover** : Legitimate packages that have been compromised by malicious actors.
    * **Malicious binaries** : Prebuilt binaries for a package that contain malicious code.
    * **Security researcher activity** : Packages created by researchers to demonstrate vulnerabilities or track package usage.



In most cases, each vulnerability is assigned a [CVE ID](https://www.cve.org/About/Process#CVERecordLifecycle) and this ID becomes the main identifier for that vulnerability. In cases where there is no CVE ID assigned to a vulnerability, a [GHSA ID](https://docs.github.com/en/code-security/security-advisories/working-with-global-security-advisories-from-the-github-advisory-database/about-the-github-advisory-database#about-ghsa-ids) is assigned as identifier instead. If later on that vulnerability gets a CVE ID, then the vulnerability ID is updated to match the CVE. Malicious package advisories have IDs with a `MAL-` prefix. See [Check for a specific vulnerability in a project](https://docs.cloud.google.com/artifact-analysis/docs/investigate-vulnerabilities#cve) for more information.

## Supported OS versions

Artifact Analysis supports vulnerability scanning for the following versions of operating system software:

  * AlmaLinux OS - Versions: 8, 9, 10, and minor versions
  * Alpine Linux - Versions: 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 3.10, 3.11, 3.12, 3.13, 3.14, 3.15, 3.16, 3.17, 3.18, 3.19, 3.20, 3.21, 3.22, 3.23
  * CentOS - Versions: 6, 7, 8, and minor versions
  * Chainguard - Rolling updates on a [single release track](https://github.com/chainguard-dev/vulnerability-scanner-support/blob/main/docs/foundational_concepts.md).
  * Debian GNU/Linux - Versions: 11, 12, 13, 14, 15
  * MinimOS - Rolling updates on a [single release track](https://docs.minimus.io/foundations/daily-updates).
  * Red Hat Enterprise Linux (RHEL) - Versions: 7, 8, 9, and minor versions are supported for automatic registry scans.
  * Red Hat Universal Base Image (UBI) - Versions 8, 9, and minor versions
  * Rocky Linux - Versions: 8, 9, 10, and minor versions
  * SUSE Linux Enterprise Server (SLES) - Versions: 12, 15, and minor versions; SLES for SAP is also supported with the same versions
  * Ubuntu - Versions: 14.04, 16.04, 18.04, 20.04, 22.04, 24.04, 24.10, 25.04, 25.10, 26.04
  * Wolfi - Rolling updates on a [single release track](https://github.com/chainguard-dev/vulnerability-scanner-support/blob/main/docs/foundational_concepts.md).



### Limitations

  * The primary function of Artifact Analysis is to scan and detect vulnerabilities in containers and make those vulnerabilities visible to your organization. Artifact Analysis does not claim to identify characteristics of images that could increase or decrease your organization's ability to verify the integrity or trust of an image. To further develop this trust, Google has solutions that you can use individually or in combination. [Learn more about our approach to software supply chain security](https://docs.cloud.google.com/software-supply-chain-security/docs/overview).

  * Artifact Analysis delivers vulnerability scanning results for RHEL based on the latest minor version for each major version released. If you scan an older minor version, then you may get inaccurate results.

  * RHEL Version 9 isn't supported for on-demand scanning.




## Package managers and semantic versioning

  * Go - Artifact Analysis reports vulnerabilities for packages in the [Go standard library](https://pkg.go.dev/std), and external Go packages not included in the standard library. The vulnerabilities are reported with a different label for each type of package.
  * Java - Artifact Analysis supports Maven packages that follow the [Maven naming conventions](https://maven.apache.org/guides/mini/guide-naming-conventions.html). If the package version includes spaces, it won't be scanned.
  * Node.js - Package version matching follows the [semantic versioning](https://docs.npmjs.com/about-semantic-versioning) specification.
  * PHP - Artifact Analysis scans [Composer](https://getcomposer.org/) packages. See [Composer semantic versioning](https://getcomposer.org/doc/articles/versions.md).
  * Python - Python version matching follows [PEP 440](https://peps.python.org/pep-0440/) semantics.
  * Ruby - Artifact Analysis scans [RubyGems](https://rubygems.org/) packages. See [RybyGems semantic versioning](https://guides.rubygems.org/patterns/).
  * Rust - Artifact Analysis scans [Cargo](https://doc.rust-lang.org/cargo/index.html) packages. See [Rust semantic versioning](https://doc.rust-lang.org/cargo/reference/semver.html).
  * .NET - Artifact Analysis scans [NuGet](https://www.nuget.org/) packages. See [NuGet semantic versioning](https://learn.microsoft.com/en-us/nuget/concepts/package-versioning).



## What's next

  * [Set up automatic scanning and view results](https://docs.cloud.google.com/artifact-analysis/docs/scan-os-automatically)
  * [Run on-demand scans](https://docs.cloud.google.com/artifact-analysis/docs/scan-os-on-demand)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
