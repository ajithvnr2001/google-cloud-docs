---
url: https://docs.cloud.google.com/binary-authorization/docs/release-notes/
title: Binary Authorization release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:14.916483+00:00
---

# Binary Authorization release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)
  * [ Resources ](https://docs.cloud.google.com/binary-authorization/docs/resources)



Send feedback 

#  Binary Authorization release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Binary Authorization. You can periodically check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/binary-auth-release-notes.xml) directly. 

## July 21, 2026

Feature

To provide long-term security and address threats from future quantum computers, Binary Authorization supports keys that use post-quantum cryptography (PQC) algorithms. These algorithms, such as `ML-DSA-65` (Dilithium3), are standardized to be resistant to attacks from both classical and quantum computers. To learn how to generate a PQC key pair and create an attestor, see [Create post-quantum cryptography (PQC) keys](https://docs.cloud.google.com/binary-authorization/docs/creating-attestors-cli#pqc-keys).

## August 19, 2024

Feature

Setting specific rules in Binary Authorization policies is generally available (GA) as of September 28, 2023.

## April 15, 2024

Deprecated

Binary Authorization legacy continuous validation (CV) is deprecated and will no longer be available on Google Cloud after May 1, 2025. You can instead use [continuous validation with check-based platform policies](https://docs.cloud.google.com/binary-authorization/docs/overview-cv). To learn how to migrate to check-based platform policies, see [Legacy continuous validation deprecation and shutdown](https://docs.cloud.google.com/binary-authorization/docs/deprecations/cv-project-singleton-policy).

## September 29, 2021

Change

Binary Authorization for Anthos clusters on VMware 0.2.2, which now supports Anthos clusters on VMware 0.1.9, is now available in [Preview](https://cloud.google.com/products#preview).

[Set up Binary Authorization for Anthos clusters on VMware](https://docs.cloud.google.com/binary-authorization/docs/setting-up-on-prem).

## September 28, 2021

Change

Binary Authorization for Cloud Run is now [generally available (GA)](https://cloud.google.com/products/?hl=EN#product-launch-stages).

View the [quickstart](https://docs.cloud.google.com/binary-authorization/docs/run/quickstart-cloud-run) or [set up Binary Authorization for Cloud Run](https://docs.cloud.google.com/binary-authorization/docs/run/overview) on your service.

## April 29, 2021

Change

Binary Authorization now supports Continuous Validation. See [Continuous Validation documentation](https://docs.cloud.google.com/binary-authorization/docs/overview-cv).

## June 23, 2020

Change

Added support for securing Binary Authorization resources with VPC Service Controls.

## March 04, 2020

Deprecated

Support for the Binary Authorization Beta API was discontinued on September 16, 2019. As a result, **the Binary Authorization Beta API will stop working after March 16, 2020.** To prevent service interruption, you must take actions outlined in the [Binary Authorization GA Migration Guide](https://docs.cloud.google.com/binary-authorization/docs/ga-migration-guide) prior to that date.

## September 16, 2019

Feature

The General Availability (GA) version of Binary Authorization is a feature of the [Anthos platform](https://cloud.google.com/anthos/). Use of Binary Authorization is included in the Anthos subscription. Please [contact](https://docs.cloud.google.com/anthos/pricing) your sales representative to enroll in Anthos.

## April 03, 2019

Feature

Binary Authorization now supports asymmetric PKIX key pairs to verify the identity of attestors. The asymmetric key pairs generated and stored in Cloud Key Management Service are compliant with the PKIX format. You set up PKIX keys when you create an attestor using the [Google Cloud Platform Console](https://docs.cloud.google.com/binary-authorization/docs/creating-attestors-console) or the [CLI](https://docs.cloud.google.com/binary-authorization/docs/creating-attestors-cli).

Feature

Binary Authorization now supports [global policy evaluation mode](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#global_policy_evaluation_mode).

Feature

Binary Authorization now supports dryrun mode.

Dryrun mode is a policy setting that allows non-conformant images to be deployed, but writes details about the policy violation and deployment to the audit log. Dryrun mode allows you to test a policy in your production environment before it goes into effect.

You can enable dryrun mode when you configure your policy using the [Google Cloud Platform Console](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-console) or the [CLI](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-cli).

## July 25, 2018

Issue

In the UI, detailed error messages are not shown for invalid whitelist patterns on a Policy or invalid PGP keys on an Attestor.

Issue

In the UI, you cannot manage the IAM Policy on an Attestor or Binary Authorization Policy. Project level IAM permissions work as expected.

Issue

Default whitelisting of exempt images may be incomplete, depending on the version of Kubernetes you are deploying to. You may need to add `gcr.io/google-containers/` and `k8s.io/` to the default whitelist.

Issue

Error messaging sometimes lacks detail when policies are updated. If you encounter an error when you update a policy, check the names of any attestor resources defined to make sure they are correct.

Issue

When editing a policy in the UI, you cannot remove/edit existing cluster specific deployment rules. This is possible using `gcloud` commands and the REST API.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
