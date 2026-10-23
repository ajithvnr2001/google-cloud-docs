---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/troubleshooting/connection-source-of-truth/
title: Troubleshoot connecting to the source of truth \u00a0|\u00a0 Config Sync \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:41:12.533616+00:00
---

# Troubleshoot connecting to the source of truth  |  Config Sync  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/troubleshooting/connection-source-of-truth/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview)



Send feedback 

#  Troubleshoot connecting to the source of truth Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to resolve issues that occur when Config Sync cannot establish a connection with your source of truth.

## Authentication issues

If authentication fails, Config Sync cannot connect to the source of truth. The following sections show you how to resolve some authentication issues.

### Server certificate verification failed for Git servers

Connections to private Git servers use TLS to verify server authenticity. To make this validation, you must provide a certificate that identifies the root certificate authority and any intermediate certificate authorities that certify the identity of the Git server. If the Git server certificate verification failed, that means the chain of trust cannot be established.

If you receive an error indicating that server certificate verification failed, one of the following issues might be the cause:

  * The certificate authority certificate (CACert) is not specified. To fix this issue, add the CACert as a Secret and reference the Secret in the [`spec.git.caCertSecretRef` field](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rootsync-reposync-fields#configuring-git-repo) of your `RootSync` or `RepoSync` objects.
  * The CACert is incomplete. To fix this issue, fix the CACert Secret to contain the full chain of trust, including the root and any intermediate certificates.
  * The CACert is invalid. To fix this issue, download the certificate chain from the link specified by the certificate presented by the server and then update the CACert Secret.



### Unable to mount Git Secret

If you receive the following error when the `git-sync` container tries to sync a repository with a Secret, then the Git Secret isn't mounted successfully to the `git-sync` container:
    
    
    KNV2004: unable to sync repo Error in the git-sync container: ERROR: can't configure SSH: can't access SSH key: stat /etc/git-secret/ssh: no such file or directory: lstat /repo/root/rev: no such file or directory
    

The error could be caused by switching your Git repository authentication type from `none`, `gcenode`, or `gcpserviceaccount` to other types that need a Secret.

To resolve this issue, run the following commands to restart the Reconciler Manager and the Reconcilers:
    
    
    # Stop the reconciler-manager Pod. The reconciler-manager Deployment spins
    # up a new Pod which can pick up the latest `spec.git.auth`.
    kubectl delete po -l app=reconciler-manager -n config-management-system
    
    # Delete the reconciler Deployments. The reconciler-manager recreates the
    # reconciler Deployments with correct volume mount.
    kubectl delete deployment -l app=reconciler -n config-management-system
    

## Configuration issues

Often, issues with your configuration can cause Config Sync to be unable to connect to your source of truth. The following sections explain how to identify and resolve common configuration problems.

### Invalid chart name

When syncing from a Helm repository, make sure you set the correct value for `spec.helm.chart`. The chart name doesn't contain the repository name, chart version, or `.tgz`. You can verify your chart name with the [`helm template`](https://helm.sh/docs/helm/helm_template/) command.

### Invalid configuration directory

Check your configs for mistakes such as an incorrect value for `policyDir` in the `ConfigManagement` object or `spec.git.dir` or `spec.oci.dir` in the `RootSync` or `RepoSync` object. The value of the directory is included in any `KNV2004` error messages that you receive; verify the value against your Git repository or OCI image.

### Invalid Git branch

Check the logs for the `git-sync` container for an error such as `Remote branch BRANCH_NAME not found in upstream origin` or `warning: Could not find remote branch BRANCH_NAME to clone.` The default branch is set to `master` if not specified.

### Invalid Git, Helm, or OCI credentials

Check the Config Sync logs for the `git-sync`, `helm-sync`, or `oci-sync` container for one of the following errors:

  * `Could not read from remote repository. Ensure you have the correct access rights and the repository exists.`
  * `Invalid username or password. Authentication failed for ...`
  * `401 Unauthorized`



For a Git repository, verify that the Git credentials and the `git-creds` Secret are [configured correctly](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync#git-creds-secret).

For a Helm repository, verify that Helm credentials are [configured correctly](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync#helm-access).

For OCI images, verify that the OCI credentials are [configured correctly](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync#oci-access).

### Invalid Git repository URL

Check the logs for the `git-sync` container for an error such as `Repository not found`.

Check that you are using the correct URL format. For example, if you are using an SSH key pair to [authenticate to the Git repository](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync#git-creds-secret), make sure that the URL that you enter for your Git repository when you [configure Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync#configuring-config-sync) uses the SSH protocol.

### Invalid Helm repository URL

Check the logs for the `helm-sync` container for an error such as `...not a valid chart repository`. You can verify your Helm repository URL with the [`helm template`](https://helm.sh/docs/helm/helm_template/) command.

### Invalid OCI registry URL

An invalid value in the `spec.oci.image` or `spec.oci.dir` field of a `RootSync` or `RepoSync` object can cause connection issues. Check that these values are correct. For example, if you are syncing from an OCI registry, the URL should start with `oci://`.

You can also check the logs for the `oci-sync` container for more information.

## Network issues

If you suspect the issue is related to your cluster's network, start with these troubleshooting steps.

### Couldn't resolve host: github.com

When Config Sync tries to connect to your Git repository, it uses DNS to resolve the IP of the specified hostname. If the host cannot be resolved, this usually indicates a problem with either DNS or cluster networking.

To diagnose the problem, see either [Troubleshoot Cloud DNS in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/cloud-dns) or [Troubleshoot kube-dns in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/kube-dns), depending which service you're using as your DNS provider.

### Git repository is unreachable from within the cluster

Sometimes, the `git-sync` container throws an error in its logs that indicates that it can't reach the repository. For example, `ssh: connect to host source.developers.google.com port 2022: Network is unreachable`. To fix the issue, adjust the firewall or network configuration of your cluster.

### High number of source API requests

Config Sync uses a multi-instancing strategy to scale and isolate tenants and fault domains. Because of this, each `RootSync` and `RepoSync` object gets its own reconciler instance. Each reconciler instance has its own source-specific sidecar, `git-sync`, `oci-sync`, or `helm-sync`. These sidecars poll the source of truth. When you add additional `RootSync` or `RepoSync` objects, this causes a linear increase in the number of API requests made by the reconcilers polling the source of truth. So if you have many `RootSync` and `RepoSync` objects all polling the same source of truth, this can sometimes cause significant traffic load on the source server.

Consider one of the following strategies to mitigate this issue:

  * Combine multiple `RootSyncs` or `RepoSync` objects, to reduce the number of reconcilers making source API requests.
  * Change your source type from Git to OCI. OCI repositories, like Artifact Registry, tend to scale better than most Git servers, because they can scale horizontally without needing to synchronize between server replicas.



## What's next

  * If you're still experiencing issues, check to see if your problem is a [known issue](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/known-issues).



If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/get-support-config-sync) for further help, including advice on the following topics: 

  * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
  * Getting support from the community by [asking questions on Stack Overflow](http://stackoverflow.com/questions). If you use kpt or Kustomize, use the `kpt` or `kustomize` tag to search for similar issues.
  * Opening bugs or feature requests by using the [public issue tracker](https://github.com/GoogleContainerTools/config-sync/issues) on GitHub.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
