---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity/
title: About Workload Identity Federation for GKE \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:00.200863+00:00
---

# About Workload Identity Federation for GKE  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  About Workload Identity Federation for GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document describes Workload Identity Federation for GKE, including how it works, how enabling it affects your GKE clusters, and how to grant roles to Kubernetes entities in Identity and Access Management policies. In most cases, Workload Identity Federation for GKE is the recommended way to help secure and manage how your workloads that run on GKE access Google Cloud services.

This document is for Security specialists and Operators who manage workloads on GKE that require access to other Google Cloud services. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Terminology

This page distinguishes between [Kubernetes service accounts](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/) and [Identity and Access Management (IAM) service accounts](https://docs.cloud.google.com/iam/docs/service-accounts).

Kubernetes service accounts
    Kubernetes resources that provide an identity for processes running in your GKE pods.
IAM service accounts
    Google Cloud resources that allow applications to make authorized calls to Google Cloud APIs.

## What is Workload Identity Federation for GKE?

Applications running on GKE might need access to [Google Cloud APIs](https://docs.cloud.google.com/apis) such as Compute Engine API, BigQuery Storage API, or Machine Learning APIs.

Workload Identity Federation for GKE lets you use IAM policies to grant Kubernetes workloads in your GKE cluster access to specific Google Cloud APIs without needing manual configuration or less secure methods like service account key files. Using Workload Identity Federation for GKE lets you assign distinct, fine-grained identities and authorization for each application in your cluster.

Workload Identity Federation for GKE replaces the need to use [Metadata concealment](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/protecting-cluster-metadata). The sensitive metadata protected by metadata concealment is also protected by Workload Identity Federation for GKE.

Workload Identity Federation for GKE is available through IAM Workload Identity Federation, which provides identities for workloads that run in environments inside and outside Google Cloud. You can use IAM Workload Identity Federation to securely authenticate to [supported Google Cloud APIs](https://docs.cloud.google.com/iam/docs/federated-identity-supported-services) from workloads running on, for example, AWS, Azure, and self-managed Kubernetes. In GKE, Google Cloud manages the workload identity pool and provider for you and doesn't require an external identity provider.

## How Workload Identity Federation for GKE works

When you enable Workload Identity Federation for GKE on a cluster, GKE does the following:

  * Creates a fixed _workload identity pool_ for the cluster's Google Cloud project with the following format:
        
        PROJECT_ID.svc.id.goog
        

The workload identity pool provides a naming format that allows IAM to understand and trust Kubernetes credentials. GKE doesn't delete this workload identity pool even if you delete all of the clusters in your project.

  * Registers the GKE cluster as an identity provider in the workload identity pool.

  * Deploys the _GKE metadata server_, which intercepts credential requests from workloads, on every node.


**Note:** Enabling Workload Identity Federation for GKE on the cluster doesn't grant your workloads any additional IAM permissions.

### Create IAM allow policies on Google Cloud resources

To provide access with Workload Identity Federation for GKE, you create an IAM allow policy that grants access on a specific Google Cloud resource to a principal that corresponds to your application's identity. For example, you could give read permissions on a Cloud Storage bucket to all Pods that use the `database-reader` Kubernetes ServiceAccount.

For a list of resources that support allow policies, see [Resource types that accept allow policies](https://docs.cloud.google.com/iam/docs/resource-types-with-policies).

### Use conditions in IAM policies

You can also limit the scope of the access by setting _conditions_ in your allow policies. Conditions are an extensible method of specifying when an allow policy should apply. For example, you could use conditions to grant temporary access to a workload on a specific Google Cloud resource, eliminating the need to manage that access manually.

Conditions might also be useful if you set your allow policies at the project, folder, or organization level instead of on specific resources like Secret Manager secrets or Cloud Storage buckets.

To add a condition to your allow policy, use the following resources:

  * [Manage conditional role bindings](https://docs.cloud.google.com/iam/docs/managing-conditional-role-bindings): Add, modify, or remove conditional role bindings.
  * [Configure temporary access](https://docs.cloud.google.com/iam/docs/configuring-temporary-access): Use conditions to set expiring access to Google Cloud resources in allow policies.
  * [Tags and conditional access](https://docs.cloud.google.com/iam/docs/tags-access-control): Use conditions to only apply allow policies when resources have specific tags.



The following example expressions are for common scenarios in which you might use conditions. For a list of available attributes in expressions, see [Attribute reference for IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference).

Example condition expressions |  | Allow access before the specified time | 
    
    
    request.time < timestamp('TIMESTAMP')

Replace `TIMESTAMP` with a timestamp in UTC, like `2024-08-30T00:00:00.000Z`.  
---|---  
Allow access if the resource in the request has the specified tag | 
    
    
    resource.matchTag('TAG_KEY', 'TAG_VALUE')

Replace the following:

  * `TAG_KEY`: the tag key to match, like `env`
  * `TAG_VALUE`: the value of the tag, like `dev`

  
  
### Reference Kubernetes resources in IAM policies

In your IAM policy, you refer to a Kubernetes resource by using an IAM _principal identifier_ to select the resource. This identifier has the following syntax:
    
    
    PREFIX://iam.googleapis.com/projects/1234567890/locations/global/workloadIdentityPools/example-project.svc.id.goog/SELECTOR
    

In this example, consider the following fields:

  * `PREFIX`: must be `principal` or `principalSet` depending on the resource that you select. `principal` is for a specific resource, like a single ServiceAccount. `principalSet` is for multiple resources that belong to the specified resource, like all Pods in a specific cluster.
  * `SELECTOR`: a string that selects a principal type. For example, `kubernetes.serviceaccount.uid/SERVICEACCOUNT_UID` selects a ServiceAccount by its UID.



The following table shows the supported principal types in GKE:

Principal identifier type | Syntax  
---|---  
All Pods that use a specific Kubernetes ServiceAccount | **Select the ServiceAccount by name:**
    
    
    principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/NAMESPACE/sa/SERVICEACCOUNT

Replace the following:

  * `PROJECT_NUMBER`: your numerical project number. To get the project number, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * `PROJECT_ID`: your Google Cloud project ID.
  * `NAMESPACE`: the Kubernetes namespace.
  * `SERVICEACCOUNT`: the Kubernetes ServiceAccount name.



* * *

**Select the ServiceAccount by UID:**
    
    
    principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/kubernetes.serviceaccount.uid/SERVICEACCOUNT_UID

Replace the following:

  * `PROJECT_NUMBER`: your numerical project number. To get the project number, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * `PROJECT_ID`: your Google Cloud project ID.
  * `SERVICEACCOUNT_UID`: the UID of the `ServiceAccount` object in the API server.

  
All Pods in a namespace, regardless of service account or cluster | 
    
    
    principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/namespace/NAMESPACE

Replace the following:

  * `PROJECT_NUMBER`: your numerical project number. To get the project number, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * `PROJECT_ID`: your Google Cloud project ID.
  * `NAMESPACE`: the Kubernetes namespace.

  
All Pods in a specific cluster | 
    
    
    principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/kubernetes.cluster/https://container.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_NAME

Replace the following:

  * `PROJECT_NUMBER`: your numerical project number. To get the project number, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * `PROJECT_ID`: your Google Cloud project ID.
  * `CLUSTER_NAME`: the name of your GKE cluster.
  * `LOCATION`: the location of your cluster.

  
  
### Credential flow

When a workload sends a request to access a Google Cloud API, for example when using a Google Cloud client library, the following authentication steps occur:

![How a workload gets an IAM service account token with Workload Identity.](https://docs.cloud.google.com/static/kubernetes-engine/images/workload-identity-token-flow.svg)**Figure 1:** How a workload gets a federated access token with Workload Identity Federation for GKE.

  1. [_Application default credentials (ADC)_](https://docs.cloud.google.com/docs/authentication/application-default-credentials#attached-sa) requests a Google Cloud access token from the Compute Engine metadata server that runs on the VM.
  2. The GKE metadata server intercepts the token request and asks the Kubernetes API server for a Kubernetes ServiceAccount token that identifies the requesting workload. This credential is a JSON web token (JWT) that's signed by the API server.
  3. The GKE metadata server uses [Security Token Service](https://docs.cloud.google.com/iam/docs/reference/sts/rest) to exchange the JWT for a short-lived [federated access token](https://docs.cloud.google.com/docs/authentication/token-types#fed-access-tokens) that references the identity of the Kubernetes workload.



The federated access token that's returned by Security Token Service might have limitations when trying to access some Google Cloud services, as described in [Supported products and limitations](https://docs.cloud.google.com/iam/docs/federated-identity-supported-services). If your selected Google Cloud service has limitations, you can optionally configure service account impersonation. This method results in an access token for an IAM service account that your workload can use to access the target service. For details, see [link Kubernetes ServiceAccounts to IAM](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#kubernetes-sa-to-iam).

The workload can then access any Google Cloud APIs that the IAM principal identifier of the workload can access.

**Note:** Even with Workload Identity Federation for GKE configured on a cluster, GKE still uses the configured IAM service account for the node pool to pull container images from the image registry. If you encounter `ImagePullBackOff` or `ErrImagePull` errors, see [Troubleshoot image pulls](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/image-pulls).

#### Quota for the Exchange Token API in Security Token Service

The Exchange Token API in Security Token Service has a [quota limit](https://cloud.google.com/iam/quotas) of 6,000 requests per minute. If you see `QUOTA_EXCEEDED` errors, you can request an increase for the `Token exchange requests per minute` quota through the [Quotas & System Limits](https://console.cloud.google.com/iam-admin/quotas) page.

## Identity sameness

If the metadata in your principal identifier is the same for workloads in multiple clusters that share a workload identity pool because they belong to the same Google Cloud project, IAM identifies those workloads as the same. For example, if you have the same namespace in two clusters and you grant access to that namespace in IAM, the workloads in that namespace in both clusters get that access. You can limit this access to specific clusters by using conditional IAM policies.

For example, consider the following diagram. Clusters A and B belong to the same workload identity pool. Google Cloud identifies applications that use the `back-ksa` ServiceAccount in the `backend` namespace of both Cluster A and Cluster B as the same identity. IAM doesn't distinguish between the clusters making the calls.

[ ![Diagram illustrating identity sameness within a workload identity pool](https://docs.cloud.google.com/static/kubernetes-engine/images/identity-sameness-workload-identity.svg)](https://docs.cloud.google.com/static/kubernetes-engine/images/identity-sameness-workload-identity.svg) **Figure 2:** Identity sameness accessing Google Cloud APIs with Workload Identity Federation for GKE.

This identity sameness also means that you must be able to trust every cluster in a specific workload identity pool. For example, if a new cluster, Cluster C in the previous example was owned by an untrusted team, they could create a `backend` namespace and access Google Cloud APIs using the `back-ksa` ServiceAccount, just like Cluster A and Cluster B.

To avoid untrusted access, place your clusters in separate projects to ensure that they get different workload identity pools, or ensure that the namespace names are distinct from each other to avoid a common principal identifier.

## GKE metadata server

When you enable Workload Identity Federation for GKE for a cluster, every node in the cluster stores metadata on the _GKE metadata server_. The GKE metadata server is a subset of the [Compute Engine metadata server](https://docs.cloud.google.com/compute/docs/metadata/overview) endpoints required for Kubernetes workloads.

The GKE metadata server runs as a DaemonSet, with one Pod on every Linux node or a native Windows service on every Windows node in the cluster. The metadata server intercepts HTTP requests to `http://metadata.google.internal` (`169.254.169.254:80`). For example, the `GET /computeMetadata/v1/instance/service-accounts/default/token` request retrieves a token for the IAM service account that the Pod is configured to impersonate. Traffic to the GKE metadata server never leaves the VM instance that hosts the Pod.

### Token lifetime

By default, the access token returned has a lifetime of 1 hour (3,600 seconds). To reduce client latency, the GKE metadata server caches the access tokens. In some situations, the cached token that the metadata server returns might be close to its expiry time.

[Cloud Client Libraries](https://docs.cloud.google.com/apis/docs/cloud-client-libraries) have built-in logic that, by default, checks whether the access token expires in the next 3 minutes and 45 seconds. If the token is within the expiry period, GKE refreshes the token. Consecutive API calls can use the refreshed token.

If you use your own code to directly access Google Cloud APIs, implement similar logic to handle token expiry. Your code should do the following:

  1. Check whether the access token expires after a period of 3 minutes and 45 seconds. The `exp` parameter in the token payload indicates the token expiration timestamp.
  2. If the token is set to expire in the next 3 minutes and 45 seconds, make a token request.

**Note:** If you have a strict [cluster network policy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy) in place, you must allow egress to the following IP addresses and port numbers so your Pod can communicate with the GKE metadata server. Allow egress to `169.254.169.252/32` on port `988`. For clusters running GKE Dataplane V2, ensure that you allowed egress to `169.254.169.254/32` on port `80`.

The following tables describe the subset of Compute Engine metadata server endpoints available with the GKE metadata server. For a full list of endpoints available in the Compute Engine metadata server, see [Default VM metadata values](https://docs.cloud.google.com/compute/docs/metadata/default-metadata-values).

### Instance metadata

Instance metadata is stored under the following directory.

`http://metadata.google.internal/computeMetadata/v1/instance/`

Entry | Description  
---|---  
`hostname` | The hostname of your node.  
`id` | The unique ID of your node.  
`service-accounts/` |  A directory of service accounts associated with the node. For each service account, the following information is available: 

  * `aliases`
  * `email`: the service account email address.
  * `identity`: a JSON Web Token (JWT) unique to the node. You must include the `audience` parameter in your request. For example, `?audience=http://www.example.com`.
  * `scopes`: the access scopes assigned to the service account.
  * `token`: the OAuth 2.0 access token to authenticate your workloads.

  
`zone` |  The Compute Engine zone of your GKE node.  
  
#### Instance attributes

Instance attributes are stored under the following directory.

`http://metadata.google.internal/computeMetadata/v1/instance/attributes/`

Entry | Description  
---|---  
`cluster-location` | The Compute Engine zone or region of your cluster.  
`cluster-name` | The name of your GKE cluster.  
`cluster-uid` |  The UID of your GKE cluster.  
  
The attributes listed in the table are the only supported attributes. If you attempt to access any unsupported attributes, the `gke-metadata-server` Pod in the `kube-system` namespace generates and logs a `404` error. The error is similar to the following:
    
    
    HTTP/404: generic::not_found: no child "", Reason: "NOT_FOUND", UserMessage: "Not Found"
    

If you are using `istio-proxy`, you will encounter an error message like the following:
    
    
    Error fetching GCP Metadata property gcp_gce_instance_template: metadata: GCE metadata "instance/attributes/UNSUPPORTED_ATTRIBUTE" not defined
    

### Project metadata

Cluster project metadata is stored under the following directory.

`http://metadata.google.internal/computeMetadata/v1/project/`

Entry | Description  
---|---  
`project-id` | Your Google Cloud project ID.  
`numeric-project-id` | Your Google Cloud project number.  
  
## Restrictions of Workload Identity Federation for GKE

  * You can't change the name of the workload identity pool that GKE creates for your Google Cloud project.

  * If you [link Kubernetes ServiceAccounts to IAM service accounts](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#kubernetes-sa-to-iam) to configure Workload Identity Federation for GKE, the GKE metadata server returns a value of `SERVICEACCOUNT_NAME.svc.id.goog` as the service account identifier. This identifier doesn't use the standard IAM principal identifier syntax, which might cause errors in some programmatic operations. To get the service account identifier as an IAM principal identifier, add the `iam.gke.io/return-principal-id-as-email: "true"` annotation to your Kubernetes ServiceAccount.

  * When GKE enables the [GKE metadata server](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity#metadata_server) on a node pool, Pods can no longer access the [Compute Engine metadata server](https://docs.cloud.google.com/compute/docs/metadata/overview). Instead, the GKE metadata server intercepts requests made from these pods to metadata endpoints, with the exception of Pods running on the host network.

**Caution:** Pods running on the [host network](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#hosts-namespaces) (`hostNetwork: true`) don't use Workload Identity Federation for GKE. GKE automatically routes requests from these Pods to the Compute Engine metadata server.
  * When using [Cloud Storage FUSE CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/cloud-storage-fuse-csi-driver) with Standard GKE clusters with version `1.33.3-gke.1226000` or later, the Pods running on the host network (`hostNetwork: true`) can authenticate using their own Kubernetes Service Account. For more information, see [Configure access for Pods with host network](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-setup#access-for-pods-with-host-network).

  * The GKE metadata server takes a few seconds to start accepting requests on a newly created Pod. Therefore, attempts to authenticate using Workload Identity Federation for GKE within the first few seconds of a Pod's life might fail. Retrying the call will resolve the problem. See [Troubleshooting](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/troubleshooting-security#troubleshoot-timeout) for more details.

  * GKE built-in logging and monitoring agents continue to use the [node's service account](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#use_least_privilege_sa).

  * Workload Identity Federation for GKE requires [manual setup for Knative serving to continue releasing request metrics](https://docs.cloud.google.com/anthos/run/docs/setup#workload-identity).

  * Workload Identity Federation for GKE sets a limit of 500 concurrent connections to the GKE metadata server for each node. Additional concurrent calls that exceed this limit are placed in a wait queue for later processing. This queuing mechanism might lead to `HTTP/499` errors if the client timeout is reached before the GKE metadata server can process the request.

  * The GKE metadata server uses memory resources proportional to the total number of Kubernetes service accounts in your cluster. If your cluster has more than 3000 Kubernetes service accounts, the kubelet might terminate the metadata server Pods. For mitigations, refer to [Troubleshooting](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/troubleshooting-security#metadata-server-crashes).

  * Workload Identity Federation for GKE operates within a VPC Service Controls perimeter, allowing access to resources within it. You can also configure Workload Identity Federation for GKE principals in [VPC Service Controls ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/configure-identity-groups) ([Preview](https://cloud.google.com/products#product-launch-stages)) to allow cross-perimeter access without requiring intermediate IAM service account impersonation.




## Alternatives to Workload Identity Federation for GKE

You can use one of the following alternatives to Workload Identity Federation for GKE to access Google Cloud APIs from GKE. We recommend that you use Workload Identity Federation for GKE because these alternatives require you to make certain security compromises.

  * Use the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts) of your nodes. You can run node pools as any [IAM service account](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#use_least_privilege_sa) in your project. If you don't specify a service account during node pool creation, GKE uses the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) for the project. The Compute Engine service account is shared by all workloads deployed on that node. This can result in over-provisioning of permissions, which violates the principle of least privilege and is inappropriate for multi-tenant clusters.

  * [Export service account keys](https://docs.cloud.google.com/iam/docs/keys-create-delete#creating) and store them as [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/) that you mount to your Pods as volumes.

**Caution:** Service account keys are a security risk if not managed correctly. You should [ choose a more secure alternative to service account keys](https://docs.cloud.google.com/docs/authentication#auth-decision-tree) whenever possible. If you must authenticate with a service account key, you are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 




## What's next

  * [Learn how to enable and configure Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity).
  * [Learn about the Compute Engine metadata server](https://docs.cloud.google.com/compute/docs/metadata/overview).
  * [Learn about Workload Identity Federation in other environments](https://docs.cloud.google.com/iam/docs/workload-identity-federation).
  * [Provide Workload Identity Federation support for clusters in fleets by using fleet workload identity](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/use-workload-identity).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
