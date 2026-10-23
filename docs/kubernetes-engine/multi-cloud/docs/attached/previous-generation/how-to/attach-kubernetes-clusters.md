---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/previous-generation/how-to/attach-kubernetes-clusters/
title: Attach third-party clusters to Google Cloud (previous generation) \u00a0|\u00a0 Anthos attached clusters (previous generation) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:43:37.240790+00:00
---

# Attach third-party clusters to Google Cloud (previous generation)  |  Anthos attached clusters (previous generation)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/previous-generation/how-to/attach-kubernetes-clusters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE attached clusters ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached)
  * [ Previous generation ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/previous-generation)



Send feedback 

#  Attach third-party clusters to Google Cloud (previous generation) Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This page shows you how to attach conformant Kubernetes clusters to your fleet using the _previous generation_ of our attached clusters feature. If you're attaching an Amazon EKS or Azure AKS cluster, see [Attach your EKS cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/how-to/attach-cluster) or [Attach your AKS cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/aks/how-to/attach-cluster) for current instructions. The remainder of this document applies only to clusters built with distributions other than AKS or EKS.

GKE attached clusters lets you view your existing Kubernetes clusters in the Google Cloud console along with your GKE clusters, and enable several GKE features on them, including centralized configuration control with Config Sync.

## Supported Kubernetes clusters

