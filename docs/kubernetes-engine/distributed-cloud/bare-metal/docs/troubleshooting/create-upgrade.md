---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/create-upgrade/
title: Troubleshoot cluster creation or upgrade \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:56:59.650205+00:00
---

# Troubleshoot cluster creation or upgrade  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/create-upgrade/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Troubleshoot cluster creation or upgrade Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to resolve issues related to installing or upgrading Google Distributed Cloud clusters.

## Installation issues

The following sections might help you to troubleshoot issues with installing Google Distributed Cloud.

### Transient error messages

The installation process for Google Distributed Cloud is a continuous reconciliation loop. As a result, you might see transient error messages in the log during installation.

As long as the installation completes successfully, these errors can be safely ignored. The following is a list of typical transient error log messages:
    
    
      Internal error occurred: failed calling webhook "webhook.cert-manager.io": Post
      https://cert-manager-webhook.cert-manager.svc:443/mutate?timeout=10s:
      dial tcp IP_ADDRESS:443: connect: connection refused
    
    
    
      Internal error occurred: failed calling webhook "vcluster.kb.io": Post
      https://webhook-service.kube-system.svc:443/validate-baremetal-cluster-gke-io-v1-cluster?timeout=30s:
      dial tcp IP_ADDRESS:443: connect: connection refused
    
    
    
      Failed to register cluster with GKE Hub; gcloud output: error running command
      'gcloud container fleet memberships register CLUSTER_NAME  --verbosity=error --quiet':
      error: exit status 1, stderr: 'ERROR: (gcloud.container.hub.memberships.register)
      Failed to check if the user is a cluster-admin: Unable to connect to the server: EOF
    
    
    
      Get
      https://127.0.0.1:34483/apis/infrastructure.baremetal.cluster.gke.io/v1/namespaces/cluster-
      cluster1/baremetalmachines: dial tcp 127.0.0.1:34483: connect: connection refused"
    
    
    
      Create Kind Cluster "msg"="apply run failed" "error"="unable to recognize \"/tmp/kout088683152\": no matches for kind \"NetworkLogging\" in version \"networking.gke.io/v1alpha1\""
      Create Kind Cluster "msg"="apply run failed" "error"="unable to recognize \"/tmp/kout869681888\": no matches for kind \"Provider\" in version \"clusterctl.cluster.x-k8s.io/v1alpha3\""
    

If your Google Cloud service account key has expired, you see the following error messages from `bmctl`:
    
    
    Error validating cluster config: 3 errors occurred:
            * GKEConnect check failed: Get https://gkehub.googleapis.com/v1beta1/projects/project/locations/global/memberships/admin: oauth2: cannot fetch token: 400 Bad Request
    Response: {"error":"invalid_grant","error_description":"Invalid JWT Signature."}
            * ClusterOperations check failed: Post https://cloudresourcemanager.googleapis.com/v1/projects/project:testIamPermissions?alt=json&prettyPrint=false: oauth2: cannot fetch token: 400 Bad Request
    Response: {"error":"invalid_grant","error_description":"Invalid JWT Signature."}
            * GCR pull permission for bucket: artifacts.anthos-baremetal-release.appspot.com failed: Get https://storage.googleapis.com/storage/v1/b/artifacts.anthos-baremetal-release.appspot.com/iam/testPermissions?alt=json&permissions=storage.objects.get&permissions=storage.objects.list&prettyPrint=false: oauth2: cannot fetch token: 400 Bad Request
    Response: {"error":"invalid_grant","error_description":"Invalid JWT Signature."}
    

You need to generate a [new service account key](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys).

### Use the bootstrap cluster to debug issues

