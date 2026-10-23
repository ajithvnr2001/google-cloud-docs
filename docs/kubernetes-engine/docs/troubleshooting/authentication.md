---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/authentication/
title: Troubleshoot GKE authentication issues \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:01.596635+00:00
---

# Troubleshoot GKE authentication issues  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/authentication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  Troubleshoot GKE authentication issues Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Authentication issues in Google Kubernetes Engine (GKE) can prevent principals, such as users and workloads, from accessing the Kubernetes API server, or impede access between GKE resources and other Google Cloud services.

Use this document to diagnose authentication issues, fix errors in Kubernetes RBAC and IAM, and troubleshoot issues with Workload Identity Federation for GKE.

This information is important for Platform admins and operators and security administrators responsible for securing GKE clusters and managing access control. For more information about the common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## RBAC and IAM

### Authenticated IAM accounts fail to perform in-cluster actions

The following issue occurs when you try to perform an action in the cluster but GKE can't find an RBAC policy that authorizes the action. GKE attempts to find an IAM allow policy that grants the same permission. If that fails, you see an error message similar to the following:
    
    
    Error from server (Forbidden): roles.rbac.authorization.k8s.io is forbidden:
    User "example-account@example-project.iam.gserviceaccount.com" cannot list resource "roles" in
    API group "rbac.authorization.k8s.io" in the namespace "kube-system": requires
    one of ["container.roles.list"] permission(s).
    

To resolve this issue, use an RBAC policy to grant the permissions for the attempted action. For example, to resolve the issue in the previous sample, grant a Role that has the `list` permission on `roles` objects in the `kube-system` namespace. For instructions, see [Authorize actions in clusters using role-based access control](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control).

## Workload Identity Federation for GKE

### Pod can't authenticate to Google Cloud

If your application can't authenticate to Google Cloud, make sure that the following settings are configured properly:

  1. Confirm that Workload Identity Federation for GKE is enabled on the cluster by verifying that it has a workload identity pool set:
         
         gcloud container clusters describe CLUSTER_NAME \
             --format="value(workloadIdentityConfig.workloadPool)"
         

Replace `CLUSTER_NAME` with the name of your GKE cluster.

If you haven't already specified [a default zone or region for `gcloud`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/managing-clusters#before_you_begin), you might also need to specify a `--region` or `--zone` flag when running this command.

  2. Make sure that the GKE metadata server is configured on the node pool where your application is running:
         
         gcloud container node-pools describe NODEPOOL_NAME \
             --cluster=CLUSTER_NAME \
             --format="value(config.workloadMetadataConfig.mode)"
         

Replace the following:

     * `NODEPOOL_NAME` with the name of your nodepool.
     * `CLUSTER_NAME` with the name of your GKE cluster.
  3. If you have a [cluster network policy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy), you must allow egress to `169.254.169.252/32` on port `988`. For clusters running GKE Dataplane V2, you must allow egress to `169.254.169.254/32` on port `80`.
         
         kubectl describe networkpolicy NETWORK_POLICY_NAME
         

Replace `NETWORK_POLICY_NAME` with the name of your GKE network policy.

  4. If your VPC network implements default-deny egress rules or custom routing appliances, confirm that outbound HTTPS traffic is allowed to Google's public Security Token Service (`sts.googleapis.com` on port `443`).

The GKE metadata server runs in the host network namespace and requires direct access to public Security Token Service endpoints to broker federated token exchanges. If egress firewall rules block this path, token requests fail with errors such as `504 Gateway Timeout` or `context deadline exceeded`.

  5. Confirm that the IAM allow policy on the target project or resource grants the required role to the Kubernetes ServiceAccount `principal://` or `principalSet://` identifier. For example, to check project-level role bindings:
         
         gcloud projects get-iam-policy PROJECT_ID \
             --flatten="bindings[].members" \
             --filter="bindings.members:workloadIdentityPools/PROJECT_ID.svc.id.goog"
         

Replace `PROJECT_ID` with your Google Cloud project ID.

