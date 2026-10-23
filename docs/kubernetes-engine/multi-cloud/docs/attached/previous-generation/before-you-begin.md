---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/previous-generation/before-you-begin/
title: Before you begin \u00a0|\u00a0 Anthos attached clusters (previous generation) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:43:45.820316+00:00
---

# Before you begin  |  Anthos attached clusters (previous generation)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/previous-generation/before-you-begin/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE attached clusters ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached)
  * [ Previous generation ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/previous-generation)



Send feedback 

#  Before you begin Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This page shows prerequisites for attaching conformant Kubernetes clusters to your fleet using the _previous generation_ of our attached clusters feature. If you're attaching an Amazon EKS or Azure AKS cluster, see [Attach your EKS cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/how-to/attach-cluster) or [Attach your AKS cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/aks/how-to/attach-cluster) for current instructions. The remainder of this document applies only to clusters built with distributions other than AKS or EKS.

Registering a Kubernetes cluster outside Google Cloud requires the following steps in addition to completing the [general prerequisites](https://docs.cloud.google.com/anthos/fleet-management/docs/before-you-begin).

## Ensure network connectivity

To successfully register your cluster, you need to ensure that the domains below are reachable from your Kubernetes cluster.

  * `cloudresourcemanager.googleapis.com` resolves metadata regarding the Google Cloud project the cluster is being connected to.
  * `oauth2.googleapis.com` to obtain short-lived OAuth tokens for agent operations against `gkeconnect.googleapis.com`.
  * `gkeconnect.googleapis.com` to establish the channel used to receive requests from Google Cloud and issues responses.
  * `gkehub.googleapis.com` to create Google Cloud-side Fleet membership resources that corresponds to the cluster you're connecting with Google Cloud.
  * `www.googleapis.com` to authenticate service tokens from incoming Google Cloud service requests.
  * `gcr.io` and `storage.googleapis.com` to pull the GKE Connect Agent image.



If you want to register the cluster [using fleet Workload Identity](https://docs.cloud.google.com/anthos/fleet-management/docs/use-workload-identity#cluster_setup), the following domains also must be reachable:

  * `securetoken.googleapis.com`
  * `iamcredentials.googleapis.com`
  * `sts.googleapis.com`



If you're using a [proxy](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/previous-generation/how-to/attach-kubernetes-clusters#proxy_support) for Connect, you must also update the proxy's allowlist with the relevant domains.

If you use [gcloud](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/previous-generation/how-to/attach-kubernetes-clusters#register_your_cluster) to register your Kubernetes cluster, these domains also need to be reachable in the environment where you run the gcloud commands.

## Using VPC Service Controls

If you want to use [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) for additional data security in your application, you need to ensure that the following services are in your service perimeter:

  * Resource Manager API (`cloudresourcemanager.googleapis.com`)
  * GKE Connect API (`gkeconnect.googleapis.com`)
  * Fleet API (`gkehub.googleapis.com`)



If you want to register your cluster with fleet Workload Identity enabled, you also need the following services:

  * IAM Service Account Credentials API (`iamcredentials.googleapis.com`)
  * Security Token Service API (`sts.googleapis.com`)



You also need to set up [private connectivity](https://docs.cloud.google.com/vpc-service-controls/docs/private-connectivity) for access to the relevant APIs. You can find out how to do this in [Setting up private connectivity](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-private-connectivity).

## Set up identity

All manual cluster registration options outside Google Cloud require you to configure authentication to Google. This can be either:

  * [Fleet Workload Identity](https://docs.cloud.google.com/anthos/fleet-management/docs/use-workload-identity) (recommended where available). You can find out more about the advantages of enabling fleet Workload Identity in [Use fleet Workload Identity](https://docs.cloud.google.com/anthos/fleet-management/docs/use-workload-identity).
  * A Google Cloud [service account](https://docs.cloud.google.com/iam/docs/service-accounts)



Attached clusters can be registered with fleet Workload Identity enabled if the cluster meets our Attached cluster prerequisites, as described below. Otherwise, register attached clusters with a Google Cloud service account for authentication. The next section shows you how to create a service account.

### Create a Google Cloud service account using `gcloud`

To manually register a cluster using a Google Cloud service account, you need a JSON file containing the service account credentials. To follow the [principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege), we recommend that you create a distinct service account for each Kubernetes cluster that you register, and only bind IAM roles to it for the corresponding cluster.

To create this file, perform the following steps:

### gcloud

Create a service account by running the following command:
    
    
    gcloud iam service-accounts create SERVICE_ACCOUNT_NAME --project=FLEET_HOST_PROJECT_ID
    

List all of a project's service accounts by running the following command:
    
    
    gcloud iam service-accounts list --project=FLEET_HOST_PROJECT_ID
    

If you are creating a distinct service account for each Kubernetes cluster that you register, bind the gkehub.connect IAM role to the service account for its corresponding cluster with an [IAM Condition](https://docs.cloud.google.com/iam/docs/conditions-overview) on the cluster's membership name:
    
    
    MEMBERSHIP_NAME=MEMBERSHIP_NAME
    FLEET_HOST_PROJECT_ID=FLEET_HOST_PROJECT_ID
    SERVICE_ACCOUNT_NAME=SERVICE_ACCOUNT_NAME
    gcloud projects add-iam-policy-binding ${FLEET_HOST_PROJECT_ID} \
       --member="serviceAccount:${SERVICE_ACCOUNT_NAME}@${FLEET_HOST_PROJECT_ID}.iam.gserviceaccount.com" \
       --role="roles/gkehub.connect" \
       --condition "expression=resource.name == \
    'projects/${FLEET_HOST_PROJECT_ID}/locations/global/memberships/${MEMBERSHIP_NAME}',\
    title=bind-${SERVICE_ACCOUNT_NAME}-to-${MEMBERSHIP_NAME}"
    

Otherwise, bind the role to the service account for all clusters in the project without the condition.
    
    
    FLEET_HOST_PROJECT_ID=FLEET_HOST_PROJECT_ID
    gcloud projects add-iam-policy-binding ${FLEET_HOST_PROJECT_ID} \
       --member="serviceAccount:SERVICE_ACCOUNT_NAME@${FLEET_HOST_PROJECT_ID}.iam.gserviceaccount.com" \
       --role="roles/gkehub.connect"
    

Download the service account's private key JSON file. You use this file when you [Register a cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster):
    
    
    FLEET_HOST_PROJECT_ID=FLEET_HOST_PROJECT_ID
    gcloud iam service-accounts keys create LOCAL_KEY_PATH \
       --iam-account=SERVICE_ACCOUNT_NAME@${FLEET_HOST_PROJECT_ID}.iam.gserviceaccount.com \
       --project=${FLEET_HOST_PROJECT_ID}
    

where:

  * FLEET_HOST_PROJECT_ID is the Google Cloud project ID in which you want to register clusters. [Learn how to find this value](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * SERVICE_ACCOUNT_NAME is the display name that you choose for the [Service Account].
  * MEMBERSHIP_NAME is the membership name that you choose to uniquely represent the cluster while [registering it](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster#register_cluster).
  * LOCAL_KEY_PATH is a local filepath where you'd like to save the service account's private key, a JSON file. We recommend that you name the file using the service account name and your project ID, such as `/tmp/creds/[SERVICE_ACCOUNT_NAME]-[FLEET_HOST_PROJECT_ID].json`.



## Attached cluster prerequisites

Depending on the type of third-party Kubernetes cluster you want to register as an [attached cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/previous-generation/how-to/attach-kubernetes-clusters), you may have to meet some additional requirements to install the Connect Agent and/or use fleet Workload Identity.

### Configure Security Context Constraints [(SCC)](https://docs.openshift.com/container-platform/4.6/authentication/managing-security-context-constraints.html) (OpenShift clusters)

On [OpenShift OKE](https://docs.openshift.com/container-platform/4.6/welcome/oke_about.html) and [OKD](https://www.okd.io/) clusters, administrators can use SCCs to control permissions for pods. To allow installing Connect Agent in your cluster, you need to create a custom SCC.

The following sample SCC definition specifies the set of conditions that Connect Agent must run with in order to be accepted into the cluster:
    
    
    # Connect Agent SCC
    apiVersion: security.openshift.io/v1
    kind: SecurityContextConstraints
    metadata:
      name: gke-connect-scc
    allowPrivilegeEscalation: false
    # This is redundant with non-root + disallow privilege escalation,
    # but we provide it for defense in depth.
    requiredDropCapabilities:
    - ALL
    runAsUser:
      type: MustRunAsNonRoot
    seLinuxContext:
      type: RunAsAny
    supplementalGroups:
      type: MustRunAs
      ranges:
      - min: 1
        max: 65535
    fsGroup:
      type: MustRunAs
      ranges:
      - min: 1
        max: 65535
    volumes:
    - secret
    - projected
    readOnlyRootFilesystem: true
    seccompProfiles:
    - docker/default
    users:
    groups:
      # Grants all service accounts in the gke-connect namespace access to this SCC
      - system:serviceaccounts:gke-connect

Assuming that you've saved your SCC definition as `gke-connect-scc.yaml`, use the OpenShift `oc` command line tool to create the `gke-connect-scc` SCC for your cluster, as follows:
    
    
    $ oc create -f gke-connect-scc.yaml
    

To verify that the custom SCC has been created, run the following `oc` command:
    
    
    $ oc get scc | grep gke-connect-scc
    

### Fleet Workload Identity requirements

You can register attached clusters with [fleet Workload Identity enabled](https://docs.cloud.google.com/anthos/fleet-management/docs/use-workload-identity) if your platform creates a public OIDC endpoint for your cluster (or allows you to create one), or if you have Kubernetes [service account issuer discovery](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#service-account-issuer-discovery) enabled for the cluster. If you can't meet these requirements, you must register attached clusters with a Google Cloud service account for authentication.

For specific cluster types, see the following:

  * **OpenShift clusters** : Can be registered with fleet Workload Identity enabled after you have configured your custom SCC, as described above.
  * **kind clusters** : Require [service account issuer discovery](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#service-account-issuer-discovery) to be enabled to use fleet Workload Identity. This is enabled by default from Kubernetes version 1.20. If you need to enable this feature, follow the instructions in [Service account token volume projection](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#service-account-token-volume-projection). Service account issuer discovery is enabled automatically when service account token volume project is enabled.



## What's next?

Follow the instructions to [register a cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/previous-generation/how-to/attach-kubernetes-clusters).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
