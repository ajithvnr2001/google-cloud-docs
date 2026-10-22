---
url: https://docs.cloud.google.com/binary-authorization/docs/overview/
title: Binary Authorization overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:20.373853+00:00
---

# Binary Authorization overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)
  * [ Guides ](https://docs.cloud.google.com/binary-authorization/docs/overview)



Send feedback 

#  Binary Authorization overview Stay organized with collections  Save and categorize content based on your preferences. 

This document provides an overview of Binary Authorization.

## What is Binary Authorization?

Binary Authorization is a Google Cloud product that you can use to implement software supply-chain security measures when you develop and deploy container-based applications.

## What does Binary Authorization do?

You can use Binary Authorization to do the following:

  * Monitor: You can configure continuous validation (CV) with check-based platform policies ([Preview](https://cloud.google.com/products/#product-launch-stages)) to periodically monitor that container images associated with running Pods conform to a policy that you define. If images don't conform with the policy, CV produces log entries in Cloud Logging.

  * Enforce: You can configure Binary Authorization enforcement to enforce that images that are being deployed to one of the supported container-based platforms conform with a policy that you define. Images that conform with the policy are allowed to be deployed; otherwise, they are disallowed from being deployed.




## What platforms does Binary Authorization support?

Binary Authorization supports the following platforms:

  * [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine/docs): runs images in clusters that are hosted on Google Cloud.
  * [Cloud Run](https://docs.cloud.google.com/run/docs): runs containerized applications on a fully managed serverless platform.
  * [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs): manages a reliable service mesh that is on-premises or on Google Cloud.
  * [Google Distributed Cloud software](https://docs.cloud.google.com/anthos/gke/docs/on-prem/overview): runs the images in GKE clusters that you host on your own hardware.



## Binary Authorization-related products

Binary Authorization is part of a deployment architecture that includes the following related products:

  * [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs), [Container Registry](https://docs.cloud.google.com/container-registry/docs) and other registries that store the images you want to deploy.
  * [Artifact Analysis](https://docs.cloud.google.com/artifact-analysis/docs/artifact-analysis) provides vulnerability information that you can use with Binary Authorization to control deployment. Separately, Artifact Analysis stores trusted metadata that is used in the authorization process.
  * [Security monitoring](https://docs.cloud.google.com/anthos/docs/concepts/security-monitoring), a dashboard you can use to assess your application security posture across interdependent Google Cloud products, including Binary Authorization.
  * Cloud Build, which produces attestations and provenance that Binary Authorization can use for enforcement and monitoring.
  * [Cloud Deploy](https://docs.cloud.google.com/deploy/docs/overview) is a managed continuous-delivery service, which automates delivery of applications to a series of target environments in a defined sequence.



Binary Authorization is based on the [Kritis](https://github.com/grafeas/kritis/blob/master/docs/binary-authorization.md) specification, which is part of the [Grafeas](https://grafeas.io/) open source project.

## Background

Software supply chain security aims to ensure that software is sourced, built, tested, released, and deployed according to internal best practices and standards.

Container-based architectures allow teams to develop highly decoupled systems—for example, those based on microservices architectures—and encourages the use of short-lifecycle development practices, including continuous integration (CI) and continuous deployment (CD).

In a container-based development environment, images can be deployed on a succession of clusters—such as testing, staging and release—which are part of the software supply chain.

Binary Authorization aims to reduce the risk of deploying defective, vulnerable, or unauthorized software in this type of environment. Using this service, you can prevent images from being deployed unless it satisfies a policy you define.

While Binary Authorization does not prescribe internal processes or best practices it helps you enforce your own practices by restricting deployment of images that have not passed your required checks.

## Lifecycle

A deployment lifecycle for images can consist of the following stages, where completing one stage is a prerequisite for progression to the next one—for example:

  1. Build and unit testing
  2. Deployment into a development environment where users aren't affected
  3. Deployment into a QA environment, where only internal users are affected
  4. Deployment into a canary environment, where only a fraction of external users are affected
  5. Deployment into production



Each stage can have its own deployment environment—for example, a GKE cluster or a Google Cloud project—and its own criteria that must be satisfied before an image can move onto the next stage. Binary Authorization allows you to define the rules by which an image passes from one stage to another and it provides the means for enforcing those rules.

## Attestations

The most common Binary Authorization use cases involve [attestations](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#attestations). An attestation certifies that a specific image has completed a previous stage, as described previously. You configure the Binary Authorization policy to verify the attestation before allowing the image to be deployed. At deploy time, instead of redoing activities that were completed in earlier stages, Binary Authorization only needs to verify the attestation.

Use cases involving attestations include the following:

  * **Build verification** , in which Binary Authorization uses attestations to verify that an image was built by a specific build system or continuous integration (CI) pipeline.

To learn how to set up a CI pipeline, based on Cloud Build, that can create an attestation, see [Cloud Build integration](https://docs.cloud.google.com/binary-authorization/docs/cloud-build).

  * **Manual check** , where a person, for example, a QA representative, manually creates the attestation.

To learn how to manually create an attestation, see [Create attestations](https://docs.cloud.google.com/binary-authorization/docs/making-attestations).




See [Get started with the Google Cloud console](https://docs.cloud.google.com/binary-authorization/docs/getting-started-console) for an end-to-end attestation tutorial.

## Features

Binary Authorization provides:

  * A [policy](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#policies) model that lets you describe the constraints under which images can be deployed
  * An [attestation](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#attestations) model that lets you define trusted authorities who can attest or verify that required processes in your environment have completed before deployment
  * A deploy-time enforcer that prevents images that violate the policy from being deployed



## Policy model

Binary Authorization implements a policy model, where a _policy_ is a set of rules that governs the deployment of container images. [_Rules_](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#rules) in a policy provide specific criteria that an image must satisfy before it can be deployed.

For more information about the Binary Authorization policy model and other concepts, see [Key concepts](https://docs.cloud.google.com/binary-authorization/docs/key-concepts).

## Setup

To set up Binary Authorization, you must first enable the service for the Google Cloud projects that comprise your deployment and authorization pipeline.

You then define the policy that specifies the constraints under which container images can be deployed. If your policy requires attestations before deployment, you must also set up attestors that can verify attestations before allowing associated images to deploy.

To set up Binary Authorization, see the following guides:

  * [Set up Binary Authorization on GKE](https://docs.cloud.google.com/binary-authorization/docs/setting-up)
  * [Set up Binary Authorization on Distributed Cloud](https://docs.cloud.google.com/binary-authorization/docs/setting-up-on-prem)
  * [Set up Binary Authorization on Cloud Run](https://docs.cloud.google.com/binary-authorization/docs/run/enabling-binauthz-cloud-run)



## Authorization

Before an image can be deployed, any required signers must create an attestation that verifies that the image is ready to move to the next deployment stage. The attestation is a record that contains the registry path and digest of the image, and that has been digitally signed using the signer's private cryptographic key.

For more information on authorization, see [Use attestations](https://docs.cloud.google.com/binary-authorization/docs/attestations).

## Enforcement

When you deploy an image, Binary Authorization checks the policy and enforces any rule it finds that governs its deployment.

If the image passes the constraints defined in the policy, Binary Authorization allows it to be deployed. If not, the service blocks deployment and writes a message to Cloud Audit Logs that describes why the image is out of compliance.

To view Binary Authorization enforcement events in Cloud Audit Logs, see the following guides:

  * [View audit logs (GKE)](https://docs.cloud.google.com/binary-authorization/docs/viewing-audit-logs)
  * [View audit logs (Cloud Run)](https://docs.cloud.google.com/binary-authorization/docs/run/viewing-audit-logs-cloud-run)
  * [View audit logs (Distributed Cloud)](https://docs.cloud.google.com/binary-authorization/docs/viewing-on-prem-logs)



For more information on deployment, see the following guides:

  * [Deploy containers (GKE)](https://docs.cloud.google.com/binary-authorization/docs/deploying-containers)
  * [Deploy containers (Distributed Cloud example](https://docs.cloud.google.com/binary-authorization/docs/setting-up-on-prem#disallow_all)
  * [Use Binary Authorization with Cloud Run](https://docs.cloud.google.com/binary-authorization/docs/run/enabling-binauthz-cloud-run)



## Continuous validation

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Continuous validation (CV) with check-based platform policies is a feature of Binary Authorization that periodically checks the metadata of container images associated with running Pods for continued policy conformance.

[Learn more about CV](https://docs.cloud.google.com/binary-authorization/docs/overview-cv).

## Secure Binary Authorization with VPC Service Controls

[VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) improves your ability to mitigate the risk of unauthorized copying or transfer of data from your Google-managed services and resources.

For more information about securing Binary Authorization-related resources, see [Secure with VPC Service Controls](https://docs.cloud.google.com/binary-authorization/docs/securing-with-vpcsc).

## Software supply chain security

Binary Authorization is one of the Google Cloud components you can use to protect your software supply chain. You can use Binary Authorization together with other Google Cloud products and features to improve the security posture of developer workflows and tools, software dependencies, CI/CD systems used to build and deploy your software, and runtime environments such as Google Kubernetes Engine and Cloud Run. To learn more, see [Software supply chain security](https://docs.cloud.google.com/software-supply-chain-security/docs/overview).

## What's next

  * For complete, end-to-end tutorials, see the following: 
    * [Get started using the Google Cloud console](https://docs.cloud.google.com/binary-authorization/docs/getting-started-console)
    * [Get started using the command-line tool](https://docs.cloud.google.com/binary-authorization/docs/getting-started-cli)
  * Configure a Binary Authorization policy for Cloud Service Mesh by using the [Google Cloud console](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-console#add-specific-rules-asm) or the [command-line tool](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-cli#set_specific_rules).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
