---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/autopilot-privileged-workloads/
title: Troubleshoot privileged Autopilot workloads and allowlists \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:02:11.389800+00:00
---

# Troubleshoot privileged Autopilot workloads and allowlists  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/autopilot-privileged-workloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Troubleshoot privileged Autopilot workloads and allowlists Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)

Privileged workloads in Google Kubernetes Engine (GKE) Autopilot clusters must be configured correctly to avoid problems. Misconfigurations can lead to synchronization failures with allowlists or cause the workload to be rejected. These problems can prevent essential agents or services from running with the necessary permissions.

Use this document to troubleshoot issues with deploying privileged workloads on Autopilot. Find guidance on resolving allowlist synchronization errors and diagnosing why a privileged workload might be rejected.

This information is important for Platform admins and operators and security teams who deploy workloads with elevated permissions on Autopilot clusters. For more information about the common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Allowlist synchronization issues

When you deploy an AllowlistSynchronizer, GKE attempts to install and synchronize the allowlist files that you specify. If this synchronization fails, the `status` field of the AllowlistSynchronizer reports the error.

Get the status of the `AllowlistSynchronizer` object:
    
    
    kubectl get allowlistsynchronizer ALLOWLIST_SYNCHRONIZER_NAME -o yaml
    

Replace `ALLOWLIST_SYNCHRONIZER_NAME` with the name of the AllowlistSynchronizer.

The output is similar to the following:
    
    
    ...
    status:
      conditions:
      - type: Ready
        status: "False"
        reason: "SyncError"
        message: "some allowlists failed to sync: example-allowlist-1.yaml"
        lastTransitionTime: "2024-10-12T10:00:00Z"
        observedGeneration: 2
      managedAllowlistStatus:
        - filePath: "gs://path/to/allowlist1.yaml"
          generation: 1
          phase: Installed
          lastSuccessfulSync: "2024-10-10T10:00:00Z"
        - filePath: "gs://path/to/allowlist2.yaml"
          phase: Failed
          lastError: "Initial install failed: invalid contents"
          lastSuccessfulSync: "2024-10-08T10:00:00Z"
    

The `conditions.message` field and the `managedAllowlistStatus.lastError` field provide detailed information about the error. Use this information to resolve the issue.

### Multiple AllowlistSynchronizers

In GKE clusters on versions earlier than 1.33.4-gke.1035000, `WorkloadAllowlists` might fail to install if more than one `AllowlistSynchronizer` is present.

To resolve the issue, use only a single `AllowlistSynchronizer` that contains multiple `allowlistPaths`.

Alternatively, you can upgrade your cluster to a newer version.

### Workload container sorting

In GKE clusters on versions earlier than 1.34.0-gke.0000000, if one or more workload container images match a container image that's specified in an in-cluster WorkloadAllowlist, then the workload containers might be created and sorted in reverse-alphabetical order.

To resolve this issue, try the following options:

  * Upgrade your cluster to version 1.34.0-gke.0000000 or later.
  * Rename your workload's containers so that they are sorted in the correct order.



## Privileged workload deployment issues

After successfully installing an allowlist, you deploy the corresponding privileged workload in your cluster. In some cases, GKE might reject the workload.

Try the following resolution options:

  * Ensure that the GKE version of your cluster meets the version requirement of the workload.
  * Ensure that the workload that you're deploying is the workload to which the allowlist file applies.



To see why a privileged workload was rejected, request detailed information from GKE about allowlist violations:

  1. Get a list of the installed allowlists in the cluster:
         
         kubectl get workloadallowlist
         

Find the name of the allowlist that should apply to the privileged workload.

  2. Open the YAML manifest of the privileged workload in a text editor. If you can't access the YAML manifests, for example if the workload deployment process uses other tooling, contact the workload provider to open an issue. Skip the remaining steps.

  3. Add the following label to the `spec.metadata.labels` section of the privileged workload Pod specification:
         
         labels:
           **cloud.google.com/matching-allowlist : ALLOWLIST_NAME**
         

Replace `ALLOWLIST_NAME` with the name of the allowlist that you obtained in the previous step. Use the name from the output of the `kubectl get workloadallowlist` command, not the path to the allowlist file.

  4. Save the manifest and apply the workload to the cluster:
         
         kubectl apply -f WORKLOAD_MANIFEST_FILE
         

Replace `WORKLOAD_MANIFEST_FILE` with the path to the manifest file.

