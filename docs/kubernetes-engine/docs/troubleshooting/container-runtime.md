---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/container-runtime/
title: Troubleshooting the container runtime \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:24.064128+00:00
---

# Troubleshooting the container runtime  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/container-runtime/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Troubleshooting the container runtime Stay organized with collections  Save and categorize content based on your preferences. 

Issues with the container runtime on your Google Kubernetes Engine (GKE) nodes can cause a variety of workload failures, preventing your containers from starting or running reliably. These problems are often caused by issues such as network misconfigurations, permission issues, or differences between container runtimes.

Use this page to troubleshoot common issues with the container runtime on your GKE node pools. Find solutions for problems such as mount path errors on Windows, failed image pulls from private registries, missing file system metrics, CNI initialization errors, and behavioral differences in exec probes.

This information is important for Platform admins and operators and Application developers who manage and deploy workloads on GKE clusters. Understanding these troubleshooting steps can help ensure your containers run reliably across different node images and configurations. For more information about the common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Issues on Windows Server node pools

The following sections cover container runtime issues specific to GKE clusters running Windows Server node pools.

### Mount paths with bare drive letters fail

_This issue has been resolved in containerd version 1.6.6 and higher._

GKE clusters running Windows Server node pools that use the containerd runtime earlier than version 1.6.6 might experience errors similar to the following:
    
    
    failed to create containerd task : CreateComputeSystem : The parameter is incorrect : unknown
    

