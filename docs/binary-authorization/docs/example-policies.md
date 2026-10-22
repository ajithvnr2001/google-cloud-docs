---
url: https://docs.cloud.google.com/binary-authorization/docs/example-policies/
title: Example policies \u00a0|\u00a0 Binary Authorization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:47.951774+00:00
---

# Example policies  |  Binary Authorization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/docs/example-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)
  * [ Reference ](https://docs.cloud.google.com/binary-authorization/docs/api)



Send feedback 

#  Example policies Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This document or section includes references to one or more terms that Google considers disrespectful or offensive. The terms are used because they are keywords in the software that's described in the document. 

The terms: `whitelist`

This page contains example [policies](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#policies) for Binary Authorization specified in [YAML format](https://docs.cloud.google.com/binary-authorization/docs/policy-yaml-reference). For instructions on configuring policies in Binary Authorization, see [Configure a policy using the Google Cloud CLI](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-cli) or [Configure a policy using the Google Cloud console](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-console).

## Allow all deployments

The following example shows how to allow all container images to be deployed with no constraints.
    
    
    name: projects/example-project/policy
    defaultAdmissionRule:
      evaluationMode: ALWAYS_ALLOW
      enforcementMode: ENFORCED_BLOCK_AND_AUDIT_LOG
    

Here, the [default rule](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#default-rules) has an [`evaluationMode`](https://docs.cloud.google.com/binary-authorization/docs/policy-yaml-reference#evaluationmode) of `ALWAYS_ALLOW`, which causes Binary Authorization to allow deployment of all container images. The default [`enforcementMode`](https://docs.cloud.google.com/binary-authorization/docs/policy-yaml-reference#enforcementmode) is set to `ENFORCED_BLOCK_AND_AUDIT_LOG`, but as all deployments are allowed, this action is never taken.

## Block (almost) all deployments

The following example shows how to block all container images from being deployed, while allowing Google-maintained system images. These container images are required for most Google Kubernetes Engine (GKE) clusters to start successfully.
    
    
    name: projects/example-project/policy
    globalPolicyEvaluationMode: ENABLE
    defaultAdmissionRule:
      evaluationMode: ALWAYS_DENY
      enforcementMode: ENFORCED_BLOCK_AND_AUDIT_LOG
    

Here, [globalPolicyEvaluationMode](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#google-maintained_system_images) is enabled so that images that are required by GKE are not blocked by policy enforcement. The [default rule](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#default-rules) has an [`evaluationMode`](https://docs.cloud.google.com/binary-authorization/docs/policy-yaml-reference#evaluationmode) of `ALWAYS_DENY`, which causes Binary Authorization to deny deployment of all container images. The [`enforcementMode`](https://docs.cloud.google.com/binary-authorization/docs/policy-yaml-reference#enforcementmode) is set to `ENFORCED_BLOCK_AND_AUDIT_LOG`, which causes Binary Authorization to block deployment and write to the [audit log](https://docs.cloud.google.com/binary-authorization/docs/viewing-audit-logs).

## Require attestors to sign before deployment

The following example shows how to require [attestors](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#attestors) to authorize a release before a container image can be deployed. The deployment is blocked if all attestors have not signed.
    
    
    name: projects/example-project/policy
    globalPolicyEvaluationMode: ENABLE
    defaultAdmissionRule:
      evaluationMode: REQUIRE_ATTESTATION
      enforcementMode: ENFORCED_BLOCK_AND_AUDIT_LOG
      requireAttestationsBy:
      - projects/example-project/attestors/secure-build
    

Here, the default rule has an `evaluationMode` of `REQUIRE_ATTESTATION`, which causes Binary Authorization to allow deployment of only those images which have been authorized by the required attestors in [`requireAttestationsBy`](https://docs.cloud.google.com/binary-authorization/docs/policy-yaml-reference#requireattestationsby).

## Allow deployments in dry run mode

Dry run mode is an enforcement mode in a policy that allows non-conformant images to be deployed, but writes details about the policy violation and deployment to the audit log. Dry run mode allows you to test a policy in your production environment before it goes into effect.

The following example shows how to allow all non-conformant images to be deployed in dry run mode.
    
    
    name: projects/example-project/policy
    globalPolicyEvaluationMode: ENABLE
    defaultAdmissionRule:
      evaluationMode: REQUIRE_ATTESTATION
      enforcementMode: DRYRUN_AUDIT_LOG_ONLY
      requireAttestationsBy:
      - projects/example-project/attestors/secure-build
    

Here, the default rule has an [`enforcementMode`](https://docs.cloud.google.com/binary-authorization/docs/policy-yaml-reference#enforcementmode) of `DRYRUN_AUDIT_LOG_ONLY`, which allows deployment of images that have not been authorized by the specified attestor to be deployed, but writes information about the non-conformant deployment to the audit log.

## Use a cluster-specific rule

The following examples shows a [cluster-specific rule](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#cluster-specific_rules) that only allows those container images to be deployed which have been authorized by the specified attestors:
    
    
    name: projects/example-project/policy
    globalPolicyEvaluationMode: ENABLE
    defaultAdmissionRule:
      evaluationMode: ALWAYS_DENY
      enforcementMode: ENFORCED_BLOCK_AND_AUDIT_LOG
    clusterAdmissionRules:
      us-east1-a.prod-cluster:
        evaluationMode: REQUIRE_ATTESTATION
        enforcementMode: ENFORCED_BLOCK_AND_AUDIT_LOG
        requireAttestationsBy:
        - projects/example-project/attestors/secure-build
        - projects/example-project/attestors/prod-qualified
    

Here, the cluster-specific rule only applies to those container images deployed to `us-east1-a.prod-cluster`. The rule requires attestation by two attestors before an image can be deployed.

## Add exempt images

The following example shows how to add additional paths in Container Registry or another registry to the list of images [exempt from the policy](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#exempt_images):
    
    
    name: projects/example-project/policy
    globalPolicyEvaluationMode: ENABLE
    admissionWhitelistPatterns:
    - namePattern: gcr.io/example-project-1/*
    - namePattern: gcr.io/example-project-2/my-app
    defaultAdmissionRule:
      evaluationMode: ALWAYS_DENY
      enforcementMode: ENFORCED_BLOCK_AND_AUDIT_LOG
    

Here, the matching patterns for additional exempt images are `gcr.io/example-project-1/*` and `gcr.io/example-project-2/my-app`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
