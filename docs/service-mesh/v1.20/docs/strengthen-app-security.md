---
url: https://docs.cloud.google.com/service-mesh/v1.20/docs/strengthen-app-security/
title: Strengthen your app's security with Cloud Service Mesh, Config Sync, and Policy Controller \u00a0|\u00a0 Cloud Service Mesh v1.20 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:50:44.081037+00:00
---

# Strengthen your app's security with Cloud Service Mesh, Config Sync, and Policy Controller  |  Cloud Service Mesh v1.20  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.20/docs/strengthen-app-security/

You are viewing archived v1.20 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ v1.20 ](https://docs.cloud.google.com/service-mesh/v1.20/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.20/docs/overview)



Send feedback 

#  Strengthen your app's security with Cloud Service Mesh, Config Sync, and Policy Controller Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows you how to improve your cluster and app's security posture. Imagine you are a platform administrator whose organization is managing the apps for their online store with [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/overview), a suite of tools that helps you monitor and manage a reliable service mesh. You are responsible for ensuring that your mesh and apps are secure.

You can prevent misconfiguration and automatically validate your Cloud Service Mesh policies by using [Policy Controller](https://docs.cloud.google.com/anthos-config-management/docs/concepts/policy-controller) and [Config Sync](https://docs.cloud.google.com/anthos-config-management/docs/config-sync-overview). Policy Controller enables the enforcement of fully programmable policies for your clusters. Policy Controller also comes with a default library of [constraint templates](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library) that you can use with the [Cloud Service Mesh security bundle](https://github.com/GoogleCloudPlatform/acm-policy-controller-library/blob/master/bundles/asm-policy-v0.0.1) to audit the compliance of your mesh security vulnerabilities and best practices. Config Sync continuously reconciles the state of clusters with a central set of Kubernetes declarative configuration files. Using Policy Controller and Config Sync together enables you to continuously enforce [constraints](https://docs.cloud.google.com/anthos-config-management/docs/how-to/creating-policy-controller-constraints) on your Cloud Service Mesh policy configurations.

The following diagram shows you an overview of how Cloud Service Mesh, Policy Controller, and Config Sync work together in this tutorial to manage and protect an [ingress gateway](https://docs.cloud.google.com/service-mesh/docs/gateways) and the [Online Boutique sample apps](https://github.com/GoogleCloudPlatform/microservices-demo) that you use in this tutorial:

![A diagram showing the architecture that you create for this tutorial](https://docs.cloud.google.com/static/anthos-config-management/docs/img/asm-acm-tutorial-architecture.svg)

## Objectives

  * Create a Google Kubernetes Engine (GKE) cluster and register the cluster to a [fleet](https://docs.cloud.google.com/anthos/multicluster-management/fleets).
  * Install Policy Controller, Config Sync, and Cloud Service Mesh on a cluster.
  * Configure Config Sync to [sync multiple repositories](https://docs.cloud.google.com/anthos-config-management/docs/how-to/multiple-repositories)
  * Apply best practices to deploy configs, apps and Istio resources with Config Sync.
  * Deploy cluster configs, the Online Boutique sample apps, and an ingress gateway with Config Sync.
  * Leverage the [Cloud Service Mesh policy bundle](https://docs.cloud.google.com/anthos-config-management/docs/how-to/using-asm-security-policy) of Policy Controller to enforce the following security best practices: 
    * Ensure that all workloads in the mesh have automatic sidecar injection.
    * Encrypt all traffic in the mesh.
    * Guarantee that all workloads in the mesh have granular access control.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [ GKE](https://docs.cloud.google.com/kubernetes-engine/pricing).
  * [ GKE Enterprise](https://docs.cloud.google.com/anthos/pricing). The billing for GKE Enterprise includes billing for the Cloud Service Mesh, Config Sync, and Policy Controller.



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 




## Prepare your environment

In this section, you prepare your environment so that you can install Cloud Service Mesh, Policy Controller, and Config Sync:

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. Upgrade to the latest version of the Google Cloud CLI:
         
         gcloud components update
         

  3. To store the files that you create in this tutorial, create a directory:
         
         mkdir ~/asm-acm-tutorial-dir
         

  4. To simplify the remainder of the tutorial, create the following environment variables:
         
         PROJECT_ID=PROJECT_ID
         gcloud config set project $PROJECT_ID
         CLUSTER=asm-acm-tutorial
         CLUSTER_ZONE=us-east4-a
         MEMBERSHIP=asm-acm-tutorial
         PROJECT_NUMBER=$(gcloud projects describe ${PROJECT_ID} --format='get(projectNumber)')
         

Replace `PROJECT_ID` with the project ID that you want to use for this tutorial.

If you're asked to authorize Cloud Shell, click **Authorize** to complete the operation.

  5. Enable the APIs that you need for this tutorial:

### gcloud
         
         gcloud services enable \
             mesh.googleapis.com \
             anthos.googleapis.com
         

###  Config Connector 

This tutorial includes [Config Connector](https://docs.cloud.google.com/config-connector/docs/overview) resources. You can use these resources to complete the same tasks that you complete in the `gcloud` tab. To utilize these resources, [install Config Connector](https://docs.cloud.google.com/config-connector/docs/concepts/installation-types) and apply the resources in the way that works best for your environment.

Use the following [`Services`](https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/serviceusage/service) manifest:
         
         apiVersion: serviceusage.cnrm.cloud.google.com/v1beta1
         kind: Service
         metadata:
           annotations:
             cnrm.cloud.google.com/deletion-policy: "abandon"
             cnrm.cloud.google.com/disable-dependent-services: "false"
           name: mesh.googleapis.com
         spec:
           resourceID: mesh.googleapis.com
           projectRef:
             external: PROJECT_ID
         ---
         apiVersion: serviceusage.cnrm.cloud.google.com/v1beta1
         kind: Service
         metadata:
           annotations:
             cnrm.cloud.google.com/deletion-policy: "abandon"
             cnrm.cloud.google.com/disable-dependent-services: "false"
           name: anthos.googleapis.com
         spec:
           resourceID: anthos.googleapis.com
           projectRef:
             external: PROJECT_ID
         

This operation can take over one minute to complete.




## Set up a GKE cluster

In this section, you create a GKE cluster and then register it to a [fleet](https://docs.cloud.google.com/anthos/multicluster-management/fleets). Fleets are a Google Cloud concept for logically organizing clusters and other resources, letting you use and manage multi-cluster capabilities and apply consistent policies across your systems.

The cluster that you create in this section is the cluster that you install Cloud Service Mesh, Policy Controller, and Config Sync on. It's also the cluster where you deploy the Online Boutique sample apps.

To set up your cluster, complete the following steps:

  1. Create a GKE cluster:

###  gcloud 
         
         gcloud container clusters create ${CLUSTER} \
             --zone ${CLUSTER_ZONE} \
             --machine-type=e2-standard-4 \
             --num-nodes 4 \
             --workload-pool ${PROJECT_ID}.svc.id.goog \
             --labels mesh_id=proj-${PROJECT_NUMBER}
         

###  Config Connector 

Use the following [`ContainerCluster`](https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/container/containercluster) and [`ContainerNodePool`](https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/container/containernodepool) manifests:
         
         apiVersion: container.cnrm.cloud.google.com/v1beta1
         kind: ContainerNodePool
         metadata:
           annotations:
             cnrm.cloud.google.com/project-id: PROJECT_ID
           name: asm-acm-tutorial
         spec:
           clusterRef:
             name: asm-acm-tutorial
           location: us-east4-a
           nodeConfig:
             machineType: e2-standard-4
           nodeCount: 4
         ---
         apiVersion: container.cnrm.cloud.google.com/v1beta1
         kind: ContainerCluster
         metadata:
           annotations:
             cnrm.cloud.google.com/project-id: PROJECT_ID
             cnrm.cloud.google.com/remove-default-node-pool: "true"
           labels:
             mesh_id: proj-PROJECT_NUMBER
           name: asm-acm-tutorial
         spec:
           location: us-east4-a
           initialNodeCount: 1
           workloadIdentityConfig:
             workloadPool: PROJECT_ID.svc.id.goog
         

Replace `PROJECT_NUMBER` by the value of the `PROJECT_NUMBER` environment variable retrieved earlier.

This operation can take over five minutes to complete.

  2. To ensure the successful creation of the GKE cluster, describe its status:
         
         gcloud container clusters list \
             --zone ${CLUSTER_ZONE} \
             --project ${PROJECT_ID}
         

The output is similar to the following:
         
         NAME                LOCATION      MASTER_VERSION   MASTER_IP      MACHINE_TYPE   NODE_VERSION     NUM_NODES  STATUS
         asm-acm-tutorial    us-east4-a    1.23.12-gke.100  35.186.179.30  e2-standard-4  1.23.12-gke.100  3          RUNNING
         

  3. Connect to the GKE cluster:
         
         gcloud container clusters get-credentials ${CLUSTER} \
             --zone ${CLUSTER_ZONE} \
             --project ${PROJECT_ID}
         

  4. Register your cluster to a fleet:

###  gcloud 
         
         gcloud container fleet memberships register ${MEMBERSHIP} \
             --project ${PROJECT_ID} \
             --gke-cluster ${CLUSTER_ZONE}/${CLUSTER} \
             --enable-workload-identity
         

The output is similar to the following:
         
         kubeconfig entry generated for asm-acm-tutorial.
         Waiting for membership to be created...done.
         Created a new membership [projects/PROJECT_ID/locations/global/memberships/asm-acm-tutorial] for the cluster [asm-acm-tutorial]
         Generating the Connect Agent manifest...
         Deploying the Connect Agent on cluster [asm-acm-tutorial] in namespace [gke-connect]...
         Deployed the Connect Agent on cluster [asm-acm-tutorial] in namespace [gke-connect].
         Finished registering the cluster [asm-acm-tutorial] with the Fleet.
         

###  Config Connector 

Use the following [`GKEHubMembership`](https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/gkehub/gkehubmembership) manifest:
         
         apiVersion: gkehub.cnrm.cloud.google.com/v1beta1
         kind: GKEHubMembership
         metadata:
           annotations:
             cnrm.cloud.google.com/project-id: PROJECT_ID
           name: asm-acm-tutorial
         spec:
           location: global
           authority:
             issuer: https://container.googleapis.com/v1/projects/PROJECT_ID/locations/us-east4-a/clusters/asm-acm-tutorial
           endpoint:
             gkeCluster:
               resourceRef:
                 name: asm-acm-tutorial
         

  5. To ensure the successful registration of the GKE cluster, describe its status:
         
         gcloud container fleet memberships list
         

The output is similar to the following:
         
         NAME              EXTERNAL_ID                           LOCATION
         asm-acm-tutorial  0e12258c-8831-4d81-b5c0-5e7099a468cc  global
         




## Explore the repositories

In the following installation section, you apply a manifest `acm-config.yaml` file. This manifest configures your cluster to sync from the [`asm-acm-tutorial` folder](https://github.com/GoogleCloudPlatform/anthos-config-management-samples/tree/main/asm-acm-tutorial) of the sample repository. This folder contains all the configuration files that you need to complete the remainder of the tutorial.

To simplify this tutorial, you use `sed` commands to update the `acm-config.yaml`. With the `acm-config.yaml` file, Config Sync deploys the manifests required for each step of this tutorial. Updating a single file helps you focus on the concepts and the flow of securing your clusters, mesh, and applications without repeatedly manipulating the files and repeatedly running `git` commands.

To utilize Config Sync's ability to [sync multiple repositories](https://docs.cloud.google.com/anthos-config-management/docs/how-to/multiple-repositories), you use the following resources:

  * [`root-sync`](https://github.com/GoogleCloudPlatform/anthos-config-management-samples/tree/main/asm-acm-tutorial/root-sync), as a [`RootSync`](https://docs.cloud.google.com/anthos-config-management/docs/reference/rootsync-reposync-fields) repository, contains all the configs across your cluster including `RepoSyncs`, `Constraints`, `ClusterRole`, `RoleBindings`, and resources included in some system namespaces such as `istio-system`.
  * [`ingress-gateway`](https://github.com/GoogleCloudPlatform/anthos-config-management-samples/tree/main/asm-acm-tutorial/ingress-gateway), as a first `RepoSync`, contains all the resources needed to deploy an ingress gateway and progressively secure it throughout this tutorial.
  * [`online-boutique`](https://github.com/GoogleCloudPlatform/anthos-config-management-samples/tree/main/asm-acm-tutorial/online-boutique), as a second `RepoSync`, contains all the resources needed to deploy the Online Boutique apps and progressively secure them throughout this tutorial.



## Install Policy Controller, Config Sync, and managed Cloud Service Mesh

Now that you have created and registered your cluster, you can install Config Sync, Policy Controller, and Cloud Service Mesh on your cluster and configure your cluster to sync from the configs of the default `RootSync`:

  1. Enable the `ConfigManagement` operator, which manages Config Sync and Policy Controller:

###  gcloud 
         
         gcloud beta container fleet config-management enable
         

###  Config Connector 

Use the following [`GKEHubFeature`](https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/gkehub/gkehubfeature) manifest:
         
         apiVersion: gkehub.cnrm.cloud.google.com/v1beta1
         kind: GKEHubFeature
         metadata:
           name: configmanagement
         spec:
           projectRef:
             external: PROJECT_ID
           location: global
           resourceID: configmanagement
         

  2. Enable Cloud Service Mesh in your fleet.

###  gcloud 
         
         gcloud container fleet mesh enable
         

###  Config Connector 

Use the following [`GKEHubFeature`](https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/gkehub/gkehubfeature) manifest:
         
         apiVersion: gkehub.cnrm.cloud.google.com/v1beta1
         kind: GKEHubFeature
         metadata:
           name: servicemesh
         spec:
           projectRef:
             external: PROJECT_ID
           location: global
           resourceID: servicemesh
         

  3. Enable the Cloud Service Mesh automatic management to let Google apply the recommended configuration of managed Cloud Service Mesh:

###  gcloud 
         
         gcloud container fleet mesh update \
             --management automatic \
             --memberships ${MEMBERSHIP}
         

###  Config Connector 

Use the following [`GKEHubFeatureMembership`](https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/gkehub/gkehubfeaturemembership) manifest:
         
         apiVersion: gkehub.cnrm.cloud.google.com/v1beta1
         kind: GKEHubFeatureMembership
         metadata:
           name: servicemesh-membership
         spec:
           projectRef:
             external: PROJECT_ID
           location: global
           membershipRef:
             name: asm-acm-tutorial
           featureRef:
             name: servicemesh
           mesh:
             management: MANAGEMENT_AUTOMATIC
         

  4. Enable Config Sync and Policy Controller:

###  gcloud 

Save the following manifest as `acm-config.yaml` in the `~/asm-acm-tutorial-dir` directory:
         
         applySpecVersion: 1
         spec:
           configSync:
             enabled: true
             policyDir: asm-acm-tutorial/root-sync/init
             secretType: none
             sourceFormat: unstructured
             syncRepo: https://github.com/GoogleCloudPlatform/anthos-config-management-samples
             syncBranch: main
           policyController:
             enabled: true
             referentialRulesEnabled: true
             templateLibraryInstalled: true
         

To learn more about the Google Cloud CLI config fields, see [gcloud apply spec fields](https://docs.cloud.google.com/anthos-config-management/docs/reference/gcloud-apply-fields).

Apply the file:
         
         gcloud beta container fleet config-management apply \
             --membership ${MEMBERSHIP} \
             --config ~/asm-acm-tutorial-dir/acm-config.yaml
         

###  Config Connector 

Use the following [`GKEHubFeatureMembership`](https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/gkehub/gkehubfeaturemembership) manifest:
         
         apiVersion: gkehub.cnrm.cloud.google.com/v1beta1
         kind: GKEHubFeatureMembership
         metadata:
           name: configmanagement-membership
         spec:
           projectRef:
             external: PROJECT_ID
           location: global
           membershipRef:
             name: asm-acm-tutorial
           featureRef:
             name: configmanagement
           configmanagement:
             configSync:
               sourceFormat: unstructured
               git:
                 policyDir: asm-acm-tutorial/root-sync/init
                 secretType: none
                 syncBranch: main
                 syncRepo: https://github.com/GoogleCloudPlatform/anthos-config-management-samples
             policyController:
               enabled: true
               referentialRulesEnabled: true
               templateLibraryInstalled: true
         

Policy Controller and Config Sync are installed on your cluster. Next, Config Sync begins syncing all the configs of the default `RootSync` to your cluster. These configs install and configure the following key components:

     * The `RepoSync` objects that configure the Online Boutique apps and the ingress gateway are synced:
           
           apiVersion: configsync.gke.io/v1beta1
           kind: RepoSync
           metadata:
             name: repo-sync
           spec:
             override:
               enableShellInRendering: true
             sourceFormat: unstructured
             git:
               repo: https://github.com/GoogleCloudPlatform/anthos-config-management-samples
               revision: HEAD
               branch: main
               dir: asm-acm-tutorial/online-boutique/init
               auth: none
           
           apiVersion: configsync.gke.io/v1beta1
           kind: RepoSync
           metadata:
             name: repo-sync
           spec:
             override:
               enableShellInRendering: true
             sourceFormat: unstructured
             git:
               repo: https://github.com/GoogleCloudPlatform/anthos-config-management-samples
               revision: HEAD
               branch: main
               dir: asm-acm-tutorial/ingress-gateway/init
               auth: none

     * Since the [`RepoSync` reconcilers need additional permissions](https://docs.cloud.google.com/anthos-config-management/docs/how-to/multiple-repositories#manage-namespace-repos-in-namespace) to create Istio resources, a `ClusterRole` and two `RoleBinding` objects to grant these permissions are also applied to your cluster:
           
           apiVersion: rbac.authorization.k8s.io/v1
           kind: ClusterRole
           metadata:
             labels:
               rbac.authorization.k8s.io/aggregate-to-edit: "true"
             name: custom:aggregate-to-edit:istio
           rules:
           - apiGroups:
             - "networking.istio.io"
             - "security.istio.io"
             resources:
             - "virtualservices"
             - "authorizationpolicies"
             - "gateways"
             verbs:
             - "*"
           
           apiVersion: rbac.authorization.k8s.io/v1
           kind: RoleBinding
           metadata:
             name: repo-sync
           subjects:
           - kind: ServiceAccount
             name: ns-reconciler-onlineboutique
             namespace: config-management-system
           roleRef:
             kind: ClusterRole
             name: edit
             apiGroup: rbac.authorization.k8s.io
           
           apiVersion: rbac.authorization.k8s.io/v1
           kind: RoleBinding
           metadata:
             name: repo-sync
           subjects:
           - kind: ServiceAccount
             name: ns-reconciler-asm-ingress
             namespace: config-management-system
           roleRef:
             kind: ClusterRole
             name: edit
             apiGroup: rbac.authorization.k8s.io

  5. To ensure the successful installation of Policy Controller and Config Sync, check the status:
         
         gcloud beta container fleet config-management status
         

The output is similar to the following:
         
         Name: asm-acm-tutorial
         Status: SYNCED
         Last_Synced_Token: 4b3384d
         Sync_Branch: main
         Last_Synced_Time: 2022-05-04T21:32:58Z
         Policy_Controller: INSTALLED
         

If you see `PENDING` or `NOT_INSTALLED` in the `Status` or `Policy_Controller` rows, wait a few minutes and run `gcloud beta container fleet config-management status` again.

  6. To ensure the successful installation of Cloud Service Mesh, describe its status:
         
         gcloud container fleet mesh describe
         

The output is similar to the following:
         
         createTime: '2022-09-13T23:12:56.477042921Z'
         membershipSpecs:
           projects/PROJECT_NUMBER/locations/global/memberships/asm-acm-tutorial:
             mesh:
               management: MANAGEMENT_AUTOMATIC
         membershipStates:
           projects/PROJECT_NUMBER/locations/global/memberships/asm-acm-tutorial:
             servicemesh:
               controlPlaneManagement:
                 details:
                 - code: REVISION_READY
                   details: 'Ready: asm-managed'
                 state: ACTIVE
               dataPlaneManagement:
                 details:
                 - code: OK
                   details: Service is running.
                 state: ACTIVE
             state:
               code: OK
               description: |-
                 Revision(s) ready for use: asm-managed.
                 All Canonical Services have been reconciled successfully.
               updateTime: '2022-09-14T00:19:10.571552206Z'
         name: projects/PROJECT_ID/locations/global/features/servicemesh
         resourceState:
           state: ACTIVE
         spec: {}
         state:
           state: {}
         updateTime: '2022-09-14T00:19:14.135113118Z'
         

If you see `state.code: ERROR` instead of `state.code: OK`, wait a few minutes and run `gcloud container fleet mesh describe` again. Before moving forward with the tutorial, you need to make sure that the `servicemesh.controlPlaneManagement.details.code` field has the `REVISION_READY` value.




## Deploy an ingress gateway and a sample application

In this section, you deploy the [Online Boutique sample application](https://github.com/GoogleCloudPlatform/microservices-demo) and an [ingress gateway](https://docs.cloud.google.com/service-mesh/docs/gateways) to manage ingress traffic.

  1. Deploy the Online Boutique sample application and the ingress gateway.

The following command uses `sed` to update the `acm-config.yaml` manifest to get Config Sync deploying the resources you need to deploy the ingress gateway and sample app.
         
         sed -i "s,root-sync/init,root-sync/deployments,g" ~/asm-acm-tutorial-dir/acm-config.yaml
         gcloud beta container fleet config-management apply \
             --membership ${MEMBERSHIP} \
             --config ~/asm-acm-tutorial-dir/acm-config.yaml
         

Note this step can take a few minutes to complete.

  2. View the Config Sync status for the `RootSync` and the two `RepoSyncs`:
         
         gcloud alpha anthos config sync repo describe
         

The output is similar to:
         
         getting 3 RepoSync and RootSync from projects/PROJECT_ID/locations/global/memberships/asm-acm-tutorial
         [
           {
             "clusters": [
               "projects/PROJECT_ID/locations/global/memberships/asm-acm-tutorial"
             ],
             "commit": "95a30c052566357afb9db3d7f6153d9c0f219c03",
             "errors": [],
             "source": "https://github.com/GoogleCloudPlatform/anthos-config-management-samples//asm-acm-tutorial/root-sync/deployments@main",
             "status": "SYNCED"
           },
           {
             "clusters": [
               "projects/PROJECT_ID/locations/global/memberships/asm-acm-tutorial"
             ],
             "commit": "95a30c052566357afb9db3d7f6153d9c0f219c03",
             "errors": [],
             "source": "https://github.com/GoogleCloudPlatform/anthos-config-management-samples//asm-acm-tutorial/ingress-gateway/deployments@main",
             "status": "SYNCED"
           },
           {
             "clusters": [
               "projects/PROJECT_ID/locations/global/memberships/asm-acm-tutorial"
             ],
             "commit": "95a30c052566357afb9db3d7f6153d9c0f219c03",
             "errors": [],
             "source": "https://github.com/GoogleCloudPlatform/anthos-config-management-samples//asm-acm-tutorial/online-boutique/deployments@main",
             "status": "SYNCED"
           }
         ]
         

If you see `status: RECONCILING` instead of `status: SYNCED`, wait a few minutes and run `gcloud alpha anthos config sync repo describe` again.

To only view the information of one repository you can use the `--sync-name` and `--sync-namespace` flags. To view the managed resources in detail, add the `--managed-resources` flag. For more information, see [View Config Sync status across multiple clusters](https://docs.cloud.google.com/anthos-config-management/docs/how-to/config-sync-status-gcloud#describe_a_repo).

  3. Wait for the ingress gateway's public IP address to be provisioned:
         
         until kubectl -n asm-ingress get svc asm-ingressgateway -o jsonpath='{.status.loadBalancer}' | grep "ingress"; do : ; done
         

  4. Get the ingress gateway's public IP address:
         
         EXTERNAL_IP=$(kubectl get svc asm-ingressgateway -n asm-ingress -o jsonpath="{.status.loadBalancer.ingress[*].ip}")
         

  5. Visit the IP address from your browser to verify that the Online Boutique app has successfully deployed:
         
         echo http://${EXTERNAL_IP}
         




## Enforce policies to secure your mesh

In the following sections, you leverage [Policy Controller](https://docs.cloud.google.com/anthos-config-management/docs/concepts/policy-controller) to enforce policies from the [Cloud Service Mesh policy bundle](https://docs.cloud.google.com/anthos-config-management/docs/how-to/using-asm-security-policy) by [creating constraints](https://docs.cloud.google.com/anthos-config-management/docs/how-to/creating-policy-controller-constraints).

### Enforce sidecar proxies injection

In this section you enforce policies to ensure that all workloads in the mesh have [automatic sidecar injection](https://docs.cloud.google.com/service-mesh/docs/anthos-service-mesh-proxy-injection) enabled.

  1. To enforce sidecar proxies injection, apply constraints.

The following command uses `sed` to update the `acm-config.yaml` manifest to get Config Sync deploying the associated resources.
         
         sed -i "s,root-sync/deployments,root-sync/enforce-sidecar-injection,g" ~/asm-acm-tutorial-dir/acm-config.yaml
         gcloud beta container fleet config-management apply \
             --membership ${MEMBERSHIP} \
             --config ~/asm-acm-tutorial-dir/acm-config.yaml
         

The preceding command deploys the following resources:

     * A [`K8sRequiredLabels`](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8srequiredlabels) `Constraint` that requires any `Namespace` in the mesh to contain the specific [Cloud Service Mesh sidecar proxy injection label](https://docs.cloud.google.com/service-mesh/docs/revisions-overview):
           
           apiVersion: constraints.gatekeeper.sh/v1beta1
           kind: K8sRequiredLabels
           metadata:
             name: namespace-sidecar-injection-label
           spec:
             enforcementAction: deny
             match:
               kinds:
               - apiGroups:
                 - ""
                 kinds:
                 - Namespace
               excludedNamespaces:
               - config-management-monitoring
               - config-management-system
               - default
               - gatekeeper-system
               - gke-connect
               - istio-system
               - kube-node-lease
               - kube-public
               - kube-system
               - resource-group-system
             parameters:
               labels:
               - allowedRegex: enabled
                 key: istio-injection

     * An [`AsmSidecarInjection`](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#asmsidecarinjection) `Constraint` that prohibits any `Pod` in the mesh from bypassing the Istio proxy sidecar injection:
           
           apiVersion: constraints.gatekeeper.sh/v1beta1
           kind: AsmSidecarInjection
           metadata:
             name: pod-sidecar-injection-annotation
           spec:
             enforcementAction: deny
             match:
               kinds:
               - apiGroups:
                 - ""
                 kinds:
                 - Pod
               excludedNamespaces:
               - kube-system
             parameters:
               strictnessLevel: High

  2. View the Config Sync status for the `RootSync`:
         
         gcloud alpha anthos config sync repo describe \
             --sync-name root-sync \
             --sync-namespace config-management-system
         

The output is similar to:
         
         getting 1 RepoSync and RootSync from projects/PROJECT_ID/locations/global/memberships/asm-acm-tutorial
         [
           {
             "clusters": [
               "projects/PROJECT_ID/locations/global/memberships/asm-acm-tutorial"
             ],
             "commit": "7d15d49af13c44aa531a4565b2277ddcf8b81884",
             "errors": [],
             "source": "https://github.com/GoogleCloudPlatform/anthos-config-management-samples//asm-acm-tutorial/root-sync/enforce-sidecar-injection@main",
             "status": "SYNCED"
           }
         ]
         

If you see `status: RECONCILING` instead of `status: SYNCED`, wait a few minutes and run `gcloud alpha anthos config sync repo describe` again.

  3. Verify the `Constraints` are created:
         
         kubectl get constraints
         

It can take a few minutes for Policy Controller to evaluate these constraints. If you don't see values in the `TOTAL-VIOLATIONS` column, wait and run `kubectl get constraints` again.

The output is similar to:
         
         NAME                                                                                       ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         podsidecarinjectionannotation.constraints.gatekeeper.sh/pod-sidecar-injection-annotation   deny                 0
         
         NAME                                                                            ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srequiredlabels.constraints.gatekeeper.sh/namespace-sidecar-injection-label   deny                 0
         

Because we properly set up our `Namespaces` and `Pods`, there are `0` `TOTAL-VIOLATIONS` for these `Constraints`.

  4. To see these `Constraints` at work, try to create a `Namespace` in your cluster with neither a `label` nor an `annotation`:
         
         kubectl create namespace test
         

The output is similar is the following error:
         
         Error from server (Forbidden): admission webhook "validation.gatekeeper.sh" denied the request: [namespace-sidecar-injection-label] you must provide labels: {"istio-injection"}
         




### Enforce traffic encryption

In this section you enforce policies to ensure that all traffic in the mesh is [encrypted](https://docs.cloud.google.com/service-mesh/docs/security/security-overview#mutual_tls).

  1. To enforce traffic encryption, apply constraints.

The following command uses `sed` to update the `acm-config.yaml` manifest to get Config Sync deploying the associated resources.
         
         sed -i "s,root-sync/enforce-sidecar-injection,root-sync/enforce-strict-mtls,g" ~/asm-acm-tutorial-dir/acm-config.yaml
         gcloud beta container fleet config-management apply \
             --membership ${MEMBERSHIP} \
             --config ~/asm-acm-tutorial-dir/acm-config.yaml
         

The preceding command deploys the following resources:

     * An [`AsmPeerAuthnMeshStrictMtls`](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#asmpeerauthnmeshstrictmtls) `Constraint` which enforces the mesh-level mTLS `PeerAuthentication` in the `istio-system` namespace:
           
           apiVersion: constraints.gatekeeper.sh/v1beta1
           kind: AsmPeerAuthnMeshStrictMtls
           metadata:
             name: mesh-level-strict-mtls
           spec:
             enforcementAction: deny
             parameters:
               rootNamespace: istio-system
               strictnessLevel: High

     * A [referential constraint](https://docs.cloud.google.com/anthos-config-management/docs/how-to/creating-policy-controller-constraints#referential) `Config` in the `gatekeeper-system` namespace. This referential constraint enables the `AsmPeerAuthnMeshStrictMtls` `Constraint` to reference another object in its definition (for example, searching for any `PeerAuthentication` in the `istio-system` `Namespace`):
           
           apiVersion: config.gatekeeper.sh/v1alpha1
           kind: Config
           metadata:
             name: config
           spec:
             sync:
               syncOnly:
                 - group: ""
                   version: "v1"
                   kind: "Namespace"
                 - group: "security.istio.io"
                   version: "v1beta1"
                   kind: "PeerAuthentication"
                 - group: "security.istio.io"
                   version: "v1beta1"
                   kind: "AuthorizationPolicy"

     * A [`DestinationRuleTLSEnabled`](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#destinationruletlsenabled) `Constraint` which prohibits disabling TLS for all hosts and host subsets in Istio `DestinationRules`:
           
           apiVersion: constraints.gatekeeper.sh/v1beta1
           kind: DestinationRuleTLSEnabled
           metadata:
             name: destination-rule-tls-enabled
           spec:
             enforcementAction: deny
             match:
               kinds:
               - apiGroups:
                 - networking.istio.io
                 kinds:
                 - DestinationRule

     * An [`AsmPeerAuthnStrictMtls`](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#asmpeerauthnstrictmtls) `Constraint` which enforces that all `PeerAuthentications` cannot overwrite `STRICT` mTLS:
           
           apiVersion: constraints.gatekeeper.sh/v1beta1
           kind: AsmPeerAuthnStrictMtls
           metadata:
             name: peerauthentication-strict-mtls
           spec:
             enforcementAction: deny
             match:
               kinds:
               - apiGroups:
                 - security.istio.io
                 kinds:
                 - PeerAuthentication
             parameters:
               strictnessLevel: High

  2. View the Config Sync status for the `RootSync`:
         
         gcloud alpha anthos config sync repo describe \
             --sync-name root-sync \
             --sync-namespace config-management-system
         

The output is similar to:
         
         getting 1 RepoSync and RootSync from projects/PROJECT_ID/locations/global/memberships/asm-acm-tutorial
         [
           {
             "clusters": [
               "projects/PROJECT_ID/locations/global/memberships/asm-acm-tutorial"
             ],
             "commit": "7d15d49af13c44aa531a4565b2277ddcf8b81884",
             "errors": [],
             "source": "https://github.com/GoogleCloudPlatform/anthos-config-management-samples//asm-acm-tutorial/root-sync/enforce-strict-mtls@main",
             "status": "SYNCED"
           }
         ]
         

If you see `status: RECONCILING` instead of `status: SYNCED`, wait a few minutes and run `gcloud alpha anthos config sync repo describe` again.

  3. Run the following command to get more information about the `PeerAuthentication` violation:
         
         kubectl get asmpeerauthnmeshstrictmtls.constraints.gatekeeper.sh/mesh-level-strict-mtls -ojsonpath='{.status.violations}'  | jq
         

The output is similar to:
         
         [
           {
             "enforcementAction": "deny",
             "group": "constraints.gatekeeper.sh",
             "kind": "AsmPeerAuthnMeshStrictMtls",
             "message": "Root namespace <istio-system> does not have a strict mTLS PeerAuthentication",
             "name": "mesh-level-strict-mtls",
             "version": "v1beta1"
           }
         ]
         

  4. Fix the issue by deploying a `PeerAuthentication` in the `istio-system`. To prevent all your services in the mesh from accepting plaintext traffic, set a mesh-wide `PeerAuthentication` policy with the mTLS mode set to `STRICT`. When you deploy the policy, the control plane automatically provisions TLS certificates so that workloads can authenticate with each other.

The following command uses `sed` to update the `acm-config.yaml` manifest to get Config Sync deploying the associated resources.
         
         sed -i "s,root-sync/enforce-strict-mtls,root-sync/fix-strict-mtls,g" ~/asm-acm-tutorial-dir/acm-config.yaml
         gcloud beta container fleet config-management apply \
             --membership ${MEMBERSHIP} \
             --config ~/asm-acm-tutorial-dir/acm-config.yaml
         

The preceding command deploys the following `STRICT` mTLS `PeerAuthentication` in the `istio-system` namespace. This applies mTLS `STRICT` to the entire mesh:
         
         apiVersion: security.istio.io/v1beta1
         kind: PeerAuthentication
         metadata:
           name: default
         spec:
           mtls:
             mode: STRICT

  5. View the Config Sync status for the `RootSync`:
         
         gcloud alpha anthos config sync repo describe \
             --sync-name root-sync \
             --sync-namespace config-management-system
         

The output is similar to:
         
         getting 1 RepoSync and RootSync from projects/PROJECT_ID/locations/global/memberships/asm-acm-tutorial
         [
           {
             "clusters": [
               "projects/PROJECT_ID/locations/global/memberships/asm-acm-tutorial"
             ],
             "commit": "7d15d49af13c44aa531a4565b2277ddcf8b81884",
             "errors": [],
             "source": "https://github.com/GoogleCloudPlatform/anthos-config-management-samples//asm-acm-tutorial/root-sync/fix-strict-mtls@main",
             "status": "SYNCED"
           }
         ]
         

If you see `status: RECONCILING` instead of `status: SYNCED`, wait a few minutes and run `gcloud alpha anthos config sync repo describe` again.

  6. Verify the `Constraints` are created:
         
         kubectl get constraints
         

Note this can take a few minutes to get Policy Controller evaluating these `Constraints`. Wait and run again this `kubectl get constraints` command until you get values under the `TOTAL-VIOLATIONS` column for each line.

The output is similar to:
         
         NAME                                                                            ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srequiredlabels.constraints.gatekeeper.sh/namespace-sidecar-injection-label   deny                 0
         NAME                                                                          ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         asmpeerauthnmeshstrictmtls.constraints.gatekeeper.sh/mesh-level-strict-mtls   deny                 0
         NAME                                                                               ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         destinationruletlsenabled.constraints.gatekeeper.sh/destination-rule-tls-enabled   deny                 0
         NAME                                                                              ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         asmpeerauthnstrictmtls.constraints.gatekeeper.sh/peerauthentication-strict-mtls   deny                 0
         NAME                                                                             ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         asmsidecarinjection.constraints.gatekeeper.sh/pod-sidecar-injection-annotation   deny                 0
         




### Enforce granular access control

In this section you enforce policies to ensure that all workloads in the mesh have [granular access control](https://docs.cloud.google.com/service-mesh/docs/security/authorization-policy-overview).

  1. To enforce granular access control, apply constraints.

The following command uses `sed` to update the `acm-config.yaml` manifest to get Config Sync deploying the associated resources.
         
         sed -i "s,root-sync/fix-strict-mtls,root-sync/enforce-authorization-policies,g" ~/asm-acm-tutorial-dir/acm-config.yaml
         gcloud beta container fleet config-management apply \
             --membership ${MEMBERSHIP} \
             --config ~/asm-acm-tutorial-dir/acm-config.yaml
         

The preceding command deploys the following resources:

     * An [`AsmAuthzPolicyDefaultDeny`](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#asmauthzpolicydefaultdeny) `Constraint` which enforces the mesh-level default deny `AuthorizationPolicy` in the `istio-system` namespace:
           
           apiVersion: constraints.gatekeeper.sh/v1beta1
           kind: AsmAuthzPolicyDefaultDeny
           metadata:
             name: default-deny-authorization-policies
           spec:
             enforcementAction: deny
             parameters:
               rootNamespace: istio-system
               strictnessLevel: High

     * An [`AsmAuthzPolicyEnforceSourcePrincipals`](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#asmauthzpolicyenforcesourceprincipals) `Constraint` which enforces that any `AuthorizationPolicies` is defining granular source principals (other than "*"). Only the ingress gateway in the `asm-ingress` namespace is an exception to this rule in order to receive the traffic from the end-users and redirect the traffic to the Online Boutique's `frontend` app.
           
           apiVersion: constraints.gatekeeper.sh/v1beta1
           kind: AsmAuthzPolicyEnforceSourcePrincipals
           metadata:
             name: authz-source-principals-not-all
           spec:
             enforcementAction: deny
             match:
               kinds:
               - apiGroups:
                 - security.istio.io
                 kinds:
                 - AuthorizationPolicy
               excludedNamespaces:
                 - asm-ingress

  2. View the Config Sync status for the `RootSync`:
         
         gcloud alpha anthos config sync repo describe \
             --sync-name root-sync \
             --sync-namespace config-management-system
         

The output is similar to:
         
         getting 1 RepoSync and RootSync from projects/PROJECT_ID/locations/global/memberships/asm-acm-tutorial
         [
           {
             "clusters": [
               "projects/PROJECT_ID/locations/global/memberships/asm-acm-tutorial"
             ],
             "commit": "7d15d49af13c44aa531a4565b2277ddcf8b81884",
             "errors": [],
             "source": "https://github.com/GoogleCloudPlatform/anthos-config-management-samples//asm-acm-tutorial/root-sync/enforce-authorization-policies@main",
             "status": "SYNCED"
           }
         ]
         

If you see `status: RECONCILING` instead of `status: SYNCED`, wait a few minutes and run `gcloud alpha anthos config sync repo describe` again.

  3. Run the following command to get more information about the associated violation:
         
         kubectl get asmauthzpolicydefaultdeny.constraints.gatekeeper.sh/default-deny-authorization-policies -ojsonpath='{.status.violations}'  | jq
         

The output is similar to:
         
         [
           {
             "enforcementAction": "deny",
             "group": "constraints.gatekeeper.sh",
             "kind": "AsmAuthzPolicyDefaultDeny",
             "message": "Root namespace <istio-system> does not have a default deny AuthorizationPolicy",
             "name": "default-deny-authorization-policies",
             "version": "v1beta1"
           }
         ]
         

  4. Fix the issue by deploying the `AuthorizationPolicy` in the `istio-system` namespace.

The following command uses `sed` to update the `acm-config.yaml` manifest to get Config Sync deploying the associated resources.
         
         sed -i "s,root-sync/enforce-authorization-policies,root-sync/fix-default-deny-authorization-policy,g" ~/asm-acm-tutorial-dir/acm-config.yaml
         gcloud beta container fleet config-management apply \
             --membership ${MEMBERSHIP} \
             --config ~/asm-acm-tutorial-dir/acm-config.yaml
         

The preceding command deploys the following deny-all `AuthorizationPolicy` in the `istio-system` namespace:
         
         apiVersion: security.istio.io/v1beta1
         kind: AuthorizationPolicy
         metadata:
           name: deny-all
         spec:
           {}

  5. View the Config Sync status for the `RootSync`:
         
         gcloud alpha anthos config sync repo describe \
             --sync-name root-sync \
             --sync-namespace config-management-system
         

The output is similar to:
         
         getting 1 RepoSync and RootSync from projects/PROJECT_ID/locations/global/memberships/asm-acm-tutorial
         [
           {
             "clusters": [
               "projects/PROJECT_ID/locations/global/memberships/asm-acm-tutorial"
             ],
             "commit": "7d15d49af13c44aa531a4565b2277ddcf8b81884",
             "errors": [],
             "source": "https://github.com/GoogleCloudPlatform/anthos-config-management-samples//asm-acm-tutorial/root-sync/fix-default-deny-authorization-policy@main",
             "status": "SYNCED"
           }
         ]
         

If you see `status: RECONCILING` instead of `status: SYNCED`, wait a few minutes and run `gcloud alpha anthos config sync repo describe` again.

  6. Verify the `Constraints` are created:
         
         kubectl get constraints
         

Note this can take a few minutes to get Policy Controller evaluating these `Constraints`. Wait and run again this `kubectl get constraints` command until you get values under the `TOTAL-VIOLATIONS` column for each line.

The output is similar to:
         
         NAME                                                                             ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         asmsidecarinjection.constraints.gatekeeper.sh/pod-sidecar-injection-annotation   deny                 0
         NAME                                                                            ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srequiredlabels.constraints.gatekeeper.sh/namespace-sidecar-injection-label   deny                 0
         NAME                                                                                      ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         asmauthzpolicydefaultdeny.constraints.gatekeeper.sh/default-deny-authorization-policies   deny                 0
         NAME                                                                          ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         asmpeerauthnmeshstrictmtls.constraints.gatekeeper.sh/mesh-level-strict-mtls   deny                 0
         NAME                                                                               ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         destinationruletlsenabled.constraints.gatekeeper.sh/destination-rule-tls-enabled   deny                 0
         NAME                                                                              ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         asmpeerauthnstrictmtls.constraints.gatekeeper.sh/peerauthentication-strict-mtls   deny                 0
         NAME                                                                                              ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         asmauthzpolicyenforcesourceprincipals.constraints.gatekeeper.sh/authz-source-principals-not-all   deny                 0
         

  7. Visit the Online Boutique app from your browser:
         
         echo http://${EXTERNAL_IP}
         

You should receive the error: `RBAC: access denied` which confirms that the default deny `AuthorizationPolicy` is applied to the entire mesh.

  8. Fix this issue by deploying more granular `AuthorizationPolicies` in the `asm-ingress` and `onlineboutique` namespaces.

The following command uses `sed` to update the `acm-config.yaml` manifest to get Config Sync deploying the associated resources.
         
         sed -i "s,root-sync/fix-default-deny-authorization-policy,root-sync/deploy-authorization-policies,g" ~/asm-acm-tutorial-dir/acm-config.yaml
         gcloud beta container fleet config-management apply \
             --membership ${MEMBERSHIP} \
             --config ~/asm-acm-tutorial-dir/acm-config.yaml
         

The preceding command deploys the following resources:

     * An `AuthorizationPolicy` in the `asm-ingress` namespace:
           
           apiVersion: security.istio.io/v1beta1
           kind: AuthorizationPolicy
           metadata:
             name: asm-ingressgateway
           spec:
             selector:
               matchLabels:
                 asm: ingressgateway
             rules:
             - to:
               - operation:
                   ports:
                   - "8080"

     * An `AuthorizationPolicy` per app in the `onlineboutique` namespace, here is the example for the `cartservice` app:
           
           apiVersion: security.istio.io/v1beta1
           kind: AuthorizationPolicy
           metadata:
             name: cartservice
           spec:
             selector:
               matchLabels:
                 app: cartservice
             rules:
             - from:
               - source:
                   principals:
                   - cluster.local/ns/onlineboutique/sa/frontend
                   - cluster.local/ns/onlineboutique/sa/checkoutservice
               to:
               - operation:
                   paths:
                   - /hipstershop.CartService/AddItem
                   - /hipstershop.CartService/GetCart
                   - /hipstershop.CartService/EmptyCart
                   methods:
                   - POST
                   ports:
                   - "7070"

     * A `ServiceAccount` per app in the `asm-ingress` and `onlineboutique` namespaces in order to have a unique identity per app evaluated as `principal` in the `AuthorizationPolicies`. Here is the example for the `cartservice` app:
           
           apiVersion: v1
           kind: ServiceAccount
           metadata:
             name: cartservice

  9. View the Config Sync status for the `RootSync` and the two `RepoSyncs`:
         
         gcloud alpha anthos config sync repo describe
         

The output is similar to:
         
         getting 3 RepoSync and RootSync from projects/PROJECT_ID/locations/global/memberships/asm-acm-tutorial
         [
           {
             "clusters": [
               "projects/PROJECT_ID/locations/global/memberships/asm-acm-tutorial"
             ],
             "commit": "7d15d49af13c44aa531a4565b2277ddcf8b81884",
             "errors": [],
             "source": "https://github.com/GoogleCloudPlatform/anthos-config-management-samples//asm-acm-tutorial/root-sync/deploy-authorization-policies@main",
             "status": "SYNCED"
           },
           {
             "clusters": [
               "projects/PROJECT_ID/locations/global/memberships/asm-acm-tutorial"
             ],
             "commit": "7d15d49af13c44aa531a4565b2277ddcf8b81884",
             "errors": [],
             "source": "https://github.com/GoogleCloudPlatform/anthos-config-management-samples//asm-acm-tutorial/ingress-gateway/authorization-policies@main",
             "status": "SYNCED"
           },
           {
             "clusters": [
               "projects/PROJECT_ID/locations/global/memberships/asm-acm-tutorial"
             ],
             "commit": "7d15d49af13c44aa531a4565b2277ddcf8b81884",
             "errors": [],
             "source": "https://github.com/GoogleCloudPlatform/anthos-config-management-samples//asm-acm-tutorial/online-boutique/authorization-policies@main",
             "status": "SYNCED"
           }
         ]
         

If you see `status: RECONCILING` instead of `status: SYNCED`, wait a few minutes and run `gcloud alpha anthos config sync repo describe` again.

To only view the information of one repository you can use the `--sync-name` and `--sync-namespace` flags. And to view in detail the managed resources, you can add the `--managed-resources` flag. For more information, see [View Config Sync status across multiple clusters](https://docs.cloud.google.com/anthos-config-management/docs/how-to/config-sync-status-gcloud#describe-a-repo).

  10. Visit the Online Boutique app again from your browser:
         
         echo http://${EXTERNAL_IP}
         

If you wait a few minutes, you should now see the website working successfully again as expected.




## View the status of GKE Enterprise security features

You can view the status of GKE Enterprise security features, including authentication and authorization policies, in the Google Cloud console.

  1. In the Google Cloud console, go to the **GKE Enterprise Security** page.

[Go to GKE Enterprise Security](https://console.cloud.google.com/anthos/security)

The **Policy Summary** displays the status of application security, including Service access control (`AuthorizationPolicies`) and mTLS.

  2. Click **Policy Audit** to view workload policy statuses for the cluster and both namespaces (`asm-ingress` and `onlineboutique`).

The **Service access control** and **mTLS status** cards provide a high-level overview.

![High-level overview of service access control and mTLS status ](https://docs.cloud.google.com/static/anthos-config-management/docs/img/service-access-mtls-status.png)

The **Workloads** list shows the Service access control and mTLS status of each workload.

![Detailed list of each workload and its service access control and mTLS status](https://docs.cloud.google.com/static/anthos-config-management/docs/img/workloads.png)




You now have secured your cluster and your mesh with Policy Controller and Config Sync.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    gcloud projects delete PROJECT_ID




### Delete individual resources

To delete the individual resources:

  1. Unregister your cluster from the fleet:

###  gcloud 
         
         gcloud container fleet memberships unregister ${CLUSTER} \
             --project=${PROJECT_ID} \
             --gke-cluster=${CLUSTER_ZONE}/${CLUSTER}
         

The output is similar to the following:
         
         kubeconfig entry generated for asm-acm-tutorial.
         Waiting for membership to be deleted...done.
         Deleting membership CR in the cluster...done.
         Deleting namespace [gke-connect] in the cluster...done.
         

### Config Connector
         
         kubectl delete -f ~/asm-acm-tutorial-dir/fleet-membership.yaml
         

  2. Delete your cluster:

###  gcloud 
         
         gcloud container clusters delete ${CLUSTER} \
             --zone ${CLUSTER_ZONE}
         

Press `y` when prompted. This command can take over five minutes to complete.

The output is similar to the following:
         
         Deleting cluster asm-acm-tutorial...done.
         Deleted [https://container.googleapis.com/v1/projects/PROJECT_ID/zones/us-east4-a/clusters/asm-acm-tutorial].
         

### Config Connector
         
         kubectl delete -f ~/asm-acm-tutorial-dir/container-cluster.yaml
         

  3. Delete the files that you created:
         
         rm -r ~/asm-acm-tutorial-dir
         




## What's next

  * Discover [Cloud Service Mesh security best practices](https://docs.cloud.google.com/service-mesh/docs/security/anthos-service-mesh-security-best-practices).
  * Learn more about the [Cloud Service Mesh policy bundle](https://docs.cloud.google.com/anthos-config-management/docs/how-to/using-asm-security-policy).
  * Explore the Policy Controller [constraint template library](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library).
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
