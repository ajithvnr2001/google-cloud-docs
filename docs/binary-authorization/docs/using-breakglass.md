---
url: https://docs.cloud.google.com/binary-authorization/docs/using-breakglass/
title: Use breakglass (GKE, Distributed Cloud) \u00a0|\u00a0 Binary Authorization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:48:12.567761+00:00
---

# Use breakglass (GKE, Distributed Cloud)  |  Binary Authorization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/docs/using-breakglass/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)
  * [ Guides ](https://docs.cloud.google.com/binary-authorization/docs/overview)



Send feedback 

#  Use breakglass (GKE, Distributed Cloud) Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This document or section includes references to one or more terms that Google considers disrespectful or offensive. The terms are used because they are keywords in the software that's described in the document. 

The terms: `whitelist`

This page provides instructions on using breakglass with Binary Authorization.

## Before you begin

This guide assumes you have [set up Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/setting-up).

## Overview

You use _breakglass_ to deploy a container image that Binary Authorization blocks.

Breakglass provides an emergency escape hatch that lets you override Binary Authorization policy enforcement to allow images to be deployed, even those that would be disallowed by the policy.

This feature is implemented consistent with recommendations in the Kubernetes [admission controller](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/) specification.

When you use breakglass to deploy an image, a breakglass event is automatically logged to Cloud Audit Logs, regardless of whether the deployment satisfies or violates the policy. In Cloud Audit Logs, you can manually audit or automatically trigger an alert or other downstream event.

To enable breakglass, you add a `label` field to the Pod specification with a `break-glass` policy flag.

## Demonstrate a breakglass event

This section shows how to use breakglass to deploy images, including those that violate the Binary Authorization policy.

### Update the Binary Authorization policy to reject all requests to deploy

**Note:** We recommend that the following steps only be performed on a test Google Kubernetes Engine project. To demonstrate a policy violation that results in an image being blocked from deployment, the following instructions update the default Binary Authorization policy, disallowing **all** images from being deployed. This procedure replaces your existing policy. **We recommend you save your existing policy before proceeding.**

To update the policy to disallow all images from being deployed, perform the following steps:

###  Google Cloud console 

  1. Go to the Binary Authorization page in the Google Cloud console.

[Go to Binary Authorization](https://console.cloud.google.com/security/binary-authorization/)

  2. Click **Edit policy**.

  3. In the **Edit policy** page, in **Project default rule** , note the original evaluation mode, then click **Disallow all images**.

  4. Click **Save policy**.




###  gcloud 

  1. To save the existing policy in the current project, execute the following command:
         
         gcloud container binauthz policy export > SAVE_POLICY_YAML
         

Replace SAVE_POLICY_YAML with the path of the export file—for example, `/tmp/save_policy.yaml`.

  2. Create a policy file:
         
         cat > TEST_POLICY_YAML << EOM
         admissionWhitelistPatterns:
         defaultAdmissionRule:
           enforcementMode: ENFORCED_BLOCK_AND_AUDIT_LOG
           evaluationMode: ALWAYS_DENY
         globalPolicyEvaluationMode: DISABLE
         EOM
         

Replace TEST_POLICY_YAML with a file path—for example, `/tmp/policy.yaml`.

  3. Import the policy:
         
         gcloud container binauthz policy import TEST_POLICY_YAML
         

Replace TEST_POLICY_YAML with a file path—for example, `/tmp/policy.yaml`.




By default, all images are now blocked from being deployed.

### Attempt to deploy an image

In this section you attempt to deploy an image. The default rule of the policy is configured to disallow all images from being deployed, so the deploy request fails.

  1. Create a configuration file in YAML format. This file contains the basic information required to create the pod:
         
         cat > /tmp/create_pod.yaml << EOM
         apiVersion: v1
         kind: Pod
         metadata:
           name: breakglass-pod
         spec:
           containers:
           - name: container-name
             image: us-docker.pkg.dev/google-samples/containers/gke/hello-app@sha256:c62ead5b8c15c231f9e786250b07909daf6c266d0fcddd93fea882eb722c3be4
         EOM
         

  2. Create the Pod using `kubectl`:
         
         kubectl create -f /tmp/create_pod.yaml
         

You see an error indicating that the image was blocked by your policy. The error resembles the following:
         
         Error from server (Forbidden): error when creating "/tmp/create_pod.yaml": pods "breakglass-pod" is forbidden: image policy webhook backend denied one or more images: Image gcr.io/google-samples/hello-app denied by Binary Authorization default
         admission rule. Denied by always_deny admission rule`.




### Enable breakglass and deploy again

In this section you enable breakglass. Although breakglass is specific to Binary Authorization, you must update the `label` field on the Pod specification to enable it.

To enable breakglass, execute the following commands:

  1. Create a configuration file in YAML format.

The following command creates the file containing the `break-glass` label and other information required to create the pod:
         
         cat > /tmp/create_pod.yaml << EOM
         apiVersion: v1
         kind: Pod
         metadata:
           name: pod-name
           labels:
             image-policy.k8s.io/break-glass: "true"
         spec:
           containers:
           - name: container-name
             image: us-docker.pkg.dev/google-samples/containers/gke/hello-app@sha256:c62ead5b8c15c231f9e786250b07909daf6c266d0fcddd93fea882eb722c3be4
         EOM
         

  2. Create the pod using `kubectl`:
         
         kubectl create -f /tmp/create_pod.yaml
         

Note the output: `pod/pod-name created`




## Find the breakglass log entry in Cloud Audit Logs

View breakglass events in [Cloud Audit Logs](https://docs.cloud.google.com/binary-authorization/docs/viewing-audit-logs#breakglass_events_in).

Older PodSpecs that specify `annotations: alpha.image-policy.k8s.io/break-glass` also trigger breakglass and produce log entries. Using that annotation is no longer recommended but is still supported to maintain backwards compatibility.

## Clean up

To delete the Pod and disable breakglass, do the following:

  1. Delete the Pod:
         
         kubectl delete -f /tmp/create_pod.yaml
           

Verify you received output like `pod <var>pod-name</var> deleted`.

  2. Remove the `label` block from your Pod specification.

  3. Reset your policy:

###  Google Cloud console 

     1. Go to the Binary Authorization page in the Google Cloud console.

[Go to Binary Authorization](https://console.cloud.google.com/security/binary-authorization/)

     2. Click **Edit policy**.

     3. In the **Edit policy** page, in **Project default rule** , reset the evaluation mode to the previous setting.

     4. Click **Save policy**.

###  gcloud 

     1. Reimport your original policy.
            
            gcloud container binauthz policy import SAVE_POLICY_YAML
            

Replace SAVE_POLICY_YAML with the path to the file you created earlier in this guide.

Your policy is reset.




## What's next

  * View breakglass events in [Cloud Audit Logs](https://docs.cloud.google.com/binary-authorization/docs/viewing-audit-logs#breakglass_events_in).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
