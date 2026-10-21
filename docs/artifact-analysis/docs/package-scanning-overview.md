---
url: https://docs.cloud.google.com/artifact-analysis/docs/package-scanning-overview/
title: Package scanning overview \u00a0|\u00a0 Artifact Analysis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:44:42.724368+00:00
---

# Package scanning overview  |  Artifact Analysis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-analysis/docs/package-scanning-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Analysis ](https://docs.cloud.google.com/artifact-analysis/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-analysis/docs/ods-quickstart)



Send feedback 

#  Package scanning overview Stay organized with collections  Save and categorize content based on your preferences. 

Package scanning identifies existing and new vulnerabilities, malicious software, and secrets in the open-source dependencies for language-based packages in your Artifact Registry repositories.

See [pricing](https://docs.cloud.google.com/artifact-analysis/pricing) to learn more about the costs associated with scanning packages.

This overview assumes you are already familiar with using Docker repositories in [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/overview).

## Overview

Artifact Analysis scans the files in a package when the package is pushed to Artifact Registry. After the initial scan, Artifact Registry continues to monitor the metadata of scanned packages for new vulnerabilities, malicious packages, and secrets.

To evaluate potential areas of risk, Artifact Registry matches the dependencies in a package configuration file against known vulnerabilities. You can review potential vulnerabilities in your package in Artifact Analysis.

## Scan packages for vulnerabilities

Artifact Analysis scans packages in your Artifact Registry repositories to identify vulnerabilities, malicious software, secrets, and also to identify dependencies and licenses so that you can understand your package composition.

Artifact Analysis scans new packages when they're pushed to Artifact Registry. This process is called _automatic scanning_. The scan extracts information about the files in the package. After scanning a package, Artifact Analysis produces a _vulnerability report_ , which shows the vulnerability and malicious package occurrences for that package. Vulnerabilities and malicious software are detected only in packages that are publicly monitored.

**Important:** When you enable the Artifact Analysis API, Artifact Analysis automatically begins scanning each new image as they are pushed to Artifact Registry repositories in your project. However, scanning is disabled by default for packages pushed to Artifact Registry repositories. To enable scanning in a repository, see [Control scanning settings for an individual repository](https://docs.cloud.google.com/artifact-analysis/docs/enable-automatic-scanning#disable-repo).

## Continuous analysis

After a package has been scanned, Artifact Analysis continuously monitors the scanned package metadata in Artifact Registry for new vulnerabilities and malicious packages.

Artifact Analysis receives new and updated vulnerability information from [vulnerability sources](https://docs.cloud.google.com/artifact-analysis/docs/container-scanning-overview#sources) multiple times each day. When new vulnerability data arrives, Artifact Analysis updates existing vulnerability occurrences, creates new vulnerability occurrences for new notes, and deletes vulnerability occurrences that are no longer valid.

Artifact Analysis continues to scan images and packages as long as they have been pulled within the last 30 days. After 30 days, metadata for scanned images and packages will no longer be updated, and the results will be stale.

Artifact Analysis archives metadata that has been stale for more than 90 days. This archived metadata can be evaluated only by using the API. You can re-scan an image with stale or archived metadata by pulling that image. Refreshing metadata can take up to 24 hours. Packages with stale or archived metadata can't be rescanned.

## Supported package types

When you push packages to Artifact Registry, Artifact Analysis can scan for vulnerabilities.

The following table shows the types of packages that Artifact Analysis can scan:

| Automatic scanning with Artifact Registry | On-demand scanning  
---|---|---  
Java packages |  |   
Python packages |  |   
Node.js packages |  |   
**Note:** By default, scanning is disabled for Java, Python, and Node.js repositories in Artifact Registry. For information about enabling scanning for a repository, see [Control scanning settings for an individual repository](https://docs.cloud.google.com/artifact-analysis/docs/enable-automatic-scanning#disable-repo).

## Artifact Analysis interfaces

In the Google Cloud console, you can view vulnerabilities and metadata for packages in [Artifact Registry](https://console.cloud.google.com/artifacts).

You can use the gcloud CLI to [view vulnerabilities and metadata](https://docs.cloud.google.com/artifact-analysis/docs/scan-os-automatically#view-gcloud).

You can also use the [Artifact Analysis REST API](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest) to perform any of these actions. As with other Cloud Platform APIs, you must authenticate access using [OAuth2](https://cloud.google.com/docs/authentication).

The Artifact Analysis API supports both gRPC and REST/JSON. You can make calls to the API either using the [client libraries](https://docs.cloud.google.com/artifact-analysis/docs/reference/libraries) or using curl for REST/JSON.

## Vulnerability sources

The following section lists the vulnerability sources that Artifact Analysis uses to obtain [CVE](https://cve.mitre.org/) data.

### Language package scans

Artifact Analysis supports vulnerability and malicious package scanning for files within a package. Vulnerability data is obtained from the [GitHub Advisory Database](https://github.com/advisories), and malicious package data is obtained from the [OpenSSF Malicious Packages Repository](https://github.com/ossf/malicious-packages).

In most cases, each vulnerability is assigned a [CVE ID](https://www.cve.org/About/Process#CVERecordLifecycle) and this ID becomes the main identifier for that vulnerability. In cases where there is no CVE ID assigned to a vulnerability, a [GHSA ID](https://docs.github.com/en/code-security/security-advisories/working-with-global-security-advisories-from-the-github-advisory-database/about-the-github-advisory-database#about-ghsa-ids) is assigned as identifier instead. If later on that vulnerability gets a CVE ID, then the vulnerability ID is updated to match the CVE. Malicious package advisories have IDs with a `MAL-` prefix. See [Check for a specific vulnerability in a project](https://docs.cloud.google.com/artifact-analysis/docs/investigate-vulnerabilities#cve) for more information.

## Package managers and semantic versioning

  * Java - Artifact Analysis supports Maven packages that follow the [Maven naming conventions](https://maven.apache.org/guides/mini/guide-naming-conventions.html). If the package version includes spaces, it won't be scanned.
  * Node.js - Package version matching follows the [semantic versioning](https://docs.npmjs.com/about-semantic-versioning) specification.
  * Python - Python version matching follows [PEP 440](https://peps.python.org/pep-0440/) semantics.



## Limitations

  * Artifact Analysis scans only packages with 100 or fewer files.

  * If you push the same package to multiple repositories, then you are charged for each push. For more information, see [Artifact Analysis pricing](https://docs.cloud.google.com/artifact-analysis/pricing).




## What's next

  * For information about viewing package vulnerabilities and filtering vulnerability occurrences, see [Scan packages automatically](https://docs.cloud.google.com/artifact-analysis/docs/package-scan-automatic).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
