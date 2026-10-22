---
url: https://docs.cloud.google.com/binary-authorization/docs/attestations/
title: Attestations overview \u00a0|\u00a0 Binary Authorization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:12:00.633714+00:00
---

# Attestations overview  |  Binary Authorization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/docs/attestations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)
  * [ Guides ](https://docs.cloud.google.com/binary-authorization/docs/overview)



Send feedback 

#  Attestations overview Stay organized with collections  Save and categorize content based on your preferences. 

This guide describes how to create and use Binary Authorization [attestations](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#attestations). After a container image is built, an attestation can be created to affirm that a required activity was performed on the image such as a regression test, vulnerability scan, or other test. The attestation is created by signing the image's unique digest.

During deployment, instead of repeating the activities, Binary Authorization verifies the attestations using an attestor. If all of the attestations for an image are verified, Binary Authorization allows the image to be deployed.

## Before you begin

  1. [Enable Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/enabling).

  2. Set up Binary Authorization with one of the following products:

     * [Binary Authorization for Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/binary-authorization/docs/setting-up)
     * [Binary Authorization for Cloud Run](https://docs.cloud.google.com/binary-authorization/docs/run/enabling-binauthz-cloud-run)
     * [Binary Authorization for Google Distributed Cloud](https://docs.cloud.google.com/binary-authorization/docs/setting-up-on-prem)



Cloud Service Mesh users need to only set up the Binary Authorization policy. To do so, see Configure a policy, later in this guide.

## Create an attestor

To use attestations, you first create [attestors](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#attestors). At deploy time, Binary Authorization uses attestors to verify the attestation associated with the container image.

**Note:** Cloud Build users, you can use the `built-by-cloud-build` attestor to [deploy only images built by Cloud Build](https://docs.cloud.google.com/binary-authorization/docs/deploy-cloud-build).

You can create attestors using the following methods:

  * The [Google Cloud CLI](https://docs.cloud.google.com/binary-authorization/docs/creating-attestors-cli)
  * The [Google Cloud console](https://docs.cloud.google.com/binary-authorization/docs/creating-attestors-console)



## Configure a policy rule to require attestations

This section describes how to configure the policy to require attestations.

###  GKE 

  * Configure the default rule to require attestations using the following methods:

    * The [Google Cloud console](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-console#default-rule)
    * The [command-line tool](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-cli#default-rule)
  * Configure a cluster-specific rule to require attestations using the following methods:

    * The [Google Cloud console](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-console#add-cluster-name-gke)
    * The [command-line tool](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-cli#set_cluster_specific_rules)



###  Cloud Run 

Configure the default rule to require attestations using one of the following methods:

  * [The Google Cloud console](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-console)
  * [The command-line tool](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-cli)



###  Distributed Cloud 

  * Configure the default rule to require attestations using the following methods: 
    * The [Google Cloud console](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-console#default-rule)
    * The [command-line tool](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-cli#default-rule)
  * Configure a cluster-specific rule to require attestations using the following methods: 
    * The [Google Cloud console](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-console#add-cluster-name-anthos)
    * The [command-line tool](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-cli#set_cluster_specific_rules)



###  Cloud Service Mesh 

Cloud Service Mesh users can create rules—including rules that require attestations—that are scoped to either a mesh service identity, a Kubernetes service account, or a Kubernetes namespace.

To configure a specific rule, use the following methods:

  * The [Google Cloud console](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-console#add-specific-rules-asm)
  * The [command-line tool](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-cli#set_specific_rules)



## Create attestations

Attestations are created by a [signer](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#signers). The process of creating an attestation is also known as _signing an image_. A signer can be a person who manually creates an attestation. Alternatively, a signer can be an automated service. For instructions that describe different approaches to creating attestations, see the following pages:

  * [Create attestations manually](https://docs.cloud.google.com/binary-authorization/docs/making-attestations) by signing a container image.
  * [Create attestations in a Cloud Build pipeline](https://docs.cloud.google.com/binary-authorization/docs/cloud-build).



## Deploy an image

After you create an attestation, you are ready to deploy the associated image.

###  GKE 

[Deploy images using GKE](https://docs.cloud.google.com/binary-authorization/docs/deploying-containers).

###  Cloud Run 

[Deploy images using Cloud Run](https://docs.cloud.google.com/binary-authorization/docs/run/enabling-binauthz-cloud-run).

###  Distributed Cloud 

[Deploy images using Distributed Cloud](https://docs.cloud.google.com/binary-authorization/docs/deploying-containers).

###  Cloud Service Mesh 

Cloud Service Mesh workloads are enforced as soon as the policy is saved.

## What's next

  * [View audit logs](https://docs.cloud.google.com/binary-authorization/docs/viewing-audit-logs)
  * [View Cloud Run breakglass audit logs](https://docs.cloud.google.com/binary-authorization/docs/run/viewing-audit-logs-cloud-run)
  * [Use breakglass (GKE)](https://docs.cloud.google.com/binary-authorization/docs/using-breakglass)
  * [Use breakglass (Cloud Run)](https://docs.cloud.google.com/binary-authorization/docs/run/using-breakglass-cloud-run)
  * [Use image digests in Kubernetes manifests](https://docs.cloud.google.com/architecture/using-container-image-digests-in-kubernetes-manifests)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