The expected output contains a `principal://` or `principalSet://` binding that matches your project number, namespace, and Kubernetes ServiceAccount name:
         
         principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/NAMESPACE/sa/SERVICEACCOUNT_NAME
         




If your configuration instead [links Kubernetes ServiceAccounts to IAM service accounts](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#kubernetes-sa-to-iam), verify the following:

  1. Check that you have enabled the IAM Service Account Credentials API in the project containing the GKE cluster:

[Enable IAM Credentials API](https://console.cloud.google.com/apis/api/iamcredentials.googleapis.com/overview)

  2. Check that the Kubernetes service account is annotated correctly:
         
         kubectl describe serviceaccount \
             --namespace NAMESPACE SERVICEACCOUNT_NAME
         

Replace the following:

     * `NAMESPACE` with your GKE cluster's namespace.
     * `SERVICEACCOUNT_NAME` with the name of your Kubernetes service account.

The expected output contains an annotation similar to the following:
    
    iam.gke.io/gcp-service-account: GSA_NAME@PROJECT_ID.iam.gserviceaccount.com
    

  3. Check that the IAM service account is configured correctly:
         
         gcloud iam service-accounts get-iam-policy \
             GSA_NAME@GSA_PROJECT.iam.gserviceaccount.com
         

The expected output contains a binding similar to the following:
         
         - members:
           - serviceAccount:PROJECT_ID.svc.id.goog[NAMESPACE/SERVICEACCOUNT_NAME]
           role: roles/iam.workloadIdentityUser
         

**Note:** If a binding is missing from the expected output, it has likely been removed. To identify the principal responsible, check the `setIamPolicy` audit logs for the corresponding timestamp.



### Error: Invalid form of account ID

The following error occurs when you attempt an operation that requires an IAM service account email address, such as [manually creating a Cloud Storage signed URL](https://docs.cloud.google.com/storage/docs/access-control/signing-urls-manually):
    
    
    ERROR: Error: Invalid form of account ID test_account.svc.id.goog. Should be [Gaia ID |Email |Unique ID |] of the account
    # Multiple lines are omitted here
    command terminated with exit code 137
    

This error occurs when you use an annotation to [link Kubernetes ServiceAccounts to IAM service accounts](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#kubernetes-sa-to-iam) instead of using an IAM principal identifier to configure Workload Identity Federation for GKE.

By default, the GKE metadata server returns a value of `SERVICEACCOUNT_NAME.svc.id.goog` as the service account identifier for linked ServiceAccounts. This identifier doesn't use the IAM principal identifier syntax.

To resolve this error, add the `iam.gke.io/return-principal-id-as-email="true"` annotation to the Kubernetes ServiceAccount of the Pod:
    
    
    kubectl annotate serviceaccount SERVICEACCOUNT_NAME \
        --namespace=NAMESPACE \
        iam.gke.io/return-principal-id-as-email="true"
    

Replace the following:

  * `SERVICEACCOUNT_NAME`: the name of the Kubernetes ServiceAccount.
  * `NAMESPACE`: the namespace of the ServiceAccount.



### IAM service account access denied

Pods might fail to access a resource with Workload Identity Federation for GKE immediately after adding IAM role bindings. Access failure is more likely to occur in deployment pipelines or in declarative Google Cloud configurations where resources like IAM allow policies, role bindings, and Kubernetes Pods are created together. The following error message appears in the Pod logs:
    
    
    HTTP/403: generic::permission_denied: loading: GenerateAccessToken("SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com", ""): googleapi: Error 403: Permission 'iam.serviceAccounts.getAccessToken' denied on resource (or it may not exist).
    

This error might be caused by _access change propagation_ in IAM, which means that access changes like role grants take time to propagate across the system. For role grants, propagation usually takes about two minutes, but can sometimes take seven or more minutes. For more details, see [Access change propagation](https://docs.cloud.google.com/iam/docs/access-change-propagation).

To resolve this error, consider adding a delay before your Pods attempt to access Google Cloud resources after being created.

### DNS Resolution issues

This section describes how to identify and resolve connection errors from Pods to Google Cloud APIs that are caused by DNS resolution issues. If the steps in this section don't resolve your connection errors, see the Timeout errors at Pod startup section.

Some Google Cloud client libraries are configured to connect to the GKE and Compute Engine metadata servers by resolving the DNS name `metadata.google.internal`; for these libraries, healthy in-cluster DNS resolution is a critical dependency for your workloads to authenticate to Google Cloud services.

How you detect this problem depends on the details of your deployed application, including its logging configuration. Look for error messages that tell you to configure `GOOGLE_APPLICATION_CREDENTIALS`, tell you that your requests to a Google Cloud service were rejected because the request had no credentials, or tell you that the metadata server couldn't be found.

For example, the following error message might indicate that there's a DNS resolution issue:
    
    
    ComputeEngineCredentials cannot find the metadata server. This is likely because code is not running on Google Compute Engine
    

If you encounter problems with DNS resolution of `metadata.google.internal`, some Google Cloud client libraries can be instructed to skip DNS resolution by setting the environment variable `GCE_METADATA_HOST` to `169.254.169.254`:
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: example-pod
      namespace: default
    spec:
      containers:
      - image: debian
        name: main
        command: ["sleep", "infinity"]
        **env :**
        **- name: GCE_METADATA_HOST**
        **** value: "169.254.169.254"
    

This is the hardcoded IP address at which the metadata service is always available on Google Cloud compute platforms.

The following Google Cloud libraries are supported:

  * [Python](https://googleapis.dev/python/google-auth/latest/reference/google.auth.environment_vars.html#google.auth.environment_vars.GCE_METADATA_HOST)
  * [Java](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2)
  * [Node.js](https://docs.cloud.google.com/nodejs/docs/reference/gcp-metadata/latest#environment-variables)
  * [Golang](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/metadata/latest#cloud_google_com_go_compute_metadata_Client_GetWithContext)

By default, the Go client library connects using the IP address.




### Timeout errors at Pod start up

The GKE metadata server needs a few seconds before it can start accepting requests on a new Pod. Attempts to authenticate using Workload Identity Federation for GKE within the first few seconds of a Pod's life might fail for applications and Google Cloud client libraries configured with a short timeout.

If you encounter timeout errors try the following:

  * Update the Google Cloud client libraries that your workloads use.
  * Change the application code to wait a few seconds and retry.
  * Deploy an [initContainer](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/) that waits until the GKE metadata server is ready before running the Pod's main container.

For example, the following manifest is for a Pod with an `initContainer`:
        
        apiVersion: v1
        kind: Pod
        metadata:
          name: pod-with-initcontainer
        spec:
          serviceAccountName: SERVICEACCOUNT_NAME
          initContainers:
          - image:  gcr.io/google.com/cloudsdktool/cloud-sdk:alpine
            name: workload-identity-initcontainer
            command:
            - '/bin/bash'
            - '-c'
            - |
              curl -sS -H 'Metadata-Flavor: Google' 'http://169.254.169.254/computeMetadata/v1/instance/service-accounts/default/token' --retry 30 --retry-connrefused --retry-max-time 60 --connect-timeout 3 --fail --retry-all-errors > /dev/null && exit 0 || echo 'Retry limit exceeded. Failed to wait for metadata server to be available. Check if the gke-metadata-server Pod in the kube-system namespace is healthy.' >&2; exit 1
          containers:
          - image: gcr.io/your-project/your-image
            name: your-main-application-container
        




### Workload Identity Federation for GKE fails due to control plane unavailability

The metadata server can't return the Workload Identity Federation for GKE when the cluster control plane is unavailable. Calls to the metadata server return status code 500.

A log entry might appear similar to the following in the Logs Explorer:
    
    
    dial tcp 35.232.136.58:443: connect: connection refused
    

This behavior leads to unavailability of Workload Identity Federation for GKE.

The control plane might be unavailable on zonal clusters during cluster maintenance like rotating IPs, upgrading control plane VMs, or resizing clusters or node pools. See [Choosing a regional or zonal control plane](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/planning-scalability#choosing_a_regional_or_zonal_control_plane) to learn about control plane availability. Switching to a regional cluster eliminates this issue.

### Workload Identity Federation for GKE authentication fails in clusters using Cloud Service Mesh or OSS Istio

You might see errors similar to the following when your application starts in clusters using Cloud Service Mesh or Istio sidecars and tries to communicate with an endpoint:
    
    
    Connection refused (169.254.169.254:80)
    
    
    
    Connection timeout
    

These errors can occur when your application tries to make a network connection before the `istio-proxy` container is ready. By default, Istio and Cloud Service Mesh allow workloads to send requests as soon as the workloads start, regardless of whether the service mesh proxy workload that intercepts and redirects traffic is running. For Pods that use Workload Identity Federation for GKE, these initial requests that happen before the proxy starts might not reach the GKE metadata server. As a result, authentication to Google Cloud APIs fails. If you don't configure your applications to retry the requests, your workloads might fail.

To confirm that this issue is the cause of your errors, view your logs and check if the `istio-proxy` container has started successfully:

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs)

  2. In the query pane, enter the following query:
         
         (resource.type="k8s_container"
         resource.labels.pod_name="POD_NAME"
         textPayload:"Envoy proxy is ready" OR textPayload:"ERROR_MESSAGE")
         OR
         (resource.type="k8s_pod"
         logName:"events"
         jsonPayload.involvedObject.name="POD_NAME")
         

Replace the following:

     * `POD_NAME`: the name of the Pod with the affected workload.
     * `ERROR_MESSAGE`: the error that the application received (either `connection timeout` or `connection refused`).
  3. Click **Run query**.

  4. Review the output and check when the `istio-proxy` container became ready.

In the following example, the application tried to make a gRPC call. However, because the `istio-proxy` container was still initializing, the application received a `Connection refused` error. The timestamp next to the `Envoy proxy is ready` message indicates when the `istio-proxy` container became ready for connection requests:
         
         2024-11-11T18:37:03Z started container istio-init
         2024-11-11T18:37:12Z started container gcs-fetch
         2024-11-11T18:37:42Z Initializing environment
         2024-11-11T18:37:55Z Started container istio-proxy
         2024-11-11T18:38:06Z StatusCode="Unavailable", Detail="Error starting gRPC call. HttpRequestException: Connection refused (169.254.169.254:80)
         2024-11-11T18:38:13Z Envoy proxy is ready
         




To resolve this issue, and prevent it from recurring, use one of the following methods:

  * For Cloud Service Mesh and open source Istio:

    * Prevent application containers from sending requests until the proxy workload is ready by adding the following annotation to the `metadata.annotations` field in your Pod specification:
          
          proxy.istio.io/config: '{ "holdApplicationUntilProxyStarts": true }'
          

**Important:** The `holdApplicationUntilProxyStarts` configuration option applies only to application containers. It does not prevent `initContainers` or other Kubernetes sidecars from sending requests before the proxy is ready. For example, in GKE versions 1.29 and later, the Cloud Storage FUSE sidecar runs as an initContainer and might fail to authenticate if the proxy is not ready. For these workloads, you must exclude the GKE metadata server IP address from redirection using the `traffic.sidecar.istio.io/excludeOutboundIPRanges` annotation.
    * Exclude the GKE metadata server IP address from redirection by adding the following annotation to the `metadata.annotations` field of your Pod specification to configure Istio or Cloud Service Mesh to exclude `169.254.169.254/32` from redirection:
          
          traffic.sidecar.istio.io/excludeOutboundIPRanges: 169.254.169.254/32
          

  * For open source Istio only, you can optionally mitigate this issue for all Pods in the cluster by setting one of the following global configuration options:

**Note:** The `global.proxy.*` configuration option is not available with managed Cloud Service Mesh.
    * Exclude the GKE metadata server IP address from redirection by updating the `global.proxy.excludeIPRanges` global configuration option to add the `169.254.169.254/32` IP address range.

    * Prevent applications from sending requests until the proxy starts by adding the [`global.proxy.holdApplicationUntilProxyStarts`](https://istio.io/latest/docs/reference/config/istio.mesh.v1alpha1/#ProxyConfig) global configuration option with a value of `true` to your Istio configuration. This option doesn't apply to `initContainers`. If you have `initContainers` that need to authenticate, use the `global.proxy.excludeIPRanges` option instead.




### `gke-metadata-server` Pod is crashing

The `gke-metadata-server` system DaemonSet Pod facilitates Workload Identity Federation for GKE on your nodes. The Pod uses memory resources proportional to the number of Kubernetes service accounts in your cluster.

The following issue occurs when the resource usage of the `gke-metadata-server` Pod exceeds its limits. The kubelet evicts the Pod with an out of memory error. You might have this issue if your cluster has more than 3,000 Kubernetes service accounts.

To identify the issue, do the following:

  1. Find crashing `gke-metadata-server` Pods in the `kube-system` namespace:
         
         kubectl get pods -n=kube-system | grep CrashLoopBackOff
         

The output is similar to the following:
         
         NAMESPACE     NAME                        READY     STATUS             RESTARTS   AGE
         kube-system   gke-metadata-server-8sm2l   0/1       CrashLoopBackOff   194        16h
         kube-system   gke-metadata-server-hfs6l   0/1       CrashLoopBackOff   1369       111d
         kube-system   gke-metadata-server-hvtzn   0/1       CrashLoopBackOff   669        111d
         kube-system   gke-metadata-server-swhbb   0/1       CrashLoopBackOff   30         136m
         kube-system   gke-metadata-server-x4bl4   0/1       CrashLoopBackOff   7          15m
         

  2. Describe the crashing Pod to confirm that the cause was an out-of-memory eviction:
         
         kubectl describe pod POD_NAME --namespace=kube-system | grep OOMKilled
         

Replace `POD_NAME` with the name of the Pod to check.




To restore functionality to the GKE metadata server, reduce the number of service accounts in your cluster to less than 3,000.

### Workload Identity Federation for GKE fails to enable with DeployPatch failed error message

GKE uses the Google Cloud-managed [Kubernetes Engine Service Agent](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/service-accounts#gke-service-agents) to facilitate Workload Identity Federation for GKE in your clusters. Google Cloud automatically grants this service agent the Kubernetes Engine Service Agent role (`roles/container.serviceAgent`) on your project when you enable the Kubernetes Engine API.

If you try to enable Workload Identity Federation for GKE on clusters in a project where the service agent doesn't have the Kubernetes Engine Service Agent role, the operation fails with an error message similar to the following:
    
    
    Error waiting for updating GKE cluster workload identity config: DeployPatch failed
    

To resolve this issue, try the following steps:

  1. Check whether the service agent exists in your project and is configured correctly:
         
         gcloud projects get-iam-policy PROJECT_ID \
             --flatten=bindings \
             --filter=bindings.role=roles/container.serviceAgent \
             --format="value[delimiter='\\n'](bindings.members)"
         

Replace `PROJECT_ID` with your Google Cloud project ID.

If the service agent is configured correctly, the output shows the full identity of the service agent:
         
         serviceAccount:service-PROJECT_NUMBER@container-engine-robot.iam.gserviceaccount.com
         

If the output doesn't display the service agent, you must grant it the Kubernetes Engine Service Agent role. To grant this role, complete the following steps.

  2. Get your Google Cloud project number:
         
         gcloud projects describe PROJECT_ID \
             --format="value(projectNumber)"
         

The output is similar to the following:
         
         123456789012
         

  3. Grant the service agent the role:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:service-PROJECT_NUMBER@container-engine-robot.iam.gserviceaccount.com \
             --role=roles/container.serviceAgent \
             --condition=None
         

Replace `PROJECT_NUMBER` with your Google Cloud project number.

  4. Try to enable Workload Identity Federation for GKE again.




## What's next

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further help, including advice on the following topics:

    * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
    * Getting support from the community by [asking questions on StackOverflow](http://stackoverflow.com/questions/tagged/google-kubernetes-engine) and using the `google-kubernetes-engine` tag to search for similar issues. You can also join the [`#kubernetes-engine` Slack channel](https://googlecloud-community.slack.com/messages/C0B9GKTKJ/) for more community support.
    * Opening issues or feature requests by using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
