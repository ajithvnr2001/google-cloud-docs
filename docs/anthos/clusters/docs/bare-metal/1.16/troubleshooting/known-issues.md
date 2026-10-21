---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/known-issues/
title: Google Distributed Cloud known issues \u00a0|\u00a0 Google Distributed Cloud Virtual for Bare Metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:46:52.573044+00:00
---

# Google Distributed Cloud known issues  |  Google Distributed Cloud Virtual for Bare Metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/known-issues/

**Version 1.16**. This version is no longer supported. For information about how to upgrade to version 1.28, see [ Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) in the latest documentation. For more information about supported and unsupported versions, see the [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for Bare Metal 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal)



Send feedback 

#  Google Distributed Cloud known issues Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.16 keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/troubleshooting/known-issues)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/known-issues)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support)



This page lists all known issues for Google Distributed Cloud (software only) for bare metal, formerly known as Google Distributed Cloud. To filter the known issues by a product version or category, select your filters from the following drop-down menus. 

Select your Distributed Cloud version:

1.291.281.161.151.141.131.121.111.10

Select your problem category:

ConfigurationInstallationUpgrades and updatesOperationLogging and monitoringNetworkingSecurityReset/DeletionVM Runtime on GDC

Or, search for your issue:

Category | Identified version(s) | Issue and workaround  
---|---|---  
Installation  |  1.30.0 and 1.30.100  | 

### Cluster installation might fail when using control plane node as admin workstation with cgroup v2 enabled

If you use a control plane node as the admin workstation and cgroup v2 is enabled, the machine-init job might get stuck during a cluster installation, preventing the installation from finishing successfully. **Workaround:** The issue is fixed in version 1.30.200. If you want to use a control plane node as the admin workstation and also have cgroup v2 enabled, don't attempt to create version 1.30.0 or 1.30.100 clusters.  
Installation, Upgrades and updates  |  1.28.0 to 1.28.600 and 1.29.0 to 1.29.200  | 

###  Machine preflight check failures for check_inotify_max_user_instances and check_inotify_max_user_watches settings

During cluster installation or upgrade, the machine preflight checks related to `fs.inotify` kernel settings might fail. If you're affected by this issue, the machine preflight check log contains an error like the following: 
    
    
    Minimum kernel setting required for fs.inotify.max_user_instances is 8192. Current fs.inotify.max_user_instances value is 128. Please run "echo "fs.inotify.max_user_instances=8192" | sudo tee --append /etc/sysctl.conf" to set the correct value.

This issue occurs because the `fs.inotify max_user_instances` and `max_user_watches` values are read incorrectly from the control plane and bootstrap hosts, instead of the intended node machines.  **Workaround:**  
To work around this issue, adjust the `fs.inotify.max_user_instances` and `fs.inotify.max_user_watches` to the recommended values on all control plane and the bootstrap machines: 
    
    
    echo fs.inotify.max_user_watches=524288 | sudo tee --append /etc/sysctl.conf
    echo fs.inotify.max_user_instances=8192 | sudo tee --append /etc/sysctl.conf
    sudo sysctl -p

After the installation or upgrade operation completes, these values can be reverted, if necessary.   
Configuration, Installation, Upgrades and updates, Networking, Security | 1.15, 1.16, 1.28, 1.29 | 

### Cluster installation and upgrade fails when ipam-controller-manager is required

Cluster installation and upgrade fails when the `ipam-controller-manager` is required and your cluster is running on Red Hat Enterprise Linux (RHEL) 8.9 or higher (depending on upstream RHEL changes) with SELinux running in enforcing mode. This applies specifically when the `container-selinux` version is higher than 2.225.0.  Your cluster requires the `ipam-controller-manager` in any of the following situations: 

  * Your cluster is configured for IPv4/IPv6 dual-stack networking
  * Your cluster is configured with `clusterNetwork.flatIPv4` set to `true`
  * Your cluster is configured with the `preview.baremetal.cluster.gke.io/multi-networking: enable` annotation

Cluster installation and upgrade don't succeed when the `ipam-controller-manager` is installed.  **Workaround** Set the default context for the `/etc/kubernetes` directory on each control plane node to type `etc_t`: 
    
    
    semanage fcontext /etc/kubernetes --add -t etc_t
    semanage fcontext /etc/kubernetes/controller-manager.conf --add -t etc_t
    restorecon -R /etc/kubernetes

These commands revert the `container-selinux` change on the `/etc/kubernetes` directory.  After the cluster is upgraded to a version with the fix, undo the preceding file context change on each control plane node: 
    
    
    semanage fcontext /etc/kubernetes --delete -t etc_t
    semanage fcontext /etc/kubernetes/controller-manager.conf --delete -t etc_t
    restorecon -R /etc/kubernetes  
  
Upgrades | 1.28.0 - 1.28.500 | 

### Cluster upgrade fails with Google Cloud reachability check error

When you use `bmctl` to upgrade a cluster, the upgrade might fail with a `GCP reachability check failed` error even though the target URL is reachable from the admin workstation. This issue is caused by a bug in `bmctl` versions 1.28.0 to 1.28.500. **Workaround:** Before you run the `bmctl upgrade` command, set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to point to a valid service account key file:
    
    
    export GOOGLE_APPLICATION_CREDENTIALS=JSON_KEY_PATH
    bmctl upgrade cluster -c CLUSTER_NAME --kubeconfig ADMIN_KUBECONFIG

Setting Application Default Credentials (ADC) this way ensures that `bmctl` has the necessary credentials to access the Google API endpoint.  
Configuration, Installation, Upgrades and updates, Networking, Security | 1.15, 1.16, 1.28, 1.29 | 

### Cluster installation and upgrade fails when ipam-controller-manager is required

Cluster installation and upgrade fails when the `ipam-controller-manager` is required and your cluster is running on Red Hat Enterprise Linux (RHEL) 8.9 or higher (depending on upstream RHEL changes) with SELinux running in enforcing mode. This applies specifically when the `container-selinux` version is higher than 2.225.0.  Your cluster requires the `ipam-controller-manager` in any of the following situations: 

  * Your cluster is configured for IPv4/IPv6 dual-stack networking
  * Your cluster is configured with `clusterNetwork.flatIPv4` set to `true`
  * Your cluster is configured with the `preview.baremetal.cluster.gke.io/multi-networking: enable` annotation

Cluster installation and upgrade don't succeed when the `ipam-controller-manager` is installed.  **Workaround** Set the default context for the `/etc/kubernetes` directory on each control plane node to type `etc_t`: 
    
    
    semanage fcontext /etc/kubernetes --add -t etc_t
    semanage fcontext /etc/kubernetes/controller-manager.conf --add -t etc_t
    restorecon -R /etc/kubernetes

These commands revert the `container-selinux` change on the `/etc/kubernetes` directory.  After the cluster is upgraded to a version with the fix, undo the preceding file context change on each control plane node: 
    
    
    semanage fcontext /etc/kubernetes --delete -t etc_t
    semanage fcontext /etc/kubernetes/controller-manager.conf --delete -t etc_t
    restorecon -R /etc/kubernetes  
  
Upgrades | 1.28.0 - 1.28.500 | 

### Cluster upgrade fails with Google Cloud reachability check error

When you use `bmctl` to upgrade a cluster, the upgrade might fail with a `GCP reachability check failed` error even though the target URL is reachable from the admin workstation. This issue is caused by a bug in `bmctl` versions 1.28.0 to 1.28.500. **Workaround:** Before you run the `bmctl upgrade` command, set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to point to a valid service account key file:
    
    
    export GOOGLE_APPLICATION_CREDENTIALS=JSON_KEY_PATH
    bmctl upgrade cluster -c CLUSTER_NAME --kubeconfig ADMIN_KUBECONFIG

Setting Application Default Credentials (ADC) this way ensures that `bmctl` has the necessary credentials to access the Google API endpoint.  
Installation | 1.29 | 

### Binary Authorization issue for cluster with separate load balancer node pool

