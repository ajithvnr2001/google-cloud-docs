---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/automatically-bootstrapping-gke-nodes-with-daemonsets/
title: Automatically bootstrap GKE nodes with DaemonSets \u00a0|\u00a0 Kubernetes Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:25:48.359656+00:00
---

# Automatically bootstrap GKE nodes with DaemonSets  |  Kubernetes Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/automatically-bootstrapping-gke-nodes-with-daemonsets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Automatically bootstrap GKE nodes with DaemonSets Stay organized with collections  Save and categorize content based on your preferences. 

Standard 

This tutorial shows how to customize the nodes of a [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine) cluster by using [DaemonSets](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/). A DaemonSet helps ensure that all (or selected) nodes run a copy of a [Pod](https://kubernetes.io/docs/concepts/workloads/pods/pod/). When new nodes are added to a cluster, they also run a Pod from the DaemonSet.

If the tools and systems you use to initialize your clusters are different from the tools and systems you use to run your workloads, you increase the effort it takes to manage your environment. For example, if you use a configuration management tool to initialize the cluster nodes, you're relying on a procedure that's outside the runtime environment where the rest of your workloads run. Using a DaemonSet lets you use the same tools to orchestrate your workloads that you use to [modify your GKE nodes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images#modifications).

The goal of this tutorial is to help system administrators, system engineers, or infrastructure operators streamline the initialization of Kubernetes clusters.

**Caution:** Customizing your GKE nodes can lead to unintended behavior that might negatively affect the health of your workloads and nodes. Not all customizations are supported. Ensure that you implement extensive testing of any customizations before deploying them on clusters running production workloads. This tutorial uses a privileged container, which has security implications that you must review and understand.

Before reading this page, ensure that you're familiar with:

  * [Kubernetes](https://kubernetes.io/)
  * [GKE](https://docs.cloud.google.com/kubernetes-engine)
  * [Docker](https://www.docker.com/)
  * [`chroot`](https://wikipedia.org/wiki/Chroot)



In this tutorial, you learn to use Kubernetes taints and tolerations to help ensure that nodes are configured by a DaemonSet before application workloads can be scheduled on them.

## Objectives

In this tutorial you do the following:

  * Provision a GKE cluster.
  * Taint a node pool to prevent workload scheduling before applying the node configuration.
  * Deploy a DaemonSet that configures nodes and removes the taint.
  * Verify that cluster nodes are configured and the taint is removed.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [ GKE](https://docs.cloud.google.com/kubernetes-engine/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 




### Privileged DaemonSet security implications

Using the `securityContext: privileged: true` setting in a DaemonSet (or any Pod) is powerful but comes with significant security implications because it disables most container isolation boundaries for that Pod. You should be aware of the following security restrictions and risks that it introduces:

  * **Container escape or host compromise:** a vulnerability within the privileged container application or image can directly lead to root access on the host node.
  * **Violation of least privilege:** privileged mode grants _all_ capabilities, likely far more than needed for a specific task. This broad access increases the potential damage if the container is compromised.
  * **Node destabilization:** accidental or malicious commands could run within the privileged container, for example incorrect `sysctl` values or commands like `rm -rf /host/boot`. These types of commands can crash or corrupt the host node operating system.
  * **Lateral movement:** compromising one node through a privileged DaemonSet gives an attacker a strong foothold to attack other nodes, the Kubernetes control plane, or connected systems.
  * **Data exposure:** unrestricted access to the host file system (`/`) can expose sensitive data stored on the node, including credentials, keys, or data belonging to other Pods if they use hostPath volumes.
  * **Increased attack surface:** privileged mode exposes more of the host kernel system calls and features to potential exploits from within the container.



To avoid security risks, you should be aware of the following best practices and mitigations:

  * **Avoid using the privileged mode:** the most secure approach is to avoid the `privileged: true` setting entirely.
  * **Use Linux capabilities:** if elevated rights are needed, you can grant specific Linux capabilities such as `NET_ADMIN`, `SYS_ADMIN`, `SYS_MODULE` in the `securityContext.capabilities.add` field instead of full privilege. This approach follows the principle of least privilege, which we recommend over granting broad permissions.
  * **Limit scope:** run privileged DaemonSets only on dedicated, possibly tainted, node pools to contain the potential impact if a container is compromised.
  * **Enforce policies:** use tools like Policy Controller or Gatekeeper to create policies that restrict, audit, or require justification for deploying privileged containers.
  * **Scan and use trusted images:** use Binary Authorization and rigorous image scanning to help ensure only vetted, trusted container images are run with elevated privileges.
  * **Minimize host mounts:** only mount the specific host paths needed, and use `readOnly: true` whenever possible. Avoid mounting the entire root file system (`/`).
  * **Perform regular audits:** periodically review all workloads running with the `privileged: true` setting.



## Bootstrap the environment

In this section, you do the following:

  1. Enable the necessary [Cloud APIs](https://docs.cloud.google.com/apis).
  2. Provision a [service account](https://docs.cloud.google.com/compute/docs/access/service-accounts) with limited privileges for the nodes in the GKE cluster.
  3. Prepare the GKE cluster.
  4. Grant the user cluster administration privileges.



### Enable Cloud APIs

  1. Open Cloud Shell.

[OPEN Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. Select the Google Cloud project:
         
         gcloud config set project project-id
         

Replace `project-id` with the ID of the Google Cloud project that you created or selected for this tutorial.

  3. Enable the Kubernetes Engine API:
         
         gcloud services enable container.googleapis.com
         




### Provision a service account to manage GKE clusters

In this section, you create a [service account](https://docs.cloud.google.com/compute/docs/access/service-accounts) that is associated with the nodes in the cluster. In this tutorial, GKE nodes use this service account instead of the default service account. As a best practice, [grant the service account just the roles and access permissions that are required](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#use_least_privilege_sa) to run the application.

The roles required for the service account are as follows:

  * Monitoring Viewer role (`roles/monitoring.viewer`). This role gives read-only access to monitoring data.
  * Monitoring Metric Writer role (`roles/monitoring.metricWriter`). This role permits writing monitoring data.
  * Logs Writer role (`roles/logging.logWriter`). This role gives permissions to write logs.



To provision a service account, follow these steps:

  1. In Cloud Shell, initialize an environment variable that stores the service account name:
         
         GKE_SERVICE_ACCOUNT_NAME=ds-init-tutorial-gke
         

  2. Create a service account:
         
         gcloud iam service-accounts create "$GKE_SERVICE_ACCOUNT_NAME" \
           --display-name="$GKE_SERVICE_ACCOUNT_NAME"
         

  3. Initialize an environment variable that stores the service account email account name:
         
         GKE_SERVICE_ACCOUNT_EMAIL="$(gcloud iam service-accounts list \
             --format='value(email)' \
             --filter=displayName:"$GKE_SERVICE_ACCOUNT_NAME")"
         

  4. Bind the Identity and Access Management (IAM) roles to the service account:
         
         gcloud projects add-iam-policy-binding \
             "$(gcloud config get-value project 2> /dev/null)" \
             --member serviceAccount:"$GKE_SERVICE_ACCOUNT_EMAIL" \
             --role roles/monitoring.viewer
         gcloud projects add-iam-policy-binding \
             "$(gcloud config get-value project 2> /dev/null)" \
             --member serviceAccount:"$GKE_SERVICE_ACCOUNT_EMAIL" \
             --role roles/monitoring.metricWriter
         gcloud projects add-iam-policy-binding \
             "$(gcloud config get-value project 2> /dev/null)" \
             --member serviceAccount:"$GKE_SERVICE_ACCOUNT_EMAIL" \
             --role roles/logging.logWriter
         




### Prepare the GKE cluster

In this section, you launch the GKE cluster, grant permissions, and finish the cluster configuration.

For this tutorial, a cluster with a relatively low number of small, [general purpose](https://docs.cloud.google.com/compute/docs/machine-types#general_purpose) nodes is enough to demonstrate the concept of this tutorial. You create a cluster with [one node pool](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools) (the default one).

  * In Cloud Shell, create and launch a [regional](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/regional-clusters) GKE cluster:
        
        gcloud container clusters create ds-init-tutorial \
            --enable-ip-alias \
            --machine-type=n1-standard-2 \
            --metadata disable-legacy-endpoints=true \
            --node-labels=app=default-init \
            --node-locations us-central1-a,us-central1-b,us-central1-c \
            --no-enable-basic-auth \
            --no-issue-client-certificate \
            --num-nodes=1 \
            --location us-central1 \
            --service-account="$GKE_SERVICE_ACCOUNT_EMAIL"
        




## Apply node configurations using a DaemonSet

In this section, you prevent workloads from running on nodes before configuration is complete by applying a taint to the node pool. Then you deploy a DaemonSet that does the following:

  1. Schedules Pods on tainted nodes by using a toleration for the taint.
  2. Runs a privileged init container that first applies the node configuration using `sysctl`, and then removes the taint from the node using `kubectl`. Removing the taint makes the node schedulable for workloads.
  3. Schedules and runs a pause container that stays idle and consumes no resources to prevent the DaemonSet from rescheduling the Pod used for configuration.



This tutorial applies the `vm.max_map_count=262144` kernel parameter as an example configuration.

  1. Apply a taint to the default node pool:
         
         gcloud container node-pools update default-pool \
           --cluster=ds-init-tutorial \
           --node-taints=node.config.status/stage=configuring:NoSchedule \
           --region=us-central1
         

With this taint, only Pods that tolerate it, like the DaemonSet Pod, can be scheduled in this node pool.

  2. Verify that the taint is applied:
         
         kubectl describe nodes -l cloud.google.com/gke-nodepool=default-pool | grep Taints
         

The node status should show `node.config.status/stage=configuring:NoSchedule`.

  3. Save the following manifest as `auto-untaint-daemonset.yaml`:
         
         # WARNING: This DaemonSet runs as privileged, which has significant
         # security implications. Only use this on clusters where you have
         # strict controls over what is deployed.
         ---
         apiVersion: v1
         kind: ServiceAccount
         metadata:
           name: node-config-sa
           namespace: default
         ---
         apiVersion: rbac.authorization.k8s.io/v1
         kind: ClusterRole
         metadata:
           name: node-patcher-role
         rules:
         - apiGroups: [""]
           resources: ["nodes"]
           # Permissions needed to read and remove a taint from the node.
           verbs: ["get", "patch", "update"]
         ---
         apiVersion: rbac.authorization.k8s.io/v1
         kind: ClusterRoleBinding
         metadata:
           name: node-config-binding
         subjects:
         - kind: ServiceAccount
           name: node-config-sa
           namespace: default
         roleRef:
           kind: ClusterRole
           name: node-patcher-role
           apiGroup: rbac.authorization.k8s.io
         ---
         apiVersion: apps/v1
         kind: DaemonSet
         metadata:
           name: auto-untaint-daemonset
           labels:
             app: auto-untaint-configurator
         spec:
           selector:
             matchLabels:
               app: auto-untaint-configurator
           updateStrategy:
             type: RollingUpdate
           template:
             metadata:
               labels:
                 app: auto-untaint-configurator
             spec:
               serviceAccountName: node-config-sa
               hostPID: true
               # Toleration now matches the taint on your node.
               tolerations:
               - key: "node.config.status/stage"
                 operator: "Equal"
                 value: "configuring"
                 effect: "NoSchedule"
               volumes:
               - name: host-root-fs
                 hostPath:
                   path: /
               initContainers:
               - name: configure-and-untaint
                 image: ubuntu:22.04 # Using a standard container image.
                 securityContext:
                   privileged: true # Required for chroot and sysctl.
                 env:
                 - name: NODE_NAME
                   valueFrom:
                     fieldRef:
                       fieldPath: spec.nodeName
                 volumeMounts:
                 - name: host-root-fs
                   mountPath: /host
                 command: ["/bin/bash", "-c"]
                 args:
                 - |
                   # Using explicit error checking for each critical command.
         
                   # Define the configuration and taint details.
                   SYSCTL_PARAM="vm.max_map_count"
                   SYSCTL_VALUE="262144"
                   TAINT_KEY="node.config.status/stage"
         
                   echo "Running configuration on node: ${NODE_NAME}"
         
                   # 1. APPLY CONFIGURATION
                   echo "--> Applying ${SYSCTL_PARAM}=${SYSCTL_VALUE}..."
                   if ! chroot /host sysctl -w "${SYSCTL_PARAM}=${SYSCTL_VALUE}"; then
                     echo "ERROR: Failed to apply sysctl parameter." >&2
                     exit 1
                   fi
                   echo "--> Configuration applied successfully."
         
                   # 2. UNTAINT THE NODE
                   # This command removes the taint from the node this Pod is running on.
                   echo "--> Untainting node ${NODE_NAME} by removing taint ${TAINT_KEY}..."
                   if ! /host/home/kubernetes/bin/kubectl taint node "${NODE_NAME}" "${TAINT_KEY}:NoSchedule-"; then
                     echo "ERROR: Failed to untaint the node." >&2
                     exit 1
                   fi
                   echo "--> Node has been untainted and is now schedulable."
               # The main container is minimal; it just keeps the Pod running.
               containers:
               - name: pause-container
                 image: registry.k8s.io/pause:3.9
         

This manifest creates a ServiceAccount, ClusterRole, and ClusterRoleBinding to grant the DaemonSet permission to remove taints from nodes. The DaemonSet deploys a Pod to each node that tolerates the `configuring:NoSchedule` taint. This Pod runs a privileged init container that applies the `sysctl` configuration (`vm.max_map_count=262144`) and removes the node taint, which makes the node schedulable. A pause container then starts to keep the Pod running.

The init container runs in privileged mode, which has security implications. For more details, see Privileged DaemonSet tradeoffs and security restrictions.

  4. Apply the manifest:
         
         kubectl apply -f auto-untaint-daemonset.yaml
         

  5. Verify that the DaemonSet Pods are created and wait for them to reach the `Running` state:
         
         kubectl get pods -l app=auto-untaint-configurator -o wide
         

The `Running` state indicates that the init container has completed successfully. Make a note of the Pod name so you can use it to verify the initialization in the next section.




## Validate and verify the initialization procedure

After node configuration is complete, you can verify the results by checking the logs.

  1. Check the init container logs of one of the Pods to see its output:
         
         kubectl logs POD_NAME -c configure-and-untaint
         

Replace `POD_NAME` with the name of your Pod.

You should see output indicating successful configuration and node untainting.

  2. Verify that the taint is removed:
         
         kubectl describe nodes -l cloud.google.com/gke-nodepool=default-pool | grep Taints
         

The node status should show `Taints: <none>`, or show taints that have the key `node.config.status/stage`.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, you could delete the project you created for this tutorial. If you created a project dedicated to this tutorial, you can delete it entirely. If you used an existing project but don't want to delete it, use the following steps for cleaning up the project.

### Clean up the project

To clean up a project without deleting it, you need to remove the resources that you created in this tutorial.

  1. In Cloud Shell, delete the GKE cluster:
         
         gcloud container clusters delete ds-init-tutorial --quiet --region us-central1
         

  2. Delete the service account:
         
         gcloud iam service-accounts delete "$GKE_SERVICE_ACCOUNT_EMAIL" --quiet
         




### Delete the project

The easiest way to eliminate billing is to delete the project you created for the tutorial.

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

  * Read about [GKE](https://docs.cloud.google.com/kubernetes-engine).
  * Implement a [secure software supply chain](https://docs.cloud.google.com/software-supply-chain-security/docs/overview).
  * Learn how you can [harden your GKE cluster's security](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster).
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
