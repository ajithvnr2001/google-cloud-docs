---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/run-pods-default-compute-classes/
title: Apply ComputeClasses to Pods by default \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:31:58.576450+00:00
---

# Apply ComputeClasses to Pods by default  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/run-pods-default-compute-classes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Apply ComputeClasses to Pods by default Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document shows you how to apply ComputeClasses by default to Google Kubernetes Engine (GKE) Pods that don't explicitly select a ComputeClass. You can set a ComputeClass as the default for a namespace or for an entire cluster. This document is intended for cluster administrators who want to reduce manual overhead caused by individual workload and node configuration.

You should already be familiar with [custom ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes).

## About default ComputeClasses

You can configure GKE clusters or specific namespaces to have a _default_ ComputeClass. The default class that you configure applies to any Pod in that cluster or namespace that doesn't select a different ComputeClass. When you deploy a Pod that doesn't select a ComputeClass, GKE applies default ComputeClasses in the following order:

  1. If the namespace has a default ComputeClass, GKE modifies the Pod specification to select that ComputeClass.
  2. If the namespace doesn't have a default ComputeClass, the cluster-level default class applies. GKE doesn't modify the Pod specification.



When you set a default ComputeClass for a cluster or a namespace, your change applies only to new Pods. Existing Pods aren't affected until the Pods are re-created. This behavior applies even if your ComputeClass has active migration enabled.