This error is caused by specifying a drive letter without a trailing backslash (for example, `D:` instead of `D:`). For more details, see [GitHub issue #6589](https://github.com/containerd/containerd/issues/6589).

#### Solution

To resolve this issue, upgrade your node pools to the latest GKE versions that use containerd runtime version 1.6.6 or higher.

### Container images with non-array pre-escaped `CMD` or `ENTRYPOINT` command lines fail on Windows node pools with containerd

_This issue has been resolved in containerd version 1.6 and higher._

GKE clusters running Windows Server node pools that use the containerd runtime 1.5.X might experience errors when starting containers like the following:
    
    
    failed to start containerd task : hcs::System::CreateProcess : The system cannot find the file specified.: unknown
    

For more details, refer to [GitHub issue #5067](https://github.com/containerd/containerd/issues/5067) and [GitHub issue #6300](https://github.com/containerd/containerd/issues/6300).

#### Solution

To resolve this issue, upgrade your node pools to the latest GKE versions that uses containerd runtime version 1.6.6 or higher.

### Container image volumes with non-existing paths or Linux-like (forward slash) paths fail on Windows node pools with containerd

_This issue has been resolved in containerd version 1.6 and higher._

GKE clusters running Windows Server node pools that use the containerd runtime 1.5.X might experience errors when starting containers like the following:
    
    
    failed to generate spec: failed to stat "<volume_path>": CreateFile : The system cannot find the path specified.
    

For more details, refer to [GitHub issue #5671](https://github.com/containerd/containerd/issues/5671).

#### Solution

To resolve this issue, upgrade your node pools to the latest GKE versions that uses containerd runtime version 1.6.x or higher.

### Attach-based operations don't function correctly after container-runtime restarts on GKE Windows Server node pools

_Affected GKE versions:_ 1.21 to 1.21.5-gke.1802, 1.22 to 1.22.3-gke.700

GKE clusters running Windows Server node pools that use the containerd runtime (version 1.5.4 and 1.5.7-gke.0) might experience issues if the container runtime is forcibly restarted, with attach operations to existing running containers not being able to bind IO again. The issue won't cause failures in API calls, however data won't be sent or received. This includes data for attach and logs CLIs and APIs through the cluster API server.

#### Solution

To resolve this issue, upgrade to patched container runtime version (1.5.7-gke.1) with newer GKE releases.

## `/etc/mtab`: No such file or directory

The Docker container runtime populates this symlink inside the container by default, but the containerd runtime does not.

For more details, refer to [GitHub issue #2419](https://github.com/containerd/containerd/issues/2419).

### Solution

To resolve this issue, manually create the symlink `/etc/mtab` during your image build.
    
    
    ln -sf /proc/mounts /etc/mtab
    

## Image pull error: not a directory

_Affected GKE versions:_ all

When you build an image with [kaniko](https://github.com/GoogleContainerTools/kaniko), it might fail to be pulled with containerd with the error message "not a directory". This error happens if the image is built in a special way: when a previous command removes a directory and the next command recreates the same files in that directory.

The following Dockerfile example with `npm` that illustrates this problem.
    
    
    RUN npm cache clean --force
    RUN npm install
    

For more details, refer to [GitHub issue #4659](https://github.com/containerd/containerd/issues/4659).

### Solution

To resolve this issue, build your image using `docker build`, which is unaffected by this issue.

If `docker build` isn't an option for you, then combine the commands into one. The following Dockerfile example combines `RUN npm cache clean --force` and `RUN npm install`:
    
    
    RUN npm cache clean --force && npm install
    

## Some file system metrics are missing and the metrics format is different

**Note:** This issue doesn't affect customers that use [Cloud Monitoring](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes).

_Affected GKE versions:_ all

The Kubelet `/metrics/cadvisor` endpoint provides Prometheus metrics, as documented in [Metrics for Kubernetes system components](https://kubernetes.io/docs/concepts/cluster-administration/system-metrics/). If you install a metrics collector that depends on that endpoint, you might see the following issues:

  * The metrics format on the Docker node is `k8s_<container-name>_<pod-name>_<namespace>_<pod-uid>_<restart-count>` but the format on the containerd node is `<container-id>`.
  * Some file system metrics are missing on the containerd node, as follows:
        
        container_fs_inodes_free
        container_fs_inodes_total
        container_fs_io_current
        container_fs_io_time_seconds_total
        container_fs_io_time_weighted_seconds_total
        container_fs_limit_bytes
        container_fs_read_seconds_total
        container_fs_reads_merged_total
        container_fs_sector_reads_total
        container_fs_sector_writes_total
        container_fs_usage_bytes
        container_fs_write_seconds_total
        container_fs_writes_merged_total
        




### Solution

You can mitigate this issue by using [cAdvisor](https://github.com/google/cadvisor) as a standalone daemonset.

  1. Find the latest [cAdvisor release](https://github.com/google/cadvisor/releases) with the name pattern `vX.Y.Z-containerd-cri` (for example, `v0.42.0-containerd-cri`).
  2. Follow the steps in [cAdvisor Kubernetes Daemonset](https://github.com/google/cadvisor/tree/master/deploy/kubernetes) to create the daemonset.
  3. Point the installed metrics collector to use the cAdvisor `/metrics` endpoint that provides the full set of [Prometheus container metrics](https://github.com/google/cadvisor/blob/master/docs/storage/prometheus.md).



### Alternatives

  1. Migrate your monitoring solution to [Cloud Monitoring](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes), which provides the full set of container metrics.
  2. Collect metrics from the [Kubelet summary API](https://pkg.go.dev/k8s.io/kubelet/pkg/apis/stats/v1alpha1) with an endpoint of `/stats/summary`.



## Exec probe behavior difference when probe exceeds the timeout

_Affected GKE versions:_ all

Exec probe behavior on containerd images is different from the behavior on `dockershim` images. When exec probe that is defined for the Pod exceeds the declared [Kubernetes `timeoutSeconds`](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#configure-probes) threshold, on `dockershim` images, it is treated as a probe failure. On containerd images, probe results returned after the declared `timeoutSeconds` threshold are ignored.

### Solution

In GKE, the feature gate `ExecProbeTimeout` is set to `false` and cannot be changed. To resolve this issue, increase the `timeoutSeconds` threshold for all affected exec probes or implement the timeout functionality as part of the probe logic.

## Troubleshoot issues with private registries

This section provides troubleshooting information for private registry configurations in containerd.

### Image pull fails with error x509: certificate signed by unknown authority

This issue occurs if GKE couldn't find a certificate for a specific private registry domain. You can check for this error in Cloud Logging using the following query:

  1. Go to the **Logs Explorer** page in the Google Cloud console:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Run the following query:
         
         ("Internal error pulling certificate" OR
         "Failed to get credentials from metadata server" OR
         "Failed to install certificate")
         




To resolve this issue, try the following:

  1. In GKE Standard, open the configuration file exists in the following path:
         
         /etc/containerd/hosts.d/DOMAIN/config.toml
         

Replace `DOMAIN` with the FQDN for the registry.

  2. Verify that your configuration file contains the correct FQDN.

  3. Verify that the path to the certificate in the `secretURI` field in the configuration file is correct.

  4. Verify that the certificate exists in Secret Manager.




### Certificate not present

This issue occurs if GKE couldn't pull the certificate from Secret Manager to configure containerd on your nodes. If GKE can't access the certificate, the node boots without the certificate. Workloads that run on the node can't access your private registry.

To resolve this issue, try the following:

  1. Ensure that the affected node runs Container-Optimized OS. Ubuntu and Windows nodes aren't supported.
  2. In your configuration file, ensure that the path to the secret in the `secretURI` field is correct.
  3. Check that your cluster's IAM service account has the correct [permissions](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/access-private-registries-private-certificates#configure-secret-manager-access-gke) to access the secret.
  4. Check that the cluster has the `cloud-platform` access scope. For instructions, see [Check access scopes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/access-private-registries-private-certificates#check-access-scopes).
  5. Re-create the node by using one of the following methods:

     * [Upgrade the node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#upgrade_nodes) to the same GKE version that it already uses.
     * [Migrate the workloads to a node pool](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/node-pools#migrate-node-pools) that has access to the certificate.
     * [Drain the problematic node](https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/), and then [delete the host instance in Compute Engine](https://docs.cloud.google.com/compute/docs/instances/deleting-instance).



### Insecure registry option is not configured for local network (10.0.0.0/8)

_Affected GKE versions:_ all

On containerd images, the insecure registry option is **not** configured for local network `10.0.0.0/8`. If you use insecure private registries, you might notice errors similar to the following:
    
    
    pulling image: rpc error: code = Unknown desc = failed to pull and unpack image "IMAGE_NAME": failed to do request: Head "IMAGE_NAME": http: server gave HTTP response to HTTPS client
    

To resolve this issue, try the following:

  * Use [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos)
  * Configure TLS on your private registries if your use case supports this option. You can use a _containerd configuration file_ to tell GKE to use certificates that you store in Secret Manager to access your private registry. For instructions, see [Access private registries with private CA certificates](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/access-private-registries-private-certificates).



#### Configure privileged DaemonSets to modify your containerd configuration

For Standard clusters, try the following steps. This workaround isn't available in Autopilot because privileged containers are a security risk. If your environment is exposed to the internet, consider your risk tolerance before deploying this solution. In all cases, we strongly recommend that you configure TLS for your private registry and use the Secret Manager option instead.

**Caution:** This operation requires a containerd restart, which might cause disruptions in workloads that are already running on the node.

  1. Review the following manifest:
         
         apiVersion: apps/v1
         kind: DaemonSet
         metadata:
           name: insecure-registries
           namespace: default
           labels:
             k8s-app: insecure-registries
         spec:
           selector:
             matchLabels:
               name: insecure-registries
           updateStrategy:
             type: RollingUpdate
           template:
             metadata:
               labels:
                 name: insecure-registries
             spec:
               nodeSelector:
                 cloud.google.com/gke-container-runtime: "containerd"
               hostPID: true
               containers:
                 - name: startup-script
                   image: gke.gcr.io/startup-script:v2
                   imagePullPolicy: Always
                   securityContext:
                     privileged: true
                   env:
         ** - name: ADDRESS**
         ** value: "REGISTRY_ADDRESS"**
                   - name: STARTUP_SCRIPT
                     value: |
                       set -o errexit
                       set -o pipefail
                       set -o nounset
         
                       if [[ -z "$ADDRESS" || "$ADDRESS" == "REGISTRY_ADDRESS" ]]; then
                         echo "Error: Environment variable ADDRESS is not set in containers.spec.env"
                         exit 1
                       fi
         
                       echo "Allowlisting insecure registries..."
                       containerd_config="/etc/containerd/config.toml"
                       hostpath=$(sed -nr 's;  config_path = "([-/a-z0-9_.]+)";\1;p' "$containerd_config")
                       if [[ -z "$hostpath" ]]; then
                         echo "Node uses CRI config model V1 (deprecated), adding mirror under $containerd_config..."
                         grep -qxF '[plugins."io.containerd.grpc.v1.cri".registry.mirrors."'$ADDRESS'"]' "$containerd_config" || \
                           echo -e '[plugins."io.containerd.grpc.v1.cri".registry.mirrors."'$ADDRESS'"]\n  endpoint = ["http://'$ADDRESS'"]' >> "$containerd_config"
                       else
                         host_config_dir="$hostpath/$ADDRESS"
                         host_config_file="$host_config_dir/hosts.toml"
                         echo "Node uses CRI config model V2, adding mirror under $host_config_file..."
                         if [[ ! -e "$host_config_file" ]]; then
                           mkdir -p "$host_config_dir"
                           echo -e "server = \"https://$ADDRESS\"\n" > "$host_config_file"
                         fi
                         echo -e "[host.\"http://$ADDRESS\"]\n  capabilities = [\"pull\", \"resolve\"]\n" >> "$host_config_file"
                       fi
                       echo "Reloading systemd management configuration"
                       systemctl daemon-reload
                       echo "Restarting containerd..."
                       systemctl restart containerd

In the `.spec.containers.env` field, replace the `REGISTRY_ADDRESS` value of the `ADDRESS` variable with the address of your local HTTP registry in the format `DOMAIN_NAME:PORT`. For example,
         
         containers:
         - name: startup-script
           ...
           env:
           - name: ADDRESS
             value: "example.com:5000"
         

  2. Deploy the DaemonSet:
         
         kubectl apply -f insecure-registry-ds.yaml
         




The DaemonSet adds your insecure registry to the containerd configuration on every node.

## containerd ignores any device mappings for privileged pods

_Affected GKE versions:_ all

For [privileged Kubernetes Pods](https://kubernetes.io/docs/concepts/policy/pod-security-policy/#privileged), the container runtime ignores any device mappings that `volumeDevices.devicePath` pass to it, and instead makes every device on the host available to the container under `/dev`.

## containerd leaks shim processes when nodes are under I/O pressure

_Affected GKE versions: 1.25.0 to 1.25.15-gke.1040000, 1.26.0 to 1.26.10-gke.1030000, 1.27.0 to 1.27.6-gke.1513000, and 1.28.0 to 1.28.3-gke.1061000_

When a GKE node is under I/O pressure, containerd might fail to delete the `containerd-shim-runc-v2` processes when a Pod is deleted, resulting in process leaks. When the leak happens on a node, you'll see more `containerd-shim-runc-v2` processes on the node than the number of Pods on that node. You might also see increased memory and CPU usage along with extra PIDs. For details, see the GitHub issue [Fix leaked shim caused by high IO pressure](https://github.com/containerd/containerd/pull/8954).

To resolve this issue, [upgrade your nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#upgrade_cp) to the following versions or later:

  * 1.25.15-gke.1040000
  * 1.26.10-gke.1030000
  * 1.27.6-gke.1513000
  * 1.28.3-gke.1061000



## IPv6 address family is enabled on pods running containerd

_Affected GKE versions:_ 1.18, 1.19, 1.20.0 to 1.20.9

IPv6 image family is enabled for Pods running with containerd. The `dockershim` image disables IPv6 on all Pods, while the containerd image does not. For example, `localhost` resolves to IPv6 address `::1` first. This typically isn't a problem, but this might result in unexpected behavior in certain cases.

### Solution

To resolve this issue, use an IPv4 address such as `127.0.0.1` explicitly, or configure an application running in the Pod to work on both address families.

## Conflict with `172.17/16` IP address range

_Affected GKE versions:_ 1.18.0 to 1.18.14

The `172.17/16` IP address range is occupied by the `docker0` interface on the node VM with containerd enabled. Traffic sending to or originating from that range might not be routed correctly (for example, a Pod might not be able to connect to a VPN-connected host with an IP address within `172.17/16`).

## GPU metrics not collected

_Affected GKE versions:_ 1.18.0 to 1.18.18

[GPU usage metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus#monitoring) are not collected when using containerd as a runtime on GKE versions before 1.18.18.

### Solution

To resolve this issue, upgrade your clusters to GKE versions 1.18.18 or later.

## Images with `config.mediaType` set to `application/octet-stream` can't be used on containerd

_Affected GKE versions:_ all

Images with `config.mediaType` set to `"application/octet-stream"` cannot be used on containerd. For more information, see [GitHub issue #4756](https://github.com/containerd/containerd/issues/4756#issuecomment-731287262). These images are not compatible with the Open Container Initiative specification and are considered incorrect. These images work with Docker to provide backward compatibility, while in containerd these images are not supported.

### Symptom and diagnosis

Example error in node logs:
    
    
    Error syncing pod <pod-uid> ("<pod-name>_<namespace>(<pod-uid>)"), skipping: failed to "StartContainer" for "<container-name>" with CreateContainerError: "failed to create containerd container: error unpacking image: failed to extract layer sha256:<some id>: failed to get reader from content store: content digest sha256:<some id>: not found"
    

The image manifest can usually be found in the registry where it is hosted. Once you have the manifest, check `config.mediaType` to determine if you have this issue:
    
    
    "mediaType": "application/octet-stream",
    

### Solution

As the containerd community decided to not support such images, all versions of containerd are affected and there is no fix. The container image must be rebuilt with Docker version 1.11 or later and you must ensure that the `config.mediaType` field is not set to `"application/octet-stream"`.

## CNI not initialized

_Affected GKE versions:_ all

If you see an error similar to the following, the Container Network Interface (CNI) config isn't ready:
    
    
    Error: "network is not ready: container runtime network not ready: NetworkReady=false reason:NetworkPluginNotReady message:Network plugin returns error: cni plugin not initialized".
    

There are two main reasons that this error occurs:

  * The CNI hasn't finished installing
  * The webhook is misconfigured



### Ensure the CNI has finished installation

You might see this error in your log files during node bootstrapping while GKE installs the CNI config. If you see this error, but GKE is creating all nodes correctly, you can safely ignore this error.

This situation can happen because the CNI provides Pods with their network connectivity, so Pods need the CNI to work. However, Kubernetes uses taints to mark nodes that aren't ready and system Pods can tolerate these taints. This means that system Pods can start on a new node before the network is ready, resulting in the error.

To resolve this issue, wait for GKE to finish installing the CNI config. After CNI finishes configuring the network, the system Pods start successfully with no intervention required.

### Fix misconfigured webhooks

If the CNI not initialized error persists and you notice that GKE is failing to create nodes during an upgrade, resize, or other action, you might have a misconfigured webhook.

If you have a custom webhook that intercepts the DaemonSet controller command to create a Pod and that webhook is misconfigured, you might see the error as a node error status in the Google Cloud console. This misconfiguration prevents GKE from creating a `netd` or `calico-node` Pod. If the `netd` or `calico-node` Pods started successfully while the error persists, [contact Customer Care](https://docs.cloud.google.com/support/docs).

To fix any misconfigured webhooks, complete the following steps:

  1. [Identify misconfigured webhooks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-webhooks#identify-webhooks).

If you're using a cluster with Dataplane V1 network policy enforcement enabled, you can also check the status of the `calico-typha` Pod for information about which webhooks are causing this error:
         
         kubectl describe pod -n kube-system -l k8s-app=calico-typha
         

If the Pod has an error, the output is similar to the following:
         
         Events:
         Type     Reason        Age                     From                   Message
         ----     ------        ----                    ----                   -------
         Warning  FailedCreate  9m15s (x303 over 3d7h)  replicaset-controller  Error creating: admission webhook WEBHOOK_NAME denied the request [...]
         

In this output, `WEBHOOK_NAME` is the name of a failing webhook. Your output might include information about a different type of error.

  2. If you want to keep the misconfigured webhooks, [troubleshoot them](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-webhooks#troubleshoot-webhooks). If they're not required, delete them by running the following commands:
         
         kubectl delete mutatingwebhookconfigurations WEBHOOK_NAME
         kubectl delete validatingwebhookconfigurations WEBHOOK_NAME
         

Replace `WEBHOOK_NAME` with the name of the misconfigured webhook that you want to remove.

  3. Configure your webhooks to [ignore system Pods](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/#avoiding-operating-on-the-kube-system-namespace).




## What's next

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further help, including advice on the following topics:

    * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
    * Getting support from the community by [asking questions on StackOverflow](http://stackoverflow.com/questions/tagged/google-kubernetes-engine) and using the `google-kubernetes-engine` tag to search for similar issues. You can also join the [`#kubernetes-engine` Slack channel](https://googlecloud-community.slack.com/messages/C0B9GKTKJ/) for more community support.
    * Opening issues or feature requests by using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
