---
url: https://docs.cloud.google.com/security-command-center/docs/artifact-guard-overview/
title: Artifact guard overview \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:34:09.301957+00:00
---

# Artifact guard overview  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/artifact-guard-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Artifact guard overview Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions.  Artifact guard and CI/CD integration will be shut down on October 30, 2026. 

Artifact guard is a security service that detects and manages container image vulnerabilities. It evaluates container images against configurable security policies during build generation, registry storage, and runtime execution.

## Key capabilities

Artifact guard enforces vulnerability policies across three main stages of your container lifecycle:

  * **Build-time scanning** : Integrates directly into CI/CD platforms (such as Cloud Build, GitHub Actions, and Jenkins) to scan containers as they are built. If an image violates your security policy, the build fails before the image can be published.
  * **Registry admission control** : Evaluates images stored in Artifact Registry. Using Binary Authorization, artifact guard blocks non-compliant images from being deployed to Google Kubernetes Engine (GKE) clusters.
  * **Runtime monitoring** : Continuously monitors running containers in GKE clusters for newly disclosed vulnerabilities and enriches findings in Security Command Center.



## Security policy enforcement

Artifact guard lets you define centralized vulnerability policies that help protect your environment by doing the following:

  * **Blocking vulnerable artifacts early** : Helps prevent developers from pushing container images that contain vulnerabilities exceeding your specified severity threshold (for example, blocking images with `HIGH` or `CRITICAL` vulnerabilities).
  * **Restricting specific packages and CVEs** : Lets you explicitly allow or deny specific software packages, package versions, or Common Vulnerabilities and Exposures (CVEs).
  * **Managing exceptions** : Provides grace periods for specific CVEs so teams can continue deploying while fixes are developed, without permanently compromising security.
  * **Centralizing security findings** : Combines scan results from CI/CD pipelines, artifact registries, and running GKE clusters into a single view in Security Command Center.



### Target roles and responsibilities

Artifact guard is designed for the following teams:

  * **Security Administrators** : Define and manage centralized vulnerability policies.
  * **DevOps or Platform Engineering teams** : Add CI/CD scanning connectors to build pipelines and configure GKE admission controllers.
  * **Application Developers** : View build failure logs to identify and update vulnerable dependencies before redeploying.



### Key terms and concepts

  * **Common Vulnerabilities and Exposures (CVE)** : A publicly disclosed computer security vulnerability that is assigned a unique identifier.
  * **Software Bill of Materials (SBOM)** : A machine-readable inventory of software components and dependencies used to identify CVEs and other security risks.
  * **Artifact** : In the context of artifact guard, a container image built by a CI/CD pipeline or stored in a container registry.



### High-level workflow

Artifact guard policies apply to three distinct scopes:

  * **CI/CD platform** : [Cloud Build](https://docs.cloud.google.com/build/docs/overview), GitHub Actions, or Jenkins pipelines.
  * **Registry** : Artifact Registry repositories.
  * **Runtime** : GKE clusters.



To protect your environment, complete the following workflow:

  1. To create a policy for a CI/CD pipeline, create a connector to your CI/CD environment using the [CI/CD integration](https://docs.cloud.google.com/security-command-center/docs/configure-cicd-integration). For repositories or GKE clusters, you define the policy scope natively during policy configuration.

  2. [Configure artifact guard policies](https://docs.cloud.google.com/security-command-center/docs/configure-artifact-guard) for your target scopes (pipeline, registry, or runtime).

  3. Run evaluations against your policies:

     * **Pipeline** : When a CI/CD build runs, build-time scanning evaluates the container image against your policy. If the image violates your security policy, the build fails before the image can be published. Developers can examine the failure details in the build logs and update their dependencies.
     * **Registry** : During deployment of an image stored in Artifact Registry, registry admission control uses Binary Authorization to evaluate the policy and block non-compliant images from being deployed to GKE clusters.
     * **Runtime** : Runtime monitoring continuously evaluates running containers in GKE clusters for newly disclosed vulnerabilities and enriches findings in Security Command Center for policy violations.



## What's next

Learn how to [configure artifact guard policies](https://docs.cloud.google.com/security-command-center/docs/configure-artifact-guard).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