If your default ComputeClass has the `activeMigration.optimizeRulePriority` field set to `true`, this setting might affect workloads in your clusters. For more information, see [Active migration in default ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes#default-ccc-and-active-migration).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Have a GKE Autopilot or Standard cluster that runs a version that supports setting a default ComputeClass at the cluster- or namespace-level. For more information, see the Requirements section.
  * If you're using a Standard mode cluster, ensure that you meet one of the following requirements:

    * Enable [autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler) on at least one node pool in the cluster.
    * If your Standard cluster runs a version earlier than 1.33.3-gke.1136000 and isn't enrolled in the Rapid release channel, [enable cluster-level node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning#enable-cluster-level).
  * If you want to set a custom ComputeClass as the default for a namespace, [deploy a custom ComputeClass](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-attributes-compute-classes#configure-compute-class-standard).




### Requirements

  * To set a ComputeClass as the cluster-level default, the cluster must run GKE version 1.33.1-gke.1744000 or later.
  * To set a ComputeClass as the namespace-level default for only non-DaemonSet Pods, the cluster must run GKE version 1.33.1-gke.1788000 or later.



### Required roles and permissions

To get the permissions that you need to configure cluster- or namespace-level default ComputeClasses, ask your administrator to grant you the following IAM roles on the Google Cloud project: 

  * [Kubernetes Engine Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.developer) (`roles/container.developer`)
  * Update the cluster-level default ComputeClass: [Kubernetes Engine Cluster Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.clusterAdmin) (`roles/container.clusterAdmin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to configure cluster- or namespace-level default ComputeClasses. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to configure cluster- or namespace-level default ComputeClasses:

  * `container.customResourceDefinitions.create`
  * `container.customResourceDefinitions.update`
  * `container.customResourceDefinitions.get`
  * `container.customResourceDefinitions.list`
  * `container.namespaces.get`
  * `container.namespaces.list`
  * `container.pods.get`
  * `container.nodes.get`
  * `container.nodes.list`
  * `container.deployments.create`
  * `container.deployments.get`
  * Add labels to namespaces: `container.namespaces.update`
  * Enable the cluster-level default ComputeClass: `container.clusters.update`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Configure a default ComputeClass for a namespace

You can annotate any Kubernetes namespace in your cluster with the name of a ComputeClass to use as the default. If a Pod that's deployed to that namespace doesn't already select a ComputeClass, GKE modifies the Pod specification to select the default class in the namespace. You can set any custom or built-in ComputeClass as the default.

  * To apply a ComputeClass to all Pods in a namespace by default, add the `cloud.google.com/default-compute-class` label to that namespace:
        
        kubectl label namespaces NAMESPACE_NAME \
            cloud.google.com/default-compute-class=COMPUTECLASS_NAME
        

Replace the following:

    * `NAMESPACE_NAME`: the name of the namespace to update.
    * `COMPUTECLASS_NAME`: the name of the ComputeClass to set as the default for the namespace.

If the command fails with the following error message, the namespace already has a default ComputeClass:
    
    error: 'cloud.google.com/default-compute-class' already has a value, and --overwrite is false
    

To resolve this error, update the default ComputeClass for the namespace.

  * To apply a ComputeClass to all non-DaemonSet Pods in a namespace by default, add the `cloud.google.com/default-compute-class-non-daemonset` label to that namespace:
        
        kubectl label namespaces NAMESPACE_NAME \
            cloud.google.com/default-compute-class-non-daemonset=COMPUTECLASS_NAME
        

If the command fails with the following error message, the namespace already has a default ComputeClass for non-DaemonSet Pods:
        
        error: 'cloud.google.com/default-compute-class-non-daemonset' already has a value, and --overwrite is false
        

To resolve this error, update the default ComputeClass for the namespace.




Your changes apply to any new Pods in that namespace. Existing Pods aren't affected.

### Update the existing default ComputeClass in a namespace

To overwrite the existing default ComputeClass for a namespace, run one of the following commands:

  * Update the default ComputeClass for all Pods in the namespace:
        
        kubectl label namespaces NAMESPACE_NAME   \
            cloud.google.com/default-compute-class=COMPUTECLASS_NAME \
            --overwrite
        

Replace the following:

    * `NAMESPACE_NAME`: the name of the namespace to update.
    * `COMPUTECLASS_NAME`: the name of the ComputeClass to set as the new default for the namespace.
  * Overwrite the default ComputeClass for non-DaemonSet Pods in the namespace:
        
        kubectl label namespaces NAMESPACE_NAME \
            cloud.google.com/default-compute-class-non-daemonset=COMPUTECLASS_NAME \
            --overwrite
        




### Configure a default ComputeClass for system namespaces

GKE uses system namespaces to run various managed workloads, such as monitoring agents. Some of these managed workloads are DaemonSets, which must run on every node in the cluster to provide critical functionality. However, you can specify a default ComputeClass for non-DaemonSet Pods in system namespaces, so that those Pods run separately from your workloads.

To set a default ComputeClass for system namespaces, follow these steps:

  1. Save the following script as `apply-system-cc.sh`. This script lets you apply a recommended ComputeClass or your own existing ComputeClass to system namespaces.
         
         #!/bin/bash
         
         # The recommended default ComputeClass name for system pods.
         DEFAULT_SYSTEM_CC_NAME="system-default-computeclass"
         
         # The YAML manifest for the recommended default ComputeClass for system pods.
         read -r -d '' DEFAULT_CC_YAML << EOF
         apiVersion: cloud.google.com/v1
         kind: ComputeClass
         metadata:
           name: ${DEFAULT_SYSTEM_CC_NAME}
         spec:
           nodePoolAutoCreation:
             enabled: true
           whenUnsatisfiable: ScaleUpAnyway
           priorities:
           - machineFamily: t2d
         EOF
         
         # The label key to apply to namespaces.
         LABEL_KEY="cloud.google.com/default-compute-class-non-daemonset"
         
         
         # List of GKE system namespaces.
         SYSTEM_NAMESPACES=(
           "kube-system"
           "gke-gmp-system"
           "gmp-system"
           "gke-managed-cim"
           "gke-managed-volumepopulator"
           "gke-managed-checkpointing"
           "gkebackup"
           "gke-managed-lustrecsi"
         )
         
         
         # 1. Ask the user for their choice.
         echo "This script sets a default ComputeClass for GKE system namespaces."
         echo "--------------------------------------------------------------------"
         echo "The following ComputeClass is recommended for system Pods:"
         echo ""
         echo "$DEFAULT_CC_YAML"
         echo "--------------------------------------------------------------------"
         read -p "Do you want to use the recommended ComputeClass? (y/N): " user_choice
         
         CC_TO_APPLY=""
         
         # 2. Process the user's choice.
         if [[ "$user_choice" =~ ^[Yy]$ ]]; then
           # Path 1: User chose YES.
           echo "Installing the recommended default ComputeClass '${DEFAULT_SYSTEM_CC_NAME}'..."
         
           if ! echo "$DEFAULT_CC_YAML" | kubectl apply -f -; then
               # If kubectl apply fails, print an error and exit.
               echo "❌ Error: Failed to create the default ComputeClass. An internal error occurred."
               echo "Check for kubectl permissions or other cluster issues and re-run the script."
               exit 1
           fi
           # If the command succeeded, set the name to be used for labeling.
           CC_TO_APPLY="$DEFAULT_SYSTEM_CC_NAME"
         
         else
           read -p "Specify the name of an existing ComputeClass to set as the default for system Pods: " custom_cc_name
         
           # Validate that the user entered a name.
           while [[ -z "$custom_cc_name" ]]; do
             echo "Error: Name cannot be empty."
             read -p "Specify the name of an existing ComputeClass: " custom_cc_name
           done
         
           # Check if the specified ComputeClass actually exists in the cluster.
           echo "--> Verifying that ComputeClass '${custom_cc_name}' exists..."
           if kubectl get computeclass "$custom_cc_name" > /dev/null 2>&1; then
             echo "Verified."
             CC_TO_APPLY="$custom_cc_name"
           else
             echo "Error: ComputeClass '${custom_cc_name}' doesn't exist in the cluster."
             echo "Create the ComputeClass, and then then re-run this script."
             exit 1
           fi
         fi
         
         echo ""
         echo "Labelling system namespaces with ComputeClass: '${CC_TO_APPLY}'"
         echo "--------------------------------------------------------------------"
         
         # 3. Apply the label to all system namespaces.
         for ns in "${SYSTEM_NAMESPACES[@]}"; do
           # Gracefully handle namespaces that don't exist on this specific cluster.
           if kubectl get namespace "${ns}" > /dev/null 2>&1; then
             echo "--> Applying label to namespace: ${ns}"
             kubectl label namespace "${ns}" \
               "${LABEL_KEY}=${CC_TO_APPLY}" --overwrite
           else
             echo "--> Skipping namespace ${ns} (does not exist)"
           fi
         done
         
         echo ""
         echo "✅ Script finished successfully."

This script uses the `cloud.google.com/default-compute-class-non-daemonset` label, which affects only non-DaemonSet Pods in system namespaces.

**Warning:** Don't set the `cloud.google.com/default-compute-class` label for a system namespace. This label affects DaemonSets and might cause disruptions to your cluster.
  2. Run the script:
         
         ./apply-system-cc.sh
         




After the script completes, all new non-DaemonSet system Pods use the specified ComputeClass by default, unless they already have a ComputeClass. Existing Pods in those namespaces aren't affected. If GKE adds new system namespaces, run this script again to apply changes to those namespaces.

To unset the default ComputeClass for system namespaces, follow these steps:

  1. Save the following script as `unset-system-cc.sh`:
         
         #!/bin/bash
         
         # The recommended default ComputeClass name for system pods.
         DEFAULT_SYSTEM_CC_NAME="system-default-computeclass"
         
         # The YAML manifest for the recommended default ComputeClass for system pods.
         read -r -d '' DEFAULT_CC_YAML << EOF
         apiVersion: cloud.google.com/v1
         kind: ComputeClass
         metadata:
           name: ${DEFAULT_SYSTEM_CC_NAME}
         spec:
           nodePoolAutoCreation:
             enabled: true
           whenUnsatisfiable: ScaleUpAnyway
           priorities:
           - machineFamily: t2d
         EOF
         
         # The label key to apply to namespaces.
         LABEL_KEY="cloud.google.com/default-compute-class-non-daemonset"
         
         
         # List of GKE system namespaces.
         SYSTEM_NAMESPACES=(
           "kube-system"
           "gke-gmp-system"
           "gmp-system"
           "gke-managed-cim"
           "gke-managed-volumepopulator"
           "gke-managed-checkpointing"
           "gkebackup"
           "gke-managed-lustrecsi"
         )
         
         
         # 1. Ask the user for their choice.
         echo "This script sets a default ComputeClass for GKE system namespaces."
         echo "--------------------------------------------------------------------"
         echo "The following ComputeClass is recommended for system Pods:"
         echo ""
         echo "$DEFAULT_CC_YAML"
         echo "--------------------------------------------------------------------"
         read -p "Do you want to use the recommended ComputeClass? (y/N): " user_choice
         
         CC_TO_APPLY=""
         
         # 2. Process the user's choice.
         if [[ "$user_choice" =~ ^[Yy]$ ]]; then
           # Path 1: User chose YES.
           echo "Installing the recommended default ComputeClass '${DEFAULT_SYSTEM_CC_NAME}'..."
         
           if ! echo "$DEFAULT_CC_YAML" | kubectl apply -f -; then
               # If kubectl apply fails, print an error and exit.
               echo "❌ Error: Failed to create the default ComputeClass. An internal error occurred."
               echo "Check for kubectl permissions or other cluster issues and re-run the script."
               exit 1
           fi
           # If the command succeeded, set the name to be used for labeling.
           CC_TO_APPLY="$DEFAULT_SYSTEM_CC_NAME"
         
         else
           read -p "Specify the name of an existing ComputeClass to set as the default for system Pods: " custom_cc_name
         
           # Validate that the user entered a name.
           while [[ -z "$custom_cc_name" ]]; do
             echo "Error: Name cannot be empty."
             read -p "Specify the name of an existing ComputeClass: " custom_cc_name
           done
         
           # Check if the specified ComputeClass actually exists in the cluster.
           echo "--> Verifying that ComputeClass '${custom_cc_name}' exists..."
           if kubectl get computeclass "$custom_cc_name" > /dev/null 2>&1; then
             echo "Verified."
             CC_TO_APPLY="$custom_cc_name"
           else
             echo "Error: ComputeClass '${custom_cc_name}' doesn't exist in the cluster."
             echo "Create the ComputeClass, and then then re-run this script."
             exit 1
           fi
         fi
         
         echo ""
         echo "Labelling system namespaces with ComputeClass: '${CC_TO_APPLY}'"
         echo "--------------------------------------------------------------------"
         
         # 3. Apply the label to all system namespaces.
         for ns in "${SYSTEM_NAMESPACES[@]}"; do
           # Gracefully handle namespaces that don't exist on this specific cluster.
           if kubectl get namespace "${ns}" > /dev/null 2>&1; then
             echo "--> Applying label to namespace: ${ns}"
             kubectl label namespace "${ns}" \
               "${LABEL_KEY}=${CC_TO_APPLY}" --overwrite
           else
             echo "--> Skipping namespace ${ns} (does not exist)"
           fi
         done
         
         echo ""
         echo "✅ Script finished successfully."

  2. Run the script:
         
         ./unset-system-cc.sh
         




## Configure a default ComputeClass for a cluster

You can set any custom ComputeClass as the default for your entire cluster. This process involves enabling cluster-level default ComputeClasses in your cluster, and then creating a ComputeClass that's named `default`. You can even get the behavior of the [built-in Autopilot ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-built-in-compute-classes) by specifying the same priority rules in a ComputeClass that's named `default`.

**Best practice** : If you set a cluster-level default ComputeClass, don't add ComputeClass node labels and taints to existing node pools in the cluster. GKE doesn't scale node pools that have node taints for other ComputeClasses when scheduling Pods that use the cluster-level default ComputeClass.

You must perform both of the following steps to correctly use a default ComputeClass in your cluster:

  1. To enable setting a cluster-level default ComputeClass for a cluster, use the [`--enable-default-compute-class` flag](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/update#--enable-default-compute-class) when you create or update a cluster:

     * **Create a cluster** :
           
           gcloud container clusters create CLUSTER_NAME \
               --location=CONTROL_PLANE_LOCATION \
               --enable-default-compute-class
           

Replace the following:

       * `CLUSTER_NAME`: a name for your cluster.
       * `CONTROL_PLANE_LOCATION`: the location of your cluster control plane, like `us-central1`.
     * **Update a cluster** :
           
           gcloud container clusters update CLUSTER_NAME \
               --location=CONTROL_PLANE_LOCATION \
               --enable-default-compute-class
           

Replace the following:

       * `CLUSTER_NAME`: the name of your cluster.
       * `CONTROL_PLANE_LOCATION`: the location of your cluster control plane, like `us-central1`.

After you complete this step, GKE looks for a ComputeClass named `default` in your cluster. You won't notice any changes to your workloads until you set up the `default` ComputeClass.

  2. Create a ComputeClass that's named `default`, like in the following examples:

     * The following ComputeClass requests specific machine series:
           
           apiVersion: cloud.google.com/v1
           kind: ComputeClass
           **metadata :
             name: default**
           spec:
             priorities:
             - machineFamily: n4
             - machineFamily: n2
             whenUnsatisfiable: ScaleUpAnyway
             nodePoolAutoCreation:
               enabled: true
           

This ComputeClass requests nodes that use N4 instances. If N4 instances aren't available, the ComputeClass requests N2 instances instead. You can configure the `default` ComputeClass with any of the available fields in the [ComputeClass CustomResourceDefinition](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass).

     * The following ComputeClass requests the Autopilot container-optimized compute platform:
           
           apiVersion: cloud.google.com/v1
           kind: ComputeClass
           **metadata :
             name: default**
           spec:
             autopilot:
               enabled: true
             priorities:
             - podFamily: general-purpose
             whenUnsatisfiable: ScaleUpAnyway
           

This ComputeClass matches the behavior of the `autopilot` built-in ComputeClass with the exception of the `whenUnsatisfiable` field, which has a value of `ScaleUpAnyway` instead of `DoNotScaleUp`. This modification helps to prevent situations where Pods that use a node selector for specific hardware remain in a pending state because the cluster-level default ComputeClass was applied to those Pods.

The `podFamily` priority rule places Pods on the Autopilot container-optimized compute platform. This priority rule requires GKE version 1.35.2-gke.1485000 or later.

  3. Create the `default` ComputeClass in your cluster:
         
         kubectl apply -f PATH_TO_MANIFEST
         

Replace `PATH_TO_MANIFEST` with the path to the manifest for the ComputeClass.

  4. Optional: If your Standard cluster already has manually created node pools that you use as the default for your general-purpose workloads, you can move those workloads to run in Autopilot mode after you set an Autopilot ComputeClass as the cluster-level default. To move those workloads, [cordon and drain all of the nodes in the node pools](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/node-pools#create-migrate). GKE uses the cluster-level default ComputeClass to schedule the new pending Pods.




After you set a cluster-level default ComputeClass, GKE scales node pools that meet both of the following requirements:

  * The node configuration is the same as the configuration of the `default` ComputeClass.
  * The node pool has no taints or labels for a different ComputeClass. GKE can scale node pools that have a taint and a label for the `default` ComputeClass.



For example, if the `default` ComputeClass specifies the N4 machine series, GKE can scale an existing node pool that uses N4 instances and doesn't have taints or labels for a different ComputeClass.

Your changes apply to all new Pods in the cluster that don't already have a ComputeClass. Existing Pods might be affected depending on the active migration settings of the cluster-level default ComputeClass. For more information, see [Active migration in default ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes#default-ccc-and-active-migration).

## Verify the default ComputeClass behavior

To check whether the default ComputeClass that you set for a namespace or for a cluster works as expected, do the following:

  1. Review the following example Deployment:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: helloweb
           labels:
             app: hello
         spec:
           selector:
             matchLabels:
               app: hello
               tier: web
           template:
             metadata:
               labels:
                 app: hello
                 tier: web
             spec:
               containers:
               - name: hello-app
                 image: us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0
                 ports:
                 - containerPort: 8080
                 resources:
                   requests:
                     cpu: 200m

This Deployment doesn't explicitly request a ComputeClass.

  2. Create the Deployment:
         
         kubectl apply --namespace=NAMESPACE_NAME \
             -f https://raw.githubusercontent.com/GoogleCloudPlatform/kubernetes-engine-samples/refs/heads/main/quickstarts/hello-app/manifests/helloweb-deployment.yaml
         

Replace `NAMESPACE_NAME` with one of the following, depending on what you want to verify:

     * The name of a namespace that has a default ComputeClass.
     * The name of a namespace that doesn't have a default ComputeClass.

GKE might take some time to create new nodes to run the Pods.

  3. Identify the nodes that run the Pods from the example Deployment:
         
         kubectl get pods --namespace=NAMESPACE_NAME \
             --selector=app=hello -o=wide
         

The output is similar to the following:
         
         NAME                        READY   STATUS    RESTARTS   AGE     IP          NODE                                                  NOMINATED NODE   READINESS GATES
         helloweb-7795fbf856-58n5l   1/1     Running   0          9m21s   10.52.2.3   gke-cluster-1-nap-n2-highcpu-2-3muqi8-f213e529-rx7d   <none>           <none>
         

  4. Get the node labels:
         
         kubectl get node NODE_NAME --show-labels \
             | grep "cloud.google.com/compute-class"
         

Replace `NODE_NAME` with the name of the node from the output of the previous step.

The output is similar to the following:
         
         NODE_NAME   Ready    <none>   22m   v1.32.4-gke.1236007
         # lines are omitted from this output
         **cloud.google.com/compute-class= COMPUTECLASS_NAME**,cloud.google.com/gke-boot-disk=pd-balanced,cloud.google.com/gke-container-runtime=containerd
         

The value in `COMPUTECLASS_NAME` is one of the following:

     * **Cluster-level default ComputeClass** : `default` for nodes that were created by GKE Autopilot or by node pool auto-creation. Nodes in existing manually created node pools might not have the `cloud.google.com/compute-class` label.
     * **Namespace-level default ComputeClass** : the name of the ComputeClass that you configured as the namespace default.



## Disable the default ComputeClass

To disable the default ComputeClass in a namespace or a cluster, do one of the following:

  * To disable the namespace-level default ComputeClass for all Pods, remove the `cloud.google.com/default-compute-class` label from the namespace:
        
        kubectl label namespaces NAMESPACE_NAME \
          cloud.google.com/default-compute-class-
        

The `-` character at the end of the label key removes any labels with that key from the `Namespace` object in the Kubernetes API.

  * To disable the namespace-level default ComputeClass for non-DaemonSet Pods, remove the `cloud.google.com/default-compute-class-non-daemonset` label from the namespace:
        
        kubectl label namespaces NAMESPACE_NAME \
          cloud.google.com/default-compute-class-non-daemonset-
        

  * To disable the cluster-level default ComputeClass, use the `gcloud container clusters update` command with the `--no-enable-default-compute-class` flag:
        
        gcloud container clusters update CLUSTER_NAME \
            --location=CONTROL_PLANE_LOCATION \
            --no-enable-default-compute-class
        




## What's next

  * Learn about [best practices for ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/computeclasses).
  * Learn more about [custom ComputeClasses in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
