---
url: https://docs.cloud.google.com/software-supply-chain-security/docs/overview/
title: Software supply chain security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:37:40.181338+00:00
---

# Software supply chain security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/software-supply-chain-security/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Software supply chain security ](https://docs.cloud.google.com/software-supply-chain-security/docs)
  * [ Guides ](https://docs.cloud.google.com/software-supply-chain-security/docs/overview)



Send feedback 

#  Software supply chain security Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud provides a comprehensive and modular set of capabilities and tools across Google Cloud products that your developers, DevOps, and security teams can use to improve the security posture of your software supply chain.

## Software supply chains

A _software supply chain_ consists of all the code, people, systems, and processes that contribute to development and delivery of your software, both inside and outside of your organization. It includes:

  * Code you create, its dependencies, and the internal and external software you use to develop, build, package, install, and run your software.
  * Processes and policies for system access, testing, review, monitoring and feedback, communication, and approval.
  * Systems you trust to develop, build, store, and run your software and its dependencies.



Given the broad reach and complexity of software supply chains, there are numerous ways to introduce unauthorized changes to the software that you deliver to your users. These [attack vectors](https://docs.cloud.google.com/software-supply-chain-security/docs/attack-vectors) span the software lifecycle. While some attacks are targeted, such as the attack on the [SolarWinds](https://www.crowdstrike.com/blog/sunspot-malware-technical-analysis/) build system, other threats are indirect or enter the supply chain through weaknesses in process or neglect.

For example, an assessment of the [Apache Log4j vulnerability](https://security.googleblog.com/2021/12/understanding-impact-of-apache-log4j.html) in December 2021 by the Google Open Source Insights team found that there were over 17,000 affected packages in Maven Central. Most of these packages did not depend directly on the vulnerable `log4j-core` package, but had dependencies that required the package.

Development practices and processes also impact software supply chains. Process gaps such as lack of code review or security criteria for deployment to production can allow bad code to unintentionally enter the supply chain. Similarly, lack of dependency management increases the risk of vulnerabilities from external source or software packages that you use for development, builds, or deployment.

## Safeguard software supply chains on Google Cloud

Google Cloud provides:

  * Products and features that incorporate security best practices for development, building, testing, deployment, and policy enforcement.
  * Dashboards in the Google Cloud console that provide security information about source, builds, artifacts, deployments, and runtimes. This information includes vulnerabilities in build artifacts, build provenance, and [Software Bill of Materials (SBOM)](https://www.cisa.gov/sbom) dependency lists.
  * Information identifying the maturity level of your software supply chain security using the [Supply-chain Levels for Software Artifacts (SLSA) framework](https://slsa.dev/spec/v0.1/levels).



The following diagram shows Google Cloud services that work together to protect the software supply chain. You can integrate some or all of these components into your software supply chain to improve your security posture.

![Google Cloud software supply chain components](https://docs.cloud.google.com/software-supply-chain-security/images/sds-overview.png)

### Protect the development environment

[Cloud Workstations](https://docs.cloud.google.com/workstations/docs/concepts) provides fully-managed development environments on Google Cloud. IT and security administrators can provision, scale, manage, and protect their development environments. Developers can access development environments with consistent configurations and customizable tooling.

Cloud Workstations shifts security left by enhancing the security posture of your application development environments. Security features include VPC Service Controls, private ingress or egress, forced image update, and Identity and Access Management access policies. Cloud Workstations provides additional data loss prevention capabilities when combined with Chrome Enterprise Premium.

### Protect the software supply

Securing the software supply — build artifacts and application dependencies — is a critical step in improving your software supply chain security. The widespread use of open source software makes this problem particularly challenging.

  * [Assured Open Source Software](https://docs.cloud.google.com/assured-open-source-software/docs) provides open source packages that Google has verified and tested. These packages are built using Google's secure pipelines and are regularly scanned, analyzed, and tested for vulnerabilities.

  * [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/overview) is a universal package manager for all your build artifacts and dependencies. By centralizing all your artifacts and dependencies, you have more visibility into and control over the code in your software supply chain.

    * [Remote repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-overview) store artifacts from preset external sources such as Docker Hub, Maven Central, the Python Package Index (PyPI), Debian or CentOS as well as user-defined sources for [supported formats](https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-overview#supported-formats). Caching artifacts in remote repositories reduces download time, improves package availability, and includes vulnerability scanning if scanning is enabled.
    * [Virtual repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/virtual-overview) consolidate repositories of the same format behind a single endpoint and let you control the search order across upstream repositories. You can prioritize your private packages, which reduces the risk of [dependency confusion attacks](https://docs.cloud.google.com/software-supply-chain-security/docs/dependencies#public-dependencies)
    * You can also protect artifacts by configuring security features such as access control, VPC Service Controls service perimeters, organizational policies, and other security features. For details, see the [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/protect-artifacts) documentation.
  * [Artifact Analysis](https://docs.cloud.google.com/artifact-analysis/docs/container-analysis) proactively detects vulnerabilities for artifacts in Artifact Registry.

    * Integrated [on-demand](https://docs.cloud.google.com/artifact-analysis/docs/scanning-types#ods) or [automated scanning](https://docs.cloud.google.com/artifact-analysis/docs/scanning-types#automated) for base container images and language packages in containers.
    * The ability to [generate a software bill of materials (SBOM)](https://docs.cloud.google.com/artifact-analysis/docs/generate-store-sboms) and upload [Vulnerability Exploitability eXchange (VEX) statements](https://docs.cloud.google.com/artifact-analysis/docs/upload-view-vex-statements) for the images in Artifact Registry.



### Protect the CI/CD pipeline

Bad actors can attack software supply chains by compromising the CI/CD pipelines. The following products help you to secure your CI/CD pipeline:

  * [Cloud Build](https://docs.cloud.google.com/build/docs/overview) runs your builds on Google Cloud infrastructure. Security features include granular IAM permissions, VPC Service Controls, and isolated and ephemeral build environments. Features specific to software supply chain security include:

    * Support for [SLSA Level 3 builds for container images](https://docs.cloud.google.com/build/docs/securing-builds/view-build-provenance).
    * Ability to generate authenticated and non-falsifiable [build provenance](https://docs.cloud.google.com/build/docs/securing-builds/view-build-provenance) for containerized applications.
    * [Security insights](https://docs.cloud.google.com/software-supply-chain-security/docs/sds/build-view-security-insights) for built applications. This includes:

      * The SLSA build level, which identifies the maturity level of your software build process in accordance with the [SLSA specification](https://slsa.dev/spec/v0.1/levels).
      * Vulnerabilities in build artifacts.
      * Build provenance, which is a collection of verifiable metadata about a build. It includes details such as the digests of the built images, the input source locations, the build toolchain, build steps, and the build duration.

For instructions on viewing security insights for built applications, see [Build an application and view security insights](https://docs.cloud.google.com/software-supply-chain-security/docs/sds/build-view-security-insights).

  * [Cloud Deploy](https://docs.cloud.google.com/deploy/docs/overview) automates delivery of your applications to a series of target environments in a defined sequence. It supports continuous delivery directly to Google Kubernetes Engine, GKE Enterprise, and Cloud Run, with one-click approvals and rollbacks, enterprise security and audit, as well as built-in delivery metrics. Additionally, [it displays security insights for deployed applications](https://docs.cloud.google.com/deploy/docs/securing/security-insights).




### Protect applications in production

[Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview) and [Cloud Run](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run) help secure the security posture of your runtime environments. They both come with security features to protect your applications at runtime.

  * GKE can assess your container security posture and give active guidance around cluster settings, workload configuration, and vulnerabilities. GKE includes a security posture dashboard that provides opinionated, actionable recommendations to improve your security posture. For instructions on viewing security insights in the GKE security posture dashboard, see [Deploy on GKE and view security insights](https://docs.cloud.google.com/software-supply-chain-security/docs/sds/deploy-gke-view-security-insights).

  * Cloud Run includes a security panel that displays software supply chain security insights such as the SLSA build level compliance info, build provenance, and vulnerabilities found in running services. For instructions on viewing security insights in the Cloud Run security insights panel, see [Deploy on Cloud Run and view security insights](https://docs.cloud.google.com/software-supply-chain-security/docs/sds/deploy-run-view-security-insights).




### Build a chain of trust through policy

[Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/overview) helps establish, maintain, and verify a chain of trust along your software supply chain by collecting _attestations_ , which are digital documents that certify images.

An attestation signifies that the associated image was built by successfully executing a specific, required process. Based on these attestations collected, Binary Authorization helps define, verify, and enforce trust-based policies. It makes sure the image is deployed only when the attestations meet your organization's policy. You can configure Binary Authorization to notify you if it finds any policy violations.

For example, attestations can indicate that an image is:

  * [Built by Cloud Build](https://docs.cloud.google.com/binary-authorization/docs/deploy-cloud-build).
  * Does not contain vulnerabilities higher than a specified severity. If there are specific vulnerabilities that don't apply to your applications, you can add them to an allowlist.



You can use Binary Authorization with GKE and Cloud Run.

## Pricing

Each Google Cloud service has its own pricing. For details, refer to the pricing documentation for the services you are interested in.

  * [Cloud Workstations](https://cloud.google.com/workstations/pricing)
  * Cloud Code: Available to all Google Cloud customers at no charge.
  * Assured OSS: Contact the [sales team](https://cloud.google.com/contact/) for pricing information.
  * [Artifact Registry](https://cloud.google.com/artifact-registry/pricing)
  * [Artifact Analysis](https://cloud.google.com/artifact-analysis/pricing)
  * [Cloud Build](https://cloud.google.com/build/pricing)
  * [Cloud Deploy](https://cloud.google.com/deploy/pricing)
  * [Cloud Run](https://cloud.google.com/run/pricing)
  * [GKE](https://cloud.google.com/kubernetes-engine/pricing)
  * [Binary Authorization](https://cloud.google.com/binary-authorization/pricing)



## What's next

  * [Learn about threats to software supply chains](https://docs.cloud.google.com/software-supply-chain-security/docs/attack-vectors).
  * [Assess](https://docs.cloud.google.com/software-supply-chain-security/docs/assess) your existing security posture so that you can identify ways to strengthen it.
  * Learn about [practices to protect your software supply chain](https://docs.cloud.google.com/software-supply-chain-security/docs/practices) and how Google Cloud products supports these practices.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