When Google Distributed Cloud creates self-managed (admin, hybrid, or standalone) clusters, it deploys a [Kubernetes in Docker](https://kind.sigs.k8s.io/) (kind) cluster to temporarily host the Kubernetes controllers needed to create clusters. This transient cluster is called a bootstrap cluster. User clusters are created and upgraded by their managing admin or hybrid cluster without the use of a bootstrap cluster.

**Note:** Starting with Google Distributed Cloud version 1.15.0, the default upgrade behavior for self-managed (admin, hybrid, or standalone) clusters is an _in-place_ upgrade. In-place upgrades use lifecycle controllers, instead of a bootstrap cluster, to manage the entire upgrade operation. This change simplifies the process and reduces resource requirements, which makes cluster upgrades more reliable and scalable. Although it isn't recommended, by setting `--use-bootstrap=true` flag with the `bmctl upgrade` command, you still have the option to use a bootstrap cluster.

If a kind cluster already exists in your deployment when you attempt to install, Google Distributed Cloud deletes the existing kind cluster. Deletion only happens after the installation or upgrade is successful. To preserve the existing kind cluster even after success, use the `--keep-bootstrap-cluster` flag of `bmctl`.

Google Distributed Cloud creates a configuration file for the bootstrap cluster under `WORKSPACE_DIR/.kindkubeconfig`. You can connect to the bootstrap cluster only during cluster creation and upgrade.

The bootstrap cluster needs to access a Docker repository to pull images. The registry defaults to Artifact Registry unless you are using a private registry. During cluster creation,`bmctl` creates the following files:

  * `bmctl-workspace/config.json`: Contains Google Cloud service account credentials for the registry access. The credentials are obtained from the `gcrKeyPath` field in the cluster configuration file.

  * `bmctl-workspace/config.toml`: Contains the containerd configuration in the kind cluster.




### Examine the bootstrap cluster logs

To debug the bootstrap cluster you can take the following steps:

  * Connect to the bootstrap cluster during cluster creation and upgrade.
  * Get the logs of the bootstrap cluster.



You can find the logs in the machine you use to run `bmctl` in the following folders:

  * `bmctl-workspace/CLUSTER_NAME/log/create-cluster-TIMESTAMP/bootstrap-cluster/`
  * `bmctl-workspace/CLUSTER_NAME/log/upgrade-cluster-TIMESTAMP/bootstrap-cluster/`



Replace `CLUSTER_NAME` and `TIMESTAMP` with the name of your cluster and the corresponding system's time.

To get the logs from the bootstrap cluster directly, you can run the following command during cluster creation and upgrade:
    
    
    docker exec -it bmctl-control-plane bash
    

The command opens a terminal inside the bmctl control plane container that runs in the bootstrap cluster.

To inspect the `kubelet` and containerd logs, use the following commands and look for errors or warnings in the output:
    
    
    journalctl -u kubelet
    journalctl -u containerd
    

### Enable containerd debug logging

If the standard containerd logs don't provide enough information for troubleshooting, you can increase the logging level. Increasing the logging level is often necessary when diagnosing complex issues, such as problems with a registry mirror or `ImagePullBackOff` errors.

**Note:** If a `machine-update` job gets triggered while you're troubleshooting, the job undoes any changes that you made to the `config.toml` file. If this event happens, then wait for the job to complete and try again.

To increase the logging level, do the following:

  1. Enable debug logging:

     1. Open the containerd configuration file (`/etc/containerd/config.toml`) using your preferred text editor.

     2. In the file, find the `[debug]` section and change the value of `level` from `""` to `"debug"`.

     3. Save the file and exit the text editor.

     4. Verify the that you updated the configuration file successfully:
            
            cat /etc/containerd/config.toml | grep debug
            

The output should be the following:
            
            [debug]
              level = "debug"
                shim_debug = false
            

     5. To apply the change in logging level, restart containerd:
            
            sudo systemctl restart containerd
            

  2. To generate new log entries, try to pull an image that doesn't exist or isn't used by any nodes or clusters. For example:
         
         # This command fails because the image doesn't exist
         crictl pull us-west1-docker.pkg.dev/gdc-project/samples/non-existent-image:latest
         

This forces containerd to perform an action and generate detailed logs.

  3. Wait for the image to be pulled or fail, then collect the containerd logs in a file named `containerd_log.txt`:
         
         journalctl -u containerd --no-pager --since TIME_PERIOD > containerd_log.txt
         

Replace `TIME_PERIOD` with a value specifying the start time for the logs. Enclose any value that contains spaces in double quotes. For example, `"2 hours ago"`.

  4. When you have finished troubleshooting, revert the log level to back to default. Leaving debug logging enabled can flood your system logs, affect performance, and potentially expose sensitive information.

     1. Open the `/etc/containerd/config.toml` file and change the value of `level` back to `""`, the default logging level.

     2. Verify that you updated the configuration successfully:
            
            cat /etc/containerd/config.toml | grep level
            

The output should be the following:
            
            level = ""
            

     3. To apply the change, restart containerd:
            
            sudo systemctl restart containerd
            

Your system is now back to its standard logging configuration.




## Cluster upgrade issues

When you upgrade Google Distributed Cloud clusters, you can monitor the progress and check the status of your clusters and nodes.

  * If you have problems during an upgrade, try to determine at which stage the failure occurs. To learn more about what happens to a cluster during the upgrade process, see [Lifecycle and stages of cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade-lifecycle).
  * To learn more about the impact of a problem during cluster upgrades, see [Understand the impact of failures in Google Distributed Cloud](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/failure-mode-analysis#upgrade_failures).



The following guidance can help determine if the upgrade is continuing as normal or there's a problem.

### Monitor the upgrade progress

Use the `kubectl describe cluster` command to view the status of a cluster during the upgrade process:
    
    
    kubectl describe cluster CLUSTER_NAME \
        --namespace CLUSTER_NAMESPACE \
        --kubeconfig ADMIN_KUBECONFIG
    

Replace the following values:

  * `CLUSTER_NAME`: the name of your cluster.
  * `CLUSTER_NAMESPACE`: the namespace of your cluster.
  * `ADMIN_KUBECONFIG`: the admin kubeconfig file. 
    * By default, admin, hybrid, and standalone clusters use an in-place upgrade. If you use the `--use-bootstrap=true` flag with the `bmctl upgrade` command, the upgrade operation uses a bootstrap cluster. To monitor upgrade progress when a bootstrap cluster is used, specify the path to the bootstrap cluster kubeconfig file, `.kindkubeconfig`. This file is located in the workspace directory.



Look at the `Status` section of the output, which shows an aggregation of the cluster upgrade status. If the cluster reports an error, use the following sections to troubleshoot where the issue is.

### Check if the nodes are ready

Use the `kubectl get nodes` command to view the status of nodes in a cluster during the upgrade process:
    
    
    kubectl get nodes --kubeconfig KUBECONFIG
    

To check if a node has successfully completed the upgrade process, look at the `VERSION` and `AGE` columns in the command response. The `VERSION` is the Kubernetes version for the cluster. To see the Kubernetes version for a given Google Distributed Cloud version, see [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history).

If the node shows `NOT READY`, try to connect the node and check the kubelet status:
    
    
    systemctl status kubelet
    

You can also review the kubelet logs:
    
    
    journalctl -u kubelet
    

Review the output of the kubelet status and logs to messages that indicate why the node has a problem.

### Check which node is upgrading

To check which node in the cluster is in the process of being upgraded, use the `kubectl get baremetalmachines` command:
    
    
    kubectl get baremetalmachines --namespace CLUSTER_NAMESPACE \
        --kubeconfig ADMIN_KUBECONFIG
    

Replace the following values:

  * `CLUSTER_NAMESPACE`: the namespace of your cluster.
  * `ADMIN_KUBECONFIG`: the admin kubeconfig file. 
    * If a bootstrap cluster is used for an admin, hybrid, or standalone upgrade, specify the bootstrap cluster kubeconfig file (`bmctl-workspace/.kindkubeconfig`).



The following example output shows that the node being upgraded has an `ABM VERSION` different from the `DESIRED ABM VERSION`:
    
    
    NAME         CLUSTER    READY   INSTANCEID               MACHINE      ABM VERSION   DESIRED ABM VERSION
    10.200.0.2   cluster1   true    baremetal://10.200.0.2   10.200.0.2   1.13.0        1.14.0
    10.200.0.3   cluster1   true    baremetal://10.200.0.3   10.200.0.3   1.13.0        1.13.0
    

### Check what nodes are in the process of draining

During the upgrade process, nodes are drained of Pods, and scheduling is disabled until the node is successfully upgraded. To see which nodes are draining, use the `kubectl get nodes` command:
    
    
    kubectl get nodes --kubeconfig USER_CLUSTER_KUBECONFIG | grep "SchedulingDisabled"
    

Replace `USER_CLUSTER_KUBECONFIG` with the path to the user cluster kubeconfig file.

The `STATUS` column is filtered using `grep` to only show nodes that report `SchedulingDisabled`. This status indicates that the nodes are being drained.

You can also check the node status from the admin cluster:
    
    
    kubectl get baremetalmachines -n CLUSTER_NAMESPACE \
      --kubeconfig ADMIN_KUBECONFIG
    

Replace the following values:

  * `CLUSTER_NAMESPACE`: the namespace of your cluster.
  * `ADMIN_KUBECONFIG`: the admin kubeconfig file. 
    * If a bootstrap cluster is used for an admin, hybrid, or standalone upgrade, specify the bootstrap cluster kubeconfig file (`bmctl-workspace/.kindkubeconfig`).



The node getting drained shows the status under the `MAINTENANCE` column.

### Check why a node has been in the status of draining for a long time

Use one of the methods in the previous section to identify the node getting drained by using the using `kubectl get nodes` command. Use the `kubectl get pods` command and filter on this node name to view additional details:
    
    
    kubectl get pods --all-namespaces -o wide --field-selector spec.nodeName=NODE_NAME
    

Replace `NODE_NAME` with the name of the node being drained. The output returns a list of Pods that are stuck or slow to drain. The upgrade proceeds, even with stuck Pods, when the draining process on a node takes more than 20 minutes.

Starting with release 1.29, the [node draining process](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/maintenance-mode#how_it_works) uses the Eviction API, which honors `PodDisruptionBudgets` (PDBs).

The following PDB settings can cause node draining problems:

  * Pods that are managed by multiple PDBs

  * PDB static configurations like the following:

    * `maxUnavailable` == `0`
    * `minUnavailable` >= total replicas

The total replicas count is difficult to determine from the PDB resource, because it's defined in a higher-level resource, such as a `Deployment`, `ReplicaSet`, or `StatefulSet`. PDBs match to pods based on the [selector](https://kubernetes.io/docs/tasks/run-application/configure-pdb/#specifying-a-poddisruptionbudget) in their config only. A good approach at diagnosing whether a static PDB configuration is causing a problem is looking at whether `pdb.Status.ExpectPods` <= `pdb.Status.DesiredHealthy` first and seeing whether one of the mentioned static configurations allowing this to happen.




Runtime violations, such as the calculated `DisruptionsAllowed` value for a PDB resource being `0`, can also block node draining. If you have [`PodDisruptionBudget` objects configured](https://kubernetes.io/docs/tasks/run-application/configure-pdb/) that are unable to allow any additional disruptions, node upgrades might fail to upgrade to the control plane version after repeated attempts. To prevent this failure, we recommend that you scale up the `Deployment` or `HorizontalPodAutoscaler` to allow the node to drain while still respecting the `PodDisruptionBudget` configuration.

To see all `PodDisruptionBudget` objects that don't allow any disruptions, use the following command:
    
    
    kubectl get poddisruptionbudget --all-namespaces \
        -o jsonpath='{range .items[?(@.status.disruptionsAllowed==0)]}{.metadata.name}/{.metadata.namespace}{"\n"}{end}'
    

### Check why Pods are unhealthy

Upgrades can fail if a Pod contains `upgrade-first-node` or `upgrade-node` control plane IP addresses. This behavior is usually because the static Pods aren't healthy.

  1. Check the static Pods with the `crictl ps -a` command and look for any crashing Kubernetes or `etcd` Pods. If you have any failed Pods, review the logs for the Pods to see why they're crashing.

Some possibilities for crashloop behavior include the following:

     * Permissions or owner of files mounted to static Pods aren't correct.
     * Connectivity to the virtual IP address doesn't work.
     * Issues with `etcd`.
  2. If the `crictl ps` command doesn't work or return nothing, check the `kubelet` and containerd status. Use the `systemctl status SERVICE` and `journalctl -u SERVICE` commands to look at the logs.




## What's next

If you need additional assistance, reach out to [Cloud Customer Care](https://cloud.google.com/support-hub). You can also see [Getting support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support) for more information about support resources, including the following: 

  * [Requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#intro-support) for opening a support case.
  * [Tools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#support-tools) to help you troubleshoot, such as your environment configuration, logs, and metrics.
  * Supported [components](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#what-we-support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
