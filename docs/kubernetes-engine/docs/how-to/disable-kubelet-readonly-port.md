---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/disable-kubelet-readonly-port/
title: Disable the kubelet read-only port in GKE clusters \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:01.482382+00:00
---

# Disable the kubelet read-only port in GKE clusters  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/disable-kubelet-readonly-port/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  Disable the kubelet read-only port in GKE clusters Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to disable the insecure kubelet read-only port in Google Kubernetes Engine (GKE) clusters to reduce the risk of unauthorized access to the kubelet, and how to migrate applications to a more secure port.

In Kubernetes clusters, including GKE, the `kubelet` process running on nodes serves a read-only API using the insecure port `10255`. Kubernetes doesn't perform any authentication or authorization checks on this port. The kubelet serves the same endpoints on the more secure, authenticated port `10250`.

**Disable the kubelet read-only port and switch any workloads that use port`10255` to use the more secure port `10250` instead.**

**Note:** The kubelet read-only port is disabled by default in new clusters that run version 1.32 or later.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure that you have an existing Autopilot or Standard cluster. To create a new cluster, see [Create an Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster).



### Requirements

  * You can only disable the insecure kubelet read-only port in GKE version 1.26.4-gke.500 or later.



## Check for insecure port usage and migrate applications

Before you disable the insecure read-only port, migrate any of your running applications that use the port to the more secure read-only port. Workloads that might need migration include custom metrics pipelines and workloads that access kubelet endpoints.

  * For workloads that need access to the information served by the kubelet API on the node, like metrics, use port `10250`.
  * For workloads that get Kubernetes information using the kubelet API on the node, like listing Pods on the node, use the Kubernetes API instead.



### Check whether applications use the insecure kubelet read-only port

This section shows you how to check for insecure port usage in your cluster.

#### Check for port usage on Autopilot mode

To check for port usage in an Autopilot cluster, ensure that you have at least one workload that isn't a DaemonSet running in the cluster. If you perform the following steps on an empty Autopilot cluster, the results might be invalid.

  1. Save the following manifest as `read-only-port-metrics.yaml`:
         
         # Create a namespace for the DaemonSet that checks for port usage.
         apiVersion: v1
         kind: Namespace
         metadata:
           name: node-metrics-printer-namespace
         ---
         # Grant access to read node metrics in the cluster.
         apiVersion: rbac.authorization.k8s.io/v1
         kind: ClusterRole
         metadata:
           name: node-metrics-printer-role
         rules:
         - apiGroups:
           - ""
           resources:
           - nodes/metrics
           verbs:
           - get
         ---
         apiVersion: rbac.authorization.k8s.io/v1
         kind: ClusterRoleBinding
         metadata:
           name: node-metrics-printer-binding
         roleRef:
           apiGroup: rbac.authorization.k8s.io
           kind: ClusterRole
           name: node-metrics-printer-role
         # Bind the ClusterRole to the ServiceAccount that the DaemonSet will use.
         subjects:
         - kind: ServiceAccount
           name: node-metrics-printer-sa
           namespace: node-metrics-printer-namespace
         ---
         # Create a ServiceAccount for the DaemonSet.
         apiVersion: v1
         kind: ServiceAccount
         metadata:
           name: node-metrics-printer-sa
           namespace: node-metrics-printer-namespace
         ---
         apiVersion: apps/v1
         kind: DaemonSet
         metadata:
           name: node-metrics-printer
           namespace: node-metrics-printer-namespace
         spec:
           selector:
             matchLabels:
               app: node-metrics-printer
           template:
             metadata:
               labels:
                 app: node-metrics-printer
             spec:
               # Assign the ServiceAccount to the DaemonSet.
               serviceAccountName: node-metrics-printer-sa
               containers:
               - name: metrics-printer
                 image: us-docker.pkg.dev/cloud-builders/ga/v1/curl:latest
                 command: ["sh", "-c"]
                 # Call the /metrics endpoint using the insecure kubelet read-only
                 # port.
                 args:
                 - 'while true; do curl -s --cacert "${CA_CERT}" -H "Authorization: Bearer $(cat ${TOKEN_FILE})" "https://${NODE_ADDRESS}:10250/metrics"|grep kubelet_http_requests_total; sleep 20; done'
                 env:
                 # Provide credentials and the IP address for the command.
                 - name: CA_CERT
                   value: /var/run/secrets/kubernetes.io/serviceaccount/ca.crt
                 - name: TOKEN_FILE
                   value: /var/run/secrets/kubernetes.io/serviceaccount/token
                 - name: NODE_ADDRESS
                   valueFrom:
                     fieldRef:
                       fieldPath: status.hostIP
         