The output provides detailed information about which fields in the workload didn't match the specified allowlist, like in the following example:
         
         Error from server (GKE Warden constraints violations): error when creating "STDIN": admission webhook "warden-validating.common-webhooks.networking.gke.io" denied the request:
         
         ===========================================================================
         Workload Mismatches Found for Allowlist (example-allowlist-1):
         ===========================================================================
         HostNetwork Mismatch: Workload=true, Allowlist=false
         HostPID Mismatch: Workload=true, Allowlist=false
         Volume[0]: data
                  - data not found in allowlist. Verify volume with matching name exists in allowlist.
         Container[0]:
         - Envs Mismatch:
                 - env[0]: 'ENV_VAR1' has no matching string or regex pattern in allowlist.
                 - env[1]: 'ENV_VAR2' has no matching string or regex pattern in allowlist.
         - Image Mismatch: Workload=k8s.gcr.io/diff/image, Allowlist=k8s.gcr.io/pause2. Verify that image string or regex match.
         - SecurityContext:
                 - Capabilities.Add Mismatch: the following added capabilities are not permitted by the allowlist: [SYS_ADMIN SYS_PTRACE]
         - VolumeMount[0]: data
                 - data not found in allowlist. Verify volumeMount with matching name exists in allowlist.
         

In this example, the following violations occur:

     * The workload specifies `hostNetwork: true`, but the allowlist doesn't specify `hostNetwork: true`.
     * The workload specifies `hostPID: true`, but the allowlist doesn't specify `hostPID: true`.
     * The workload specifies a volume named `data`, but the allowlist doesn't specify a volume named `data`.
     * The container specifies environment variables named `ENV_VAR1` and `ENV_VAR2`, but the allowlist doesn't specify these environment variables.
     * The container specifies the image `k8s.gcr.io/diff/image`, but the allowlist specifies `k8s.gcr.io/pause2`.
     * The container adds the `SYS_ADMIN` and `SYS_PTRACE` capabilities, but the allowlist doesn't allow adding these capabilities.
     * The container specifies a volume mount named `data`, but the allowlist doesn't specify a volume mount named `data`.



If you're deploying a workload that's owned by a third-party provider, open an issue with that provider to resolve the violations. Provide the output from the previous step in the issue.

### Incompatible GKE version

GKE might reject a workload if the allowlist specifies a minimum GKE version that's later than the cluster GKE version.

  1. Check whether the allowlist specifies a minimum GKE version:
         
         kubectl describe workloadallowlist ALLOWLIST_NAME | grep "minGKEVersion"
         

Replace `ALLOWLIST_NAME` with the name of the allowlist.

If the output is empty, the allowlist doesn't specify a minimum GKE version. Skip this section. If the output is a value, the allowlist specifies a minimum GKE version.

  2. Check the cluster GKE version:
         
         gcloud container clusters describe CLUSTER_NAME \
             --location=CLUSTER_LOCATION \
             --format="value(currentMasterVersion)"
         

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster.
     * `CLUSTER_LOCATION`: the Google Cloud location of the cluster.

