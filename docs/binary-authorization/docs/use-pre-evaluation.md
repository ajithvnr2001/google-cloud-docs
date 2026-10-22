---
url: https://docs.cloud.google.com/binary-authorization/docs/use-pre-evaluation/
title: Use the policy evaluation service \u00a0|\u00a0 Binary Authorization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:02.811532+00:00
---

# Use the policy evaluation service  |  Binary Authorization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/docs/use-pre-evaluation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)
  * [ Guides ](https://docs.cloud.google.com/binary-authorization/docs/overview)



Send feedback 

#  Use the policy evaluation service Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page shows you how to use the policy evaluation service Google Cloud CLI command to rapidly evaluate whether an image or Kubernetes resource conforms to a continuous validation check-based platform policy.

## Overview

The policy evaluation service is a feature of Binary Authorization that you can use with [continuous validation (CV)](https://docs.cloud.google.com/binary-authorization/docs/overview-cv) check-based platform policies. The policy evaluation service evaluates on demand whether a container image that you specify conforms to a CV platform policy. The policy evaluation service is available as a gcloud CLI command and the [projects.platforms.gke.policies.evaluate](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.platforms.gke.policies/evaluate) method.

CV checks for policy violations at least once every 24 hours. As a result, it can take up to 24 hours for CV events to appear in Logging after CV is enabled or a Kubernetes resource is deployed. Additionally, CV produces log entries when it detects a policy violation. CV doesn't produce log entries when Kubernetes resources conform to the policy.

The policy evaluation service outputs a verdict that indicates whether the image is conformant with the policy or whether the image violates the policy.

By using the policy evaluation service, you can rapidly determine whether your image conforms to a policy.

When you use the service, you specify the image URL, either directly or within a Kubernetes resource, and you also specify the name of the GKE CV check-based policy.

In this way, the policy evaluation service service can help you to develop policies and debug non-conformant Kubernetes resources before you use CV.

This feature supports only GKE CV check-based policies.

Images must also specify an image digest in the form `IMAGE_URL@IMAGE_DIGEST`, except in the following cases:

  * Trusted directory check: The check passes if the image is located in a directory that you specify.
  * Exempt image allowlists: All other checks require an image digest in the form `IMAGE_URL@IMAGE_DIGEST`.



## Before you begin

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  3. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

**Note:** You can run the gcloud CLI in the Google Cloud console without installing the Google Cloud CLI. To run the gcloud CLI in the Google Cloud console, [use Cloud Shell](https://console.cloud.google.com/?cloudshell=true). **Note:** If you haven't created a project, your current project appears as `None` in the command output. After you finish authenticating, [create a new project](https://console.cloud.google.com/project), and then set it as your default project by running the following command: 
         
         gcloud config set project PROJECT_ID




### Required roles

To get the permissions that you need to use the policy evaluation service, ask your administrator to grant you the [Policy Evaluator ](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.policyEvaluator) (`roles/binaryauthorization.policyEvaluator`) IAM role on the policy project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

If your policy uses certain checks, you might need to ask your administrator to grant the following check-specific required roles:

  * [Simple signing attestation check required roles](https://docs.cloud.google.com/binary-authorization/docs/cv-attestation-check#required-roles)
  * [Vulnerability check required roles](https://docs.cloud.google.com/binary-authorization/docs/cv-vulnerability-check#required-roles)
  * [Freshness check required roles](https://docs.cloud.google.com/binary-authorization/docs/cv-freshness-check#required-roles)



## Evaluate check-based platform policies

The policy evaluation service can evaluate a single image URL or an image that is specified in a JSON-formatted or YAML-formatted Kubernetes resource.

### Evaluate check-based platform policies with a Kubernetes resource

To evaluate a policy with a Kubernetes resource using the gcloud CLI, run the following command:

Before using any of the command data below, make the following replacements: 

  * `POLICY_ID`: The ID of the platform policy. If the policy is in another project, you can use the full resource name: `projects/POLICY_PROJECT_ID/platforms/gke/policies/POLICY_ID`.
  * `POD_SPECIFICATION_PATH`: The path of your Pod specification.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud beta container binauthz policy evaluate POLICY_ID \
        --resource=POD_SPECIFICATION_PATH

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud beta container binauthz policy evaluate POLICY_ID `
        --resource=POD_SPECIFICATION_PATH

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud beta container binauthz policy evaluate POLICY_ID ^
        --resource=POD_SPECIFICATION_PATH

To evaluate a policy that specifies the platform, which must be set to `gke`, run the following command:

Before using any of the command data below, make the following replacements: 

  * `POLICY_ID`: The ID of the platform policy. If the policy is in another project, you can use the full resource name: `projects/POLICY_PROJECT_ID/platforms/gke/policies/POLICY_ID`.
  * `POD_SPECIFICATION_PATH`: The path of your Pod specification.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud beta container binauthz policy evaluate POLICY_ID \
        --platform=gke \
        --resource=POD_SPECIFICATION_PATH

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud beta container binauthz policy evaluate POLICY_ID `
        --platform=gke `
        --resource=POD_SPECIFICATION_PATH

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud beta container binauthz policy evaluate POLICY_ID ^
        --platform=gke ^
        --resource=POD_SPECIFICATION_PATH

### Evaluate check-based platform policies with an image URL

To evaluate a policy using an image URL, run the following command:

Before using any of the command data below, make the following replacements: 

  * `POLICY_ID`: The ID of the platform policy. If the policy is in another project, you can use the full resource name: `projects/POLICY_PROJECT_ID/platforms/gke/policies/POLICY_ID`.
  * `IMAGE_URL`: The path of your Pod specification.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud beta container binauthz policy evaluate POLICY_ID \
        --image=IMAGE_URL

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud beta container binauthz policy evaluate POLICY_ID `
        --image=IMAGE_URL

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud beta container binauthz policy evaluate POLICY_ID ^
        --image=IMAGE_URL

When you use the `--image` flag, the namespace and service account are implicitly assumed to be empty. If the policy that you're evaluating uses checksets that are scoped to `kubernetesNamespace` or `kubernetesServiceAccount`, the returned results might not be accurate.

## Review command output

The command output contains a top-level verdict that indicates the Pod's conformance state. The following conformance states can be returned:

  * `CONFORMANT`: The Kubernetes resource conforms to the platform policy.
  * `NON_CONFORMANT`: The Kubernetes resource doesn't conform to the platform policy.
  * `ERROR`: The evaluation ended in an error.



The response also contains nested results containing detailed information about the conformance state of all of the checks that were evaluated for each image contained in the Kubernetes resource.

Each `ImageResults` block contains a human-readable `explanation` field that describes why the image would be allowed or disallowed.

To facilitate scripting, the command returns a non-zero exit code when the Pod specification doesn't conform with the policy or the evaluation fails.

The following output examples demonstrate two cases. In the first case, the Kubernetes resource conforms to the policy. In the second case, the resource doesn't conform to the policy.

### View a conformant result

This section describes the output of a policy evaluation service check in which the Pod conforms with the platform policy.
    
    
    results:
    - imageResults:
      - checkSetResult:
          checkResults:
            results:
            - displayName: My trusted directory check
              evaluationResult:
                verdict: CONFORMANT
              explanation: Image is in a trusted directory
              type: TrustedDirectoryCheck
          displayName: Default check set
          scope: {}
        imageUri: us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0
        verdict: CONFORMANT
      kubernetesNamespace: default
      kubernetesServiceAccount: default
      podName: my-pod
      verdict: CONFORMANT
    verdict: CONFORMANT
    

In the output, a verdict of `CONFORMANT` is returned for the following types of evaluation:

  * Check: The image is conformant for the individual check—in this case, the trusted directory check.
  * CheckSet: The image is conformant for each of the checks in the CheckSet.
  * Policy: The image is conformant with the policy.



Because the image is conformant with the policy, the command returns an exit code of zero.

### View a non-conformant result

This section describes the output of a policy evaluation service check in which the Pod doesn't conform with the platform policy.
    
    
    results:
    - imageResults:
      - checkSetResult:
          checkResults:
            results:
            - displayName: My trusted directory check
              evaluationResult:
                verdict: NON_CONFORMANT
              explanation: Image isn't in a trusted directory
              type: TrustedDirectoryCheck
          displayName: Default check set
          scope: {}
        imageUri: us-docker.pkg.dev/untrusted-directory/containers/gke/hello-app:1.0
        verdict: NON_CONFORMANT
      kubernetesNamespace: default
      kubernetesServiceAccount: default
      podName: my-pod
      verdict: NON_CONFORMANT
    verdict: NON_CONFORMANT
    

In the output, because the image isn't conformant with the individual check, in this case the trusted directory check, and therefore the set of all checks, the top-level verdict is `NON_CONFORMANT`, and the command returns a non-zero exit code.

## Test the policy evaluation service

This section describes how you can test the policy evaluation service. You create a check-based platform policy that contains the trusted directory check. In the first test, you can then evaluate a Pod specification that conforms to the policy. In the second test, you evaluate a Pod specification that doesn't conform to the policy.

To create a policy that contains a trusted directory check, run the following commands:

  1. Create a platform policy file:
         
         cat << EOF > my-policy.yaml
         gkePolicy:
           checkSets:
           - checks:
             - displayName: "My trusted directory check"
               trustedDirectoryCheck:
                 trustedDirPatterns:
                 - "us-docker.pkg.dev/google-samples/containers/gke/"
             displayName: "My default check set"
         EOF
         

  2. Create the policy:

Before using any of the command data below, make the following replacements: 

     * POLICY_ID: A platform policy ID of your choice. If the policy is in another project, you can use the full resource name: `projects/POLICY_PROJECT_ID/platforms/gke/policies/POLICY_ID`.
     * POLICY_PATH: A path to the policy file.
     * POLICY_PROJECT_ID: The policy project ID.

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud beta container binauthz policy create POLICY_ID \
        --platform=gke \
        --policy-file=POLICY_PATH \
        --project=POLICY_PROJECT_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud beta container binauthz policy create POLICY_ID `
        --platform=gke `
        --policy-file=POLICY_PATH `
        --project=POLICY_PROJECT_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud beta container binauthz policy create POLICY_ID ^
        --platform=gke ^
        --policy-file=POLICY_PATH ^
        --project=POLICY_PROJECT_ID
    
    gcloud beta container binauthz policy create POLICY_ID \
    --platform=gke \
    --policy-file=my-policy.yaml
    




### Evaluate a conformant image

In this section, you evaluate a Pod specification that conforms to the policy that you created earlier in this guide. The evaluation produces a verdict indicating that the Pod specification is `CONFORMANT`, because the Pod specification references an image that resides in the directory that is specified in `trustedDirPatterns` in the trusted directory check.

  1. Create the Pod specification:
         
         cat << EOF > my-conforming-pod.json
         {
           "apiVersion": "v1",
           "kind": "Pod",
           "metadata": {
             "name": ""
           },
           "spec": {
             "containers": [
               {
                 "image": "us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0"
               }
               ]
           }
         }
         EOF
         

  2. Use the policy evaluation service by running the following command:

Before using any of the command data below, make the following replacements: 

     * `POLICY_ID`: The ID of the platform policy. If the policy is in another project, you can use the full resource name: `projects/POLICY_PROJECT_ID/platforms/gke/policies/POLICY_ID`.
     * `my-conforming-pod.json`: The path of your Pod specification.

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud beta container binauthz policy evaluate POLICY_ID \
        --image=my-conforming-pod.json

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud beta container binauthz policy evaluate POLICY_ID `
        --image=my-conforming-pod.json

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud beta container binauthz policy evaluate POLICY_ID ^
        --image=my-conforming-pod.json




### Evaluate a non-conformant image

In this section, you evaluate a Pod specification that doesn't conform to the policy that you created earlier in this guide. The evaluation produces a verdict that indicates that the Pod specification is `NON_CONFORMANT`, because the Pod specification references an image that resides outside of the directory that is specified in `trustedDirPatterns` in the trusted directory check.

To evaluate a non-conformant image, run the following commands:

  1. Create the Pod specification:
         
         cat << EOF > my-non-conforming-pod.json
         {
           "apiVersion": "v1",
           "kind": "Pod",
           "metadata": {
             "name": ""
           },
           "spec": {
             "containers": [
               {
                 "image": "us-docker.pkg.dev/untrusted-directory/containers/gke/hello-app:1.0"
               }
             ]
           }
         }
         EOF
         

  2. Use the policy evaluation service by running the following command:

Before using any of the command data below, make the following replacements: 

     * `POLICY_ID`: The ID of the platform policy. If the policy is in another project, you can use the full resource name: `projects/POLICY_PROJECT_ID/platforms/gke/policies/POLICY_ID`.
     * `my-non-conforming-pod.json`: The path of your Pod specification.

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud beta container binauthz policy evaluate POLICY_ID \
        --image=my-non-conforming-pod.json

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud beta container binauthz policy evaluate POLICY_ID `
        --image=my-non-conforming-pod.json

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud beta container binauthz policy evaluate POLICY_ID ^
        --image=my-non-conforming-pod.json




## What's next

  * [Learn more about CV](https://docs.cloud.google.com/binary-authorization/docs/overview-cv)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
