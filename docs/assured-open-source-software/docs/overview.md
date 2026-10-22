---
url: https://docs.cloud.google.com/assured-open-source-software/docs/overview/
title: Overview of Assured Open Source Software \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:36:25.028312+00:00
---

# Overview of Assured Open Source Software  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-open-source-software/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Open Source Software ](https://docs.cloud.google.com/assured-open-source-software/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-open-source-software/docs/service-account-creation)



Send feedback 

#  Overview of Assured Open Source Software Stay organized with collections  Save and categorize content based on your preferences. 

Assured Open Source Software (Assured OSS) lets you take advantage of the security and experience that Google applies to open source software (OSS) by incorporating the same OSS packages that Google secures and uses into your own developer workflows.

Assured OSS lets you do the following:

  * Obtain your OSS packages from a trusted and known supplier.
  * Learn more about package contents with Assured [SBOMs](https://www.cisa.gov/sbom) that are provided in industry standard formats like [SPDX](https://spdx.dev/).
  * Learn about threats and security of a package with VEX information in an industry-standard format like [CycloneDX](https://cyclonedx.org/).
  * Reduce security risk as Google is actively scanning, finding, and fixing new vulnerabilities in curated packages.
  * Increase confidence in the integrity of the OSS that you are using through signed, tamper-evident [provenance](https://slsa.dev/provenance/v0.2).
  * Choose from more than one thousand of the most popular Java, Go, Python, and JavaScript (NPM) packages, including common machine learning and artificial intelligence projects like TensorFlow, Pandas, and Scikit-learn.



The open-source packages are built by Google in a secure manner. These packages meet [Supply-chain Levels for Software Artifacts (SLSA) level 3 requirements](https://slsa.dev/spec/v0.1/levels) and have a verifiable provenance and SBOM.

## Assured OSS tiers

Assured OSS has a Free tier and a Premium tier. The Premium tier is available when you purchase Security Command Center Premium or Security Command Center Enterprise.

The Free tier includes the following:

  * Python, Go, and Java open-source packages in curated repositories.
  * Manual setup steps.
  * Curated repositories created in a Google-managed project.
  * Universal proxy endpoints for open-source packages. This proxy lets you download open-source packages and their metadata from one source, whether the packages were built by Google or not.
  * Support for Amazon Web Service (AWS) account access.



The Premium tier lets you [integrate Assured OSS with Security Command Center Premium or Security Command Center Enterprise](https://docs.cloud.google.com/security-command-center/docs/integrate-aoss-with-scc). It includes the following:

  * Python, Go, Java, and JavaScript (NPM) open-source packages in curated repositories.
  * JavaScript open-source packages in a canonical repository.
  * Automated setup as part of the organization-level activation process for Security Command Center Premium or Security Command Center Enterprise.
  * Curated repositories created in a project that you specify.
  * Universal package metadata that's collected and signed by Google. This metadata provides information about the package build, any vulnerabilities, and package health. The package health information is only available for packages that are built by Google.



For more information about Security Command Center subscription pricing, see [Security Command Center pricing](https://cloud.google.com/security-command-center/pricing).

## Assured OSS repository options

Assured OSS packages are stored on a Google-managed [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs) repository. You can access and download the open source packages offered by Assured OSS using one of the following methods:

  * Set up a remote (also called a _mirror_ or a _proxy_) repository in your environment to act as a proxy for the Google-managed Artifact Registry repository. Your developers can connect to the remote repository to download the packages. Use this method if you are using a repository manager like Jfrog Artifactory or Sonatype Nexus.

  * Connect to the Artifact Registry repository directly using a service account. Use this method if developers are using build tools like Maven, Gradle, Go, or pip.

  * Use a virtual upstream repository that acts as a single access point for your developers so that they can download, install, or deploy packages.  
In the Premium tier, two virtual repositories are created automatically: one for Java packages and one for Python packages. In the Free tier, you must configure a virtual repository yourself. You can use an Artifact Registry standard repository or an Artifact Registry remote repository as your upstream virtual repository. You can also use an Assured OSS type repository, which is a wrapper over a virtual repository that has access to both Free tier and Premium tier packages. Assured OSS type repository performs server-side checks.




The following diagram shows Assured OSS connected to a remote repository.

![Connecting to a remote repository.](https://docs.cloud.google.com/static/assured-open-source-software/images/aoss-remote-repository.svg)

## Software supply chain security

Assured Open Source Software is one of the Google Cloud components you can use to protect your software supply chain. You can use Assured Open Source Software together with other Google Cloud products and features to improve the security posture of developer workflows and tools, software dependencies, CI/CD systems used to build and deploy your software, and runtime environments such as Google Kubernetes Engine and Cloud Run. To learn more, see [Software supply chain security](https://docs.cloud.google.com/software-supply-chain-security/docs/overview).

## What's next

  * To use the Free tier, see [Enable Assured OSS](https://docs.cloud.google.com/assured-open-source-software/docs/enable).
  * To integrate with Security Command Center Enterprise, see [Integrate with Assured OSS for code security](https://docs.cloud.google.com/security-command-center/docs/integrate-aoss-with-scc).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