Installing a cluster with a separate load balancer node pool might fail if you [enable the Binary Authorization policy](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/binary-authorization-policy#enable_the_binary_authorization_policy_during_cluster_creation) during cluster creation. This issue happens because the creation of the GKE Identity Service Pod and other critical Pods are blocked by the Binary Authorization webhook. To determine if you're affected by this issue, complete the following steps:

  1. Identify which Pods are failing: 
         
         kubectl get pods \
             -n anthos-identity-service \
             --kubeconfig CLUSTER_KUBECONFIG

  2. Describe the failing Pod.
  3. Look for the following message in the output:
    
    admission webhook "binaryauthorization.googleapis.com" denied the
            request: failed to post request to endpoint: Post
    "https://binaryauthorization.googleapis.com/internal/projects/PROJECT_NUMBER/policy/locations/LOCATION/clusters/CLUSTER_NAME:admissionReview":
            oauth2/google: status code 400:
    {"error":"invalid_target","error_description":"The
            target service indicated by the \"audience\" parameters is invalid.
    This might either be because the pool or provider is disabled or deleted
    or because it doesn't exist."}
    

If you see the preceding message, your cluster has this issue. 
**Workaround:** To workaround this issue, complete the following steps:

  1. Cancel the cluster creation operation.
  2. Remove the `spec.binaryAuthorization` block from the cluster configuration file.
  3. Create the cluster with Binary Authorization disabled.
  4. After the installation is complete, [enable the Binary Authorization policy for an existing cluster](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/binary-authorization-policy#enable_or_disable_the_binary_authorization_policy_for_an_existing_cluster).

  
Configuration, Installation | 1.10, 1.11, 1.12, 1.13, 1.14, 1.15, 1.16, 1.28, 1.29 | 

### Mount points with SELinux enabled causing issues

If you have SELinux enabled and mount file systems to Kubernetes related directories, you might experience issues such as cluster creation failure, unreadable files, or permission issues. To determine if you're affected by this issue, run the following command: 
    
    
    ls -Z /var/lib/containerd

. If you see `system_u:object_r:unlabeled_t:s0` where you would expect to see another label, such as `system_u:object_r:container_var_lib_t:s0`, you're affected. **Workaround:** If you've recently mounted file systems to directories, make sure those directories are up to date with your SELinux configuration. You should also run the following commands on each machine before running `bmctl create cluster`:
    
    
    restorecon -R -v /var
    
    
    restorecon -R -v /etc

This one time fix will persist after the reboot but is required every time a new node with the same mount points is added. To learn more, see [Mounting File Systems](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/selinux_users_and_administrators_guide/sect-security-enhanced_linux-working_with_selinux-mounting_file_systems) in the Red Hat documentation.  
Reset/Deletion | 1.29.0 | 

### Reset user cluster fails trying to delete namespace

When running `bmctl reset cluster -c ${USER_CLUSTER}`, after all related jobs have finished, the command fails to delete the user cluster namespace. The user cluster namespace is stuck in the `Terminating` state. Eventually, the cluster reset times out and returns an error. **Workaround:** To remove the namespace and complete the user cluster reset, use the following steps:

  1. Delete the `metrics-server` Pod from the admin cluster: 
         
         kubectl delete pods -l k8s-app=metrics-server \
             -n gke-managed-metrics-server --kubeconfig ADMIN_KUBECONFIG_PATH

In this situation, the `metrics-server` Pod prevents the cluster namespace removal.
  2. In the admin cluster, force remove the finalizer in the user cluster namespace: 
         
         kubectl get ns ${USER_CLUSTER_NAMESPACE} -ojson | \
             jq '.spec.finalizers = []' | \
             kubectl replace --raw "/api/v1/namespaces/${USER_CLUSTER_NAMESPACE}/finalize" -f -

Once the finalizer is removed, the cluster namespace is removed and the cluster reset is complete.

  
Configuration, Installation, Security | 1.16.0 to 1.16.7 and 1.28.0 to 1.28.400  | 

### Binary Authorization Deployment is missing a nodeSelector

If you've enabled [Binary Authorization for Google Distributed Cloud](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/binary-authorization-policy) and are using a version of 1.16.0 to 1.16.7 or 1.28.0 to 1.28.400, you might experience an issue with where the Pods for the feature are scheduled. In these versions, the Binary Authorization Deployment is missing a `nodeSelector`, so the Pods for the feature can be scheduled on worker nodes instead of control plane nodes. This behavior doesn't cause anything to fail, but isn't intended. **Workaround:** For all affected clusters, complete the following steps:

  1. Open the Binary Authorization Deployment file: 
         
         kubectl edit -n binauthz-system deployment binauthz-module-deployment

  2. Add the following `nodeSelector` in the `spec.template.spec` block:
    
    nodeSelector:
            node-role.kubernetes.io/control-plane: ""
    

  3. Save the changes.

After the change is saved, the Pods are re-deployed only to the control plane nodes. This fix needs to be applied after every upgrade.  
Upgrades and updates | 1.28.0, 1.28.100, 1.28.200, 1.28.300 | 

### Error when upgrading a cluster to 1.28.0-1.28.300

Upgrading clusters created before version 1.11.0 to versions 1.28.0-1.28.300 might cause the lifecycle controller deployer Pod to enter an error state during upgrade. When this happens, the logs of the lifecycle controller deployer Pod have an error message similar to the following: 
    
    
    "inventorymachines.baremetal.cluster.gke.io\" is invalid: status.storedVersions[0]: Invalid value: \"v1alpha1\": must appear in spec.versions
    

**Workaround:** This issue was fixed in version 1.28.400. Upgrade to version 1.28.400 or later to resolve the issue.  If you're not able to upgrade, run the following commands to resolve the problem: 
    
    
    kubectl patch customresourcedefinitions/nodepoolclaims.baremetal.cluster.gke.io \
        --subresource status --type json \
        --patch='[{ "op": "replace", "path": "/status/storedVersions", "value": ["v1"]}]'
    
    kubectl patch customresourcedefinitions/machineclasses.baremetal.cluster.gke.io \
        --subresource status --type json \
        --patch='[{ "op": "replace", "path": "/status/storedVersions", "value": ["v1"]}]'
    
    kubectl patch customresourcedefinitions/inventorymachines.baremetal.cluster.gke.io \
        --subresource status --type json \
        --patch='[{ "op": "replace", "path": "/status/storedVersions", "value": ["v1"]}]'  
  
Logging and monitoring | 1.13.7, 1.14, 1.15, 1.16, 1.28 | 

### Incorrect project ID displayed in Logs Explorer

Sometimes cluster or container logs are tagged with a different project ID in `resource.labels.project_id` in the Logs Explorer.  This can happen when the cluster is configured to use observability `PROJECT_ONE`, which is set in the `clusterOperations.projectID` field in the cluster config. However, the `cloudOperationsServiceAccountKeyPath` in the config has a service account key from project `PROJECT_TWO`.  In such cases, all logs are routed to `PROJECT_ONE`, but `resource.labels.project_id` is labeled as `PROJECT_TWO`.  **Workaround:** Use one of the following options to resolve the issue: 

  * Use a service account from the same destination project.
  * Change the `project_id` in the service account key JSON file to the current project.
  * Change the `project_id` directly in the log filter from the Logs Explorer.

  
Networking | 1.29.0 | 

### Performance degradation for clusters using bundled load balancing with BGP

For version 1.29.0 clusters using bundled load balancing with BGP, load balancing performance can degrade as the total number of Services of type `LoadBalancer` approaches 2,000. As performance degrades, Services that are newly created either take a long time to connect or can't be connected to by a client. Existing Services continue to work, but don't handle failure modes, such as the loss of a load balancer node, effectively. These Service problems happen when the `ang-controller-manager` Deployment is terminated due to running out of memory. If your cluster is affected by this issue, Services in the cluster are unreachable and not healthy and the `ang-controller-manager` Deployment is in a `CrashLoopBackOff`. The response when listing the `ang-controller-manager` Deployments is similar to the following: 
    
    
    ang-controller-manager-79cdd97b88-9b2rd   0/1    CrashLoopBackOff   639 (59s ago)   2d10h   10.250.210.152   vm-bgplb-centos4-n1-02   <none>   <none>
    
    ang-controller-manager-79cdd97b88-r6tcl   0/1   CrashLoopBackOff   620 (4m6s ago)   2d10h   10.250.202.2     vm-bgplb-centos4-n1-11   <none>   <none>

**Workaround** As a workaround, you can increase the memory resource limit of the `ang-controller-manager` Deployment by 100MiB and remove the CPU limit:
    
    
    kubectl edit deployment ang-controller-manager -n kube-system --kubeconfig ADMIN_KUBECONFIG

Upon successfully making the changes and closing the editor you should see the following output: 
    
    
    deployment.apps/ang-controller-manager edited

To verify that the changes have been applied, inspect the manifest of the `ang-controller-manager` in the cluster: 
    
    
    kubectl get deployment ang-controller-manager \
       -n kube-system \
       -o custom-columns=NAME:.metadata.name,CPU_LIMITS:.spec.template.spec.containers[*].resources.limits.cpu,MEMORY_LIMITS:.spec.template.spec.containers[*].resources.limits.memory \
       --kubeconfig ADMIN_KUBECONFIG

The response should look similar to the following: 
    
    
    NAME                     CPU_LIMITS   MEMORY_LIMITS
    ang-controller-manager   <none>       400Mi  
  
Installation, Upgrades, Backup and Restore | 1.28.0, 1.28.100 | 

### Container Registry endpoint `gcr.io` connectivity issues can block cluster operations

Multiple cluster operations for admin clusters create a bootstrap cluster. Before creating a bootstrap cluster, `bmctl` performs a Google Cloud reachability check from the admin workstation. This check might fail due to connectivity issues with the Container Registry endpoint, `gcr.io`, and you might see an error message like the following:
    
    
            system checks failed for bootstrap machine: GCP reachability check failed: failed to reach url https://gcr.io: Get "https://cloud.google.com/artifact-registry/": net/http: request canceled (Client.Timeout exceeded while awaiting headers)
            

**Workaround** To work around this issue, retry the operation with the flag `--ignore-validation-errors`.  
Networking | 1.15, 1.16 | 

### GKE Dataplane V2 incompatible with some storage drivers

Distributed Cloud clusters use GKE Dataplane V2, which is incompatible with some storage providers. You might experience problems with stuck NFS volumes or Pods. This is especially likely if you have workloads using `ReadWriteMany` volumes backed by storage drivers that are susceptible to this issue:

  * Robin.io
  * Portworx (`sharedv4` service volumes)
  * `csi-nfs`

This list is not exhaustive. **Workaround** A fix for this issue is available for the following Ubuntu versions:

  * 20.04 LTS: Use a 5.4.0 kernel image later than `linux-image-5.4.0-166-generic`
  * 22.04 LTS: Either use a 5.15.0 kernel image later than `linux-image-5.15.0-88-generic` or use the 6.5 HWE kernel.

If you're not using one of these versions, contact [Google Support](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support).  
Logging and monitoring | 1.15, 1.16, 1.28 | 

### `kube-state-metrics` OOM in large cluster

You might notice that `kube-state-metrics` or the `gke-metrics-agent` Pod that exists on the same node as `kube-state-metrics `is out of memory (OOM). This can happen in clusters with more that 50 nodes or with many Kubernetes objects. **Workaround** To resolve this issue, update the `stackdriver` custom resource definition to use the `ksmNodePodMetricsOnly` feature gate. This feature gate makes sure that only a small number of critical metrics are exposed. To use this workaround, complete the following steps:

  1. Check the `stackdriver` custom resource definition for available feature gates: 
         
         kubectl -n kube-system get crd stackdrivers.addons.gke.io -o yaml | grep ksmNodePodMetricsOnly
                 

  2. Update the `stackdriver` custom resource definition to enable `ksmNodePodMetricsOnly`: 
         
         kind:stackdriver
         spec:
           **featureGates :
              ksmNodePodMetricsOnly: true**
                 


  
Installation | 1.28.0-1.28.200 | 

### Preflight check fails on RHEL 9.2 due to missing iptables

When installing a cluster on the Red Hat Enterprise Linux (RHEL) 9.2 operating system, you might experience a failure due to the missing `iptables` package. The failure occurs during preflight checks and triggers an error message similar to the following:
    
    
    'check_package_availability_pass': "The following packages are not available: ['iptables']"
            

RHEL 9.2 is in [Preview](https://cloud.google.com/products/#product-launch-stages) for Google Distributed Cloud version 1.28. **Workaround** Bypass the preflight check error by setting `spec.bypassPreflightCheck` to `true` on your Cluster resource.  
Operation | 1.10, 1.11, 1.12, 1.13, 1.14, 1.15, 1.16 | 

### Slow MetalLB failover at high scale

When MetalLB handles a high number of services (over 10,000), failover can take over an hour. This happens because MetalLB uses a rate limited queue that, when under high scale, can take a while to get to the service that needs to fail over. **Workaround** Upgrade your cluster to version 1.28 or later. If you're unable to upgrade, manually editing the service (for example, adding an annotation) causes the service to failover more quickly.  
Operation | 1.16.0-1.16.6, 1.28.0-1.28.200 | 

### Environment variables have to be set on the admin workstation if proxy is enabled

`bmctl check cluster` can fail due to proxy failures if you don't have the environment variables `HTTPS_PROXY` and `NO_PROXY` defined on the admin workstation. The bmctl command reports an error message about failing to call some google services, like the following example:
    
    
    [2024-01-29 23:49:03+0000] error validating cluster config: 2 errors occurred:
            * GKERegister check failed: 2 errors occurred:
            * Get "https://gkehub.googleapis.com/v1beta1/projects/baremetal-runqi/locations/global/memberships/ci-ec1a14a903eb1fc": oauth2: cannot fetch token: Post "https://oauth2.googleapis.com/token": dial tcp 108.177.98.95:443: i/o timeout
            * Post "https://cloudresourcemanager.googleapis.com/v1/projects/baremetal-runqi:testIamPermissions?alt=json&prettyPrint=false": oauth2: cannot fetch token: Post "https://oauth2.googleapis.com/token": dial tcp 74.125.199.95:443: i/o timeout

**Workaround** Manually set the `HTTPS_PROXY` and `NO_PROXY` on the admin workstation.  
Upgrades and updates | 1.28.0-gke.435 | 

### Upgrades to version 1.28.0-gke.435 might fail if `audit.log` has incorrect ownership

In some cases, the `/var/log/apiserver/audit.log` file on control plane nodes has both group and user ownership set to `root`. This file ownership setting causes upgrade failures for the control plane nodes when upgrading a cluster from version 1.16.x to version 1.28.0-gke.435. This issue only applies to clusters that were created prior to version 1.11 and that had Cloud Audit Logs disabled. Cloud Audit Logs is enabled by default for clusters at version 1.9 and higher. **Workaround** If you're unable to upgrade your cluster to version 1.28.100-gke.146, use the following steps as a workaround to complete your cluster upgrade to version 1.28.0-gke.435:

  * If Cloud Audit Logs is enabled, remove the `/var/log/apiserver/audit.log` file.
  * If Cloud Audit Logs is disabled, change `/var/log/apiserver/audit.log` ownership to the same as the parent directory, `/var/log/apiserver`.

  
Networking, Upgrades and updates | 1.28.0-gke.435 | 

### MetalLB doesn't assign IP addresses to VIP Services

Google Distributed Cloud uses MetalLB for bundled load balancing. In Google Distributed Cloud release 1.28.0-gke.435, the bundled MetalLB is upgraded to version 0.13, which introduces CRD support for `IPAddressPools`. However, because `ConfigMaps` allow any name for an `IPAddressPool`, the pool names had to be converted to a Kubernetes-compliant name by appending a hash to the end of the name of the `IPAddressPool`. For example, an `IPAddressPool` with a name `default` is converted to a name like `default-qpvpd` when you upgrade your cluster to version 1.28.0-gke.435. Since MetalLB requires a specific name of an `IPPool` for selection, the name conversion prevents MetalLB from making a pool selection and assigning IP addresses. Therefore, Services that use `metallb.universe.tf/address-pool` as an annotation to select the address pool for an IP address no longer receive an IP address from the MetalLB controller. This issue is fixed in Google Distributed Cloud version 1.28.100-gke.146. **Workaround** If you can't upgrade your cluster to version 1.28.100-gke.146, use the following steps as a workaround:

  1. Get the converted name of the `IPAddressPool`: 
         
         kubectl get IPAddressPools -n kube-system

  2. Update the affected Service to set the `metallb.universe.tf/address-pool` annotation to the converted name with the hash. For example, if the `IPAddressPool` name was converted from `default` to a name like `default-qpvpd`, change the annotation `metallb.universe.tf/address-pool: default` in the Service to `metallb.universe.tf/address-pool: default-qpvpd`.

The hash used in the name conversion is deterministic, so the workaround is persistent.  
Upgrades and updates | 1.14, 1.15, 1.16, 1.28, 1.29 | 

### Orphan pods after upgrading to version 1.14.x

When you upgrade Google Distributed Cloud clusters to version 1.14.x, some resources from the previous version aren't deleted. Specifically, you might see a set of orphaned pods like the following:
    
    
    capi-webhook-system/capi-controller-manager-xxx
    capi-webhook-system/capi-kubeadm-bootstrap-controller-manager-xxx

These orphan objects don't impact cluster operation directly, but as a best practice, we recommend that you remove them.

  * Run the following commands to remove the orphan objects: 
        
        kubectl delete ns capi-webhook-system
        kubectl delete validatingwebhookconfigurations capi-validating-webhook-configuration
        kubectl delete mutatingwebhookconfigurations capi-mutating-webhook-configuration


This issue is fixed in Google Distributed Cloud version 1.15.0 and higher.  
Installation | 1.14 | 

### Cluster creation stuck on the `machine-init` job

If you try to install Google Distributed Cloud version 1.14.x, you might experience a failure due to the `machine-init` jobs, similar to the following example output:
    
    
    "kubeadm join" task failed due to:
    error execution phase control-plane-join/etcd: error creating local etcd static pod manifest file: etcdserver: re-configuration failed due to not enough started members
    
    "kubeadm reset" task failed due to:
    panic: runtime error: invalid memory address or nil pointer dereference

  
**Workaround:** Remove the obsolete etcd member that causes the `machine-init` job to fail. Complete the following steps on a functioning control plane node:

  1. List the existing etcd members: 
         
         etcdctl --key=/etc/kubernetes/pki/etcd/peer.key \
           --cacert=/etc/kubernetes/pki/etcd/ca.crt \
           --cert=/etc/kubernetes/pki/etcd/peer.crt \
           member list

Look for members with a status of `unstarted`, as shown in the following example output: 
         
         5feb7ac839625038, started, vm-72fed95a, https://203.0.113.11:2380, https://203.0.113.11:2379, false
         99f09f145a74cb15, started, vm-8a5bc966, https://203.0.113.12:2380, https://203.0.113.12:2379, false
         bd1949bcb70e2cb5, unstarted, , https://203.0.113.10:2380, , false

  2. Remove the failed etcd member: 
         
         etcdctl --key=/etc/kubernetes/pki/etcd/peer.key \
           --cacert=/etc/kubernetes/pki/etcd/ca.crt \
           --cert=/etc/kubernetes/pki/etcd/peer.crt \
           member remove MEMBER_ID

Replace `MEMBER_ID` with the ID of the failed etcd member. In the previous example output, this ID is `bd1949bcb70e2cb5`.  
  
The following example output shows that the member has been removed: 
         
         Member bd1949bcb70e2cb5 removed from cluster  9d70e2a69debf2f


  
Networking | 1.28.0 | 

### `Cilium-operator` missing Node `list` and `watch` permissions

In Cilium 1.13, the `cilium-operator` ClusterRole permissions are incorrect. The Node `list` and `watch` permissions are missing. The `cilium-operator` fails to start garbage collectors, which results in the following issues:

  * Leakage of Cilium resources.
  * Stale identities aren't removed from BFP policy maps.
  * Policy maps might reach the 16K limit. 
    * New entries can't be added.
    * Incorrect NetworkPolicy enforcement.
  * Identities might reach the 64K limit. 
    * New Pods can't be created.

An operator that's missing the Node permissions reports the following example log message:
    
    
    2024-01-02T20:41:37.742276761Z level=error msg=k8sError error="github.com/cilium/cilium/operator/watchers/node.go:83: Failed to watch *v1.Node: failed to list *v1.Node: nodes is forbidden: User \"system:serviceaccount:kube-system:cilium-operator\" cannot list resource \"nodes\" in API group \"\" at the cluster scope" subsys=k8s

The Cilium agent reports an error message when it's unable to insert an entry into a policy map, like the following example:
    
    
    level=error msg="Failed to add PolicyMap key" bpfMapKey="{6572100 0 0 0}" containerID= datapathPolicyRevision=0 desiredPolicyRevision=7 endpointID=1313 error="Unable to update element for Cilium_policy_01313 map with file descriptor 190: the map is full, please consider resizing it. argument list too long" identity=128 ipv4= ipv6= k8sPodName=/ port=0 subsys=endpoint

  
**Workaround:** Remove the Cilium identities, then add the missing ClusterRole permissions to the operator:

  1. Remove the existing `CiliumIdentity` objects: 
         
         kubectl delete ciliumid –-all

  2. Edit the `cilium-operator` ClusterRole object: 
         
         kubectl edit clusterrole cilium-operator

  3. Add a section for `nodes` that includes the missing permissions, as shown in the following example: 
         
         - apiGroups:
           - ""
           resources:
           - nodes
           verbs:
           - get
           - list
           - watch

  4. Save and close the editor. The operator dynamically detects the permission change. You don't need to manually restart the operator.

  
Upgrades and updates | 1.15.0-1.15.7, 1.16.0-1.16.3 | 

### Transient issue encountered during the preflight check

One of the kubeadm health check tasks that runs during the upgrade preflight check might fail with the following error message:
    
    
    [ERROR CreateJob]: could not delete Job \"upgrade-health-check\" in the namespace \"kube-system\": jobs.batch \"upgrade-health-check\" not found

This error can be safely ignored. If you encounter this error that blocks the upgrade, re-run the upgrade command. If you observe this error when you run the preflight using the `bmctl preflightcheck` command, nothing is blocked by this failure. You can run the preflight check again to get the accurate preflight information.   
**Workaround:** Re-run the upgrade command, or if encountered during `bmctl preflightcheck`, re-run `preflightcheck` command.  
Operation | 1.14, 1.15.0-1.15.7, 1.16.0-1.16.3, 1.28.0 | 

### Periodic Network health check fails when a node is replaced or removed

This issue affects clusters that perform periodic network health checks after a node has been replaced or removed. If your cluster undergoes periodic health checks, the periodic network health check results in failure following the replacement or removal of a node, because the network inventory ConfigMap doesn't get updated once it's created.   
**Workaround:** The recommended workaround is to delete the inventory ConfigMap and the periodic network health check. The cluster operator automatically recreates them with the most up-to-date information. For 1.14.x clusters, run the following commands:
    
    
    kubectl delete configmap \
        $(kubectl get cronjob CLUSTER_NAME-network -o=jsonpath='{.spec.jobTemplate.spec.template.spec.volumes[?(@name=="inventory-config-volume")].configMap.name}' \
        -n CLUSTER_NAMESPACE) \
        -n CLUSTER_NAMESPACE \
        --kubeconfig ADMIN_KUBECONFIG
    kubectl delete healthchecks.baremetal.cluster.gke.io \
        CLUSTER_NAME-network -n CLUSTER_NAMESPACE \
        --kubeconfig ADMIN_KUBECONFIG

For 1.15.0 and later clusters, run the following commands:
    
    
    kubectl delete configmap \
        $(kubectl get cronjob bm-system-network -o=jsonpath='{.spec.jobTemplate.spec.template.spec.volumes[?(@.name=="inventory-config-volume")]configMap.name}' \
        -n CLUSTER_NAMESPACE) \
        -n CLUSTER_NAMESPACE \
        --kubeconfig ADMIN_KUBECONFIG
    kubectl delete healthchecks.baremetal.cluster.gke.io \
        bm-system-network -n CLUSTER_NAMESPACE \
        --kubeconfig ADMIN_KUBECONFIG  
  
Networking | 1.14, 1.15, 1.16.0-1.16.2 | 

### Network Gateway for GDC can't apply your configuration when the device name contains a period

If you have a network device that includes a period character (`.`) in the name, such as `bond0.2`, Network Gateway for GDC treats the period as a path in the directory when it runs `sysctl` to make changes. When Network Gateway for GDC checks if duplicate address detection (DAD) is enabled, the check might fail and so won't reconcile. The behavior is different between cluster versions:

  * **1.14 and 1.15** : This error only exists when you use IPv6 floating IP addresses. If you don't use IPv6 floating IP addresses, you won't notice this issue when your device names contain a period.
  * **1.16.0 - 1.16.2** : This error always exists when your device names contain a period.

  
**Workaround:** Upgrade your cluster to version 1.16.3 or later. As a workaround until you can upgrade your clusters, remove the period (`.`) from the name of the device.  
Upgrades and updates, Networking, Security | 1.16.0 | 

### Upgrades to 1.16.0 fail when `seccomp` is disabled

If `seccomp` is disabled for your cluster (`spec.clusterSecurity.enableSeccomp` set to `false`), then **upgrades** to version **1.16.0** fail. Google Distributed Cloud version 1.16 uses Kubernetes version 1.27. In Kubernetes version 1.27.0 and higher, the feature for setting `seccomp` profiles is GA and no longer uses a [feature gate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/). This Kubernetes change causes upgrades to version 1.16.0 to fail when `seccomp` is disabled in the cluster configuration. This issue is fixed in version 1.16.1 and higher clusters. If you have the `cluster.spec.clusterSecurity.enableSeccomp` field set to `false`, you can upgrade to version 1.16.1 or higher. Clusters with `spec.clusterSecurity.enableSeccomp` unset or set to `true` are not affected.  
Installation, Operation | 1.11, 1.12, 1.13, 1.14, 1.15.0-1.15.5, 1.16.0-1.16.1 | 

### containerd metadata might become corrupt after reboot when `/var/lib/containerd` is mounted

If you have optionally mounted `/var/lib/containerd`, the containerd metadata might become corrupt after a reboot. Corrupt metadata might cause Pods to fail, including system-critical Pods. To check if this issue affects you, see if an optional mount is defined in `/etc/fstab` for `/var/lib/containerd/` and has `nofail` in the mount options.   
**Workaround:** Remove the `nofail` mount option in `/etc/fstab`, or upgrade your cluster to version 1.15.6 or later.  
Operation | 1.13, 1.14, 1.15, 1.16, 1.28 | 

### Clean up stale Pods in the cluster

You might see Pods managed by a Deployment (ReplicaSet) in a `Failed` state and with the status of `TaintToleration`. These Pods don't use cluster resources, but should be deleted. You can use the following `kubectl` command to list the Pods that you can clean up:
    
    
    kubectl get pods –A | grep TaintToleration

The following example output shows a Pod with the `TaintToleration` status:
    
    
    kube-system    stackdriver-metadata-agent-[...]    0/1    TaintToleration    0

  
**Workaround:** For each Pod with the described symptoms, check the ReplicaSet that the Pod belongs to. If the ReplicaSet is satisfied, you can delete the Pods:

  1. Get the ReplicaSet that manages the Pod and find the `ownerRef.Kind` value: 
         
         kubectl get pod POD_NAME -n NAMESPACE -o yaml

  2. Get the ReplicaSet and verify that the `status.replicas` is the same as `spec.replicas`: 
         
         kubectl get replicaset REPLICA_NAME -n NAMESPACE -o yaml

  3. If the names match, delete the Pod: 
         
         kubectl delete pod POD_NAME -n NAMESPACE.


  
Upgrades | 1.16.0 | 

### etcd-events can stall when upgrade to version 1.16.0

When you upgrade an existing cluster to version 1.16.0, Pod failures related to etcd-events can stall the operation. Specifically, the upgrade-node job fails for the `TASK [etcd_events_install : Run etcdevents]` step. If you're affected by this issue, you see Pod failures like the following:

  * The `kube-apiserver` Pod fails to start with the following error: 
        
        connection error: desc = "transport: Error while dialing dial tcp 127.0.0.1:2382: connect: connection refused"

  * The `etcd-events` pod fails to start with the following error: 
        
        Error: error syncing endpoints with etcd: context deadline exceeded


  
**Workaround:** If you can't upgrade your cluster to a version with the fix, use the following temporary workaround to address the errors:

  1. Use SSH to access the control plane node with the reported errors.
  2. Edit the etcd-events manifest file, `/etc/kubernetes/manifests/etcd-events.yaml`, and remove the `initial-cluster-state=existing` flag.
  3. Apply the manifest.
  4. Upgrade should continue.

  
Networking | 1.15.0-1.15.2 | 

### CoreDNS `orderPolicy` not recognized

`OrderPolicy` doesn't get recognized as a parameter and isn't used. Instead, Google Distributed Cloud always uses `Random`. This issue occurs because the CoreDNS template was not updated, which causes `orderPolicy` to be ignored.   
**Workaround:** Update the CoreDNS template and apply the fix. This fix persists until an upgrade.

  1. Edit the existing template: 
         
         kubectl edit cm -n kube-system coredns-template

Replace the contents of the template with the following: 
         
         coredns-template: |-
           .:53 {
             errors
             health {
               lameduck 5s
             }
             ready
             kubernetes cluster.local in-addr.arpa ip6.arpa {
               pods insecure
               fallthrough in-addr.arpa ip6.arpa
             }
         {{- if .PrivateGoogleAccess }}
             import zones/private.Corefile
         {{- end }}
         {{- if .RestrictedGoogleAccess }}
             import zones/restricted.Corefile
         {{- end }}
             prometheus :9153
             forward . {{ .UpstreamNameservers }} {
               max_concurrent 1000
               {{- if ne .OrderPolicy "" }}
               policy {{ .OrderPolicy }}
               {{- end }}
             }
             cache 30
         {{- if .DefaultDomainQueryLogging }}
             log
         {{- end }}
             loop
             reload
             loadbalance
         }{{ range $i, $stubdomain := .StubDomains }}
         {{ $stubdomain.Domain }}:53 {
           errors
         {{- if $stubdomain.QueryLogging }}
           log
         {{- end }}
           cache 30
           forward . {{ $stubdomain.Nameservers }} {
             max_concurrent 1000
             {{- if ne $.OrderPolicy "" }}
             policy {{ $.OrderPolicy }}
             {{- end }}
           }
         }
         {{- end }}


  
Networking, Operation | 1.10, 1.11, 1.12, 1.13, 1.14 | 

### Network Gateway for GDC components evicted or pending due to missing priority class

Network gateway Pods in `kube-system` might show a status of `Pending` or `Evicted`, as shown in the following condensed example output:
    
    
    $ kubectl -n kube-system get pods | grep ang-node
    ang-node-bjkkc     2/2     Running     0     5d2h
    ang-node-mw8cq     0/2     Evicted     0     6m5s
    ang-node-zsmq7     0/2     Pending     0     7h

These errors indicate eviction events or an inability to schedule Pods due to node resources. As Network Gateway for GDC Pods have no PriorityClass, they have the same default priority as other workloads. When nodes are resource-constrained, the network gateway Pods might be evicted. This behavior is particularly bad for the `ang-node` DaemonSet, as those Pods must be scheduled on a specific node and can't migrate.   
**Workaround:** Upgrade to 1.15 or later. As a short-term fix, you can manually assign a [PriorityClass](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/#priorityclass) to the Network Gateway for GDC components. The Google Distributed Cloud controller overwrites these manual changes during a reconciliation process, such as during a cluster upgrade.

  * Assign the `system-cluster-critical` PriorityClass to the `ang-controller-manager` and `autoscaler` cluster controller Deployments.
  * Assign the `system-node-critical` PriorityClass to the `ang-daemon` node DaemonSet.

  
Installation, Upgrades and updates | 1.15.0, 1.15.1, 1.15.2 | 

### Cluster creation and upgrades fail due to cluster name length

Creating version 1.15.0, 1.15.1, or 1.15.2 clusters or upgrading clusters to version 1.15.0, 1.15.1, or 1.15.2 fails when the cluster name is longer than 48 characters (version 1.15.0) or 45 characters (version 1.15.1 or 1.15.2). During cluster creation and upgrade operations, Google Distributed Cloud creates a health check resource with a name that incorporates the cluster name and version:

  * For version 1.15.0 clusters, the health check resource name is `CLUSTER_NAME-add-ons-CLUSTER_VER`.
  * For version 1.15.1 or 1.15.2 clusters, the health check resource name is `CLUSTER_NAME-kubernetes-CLUSTER_VER`.

For long cluster names, the health check resource name exceeds the [Kubernetes 63 character length restriction for label names](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/), which prevents the creation of the health check resource. Without a successful health check, the cluster operation fails.  To see if you are affected by this issue, use `kubectl describe` to check the failing resource: 
    
    
    kubectl describe healthchecks.baremetal.cluster.gke.io \
        HEALTHCHECK_CR_NAME -n CLUSTER_NAMESPACE \
        --kubeconfig ADMIN_KUBECONFIG

If this issue is affecting you, the response contains a warning for a `ReconcileError` like the following: 
    
    
    ...
    Events:
      Type     Reason          Age                   From                    Message
      ----     ------          ----                  ----                    -------
      Warning  ReconcileError  77s (x15 over 2m39s)  healthcheck-controller  Reconcile error, retrying: 1 error occurred:
               * failed to create job for health check
    db-uat-mfd7-fic-hybrid-cloud-uk-wdc-cluster-02-kubernetes-1.15.1: Job.batch
    "bm-system-db-uat-mfd7-fic-hybrid-cloud-u24d5f180362cffa4a743" is invalid: [metadata.labels: Invalid
    value: "db-uat-mfd7-fic-hybrid-cloud-uk-wdc-cluster-02-kubernetes-1.15.1": must be no more than 63
    characters, spec.template.labels: Invalid value:
    "db-uat-mfd7-fic-hybrid-cloud-uk-wdc-cluster-02-kubernetes-1.15.1": must be no more than 63 characters]

**Workaround** To unblock the cluster upgrade or creation, you can bypass the healthcheck. Use the following command to patch the healthcheck custom resource with passing status: `(status: {pass: true})`
    
    
    kubectl patch healthchecks.baremetal.cluster.gke.io \
        HEALTHCHECK_CR_NAME -n CLUSTER_NAMESPACE \
        --kubeconfig ADMIN_KUBECONFIG --type=merge \
        --subresource status --patch 'status: {pass: true}'  
  
Upgrades and Updates | 1.14, 1.15 | 

### Version 1.14.0 and 1.14.1 clusters with preview features can't upgrade to version 1.15.x

If version 1.14.0 and 1.14.1 clusters have a preview feature enabled, they're blocked from successfully upgrading to version 1.15.x. This applies to preview features like the ability to create a cluster without kube-proxy, which is enabled with the following annotation in the cluster configuration file:
    
    
    preview.baremetal.cluster.gke.io/kube-proxy-free: "enable"

If you're affected by this issue, you get an error like the following during the cluster upgrade:
    
    
    [2023-06-20 23:37:47+0000] error judging if the cluster is managing itself:
    error to parse the target cluster: error parsing cluster config: 1 error
    occurred:
    
    Cluster.baremetal.cluster.gke.io "$cluster-name" is invalid:
    Annotations[preview.baremetal.cluster.gke.io/$preview-feature-name]:
    Forbidden: preview.baremetal.cluster.gke.io/$preview-feature-name feature
    isn't supported in 1.15.1 Anthos Bare Metal version

This issue is fixed in version 1.14.2 and higher clusters.   
**Workaround:** If you're unable to upgrade your clusters to version 1.14.2 or higher before upgrading to version 1.15.x, you can upgrade to version 1.15.x directly by using a bootstrap cluster:
    
    
    bmctl upgrade cluster **--use-bootstrap =true**  
  
Operation | 1.15 | 

### Version 1.15 clusters don't accept duplicate floating IP addresses

Network Gateway for GDC doesn't let you create new `NetworkGatewayGroup` custom resources that contain IP addresses in `spec.floatingIPs` that are already used in existing `NetworkGatewayGroup` custom resources. This rule is enforced by a webhook in Google Distributed Cloud clusters version 1.15.0 and higher. Pre-existing duplicate floating IP addresses don't cause errors. The webhook only prevents the creation of new `NetworkGatewayGroups` custom resources that contain duplicate IP addresses.  The webhook error message identifies the conflicting IP address and the existing custom resource that is already using it: 
    
    
    IP address exists in other gateway with name **default**

The initial documentation for advanced networking features, such as the Egress NAT gateway, doesn't caution against duplicate IP addresses. Initially, only the `NetworkGatewayGroup` resource named `default` was recognized by the reconciler. Network Gateway for GDC now recognizes all `NetworkGatewayGroup` custom resources in the system namespace. Existing `NetworkGatewayGroup` custom resources are honored, as is.   
**Workaround:** Errors happen for the creation of a new `NetworkGatewayGroup` custom resource only. To address the error:

  1. Use the following command to list `NetworkGatewayGroups` custom resources: 
         
         kubectl get NetworkGatewayGroups --kubeconfig ADMIN_KUBECONFIG \
             -n kube-system -o yaml

  2. Open existing `NetworkGatewayGroup` custom resources and remove any conflicting floating IP addresses (`spec.floatingIPs`): 
         
         kubectl edit NetworkGatewayGroups --kubeconfig ADMIN_KUBECONFIG \
             -n kube-system RESOURCE_NAME

  3. To apply your changes, close and save edited custom resources.

  
VM Runtime on GDC | 1.13.7 | 

### VMs might not start on 1.13.7 clusters that use a private registry

When you enable VM Runtime on GDC on a new or upgraded version 1.13.7 cluster that uses a private registry, VMs that connect to the node network or use a GPU might not start properly. This issue is due to some system Pods in the `vm-system` namespace getting image pull errors. For example, if your VM uses the node network, some Pods might report image pull errors like the following:
    
    
    macvtap-4x9zp              0/1   Init:ImagePullBackOff  0     70m

This issue is fixed in version 1.14.0 and higher Google Distributed Cloud clusters.  **Workaround** If you're unable to upgrade your clusters immediately, you can pull images manually. The following commands pull the macvtap CNI plugin image for your VM and push it to your private registry: 
    
    
    docker pull \
        gcr.io/anthos-baremetal-release/kubevirt/macvtap-cni:v0.5.1-gke.:21
    docker tag \
        gcr.io/anthos-baremetal-release/kubevirt/macvtap-cni:v0.5.1-gke.:21 \
        REG_HOST/anthos-baremetal-release/kubevirt/macvtap-cni:v0.5.1-gke.:21
    docker push \
        REG_HOST/anthos-baremetal-release/kubevirt/macvtap-cni:v0.5.1-gke.:21

Replace `REG_HOST` with the domain name of a host that you mirror locally.   
Installation | 1.11, 1.12 | 

### During cluster creation in the kind cluster, the gke-metric-agent pod fails to start

During cluster creation in the kind cluster, the gke-metrics-agent pod fails to start because of an image pulling error as follows:
    
    
    error="failed to pull and unpack image \"gcr.io/gke-on-prem-staging/gke-metrics-agent:1.8.3-anthos.2\": failed to resolve reference \"gcr.io/gke-on-prem-staging/gke-metrics-agent:1.8.3-anthos.2\": pulling from host gcr.io failed with status code [manifests 1.8.3-anthos.2]: 403 Forbidden"

Also, in the bootstrap cluster's containerd log, you will see the following entry:
    
    
    Sep 13 23:54:20 bmctl-control-plane containerd[198]: time="2022-09-13T23:54:20.378172743Z" level=info msg="PullImage \"gcr.io/gke-on-prem-staging/gke-metrics-agent:1.8.3-anthos.2\" " Sep 13 23:54:21 bmctl-control-plane containerd[198]: time="2022-09-13T23:54:21.057247258Z" level=error msg="PullImage \"gcr.io/gke-on-prem-staging/gke-metrics-agent:1.8.3-anthos.2\" failed" error="failed to pull and unpack image \"gcr.io/gke-on-prem-staging/gke-metrics-agent:1.8.3-anthos.2\": failed to resolve reference \"gcr.io/gke-on-prem-staging/gke-metrics-agent:1.8.3-anthos.2\": pulling from host gcr.io failed with status code [manifests 1.8.3-anthos.2]: 403 Forbidden"

You will see the following "failing to pull" error in the pod:
    
    
    gcr.io/gke-on-prem-staging/gke-metrics-agent

**Workaround** Despite the errors, the cluster creation process isn't blocked as the purpose of gke-metrics-agent pod in kind cluster is to facilitate the cluster creation success rate and for internal tracking and monitoring. Hence, you can ignore this error. **Workaround** Despite the errors, the cluster creation process isn't blocked as the purpose of gke-metrics-agent pod in kind cluster is to facilitate the cluster creation success rate and for internal tracking and monitoring. Hence, you can ignore this error.  
Operation, Networking | 1.12, 1.13, 1.14, 1.15, 1.16, 1.28 | 

### Accessing an IPv6 Service endpoint crashes the LoadBalancer Node on CentOS or RHEL

When you access a dual-stack Service (a Service that has both IPv4 and IPv6 endpoints) and use the IPv6 endpoint, the LoadBalancer Node that serves the Service might crash. This issue affects customers that use dual-stack services with CentOS or RHEL and kernel version earlier than `kernel-4.18.0-372.46.1.el8_6`. If you believe that this issue affects you, check the kernel version on the LoadBalancer Node using the `uname -a` command.   
**Workaround:** Update the LoadBalancer Node to kernel version `kernel-4.18.0-372.46.1.el8_6` or later. This kernel version is available by default in CentOS and RHEL version 8.6 and later.  
Networking | 1.11, 1.12, 1.13, 1.14.0 | 

### Intermittent connectivity issues after Node reboot

After you restart a Node, you might see intermittent connectivity issues for a NodePort or LoadBalancer Service. For example, you might have intermittent TLS handshake or connection reset errors. This issue is fixed for cluster versions 1.14.1 and higher. To check if this issue affects you, look at the `iptables` forward rules on Nodes where the backend Pod for the affected Service is running:
    
    
    sudo iptables -L FORWARD

If you see the `KUBE-FORWARD` rule before the `CILIUM_FORWARD` rule in `iptables`, you might be affected by this issue. The following example output shows a Node where the problem exists:
    
    
    Chain FORWARD (policy ACCEPT)
    target                  prot opt source   destination
    KUBE-FORWARD            all  --  anywhere anywhere                /* kubernetes forwarding rules */
    KUBE-SERVICES           all  --  anywhere anywhere    ctstate NEW /* kubernetes service portals */
    KUBE-EXTERNAL-SERVICES  all  --  anywhere anywhere    ctstate NEW /* kubernetes externally-visible service portals */
    CILIUM_FORWARD          all  --  anywhere anywhere                /* cilium-feeder: CILIUM_FORWARD */
    

  
**Workaround:** Restart the anetd Pod on the Node that's misconfigured. After you restart the anetd Pod, the forwarding rule in `iptables` should be configured correctly. The following example output shows that the `CILIUM_FORWARD` rule is now correctly configured before the `KUBE-FORWARD` rule:
    
    
    Chain FORWARD (policy ACCEPT)
    target                  prot opt source   destination
    CILIUM_FORWARD          all  --  anywhere anywhere                /* cilium-feeder: CILIUM_FORWARD */
    KUBE-FORWARD            all  --  anywhere anywhere                /* kubernetes forwarding rules */
    KUBE-SERVICES           all  --  anywhere anywhere    ctstate NEW /* kubernetes service portals */
    KUBE-EXTERNAL-SERVICES  all  --  anywhere anywhere    ctstate NEW /* kubernetes externally-visible service portals */
      
  
Upgrades and updates | 1.9, 1.10 | 

### The preview feature does not retain the original permission and owner information

The preview feature of 1.9.x cluster using bmctl 1.9.x does not retain the original permission and owner information. To verify if you are affected by this feature, extract the backed-up file using the following command:
    
    
    tar -xzvf BACKUP_FILE

**Workaround** Verify if the `metadata.json` is present and if the `bmctlVersion` is 1.9.x. If the `metadata.json` isn't present, upgrade to 1.10.x cluster and use bmctl 1.10.x to backup/restore.  
Upgrades and creates | 1.14.2 | 

### `clientconfig-operator` stuck in pending state with `CreateContainerConfigError`

If you've upgraded to or created a version 1.14.2 cluster with an OIDC/LDAP configuration, you may see the `clientconfig-operator` Pod stuck in a pending state. With this issue, there are two `clientconfig-operator` Pods, with one in a running state and the other in a pending state.  This issue applies to version 1.14.2 clusters only. Earlier cluster versions such as 1.14.0 and 1.14.1 aren't affected. This issue is fixed in version 1.14.3 and all subsequent releases, including 1.15.0 and later.   
**Workaround:** As a workaround, you can patch the `clientconfig-operator` deployment to add additional security context and ensure that the deployment is ready. Use the following command to patch `clientconfig-operator` in the target cluster: 
    
    
    kubectl patch deployment clientconfig-operator -n kube-system \
        -p '{"spec":{"template":{"spec":{"containers": [{"name":"oidcproxy","securityContext":{"runAsGroup":2038,"runAsUser":2038}}]}}}}' \
        --kubeconfig CLUSTER_KUBECONFIG

Replace the following:

  * `CLUSTER_KUBECONFIG`: the path of the kubeconfig file for the target cluster.

  
Operation | 1.11, 1.12, 1.13, 1.14, 1.15 | 

### Certificate authority rotation fails for clusters without bundled load balancing

For clusters without bundled load balancing (`spec.loadBalancer.mode` set to `manual`), the `bmctl update credentials certificate-authorities rotate` command can become unresponsive and fail with the following error: `x509: certificate signed by unknown authority`. If you're affected by this issue, the `bmctl` command might output the following message before becoming unresponsive:
    
    
    Signing CA completed in 3/0 control-plane nodes

In this case, the command eventually fails. The rotate certificate-authority log for a cluster with three control planes may include entries like the following: 
    
    
    [2023-06-14 22:33:17+0000] waiting for all nodes to trust CA bundle OK
    [2023-06-14 22:41:27+0000] waiting for first round of pod restart to complete OK
    Signing CA completed in 0/0 control-plane nodes
    Signing CA completed in 1/0 control-plane nodes
    Signing CA completed in 2/0 control-plane nodes
    Signing CA completed in 3/0 control-plane nodes
    ...
    Unable to connect to the server: x509: certificate signed by unknown
    authority (possibly because of "crypto/rsa: verification error" while
    trying to verify candidate authority certificate "kubernetes")

**Workaround** If you need additional assistance, contact [Google Support](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support).  
Installation, Networking | 1.11, 1.12, 1.13, 1.14.0-1.14.1 | 

### `ipam-controller-manager` crashloops in dual-stack clusters

When you deploy a dual-stack cluster (a cluster with both IPv4 and IPv6 addresses), the `ipam-controller-manager` Pod(s) might crashloop. This behavior causes the Nodes to cycle between `Ready` and `NotReady` states, and might cause the cluster installation to fail. This problem can occur when the API server is under high load. To see if this issue affects you, check if the `ipam-controller-manager` Pod(s) are failing with `CrashLoopBackOff` errors:
    
    
    kubectl -n kube-system get pods | grep  ipam-controller-manager

The following example output shows Pods in a `CrashLoopBackOff` state:
    
    
    ipam-controller-manager-h7xb8   0/1  CrashLoopBackOff   3 (19s ago)   2m ipam-controller-manager-vzrrf   0/1  CrashLoopBackOff   3 (19s ago)   2m1s
    ipam-controller-manager-z8bdw   0/1  CrashLoopBackOff   3 (31s ago)   2m2s
    

Get details for the Node that's in a `NotReady` state:
    
    
    kubectl describe node <node-name> | grep PodCIDRs

In a cluster with this issue, a Node has no PodCIDRs assigned to it, as shown in the following example output:
    
    
    PodCIDRs:
    

In a healthy cluster, all the Nodes should have dual-stack PodCIDRs assigned to it, as shown in the following example output:
    
    
    PodCIDRs:    192.168.6.0/24,222:333:444:555:5:4:7:0/120
    

  
**Workaround:** Restart the `ipam-controller-manager` Pod(s):
    
    
    kubectl -n kube-system rollout restart ds ipam-controller-manager  
  
Operation | 1.6, 1.7, 1.8, 1.9, 1.10, 1.11, 1.12, 1.13, and 1.14 | 

### etcd watch starvation

Clusters running etcd version 3.4.13 or earlier may experience watch starvation and non-operational resource watches, which can lead to the following problems: 

  * Pod scheduling is disrupted
  * Nodes are unable to register
  * kubelet doesn't observe pod changes

These problems can make the cluster non-functional.  This issue is fixed in Distributed Cloud version 1.12.9, 1.13.6, 1.14.3, and subsequent releases. These newer releases use etcd version 3.4.21. All prior versions of Distributed Cloud are affected by this issue.  **Workaround** If you can't upgrade immediately, you can mitigate the risk of cluster failure by reducing the number of nodes in your cluster. Remove nodes until the `etcd_network_client_grpc_sent_bytes_total` metric is less than 300 MBps.  To view this metric in Metrics Explorer:

  1. Go to the Metrics Explorer in the Google Cloud console: [Go to Metrics Explorer](https://console.cloud.google.com/monitoring/metrics-explorer)
  2. Select the **Configuration** tab.
  3. Expand the **Select a metric** , enter `Kubernetes Container` in the filter bar, and then use the submenus to select the metric: 
     1. In the **Active resources** menu, select **Kubernetes Container**. 
     2. In the **Active metric categories** menu, select **Anthos**.
     3. In the **Active metrics** menu, select `etcd_network_client_grpc_sent_bytes_total`.
     4. Click Apply.

  
Networking | 1.11.6, 1.12.3 | 

### SR-IOV operator's `vfio-pci` mode "Failed" state

The `SriovNetworkNodeState` object's `syncStatus` can report the "Failed" value for a configured node. To view the status of a node and determine if the problem affects you, run the following command:
    
    
    kubectl -n gke-operators get \
        sriovnetworknodestates.sriovnetwork.k8s.cni.cncf.io NODE_NAME \
        -o jsonpath='{.status.syncStatus}'

Replace NODE_NAME with the name of the node to check.   
**Workaround:** If the `SriovNetworkNodeState` object status is "Failed", upgrade your cluster to version 1.11.7 or later or version 1.12.4 or later.  
Upgrades and updates | 1.10, 1.11, 1.12, 1.13, 1.14.0, 1.14.1 | 

### Some worker nodes aren't in a Ready state after upgrade

Once upgrade is finished, some worker nodes may have their Ready condition set to `false`. On the Node resource, you will see an error next to the Ready condition similar to the following example:
    
    
    container runtime network not ready: NetworkReady=false reason:NetworkPluginNotReady message:Network plugin returns error: cni plugin not initialized

When you log into the stalled machine, the CNI configuration on the machine is empty:
    
    
    sudo ls /etc/cni/net.d/

**Workaround** Restart the node's `anetd` pod by deleting it.  
Upgrades and updates, Security | 1.10 | 

### Multiple certificate rotations from cert-manager result in inconsistency

After multiple manual or auto certificate rotations, the webhook pod, such as `anthos-cluster-operator` isn't updated with the new certificates issued by `cert-manager`. Any update to the cluster custom resource fails and results in an error similar as follows: 
    
    
    Internal error occurred: failed calling
    webhook "vcluster.kb.io": failed to call webhook: Post "https://webhook-service.kube-system.svc:443/validate-baremetal-cluster-gke-io-v1-cluster?timeout=10s": x509: certificate signed by unknown authority (possibly because of "x509:
    invalid signature: parent certificate cannot sign this kind of certificate"
    while trying to verify candidate authority certificate
    "webhook-service.kube-system.svc")
    

This issue might occur in the following circumstances:

  * If you have done two manual cert-manager issued certificate rotations on a cluster older than 180 days or more and never restarted the `anthos-cluster-operator`. 
  * If you have done a manual `cert-manager` issued certificate rotations on a cluster older than 90 days or more and never restarted the `anthos-cluster-operator`. 

**Workaround** Restart the pod by terminating the `anthos-cluster-operator`.  
Upgrades and updates | 1.14.0 | 

### Outdated lifecycle controller deployer pods created during user cluster upgrade

In version 1.14.0 admin clusters, one or more outdated lifecycle controller deployer pods might be created during user cluster upgrades. This issue applies for user clusters that were initially created at versions lower than 1.12. The unintentionally created pods don't impede upgrade operations, but they might be found in an unexpected state. We recommend that you remove the outdated pods.  This issue is fixed in release 1.14.1. **Workaround:** To remove the outdated lifecycle controller deployer pods:

  1. List preflight check resources: 
         
         kubectl get preflightchecks --kubeconfig ADMIN_KUBECONFIG -A

The output looks like this:
         
         NAMESPACE                    NAME                      PASS   AGE
         cluster-ci-87a021b9dcbb31c   ci-87a021b9dcbb31c        true   20d
         cluster-ci-87a021b9dcbb31c   ci-87a021b9dcbb31cd6jv6   false  20d

where ci-87a021b9dcbb31c is the cluster name.
  2. Delete resources whose value in the PASS column is either `true` or `false`. For example, to delete the resources in the preceding sample output, use the following commands:
         
         kubectl delete preflightchecks ci-87a021b9dcbb31c \
             -n cluster-ci-87a021b9dcbb31c \
             --kubeconfig ADMIN_KUBECONFIG 
         kubectl delete preflightchecks ci-87a021b9dcbb31cd6jv6 \
             -n cluster-ci-87a021b9dcbb31c \
             --kubeconfig ADMIN_KUBECONFIG


  
Networking | 1.9, 1.10, 1.11, 1.12, 1.13, 1.14, 1.15, 1.16, 1.28 | 

### `BGPSession` state constantly changing due to large number of incoming routes

Google Distributed Cloud advanced networking fails to manage BGP sessions correctly when external peers advertise a high number of routes (about 100 or more). With a large number of incoming routes, the node-local BGP controller takes too long to reconcile BGP sessions and fails to update the status. The lack of status updates, or a health check, causes the session to be deleted for being stale. Undesirable behavior on BGP sessions that you might notice and indicate a problem include the following:

  * Continuous `bgpsession` deletion and recreation.
  * `bgpsession.status.state` never becomes `Established`
  * Routes failing to advertise or being repeatedly advertised and withdrawn.

BGP load balancing problems might be noticeable with connectivity issues to `LoadBalancer` services. BGP `FlatIP` issue might be noticeable with connectivity issues to Pods. To determine if your BGP issues are caused by the remote peers advertising too many routes, use the following commands to review the associated statuses and output:

  * Use `kubectl get bgpsessions` on the affected cluster. The output shows `bgpsessions` with state "Not Established" and the last report time continuously counts up to about 10-12 seconds before it appears to reset to zero.
  * The output of `kubectl get bgpsessions` shows that the affected sessions are being repeatedly recreated: 
        
        kubectl get bgpsessions \
            -o jsonpath="{.items[*]['metadata.name', 'metadata.creationTimestamp']}"

  * Log messages indicate that stale BGP sessions are being deleted: 
        
        kubectl logs ang-controller-manager-POD_NUMBER

Replace `POD_NUMBER` with the leader pod in your cluster.

  
**Workaround:** Reduce or eliminate the number of routes advertised from the remote peer to the cluster with an export policy. In Google Distributed Cloud cluster version 1.14.2 and later, you can also disable the feature that processes received routes by using an `AddOnConfiguration`. Add the `--disable-received-routes` argument to the `ang-daemon` daemonset's `bgpd` container.  
Networking | 1.14, 1.15, 1.16, 1.28 | 

### Application timeouts caused by conntrack table insertion failures

Clusters running on an Ubuntu OS that uses kernel 5.15 or higher are susceptible to netfilter connection tracking (conntrack) table insertion failures. Insertion failures can occur even when the conntrack table has room for new entries. The failures are caused by changes in kernel 5.15 and higher that restrict table insertions based on chain length.  To see if you are affected by this issue, you can check the in-kernel connection tracking system statistics with the following command:
    
    
    sudo conntrack -S

The response looks like this:
    
    
    cpu=0       found=0 invalid=4 insert=0 insert_failed=0 drop=0 early_drop=0 error=0 search_restart=0 clash_resolve=0 chaintoolong=0
    cpu=1       found=0 invalid=0 insert=0 insert_failed=0 drop=0 early_drop=0 error=0 search_restart=0 clash_resolve=0 chaintoolong=0
    cpu=2       found=0 invalid=16 insert=0 insert_failed=0 drop=0 early_drop=0 error=0 search_restart=0 clash_resolve=0 chaintoolong=0
    cpu=3       found=0 invalid=13 insert=0 insert_failed=0 drop=0 early_drop=0 error=0 search_restart=0 clash_resolve=0 chaintoolong=0
    cpu=4       found=0 invalid=9 insert=0 insert_failed=0 drop=0 early_drop=0 error=0 search_restart=0 clash_resolve=0 chaintoolong=0
    cpu=5       found=0 invalid=1 insert=0 insert_failed=0 drop=0 early_drop=0 error=519 search_restart=0 clash_resolve=126 chaintoolong=0
    ...

If a `chaintoolong` value in the response is a non-zero number, you're affected by this issue. **Workaround** The short term mitigation is to increase the size of both the netfiler hash table (`nf_conntrack_buckets`) and the netfilter connection tracking table (`nf_conntrack_max`). Use the following commands on each cluster node to increase the size of the tables:
    
    
    sysctl -w net.netfilter.nf_conntrack_buckets=TABLE_SIZE
    
    sysctl -w net.netfilter.nf_conntrack_max=TABLE_SIZE

Replace TABLE_SIZE with new size in bytes. The default table size value is `262144`. We suggest that you set a value equal to 65,536 times the number of cores on the node. For example, if your node has eight cores, set the table size to `524288`.  
Upgrades and updates | 1.11.3, 1.11.4, 1.11.5, 1.11.6, 1.11.7, 1.11.8, 1.12.4, 1.12.5, 1.12.6, 1.12.7, 1.12.8, 1.13.4, 1.13.5 | 

### Can't restore cluster backups with `bmctl` for some versions

We recommend that you back up your clusters before you upgrade so that you can restore the earlier version if the upgrade doesn't succeed. A problem with the `bmctl restore cluster` command causes it to fail to restore backups of clusters with the identified versions. This issue is specific to upgrades, where you're restoring a backup of an earlier version. If your cluster is affected, the `bmctl restore cluster` log contains the following error:
    
    
    Error: failed to extract image paths from profile: anthos version VERSION not supported
    

**Workaround:** Until this issue is fixed, we recommend that you use the instructions in [Back up and restore clusters](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/bmctl-backup-restore) to back up your clusters manually and restore them manually, if necessary.   
Networking | 1.10, 1.11, 1.12, 1.13, 1.14.0-1.14.2 | 

### `NetworkGatewayGroup` crashes if there's no IP address on the interface

`NetworkGatewayGroup` fails to create daemons for nodes that don't have both IPv4 and IPv6 interfaces on them. This causes features like BGP LB and EgressNAT to fail. If you check the logs of the failing `ang-node` Pod in the `kube-system` namespace, errors similar to the following example are displayed when an IPv6 address is missing:
    
    
    ANGd.Setup    Failed to create ANG daemon    {"nodeName": "bm-node-1", "error":
    "creating NDP client failed: ndp: address \"linklocal\" not found on interface \"ens192\""}
    

In the previous example, there's no IPv6 address on the `ens192` interface. Similar ARP errors are displayed if the node is missing an IPv4 address. `NetworkGatewayGroup` tries to establish an ARP connection and an NDP connection to the link local IP address. If the IP address doesn't exist (IPv4 for ARP, IPv6 for NDP) then the connection fails and the daemon doesn't continue. This issue is fixed in release 1.14.3.   
**Workaround:** Connect to the node using SSH and add an IPv4 or IPv6 address to the link that contains the node IP. In the previous example log entry, this interface was `ens192`:
    
    
    ip address add dev INTERFACE scope link ADDRESS

Replace the following:

  * `INTERFACE`: The interface for your node, such as `ens192`.
  * `ADDRESS`: The IP address and subnet mask to apply to the interface.

  
Reset/Deletion | 1.10, 1.11, 1.12, 1.13.0-1.13.2 | 

### `anthos-cluster-operator` crash loop when removing a control plane node

When you try to remove a control plane node by removing the IP address from the `Cluster.Spec`, the `anthos-cluster-operator` enters into a crash loop state that blocks any other operations.   
**Workaround:** Issue is fixed in 1.13.3 and 1.14.0 and later. All other versions are affected. Upgrade to one of the fixed versions As a workaround, run the following command:
    
    
    kubectl label baremetalmachine IP_ADDRESS \
        -n CLUSTER_NAMESPACE baremetal.cluster.gke.io/upgrade-apply-

Replace the following:

  * `IP_ADDRESS`: The IP address of the node in a crash loop state.
  * `CLUSTER_NAMESPACE`: The cluster namespace.

  
Installation | 1.13.1, 1.13.2 and 1.13.3 | 

### `kubeadm join` fails in large clusters due to token mismatch

When you install Google Distributed Cloud clusters with a large number of nodes, you might see a `kubeadmin join` error message similar to the following example:
    
    
    TASK [kubeadm : kubeadm join --config /dev/stdin --ignore-preflight-errors=all] ***
    fatal: [10.200.0.138]: FAILED! => {"changed": true, "cmd": "kubeadm join
    --config /dev/stdin --ignore-preflight-errors=all", "delta": "0:05:00.140669", "end": "2022-11-01 21:53:15.195648", "msg": "non-zero return code", "rc": 1,
    "start": "2022-11-01 21:48:15.054979", "stderr": "W1101 21:48:15.082440   99570 initconfiguration.go:119]
    Usage of CRI endpoints without URL scheme is deprecated and can cause kubelet errors in the future.
    Automatically prepending scheme \"unix\" to the \"criSocket\" with value \"/run/containerd/containerd.sock\". Please update your configuration!\nerror
    execution phase preflight: couldn't validate the identity of the API Server: could not find a JWS signature in the cluster-info ConfigMap for token ID \"yjcik0\"\n
    To see the stack trace of this error execute with --v=5 or higher", "stderr_lines":
    ["W1101 21:48:15.082440   99570 initconfiguration.go:119] Usage of CRI endpoints without URL scheme is deprecated and can cause kubelet errors in the future.
    Automatically prepending scheme \"unix\" to the \"criSocket\" with value \"/run/containerd/containerd.sock\".
    Please update your configuration!", "error execution phase preflight: couldn't validate the identity of the API Server:
    could not find a JWS signature in the cluster-info ConfigMap for token ID \"yjcik0\"",
    "To see the stack trace of this error execute with --v=5 or higher"], "stdout": "[preflight]
    Running pre-flight checks", "stdout_lines": ["[preflight] Running pre-flight checks"]}
    

  
**Workaround:** This issue is resolved in Distributed Cloud version 1.13.4 and later. If you need to use an affected version, first create a cluster with less than 20 nodes, and then resize the cluster to add additional nodes after the install is complete.  
Logging and monitoring | 1.10, 1.11, 1.12, 1.13.0 | 

### Low CPU limit for `metrics-server` in Edge clusters

In Google Distributed Cloud Edge clusters, low CPU limits for `metrics-server` can cause frequent restarts of `metrics-server`. Horizontal Pod Autoscaling (HPA) doesn't work due to `metrics-server` being unhealthy. If `metrics-server` CPU limit is less than `40m`, your clusters can be affected. To check the `metrics-server` CPU limits, review one of the following files:

  * Google Distributed Cloud clusters version 1.x-1.12: 
        
        kubectl get deployment metrics-server -n kube-system \
            -o yaml > metrics-server.yaml

  * Google Distributed Cloud clusters version 1.13 or later: 
        
        kubectl get deployment metrics-server -n gke-managed-metrics-server \
            -o yaml > metrics-server.yaml


  
**Workaround:** This issue is resolved in Google Distributed Cloud clusters version 1.13.1 or later. To fix this issue, upgrade your clusters. A short-term workaround until you can upgrade clusters is to manually increase the CPU limits for `metrics-server` as follows:

  1. Scale down `metrics-server-operator`: 
         
         kubectl scale deploy metrics-server-operator --replicas=0

  2. Update the configuration and increase CPU limits: 
     * Google Distributed Cloud clusters version 1.x-1.12: 
           
           kubectl -n kube-system edit deployment metrics-server

     * Google Distributed Cloud clusters version 1.13: 
           
           kubectl -n gke-managed-metrics-server edit deployment metrics-server

Remove the `--config-dir=/etc/config` line and increase the CPU limits, as shown in the following example:
    
    [...]
    - command:
    - /pod_nanny
    # - --config-dir=/etc/config # <--- Remove this line
    - --container=metrics-server
    - --cpu=50m # <--- Increase CPU, such as to 50m
    - --extra-cpu=0.5m
    - --memory=35Mi
    - --extra-memory=4Mi
    - --threshold=5
    - --deployment=metrics-server
    - --poll-period=30000
    - --estimator=exponential
    - --scale-down-delay=24h
    - --minClusterSize=5
    - --use-metrics=true
    [...]
    

  3. Save and close the `metrics-server` to apply the changes.

  
Networking | 1.14, 1.15, 1.16 | 

### Direct NodePort connection to hostNetwork Pod doesn't work

Connection to a Pod enabled with `hostNetwork` using NodePort Service fails when the backend Pod is on the same node as the targeted NodePort. This issues affects LoadBalancer Services when used with hostNetwork-ed Pods. With multiple backends, there can be a sporadic connection failure. This issue is caused by a bug in the eBPF program.   
**Workaround:** When using a Nodeport Service, don't target the node on which any of the backend Pod runs. When using the LoadBalancer Service, make sure the hostNetwork-ed Pods don't run on LoadBalancer nodes.  
Upgrades and updates | 1.12.3, 1.13.0 | 

### 1.13.0 admin clusters can't manage 1.12.3 user clusters

Admin clusters that run version 1.13.0 can't manage user clusters that run version 1.12.3. Operations against a version 1.12.3 user cluster fail.   
**Workaround:** Upgrade your admin cluster to version 1.13.1, or upgrade the user cluster to the same version as the admin cluster.  
Upgrades and updates | 1.12 | 

### Upgrading to 1.13.x is blocked for admin clusters with worker node pools

Version 1.13.0 and higher admin clusters can't contain worker node pools. Upgrades to version 1.13.0 or higher for admin clusters with worker node pools is blocked. If your admin cluster upgrade is stalled, you can confirm if worker node pools are the cause by checking following error in the `upgrade-cluster.log` file inside the `bmctl-workspace` folder:
    
    
    Operation failed, retrying with backoff. Cause: error creating "baremetal.cluster.gke.io/v1, Kind=NodePool" cluster-test-cluster-2023-06-06-140654/np1: admission webhook "vnodepool.kb.io" denied the request: Adding worker nodepool to Admin cluster is disallowed.
    

  
**Workaround:** Before upgrading, move all worker node pools to user clusters. For instructions to add and remove node pools, see [Manage node pools in a cluster](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/add-remove-node-pools).   
Upgrades and updates | 1.10, 1.11, 1.12, 1.13, 1.14, 1.15, 1.16, 1.28 | 

### Errors when updating resources using `kubectl apply`

If you update existing resources like the `ClientConfig` or `Stackdriver` custom resources using `kubectl apply`, the controller might return an error or revert your input and planned changes. For example, you might try to edit the `Stackdriver` custom resource as follows by first getting the resource, and then applying an updated version:

  1. Get the existing YAML definition: 
         
         kubectl get stackdriver -n kube-system stackdriver \
             -o yaml > stackdriver.yaml

  2. Enable features or update configuration in the YAML file.
  3. Apply the updated YAML file back: 
         
         kubectl apply -f stackdriver.yaml


The final step for `kubectl apply` is where you might run into problems.   
**Workaround:** Don't use `kubectl apply` to make changes to existing resources. Instead, use `kubectl edit` or `kubectl patch` as shown in the following examples:

  1. Edit the `Stackdriver` custom resource: 
         
         kubectl edit stackdriver -n kube-system stackdriver

  2. Enable features or update configuration in the YAML file.
  3. Save and exit the editor

Alternate approach using `kubectl patch`:

  1. Get the existing YAML definition: 
         
         kubectl get stackdriver -n kube-system stackdriver \
             -o yaml > stackdriver.yaml

  2. Enable features or update configuration in the YAML file.
  3. Apply the updated YAML file back: 
         
         kubectl patch stackdriver stackdriver --type merge \
             -n kube-system --patch-file stackdriver.yaml


  
Logging and monitoring | 1.12, 1.13, 1.14, 1.15, 1.16 | 

### Corrupted backlog chunks cause `stackdriver-log-forwarder` crashloop

The `stackdriver-log-forwarder` crashloops if it tries to process a corrupted backlog chunk. The following example errors are shown in the container logs:
    
    
    [2022/09/16 02:05:01] [error] [storage] format check failed: tail.1/1-1659339894.252926599.flb
    [2022/09/16 02:05:01] [error] [engine] could not segregate backlog chunks
    

When this crashloop occurs, you can't see logs in Cloud Logging.   
**Workaround:** To resolve these errors, complete the following steps:

  1. Identify the corrupted backlog chunks. Review the following example error messages: 
         
         [2022/09/16 02:05:01] [error] [storage] format check failed: tail.1/1-1659339894.252926599.flb
         [2022/09/16 02:05:01] [error] [engine] could not segregate backlog chunks
         

In this example, the file `tail.1/1-1659339894.252926599.flb` that's stored in `var/log/fluent-bit-buffers/tail.1/` is at fault. Every `*.flb` file with a format check failed must be removed.
  2. End the running pods for `stackdriver-log-forwarder`: 
         
         kubectl --kubeconfig KUBECONFIG -n kube-system \
             patch daemonset stackdriver-log-forwarder \
             -p '{"spec": {"template": {"spec": {"nodeSelector": {"non-existing": "true"}}}}}'

Replace `KUBECONFIG` with the path to your user cluster kubeconfig file.  
  
Verify that the `stackdriver-log-forwarder` Pods are deleted before going to the next step.
  3. Connect to the node using SSH where `stackdriver-log-forwarder` is running.
  4. On the node, delete all corrupted `*.flb` files in `var/log/fluent-bit-buffers/tail.1/`.  
  
If there are too many corrupted files and you want to apply a script to clean up all backlog chunks, use the following scripts: 
     1. Deploy a DaemonSet to clean up all the dirty data in buffers in `fluent-bit`: 
            
            kubectl --kubeconfig KUBECONFIG -n kube-system apply -f - << EOF
            apiVersion: apps/v1
            kind: DaemonSet
            metadata:
              name: fluent-bit-cleanup
              namespace: kube-system
            spec:
              selector:
                matchLabels:
                  app: fluent-bit-cleanup
              template:
                metadata:
                  labels:
                    app: fluent-bit-cleanup
                spec:
                  containers:
                  - name: fluent-bit-cleanup
                    image: debian:10-slim
                    command: ["bash", "-c"]
                    args:
                    - |
                      rm -rf /var/log/fluent-bit-buffers/
                      echo "Fluent Bit local buffer is cleaned up."
                      sleep 3600
                    volumeMounts:
                    - name: varlog
                      mountPath: /var/log
                    securityContext:
                      privileged: true
                  tolerations:
                  - key: "CriticalAddonsOnly"
                    operator: "Exists"
                  - key: node-role.kubernetes.io/master
                    effect: NoSchedule
                  - key: node-role.gke.io/observability
                    effect: NoSchedule
                  volumes:
                  - name: varlog
                    hostPath:
                      path: /var/log
            EOF

     2. Make sure that the DaemonSet has cleaned up all the nodes. The output of the following two commands should be equal to the number of nodes in the cluster: 
            
            kubectl --kubeconfig KUBECONFIG logs \
                -n kube-system -l app=fluent-bit-cleanup | grep "cleaned up" | wc -l
            kubectl --kubeconfig KUBECONFIG \
                -n kube-system get pods -l app=fluent-bit-cleanup --no-headers | wc -l

     3. Delete the cleanup DaemonSet: 
            
            kubectl --kubeconfig KUBECONFIG -n kube-system delete ds \
                fluent-bit-cleanup

     4. Restart the `stackdriver-log-forwarder` Pods: 
            
            kubectl --kubeconfig KUBECONFIG \
                -n kube-system patch daemonset stackdriver-log-forwarder --type json \
                -p='[{"op": "remove", "path": "/spec/template/spec/nodeSelector/non-existing"}]'


  
Networking, VM Runtime on GDC | 1.14.0 | 

### Restarting Dataplane V2 (`anetd`) on clusters can result in existing VMs unable to attach to non-pod-network

On multi-nic clusters, restarting Dataplane V2 (`anetd`) can result in virtual machines being unable to attach to networks. An error similar to the following might be observed in the `anetd` pod logs:
    
    
    could not find an allocator to allocate the IP of the multi-nic endpoint
    

  
**Workaround:** You can restart the VM as a quick fix. To avoid a recurrence of the issue, upgrade your cluster to version 1.14.1 or a later.  
Operation | 1.13, 1.14.0, 1.14.1 | 

### `gke-metrics-agent` has no memory limit on Edge profile clusters

Depending on the cluster's workload, the `gke-metrics-agent` might use greater than 4608 MiB of memory. This issue only affects Google Distributed Cloud Edge profile clusters. Default profile clusters aren't impacted.   
**Workaround:** Upgrade your cluster to version 1.14.2 or later.  
Installation | 1.12, 1.13 | 

### Cluster creation might fail due to race conditions

When you create clusters using `kubectl`, due to race conditions preflight check may never finish. As a result, cluster creation may fail in certain cases.  The preflight check reconciler creates a `SecretForwarder` to copy the default `ssh-key` secret to the target namespace. Typically, preflight check leverages on the owner references and reconciles once the `SecretForwarder` is complete. However, in rare cases the owner references of the `SecretForwarder` can lose the reference to the preflight check, causing the preflight check to get stuck. As a result, cluster creation fails. In order to continue the reconciliation for the controller-driven preflight check, delete the cluster-operator pod or delete the preflight-check resource. When you delete the preflight-check resource, it creates another one and continues the reconciliation. Alternately, you can upgrade your existing clusters (that were created with an earlier version) to a fixed version.   
Networking | 1.9, 1.10, 1.11, 1.12, 1.13, 1.14, 1.15 | 

### Reserved IP addresses aren't released when using whereabouts plugin with the multi-NIC feature

In the multi-Nic feature, if you're using the CNI whereabouts plugin and you use the CNI DEL operation to delete a network interface for a Pod, some reserved IP addresses might not be released properly. This happens when the CNI DEL operation is interrupted. You can verify the unused IP address reservations of the Pods by running the following command:
    
    
    kubectl get ippools -A --kubeconfig KUBECONFIG_PATH

**Workaround:** Manually delete the IP addresses (ippools) that aren't used.  
Installation | 1.10, 1.11.0, 1.11.1, 1.11.2 | 

### Node Problem Detector fails in 1.10.4 user cluster

The Node Problem Detector might fail in version 1.10.x user clusters, when version 1.11.0, 1.11.1, or 1.11.2 admin clusters manage 1.10.x user clusters. When the Node Problem Detector fails, the log gets updated with the following error message:
    
    
    Error - NPD not supported for anthos baremetal version 1.10.4:
    anthos version 1.10.4 not supported.

**Workaround** Upgrade the admin cluster to 1.11.3 to resolve the issue.  
Operation | 1.14 | 

### 1.14 island mode IPv4 cluster nodes have a pod CIDR mask size of 24

In release 1.14, the `maxPodsPerNode` setting isn't taken into account for [island mode clusters](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/reference/flat-vs-island-network), so the nodes are assigned a pod CIDR mask size of 24 (256 IP addresses).nThis might cause the cluster to run out of pod IP addresses earlier than expected. For example, if your cluster has a pod CIDR mask size of 22; each node will be assigned a pod CIDR mask of 24 and the cluster will only be able to support up to 4 nodes. Your cluster may also experience network instability in a period of high pod churn when `maxPodsPerNode` is set to 129 or higher and there isn't enough overhead in the pod CIDR for each node. This issue only affects island mode IPv4 clusters that use `maxPodsPerNode` outside of the range of 65 to 128.  If your cluster is affected, the `anetd` pod reports the following error when you add a new node to the cluster and there's no `podCIDR` available:
    
    
    error="required IPv4 PodCIDR not available"

**Workaround** Use the following steps to resolve the issue:

  1. Upgrade to 1.14.1 or a later version.
  2. Remove the worker nodes and add them back.
  3. Remove the control plane nodes and add them back, preferably one by one to avoid cluster downtime.

  
Upgrades and updates | 1.14.0, 1.14.1 | 

### Cluster upgrade rollback failure

An upgrade rollback might fail for version 1.14.0 or 1.14.1 clusters. If you upgrade a cluster from 1.14.0 to 1.14.1 and then try to rollback to 1.14.0 by using `bmctl restore cluster` command, an error like the following example might be returned:
    
    
    I0119 22:11:49.705596  107905 client.go:48] Operation failed, retrying with backoff.
    Cause: error updating "baremetal.cluster.gke.io/v1, Kind=HealthCheck" cluster-user-ci-f3a04dc1b0d2ac8/user-ci-f3a04dc1b0d2ac8-network: admission webhook "vhealthcheck.kb.io"
    denied the request: HealthCheck.baremetal.cluster.gke.io "user-ci-f3a04dc1b0d2ac8-network" is invalid:
    Spec: Invalid value: v1.HealthCheckSpec{ClusterName:(*string)(0xc0003096e0), AnthosBareMetalVersion:(*string)(0xc000309690),
    Type:(*v1.CheckType)(0xc000309710), NodePoolNames:[]string(nil), NodeAddresses:[]string(nil), ConfigYAML:(*string)(nil),
    CheckImageVersion:(*string)(nil), IntervalInSeconds:(*int64)(0xc0015c29f8)}: Field is immutable

  
**Workaround:** Delete all `healthchecks.baremetal.cluster.gke.io` resources under the cluster namespace and then rerun the `bmctl restore cluster` command:

  1. List all `healthchecks.baremetal.cluster.gke.io` resources: 
         
         kubectl get healthchecks.baremetal.cluster.gke.io \
             --namespace=CLUSTER_NAMESPACE \
             --kubeconfig=ADMIN_KUBECONFIG

Replace the following:
     * `CLUSTER_NAMESPACE`: the namespace for the cluster.
     * `ADMIN_KUBECONFIG`: the path to the admin cluster kubeconfig file.
  2. Delete all `healthchecks.baremetal.cluster.gke.io` resources listed in the previous step: 
         
         kubectl delete healthchecks.baremetal.cluster.gke.io \
             HEALTHCHECK_RESOURCE_NAME \
             --namespace=CLUSTER_NAMESPACE \
             --kubeconfig=ADMIN_KUBECONFIG

Replace `HEALTHCHECK_RESOURCE_NAME` with the name of the healthcheck resources. 
  3. Rerun the `bmctl restore cluster` command.

  
Networking | 1.12.0 | 

### Service external IP address does not work in flat mode

In a cluster that has `flatIPv4` set to `true`, Services of type `LoadBalancer` are not accessible by their external IP addresses. This issue is fixed in version 1.12.1.   
**Workaround:** In the `cilium-config` ConfigMap, set `enable-415` to `"true"`, and then restart the `anetd` Pods.  
Upgrades and updates | 1.13.0, 1.14 | 

### In-place upgrades from 1.13.0 to 1.14.x never finish

When you try to do an in-place upgrade from 1.13.0 to 1.14.x using `bmctl` 1.14.0 and the `--use-bootstrap=false` flag, the upgrade never finishes. An error with the `preflight-check` operator causes the cluster to never schedule the required checks, which means the preflight check never finishes.   
**Workaround:** Upgrade to 1.13.1 first before you upgrade to 1.14.x. An in-place upgrade from 1.13.0 to 1.13.1 should work. Or, upgrade from 1.13.0 to 1.14.x without the `--use-bootstrap=false` flag.  
Upgrades and updates, Security | 1.13 and 1.14 | 

### Clusters upgraded to 1.14.0 lose master taints

The control plane nodes require one of two specific taints to prevent workload pods from being scheduled on them. When you upgrade version 1.13 GKE clusters to version 1.14.0, the control plane nodes lose the following required taints:

  * `node-role.kubernetes.io/master:NoSchedule`
  * `node-role.kubernetes.io/master:PreferNoSchedule`

**Note:** Self-managing clusters, such as a standalone type cluster, use the `PreferNoSchedule` taint by default. This problem doesn't cause upgrade failures, but pods that aren't supposed to run on the control plane nodes may start doing so. These workload pods can overwhelm control plane nodes and lead to cluster instability. **Determine if you're affected**

  1. Find control plane nodes, use the following command: 
         
         kubectl get node -l 'node-role.kubernetes.io/control-plane' \
             -o name --kubeconfig KUBECONFIG_PATH

  2. To check the list of taints on a node, use the following command: 
         
         kubectl describe node NODE_NAME \
             --kubeconfig KUBECONFIG_PATH

If neither of the required taints is listed, then you're affected.

**Workaround** Use the following steps for each control plane node of your affected version 1.14.0 cluster to restore proper function. These steps are for the `node-role.kubernetes.io/master:NoSchedule` taint and related pods. If you intend for the control plane nodes to use the `PreferNoSchedule` taint, then adjust the steps accordingly.

#### View workaround steps

  1. Apply the missing taint:
    
    kubectl taint nodes NODE_NAME \
        node-role.kubernetes.io/master:NoSchedule \
        -–kubeconfig KUBECONFIG_PATH

  2. Find pods without the `node-role.kubernetes.io/master:NoSchedule` toleration: 
         
         kubectl get pods -A --field-selector spec.nodeName="NODE_NAME" \
             -o=custom-columns='Name:metadata.name,Toleration:spec.tolerations[*].key' \
             --kubeconfig KUBECONFIG_PATH | \
             grep -v  "node-role.kubernetes.io/master" | uniq

  3. Delete the pods that don't have the `node-role.kubernetes.io/master:NoSchedule` toleration: 
         
         kubectl delete pod POD_NAME –-kubeconfig KUBECONFIG_PATH


  
Operation, VM Runtime on GDC | 1.11, 1.12, 1.13, 1.14, 1.15, 1.16, 1.28, 1.29 | 

### VM creation fails intermittently with upload errors

Creating a new Virtual Machine (VM) with the `kubectl virt create vm` command fails infrequently during image upload. This issue applies for both Linux and Windows VMs. The error looks something like the following example: 
    
    
    PVC default/heritage-linux-vm-boot-dv not found DataVolume default/heritage-linux-vm-boot-dv created
    Waiting for PVC heritage-linux-vm-boot-dv upload pod to be ready... Pod now ready
    Uploading data to https://10.200.0.51
    
     2.38 MiB / 570.75 MiB [>----------------------------------------------------------------------------------]   0.42% 0s
    
    **fail to upload image: unexpected return value 500, ** ...

**Workaround** Retry the `kubectl virt create vm` command to create your VM.  
Upgrades and updates, Logging and monitoring | 1.11 | 

### Managed collection components in 1.11 clusters aren't preserved in upgrades to 1.12

Managed collection components are part of Managed Service for Prometheus. If you manually deployed [managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#anthos) components in the `gmp-system` namespace of your version 1.11 clusters, the associated resources aren't preserved when you upgrade to version 1.12. Starting with version 1.12.0 clusters, Managed Service for Prometheus components in the `gmp-system` namespace and related custom resource definitions are managed by `stackdriver-operator` with the `enableGMPForApplications` field. The `enableGMPForApplications` field defaults to `true`, so if you manually deploy Managed Service for Prometheus components in the namespace before upgrading to version 1.12, the resources are deleted by `stackdriver-operator`. **Workaround** To preserve manually managed collection resources:

  1. Backup all existing PodMonitoring custom resources. 
  2. Upgrade the cluster to version 1.12 and [ enable Managed Service for Prometheus](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/application-logging-monitoring#enable_managed_service_for_prometheus).
  3. Redeploy the PodMonitoring custom resources on your upgraded cluster.

  
Upgrades and updates | 1.13 | 

### Some version 1.12 clusters with the Docker container runtime can't upgrade to version 1.13

If a version 1.12 cluster that uses the Docker container runtime is missing the following annotation, it can't upgrade to version 1.13:
    
    
    baremetal.cluster.gke.io/allow-docker-container-runtime:  "true"

If you're affected by this issue, `bmctl` writes the following error in the `upgrade-cluster.log` file inside the `bmctl-workspace` folder:
    
    
    Operation failed, retrying with backoff. Cause: error creating "baremetal.cluster.gke.io/v1, Kind=Cluster": admission webhook
    "vcluster.kb.io" denied the request: Spec.NodeConfig.ContainerRuntime: Forbidden: Starting with Anthos Bare Metal version 1.13 Docker container
    runtime will not be supported. Before 1.13 please set the containerRuntime to containerd in your cluster resources.
    
    Although highly discouraged, you can create a cluster with Docker node pools until 1.13 by passing the flag "--allow-docker-container-runtime" to bmctl
    create cluster or add the annotation "baremetal.cluster.gke.io/allow-docker- container-runtime: true" to the cluster configuration file.

This is most likely to occur with version 1.12 Docker clusters that were upgraded from 1.11, as that upgrade doesn't require the annotation to maintain the Docker container runtime. In this case, clusters don't have the annotation when upgrading to 1.13. Note that starting with version 1.13, `containerd` is the only permitted container runtime.  **Workaround:** If you're affected by this problem, update the cluster resource with the missing annotation. You can add the annotation either while the upgrade is running or after canceling and before retrying the upgrade.  
Installation | 1.11 | 

### `bmctl` exits before cluster creation completes 

Cluster creation may fail for Distributed Cloud version 1.11.0 (this issue is fixed in Distributed Cloud release 1.11.1). In some cases, the `bmctl create cluster` command exits early and writes errors like the following to the logs:
    
    
    Error creating cluster: error waiting for applied resources: provider cluster-api watching namespace USER_CLUSTER_NAME not found in the target cluster

  
**Workaround** The failed operation produces artifacts, but the cluster isn't operational. If this issue affects you, use the following steps to clean up artifacts and create a cluster:

#### View workaround steps

  1. To delete cluster artifacts and reset the node machine, run the following command: 
         
         bmctl reset -c USER_CLUSTER_NAME

  2. To start the cluster creation operation, run the following command: 
         
         bmctl create cluster -c USER_CLUSTER_NAME \
             --keep-bootstrap-cluster

The `--keep-bootstrap-cluster` flag is important if this command fails. If the cluster creation command succeeds, you can skip the remaining steps. Otherwise, continue.
  3. Run the following command to get the version for the bootstrap cluster: 
         
         kubectl get cluster USER_CLUSTER_NAME \
             -n USER_CLUSTER_NAMESPACE \
             --kubeconfig bmctl-workspace/.kindkubeconfig \
             -o=jsonpath='{.status.anthosBareMetalVersion}

The output should be `1.11.0`. If the output isn't `1.11.0`, wait a minute or two and retry. 
  4. To manually move resources from the bootstrap cluster to the target cluster, run the following command: 
         
         bmctl move --from-kubeconfig bmctl-workspace/.kindkubeconfig \
             --to-kubeconfig \
             bmctl-workspace/USER_CLUSTER_NAME/USER_CLUSTER_NAME-kubeconfig \
             -n USER_CLUSTER_NAMESPACE

  5. To delete the bootstrap cluster, run the following command: 
         
         bmctl reset bootstrap


  
Installation, VM Runtime on GDC | 1.11, 1.12 | 

###  Installation reports VM runtime reconciliation error 

The cluster creation operation may report an error similar to the following:
    
    
    I0423 01:17:20.895640 3935589 logs.go:82]  "msg"="Cluster reconciling:" "message"="Internal error occurred: failed calling webhook \"vvmruntime.kb.io\": failed to call webhook: Post \"https://vmruntime-webhook-service.kube-system.svc:443/validate-vm-cluster-gke-io-v1vmruntime?timeout=10s\": dial tcp 10.95.5.151:443: connect: connection refused" "name"="xxx" "reason"="ReconciliationError"

  
**Workaround** This error is benign and you can safely ignore it.  
Installation | 1.10, 1.11, 1.12 | 

### Cluster creation fails when using multi-NIC, `containerd`, and HTTPS proxy 

Cluster creation fails when you have the following combination of conditions:

  * Cluster is configured to use `containerd` as the container runtime (`nodeConfig.containerRuntime` set to `containerd` in the cluster configuration file, the default for Distributed Cloud version 1.13 and higher).


  * Cluster is configured to provide multiple network interfaces, multi-NIC, for pods (`clusterNetwork.multipleNetworkInterfaces` set to `true` in the cluster configuration file).


  * Cluster is configured to use a proxy (`spec.proxy.url` is specified in the cluster configuration file). Even though cluster creation fails, this setting is propagated when you attempt to create a cluster. You may see this proxy setting as an `HTTPS_PROXY` environment variable or in your `containerd` configuration (`/etc/systemd/system/containerd.service.d/09-proxy.conf`). 

  
**Workaround** Append service CIDRs (`clusterNetwork.services.cidrBlocks`) to the `NO_PROXY` environment variable on all node machines.  
Installation | 1.10, 1.11, 1.12 | 

### Failure on systems with restrictive `umask` setting

Distributed Cloud release 1.10.0 introduced a rootless control plane feature that runs all the control plane components as a non-root user. Running all components as a non-root user may cause installation or upgrade failures on systems with a more restrictive `umask` setting of `0077`.   
**Workaround** Reset the control plane nodes and change the `umask` setting to `0022` on all the control plane machines. After the machines have been updated, retry the installation. Alternatively, you can change the directory and file permissions of `/etc/kubernetes` on the control-plane machines for the installation or upgrade to proceed.

  * Make `/etc/kubernetes` and all its subdirectories world readable: `chmod o+rx`.
  * Make all the files owned by `root` user under the directory (recursively) `/etc/kubernetes` world readable (`chmod o+r`). Exclude private key files (.key) from these changes as they are already created with correct ownership and permissions.
  * Make `/usr/local/etc/haproxy/haproxy.cfg` world readable.
  * Make `/usr/local/etc/bgpadvertiser/bgpadvertiser-cfg.yaml` world readable.

  
Installation | 1.10, 1.11, 1.12, 1.13 | 

### Control group v2 incompatibility

[ Control group v2](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html) (cgroup v2) isn't supported in Google Distributed Cloud clusters versions 1.13 and earlier of Distributed Cloud. However, version 1.14 supports cgroup v2 as a [Preview ](https://cloud.google.com/products/#product-launch-stages)feature. The presence of `/sys/fs/cgroup/cgroup.controllers` indicates that your system uses cgroup v2.   
**Workaround** If your system uses cgroup v2, upgrade your cluster to version 1.14.  
Installation | 1.10, 1.11, 1.12, 1.13, 1.14, 1.15, 1.16, 1.28, 1.29 | 

### Preflight checks and service account credentials

For installations triggered by admin or hybrid clusters (in other words, clusters not created with `bmctl`, like user clusters), the preflight check does not verify Google Cloud service account credentials or their associated permissions.  
Installation | 1.10, 1.11, 1.12, 1.13, 1.14, 1.15, 1.16, 1.28, 1.29 | 

### Installing on vSphere

When installing Google Distributed Cloud clusters on vSphere VMs, you must set the `tx-udp_tnl-segmentation` and `tx-udp_tnl-csum-segmentation` flags to off. These flags are related to the hardware segmentation offload done by the vSphere driver VMXNET3 and they don't work with the GENEVE tunnel of Google Distributed Cloud clusters.   
**Workaround** Run the following command on each node to check the current values for these flags:
    
    
    ethtool -k NET_INTFC | grep segm

Replace `NET_INTFC` with the network interface associated with the IP address of the node. The response should have entries like the following:
    
    
    ...
    tx-udp_tnl-segmentation: on
    tx-udp_tnl-csum-segmentation: on
    ...

Sometimes in RHEL 8.4, `ethtool` shows these flags are off while they aren't. To explicitly set these flags to off, toggle the flags on and then off with the following commands: 
    
    
    ethtool -K ens192 tx-udp_tnl-segmentation on ethtool -K ens192 \
        tx-udp_tnl-csum-segmentation on
    ethtool -K ens192 tx-udp_tnl-segmentation off ethtool -K ens192 \
        tx-udp_tnl-csum-segmentation off

This flag change does not persist across reboots. Configure the startup scripts to explicitly set these flags when the system boots.  
Upgrades and updates | 1.10 | 

### `bmctl` can't create, update, or reset lower version user clusters

The `bmctl` CLI can't create, update, or reset a user cluster with a lower minor version, regardless of the admin cluster version. For example, you can't use `bmctl` with a version of `1.N.X` to reset a user cluster of version `1.N-1.Y`, even if the admin cluster is also at version `1.N.X`. If you are affected by this issue, you should see the logs similar to the following when you use `bmctl`:
    
    
    [2022-06-02 05:36:03-0500] error judging if the cluster is managing itself: error to parse the target cluster: error parsing cluster config: 1 error occurred:
    
    *   cluster version 1.8.1 isn't supported in bmctl version 1.9.5, only cluster version 1.9.5 is supported

  
**Workaround:** Use `kubectl` to create, edit, or delete the user cluster custom resource inside the admin cluster. The ability to upgrade user clusters is unaffected.  
Upgrades and updates | 1.12 | 

### Cluster upgrades to version 1.12.1 may stall 

Upgrading clusters to version 1.12.1 sometimes stalls due to the API server becoming unavailable. This issue affects all cluster types and all supported operating systems. When this issue occurs, the `bmctl upgrade cluster`command can fail at multiple points, including during the second phase of preflight checks.   
**Workaround** You can check your upgrade logs to determine if you are affected by this issue. Upgrade logs are located in `/baremetal/bmctl-workspace/CLUSTER_NAME/log/upgrade-cluster-TIMESTAMP` by default. The `upgrade-cluster.log` may contain errors like the following:
    
    
    Failed to upgrade cluster: preflight checks failed: preflight check failed

The machine log may contain errors like the following (repeated failures indicate that you are affected by this issue): 
    
    
    FAILED - RETRYING: Query CNI health endpoint (30 retries left). FAILED - RETRYING: Query CNI health endpoint (29 retries left).
    FAILED - RETRYING: Query CNI health endpoint (28 retries left). ...

HAProxy and Keepalived must be running on each control plane node before you reattempt to upgrade your cluster to version 1.12.1. Use the [ `crictl` command-line interface](https://kubernetes.io/docs/tasks/debug/debug-cluster/crictl/) on each node to check to see if the `haproxy` and `keepalived` containers are running:
    
    
    docker/crictl ps | grep haproxy docker/crictl ps | grep keepalived

If either HAProxy or Keepalived isn't running on a node, restart `kubelet` on the node:
    
    
    systemctl restart kubelet  
  
Upgrades and updates, VM Runtime on GDC | 1.11, 1.12 | 

### Upgrading clusters to version 1.12.0 or higher fails when VM Runtime on GDC is enabled

In version 1.12.0 Google Distributed Cloud clusters, all resources related to VM Runtime on GDC are migrated to the `vm-system` namespace to better support the VM Runtime on GDC GA release. If you have VM Runtime on GDC enabled in a version 1.11.x or lower cluster, upgrading to version 1.12.0 or higher fails unless you first disable VM Runtime on GDC. When you're affected by this issue, the upgrade operation reports the following error:
    
    
    Failed to upgrade cluster: cluster isn't upgradable with vmruntime enabled from
    version 1.11.x to version 1.12.0: please disable VMruntime before upgrade to
    1.12.0 and higher version
    

  
**Workaround** To disable VM Runtime on GDC:

  1. Edit the `VMRuntime` custom resource: 
         
         kubectl edit vmruntime

  2. Set `enabled` to `false` in the spec: 
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VMRuntime
         metadata:
           name: vmruntime
         spec:**  enabled: false**
           ...

  3. Save the custom resource in your editor.
  4. Once the cluster upgrade is complete, re-enable VM Runtime on GDC.

For more information, see [Working with VM-based workloads](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/vm-workloads).   
Upgrades and updates | 1.10, 1.11, 1.12 | 

### Upgrade stuck at `error during manifests operations`

In some situations, cluster upgrades fail to complete and the `bmctl` CLI becomes unresponsive. This problem can be caused by an incorrectly updated resource. To determine if you're affected by this issue and to correct it, check the `anthos-cluster-operator` logs and look for errors similar to the following entries:
    
    
    controllers/Cluster "msg"="error during manifests operations" "error"="1 error occurred: ... {RESOURCE_NAME} is invalid: metadata.resourceVersion: Invalid value: 0x0: must be specified for an update

These entries are a symptom of an incorrectly updated resource, where `{RESOURCE_NAME}` is the name of the problem resource.   
**Workaround** If you find these errors in your logs, complete the following steps:

  1. Use `kubectl edit` to remove the `kubectl.kubernetes.io/last-applied-configuration` annotation from the resource contained in the log message.
  2. Save and apply your changes to the resource.
  3. Retry the cluster upgrade.

  
Upgrades and updates | 1.10, 1.11, 1.12 | 

### Upgrades are blocked for clusters with features that use Network Gateway for GDC

Cluster upgrades from 1.10.x to 1.11.x fail for clusters that use either [egress NAT gateway](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/egress-nat) or [bundled load-balancing with BGP](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/lb-bundled-bgp). These features both use Network Gateway for GDC. Cluster upgrades get stuck at the `Waiting for upgrade to complete...` command-line message and the `anthos-cluster-operator` logs errors like the following:
    
    
    apply run failed ... MatchExpressions:[]v1.LabelSelectorRequirement(nil)}: field
    is immutable...
    

  
**Workaround** **Caution:** The following workaround deletes manifests and causes a brief 30–60 second downtime for bundled load-balancing with BGP. BGP sessions are dropped and re-established, and LoadBalancer services are unavailable during this period. Function is restored when the `anthos-cluster-operator` reinstalls the manifests. To unblock the upgrade, run the following commands against the cluster you are upgrading:
    
    
    kubectl -n kube-system delete deployment \
        ang-controller-manager-autoscaler
    kubectl -n kube-system delete deployment \
        ang-controller-manager
    kubectl -n kube-system delete ds ang-node  
  
Upgrades and updates | 1.10, 1.11, 1.12, 1.13, 1.14, 1.15 | 

### `bmctl update` doesn't remove maintenance blocks 

The `bmctl update` command can't remove or modify the `maintenanceBlocks` section from the cluster resource configuration.    
**Workaround** For more information, including instructions for removing nodes from maintenance mode, see [Put nodes into maintenance mode](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/maintenance-mode).  
Operation | 1.10, 1.11, 1.12 | 

### Nodes uncordoned if you don't use the maintenance mode procedure 

If you runversion 1.12.0 clusters (`anthosBareMetalVersion: 1.12.0`) or lower and manually use `kubectl cordon` on a node, Google Distributed Cloud might uncordon the node before you're ready in an effort to reconcile the expected state.   
**Workaround** For version 1.12.0 and lower clusters, use [maintenance mode](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/maintenance-mode) to cordon and drain nodes safely. In version 1.12.1 (`anthosBareMetalVersion: 1.12.1`) or higher, Google Distributed Cloud won't uncordon your nodes unexpectedly when you use `kubectl cordon`.  
Operation | 1.11 | 

### Version 11 admin clusters using a registry mirror can't manage version 1.10 clusters 

If your admin cluster is on version 1.11 and uses a registry mirror, it can't manage user clusters that are on a lower minor version. This issue affects reset, update, and upgrade operations on the user cluster. To determine whether this issue affects you, check your logs for cluster operations, such as create, upgrade, or reset. These logs are located in the `bmctl-workspace/CLUSTER_NAME/` folder by default. If you're affected by the issue, your logs contain the following error message:
    
    
    flag provided but not defined: -registry-mirror-host-to-endpoints
      
  
Operation | 1.10, 1.11 | 

### kubeconfig Secret overwritten 

The `bmctl check cluster` command, when run on user clusters, overwrites the user cluster kubeconfig Secret with the admin cluster kubeconfig. Overwriting the file causes standard cluster operations, such as updating and upgrading, to fail for affected user clusters. This problem applies to Google Distributed Cloud cluster versions 1.11.1 and earlier. To determine if this issue affects a user cluster, run the following command:
    
    
    kubectl --kubeconfig ADMIN_KUBECONFIG \
        get secret -n USER_CLUSTER_NAMESPACE \
        USER_CLUSTER_NAME -kubeconfig \
        -o json  | jq -r '.data.value'  | base64 -d

Replace the following:

  * `ADMIN_KUBECONFIG`: the path to the admin cluster kubeconfig file.
  * `USER_CLUSTER_NAMESPACE`: the namespace for the cluster. By default, the cluster namespaces for Google Distributed Cloud clusters are the name of the cluster prefaced with `cluster-`. For example, if you name your cluster `test`, the default namespace is `cluster-test`.
  * `USER_CLUSTER_NAME`: the name of the user cluster to check.

If the cluster name in the output (see `contexts.context.cluster` in the following sample output) is the admin cluster name, then the specified user cluster is affected.
    
    
    apiVersion: v1
    clusters:
    - cluster:
        certificate-authority-data:LS0tLS1CRU...UtLS0tLQo=
        server: https://10.200.0.6:443
      name: ci-aed78cdeca81874** contexts:
    - context:
        cluster: ci-aed78cdeca81**
        user: ci-aed78cdeca81-admin
      name: ci-aed78cdeca81-admin@ci-aed78cdeca81
    current-context: ci-aed78cdeca81-admin@ci-aed78cdeca81
    kind: Config
    preferences: {}
    users:
    - name: ci-aed78cdeca81-admin
      user:
        client-certificate-data: LS0tLS1CRU...UtLS0tLQo=
        client-key-data: LS0tLS1CRU...0tLS0tCg==

  
**Workaround** The following steps restore function to an affected user cluster (`USER_CLUSTER_NAME`):

  1. Locate the user cluster kubeconfig file. Google Distributed Cloud generates the kubeconfig file on the admin workstation when you create a cluster. By default, the file is in the `bmctl-workspace/USER_CLUSTER_NAME` directory.
  2. Verify the kubeconfig is correct user cluster kubeconfig: 
         
         kubectl get nodes \
             --kubeconfig PATH_TO_GENERATED_FILE

Replace `PATH_TO_GENERATED_FILE` with the path to the user cluster kubeconfig file. The response returns details about the nodes for the user cluster. Confirm the machine names are correct for your cluster.
  3. Run the following command to delete the corrupted kubeconfig file in the admin cluster: 
         
         kubectl delete secret \
             -n USER_CLUSTER_NAMESPACE \
             USER_CLUSTER_NAME-kubeconfig

  4. Run the following command to save the correct kubeconfig secret back to the admin cluster: 
         
         kubectl create secret generic \
             -n USER_CLUSTER_NAMESPACE \
             USER_CLUSTER_NAME-kubeconfig \
             --from-file=value=PATH_TO_GENERATED_FILE


  
Operation | 1.10, 1.11, 1.12, 1.13, 1.14, 1.15, 1.16, 1.28, 1.29 | 

### Taking a snapshot as a non-root login user

If you use containerd as the container runtime, running snapshot as non-root user requires `/usr/local/bin` to be in the user's PATH. Otherwise it will fail with a `crictl: command not found` error. When you aren't logged in as the root user, `sudo` is used to run the snapshot commands. The `sudo` PATH can differ from the root profile and may not contain `/usr/local/bin`.   
**Workaround** Update the `secure_path` in `/etc/sudoers` to include `/usr/local/bin`. Alternatively, create a symbolic link for `crictl` in another `/bin` directory.  
Logging and monitoring | 1.10 | 

### `stackdriver-log-forwarder` has `[parser:cri] invalid time format` warning logs

If the [container runtime interface (CRI) parser](https://docs.fluentbit.io/manual/installation/kubernetes#container-runtime-interface-cri-parser) uses an incorrect regular expression for parsing time, the logs for the `stackdriver-log-forwarder` Pod contain errors and warnings like the following:
    
    
    [2022/03/04 17:47:54] [error] [parser] time string length is too long [2022/03/04 20:16:43] [ warn] [parser:cri] invalid time format %Y-%m-%dT%H:%M:%S.%L%z for '2022-03-04T20:16:43.680484387Z'

  
**Workaround:**

#### View workaround steps

Upgrade your cluster to version 1.11.0 or later. If you're unable to upgrade your clusters immediately, use the following steps to update CRI parsing regex:

  1. To prevent your following changes from reverting, scale down the `stackdriver-operator`: 
         
         kubectl  --kubeconfig KUBECONFIG \
             -n kube-system scale deploy \
             stackdriver-operator --replicas=0

  2. Edit the `Regex` entry in the `stackdriver-log-forwarder-config` ConfigMap: 
         
         kubectl --kubeconfig KUBECONFIG \
             -n kube-system edit configmap \
             stackdriver-log-forwarder-config

Your edited resource should look similar to the following: 
         
         [PARSER]
             # https://rubular.com/r/Vn30bO78GlkvyB
             Name cri
             **Format regex
             # The timestamp is described in
             https://www.rfc-editor.org/rfc/rfc3339#section-5.6
             Regex ^(?<time>[0-9]{4}-[0-9]{2}-[0-9]{2}[Tt ][0-9]
             {2}:[0-9]{2}:[0-9]{2}(?:\.[0-9]+)?(?:[Zz]|[+-][0-9]
             {2}:[0-9]{2})) (?<stream>stdout|stderr)
             (?<logtag>[^ ]*) (?<log>.*)$**
             Time_Key    time
             Time_Format %Y-%m-%dT%H:%M:%S.%L%z
             Time_Keep   off

  3. Restart the log forwarder pods: 
         
         kubectl --kubeconfig KUBECONFIG \
             -n kube-system rollout restart daemonset \
             stackdriver-log-forwarder


  
Logging and monitoring | 1.10, 1.11, 1.12, 1.13, 1.14, 1.15 | 

### Unexpected monitoring billing 

For Google Distributed Cloud cluster versions 1.10 to 1.15, some customers have found unexpectedly high billing for `Metrics volume` on the **Billing** page. This issue affects you only when all of the following circumstances apply:

  * Application monitoring is enabled (`enableStackdriverForApplications=true`) 
  * [Managed Service for Prometheus](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/application-logging-monitoring#enable_managed_service_for_prometheus) isn't enabled (`enableGMPForApplications`) 
  * Application Pods have the `prometheus.io/scrap=true` annotation

To confirm whether you are affected by this issue, [list your user-defined metrics](https://docs.cloud.google.com/monitoring/docs/metrics-management#view-metrics). If you see billing for unwanted metrics, then this issue applies to you.   
**Workaround** If you are affected by this issue, we recommend that you upgrade your clusters to version 1.12 and switch to new application monitoring solution [managed-service-for-prometheus](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/application-logging-monitoring#enable_managed_service_for_prometheus) that address this issue:
* Separate flags to control the collection of application logs versus application metrics 
* Bundled Google Cloud Managed Service for Prometheus
If you can't upgrade to version 1.12, use the following steps:

  1. Find the source Pods and Services that have the unwanted billing: 
         
         kubectl --kubeconfig KUBECONFIG \
             get pods -A -o yaml | grep 'prometheus.io/scrape: "true"'
         kubectl --kubeconfig KUBECONFIG get \
             services -A -o yaml | grep 'prometheus.io/scrape: "true"'

  2. Remove the `prometheus.io/scrap=true` annotation from the Pod or Service.

  
Logging and monitoring | 1.11, 1.12, 1.13, 1.14, 1.15, 1.16, 1.28 | 

### Edits to `metrics-server-config` aren't persisted 

High pod density can, in extreme cases, create excessive logging and monitoring overhead, which can cause Metrics Server to stop and restart. You can edit the `metrics-server-config` ConfigMap to allocate more resources to keep Metrics Server running. However, due to reconciliation, edits made to `metrics-server-config` can get reverted to the default value during a cluster update or upgrade operation. Metrics Server isn't affected immediately, but the next time it restarts, it picks up the reverted ConfigMap and is vulnerable to excessive overhead, again.   
**Workaround** For 1.11.x, you can script the ConfigMap edit and perform it along with updates or upgrades to the cluster. For 1.12 and onward, contact support.  
Logging and monitoring | 1.11, 1.12 | 

### Deprecated metrics affects Cloud Monitoring dashboard 

Several Google Distributed Cloud metrics have been deprecated and, starting with Distributed Cloud release 1.11, data is no longer collected for these deprecated metrics. If you use these metrics in any of your alerting policies, there won't be any data to trigger the alerting condition. The following table lists the individual metrics that have been deprecated and the metric that replaces them. | Deprecated metrics | Replacement metric  
---|---  
`kube_daemonset_updated_number_scheduled` | `kube_daemonset_status_updated_number_scheduled`  
`kube_node_status_allocatable_cpu_cores`  
`kube_node_status_allocatable_memory_bytes`  
`kube_node_status_allocatable_pods` | `kube_node_status_allocatable`  
`kube_node_status_capacity_cpu_cores`  
`kube_node_status_capacity_memory_bytes`  
`kube_node_status_capacity_pods` | `kube_node_status_capacity`  
  
In Google Distributed Cloud cluster versions lower than 1.11, the policy definition file for the recommended `Anthos on baremetal node cpu usage exceeds 80 percent (critical)` alert uses the deprecated metrics. The `node-cpu-usage-high.json` JSON definition file is updated for releases 1.11.0 and later.

  


**Workaround**

Use the following steps to migrate to the replacement metrics:

  1. In the Google Cloud console, select **Monitoring** or click the following button:   
[Go to Monitoring](https://console.cloud.google.com/monitoring)
  2. In the navigation pane, select **Dashboards** , and delete the **Anthos cluster node status** dashboard.
  3. Click the **Sample library** tab and reinstall the **Anthos cluster node status** dashboard.
  4. Follow the instructions in [Creating alerting policies](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/alerting-policies-creating) to create a policy using the updated [ `node-cpu-usage-high.json`](https://docs.cloud.google.com/static/anthos/clusters/docs/bare-metal/1.16/samples/node-cpu-usage-high.json) policy definition file.

  
Logging and monitoring | 1.10, 1.11 | 

### `stackdriver-log-forwarder` has `CrashloopBackOff ` errors

In some situations, the `fluent-bit` logging agent can get stuck processing corrupt chunks. When the logging agent is unable to bypass corrupt chunks, you may observe that `stackdriver-log-forwarder` keeps crashing with a `CrashloopBackOff` error. If you are having this problem, your logs have entries like the following
    
    
    [2022/03/09 02:18:44] [engine] caught signal (SIGSEGV) #0  0x5590aa24bdd5
    in  validate_insert_id() at plugins/out_stackdriver/stackdriver.c:1232
    #1  0x5590aa24c502      in  stackdriver_format() at plugins/out_stackdriver/stackdriver.c:1523
    #2  0x5590aa24e509      in  cb_stackdriver_flush() at plugins/out_stackdriver/stackdriver.c:2105
    #3  0x5590aa19c0de      in  output_pre_cb_flush() at include/fluent-bit/flb_output.h:490
    #4  0x5590aa6889a6      in  co_init() at lib/monkey/deps/flb_libco/amd64.c:117 #5  0xffffffffffffffff  in  ???() at ???:0
    

  
**Workaround:** Clean up the buffer chunks for the Stackdriver Log Forwarder. Note: In the following commands, replace `KUBECONFIG` with the path to the admin cluster kubeconfig file.

  1. Terminate all `stackdriver-log-forwarder` pods: 
         
         kubectl --kubeconfig KUBECONFIG -n kube-system patch daemonset \
             stackdriver-log-forwarder -p \
             '{"spec": {"template": {"spec": {"nodeSelector": {"non-existing": "true"}}}}}'

Verify that the `stackdriver-log-forwarder` pods are deleted before going to the next step.
  2. Deploy the following DaemonSet to clean up any corrupted data in `fluent-bit` buffers: 
         
         kubectl --kubeconfig KUBECONFIG -n kube-system apply -f - << EOF
         apiVersion: apps/v1
         kind: DaemonSet
         metadata:
           name: fluent-bit-cleanup
           namespace: kube-system
         spec:
           selector:
             matchLabels:
               app: fluent-bit-cleanup
           template:
             metadata:
               labels:
                 app: fluent-bit-cleanup
             spec:
               containers:
               - name: fluent-bit-cleanup
                 image: debian:10-slim
                 command: ["bash", "-c"]
                 args:
                 - |
                   rm -rf /var/log/fluent-bit-buffers/
                   echo "Fluent Bit local buffer is cleaned up."
                   sleep 3600
                 volumeMounts:
                 - name: varlog
                   mountPath: /var/log
                 securityContext:
                   privileged: true
               tolerations:
               - key: "CriticalAddonsOnly"
                 operator: "Exists"
               - key: node-role.kubernetes.io/master
                 effect: NoSchedule
               - key: node-role.gke.io/observability
                 effect: NoSchedule
               volumes:
               - name: varlog
                 hostPath:
                   path: /var/log
         EOF

  3. Use the following commands to verify that the DaemonSet has cleaned up all the nodes: 
         
         kubectl --kubeconfig KUBECONFIG logs \
             -n kube-system -l \
             app=fluent-bit-cleanup | grep "cleaned up" | wc -l
         kubectl --kubeconfig KUBECONFIG -n \
             kube-system get pods -l \
             app=fluent-bit-cleanup --no-headers | wc -l

The output of the two commands should be equal to the number of nodes in your cluster.
  4. Delete the cleanup DaemonSet: 
         
         kubectl --kubeconfig KUBECONFIG -n \
             kube-system delete ds fluent-bit-cleanup

  5. Restart the log forwarder pods: 
         
         kubectl --kubeconfig KUBECONFIG \
             -n kube-system patch daemonset \
             stackdriver-log-forwarder --type json \
             -p='[{"op": "remove", "path": "/spec/template/spec/nodeSelector/non-existing"}]'


  
Logging and monitoring | 1.10, 1.11, 1.12, 1.13, 1.14, 1.15, 1.16, 1.28 | 

### Unknown metrics error in gke-metrics-agent log

`gke-metrics-agent` is a daemonset that is collecting metrics on each node and forward them to Cloud Monitoring. It may produce logs such as the following:
    
    
    Unknown metric: kubernetes.io/anthos/go_gc_duration_seconds_summary_percentile

Similar errors may happen to other metrics types, including (but not limited to):

  * `apiserver_admission_step_admission_duration_seconds_summary`
  * `go_gc_duration_seconds`
  * `scheduler_scheduling_duration_seconds`
  * `gkeconnect_http_request_duration_seconds_summary`
  * `alertmanager_nflog_snapshot_duration_seconds_summary`

These error logs can be safely ignored as the metrics they refer to are not supported and not critical for monitoring purposes.  
Logging and monitoring | 1.10, 1.11 | 

### Intermittent metrics export interruptions

Google Distributed Cloud clusters might experience interruptions in normal, continuous exporting of metrics, or missing metrics on some nodes. If this issue affects your clusters, you may see gaps in data for the following metrics (at a minimum):

  * `kubernetes.io/anthos/container_memory_working_set_bytes`
  * `kubernetes.io/anthos/container_cpu_usage_seconds_total`
  * `kubernetes.io/anthos/container_network_receive_bytes_total`

  
**Workaround** Upgrade your clusters to version 1.11.1 or later. If you can't upgrade, perform the following steps as a workaround:

  1. Open your `stackdriver` resource for editing: 
         
         kubectl -n kube-system edit stackdriver stackdriver

  2. To increase the CPU request for `gke-metrics-agent` from `10m` to `50m`, add the following `resourceAttrOverride` section to the `stackdriver` manifest: 
         
         spec:
           resourceAttrOverride:
             gke-metrics-agent/gke-metrics-agent:
               limits:
                 cpu: 100m
                 memory: 4608Mi
               requests:
                 cpu: 50m
                 memory: 200Mi

Your edited resource should look similar to the following: 
         
         spec:
           anthosDistribution: baremetal
           clusterLocation: us-west1-a
           clusterName: my-cluster
           enableStackdriverForApplications: true
           gcpServiceAccountSecretName: ...
           optimizedMetrics: true
           portable: true
           projectID: my-project-191923
           proxyConfigSecretName: ...
           **resourceAttrOverride :
             gke-metrics-agent/gke-metrics-agent:
               limits:
                 cpu: 100m
                 memory: 4608Mi
               requests:
                 cpu: 50m
                 memory: 200Mi**

  3. Save your changes and close the text editor.
  4. To verify your changes have taken effect, run the following command: 
         
         kubectl -n kube-system get daemonset \
             gke-metrics-agent -o yaml | grep "cpu: 50m"

The command finds `cpu: 50m` if your edits have taken effect.

  
Networking | 1.10 | 

### Multiple default gateways breaks connectivity to external endpoints 

Having multiple default gateways in a node can lead to broken connectivity from within a Pod to external endpoints, such as `google.com`. To determine if you're affected by this issue, run the following command on the node:
    
    
    ip route show

Multiple instances of `default` in the response indicate that you're affected.  
Networking | 1.12 | 

### Networking custom resource edits on user clusters get overwritten 

Version 1.12.x Google Distributed Cloud clusters don't prevent you from manually editing networking [custom resources](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) in your user cluster. Google Distributed Cloud reconciles custom resources in the user clusters with the custom resources in your admin cluster during cluster upgrades. This reconciliation overwrites any edits made directly to the networking custom resources in the user cluster. The networking custom resources should be modified in the admin cluster only, but version 1.12.x clusters don't enforce this requirement. Advanced networking features, such as [bundled load balancing with BGP](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/lb-bundled-bgp), [egress NAT gateway](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/egress-nat), [SR-IOV networking](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/sriov), [flat-mode with BGP](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/flat-bgp-network), and [multi-NIC for Pods](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/multi-nic) use the following custom resources:

  * `BGPLoadBalancer`
  * `BGPPeer`
  * `NetworkGatewayGroup`
  * `NetworkAttachmentDefinition`
  * `ClusterCIDRConfig`
  * `FlatIPMode`

You edit these custom resources in your admin cluster and the reconciliation step applies the changes to your user clusters.   
**Workaround** If you've modified any of the previously mentioned custom resources on a user cluster, modify the corresponding custom resources on your admin cluster to match before upgrading. This step ensures that your configuration changes are preserved. Google Distributed Cloud cluster versions 1.13.0 and higher prevent you from modifying the networking custom resources on your user clusters directly.  
Networking | 1.10, 1.11, 1.12, 1.13, 1.14, 1.15, 1.16, 1.28 | 

### Pod connectivity failures and reverse path filtering

Google Distributed Cloud configures reverse path filtering on nodes to disable source validation (`net.ipv4.conf.all.rp_filter=0`). If the `rp_filter` setting is changed to `1` or `2`, pods will fail due to out-of-node communication timeouts. Reverse path filtering is set with `rp_filter` files in the IPv4 configuration folder (`net/ipv4/conf/all`). This value may also be overridden by `sysctl`, which stores reverse path filtering settings in a network security configuration file, such as `/etc/sysctl.d/60-gce-network-security.conf`.   
**Workaround** Pod connectivity can be restored by performing either of the following workarounds: Set the value for `net.ipv4.conf.all.rp_filter` back to `0` manually, and then run `sudo sysctl -p` to apply the change. Or Restart the `anetd` Pod to set `net.ipv4.conf.all.rp_filter` back to `0`. To restart the `anetd` Pod, use the following commands to locate and delete the `anetd` Pod and a new `anetd` Pod will start up in its place:
    
    
    kubectl get pods -n kube-system kubectl delete pods -n kube-system ANETD_XYZ

Replace `ANETD_XYZ` with the name of the `anetd` Pod. After performing either of the workarounds verify that the `net.ipv4.conf.all.rp_filter` value is set to `0` by running `sysctl net.ipv4.conf.all.rp_filter` on each node.  
Networking | 1.10, 1.11, 1.12, 1.13, 1.14, 1.15, 1.16, 1.28, 1.29 | 

### Bootstrap (kind) cluster IP addresses and cluster node IP addresses overlapping

`192.168.122.0/24` and `10.96.0.0/27` are the default pod and service CIDRs used by the bootstrap (kind) cluster. Preflight checks will fail if they overlap with cluster node machine IP addresses.   
**Workaround** To avoid the conflict, you can pass the `--bootstrap-cluster-pod-cidr` and `--bootstrap-cluster-service-cidr` flags to `bmctl` to specify different values.  
Operating system | 1.10, 1.11, 1.12, 1.13, 1.14, 1.15, 1.16, 1.28 | 

### Cluster creation or upgrade fails on CentOS 

In December 2020, the CentOS community and Red Hat announced the [sunset of CentOS](https://blog.centos.org/2020/12/future-is-centos-stream/). On January 31, 2022, CentOS 8 reached its end of life (EOL). As a result of the EOL, `yum` repositories stopped working for CentOS, which causes cluster creation and cluster upgrade operations to fail. This applies to all supported versions of CentOS and affects all versions of Google Distributed Cloud clusters.   
**Workaround**

#### View workaround steps

As a workaround, run the following commands to have your CentOS use an archive feed:
    
    
    sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-Linux-*
    sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' \
        /etc/yum.repos.d/CentOS-Linux-*

As a long-term solution, consider migrating to another [supported operating system](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/os-reqs).  
Security | 1.10, 1.11, 1.12, 1.13, 1.14, 1.15, 1.16, 1.28 | 

### Container can't write to `VOLUME` defined in Dockerfile with containerd and SELinux

If you use containerd as the container runtime and your operating system has SELinux enabled, the `VOLUME` defined in the application Dockerfile might not be writable. For example, containers built with the following Dockerfile aren't able to write to the `/tmp` folder.
    
    
    FROM ubuntu:20.04 RUN chmod -R 777 /tmp VOLUME /tmp
    

To verify if you're affected by this issue, run the following command on the node that hosts the problematic container:
    
    
    ausearch -m avc

If you're affected by this issue, you see a `denied` error like the following:
    
    
    time->Mon Apr  4 21:01:32 2022 type=PROCTITLE msg=audit(1649106092.768:10979): proctitle="bash" type=SYSCALL msg=audit(1649106092.768:10979): arch=c000003e syscall=257 success=no exit=-13 a0=ffffff9c a1=55eeba72b320 a2=241 a3=1b6 items=0 ppid=75712 pid=76042 auid=4294967295 uid=0 gid=0 euid=0 suid=0 fsuid=0 egid=0 sgid=0 fsgid=0 tty=pts0 ses=4294967295 comm="bash" exe="/usr/bin/bash" subj=system_u:system_r:container_t:s0:c701,c935 key=(null) type=AVC msg=audit(1649106092.768:10979): avc:  **denied** { write } for  pid=76042 comm="bash" name="aca03d7bb8de23c725a86cb9f50945664cb338dfe6ac19ed0036c" dev="sda2" ino=369501097 scontext=system_u:system_r: container_t:s0:c701,c935 tcontext=system_u:object_r: container_ro_file_t:s0 tclass=dir permissive=0

  
**Workaround** To work around this issue, make either of the following changes:

  * Turn off SELinux.
  * Don't use the `VOLUME` feature inside Dockerfile.

  
Upgrades and updates | 1.10, 1.11, 1.12 | 

### Node Problem Detector isn't enabled by default after cluster upgrades 

When you upgrade Google Distributed Cloud clusters, Node Problem Detector isn't enabled by default. This issue is applicable for upgrades in release 1.10 to 1.12.1 and has been fixed in release 1.12.2.   
**Workaround:** To enable the Node Problem Detector:

  1. Verify if `node-problem-detector systemd` service is running on the node. 
     1. Use the SSH command and connect to the node.
     2. Check if `node-problem-detector systemd` service is running on the node: 
            
            systemctl is-active node-problem-detector

If the command result displays `inactive`, then the node-problem-detector isn't running on the node.
  2. To enable the Node Problem Detector, use the `kubectl edit` command and edit the `node-problem-detector-config` ConfigMap. For more information, see [Node Problem Detector](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/node-problem-detector).

  
Operation | 1.9, 1.10 | 

### Cluster backup fails when using non-root login 

The `bmctl backup cluster` command fails if `nodeAccess.loginUser` is set to a non-root username.]   
**Workaround:** This issue applies to versions 1.9.x, 1.10.0, and 1.10.1 and is fixed in version 1.10.2 and later.  
Networking | 1.10, 1.11, 1.12 | 

### Load Balancer Services don't work with containers on the control plane host network

There is a bug in `anetd` where packets are dropped for LoadBalancer Services if the backend pods are both running on the control plane node and are using the `hostNetwork: true` field in the container's spec. The bug isn't present in version 1.13 or later.   
**Workaround:** The following workarounds can help if you use a LoadBalancer Service that is backed by hostNetwork Pods:

  1. Run them on worker nodes (not control plane nodes).
  2. Use `externalTrafficPolicy: local` in the Service spec and [ ensure your workloads run on load balancer nodes](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/bundled-lb#loadbalancer_services).

  
Upgrades and Updates | 1.12, 1.13 | 

### Orphaned anthos-version-$version$ pod failing to pull image

Cluster upgrading from 1.12.x to 1.13.x might observe a failing `anthos-version-$version$` pod with ImagePullBackOff error. This happens due to the race condition of `anthos-cluster-operator` gets upgraded and it shouldn't affect any regular cluster capabilities. The bug isn't present after version 1.13 or later.   
**Workaround:** Delete the Job of dynamic-version-installer by `kubectl delete job anthos-version-$version$ -n kube-system `  
Upgrades and updates | 1.13 | 

### 1.12 clusters upgraded from 1.11 can't upgrade to 1.13.0 

Version 1.12 clusters that were upgraded from version 1.11 can't be upgraded to version 1.13.0. This upgrade issue doesn't apply to clusters that were created at version 1.12. To determine if you're affected, check the logs of the upgrade job that contains the `upgrade-first-no*` string in the admin cluster. If you see the following error message, you're affected.
    
    
    TASK [kubeadm_upgrade_apply : Run kubeadm upgrade apply] *******
    ...
    [upgrade/config] FATAL: featureGates: Invalid value: map[string]bool{\"IPv6DualStack\":false}: IPv6DualStack isn't a valid feature name.
    ...

  
**Workaround:** To work around this issue:

  1. Run the following commands on your admin workstation: 
         
         echo '[{ "op": "remove", "path": \
             "/spec/clusterConfiguration/featureGates" }]' \
             > remove-feature-gates.patch
         export KUBECONFIG=$ADMIN_KUBECONFIG
         kubectl get kubeadmconfig -A --no-headers | xargs -L1 bash -c \
             'kubectl patch kubeadmconfig $1 -n $0 --type json \
             --patch-file remove-feature-gates.patch'

  2. Re-attempt the cluster upgrade.

  
Logging and Monitoring | 1.16.2, 1.16.3 | 

### High CPU usage for `stackdriver-operator`

There's an issue in `stackdriver-operator` that causes it to consume higher CPU time than normal. Normal CPU usage is less than 50 milliCPU (`50m`) for `stackdriver-operator` in idle state. The cause is a mismatch of Certificate resources that `stackdriver-operator` applies with the expectations from `cert-manager`. This mismatch causes a race condition between `cert-manager` and `stackdriver-operator` in updating those resources. This issue may result in reduced performance on clusters with limited CPU availability.   
**Workaround:** Until you can upgrade to a version that fixed this bug, use the following workaround:

  1. To temporarily scale down `stackdriver-operator` to 0 replicas, apply an `AddonConfiguration` custom resource: 
         
         kubectl scale deploy stackdriver-operator --replicas=0

  2. Once you've upgraded to a version that fixes this issue, scale `stackdriver-operator` back up again: 
         
         kubectl scale deploy stackdriver-operator --replicas=1


  
Logging and Monitoring | 1.16.0, 1.16.1 | 

### Annotation-based metrics scraping not working

In the Distributed Cloud 1.16 minor release, the `enableStackdriverForApplications` field in the `stackdriver` custom resource spec is deprecated. This field is replaced by two fields, `enableCloudLoggingForApplications` and `enableGMPForApplications`, in the stackdriver custom resource. We recommend that you to use Google Cloud Managed Service for Prometheus for monitoring your workloads. Use the `enableGMPForApplications` field to enable this feature. If you rely on metrics collection triggered by `prometheus.io/scrape` annotations on your workloads, you can use the `annotationBasedApplicationMetrics` feature gate flag to keep the old behavior. However, there is an issue that prevents the `annotationBasedApplicationMetrics` from working properly, preventing metrics collection from your applications into Cloud Monitoring.   
**Workaround:** To resolve this issue, upgrade your cluster to version 1.16.2 or higher. The annotation-based workload metrics collection enabled by the `annotationBasedApplicationMetrics` feature gate collects metrics for objects that have the `prometheus.io/scrape` annotation. Many software systems with open source origin may use this annotation. If you continue using this method of metrics collection, be aware of this dependency so that you aren't surprised by metrics charges in Cloud Monitoring.  
  
If you need additional assistance, reach out to [Cloud Customer Care](https://cloud.google.com/support-hub). You can also see [Getting support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support) for more information about support resources, including the following: 

  * [Requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#intro-support) for opening a support case.
  * [Tools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#support-tools) to help you troubleshoot, such as your environment configuration, logs, and metrics.
  * Supported [components](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#what-we-support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
