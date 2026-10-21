---
url: https://docs.cloud.google.com/software-supply-chain-security/docs/safeguard-deploys/
title: Safeguard deployments \u00a0|\u00a0 Software supply chain security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:11.886827+00:00
---

# Safeguard deployments  |  Software supply chain security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/software-supply-chain-security/docs/safeguard-deploys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Software supply chain security ](https://docs.cloud.google.com/software-supply-chain-security/docs)
  * [ Guides ](https://docs.cloud.google.com/software-supply-chain-security/docs/overview)



Send feedback 

#  Safeguard deployments Stay organized with collections  Save and categorize content based on your preferences. 

This document describes best practices for protecting your deployments.

## Create and enforce deployment policies

To protect your runtime environments, define policies with criteria for deployment and validate policy compliance before and after deployment. Defining a policy that only allows code signed by predefined attestors helps in gating deployments and deploying only code from trusted origins.

Examples of deployment criteria include:

  * No known vulnerabilities with a severity above Medium
  * Source code is from a trusted source repository
  * A trusted build service ran the build
  * Build artifacts you are deploying are from a trusted artifact repository



### Generate metadata

To validate these requirements, your need to provide metadata about your build artifacts.

Build origins
    

_Build provenance_ is a collection of verifiable data about a build such as the digests of built images, the input source locations, the build toolchain, and the build duration. [SLSA](https://slsa.dev), a framework for assessing security posture, provides a [model for provenance](https://slsa.dev/provenance/) and [requirements for provenance](https://slsa.dev/spec/v0.1/requirements#provenance-requirements). Provenance is one requirement category in the framework, and each requirement is associated with SLSA levels so that you can incrementally implement mitigations.

  * For SLSA level 1 assurance, provenance must be available.
  * For SLSA level 2 assurance, provenance must be generated and consumers must be able to verify its authenticity and integrity.
  * SLSA Levels 3 and 4 have stricter requirements for provenance signing and depth of provenance data detail.


    

Some build services generate build provenance metadata.

  * In Google Cloud, Cloud Build [generates and signs build provenance](https://docs.cloud.google.com/build/docs/securing-builds/view-build-provenance) for container images supporting SLSA level 3 builds.
  * The SLSA framework provides [GitHub provenance tools](https://github.com/slsa-framework/slsa-github-generator). The tools generate non-forgeable SLSA provenance on GitHub that meet requirements in the [build](https://slsa.dev/spec/v0.1/requirements#build-requirements) and [provenance](https://slsa.dev/spec/v0.1/requirements#provenance-requirements) categories for SLSA level 3.
  * The open source [sigstore](https://www.sigstore.dev) project includes the [cosign](https://github.com/sigstore/cosign) tool for signing containers.


Vulnerabilies
    

Vulnerability scanning software checks your source code and build artifacts for known vulerabilties. Artifact Analysis can [automatically scan](https://docs.cloud.google.com/container-analysis/docs/automated-scanning-howto) container images pushed to Artifact Registry for vulnerabiilities. To check artifacts for vulnerabilities before you store them, you can use the [On-Demand Scanning API](https://docs.cloud.google.com/container-analysis/docs/on-demand-scanning-howto) in a local development environment or in a CI/CD pipeline, such as a [Cloud Build build step](https://docs.cloud.google.com/container-analysis/docs/ods-cloudbuild).

### Set up policy enforcement

Once you have metadata about your deployable artifacts, you need tools to enforce your policies.

In Google Cloud, you can configure a policy in [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/overview) for your deployments. Binary Authorization enforces policy for attempted deployments to supported container-based platforms. It can also perform continuous validation of policy for workloads running on GKE, Cloud Run, and GKE Enterprise.

Pre-deployment checks can block all images that are not in the exempt image list, so that only trusted images are deployed from trusted registries. Your policy can also require [attestations](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#attestations), digital documents that signify that the image was built successfully with a specific, required process. For example an attestion can indicate that an image is:

  * [Built by Cloud Build](https://docs.cloud.google.com/binary-authorization/docs/deploy-cloud-build).
  * [Does not contain vulnerabilities above a specified severity](https://docs.cloud.google.com/binary-authorization/docs/creating-attestations-kritis). If there are specitic vulnerabilities that do not apply to your applications, you can add them to an allowlist.



[Continuous validation](https://docs.cloud.google.com/binary-authorization/docs/overview-cv) extends policy validation to the post-deploy environment. When enabled, Binary Authorization provides validation throughout the Pod lifecycle by regularly logging policy conformance in [Cloud Logging](https://docs.cloud.google.com/logging/docs/audit). This is useful in a variety of situations. For example, if you change your policy after deploying a container, continuous validation logs Pods that violate te updated policy. It also logs policy violations for Pods deployed with [dry run](https://docs.cloud.google.com/binary-authorization/docs/enabling-dry-run) or [breakglass](https://docs.cloud.google.com/binary-authorization/docs/using-breakglass).

## Use gated deployment services

Deployment gating lets you approve or deny deployments at specific points in the deployment process using a standalone CI/CD service or a CI/CD service integrated with a process automation system. Gated deployments prevent unauthorized users from making changes to application environments. They provide additional oversight to the deployment process and greater visibility of approvals.

In Google Cloud, [Cloud Deploy](https://docs.cloud.google.com/deploy/docs/overview) offers a fully-managed service for deploying workloads to Google Kubernetes Engine. The [gated deployment](https://docs.cloud.google.com/deploy/docs/overview#approvals) feature lets users specify if an approval is needed for promotion to a target.

## Monitor your workloads

_Workloads_ are applications running on container-based platforms such as GKE and Cloud Run. The workloads that you deploy should ideally have a [hardened configuration](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster) that limits their attack surface.

Checking workloads across clusters for configuration issues can be difficult to do manually at scale. Google Cloud provides dashboards in Cloud Run and GKE to view security insights for workloads.

The [GKE security posture dashboard](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-security-posture-dashboard) provides you with guidance to strengthen the security posture of your clusters based on Google's recommendations. It includes automatic [workload configuration scanning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/protect-workload-configuration), which checks for known configuration concerns across all workloads. GKE checks each deployed workload against relevant industry best practices, such as policies in the [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/). GKE rates the severity of discovered issues and returns actionable recommendations and logs. You can use [Cloud Logging](https://docs.cloud.google.com/logging/docs/audit) to get an auditable trail of concerns for better reporting and observability. For instructions on viewing security insights in the GKE security posture dashboard, see [Deploy on GKE and view security insights](https://docs.cloud.google.com/software-supply-chain-security/docs/sds/deploy-gke-view-security-insights).

Cloud Run contains a security panel that displays software supply chain security insights such as the SLSA build level compliance info, build provenance, and vulnerabilities found in running services. For instructions on viewing security insights in the Cloud Run security insights panel, see [Deploy on Cloud Run and view security insights](https://docs.cloud.google.com/software-supply-chain-security/docs/sds/deploy-run-view-security-insights).

Google Cloud also provides other services and features to improve your security posture across the software development lifecycle. For more information, see the [software supply chain overview](https://docs.cloud.google.com/software-supply-chain-security/docs/overview).

## What's next

  * Learn the [best practices to safeguard source code](https://docs.cloud.google.com/software-supply-chain-security/docs/safeguard-source).
  * Learn the [best practices to safeguard dependencies](https://docs.cloud.google.com/software-supply-chain-security/docs/dependencies).
  * Learn the [best practices to safeguard builds](https://docs.cloud.google.com/software-supply-chain-security/docs/safeguard-builds).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