This manifest does the following:

     1. Creates a namespace and sets up RBAC roles to allow reading node metrics.
     2. Deploys a DaemonSet that checks the kubelet metrics for the insecure read-only port.
  2. Deploy the manifest:
         
         kubectl create -f read-only-port-metrics.yaml
         

  3. Check the DaemonSet logs:
         
         kubectl logs --namespace=node-metrics-printer-namespace \
             --all-containers --prefix \
             --selector=app=node-metrics-printer
         

If the output has any results that contain the string `server_type=readonly`, an application is using the insecure read-only port.




#### Check for port usage on Standard mode

Run the following command on at least one node in every node pool in your cluster:
    
    
    kubectl get --raw /api/v1/nodes/NODE_NAME/proxy/metrics | grep http_requests_total | grep readonly
    

Replace `NODE_NAME` with the name of the node.

If the output contains entries with the `server_type="readonly"` string, then the following scenarios can occur:

  * Workloads on the node use the insecure kubelet read-only port.
  * After disabling the insecure port, the command still returns the `server_type="readonly"` string. This is because the `kubelet_http_requests_total` metric represents the cumulative number of HTTP requests received by the kubelet server since its last restart. This number is not reset when the insecure port is disabled. This number is reset after GKE restarts the kubelet server, such as during a node upgrade. To learn more, see [Kubernetes Metrics Reference](https://kubernetes.io/docs/reference/instrumentation/metrics/).



If the output is empty, no workloads on that node use the insecure read-only port.

### Identify the workloads that are using the insecure kubelet read-only port

To identify the workloads that are using the insecure port, check the workload's configuration files such as ConfigMaps and Pods.

Run the following commands:
    
    
    kubectl get pods --all-namespaces -o yaml | grep 10255
    kubectl get configmaps --all-namespaces -o yaml | grep 10255
    

If the output of the command is not empty, use the following script to identify the names of the ConfigMaps or Pods that are using the insecure port:
    
    
    # This function checks if a Kubernetes resource is using the insecure port 10255.
    #
    # Arguments:
    #  $1 - Resource type (e.g., pod, configmap, )
    #  $2 - Resource name
    #  $3 - Namespace
    #
    # Output:
    #  Prints a message indicating whether the resource is using the insecure port.
    isUsingInsecurePort() {
      resource_type=$1
      resource_name=$2
      namespace=$3
    
      config=$(kubectl get $resource_type $resource_name -n $namespace -o yaml)
    
      # Check if kubectl output is empty
      if [[ -z "$config" ]]; then
        echo "No configuration file detected for $resource_type: $resource_name (Namespace: $namespace)"
        return
      fi
    
      if echo "$config" | grep -q "10255"; then
        echo "Warning: The configuration file ($resource_type: $namespace/$resource_name) is using insecure port 10255. It is recommended to migrate to port 10250 for enhanced security."
      else
        echo "Info: The configuration file ($resource_type: $namespace/$resource_name) is not using insecure port 10255."
      fi
    }
    
    # Get the list of ConfigMaps with their namespaces
    configmaps=$(kubectl get configmaps -A -o custom-columns=NAMESPACE:.metadata.namespace,NAME:.metadata.name | tail -n +2 | awk '{print $1"/"$2}')
    
    # Iterate over each ConfigMap
    for configmap in $configmaps; do
      namespace=$(echo $configmap | cut -d/ -f1)
      configmap_name=$(echo $configmap | cut -d/ -f2)
      isUsingInsecurePort "configmap" "$configmap_name" "$namespace"
    done
    
    # Get the list of Pods with their namespaces
    pods=$(kubectl get pods -A -o custom-columns=NAMESPACE:.metadata.namespace,NAME:.metadata.name | tail -n +2 | awk '{print $1"/"$2}')
    
    # Iterate over each Pod
    for pod in $pods; do
      namespace=$(echo $pod | cut -d/ -f1)
      pod_name=$(echo $pod | cut -d/ -f2)
      isUsingInsecurePort "pod" "$pod_name" "$namespace"
    done
    

Once you've identified the relevant workloads, migrate them to use the secure port 10250 by completing the steps in the following section.

### Migrate from the insecure kubelet read-only port

Typically, migrating an application to the secure port involves the following steps:

  1. Update URLs or endpoints that refer to the insecure read-only port to use the secure read-only port instead. For example, change `http://203.0.113.104:10255` to `http://203.0.113.104:10250`.

  2. Set the certificate authority (CA) certificate of the HTTP client to the cluster CA certificate. To find this certificate, run the following command:
         
         gcloud container clusters describe CLUSTER_NAME \
             --location=LOCATION \
             --format="value(masterAuth.clusterCaCertificate)"
         

Replace the following:

     * `CLUSTER_NAME`: the name of your cluster.
     * `LOCATION`: the location of your cluster.



The authenticated port `10250` requires that you grant appropriate RBAC roles to the subject to access the specific resources. For details, in the Kubernetes documentation, see [kubelet authorization](https://kubernetes.io/docs/reference/access-authn-authz/kubelet-authn-authz/#kubelet-authorization).

If your workload uses the `/pods` endpoint on the insecure kubelet read-only port, you need to grant the `nodes/proxy` RBAC permission to access the endpoint on the secure kubelet port. `nodes/proxy` is a powerful permission that you can't grant in GKE Autopilot clusters and that you shouldn't grant in GKE Standard clusters. Use the Kubernetes API with a [`fieldSelector`](https://kubernetes.io/docs/concepts/overview/working-with-objects/field-selectors/) for the node name instead.

If you use third-party applications that depend on the insecure kubelet read-only port, check with the application vendor for instructions to migrate to secure port `10250`.

### Example migration

Consider a Pod that queries metrics from the insecure kubelet read-only port.
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: kubelet-readonly-example
    spec:
      restartPolicy: Never
      containers:
      - name: kubelet-readonly-example
        image: us-docker.pkg.dev/cloud-builders/ga/v1/curl:latest
        command:
          - curl
          - http://${NODE_ADDRESS}:10255/metrics
        env:
        - name: NODE_ADDRESS
          valueFrom:
            fieldRef:
              fieldPath: status.hostIP
    

This application does the following:

  * Uses the `default` ServiceAccount in the `default` namespace
  * Runs the `curl` command against the `/metrics` endpoint on the node.



To update this Pod to use the secure port `10250`, do the following steps:

  1. Create a ClusterRole with access to get node metrics:
         
         apiVersion: rbac.authorization.k8s.io/v1
         kind: ClusterRole
         metadata:
           name: curl-authenticated-role
         rules:
         # Grant access to read node metrics in the cluster.
         - apiGroups:
           - ""
           resources:
           - nodes/metrics
           verbs:
           - get
         

  2. Bind the ClusterRole to your application's identity:
         
         apiVersion: rbac.authorization.k8s.io/v1
         kind: ClusterRoleBinding
         metadata:
           name: curl-authenticated-role-binding
         roleRef:
           apiGroup: rbac.authorization.k8s.io
           kind: ClusterRole
           name: curl-authenticated-role
         # Bind the ClusterRole to the default ServiceAccount in the default
         # namespace.
         subjects:
         - kind: ServiceAccount
           name: default
           namespace: default
         

  3. Update the `curl` command to use the secure port endpoint with the corresponding authorization headers:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: kubelet-authenticated-example
         spec:
           restartPolicy: Never
           containers:
           - name: kubelet-readonly-example
             image: us-docker.pkg.dev/cloud-builders/ga/v1/curl:latest
             env:
             - name: NODE_ADDRESS
               valueFrom:
                 fieldRef:
                   fieldPath: status.hostIP
             # Update the command to send a request with the ServiceAccount
             # credentials in the header.
             **command :
             - sh
             - -c
             - 'curl -s --cacert /var/run/secrets/kubernetes.io/serviceaccount/ca.crt -H "Authorization:
               Bearer $(cat /var/run/secrets/kubernetes.io/serviceaccount/token)" https://${NODE_ADDRESS}:10250/metrics'**
         




## Modify VPC firewall rules

If you update workloads to use port `10250`, create firewall rules so that Pods in the cluster can reach the port in your node IP address ranges. The firewall rules should do the following:

  * Allow incoming traffic to TCP port `10250` on your node IP address ranges from internal Pod IP address ranges
  * Deny incoming traffic to TCP port `10250` on your node IP address ranges from the public internet.

**Caution:** Don't modify the default firewall rules that GKE creates in your clusters. Create new rules for the secure port. Modifying the default rules might result in unexpected behavior in your workloads.

You can use the following [default GKE firewall rules](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/firewall-rules#cluster-fws) as a template for the parameters to specify in your new rules:

  * `gke-[cluster-name]-[cluster-hash]-inkubelet`
  * `gke-[cluster-name]-[cluster-hash]-exkubelet`



## Disable the insecure read-only port on Autopilot clusters

You can disable the insecure kubelet read-only port for new and existing Autopilot clusters.

To disable the insecure kubelet read-only port on an Autopilot cluster, use the `--no-autoprovisioning-enable-insecure-kubelet-readonly-port` flag, like in the following command. All new and existing nodes in the cluster stop using the port.

**Caution:** This command starts a rolling update of all the nodes in your cluster, which might cause disruptions in running workloads.
    
    
    gcloud container clusters update CLUSTER_NAME \
        --location=LOCATION \
        --no-autoprovisioning-enable-insecure-kubelet-readonly-port
    

Replace the following:

  * `CLUSTER_NAME`: the name of your existing cluster.
  * `LOCATION`: the location of your existing cluster.



You can also use the `--no-autoprovisioning-enable-insecure-kubelet-readonly-port` flag when you create a new cluster by using the [gcloud container clusters create-auto](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto) command.

## Disable the insecure read-only port on Standard clusters

You can disable the insecure kubelet read-only port for entire Standard clusters or for individual node pools. We recommend that you disable the port for the entire cluster.

If you use node auto-provisioning, automatically provisioned node pools inherit the port setting that you specify at the cluster level. You can optionally specify a different setting for auto-provisioned node pools, but we recommend that you disable the port across all nodes in your cluster.

You can also use a [node system configuration file](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-system-config) to declaratively disable the insecure kubelet read-only port. If you use this file, you can't use the commands in the following sections to control the kubelet setting.

### Disable the insecure read-only port on existing Standard clusters

To disable the insecure kubelet read-only port on an existing Standard cluster, use the `--no-enable-insecure-kubelet-readonly-port` flag like in the following command. Any **new** node pools won't use the insecure port. GKE doesn't update existing node pools automatically.
    
    
    gcloud container clusters update CLUSTER_NAME \
        --location=LOCATION \
        --no-enable-insecure-kubelet-readonly-port
    

Replace the following:

  * `CLUSTER_NAME`: the name of your existing Standard cluster.
  * `LOCATION`: the location of your existing Standard cluster.



You can also use the `--no-autoprovisioning-enable-insecure-kubelet-readonly-port` flag when you create a new cluster by using the [gcloud container clusters create](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create) command.

### Disable the insecure read-only port on Standard node pools

We recommend that you set the read-only port setting at the cluster level in all cases. If you disabled the read-only port on an existing cluster that already had running node pools, use the following command to disable the port on those node pools.

**Caution:** This command starts a rolling update of the nodes in that node pool, which might cause disruptions in running workloads.
    
    
    gcloud container node-pools update NODE_POOL_NAME \
        --cluster=CLUSTER_NAME \
        --location=LOCATION \
        --no-enable-insecure-kubelet-readonly-port
    

Replace the following:

  * `NODE_POOL_NAME`: the name of your node pool.
  * `CLUSTER_NAME`: the name of the cluster.
  * `LOCATION`: the location of the cluster.



## Verify that the port is disabled

To verify that the insecure kubelet read-only port is disabled, describe the GKE resource.

### Check the port status in Autopilot clusters

Run the following command:
    
    
    gcloud container clusters describe CLUSTER_NAME \
        --location=LOCATION \
        --flatten=nodePoolAutoConfig \
        --format="value(nodeKubeletConfig)"
    

Replace the following:

  * `CLUSTER_NAME`: the name of your Autopilot cluster.
  * `LOCATION`: the location of your Autopilot cluster.



If the port is disabled, the output is the following:
    
    
    insecureKubeletReadonlyPortEnabled: false
    

### Check the port status in Standard clusters

The port status is available in the `nodePoolDefaults.nodeConfigDefaults.nodeKubeletConfig` field when you describe your cluster using the GKE API.

In Standard clusters, you'll also see a `nodeConfig` field that sets a value for the kubelet read-only port status. The `nodeConfig` field is deprecated and applies only to the default node pool that GKE creates when you create a new Standard mode cluster. The status of the port in the deprecated `nodeConfig` field doesn't apply to other node pools in the cluster.

Run the following command:
    
    
    gcloud container clusters describe CLUSTER_NAME \
        --location=LOCATION \
        --flatten=nodePoolDefaults.nodeConfigDefaults \
        --format="value(nodeKubeletConfig)"
    

Replace the following:

  * `CLUSTER_NAME`: the name of your Standard cluster.
  * `LOCATION`: the location of your Standard cluster.



If the port is disabled, the output is the following:
    
    
    insecureKubeletReadonlyPortEnabled: false
    

If the output of this command is blank, the insecure `kubelet` read-only port might still be enabled. To disable the port, run the command in the Disable the insecure read-only port on existing Standard clusters section.

### Check the port status in Standard node pools

Run the following command:
    
    
    gcloud container node-pools describe NODE_POOL_NAME \
        --cluster=CLUSTER_NAME \
        --location=LOCATION \
        --flatten=config \
        --format="value(kubeletConfig)"
    

Replace the following:

  * `NODE_POOL_NAME`: the name of your node pool.
  * `CLUSTER_NAME`: the name of the cluster.
  * `LOCATION`: the location of the cluster.



If the port is disabled, the output is the following:
    
    
    insecureKubeletReadonlyPortEnabled: false
    

## Prevent insecure port usage with an organization policy

You can use Organization Policy Service to enforce that clusters in your organization, folder, or project must disable the insecure `kubelet` read-only port. To enforce this requirement, you create a [custom constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints), and then reference that constraint in an organization policy. To deny creation or update operations when the insecure `kubelet` read-only port is enabled, see these examples:

  * The following custom constraint denies cluster creation or update operations if the insecure `kubelet` read-only port is enabled:
        
        name: organizations/ORGANIZATION_ID/customConstraints/custom.disableClusterInsecureKubeletReadOnlyPort
        resourceTypes:
        - container.googleapis.com/Cluster
        methodTypes:
        - CREATE
        - UPDATE
        condition:
          "resource.NodeKubeletConfig.insecureKubeletReadonlyPortEnabled == true ||
          resource.AutoprovisioningNodePoolDefaults.insecureKubeletReadonlyPortEnabled == true ||
          resource.NodePoolAutoConfig.NodeKubeletConfig.insecureKubeletReadonlyPortEnabled == true"
        actionType: DENY
        displayName: Disable insecure kubelet read-only port
        description: All new and existing clusters must disable the insecure kubelet read-only port.
        

Replace `ORGANIZATION_ID` with your organization ID.

  * The following custom constraint denies node pool creation or update operations if the insecure `kubelet` read-only port is enabled:
        
        name: organizations/ORGANIZATION_ID/customConstraints/custom.disableNodePoolInsecureKubeletReadOnlyPort
        resourceTypes:
        - container.googleapis.com/NodePool
        methodTypes:
        - CREATE
        - UPDATE
        condition: "resource.NodeConfig.NodeKubeletConfig.insecureKubeletReadonlyPortEnabled == true"
        actionType: DENY
        displayName: Disable insecure kubelet read-only port
        description: All new and existing node pools must disable the insecure kubelet read-only port.
        

Replace `ORGANIZATION_ID` with your organization ID.




For more information about how to create a custom constraint and enforce the constraint in an organization policy, see [Restrict actions on GKE resources using custom organization policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/custom-org-policies).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
