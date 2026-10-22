---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/image-pulls/
title: Troubleshoot image pulls \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:08:54.047989+00:00
---

# Troubleshoot image pulls  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/image-pulls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Troubleshoot image pulls Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

When containers fail to start in Google Kubernetes Engine (GKE), you might see Pod statuses like `ErrImagePull` or `ImagePullBackOff`. The cause of these statuses is often an issue with the image pull process, where Kubernetes attempts to retrieve the container image from a registry. A failure in this process can prevent your apps from starting or cause deployment delays.

**Note:** If you use Image streaming, see [Troubleshoot Image streaming](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/image-streaming#troubleshooting) for advice instead.

Use this page to diagnose and resolve the most common causes of image pull failures:

  * **Authentication settings** : your cluster lacks the necessary permissions to access the container image registry.
  * **Network connectivity** : your cluster cannot connect to the registry due to DNS problems, firewall rules, or lack of internet access in clusters that use network isolation.
  * **Image not found in registry** : the specified image name or tag is incorrect, the image has been deleted, or the registry is unavailable.
  * **Performance limitations** : large image size, slow disk I/O, or network congestion can cause slow pulls or timeouts.
  * **Incompatible image architecture** : the image was built for a different CPU architecture than your GKE node pool.
  * **Incompatible schema versions** : you might be using containerd 2.0 or later with a v1 Docker schema, which isn't supported.



This information is important for Application developers who need to resolve deployment failures by verifying image names, tags, and architectures in their manifests. It also helps Platform admins and operators debug cluster-level problems, such as configuring image pull credentials for private registries or fixing network policies that block access to an image registry. For more information about the common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

If you've already seen a specific event message, search this page for the message and follow the listed troubleshooting steps. If you haven't seen a message, work through the following sections in order. If the problem persists, [contact Cloud Customer Care](https://docs.cloud.google.com/support/docs/customer-care-procedures).

## Understand image pulls

Before you begin troubleshooting, it helps to understand a little more about the lifecycle of an image and where you can host your images.

### Image lifecycle

When you create a Pod, the kubelet receives the Pod definition, which includes the specification for the image. The kubelet needs this image so that it can run a container based on the image. Before pulling the image, the kubelet checks the container runtime to see if the image is present. The kubelet also checks the [image pull policy](https://kubernetes.io/docs/concepts/containers/images/#image-pull-policy) of the Pod. If the image isn't in the cache of the container runtime, or if the image pull policy requires it, then the kubelet directs the container runtime (containerd) to pull the specified image from the registry. A failed image pull prevents the container in the Pod from starting.

After a successful image pull, the container runtime unpacks the image to create a read-only base file system for the container. The container runtime stores this image and the image remains present as long as running containers reference it. If no running containers reference an image, the image becomes eligible for [garbage collection](https://kubernetes.io/docs/concepts/architecture/garbage-collection/#containers-images) and the kubelet eventually removes it.

### Image hosting options

We recommend that you use one of the following options to host your images:

  * **Artifact Registry** : Artifact Registry is Google's fully managed package manager. Artifact Registry closely integrates with other Google Cloud services and offers fine-grained access control. To learn more, see [Work with container images](https://docs.cloud.google.com/artifact-registry/docs/docker) in the Artifact Registry documentation.

**Note:** Image pulls from Artifact Registry by the kubelet don't use Workload Identity Federation for GKE. Instead, these image pulls use the service account associated with the VM.
  * **Self-hosted registry** : a self-hosted registry offers you more control, but it also requires you to manage the registry. Consider this option if you have specific compliance or security needs that Artifact Registry can't meet.




**Caution:** Container Registry is deprecated. Effective March 18, 2025, Container Registry is shut down, and writing images to Container Registry is unavailable. For details on the deprecation and how to migrate to Artifact Registry, see [Container Registry deprecation](https://docs.cloud.google.com/container-registry/docs/deprecations/container-registry-deprecation).

## Diagnose image pull failure

To diagnose image pull failures, perform the investigations detailed in the following sections:

  1. View Pod status and events.
  2. Understand status meaning.
  3. Use event messages to find the cause of image pull failure.
  4. View Logs Explorer logs.



### View Pod status and events

To help you verify that an image pull failed, GKE records the following statuses for Pods:

  * `ImagePullBackOff`
  * `ErrImagePull`
  * `ImageInspectError`
  * `InvalidImageName`
  * `RegistryUnavailable`
  * `SignatureValidationFailed`



`ImagePullBackOff` and `ErrImagePull` are the most common of these statuses.

In addition to these statuses, Kubernetes events help you find the cause of image pull failures.

To confirm if your image pull is failing, check for status messages and then read event messages by selecting one of the following options:

### Console

Complete the following steps:

  1. In the Google Cloud console, go to the **Workloads** page.

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload)

  2. Select the workload that you want to investigate. If you're not sure which workload that you need to examine, review the **Status** column. This column indicates which workloads are experiencing issues.

  3. In the **Details** page for the workload, find the **Managed pods** section and click the name of the Pod with a status indicating an image pull failure.

  4. In the **Details** page for the Pod, click the **Events** tab.

  5. Review the information in the table. The **Message** column lists Kubernetes events, which show more information about failed image pulls. The **Reason** column lists the Pod status.




### kubectl

Complete the following steps:

  1. View the status of your Pods:
         
         kubectl get pods -n NAMESPACE
         

Replace `NAMESPACE` with the namespace that your Pods run in.

The output is similar to the following:
         
         NAME         READY   STATUS       RESTARTS      AGE
         POD_NAME_1   2/2     Running      0             7d5h
         POD_NAME_2   0/1     ErrImagePull 0             7d5h
         

The `Status` column indicates which Pods have experienced an image pull failure.

  2. View events for Pods with image pull failures:
         
         kubectl describe pod POD_NAME -n NAMESPACE
         

Replace `POD_NAME` with the name of the Pod that you identified in the previous step.

The `Events` section shows more information about what happened during any failed image pulls.

The output is similar to the following:
         
         ...
         Events:
           Type    Reason    Age               From           Message
           ----    ------    ----              ----           -------
           Warning  Failed   5m (x4 over 7m)   kubelet, NODE  Failed to pull image "IMAGE_ADDRESS": rpc error: code = Unknown desc = Error response from daemon: repository IMAGE_ADDRESS not found
           Warning  Failed   5m (x4 over 7m)   kubelet, NODE  Error: ErrImagePull
           Normal   BackOff  5m (x6 over 7m)   kubelet, NODE  Back-off pulling image "IMAGE_ADDRESS"
           Warning  Failed   2m (x20 over 7m)  kubelet, NODE  Error: ImagePullBackOff
         

In this output, `IMAGE_ADDRESS` is the full address of the image. For example, `us-west1-docker.pkg.dev/my-project/my-repo/test:staging`.




### Understand status meaning

To better understand what the different statuses mean, see the following descriptions:

  * `ImagePullBackOff`: the kubelet failed to pull the image, but it will keep retrying with an increasing delay (or _backoff_) of up to five minutes.
  * `ErrImagePull`: a general, non-recoverable, error during the image pull process.
  * `ImageInspectError`: the container runtime encountered a problem when trying to inspect the container image.
  * `InvalidImageName`: the name of the container image specified in your Pod definition isn't valid.
  * `RegistryUnavailable`: the registry isn't accessible. This is typically a network connectivity issue.
  * `SignatureValidationFailed`: the digital signature of the container image couldn't be verified.



### Use event messages to find the cause of image pull failure

The following table lists event messages that relate to image pull failures and the troubleshooting steps that you should follow if you find one of these messages.

Messages that relate to image pull failures often have the following prefix:
    
    
    Failed to pull image "IMAGE_ADDRESS": rpc error: code = CODE = failed to pull and unpack image "IMAGE_ADDRESS": failed to resolve reference "IMAGE_ADDRESS":
    

This message includes the following values:

  * `IMAGE_ADDRESS`: the full address of the image. For example, `us-west1-docker.pkg.dev/my-project/my-repo/test:staging`.
  * `CODE`: an error code associated with the log message. For example, `NotFound` or `Unknown`.



Some causes of image pull failures don't have a related event message. If you don't see any of the event messages in the following table, but still experience image pull issues, we recommend that you continue reading the rest of the page.

Event message | Detailed troubleshooting  
---|---  
Authentication  
  
  * `Failed to authorize: failed to fetch oauth token: unexpected status: 403 Forbidden`
  * `Pulling from host HOST_NAME failed with status code: 403 Forbidden`

| 

  * Verify access to the image
  * Verify VPC Service Controls settings to access Artifact Registry

  
  
  * `Failed to authorize: failed to fetch oauth token: unexpected status: 401 Unauthorized`
  * `Unexpected status code [manifests 1.0]: 401 Unauthorized`

| 

  * Verify the node service account active status
  * Verify the node's access scope for private Artifact Registry repository

  
Network connectivity  
  
  * `Failed to do request: Head "IMAGE_ADDRESS": dial tcp: lookup gcr.io on REGISTRY_IP_ADDRESS: server misbehaving`

| 

  * Investigate DNS resolution

  
  
  * `Failed to start Download and install k8s binaries and configurations`

| 

  * Investigate your firewall configuration

  
  
  * `Failed to do request: Head "IMAGE_ADDRESS": dial tcp REGISTRY_IP_ADDRESS: i/o timeout`

| 

  * Investigate internet connectivity of external registry endpoints
  * Investigate whether the connection to Google APIs is timing out

  
Image not found  
  
  * `"IMAGE_ADDRESS": not found`
  * `Failed to copy: httpReadSeeker: failed open: could not fetch content descriptor sha256:SHA_HASH (application/vnd.docker.container.image.v1+json) from remote: not found`

| 

  * Investigate why the kubelet can't find your image

  
Image timeout  
  
  * `Unknown desc = context canceled`

| 

  * Investigate why there are image pull timeouts or slow image pulls

  
Incompatible schema  
  
  * `Failed to get converter for "IMAGE_ADDRESS": Pulling Schema 1 images have been deprecated and disabled by default since containerd v2.0. As a workaround you may set an environment variable `CONTAINERD_ENABLE_DEPRECATED_PULL_SCHEMA_1_IMAGE=1`, but this will be completely removed in containerd v2.1.`

| 

  * Verify image schema version compatibility

  
  
### View Logs Explorer logs

To examine historical image pull events or correlate image pull failures with other component activity, view logs with Logs Explorer:

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs)

  2. In the query pane, enter the following query:
         
         log_id("events")
         resource.type="k8s_pod"
         resource.labels.cluster_name="CLUSTER_NAME"
         jsonPayload.message=~"Failed to pull image"
         

Replace `CLUSTER_NAME` with the name of the cluster that the Pod with image pull errors runs on.

  3. Click **Run query** and review the results.




## Investigate authentication settings

The following sections help you to verify that your GKE environment has the proper authentication settings to pull images from the repository.

To check whether you have authentication issues causing an image pull issue, perform the investigations detailed in the following sections:

  1. Verify access to the image.
  2. Verify imagePullSecret configuration and Deployment specification.
  3. Verify the node service account active status.
  4. Verify the node's access scope for private Artifact Registry repository
  5. Verify VPC Service Controls settings to access Artifact Registry.



### Verify access to the image

If you encounter a `403 Forbidden` image pull error, verify that required components can access the container image.

The method to verify and apply the necessary roles to grant the required access differs depending on what type of repository stores your images. To verify and grant access, select one of the following options:

###  Artifact Registry 

If you use an imagePullSecret, the service account linked with the Secret needs read permission to the repository. Otherwise, the [node pool's service account](https://docs.cloud.google.com/artifact-registry/docs/access-control#gke) needs permission.

  1. Follow the instructions in the IAM documentation to [view the roles assigned to your service account](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts#view-access).
  2. If your service account doesn't have the [Artifact Registry Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.reader) (`roles/artifactregistry.reader`) IAM role, grant it:
         
         gcloud artifacts repositories add-iam-policy-binding REPOSITORY_NAME \
             --location=REPOSITORY_LOCATION \
             --member=serviceAccount:SERVICE_ACCOUNT_EMAIL \
             --role="roles/artifactregistry.reader"
         

Replace the following:

     * `REPOSITORY_NAME`: the name of your Artifact Registry repository.
     * `REPOSITORY_LOCATION`: the [region](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of your Artifact Registry repository.
     * `SERVICE_ACCOUNT_EMAIL`: the email address of the required service account. If you don't know the address, list all service account email addresses in your project by using the `gcloud iam service-accounts list` command.



###  Container Registry 

If you use an imagePullSecret, the service account linked with the Secret needs read permission to the repository. Otherwise, the [node pool's service account](https://docs.cloud.google.com/artifact-registry/docs/access-control#gke) needs permission.

  1. Follow the instructions in the IAM documentation to [view the roles assigned to your service account](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts#view-access).
  2. If your service account doesn't have the [Storage Object Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.objectViewer`) IAM role, grant it so that the service account can read from the bucket:
         
         gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME \
             --member=serviceAccount:SERVICE_ACCOUNT_EMAIL \
             --role=roles/storage.objectViewer
         

Replace the following:

     * `SERVICE_ACCOUNT_EMAIL`: the email of the required service account. You can list all the service accounts in your project by using the `gcloud iam service-accounts list` command.
     * `BUCKET_NAME`: the name of the Cloud Storage bucket that contains your images. You can list all the buckets in your project by using the `gcloud storage ls` command.



If your registry administrator set up [`gcr.io` repositories in Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/transition/setup-gcr-repo) to store images for the `gcr.io` domain instead of Container Registry, you must grant read access to Artifact Registry instead of Container Registry.

### Self-hosted registry

Depending on how you configured your self-hosted registry, you might need keys, certificates, or both to access the image.

If you use keys, use an imagePullSecret. imagePullSecrets are a secure way to provide your cluster with the credentials it requires to access a self-hosted registry. For an example that shows you how to configure an imagePullSecret, see [Pull an Image from a Private Registry](https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/) in the Kubernetes documentation.

To secure the HTTPS connection to your registry, you might also need certificates, which verify the integrity of the connection to the remote server. We recommend that you use Secret Manager to manage your own self-signed Certificate Authority. To learn more, see [Access private registries with private CA certificates](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/access-private-registries-private-certificates).

### Verify imagePullSecret configuration and Deployment specification

If you use an imagePullSecret, make sure that you created a Secret that holds the authentication credentials for pulling images and that all Deployments specify the Secret that you defined. For more information, see [Specifying imagePullSecrets on a Pod](https://kubernetes.io/docs/concepts/containers/images/#specifying-imagepullsecrets-on-a-pod) in the Kubernetes documentation.

### Verify the node service account active status

If you encounter a `401 Unauthorized` image pull error, verify that the node service account is active. Even if permissions are correctly configured, a disabled account will manifest this error. To verify the active status of the node service account, select one of the following options:

### Console

  1. Find the name of the service account that your nodes use:

     1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/kubernetes/list/overview)

     2. In the cluster list, click the name of the cluster that you want to inspect.

     3. Find the name of the node service account.

        * For Autopilot mode clusters, in the **Security** section, find the **Service account** field.
        * For Standard mode clusters, do the following:
        1. Click the **Nodes** tab.
        2. In the **Node pools** table, click a node pool name. The **Node pool details** page opens.
        3. In the **Security** section, find the **Service account** field.

If the value in the **Service account** field is `default`, your nodes use the Compute Engine default service account. If the value in this field is _not_ `default`, your nodes use a custom service account.

  2. Check if the node service account is disabled:

     1. In the Google Cloud console, go to the **Service accounts** page.

[Go to Service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

     2. Select a project.

     3. Look for the service account name that you identified in the previous step.

     4. Check the **Status** column for that account. If the service account is disabled, the account has a status of `Disabled`.




###  gcloud 

  1. Find the name of the service account that your nodes use:

     * For Autopilot mode clusters, run the following command:
    
    gcloud container clusters describe CLUSTER_NAME \
        --location=LOCATION \
        --flatten=autoscaling.autoprovisioningNodePoolDefaults.serviceAccount
    

     * For Standard mode clusters, run the following command:
    
    gcloud container clusters describe CLUSTER_NAME \
        --location=LOCATION \
        --format="table(nodePools.name,nodePools.config.serviceAccount)"
    

If the output is `default`, your nodes use the Compute Engine default service account. If the output is _not_ `default`, your nodes use a custom service account.

  2. Check if the node service account is disabled:
         
         gcloud iam service-accounts list --filter="email:SERVICE_ACCOUNT_NAME AND disabled:true" \
         --project=PROJECT_ID
         

If the command returns an output, the service account is disabled.




If the service account is disabled, then [enable the node service account](https://docs.cloud.google.com/iam/docs/service-accounts-disable-enable#enabling).

### Verify the node's access scope for private Artifact Registry repository

If you store your container image in a private Artifact Registry repository, your node might not have the correct access scope. When this happens, you might notice a `401 Unauthorized` image pull error.

To verify the access scope and grant it if needed, follow these steps:

  1. Identify the node running the Pod:
         
         kubectl describe pod POD_NAME | grep "Node:"
         

Replace `POD_NAME` with the name of the Pod that experiences an image pull failure.

  2. Verify that the node you identified in the previous step has the correct storage scope:
         
         gcloud compute instances describe NODE_NAME \
             --zone="COMPUTE_ZONE" \
             --format="flattened(serviceAccounts[].scopes)"
         

Replace the following:

     * `NODE_NAME`: the name of the node you identified in the previous step.
     * `COMPUTE_ZONE`: the [Compute Engine zone](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) that the node belongs to.

The output should contain at least one of the following access scopes:

     * `serviceAccounts[0].scopes[0]: https://www.googleapis.com/auth/devstorage.read_only`
     * `serviceAccounts[0].scopes[0]: https://www.googleapis.com/auth/cloud-platform`

If the node doesn't contain one of these scopes, the image pull fails.

  3. Recreate the node pool that the node belongs to with sufficient scope. Because you can't modify existing nodes, you must recreate the node with the correct scope.

We recommend that you create the node pool with the `gke-default` scope. This scope provides access to the following scopes:

     * `https://www.googleapis.com/auth/devstorage.read_only`
     * `https://www.googleapis.com/auth/logging.write`
     * `https://www.googleapis.com/auth/monitoring`
     * `https://www.googleapis.com/auth/service.management.readonly`
     * `https://www.googleapis.com/auth/servicecontrol`
     * `https://www.googleapis.com/auth/trace.append`

If the `gke-default` scope isn't suitable, grant the node pool the `devstorage.read_only` scope, which allows access to only read data.

### `gke-default`

Create a node pool with the `gke-default` scope:
    
    gcloud container node-pools create NODE_POOL_NAME \
        --cluster=CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --scopes="gke-default"
    

Replace the following:

     * `NODE_POOL_NAME`: the name of the new node pool.
     * `CLUSTER_NAME`: the name of your existing cluster.
     * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.

### `devstorage.read_only`

Create a node pool with the `devstorage.read_only` scope:
    
    gcloud container node-pools create NODE_POOL_NAME \
        --cluster=CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --scopes="https://www.googleapis.com/auth/devstorage.read_only"
    

Replace the following:

     * `NODE_POOL_NAME`: the name of the new node pool.
     * `CLUSTER_NAME`: the name of your existing cluster.
     * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.




### Verify VPC Service Controls settings to access Artifact Registry

If you use [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview), make sure that service perimeters allow access to Artifact Registry. To learn more, see [Protect repositories in a service perimeter](https://docs.cloud.google.com/artifact-registry/docs/securing-with-vpc-sc) in the Artifact Registry documentation.

## Investigate network connectivity

During an image pull, network connectivity can prevent the process from completing.

To check whether network connectivity issues are causing an image pull issue, perform the investigations detailed in the following sections:

  1. Investigate DNS resolution.
  2. Investigate your firewall configuration.
  3. Investigate internet connectivity of external registry endpoints.
  4. Investigate whether the connection to Google APIs is timing out.



### Investigate DNS resolution

If you see a `server misbehaving` image pull error, DNS resolution might be the cause of the image pull failure.

To investigate issues with DNS resolution, try the following solutions:

  1. [Troubleshoot the metadata server](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/authentication#wi-dns-resolution). The node's metadata server resolves all DNS queries. Any issues that involve this server can disrupt name resolution, preventing connection to the repository and causing the image pull to fail.
  2. If you use Cloud DNS for DNS resolution, ensure that your Cloud DNS managed private zones, forwarding zones, peering zones, and response policies are correctly configured. Misconfigurations in these areas can disrupt DNS resolution. To learn more about Cloud DNS, see [Using Cloud DNS for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-dns). For advice on how to troubleshoot Cloud DNS in GKE see [Troubleshoot Cloud DNS in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/cloud-dns).
  3. If you use kube-dns for DNS resolution, make sure it's working correctly. For advice on troubleshooting kube-dns, see [Troubleshoot kube-dns in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/kube-dns).
  4. If the cluster's nodes don't have external IP addresses (which is common if you use [network isolation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation)), enable [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access) on the subnetwork used by the cluster and make sure you meet the [network requirements](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#requirements). If you use [Cloud NAT](https://docs.cloud.google.com/nat/docs/gke-example), Google Cloud enables Private Google Access automatically.



### Investigate your firewall configuration

When a problem with your firewall causes your image pull to fail, you might see the following error message:
    
    
    Failed to start Download and install k8s binaries and configurations
    

#### Diagnose issues with your firewall

If you're using a Standard cluster and you want confirm if a problem with your firewall is causing issues with image pulls, follow these steps:

**Note:** If you're using an Autopilot cluster, you can't use SSH to connect to the node. Skip this section and proceed to try the solutions for firewall issues.

  1. Use SSH to connect to the node that experiences issues:
         
         gcloud compute ssh NODE_NAME --zone=ZONE_NAME
         

Replace the following:

     * `NODE_NAME`: the name of the node.
     * `ZONE_NAME`: the [Compute Engine zone](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) that the node was created in.
  2. Send the most recent logs for the `kube-node-installation.service` and `kube-node-configuration.service` Services to text files named `kube-node-installation_status.txt` and `kube-node-configuration_status.txt`:
         
         systemctl status kube-node-installation.service > kube-node-installation_status.txt
         systemctl status kube-node-configuration.service > kube-node-configuration_status.txt
         

If these logs don't include information from when your image pull failed, generate a complete copy of the logs:
         
         sudo journalctl -u kube-node-installation.service > kube-node-installation_logs.txt
         sudo journalctl -u kube-node-configuration.service > kube-node-configuration_logs.txt
         

  3. Review the contents of the `kube-node-installation_status.txt`and `kube-node-configuration_status.txt` and files. If you see `i/o timeout` in the output, the issue is likely with your firewall.




#### Resolve issues with your firewall configuration

To resolve issues with your firewall, try the following solutions:

  1. Identify and resolve any firewall rules that are blocking network traffic. For example, you might have a rule that blocks traffic to the registry that stores your image.

     1. Access VPC Flow Logs:

        1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs)

        2. In the query pane, enter the following query:
               
               resource.type="gce_subnetwork"
               logName="projects/PROJECT_ID/logs/[compute.googleapis.com%2Fvpc_flows](http://compute.googleapis.com%2Fvpc_flows)"
               resource.labels.subnetwork_name="SUBNET_NAME",
               

Replace the following:

           * `PROJECT_ID`: the ID of your Google Cloud project.
           * `SUBNET_NAME`: the name of your subnetwork.

To learn more, see [Access flow logs by using queries](https://docs.cloud.google.com/vpc/docs/access-flow-logs#flow-logs-queries) in the VPC documentation.

     2. If you find any firewall rules that are blocking required traffic, [update them](https://docs.cloud.google.com/firewall/docs/using-firewalls#updating_firewall_rules).

  2. If the cluster's nodes don't have external IP addresses (which is common if you use [network isolation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation)), enable [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access) on the subnetwork used by the cluster and make sure you meet the [network requirements](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#requirements). If you use [Cloud NAT](https://docs.cloud.google.com/nat/docs/gke-example), Google Cloud enables Private Google Access automatically.




### Investigate internet connectivity of external registry endpoints

If your network configuration directs traffic through an external registry endpoint, that endpoint might lack internet connectivity. When the endpoint lacks access, the image pull might fail and you see an `i/o timeout` image pull error.

To check the network connectivity from the external registry endpoint to the registry, use `ping` or `traceroute`:
    
    
    ping REGISTRY_ENDPOINT
    

Or
    
    
    traceroute REGISTRY_ENDPOINT
    

Replace `REGISTRY_ENDPOINT` with the registry endpoint. This value could be a hostname or an IP address.

If you find an error with the connectivity, review VPC routes:

  1. In the Google Cloud console, go to **Routes**.

[Go to Routes](https://console.cloud.google.com/networking/routes/list)

  2. Review the **Priority** column and make sure the highest priority route is going to a source which has access to the registry. Routes with lower values take precedence.




### Investigate whether the connection to Google APIs is timing out

If you use [network isolation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation), you might experience an error where the connection to Google APIs and services time out, leading to an `i/o timeout` image pull error.

This error occurs because your nodes couldn't reach one of the following APIs when they tried to pull images from the registry:

  * `containerregistry.googleapis.com`
  * `artifactregistry.googleapis.com`



To make sure you can connect to the required APIs, try the following solutions:

  1. Enable [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access). Nodes without external IP addresses need Private Google Access to reach the external IP addresses of Google APIs and services.
  2. Use a [supported domain](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#domain-options).
  3. Review your firewall policies:

     1. In the Google Cloud console, go to Firewall policies.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

     2. Verify if you have any rules that block egress TCP traffic on port `443` to `199.36.153.4/30`, `199.36.153.8/30`, or any [IP address range used by your chosen domain](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#domain-options) for Google APIs and services. The IP address ranges `199.36.153.4/30` and `199.36.153.8/30` are used for Private Google Access and Restricted Google Access, respectively. TCP traffic on port `443` to these ranges is for accessing Google APIs and services.

If you find any of these rules, [create an egress firewall rule](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#config-firewall) to allow such traffic.

  4. If you use Artifact Registry, make sure your environment meets the [requirements](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-gke) for using Artifact Registry with network isolation.

  5. Verify that virtual IP addresses (VIPs) (`199.36.153.4/30` or `199.36.153.8/30`) have VPC routes configured:

     1. In the Google Cloud console, go to VPC networks.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

     2. In the **Name** column, click **default**.

     3. In the VPC network details page, click the **Routes** tab.

     4. Review the routes table.

If your VPC network contains a default route (destination `0.0.0.0/0` or `::0/0`) and the next hop for that route is the default internet gateway (**Network default**), use that route for the VIPs to access Google APIs and services.

If you replaced a default route with a custom route whose next hop isn't the default internet gateway, meet the routing requirements for Google APIs and services by [using custom routing](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#config-routing-custom).




## Investigate why the kubelet can't find your image

When the kubelet can't find your image, you might see an `image not found` error and experience image pull failures.

To help the kubelet find your image, try the following solutions:

  1. Review the manifest of your Pod and ensure that the name of your image and image tag are spelled correctly. Any spelling or formatting errors cause the image pull to fail.
  2. Verify that the image still exists in the registry that you stored it in. If the image has a full registry path, verify that it exists in the Docker registry that you use. If you provide only the image name, check the Docker Hub registry.
  3. If your cluster uses [network isolation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation), try the following solutions: 
     1. [Enable Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#enabling-pga).
     2. Verify that your [service perimeter is configured correctly](https://docs.cloud.google.com/artifact-registry/docs/gke-private-clusters#configure-perimeter).



## Investigate why there are image pull timeouts or slow image pulls

If you use a very large image for your GKE workload, the image pull might time out and cause a `context cancelled` error. Although images don't have a defined size limit, the `context cancelled` error often indicates that the size of the image is the cause.

You might also notice image pulls that don't fail, but take much longer than usual. If you want to have a baseline of what your regular image pull times are, review the `Successfully pulled image` log entry. For example, the following log message shows that the image pull took 30.313387996 seconds:
    
    
    Successfully pulled image "IMAGE_ADDRESS" in 30.313387996s.
    

Timeouts and slow image pulls share many of the same causes. To resolve these issues, try the following solutions:

  1. Check for outages. If you only noticed this issue during a particular timeframe, [check if there were any Google Cloud outages](https://status.cloud.google.com/).
  2. Check disk performance. Slow disk I/O can increase image pull times. Consider upgrading to Persistent Disks with SSDs (`pd-ssd`) or using larger disks for improved performance. For more advice, see [Troubleshooting issues with disk performance](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/storage#disk_performance_issues).
  3. Reduce image size. For example, you might be able to move some data from the container images to Persistent Volumes.
  4. Take advantage of image caching for fast Pod startup times. GKE caches images on nodes. During an image pull, the container runtime only downloads layers that are not already present in the cache. To maximize the effectiveness of this caching mechanism and minimize image pull times, structure your Dockerfile to put frequently changing parts of the image (like your application code) towards the end of the file and use smaller base images.
  5. Enable Image streaming. This feature can speed up Pod startup and image downloads. To learn more, see [Use Image streaming to pull container images](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/image-streaming).
  6. Ensure the default service account has the necessary permissions. Modifying roles that are assigned to the default service account can disrupt workloads, including image pulls. For more advice, see [Identify clusters with node service accounts that are missing critical permissions](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/logging#identify-fix-permissions-in-all-clusters).
  7. Examine proxy configurations. If a proxy exists between your GKE cluster and a non-Google managed repository, it could introduce latency.
  8. Check third-party software. Some third-party software can interfere with image pulls. Investigate if any recently installed tools might be causing conflicts.



## Verify that the image manifest uses the right architecture

If the image that you're trying to pull was built for a different computer architecture than the one that your node pools use, the image pull fails.

To confirm whether your image manifest uses the right architecture, follow these steps:

  1. To confirm which architecture your image uses, view the manifest for your image. For example, to view a Docker image, run the following command:
         
         docker manifest inspect --verbose IMAGE_NAME
         

Replace `IMAGE_NAME` with the name of the image you want to view.

The output is similar to the following:
         
         ...
         "Platform": {
                   "architecture": "amd64",
                   "os": "linux"
           }
         ...
         

In this example, the supported architecture is `amd64`.

  2. Review the machine type that your node pools use:
         
         gcloud container node-pools list --cluster CLUSTER_NAME --location CONTROL_PLANE_LOCATION
         

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster that the Pod with image pull errors runs on.
     * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.

The output is similar to the following:
    
    NAME: example-node-pool
    MACHINE_TYPE: e2-standard-2
    DISK_SIZE_GB: 100
    NODE_VERSION: 1.30.8-gke.1162000
    

In this example, the machine type is `e2-standard-2`.

  3. Compare the values in the `architecture` and `MACHINE_TYPE` fields and make sure that both values are compatible. For example, if the image has a `amd64` architecture, it would be compatible with a node pool that uses `e2-standard-2` as its machine type. However, if the node pool used `t2a-standard-1` (an Arm based machine type), this machine type would cause a failure.

  4. If the image's architecture isn't compatible with the node pool's machine type, rebuild the image to target the required architecture.




## Verify image schema version compatibility

Using containerd 2.0 with a v1 Docker schema image causes image pulls to fail because containerd 2.0 removed support for pulling Docker Schema 1 images in GKE 1.33. When this issue is the cause of your image pull failure, you might see the following error message:
    
    
    Failed to get converter for "IMAGE_ADDRESS": Pulling Schema 1 images have been deprecated and disabled by default since containerd v2.0. As a workaround you may set an environment variable `CONTAINERD_ENABLE_DEPRECATED_PULL_SCHEMA_1_IMAGE=1`, but this will be completely removed in containerd v2.1.
    

To resolve this issue, identify and migrate these images by following the instructions in [Migrate from Docker Schema 1 images](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/migrate-containerd-2#migrate-schema-1).

## What's next

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further help, including advice on the following topics:

    * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
    * Getting support from the community by [asking questions on StackOverflow](http://stackoverflow.com/questions/tagged/google-kubernetes-engine) and using the `google-kubernetes-engine` tag to search for similar issues. You can also join the [`#kubernetes-engine` Slack channel](https://googlecloud-community.slack.com/messages/C0B9GKTKJ/) for more community support.
    * Opening issues or feature requests by using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
