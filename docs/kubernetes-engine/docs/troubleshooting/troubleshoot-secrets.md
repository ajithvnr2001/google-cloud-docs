---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/troubleshoot-secrets/
title: Troubleshoot application-layer secrets encryption \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:23.380307+00:00
---

# Troubleshoot application-layer secrets encryption  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/troubleshoot-secrets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  Troubleshoot application-layer secrets encryption Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

[Application-layer secrets encryption](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/encrypting-secrets) adds a configurable layer of protection for sensitive data in Google Kubernetes Engine (GKE), such as credentials and keys. Issues with this configuration can prevent this extra security layer from working correctly.

Use this document to troubleshoot application-layer secrets encryption by inspecting the debugging fields available in the GKE API Cluster object. These fields help you diagnose the root cause of common errors, such as failed updates or issues with your Cloud KMS key.

This information is important for Platform admins and operators and Security engineers responsible for protecting sensitive information stored in GKE clusters. For more information about the common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Failed update

When you update the encryption configuration of application-layer secrets encryption, GKE must rewrite all [Secret](https://kubernetes.io/docs/concepts/configuration/secret/) objects in the Kubernetes cluster. GKE does this to help ensure that all Secrets are encrypted by the new Cloud KMS Key, or are written un-encrypted if that is what you configure.

This update operation can fail due to any of the following conditions:

  * The Kubernetes control plane is temporarily unavailable while the update is in progress.
  * A user-defined `AdmissionWebhook` prevents GKE from being able to update Secret objects.
  * The updated or previous Cloud KMS key is disabled before the update operation completes.



Until the update operation is successful, don't interact with either the updated or previous Cloud KMS keys.

## Debugging fields

**New** GKE clusters running version 1.29 and later contain additional fields that help you track updates to `Cluster.DatabaseEncryption` and help you recover from failures.

The following steps only apply to clusters where the `DatabaseEncryption.CurrentState` field is not empty. If the `CurrentState` field is empty, the feature is not enabled on this cluster version yet.

The following limits apply to these fields:

  * Are **output only** , which means that you can't set them during cluster create or update requests.



### `CurrentState` field

You can inspect the current status of a `DatabaseEncryption` update operation by examining the `CurrentState` field in `Cluster.DatabaseEncryption`.

Value of `CurrentState` | Description  
---|---  
`CURRENT_STATE_ENCRYPTED` `CURRENT_STATE_ALL_OBJECTS_ENCRYPTION_ENABLED` `CURRENT_STATE_DECRYPTED` |  The latest update operation was successful. No further action is needed. You can dispose of any previously used keys.   
`CURRENT_STATE_ENCRYPTION_PENDING` `CURRENT_STATE_ALL_OBJECTS_ENCRYPTION_PENDING` `CURRENT_STATE_DECRYPTION_PENDING` | The update is in progress.  
`CURRENT_STATE_ENCRYPTION_ERROR` `CURRENT_STATE_ALL_OBJECTS_ENCRYPTION_ERROR` `CURRENT_STATE_DECRYPTION_ERROR` |  There was an error with the most recent update. Don't disable or destroy any previously used Cloud KMS keys, as they might still be in use by GKE.  Refer to the `LastOperationErrors` field for more information.   
  
### `LastOperationErrors` field

When an update operation fails, the underlying error from the GKE control plane is displayed in the output of `gcloud container clusters update`.

The error messages from the two most recent failed update operations are also available in `Cluster.DatabaseEncryption.LastOperationErrors`.

### `DecryptionKeys` field

The Cloud KMS key used for new encryption operations is shown in `DatabaseEncryption.KeyName`. Usually this is the only key used by the cluster.

However, `DatabaseEncryption.DecryptionKeys` contains additional keys that are also used by the cluster if an update is in progress or after a failure.

## Recover from a failed update

To recover from a failed update, do the following:

  1. Examine the error message and address any issues indicated.
  2. Retry the update request by running the failed command, such as `gcloud container clusters update ... --database-encryption-key`. We recommend that you retry with the same update request that you originally issued, or update the cluster back to the previous state. GKE might not be able to transition to a different key or encryption state if it can't read one or more Secrets.



The following sections list common reasons for errors.

### Cloud KMS key error

If the error message contains a reference to one or more Cloud KMS keys, examine your Cloud KMS key configuration to make sure the relevant key versions are usable.

If the error indicates that a Cloud KMS key has been disabled or destroyed, re-enable the key or key version.

#### Error: Unable to use CloudKMS key configured for Application Level encryption

The following error message occurs if GKE's default service account can't access the Cloud KMS key:
    
    
    Cluster problem detected (Kubernetes Engine Service Agent account unable to use CloudKMS key configured for Application Level encryption).
    

To resolve this issue, [re-enable the disabled key](https://docs.cloud.google.com/kms/docs/enable-disable#enable).

### Unable to update Secret

The following error might occur if the Kubernetes API rejected the update request due to an admission webhook:
    
    
    error admission webhook WEBHOOK_NAME denied the request
    

To resolve this error, remove the webhook or modify it so that GKE can update Secrets in all namespaces during key updates.

### Error: the namespace is managed

The following error occurs when you try to re-encrypt Secrets that are in a GKE-managed namespace, such as `kube-system`, in an Autopilot cluster. The error message is similar to the following:
    
    
    Error from server (Forbidden): secrets "alertmanager" is
    forbidden: User cannot patch resource "secrets" in API group "" in the namespace "gke-gmp-system":
    GKE Warden authz [denied by managed-namespaces-limitation]: the namespace "gke-gmp-system"
    is managed and the request's verb "patch" is denied'
    

GKE Autopilot clusters don't allow you to modify Kubernetes resources, including Secrets, in managed namespaces.

To resolve this error, do the following:

  * If you use `kubectl` commands to re-encrypt Secrets, use the `--namespace` flag to scope the command to namespaces that you manage.
  * If you use a CronJob to re-encrypt Secrets, deploy it in only the namespaces that you manage.



## Unresponsive control plane after disabling encryption

Disabling the application-layer secrets encryption too quickly after you enable it can interrupt the initial encryption job, which can cause your cluster's `kube-apiserver` control plane to become unresponsive.

The following are symptoms of this issue:

  * Cluster operations like `list node`, `list pods`, and `get apiserver readiness` fail with error code 13 and the `Internal Server Error` message.
  * Kube controllers are non-functional, and deleted Pods from StatefulSets or ReplicaSets are not re-created.
  * Webhook calls fail because the connection is refused.



To mitigate this issue, do the following:

  * Re-enable application-layer secret encryption by using the same Cloud KMS key that you previously used to enable the encryption.



To prevent this issue, ensure the following:

  * After you enable application-layer secret encryption, verify that the cluster has been stable for a few hours before you disable the encryption.



## What's next

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further help, including advice on the following topics:

    * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
    * Getting support from the community by [asking questions on StackOverflow](http://stackoverflow.com/questions/tagged/google-kubernetes-engine) and using the `google-kubernetes-engine` tag to search for similar issues. You can also join the [`#kubernetes-engine` Slack channel](https://googlecloud-community.slack.com/messages/C0B9GKTKJ/) for more community support.
    * Opening issues or feature requests by using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
