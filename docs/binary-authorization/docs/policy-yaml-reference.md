---
url: https://docs.cloud.google.com/binary-authorization/docs/policy-yaml-reference/
title: Policy YAML reference \u00a0|\u00a0 Binary Authorization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:15:16.457187+00:00
---

# Policy YAML reference  |  Binary Authorization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/docs/policy-yaml-reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)
  * [ Reference ](https://docs.cloud.google.com/binary-authorization/docs/api)



Send feedback 

#  Policy YAML reference Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This document or section includes references to one or more terms that Google considers disrespectful or offensive. The terms are used because they are keywords in the software that's described in the document. 

The terms: `whitelist`

This page contains reference information for Binary Authorization [policies](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#policies) as specified in [YAML](http://yaml.org) format. When you configure a policy using the [command-line interface](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-cli), you edit a YAML-formatted file that complies with this specification. For examples of policies in YAML format, see [Example Policies](https://docs.cloud.google.com/binary-authorization/docs/example-policies).

Policy YAML files have the following format:
    
    
    name: projects/<PROJECT_ID>/policy
    admissionWhitelistPatterns:
    - namePattern: <MATCHING_PATTERN>
    - ...
    globalPolicyEvaluationMode: <GLOBAL_EVAL_MODE>
    defaultAdmissionRule:
      <ADMISSION_RULE>
    clusterAdmissionRules:
      <CLUSTER_SPECIFIER>:
        <ADMISSION_RULE>
      ...
    

## Nodes

The YAML format has the following top-level nodes:

Node | Description | Required  
---|---|---  
`name` | Name of the policy. | Yes  
`admissionWhitelistPatterns` | Specifies container images that are always allowed to be deployed. | No  
`globalPolicyEvaluationMode` | Specifies whether to apply a system policy that exempts Google-owned system images. | No  
`defaultAdmissionRule` | The rule to use when no specific rule applies. | Yes  
`clusterAdmissionRules` | Specifies rules that apply to specific clusters. | No  
  
### `name`

The `name` node contains the name of the policy in the following format:
    
    
    name: projects/PROJECT_ID/policy
    

where PROJECT_ID is the name of your Google Cloud project where your policy is defined.

For example:
    
    
    name: projects/example-project/policy
    

### `admissionWhitelistPatterns`

**Note:** We don't recommend using `admissionWhitelistPatterns` to allowlist Google-managed system images. Google-managed system images are allowed if `globalPolicyEvaluationMode` is set to `ENABLE` (the default setting). See `globalPolicyEvaluationMode` for details.

`admissionWhitelistPatterns` specifies an allowlist of container images that are [exempt from policy enforcement](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#exempt_images). You specify the path to the images in Container Registry and Artifact Registry, another registry, or a local reference in the `namePattern` subnode:
    
    
    admissionWhitelistPatterns:
      - namePattern: MATCHING_PATTERN
      - ...
    

Replace MATCHING_PATTERN with either a path to a single image or a matching pattern containing one of the wildcard symbols (`*`, `**`).

Note that wildcards are valid only at the end of the pattern. For example, `gcr.io/my-project/nginx*` is a valid pattern, but `gcr.io/my-project/n*x` isn't. The `*` wildcard only matches images in the specified directory. For example, `gcr.io/my-project/nginx*` matches `gcr.io/my-project/nginx:latest`, but not `gcr.io/my-project/nginx-images/nginx`. The `**` wildcard matches images in subdirectories. For example, the path `gcr.io/my-project/nginx**` matches `gcr.io/my-project/nginx-1.14.2/image:latest`.

**Caution:** Be careful when using the `**` wildcard with project IDs as doing so also matches images in different projects. For example, the path `gcr.io/my-project**`, allows images in both `gcr.io/my-project/nginx` and `gcr.io/my-project-exploit/nginx-exploit` to be deployed.

The following example adds registries containing commonly used Google Kubernetes Engine (GKE) images, an image located at `gcr.io/example-project/helloworld`, and a local reference to an image, to the list of exempt images for the policy:
    
    
    admissionWhitelistPatterns:
      - namePattern: gcr.io/google-containers/*
      - namePattern: k8s.gcr.io/**
      - namePattern: gke.gcr.io/**
      - namePattern: gcr.io/gke-release/asm/*
      - namePattern: gcr.io/stackdriver-agents/*
      - namePattern: gcr.io/example-project/helloworld
      - namePattern: loc-ref
    

**Note:** This example includes images GKE requires to start a cluster. You must include them if `globalPolicyEvaluationMode` is disabled.

#### Allowlist patterns

**Note:** The same rules apply for local references to images.

To allowlist all container images whose registry location matches the specified path:
    
    
    admissionWhitelistPatterns:
      ...
      - namePattern: gcr.io/example-project/*
    

To allowlist a specific image:
    
    
    admissionWhitelistPatterns:
      ...
      - namePattern: gcr.io/example-project/helloworld
    

To allowlist a currently-tagged version:
    
    
    admissionWhitelistPatterns:
      ...
      - namePattern: gcr.io/example-project/helloworld:latest
      - namePattern: gcr.io/example-project/helloworld:my-tag
      - namePattern: gcr.io/example-project/helloworld:v1.*
    

To allowlist a specific version of an image by its digest:
    
    
    admissionWhitelistPatterns:
      ...
      - namePattern: gcr.io/example-project/helloworld@sha256:77b0b75136b9bd0fd36fb50f4c92ae0dbdbbe164ab67885e736fa4374e0cbb8c
    

To allowlist images in subdirectories of a given path:
    
    
    admissionWhitelistPatterns:
      ...
      - namePattern: gcr.io/example-project/**
    

### `globalPolicyEvaluationMode`

[System policy evaluation mode](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#google-maintained_system_images) is a policy setting that causes Binary Authorization to evaluate a system policy before evaluating the policy that you configure. The system policy is provided by Google and exempts a list of Google-maintained system images from further policy evaluation. When you have this setting enabled, images that are required by GKE are not blocked by policy enforcement. The system policy is evaluated prior to and in addition to user policy evaluation, including `admissionWhitelistPatterns`.

To allow all Google-maintained system images, set the `globalPolicyEvaluationMode` property to `ENABLE`:
    
    
    globalPolicyEvaluationMode: ENABLE
    

To disable system policy evaluation mode:
    
    
    globalPolicyEvaluationMode: DISABLE
    

**Note:** It is recommended that you leave `globalPolicyEvaluationMode` on its default setting, `ENABLE`. For GKE to work properly, it needs to run a number of system images in your cluster. When you enable `globalPolicyEvaluationMode`, the Google-maintained allowlist of system images is automatically updated with every GKE release. While you can manage system images yourself by listing them in `admissionWhitelistPatterns`, updated system images might not be allowed to run if the allowlist is not kept up to date.**Note:** If you _disable_ `globalPolicyEvaluationMode`, the paths `gcr.io/google-containers/*`, `k8s.gcr.io/**`, `gke.gcr.io/*`, `gcr.io/gke-release/someproject/*`, and `gcr.io/stackdriver-agents/*` must be included in the `admissionWhitelistPatterns` allowlist, as they contain Google Cloud resources required by GKE to start a cluster successfully. Additional image paths might be required in the future. Those paths would also need to be included in the `admissionWhitelistPatterns` allowlist for GKE clusters to run as expected.

### `defaultAdmissionRule`

`defaultAdmissionRule` specifies the [default rule](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#default-rules) for the policy. The default rule defines the constraints that apply to all non-exempt container images with the exception of those that have their own cluster-specific rule. You specify the default rule using the ADMISSION_RULE collection:
    
    
    defaultAdmissionRule:
      ADMISSION_RULE
    

The following example shows a default rule that allows only those container images to be deployed which have been authorized by the specified [attestor](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#attestors). In the case that all required attestors have not authorized the image, Binary Authorization blocks the deployment and writes to the audit log.
    
    
    defaultAdmissionRule:
      evaluationMode: REQUIRE_ATTESTATION
      enforcementMode: ENFORCED_BLOCK_AND_AUDIT_LOG
      requireAttestationsBy:
      - projects/example-project/attestors/secure-build
    

### `clusterAdmissionRules`

`clusterAdmissionRules` declare [cluster-specific rules](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#cluster-specific_rules) for the policy. The constraints in these rules apply only to the specified cluster. If Binary Authorization applies a cluster-specific rule to a deployment, the default rule is not considered. As with default rules, you specify cluster-specific rules using the ADMISSION_RULE collection:
    
    
    clusterAdmissionRules:
      CLUSTER_SPECIFIER:
        ADMISSION_RULE
    

where CLUSTER_SPECIFIER is the resource ID of the cluster to which the rule applies in the format `location.name` (for example, `us-east1-a.prod-cluster`).

The following examples shows a cluster-specific rule that only allows those container images to be deployed which have been authorized by the specified attestors:
    
    
    clusterAdmissionRules:
      us-east1-a.prod-cluster:
        evaluationMode: REQUIRE_ATTESTATION
        enforcementMode: ENFORCED_BLOCK_AND_AUDIT_LOG
        requireAttestationsBy:
        - projects/example-project/attestors/secure-build
        - projects/example-project/attestors/prod-qualified
    

## Node collections

### `ADMISSION_RULE`

`ADMISSION_RULE` is a collection of nodes that specify the constraints for the rule in the following format:
    
    
    evaluationMode: EVAL_MODE
    enforcementMode: ENFORCEMENT_MODE
    requireAttestationsBy:
    - ATTESTOR
    - ...
    

Both `defaultAdmissionRule` and `clusterAdmissionRule` reference this collection.

#### `evaluationMode`

`evaluationMode` specifies the operation that Binary Authorization performs in order to evaluate whether to deploy a container image. The possible values are:

  * `ALWAYS_ALLOW`: Always allow deployment of images evaluated by this rule
  * `ALWAYS_DENY`: Always deny deployment of images evaluated by this rule
  * `REQUIRE_ATTESTATION`: Require one or more attestors to authorize the release before deployment



If the `evaluationMode` is `REQUIRE_ATTESTATION`, you must provide a reference to the required attestors in `requireAttestationsBy`.

#### `enforcementMode`

`enforcementMode` specifies the action that Binary Authorization takes if a container image does not conform to the constraints defined in the rule. The possible values are:

  * `ENFORCED_BLOCK_AND_AUDIT_LOG`: Blocks deployment and writes to the audit log.
  * `DRYRUN_AUDIT_LOG_ONLY`: Allows deployment of non-conformant images and writes details about the violation to the audit log.



Most production rules use the `ENFORCED_BLOCK_AND_AUDIT_LOG` enforcement mode. `DRYRUN_AUDIT_LOG_ONLY` is primarily used for testing a policy in your environment before it goes into effect.

#### `requireAttestationsBy`

`requireAttestationsBy` specifies one or more attestors who must authorize the release before a container image can be deployed. This is required for `REQUIRE_ATTESTATION` rules only. The format for this node is:
    
    
    requireAttestationsBy:
      - projects/PROJECT_ID/attestors/ATTESTOR_NAME
      - ...
    

where PROJECT_ID is the name of the project where your attestors are defined and ATTESTOR_NAME is the name of an attestor who is required to sign the release.

The following example shows how to specify attestors:
    
    
    requireAttestationsBy:
    - projects/example-project/attestors/secure-build
    - projects/example-project/attestors/prod-qualified
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
