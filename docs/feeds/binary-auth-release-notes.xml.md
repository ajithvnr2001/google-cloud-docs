---
url: https://docs.cloud.google.com/feeds/binary-auth-release-notes.xml
title: Binary Authorization - Release notes
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:54:41.927835+00:00
---

# Binary Authorization - Release notes

> Source: https://docs.cloud.google.com/feeds/binary-auth-release-notes.xml

tag:google.com,2016:binary-auth-release-notesBinary Authorization - Release notesGoogle Cloud Platform2026-07-21T00:00:00-07:00July 21, 2026tag:google.com,2016:binary-auth-release-notes#July_21_20262026-07-21T00:00:00-07:00Feature 

To provide long-term security and address threats from future quantum computers, Binary Authorization supports keys that use post-quantum cryptography (PQC) algorithms. These algorithms, such as `ML-DSA-65` (Dilithium3), are standardized to be resistant to attacks from both classical and quantum computers. To learn how to generate a PQC key pair and create an attestor, see [Create post-quantum cryptography (PQC) keys](https://docs.cloud.google.com/binary-authorization/docs/creating-attestors-cli#pqc-keys).

]]> August 19, 2024tag:google.com,2016:binary-auth-release-notes#August_19_20242024-08-19T00:00:00-07:00Feature 

Setting specific rules in Binary Authorization policies is generally available (GA) as of September 28, 2023.

]]> April 15, 2024tag:google.com,2016:binary-auth-release-notes#April_15_20242024-04-15T00:00:00-07:00Deprecated 

Binary Authorization legacy continuous validation (CV) is deprecated and will no longer be available on Google Cloud after May 1, 2025. You can instead use [continuous validation with check-based platform policies](https://docs.cloud.google.com/binary-authorization/docs/overview-cv). To learn how to migrate to check-based platform policies, see [Legacy continuous validation deprecation and shutdown](https://docs.cloud.google.com/binary-authorization/docs/deprecations/cv-project-singleton-policy).

]]> September 29, 2021tag:google.com,2016:binary-auth-release-notes#September_29_20212021-09-29T00:00:00-07:00Change 

Binary Authorization for Anthos clusters on VMware 0.2.2, which now supports Anthos clusters on VMware 0.1.9, is now available in [Preview](https://cloud.google.com/products#preview).

[Set up Binary Authorization for Anthos clusters on VMware](https://docs.cloud.google.com/binary-authorization/docs/setting-up-on-prem).

]]> September 28, 2021tag:google.com,2016:binary-auth-release-notes#September_28_20212021-09-28T00:00:00-07:00Change 

Binary Authorization for Cloud Run is now [generally available (GA)](https://cloud.google.com/products/?hl=EN#product-launch-stages).

View the [quickstart](https://docs.cloud.google.com/binary-authorization/docs/run/quickstart-cloud-run) or [set up Binary Authorization for Cloud Run](https://docs.cloud.google.com/binary-authorization/docs/run/overview) on your service.

]]> April 29, 2021tag:google.com,2016:binary-auth-release-notes#April_29_20212021-04-29T00:00:00-07:00Change 

Binary Authorization now supports Continuous Validation. See [Continuous Validation documentation](https://docs.cloud.google.com/binary-authorization/docs/overview-cv).

]]> June 23, 2020tag:google.com,2016:binary-auth-release-notes#June_23_20202020-06-23T00:00:00-07:00Change 

Added support for securing Binary Authorization resources with VPC Service Controls.

]]> March 04, 2020tag:google.com,2016:binary-auth-release-notes#March_04_20202020-03-04T00:00:00-08:00Deprecated 

Support for the Binary Authorization Beta API was discontinued on September 16, 2019. As a result, **the Binary Authorization Beta API will stop working after March 16, 2020.** To prevent service interruption, you must take actions outlined in the [Binary Authorization GA Migration Guide](https://docs.cloud.google.com/binary-authorization/docs/ga-migration-guide) prior to that date.

]]> September 16, 2019tag:google.com,2016:binary-auth-release-notes#September_16_20192019-09-16T00:00:00-07:00Feature 

The General Availability (GA) version of Binary Authorization is a feature of the [Anthos platform](https://cloud.google.com/anthos/). Use of Binary Authorization is included in the Anthos subscription. Please [contact](https://docs.cloud.google.com/anthos/pricing) your sales representative to enroll in Anthos.

]]> April 03, 2019tag:google.com,2016:binary-auth-release-notes#April_03_20192019-04-03T00:00:00-07:00Feature 

Binary Authorization now supports asymmetric PKIX key pairs to verify the identity of attestors. The asymmetric key pairs generated and stored in Cloud Key Management Service are compliant with the PKIX format. You set up PKIX keys when you create an attestor using the [Google Cloud Platform Console](https://docs.cloud.google.com/binary-authorization/docs/creating-attestors-console) or the [CLI](https://docs.cloud.google.com/binary-authorization/docs/creating-attestors-cli).

### Feature

Binary Authorization now supports [global policy evaluation mode](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#global_policy_evaluation_mode).

### Feature

Binary Authorization now supports dryrun mode.

Dryrun mode is a policy setting that allows non-conformant images to be deployed, but writes details about the policy violation and deployment to the audit log. Dryrun mode allows you to test a policy in your production environment before it goes into effect.

You can enable dryrun mode when you configure your policy using the [Google Cloud Platform Console](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-console) or the [CLI](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-cli).

]]> July 25, 2018tag:google.com,2016:binary-auth-release-notes#July_25_20182018-07-25T00:00:00-07:00Issue 

In the UI, detailed error messages are not shown for invalid whitelist patterns on a Policy or invalid PGP keys on an Attestor.

### Issue

In the UI, you cannot manage the IAM Policy on an Attestor or Binary Authorization Policy. Project level IAM permissions work as expected.

### Issue

Default whitelisting of exempt images may be incomplete, depending on the version of Kubernetes you are deploying to. You may need to add `gcr.io/google-containers/` and `k8s.io/` to the default whitelist.

### Issue

Error messaging sometimes lacks detail when policies are updated. If you encounter an error when you update a policy, check the names of any attestor resources defined to make sure they are correct.

### Issue

When editing a policy in the UI, you cannot remove/edit existing cluster specific deployment rules. This is possible using `gcloud` commands and the REST API.

]]>
