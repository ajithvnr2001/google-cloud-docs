---
url: https://docs.cloud.google.com/binary-authorization/docs/deprecations/cv-project-singleton-policy/
title: Legacy continuous validation deprecation and shutdown \u00a0|\u00a0 Binary Authorization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:48:15.660963+00:00
---

# Legacy continuous validation deprecation and shutdown  |  Binary Authorization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/docs/deprecations/cv-project-singleton-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)
  * [ Resources ](https://docs.cloud.google.com/binary-authorization/docs/resources)



Send feedback 

#  Legacy continuous validation deprecation and shutdown Stay organized with collections  Save and categorize content based on your preferences. 

The [Google Cloud Platform Terms of Service (section "Discontinuation of Services")](https://docs.cloud.google.com/terms) defines the deprecation policy that applies to Binary Authorization. The [deprecation policy](https://docs.cloud.google.com/terms/deprecation) only applies to the services, features, or products listed therein. 

After a service, feature, or product is officially deprecated, it continues to be available for at least the period of time defined in the Terms of Service. After this period of time, the service is scheduled for shutdown. 

Binary Authorization is ending support for legacy continuous validation (legacy CV) with project-singleton policies for GKE.

  * As of April 15, 2024, you can't enable legacy CV for Google Kubernetes Engine (GKE) on new projects.
  * Legacy CV will continue monitoring your GKE Pods through project-singleton policies for existing projects for which it is already enabled until May 1, 2025. After May 1, 2025, legacy CV will no longer monitor your Pods, and Cloud Logging entries will no longer be produced for Pod images that don't conform to the project-singleton Binary Authorization policy.



## Replacement: Continuous validation (CV) with check-based platform policies

Monitor your Pods using [continuous validation (CV) with check-based platform policies](https://docs.cloud.google.com/binary-authorization/docs/overview-cv).

In addition to support for attestations, check-based platform policies let you monitor the metadata of container images associated with your Pods to help you mitigate potential security issues. CV check-based policies provide checks that include the following:

  * [Vulnerability check](https://docs.cloud.google.com/binary-authorization/docs/cv-vulnerability-check): The image is checked for security vulnerabilities that are at a level of severity that you define.
  * [Sigstore check](https://docs.cloud.google.com/binary-authorization/docs/cv-sigstore-check): The image has attestations that are signed by sigstore.
  * [SLSA check](https://docs.cloud.google.com/binary-authorization/docs/cv-slsa-check): The image was built from source in a trusted directory and by a trusted builder.
  * [Trusted directory check](https://docs.cloud.google.com/binary-authorization/docs/cv-trusted-directory-check): The image must reside in a trusted directory within a trusted image repository.



Like legacy continuous validation, CV with check-based policies also logs Pods with non-conformant images to Logging.

If you use legacy continuous validation (legacy CV), see Migration.

For more information on how to use CV with check-based platform policies, see [Continuous validation overview](https://docs.cloud.google.com/binary-authorization/docs/overview-cv).

## Migration

To migrate from a legacy CV project-singleton policy to an equivalent check-based platform policy, do the following:

  * For an `ALWAYS_ALLOW` project-singleton policy, create a check-based platform policy without any `checkSet` block.
  * For an `ALWAYS_DENY` project-singleton policy, create a check-based platform policy with a single `checkSet` block that has an `alwaysDeny` check.
  * For a project-singleton policy that requires attestations, create a single check-based policy, and for each attestor in the project-singleton policy, add one [SimpleSigningAttestationCheck](https://docs.cloud.google.com/binary-authorization/docs/overview-cv#simple-signing-check) to the check-based policy. By using the same key pair, the check continues to work with your existing attestations, and logs only Pod images that don't have valid attestations.



Check-based platform policies are scoped to a GKE cluster, rather than a Google Cloud project. After you create a check-based platform policy, you can apply that policy to one or more clusters.

To enable CV with check-based platform policies on a cluster, the cluster's Binary Authorization settings must be [configured](https://docs.cloud.google.com/binary-authorization/docs/creating-cluster#console) during the cluster creation or update process.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