The output is similar to the following:
    
    1.32.3-gke.1006000
    

  3. If the GKE version of the cluster is earlier than the minimum GKE version of the allowlist, upgrade the cluster to the minimum GKE version of the allowlist or later. For more information, see [Upgrading the cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#upgrading_the_cluster).




After the upgrade completes, try to deploy the workload to the cluster.

### String mismatches

Specific fields in the WorkloadAllowlist specification must be exact string matches of the corresponding fields in the workload specification.

  1. [Open the WorkloadAllowlist CustomResourceDefinition (CRD) reference page](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/workloadallowlist).
  2. For each field in your WorkloadAllowlist specification, check whether the CRD requires an exact string match.
  3. For each field that requires an exact string match, check whether the value in your WorkloadAllowlist specification matches the corresponding value in your workload specification.

For example, every command that a container runs must exactly match a command in the allowlist. Any deviation from the exact command results in a rejection.




If there's a mismatch, update your WorkloadAllowlist specification to match your workload specification.

### Regular expression mismatches

Specific fields in the WorkloadAllowlist specification support regular expression matching.

  1. In your WorkloadAllowlist specification, find the fields that specify regular expressions.
  2. Ensure that the regular expression syntax is correct. The WorkloadAllowlist CRD supports the [Google RE2 regular expression syntax](https://github.com/google/re2/wiki/syntax). Validate that your expressions have the following properties:

     * The regular expression begins with the `^` character and ends with the `$` character. For example, `^example-auth\.google\.com\/go_[a-z0-9]+\/google\/path$`.
     * Every special character is escaped with the `\` escape character. Look for extra or missing `\` characters.
     * Image paths in the allowlist don't include tags or digests. For example, use `k8s.gcr.io/pause` instead of `k8s.gcr.io/pause:3.1` or `k8s.gcr.io/pause@sha256:1234567890`.



After you fix any regular expression issues, try to deploy your workload to the cluster.

### Escape characters in commands and arguments

GKE can't match commands and arguments if you don't escape the special characters. The requirements for escaping characters depend on how you apply the allowlist. For example, applying an allowlist as a YAML or JSON file has different escaping requirements than creating an allowlist specification by using a command-line tool. This section describes the escaping requirements for YAML files.

Escape every special character in the `commands` and `args` fields of the WorkloadAllowlist specification, even if you don't use a regular expression. To escape special characters, use the `\` character, such as in the following examples:

  * **Command** : `kubectl describe \$\{POD_NAME\}`
  * **Argument** : `hostname \$NODE_NAME; dcgm-exporter --remote-hostengine-info \$\(NODE_IP\) --collectors /etc/dcgm-exporter/counters.csv`



### Webhook interference with workloads on an allowlist

In some cases, even if a workload is correctly configured to match an allowlist, it might still be rejected by GKE. This situation can happen if another admission controller (webhook) in your cluster modifies the Pods created by the workload controller after they have been allowed by the allowlist. These modifications can cause the Pod specification to no longer match the allowlist, leading to rejection by the GKE Warden admission webhook.

This issue is common with third-party monitoring and security agents that inject sidecar containers or environment variables into Pods.

The most common symptom is that your workload controller (such as a DaemonSet or Deployment) is created successfully, but it fails to create any Pods. When you inspect the controller's events, you will see messages indicating that the Pods were denied by the admission webhook.

  1. Follow the steps in the Privileged workload deployment issues section to add the `cloud.google.com/matching-allowlist` label to your workload.
  2. Copy the `spec.template` from your workload's YAML manifest.
  3. Create a new Pod manifest and paste the copied spec into the `spec` field.
  4. Set the `apiVersion`, `kind`, and `metadata.name` fields in the Pod manifest:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: POD_NAME
           labels:
             cloud.google.com/matching-allowlist: ALLOWLIST_NAME
         spec:
           # Paste the content of spec.template here
         

Replace the following:

     * `POD_NAME`: The name for your test Pod.
     * `ALLOWLIST_NAME`: The name of the allowlist.
  5. Apply the Pod manifest:
         
         kubectl apply -f YOUR_POD_MANIFEST_FILE
         

Replace `YOUR_POD_MANIFEST_FILE` with the path to your Pod manifest file.

  6. Inspect the output from the previous step. If you see unexpected fields in the "Workload Mismatches" section, such as extra environment variables (for example, `DD_AGENT_HOST`), containers, or volumes, it is a strong indication that another webhook is modifying your Pods.




To resolve this issue, you need to configure the conflicting webhook to exclude it from modifying the Pods of your allowlisted workload. This is typically done by adding a label or annotation to the workload or its namespace to signal to the webhook that it should be excluded from mutation. For example, with Datadog, you would add the `admission.datadoghq.com/enabled: "false"` label to your workload's namespace.

Consult the documentation for the specific third-party software you are using to learn how to exclude workloads from its admission controller.

By preventing the other webhook from modifying the Pods, you can help to ensure that they continue to match the allowlist and are successfully deployed on your Autopilot cluster.

## Bugs and feature requests for privileged workloads and allowlists

If you run a privileged workload that's provided by a GKE partner or a third-party provider, that provider is responsible for creating, developing, and maintaining their privileged workloads and allowlists. If you encounter a bug or have a feature request for a partner or third-party privileged workload or allowlist, contact the provider.

## What's next

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further help, including advice on the following topics:

    * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
    * Getting support from the community by [asking questions on StackOverflow](http://stackoverflow.com/questions/tagged/google-kubernetes-engine) and using the `google-kubernetes-engine` tag to search for similar issues. You can also join the [`#kubernetes-engine` Slack channel](https://googlecloud-community.slack.com/messages/C0B9GKTKJ/) for more community support.
    * Opening issues or feature requests by using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