You can attach any [conformant Kubernetes cluster](https://www.cncf.io/certification/software-conformance/) that includes x86 nodes to your fleet and view it in the Google Cloud console with your GKE clusters.

The following cluster types and versions have been validated by Google. For information on the GKE features that are supported on attached clusters, see [GKE version and upgrade support](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/version-and-upgrade-support).

Attached cluster types | Kubernetes versions  
---|---  
Red Hat OpenShift Kubernetes Engine (OKE) 4.9, 4.10 | 1.23, 1.24  
Red Hat OpenShift Container Platform (OCP) 4.9, 4.10 | 1.23, 1.24  
Rancher Kubernetes Engine (RKE) 1.3.8 | 1.23, 1.24  
KIND 0.12 | 1.23, 1.24  
[K3s](https://k3s.io/) 1.20 | 1.20  
[K3d](https://k3d.io/) 4.4.3 | 1.20  
  
## Before you start

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Anthos API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=anthos.googleapis.com&redirect=https%3A//console.cloud.google.com)

  5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  6. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  7. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  8. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. Enable the Anthos API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=anthos.googleapis.com&redirect=https%3A//console.cloud.google.com)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  14. Check the [fleet registration prerequisites](https://docs.cloud.google.com/anthos/fleet-management/docs/before-you-begin) to ensure that you have the relevant permissions and enabled APIs to register a cluster.
  15. See the [Before you begin](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/previous-generation/before-you-begin) guide for specific requirements for attaching clusters outside Google Cloud, including any special setup steps you may need for your cluster type. 



## Register attached clusters

You must register all clusters that you want to use with GKE features to your project's fleet. A fleet provides a way to logically group and normalize Kubernetes clusters, making administration of infrastructure easier. Clusters in the same fleet can be browsed and managed together in the [Google Cloud console](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/console), and many GKE and Google Cloud components use fleet concepts such as [identity sameness and namespace sameness](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity#identity_sameness) to simplify working with multiple clusters. You can find out much more about fleets and the functionality that they enable in our [Fleet management guide](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs).

You are entitled to enable and use GKE features on these clusters, and you can manage some GKE features at fleet level from the [GKE features page](https://console.cloud.google.com/kubernetes/features/overview/).

### Set up identity

All attached clusters require an identity for the Connect Agent to use when authenticating to Google. If your cluster meets the [requirements](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/previous-generation/before-you-begin#fleet_workload_identity_requirements), you can register it with fleet Workload Identity enabled for authentication. Clusters with this feature enabled use identities from a fleet-wide fleet workload identity pool. You can find out more about how fleet Workload Identity works and the advantages of using it in [Use fleet Workload Identity](https://docs.cloud.google.com/anthos/fleet-management/docs/use-workload-identity).

If you can't use fleet Workload Identity, registering an attached cluster requires a Google Cloud [service account](https://docs.cloud.google.com/iam/docs/service-accounts) for authentication. We recommend creating a new service account for each cluster you want to attach. To create a service account for a cluster with the appropriate roles, follow the instructions in [Creating a Google Cloud service account with `gcloud`](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/previous-generation/before-you-begin#create_sa). After you have created your service account, you can use the JSON file with the service account's credentials (key file) to register your cluster, as described in the next section.

### Register your cluster

We recommend [getting your cluster's membership status](https://docs.cloud.google.com/anthos/fleet-management/docs/get-fleet-status) after you register it to ensure that it is properly connected to Google Cloud. See our [troubleshooting guide](https://docs.cloud.google.com/anthos/fleet-management/docs/troubleshooting) if you have any issues with your registration.

### gcloud

Run the following command:
    
    
    gcloud container fleet memberships register MEMBERSHIP_NAME \
       --context=KUBECONFIG_CONTEXT \
       --kubeconfig=KUBECONFIG_PATH \
       --service-account-key-file=SERVICE_ACCOUNT_KEY_PATH
    

Replace the following:

  * MEMBERSHIP_NAME: the membership name that you choose and that is used to uniquely represent the cluster being registered to the fleet.
  * SERVICE_ACCOUNT_KEY_PATH: the local filepath to the service account's private key JSON file downloaded as part of Prerequisites. This service account key is stored as a secret named `creds-gcp` in the `gke-connect` namespace.
  * KUBECONFIG_CONTEXT: the cluster context of the cluster being registered as it appears in the kubeconfig file. You can get this value from the command line by running `kubectl config current-context`.
  * KUBECONFIG_PATH: the local filepath where your kubeconfig containing an entry for the cluster being registered is stored. This defaults to `$KUBECONFIG` if that environment variable is set; otherwise, this defaults to `$HOME/.kube/config`.



### Register an attached cluster with fleet Workload Identity

To register an attached cluster with fleet Workload Identity enabled, run the following command. For more information about which attached cluster types can use this feature and any additional requirements, see [Attached cluster prerequisites](https://docs.cloud.google.com/anthos/clusters/docs/multi-cloud/attached/previous-generation/before-you-begin#fleet_workload_identity_requirements).
    
    
    gcloud container fleet memberships register MEMBERSHIP_NAME \
       --context=KUBECONFIG_CONTEXT \
       --kubeconfig=KUBECONFIG_PATH \
       --enable-workload-identity \
       --has-private-issuer
    

### Console

### Generate a registration command

You can use the Google Cloud console to help generate a `gcloud` registration command to register your cluster (with a service account only).

To register a cluster:

  1. In the Google Cloud console, go to the **Google Kubernetes Engine clusters overview** page.

[Go to GKE clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. Click **Register existing cluster**.

  3. Click **Add external cluster**.

  4. Enter the name of the cluster that you want to register in the **Cluster name** field.

  5. Optional: Add Google Cloud labels to your cluster.

  6. Click **Generate registration command**.

  7. In Cloud Shell or wherever you have saved your service account credentials, edit and run the `gcloud` command that is displayed on the page. You need to specify the following values:

     * The CLUSTER_CONTEXT is the cluster's context as it appears in the kubeconfig file. You can get this value from the command line by running `kubectl config current-context`.
     * The KUBECONFIG_PATH is the local filepath where your kubeconfig file is stored. This defaults to `$KUBECONFIG` if that environment variable is set; otherwise, it defaults to `$HOME/.kube/config`.
     * The LOCAL_KEY_PATH is the path to your service account key file.

Running this command deploys the Connect Agent in your user cluster. When the Connect Agent connects to Google Cloud and your cluster is registered, a success message is displayed on the page.

  8. Click **Set labels** , or click **Skip** if you didn't set any labels.




### Advanced registration options (command line only)

#### Download the Connect Agent manifest

To download the Connect Agent installation manifest without deploying the agent, for example if you want to examine or edit the manifest before installation, pass in the `--manifest-output-file` flag to the `gcloud container fleet memberships register` command. For example:
    
    
    --manifest-output-file=[MANIFEST_FILE_PATH]

where [MANIFEST_FILE_PATH] is the local filepath where you want the Connect Agent installation manifest to be stored.

Using this option will not deploy the Connect Agent into the cluster. To deploy the Connect Agent, manually apply the downloaded manifest to your cluster.

#### Using a proxy server

To configure a proxy server, pass in the `--proxy` flag to `gcloud container fleet memberships register` command. For example:
    
    
    --proxy=[URL]

where [URL] is the proxy address.

The Connect Agent supports [CONNECT-based HTTP and HTTPS proxies](https://en.wikipedia.org/wiki/HTTP_tunnel) only, and accepts IP addresses and hostnames. Be sure to specify the protocol corresponding to the proxy type in the URL. For example, to pass in an HTTPS hostname:
    
    
    --proxy=https://mycorpproxy.com:443

Unless you specify otherwise, Connect Agent uses port 3128 for the proxy.

If your proxy requires authorization, ensure that you pass in your credentials, such as:
    
    
    --proxy=http://user:password@10.10.10.10:8888

#### Installing Connect Agent in a cluster with Windows and Linux nodes

The Connect Agent has to run on a Linux node. If you are installing in a mixed cluster with both Linux and Windows nodes, you can ensure that the Connect Agent is deployed on to a Linux node by adding an appropriate node selector to the deployment definition.

Run the following command to update the deployment with the appropriate node selector: 
    
    
    kubectl patch deployment \  
     $(kubectl get deployment -o=jsonpath='{.items[*].metadata.name}' -n gke-connect) \  
     -p '{"spec":{"template":{"spec":{"nodeSelector":{"kubernetes.io/os":"linux"}}}}}' -n gke-connect

To validate that the update succeeded run the following command: 
    
    
    kubectl get deployment -o=jsonpath='{.items[].spec.template.spec.nodeSelector}' -n gke-connect

The command should return: 
    
    
    {"kubernetes.io/os":"linux"}

### Troubleshooting

If you run into any problems during this setup, see the fleet creation [troubleshooting guide](https://docs.cloud.google.com/anthos/fleet-management/docs/troubleshooting).

## Enable GKE features on attached clusters

After you register your clusters, you can enable available GKE features on them for your applications. These features are supported only on our validated cluster types. You can see the current feature versions supported on these types in [Version and upgrade support](https://docs.cloud.google.com/anthos/docs/version-and-upgrade-support).

The following guides show you how to enable supported features on your clusters:

  * Cloud Service Mesh 1.11 and later supports Amazon EKS:

    * [Install Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/unified-install/asmcli-overview)
    * [Set up a multi-cluster mesh outside Google Cloud](https://docs.cloud.google.com/service-mesh/docs/unified-install/off-gcp-multi-cluster-setup)
  * Configuration and policy management:

    * [Install Config Management](https://docs.cloud.google.com/anthos-config-management/docs/how-to/installing)
    * [Install Config Connector](https://docs.cloud.google.com/anthos-config-management/docs/how-to/installing-config-connector)
    * [Install Policy Controller](https://docs.cloud.google.com/anthos-config-management/docs/how-to/installing-policy-controller)



## Access attached clusters

After you register an attached cluster, it appears in the GKE clusters pages in the [Google Cloud console](https://console.cloud.google.com/). However, to see more details such as nodes and workloads, you need to log in and authenticate to the cluster. To log in to your attached clusters from the Google Cloud console, follow the instructions in [Logging in to clusters from the Google Cloud console](https://docs.cloud.google.com/anthos/fleet-management/docs/console). Depending on the authentication method you choose, note that you or a platform admin may need to do some additional setup before you or other users are able to log in to the cluster.

To access attached clusters from the command line using a Google Cloud identity, see [Connecting to registered clusters with the Connect gateway](https://docs.cloud.google.com/anthos/multicluster-management/gateway).

To authenticate to attached clusters using your existing third-party identity provider (EKS on AWS clusters only, preview feature), see [Setting up GKE Identity Service for a fleet](https://docs.cloud.google.com/anthos/identity/setup/fleet) and [Accessing clusters with GKE Identity Service](https://docs.cloud.google.com/anthos/identity/accessing).

## What's next?

  * [Set up logging and monitoring for attached clusters](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/previous-generation/how-to/logging-and-monitoring)
  * [Troubleshoot attached clusters](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/previous-generation/how-to/troubleshooting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
