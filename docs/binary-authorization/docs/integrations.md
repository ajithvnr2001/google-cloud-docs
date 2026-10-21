---
url: https://docs.cloud.google.com/binary-authorization/docs/integrations/
title: Integrate with third-party tools \u00a0|\u00a0 Binary Authorization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:48:14.473207+00:00
---

# Integrate with third-party tools  |  Binary Authorization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/docs/integrations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)
  * [ Guides ](https://docs.cloud.google.com/binary-authorization/docs/overview)



Send feedback 

#  Integrate with third-party tools Stay organized with collections  Save and categorize content based on your preferences. 

This document lists third-party tool integrations with [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/overview).

## Synopsis Black Duck

**Synopsis Black Duck** is an open source management solution that enables you to create rules to govern your use of open source components. The Synopsis Black Duck GKE Binary Authorization solution creates Binary Authorization attestations based on Black Duck policy rules.

View the [Synopsis Black Duck integration guide](https://synopsys.atlassian.net/wiki/spaces/PARTNERS/pages/72777811/Attesting+an+Image+Based+on+a+Black+Duck+Scan).

## CloudBees

**CloudBees CI** is a continuous integration (CI) solution that manages Jenkins-based CI pipelines. You can use CloudBees CI with Jenkins to build and sign container images and to create Binary Authorization attestations.

View the [CloudBees Integration Guide](https://www.cloudbees.com/blog/ensure-application-compliance-cloudbees-core-and-binary-authorization-google-cloud-platform).

## CircleCI

**CircleCI** is a CI platform. You can use CircleCI to set up Binary Authorization policies, create signing keys, build and sign container images, and create Binary Authorization attestations.

View the [CircleCI integration guide](https://circleci.com/developer/orbs/orb/circleci/gcp-binary-authorization).

## Digester

[Digester](https://github.com/google/k8s-digester) is a Google-developed open source tool that automatically resolves tags to image digests and adds the digests to Kubernetes resources. Binary Authorization matches these digests with attestations. Digester resolves tags for container and init container images in Kubernetes Pod and Pod template specs.

## Terraform

[Terraform](https://www.terraform.io/intro/index.html) is an infrastructure management platform.

You can use the Terraform [Google Provider](https://www.terraform.io/docs/providers/google/index.html) to:

  * [Create attestors](https://www.terraform.io/docs/providers/google/r/binary_authorization_attestor.html),
  * [Manage IAM](https://www.terraform.io/docs/providers/google/r/binary_authorization_attestor_iam.html),
  * [Manage Binary Authorization policies](https://www.terraform.io/docs/providers/google/r/binary_authorization_policy.html).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
