---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/troubleshooting/permission-service-account/
title: Troubleshoot permission issues with a Google service account \u00a0|\u00a0 Config Sync \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:59.459495+00:00
---

# Troubleshoot permission issues with a Google service account  |  Config Sync  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/troubleshooting/permission-service-account/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview)



Send feedback 

#  Troubleshoot permission issues with a Google service account Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to resolve permission issues that occur when using Config Sync with a Google service account.

**Best practice:** If you sync from an OCI image or Helm repository in Artifact Registry, authenticate directly with a [Kubernetes ServiceAccount (`k8sserviceaccount`)](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/grant-access-helm-oci) instead of a Google service account (`gcpserviceaccount`) to avoid managing additional service account bindings.

## Missing reader access

When using a Google service account (`spec.git.gcpServiceAccountEmail`, or `spec.oci.gcpServiceAccountEmail`, or `spec.helm.gcpServiceAccountEmail`) to authenticate to Cloud Source Repositories or Artifact Registry, the Google service account requires the following reader access:

  * Cloud Source Repositories: `roles/source.reader`
  * Artifact Registry: `roles/artifactregistry.reader`



If the service account is missing these roles, `git-sync` or `oci-sync` or `helm-sync` fails with errors similar to the following:
    
    
    failed to pull image us-docker.pkg.dev/...: GET https://us-docker.pkg.dev/v2/token?scope=repository...: DENIED: Permission \"artifactregistry.repositories.downloadArtifacts\" denied on resource \"projects/.../locations/us/repositories/...\" (or it may not exist)
    
    
    
    "Err":"failed to render the helm chart: exit status 1, stdout: Error: failed to download ...
    

To fix this issue, grant the service account the correct reader access.

## Missing IAM policy binding with Workload Identity Federation for GKE

When using a Google service account for authentication, an IAM policy binding is required between the Google service account and the Kubernetes ServiceAccount. If the IAM policy binding is missing, you get the following error:
    
    
    KNV2004: unable to sync repo Error in the git-sync container: ERROR: failed to call ASKPASS callback URL: auth URL returned status 500, body: "failed to get token from credentials: oauth2/google: status code 403: {\n \"error\": {\n \"code\": 403,\n \"message\": \"The caller does not have permission\",\n \"status\": \"PERMISSION_DENIED\"\n }\n}\n"
    

To fix the issue, create the following IAM policy binding:
    
    
    gcloud iam service-accounts add-iam-policy-binding \
       --role roles/iam.workloadIdentityUser \
       --member "serviceAccount:PROJECT_ID.svc.id.goog[config-management-system/KUBERNETES_SERVICEACCOUNT]" \
       GSA_NAME@PROJECT_ID.iam.gserviceaccount.com
    

Replace the following:

  * `PROJECT_ID`: If you're using GKE Workload Identity Federation for GKE, add your organization's project ID. If you're using fleet Workload Identity Federation for GKE, you can use two different project IDs. In `serviceAccount:PROJECT_ID`, add the project ID of the fleet that your cluster is registered to. In `GSA_NAME@PROJECT_ID`, add a project ID for any project that has read access to the repository in Cloud Source Repositories.

  * `KUBERNETES_SERVICEACCOUNT`: the Kubernetes ServiceAccount for the reconciler. For root repositories, if the `RootSync` name is `root-sync`, `KUBERNETES_SERVICEACCOUNT` is `root-reconciler`. Otherwise, it is `root-reconciler-ROOT_SYNC_NAME`.

For namespace repositories, if the `RepoSync` name is `repo-sync`, `KUBERNETES_SERVICEACCOUNT` is `ns-reconciler-NAMESPACE`. Otherwise, it is `ns-reconciler-NAMESPACE-REPO_SYNC_NAME`.

  * `GSA_NAME`: the custom Google service account that you want to use to connect to Cloud Source Repositories. Make sure that the Google service account that you select has the `source.reader` role.




Creating this policy binding requires the `iam.serviceAccounts.setIamPolicy` permission.

Make sure that fleet Workload Identity Federation for GKE is enabled on your registered clusters. For more information, see [Register a cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster#register_cluster). If your cluster is in a project different from the fleet host project, you need to bind the Google service account with the Kubernetes service account in the fleet host project.

## Missing `cloud-platform` scope to access Cloud Source Repositories

When granting a Google service account access to your Git repository in Cloud Source Repositories, the read-only scope must be included in [access scopes](https://docs.cloud.google.com/compute/docs/access/service-accounts#accesscopesiam) for the nodes in the cluster.

The read-only scope can be added by including `cloud-source-repos-ro` in the `--scopes` list specified at cluster creation time, or by using the `cloud-platform` scope at cluster creation time. For example:
    
    
    gcloud container clusters create CLUSTER_NAME --scopes=cloud-platform
    

If the read-only scope is missing, you see an error similar to the following:
    
    
    Error in the git-sync container: {"Msg":"unexpected error syncing repo, will retry","Err":"Run(git clone -v --no-checkout -b main --depth 1 https://source.developers.google.com/p/PROJECT_ID/r/csr-auth-test /repo/source): exit status 128: { stdout: \"\", stderr: \"Cloning into '/repo/source'...\\nremote: INVALID_ARGUMENT: Request contains an invalid argument\\nremote: [type.googleapis.com/google.rpc.LocalizedMessage]\\nremote: locale: \\\"en-US\\\"\\nremote: message: \\\"Invalid authentication credentials. Please generate a new identifier: https://source.developers.google.com/new-password\\\"\\nremote: \\nremote: [type.googleapis.com/google.rpc.RequestInfo]\\nremote: request_id: \\\"fee01d10ba494552922d42a9b6c4ecf3\\\"\\nfatal: unable to access 'https://source.developers.google.com/p/PROJECT_ID/r/csr-auth-test/': The requested URL returned error: 400\\n\" }","Args":{}}
    

## Missing `storage-ro` scope to access Artifact Registry

When you're using Artifact Registry, image layers are kept in Cloud Storage buckets. When granting a Google service account access to your OCI image or Helm Chart in Artifact Registry, the read-only scope must be included in [access scopes](https://docs.cloud.google.com/compute/docs/access/service-accounts#accesscopesiam) for the nodes in the cluster.

The read-only scope can be added by including `storage-ro` in the `--scopes` list specified at cluster creation time, or by using the `cloud-platform` scope at cluster creation time. For example:
    
    
    gcloud container clusters create CLUSTER_NAME --scopes=cloud-platform
    

If the read-only scope is missing, you see an error similar to the following:
    
    
    Error in the oci-sync container: {"Msg":"unexpected error fetching package, will retry","Err":"failed to pull image us-docker.pkg.dev/...: GET https://us-docker.pkg.dev/v2/token?scope=repository%3A...%3Apull\u0026service=us-docker.pkg.dev: UNAUTHORIZED: failed authentication","Args":{}}
    

The error message might not include the full details for what caused the error, but it does provide a command which prints the logs from the `git-sync` container which might have more information.

If you've enabled the `RootSync` or `RepoSync` APIs, run the following command:
    
    
    kubectl logs -n config-management-system -l app=reconciler -c git-sync
    

If you haven't enabled the `RootSync` or `RepoSync` APIs, run the following command:
    
    
    kubectl logs -n config-management-system -l app=git-importer -c git-sync
    

`RootSync` and `RepoSync` APIs are enabled by default if you used the Google Cloud console or the Google Cloud CLI to install Config Sync and you cannot disable it.

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
