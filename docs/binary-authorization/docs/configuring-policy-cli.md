---
url: https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-cli/
title: Configure a policy using the gcloud CLI \u00a0|\u00a0 Binary Authorization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:11:40.541232+00:00
---

# Configure a policy using the gcloud CLI  |  Binary Authorization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-cli/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)
  * [ Guides ](https://docs.cloud.google.com/binary-authorization/docs/overview)



Send feedback 

#  Configure a policy using the gcloud CLI Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This document or section includes references to one or more terms that Google considers disrespectful or offensive. The terms are used because they are keywords in the software that's described in the document. 

The terms: `whitelist`

This page provides instructions for configuring a Binary Authorization [policy](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#policies) by using the Google Cloud CLI. As an alternative, you can also perform these tasks by using the [Google Cloud console](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-console) or the [REST API](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-rest). This step is part of [setting up Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/setting-up).

To configure a policy using the command-line tool, you export the existing policy as a YAML file. After you modify the file, you can import it to update the policy, as described later in this guide. For more information on the policy YAML format, see [Policy YAML Reference](https://docs.cloud.google.com/binary-authorization/docs/policy-yaml-reference).

**Note:** This page describes how to configure a policy for the container-based platforms that Binary Authorization supports, including Google Kubernetes Engine (GKE), Distributed Cloud, Cloud Run, and Cloud Service Mesh. Policy settings, such as rule type, rule parameters, and parameter format can vary depending on the platforms you use. Because of this, each section in this page notes the platforms the settings apply to. Make sure the settings you use are supported for your platforms.

## Before you begin

  1. [Enable Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/enabling).
  2. [Create a cluster](https://docs.cloud.google.com/binary-authorization/docs/creating-cluster).
  3. If you intend to use [attestations](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#attestations), we recommend that you create [attestors](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#attestors) before configuring the policy. You can create attestors using a [command-line tool](https://docs.cloud.google.com/binary-authorization/docs/creating-attestors-cli) or through the [Google Cloud console](https://docs.cloud.google.com/binary-authorization/docs/creating-attestors-console).
  4. Set the project ID to the project in which you enabled Binary Authorization:
         
         PROJECT_ID=PROJECT_ID
         gcloud config set project ${PROJECT_ID}
         




## Export the policy YAML file

This section applies to _**GKE, Distributed Cloud, Cloud Run, and Cloud Service Mesh**_.

To update the policy, first export it to a local YAML file, as follows:
    
    
    gcloud container binauthz policy export > /tmp/policy.yaml
    

By default, the file contents look similar to the following:
    
    
    defaultAdmissionRule:
      enforcementMode: ENFORCED_BLOCK_AND_AUDIT_LOG
      evaluationMode: ALWAYS_ALLOW
    globalPolicyEvaluationMode: ENABLE
    name: projects/PROJECT_ID/policy
    

To modify the policy, edit the file and add or update sections, as described later in this guide. After you save the file, you can import the policy.

To add an exempt image to the allowlist, add the following to the policy file: 
    
    
    admissionWhitelistPatterns:
      - namePattern: EXEMPT_IMAGE_PATH

Replace `EXEMPT_IMAGE_PATH` with the path to am image to exempt. To exempt additional images, add additional `- namePattern` entries. Learn more about [`admissionWhitelistPatterns`](https://docs.cloud.google.com/binary-authorization/docs/policy-yaml-reference#allowlistpatterns). 

## Set the default rule

This section applies to _**GKE, Distributed Cloud, Cloud Run, and Cloud Service Mesh**_.

A [rule](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#rules) is the part of a policy that defines constraints that container images must satisfy before they can be deployed. The [default rule](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#default-rules) defines constraints that apply to all [non-exempt](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#exempt_images) images that don't have their own cluster-specific rule. Every policy must have a default rule.

The default rule is defined in the [`defaultAdmissionRule`](https://docs.cloud.google.com/binary-authorization/docs/policy-yaml-reference#defaultadmissionrule) node in the policy YAML file. For more information on the parts of this rule, see [**_ADMISSION_RULE_**](https://docs.cloud.google.com/binary-authorization/docs/policy-yaml-reference#admission_rule) in the Policy YAML Reference. For examples of default rules, see [Example Policies](https://docs.cloud.google.com/binary-authorization/docs/example-policies).

To set the default rule, edit the `defaultAdmissionRule` node in the `policy.yaml` file as required:
    
    
    defaultAdmissionRule:
      evaluationMode: EVALUATION_MODE
      enforcementMode: ENFORCEMENT_MODE
      requireAttestationsBy:
      - ATTESTOR
      - ...
    

Replace the following:

  * EVALUATION_MODE: The [evaluation mode](https://docs.cloud.google.com/binary-authorization/docs/policy-yaml-reference#evaluationmode) specifies the type of constraint that the Binary Authorization enforcer enforces at deploy time. Replace EVALUATION_MODE with one of the following options:

    * `ALWAYS_ALLOW`: Allows all images to be deployed.
    * `ALWAYS_DENY`: Disallows all images from being deployed.
    * `REQUIRE_ATTESTATION`: Allows an image to be deployed if the image has one or more attestations that can be verified by all of the attestors that you add to this rule. At deploy time, the enforcer verifies the attestation using the attestors you add to the ATTESTOR list in this rule. To learn about creating attestors, see [Creating attestors](https://docs.cloud.google.com/binary-authorization/docs/creating-attestors-console). If you specify `REQUIRE_ATTESTATION`, you must also add a `requireAttestationsBy` block containing at least one attestor. To learn about creating attestors, see [Creating attestors](https://docs.cloud.google.com/binary-authorization/docs/creating-attestors-cli).
  * ENFORCEMENT_MODE: The [enforcement mode](https://docs.cloud.google.com/binary-authorization/docs/policy-yaml-reference#enforcementmode) specifies how the enforcer responds when an image violates a rule. Replace ENFORCEMENT_MODE with one of the following:

    * `ENFORCED_BLOCK_AND_AUDIT_LOG`: Block images that violate the rule and log information about the violation to Cloud Audit Logs (default).
    * `DRYRUN_AUDIT_LOG_ONLY`: Allow all images to deploy but log enforcement information, including information about violations, to Cloud Audit Logs.
  * ATTESTOR: If you set `EVALUATION_MODE` to `REQUIRE_ATTESTATION`, you must also add a [requireAttesationsBy](https://docs.cloud.google.com/binary-authorization/docs/policy-yaml-reference#requireattestationsby) block. In the block, you list one or more attestors, by resource ID. The resource ID has the format:

`projects/PROJECT_ID/attestors/ATTESTOR_NAME`.

To learn more about creating attestors, see [Creating attestors](https://docs.cloud.google.com/binary-authorization/docs/creating-attestors-cli).


**Note:** We don't recommend using the `ALWAYS_ALLOW` evaluation mode in the default rule. Doing so allows all images to deploy unless they fail to satisfy a cluster-specific or other specific rule in the policy.

## Manage exempt images

This section applies to _**GKE, Distributed Cloud, Cloud Run, and Cloud Service Mesh**_.

An [exempt image](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#exempt_images) is an image that is exempt from policy rules. Binary Authorization always allows exempt images to be deployed.

You specify exempt images by listing their registry paths in `admissionWhitelistPatterns`. The path refers to [Container Registry](https://docs.cloud.google.com/container-registry/docs) or another image registry. At deploy time, Binary Authorization exempts the list of images specified by `admissionWhitelistPatterns` after the images specified by the system policy.

To add an exempt image, add a `namePattern` node under an [`admissionWhitelistPatterns`](https://docs.cloud.google.com/binary-authorization/docs/policy-yaml-reference#allowlistpatterns) list in the `policy.yaml` file:
    
    
    admissionWhitelistPatterns:
    - namePattern: MATCHING_PATTERN
    

Replace MATCHING_PATTERN with the path to a single image in your registry by exact match, or to any images matching a pattern using the wildcard symbol (`*`, `**`).

### Cloud Run

This section applies to _**Cloud Run**_.

You cannot _directly_ specify image names that contain a tag. For example, you cannot specify `IMAGE_PATH`:latest.

If you want to specify image names that contain tags, you must specify the image name using a [wildcard](https://docs.cloud.google.com/binary-authorization/docs/policy-yaml-reference#admissionwhitelistpatterns) as follows:

  * `*` for all versions of a single image; for example, `us-docker.pkg.dev/myproject/container/hello@*`
  * `**` for all images in a project; for example, `us-docker.pkg.dev/myproject/**`



You can use path names to specify a digest in the format `IMAGE_PATH`@`DIGEST`.

### System policy evaluation mode

This section applies to _**GKE and Distributed Cloud**_.

[System policy evaluation mode](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#google-maintained_system_images) is a policy setting that causes Binary Authorization to evaluate a _system policy_ before evaluating the policy that you configure. Google manages the system policy, which exempts a list of Google-maintained system images that GKE uses. Images listed in the system policy are not blocked by policy enforcement. If you do not enable the setting, you must manage the list of exempt images yourself. Learn how to Manage exempt images.

You can view the contents of the system policy using the following command:
    
    
    gcloud alpha container binauthz policy export-system-policy
    

To enable system policy evaluation mode, add the following line to the `policy.yaml` file:
    
    
    globalPolicyEvaluationMode: ENABLE
    

To disable system policy evaluation mode, add the following:
    
    
    globalPolicyEvaluationMode: DISABLE
    

**Note:** For reliability reasons, the system policy is updated one region at a time. As a result, the system policy can differ between regions during an update.

You can export the system policy associated with a specific region as follows:
    
    
    gcloud alpha container binauthz policy export-system-policy \
      --location=REGION > /tmp/policy.yaml
    

Replace REGION with the region associated with the system policy that you want to export (or "global"). Examples include: `asia-east1`, `europe-west1`, `us-central1`.

If you omit `--location` or specify `--location=global`, the command outputs a system policy from a region in the last group of regions to receive updates. Since most changes to the system policy are additions, the output shows the set of system images that are currently allowed in all regions.

## Set cluster-specific rules (optional)

This section applies to _**GKE and Distributed Cloud**_.

A cluster can also have one or more [cluster-specific rules](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#cluster-specific_rules). This type of rule applies to images that are to be deployed to specific GKE clusters only. Cluster-specific rules are an optional part of a policy.

Cluster-specific rules are defined in [`clusterAdmissionRules`](https://docs.cloud.google.com/binary-authorization/docs/policy-yaml-reference#clusteradmissionrules) nodes in the policy YAML file. For more information on the parts of this rule, see [**_ADMISSION_RULE_**](https://docs.cloud.google.com/binary-authorization/docs/policy-yaml-reference#admission_rule) in the Policy YAML Reference. For an example, see [Use a cluster-specific rule](https://docs.cloud.google.com/binary-authorization/docs/example-policies#use_a_cluster-specific_rule) in [Example Policies](https://docs.cloud.google.com/binary-authorization/docs/example-policies).

To add a cluster-specific rule:

In the `policy.yaml` file, add a `clusterAdmissionRules` node:
    
    
    clusterAdmissionRules:
      CLUSTER_SPECIFIER:
        evaluationMode: EVALUATION_MODE
        enforcementMode: ENFORCEMENT_MODE
        requireAttestationsBy:
        - ATTESTOR
        - ...
    

Replace the following:

  * CLUSTER_SPECIFIER: the resource ID of the cluster to which the rule applies. You format the rule as follows:

    * For GKE, GKE attached clusters, and GKE on AWS, the format is `CLUSTER_LOCATION.CLUSTER_NAME`—for example, `us-central1-a.test-cluster`.

    * For Google Distributed Cloud software (GKE clusters on bare metal or VMware), the format is, `FLEET_MEMBERSHIP_LOCATION.FLEET_MEMBERSHIP_ID`—for example, `global.test-membership`.

Other properties are as described in Set the default rule earlier in this guide. For an example of a cluster-specific rule, see [Example Policies](https://docs.cloud.google.com/binary-authorization/docs/example-policies#use_a_cluster-specific_rule).

  * EVALUATION_MODE: The [evaluation mode](https://docs.cloud.google.com/binary-authorization/docs/policy-yaml-reference#evaluationmode) specifies the type of constraint that the Binary Authorization enforcer enforces at deploy time. Replace EVALUATION_MODE with one of the following options:

    * `ALWAYS_ALLOW`: Allows all images to be deployed.
    * `ALWAYS_DENY`: Disallows all images from being deployed.
    * `REQUIRE_ATTESTATION`: Allows an image to be deployed if the image has one or more attestations that can be verified by all of the attestors that you add to this rule. At deploy time, the enforcer verifies the attestation using the attestors you add to the ATTESTOR list in this rule. To learn about creating attestors, see [Creating attestors](https://docs.cloud.google.com/binary-authorization/docs/creating-attestors-console). If you specify `REQUIRE_ATTESTATION`, you must also add a `requireAttestationsBy` block containing at least one attestor. To learn about creating attestors, see [Creating attestors](https://docs.cloud.google.com/binary-authorization/docs/creating-attestors-cli).
  * ENFORCEMENT_MODE: The [enforcement mode](https://docs.cloud.google.com/binary-authorization/docs/policy-yaml-reference#enforcementmode) specifies how the enforcer responds when an image violates a rule. Replace ENFORCEMENT_MODE with one of the following:

    * `ENFORCED_BLOCK_AND_AUDIT_LOG`: Block images that violate the rule and log information about the violation to Cloud Audit Logs (default).
    * `DRYRUN_AUDIT_LOG_ONLY`: Allow all images to deploy but log enforcement information, including information about violations, to Cloud Audit Logs.
  * ATTESTOR: If you set `EVALUATION_MODE` to `REQUIRE_ATTESTATION`, you must also add a [requireAttesationsBy](https://docs.cloud.google.com/binary-authorization/docs/policy-yaml-reference#requireattestationsby) block. In the block, you list one or more attestors, by resource ID. The resource ID has the format:

`projects/PROJECT_ID/attestors/ATTESTOR_NAME`.

To learn more about creating attestors, see [Creating attestors](https://docs.cloud.google.com/binary-authorization/docs/creating-attestors-cli).




## Set specific rules (optional)

You can create rules that are scoped to either a mesh service identity, a Kubernetes service account, or a Kubernetes namespace.

### Set a rule for a Cloud Service Mesh service identity

To set a rule for a Cloud Service Mesh service identity, edit your `policy.yaml` file and add an `istioServiceIdentityAdmissionRules` block, for example:
    
    
    defaultAdmissionRule:
      enforcementMode: ENFORCED_BLOCK_AND_AUDIT_LOG
      evaluationMode: ALWAYS_DENY
    globalPolicyEvaluationMode: ENABLE
    istioServiceIdentityAdmissionRules:
      SERVICE_IDENTITY_ID:
        enforcementMode: ENFORCED_BLOCK_AND_AUDIT_LOG
        evaluationMode: ENFORCEMENT_MODE
        requireAttestationsBy:
        - <var>ATTESTOR</var>
        - ...
    
    name: projects/PROJECT_ID/policy
    

Replace the following:

  * SERVICE_IDENTITY_ID: the Cloud Service Mesh service identity to scope this rule to. The service identity has the following format: PROJECT_ID.svc.id.goog/ns/NAMESPACE/sa/SERVICE_ACCOUNT. In the service identity ID, replace the following:

    * PROJECT_ID: the project ID in which you define your Kubernetes resources.
    * NAMESPACE: the Kubernetes namespace.
    * SERVICE_ACCOUNT: the service account.
  * EVALUATION_MODE: The [evaluation mode](https://docs.cloud.google.com/binary-authorization/docs/policy-yaml-reference#evaluationmode) specifies the type of constraint that the Binary Authorization enforcer enforces at deploy time. Replace EVALUATION_MODE with one of the following options:

    * `ALWAYS_ALLOW`: Allows all images to be deployed.
    * `ALWAYS_DENY`: Disallows all images from being deployed.
    * `REQUIRE_ATTESTATION`: Allows an image to be deployed if the image has one or more attestations that can be verified by all of the attestors that you add to this rule. At deploy time, the enforcer verifies the attestation using the attestors you add to the ATTESTOR list in this rule. To learn about creating attestors, see [Creating attestors](https://docs.cloud.google.com/binary-authorization/docs/creating-attestors-console). If you specify `REQUIRE_ATTESTATION`, you must also add a `requireAttestationsBy` block containing at least one attestor. To learn about creating attestors, see [Creating attestors](https://docs.cloud.google.com/binary-authorization/docs/creating-attestors-cli).
  * ENFORCEMENT_MODE: The [enforcement mode](https://docs.cloud.google.com/binary-authorization/docs/policy-yaml-reference#enforcementmode) specifies how the enforcer responds when an image violates a rule. Replace ENFORCEMENT_MODE with one of the following:

    * `ENFORCED_BLOCK_AND_AUDIT_LOG`: Block images that violate the rule and log information about the violation to Cloud Audit Logs (default).
    * `DRYRUN_AUDIT_LOG_ONLY`: Allow all images to deploy but log enforcement information, including information about violations, to Cloud Audit Logs.
  * ATTESTOR: If you set `EVALUATION_MODE` to `REQUIRE_ATTESTATION`, you must also add a [requireAttesationsBy](https://docs.cloud.google.com/binary-authorization/docs/policy-yaml-reference#requireattestationsby) block. In the block, you list one or more attestors, by resource ID. The resource ID has the format:

`projects/PROJECT_ID/attestors/ATTESTOR_NAME`.

To learn more about creating attestors, see [Creating attestors](https://docs.cloud.google.com/binary-authorization/docs/creating-attestors-cli).




### Set a rule for a Kubernetes service account

To set a rule for a Kubernetes service account, edit your `policy.yaml` file and add a `kubernetesServiceAccountAdmissionRules` block, for example:
    
    
    defaultAdmissionRule:
      enforcementMode: ENFORCED_BLOCK_AND_AUDIT_LOG
      evaluationMode: ALWAYS_DENY
    globalPolicyEvaluationMode: ENABLE
    kubernetesServiceAccountAdmissionRules:
      KUBERNETES_SERVICE_ACCOUNT_ID:
        enforcementMode: ENFORCED_BLOCK_AND_AUDIT_LOG
        evaluationMode: ENFORCEMENT_MODE
        requireAttestationsBy:
        - <var>ATTESTOR</var>
        - ...
    name: projects/PROJECT_ID/policy
    

Replace the following:

  * KUBERNETES_SERVICE_ACCOUNT_ID: The Kubernetes service account to scope the rule to. This service account ID has the format: NAMESPACE:SERVICE_ACCOUNT. In the service account ID, replace the following:

    * NAMESPACE: the Kubernetes namespace.
    * SERVICE_ACCOUNT: the service account name.
  * EVALUATION_MODE: The [evaluation mode](https://docs.cloud.google.com/binary-authorization/docs/policy-yaml-reference#evaluationmode) specifies the type of constraint that the Binary Authorization enforcer enforces at deploy time. Replace EVALUATION_MODE with one of the following options:

    * `ALWAYS_ALLOW`: Allows all images to be deployed.
    * `ALWAYS_DENY`: Disallows all images from being deployed.
    * `REQUIRE_ATTESTATION`: Allows an image to be deployed if the image has one or more attestations that can be verified by all of the attestors that you add to this rule. At deploy time, the enforcer verifies the attestation using the attestors you add to the ATTESTOR list in this rule. To learn about creating attestors, see [Creating attestors](https://docs.cloud.google.com/binary-authorization/docs/creating-attestors-console). If you specify `REQUIRE_ATTESTATION`, you must also add a `requireAttestationsBy` block containing at least one attestor. To learn about creating attestors, see [Creating attestors](https://docs.cloud.google.com/binary-authorization/docs/creating-attestors-cli).
  * ENFORCEMENT_MODE: The [enforcement mode](https://docs.cloud.google.com/binary-authorization/docs/policy-yaml-reference#enforcementmode) specifies how the enforcer responds when an image violates a rule. Replace ENFORCEMENT_MODE with one of the following:

    * `ENFORCED_BLOCK_AND_AUDIT_LOG`: Block images that violate the rule and log information about the violation to Cloud Audit Logs (default).
    * `DRYRUN_AUDIT_LOG_ONLY`: Allow all images to deploy but log enforcement information, including information about violations, to Cloud Audit Logs.
  * ATTESTOR: If you set `EVALUATION_MODE` to `REQUIRE_ATTESTATION`, you must also add a [requireAttesationsBy](https://docs.cloud.google.com/binary-authorization/docs/policy-yaml-reference#requireattestationsby) block. In the block, you list one or more attestors, by resource ID. The resource ID has the format:

`projects/PROJECT_ID/attestors/ATTESTOR_NAME`.

To learn more about creating attestors, see [Creating attestors](https://docs.cloud.google.com/binary-authorization/docs/creating-attestors-cli).




### Set a rule for a Kubernetes namespace

To set a rule for a Kubernetes namespace, edit your `policy.yaml` file and add a `kubernetesNamespaceAdmissionRules` block, for example:
    
    
    defaultAdmissionRule:
      enforcementMode: ENFORCED_BLOCK_AND_AUDIT_LOG
      evaluationMode: ALWAYS_DENY
    globalPolicyEvaluationMode: ENABLE
    kubernetesNamespaceAdmissionRules:
      KUBERNETES_NAMESPACE:
        enforcementMode: ENFORCED_BLOCK_AND_AUDIT_LOG
        evaluationMode: EVALUATION_MODE
        requireAttestationsBy:
        - <var>ATTESTOR</var>
        - ...
    name: projects/PROJECT_ID/policy
    

Replace the following:

  * KUBERNETES_NAMESPACE: The Kubernetes namespace to scope this rule to.

  * EVALUATION_MODE: The [evaluation mode](https://docs.cloud.google.com/binary-authorization/docs/policy-yaml-reference#evaluationmode) specifies the type of constraint that the Binary Authorization enforcer enforces at deploy time. Replace EVALUATION_MODE with one of the following options:

    * `ALWAYS_ALLOW`: Allows all images to be deployed.
    * `ALWAYS_DENY`: Disallows all images from being deployed.
    * `REQUIRE_ATTESTATION`: Allows an image to be deployed if the image has one or more attestations that can be verified by all of the attestors that you add to this rule. At deploy time, the enforcer verifies the attestation using the attestors you add to the ATTESTOR list in this rule. To learn about creating attestors, see [Creating attestors](https://docs.cloud.google.com/binary-authorization/docs/creating-attestors-console). If you specify `REQUIRE_ATTESTATION`, you must also add a `requireAttestationsBy` block containing at least one attestor. To learn about creating attestors, see [Creating attestors](https://docs.cloud.google.com/binary-authorization/docs/creating-attestors-cli).
  * ENFORCEMENT_MODE: The [enforcement mode](https://docs.cloud.google.com/binary-authorization/docs/policy-yaml-reference#enforcementmode) specifies how the enforcer responds when an image violates a rule. Replace ENFORCEMENT_MODE with one of the following:

    * `ENFORCED_BLOCK_AND_AUDIT_LOG`: Block images that violate the rule and log information about the violation to Cloud Audit Logs (default).
    * `DRYRUN_AUDIT_LOG_ONLY`: Allow all images to deploy but log enforcement information, including information about violations, to Cloud Audit Logs.
  * ATTESTOR: If you set `EVALUATION_MODE` to `REQUIRE_ATTESTATION`, you must also add a [requireAttesationsBy](https://docs.cloud.google.com/binary-authorization/docs/policy-yaml-reference#requireattestationsby) block. In the block, you list one or more attestors, by resource ID. The resource ID has the format:

`projects/PROJECT_ID/attestors/ATTESTOR_NAME`.

To learn more about creating attestors, see [Creating attestors](https://docs.cloud.google.com/binary-authorization/docs/creating-attestors-cli).




## Import the policy YAML file

This section applies to _**GKE, Distributed Cloud, Cloud Run, and Cloud Service Mesh**_.

Import the policy YAML file back into Binary Authorization by entering the following:
    
    
    gcloud container binauthz policy import /tmp/policy.yaml
    

**Note:** It can take a few minutes for the policy to take effect.

## What's next

  * Use the `built-by-cloud-build` attestor to [deploy only images built by Cloud Build](https://docs.cloud.google.com/binary-authorization/docs/deploy-cloud-build).
  * [Use attestations](https://docs.cloud.google.com/binary-authorization/docs/attestations).
  * [Deploy a GKE image](https://docs.cloud.google.com/binary-authorization/docs/deploying-containers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
