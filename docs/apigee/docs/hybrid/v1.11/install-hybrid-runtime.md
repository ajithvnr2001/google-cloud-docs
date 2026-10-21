---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-hybrid-runtime/
title: Step 9: Install hybrid runtime \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:28:24.329756+00:00
---

# Step 9: Install hybrid runtime  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-hybrid-runtime/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Step 9: Install hybrid runtime Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.11 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.11 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-hybrid-runtime.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-hybrid-runtime.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/install-hybrid-runtime.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/install-hybrid-runtime.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-hybrid-runtime.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/install-hybrid-runtime.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-hybrid-runtime.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-hybrid-runtime.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-hybrid-runtime.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/install-hybrid-runtime.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/install-hybrid-runtime.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/install-hybrid-runtime.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/install-hybrid-runtime.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/install-hybrid-runtime.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/install-hybrid-runtime.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/install-hybrid-runtime.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/install-hybrid-runtime.html)



##  Apply the configuration to the cluster 

Use the following steps to install Apigee hybrid into your cluster: 

  1. Be sure that you are in the `hybrid-base-directory/hybrid-files` directory. 
         
         cd $HYBRID_FILES

**Note:** Because the overrides file specifies service account files using paths relative to your `hybrid-base-directory/hybrid-files` directory, you must execute the commands from within that directory.
  2. Verify that `kubectl` is set to the correct context using the following command. The current context should be set to the cluster to which you are deploying Apigee hybrid. 
         
         kubectl config current-context

The result should include the name of the cluster you are deploying Apigee hybrid in. For example, on GKE, the context name is usually in the form `gke_project-id_cluster-location_cluster-name`, as in: 
         
         gke_my-project_us-central1_my-cluster

If the name cluster name in the context does not match, the following command will get the `gcloud` credentials of the cluster and set the `kubectl` context:

### Regional clusters
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
         --region $CLUSTER_LOCATION \
         --project $PROJECT_ID

### Zonal clusters
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
         --zone $CLUSTER_LOCATION \
         --project $PROJECT_ID

  3.  _For**Anthos on bare metal** , **AWS on GKE** , **EKS** , and **GKE on prem** platforms only_, Verify that the [`KUBECONFIG`](https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/#set-the-kubeconfig-environment-variable) variable is set using the following command: 
         
         echo ${KUBECONFIG}

  4. Do a _dry run_ initialization. Doing a dry run lets you check for any errors before any changes are made to the cluster. Execute the `init` command with the `--dry-run` flag as follows: 
         
         **${APIGEECTL_HOME}** /apigeectl init -f overrides/overrides.yaml --dry-run=client

  5. If there are no errors, execute the `init` command as follows: 
         
         **${APIGEECTL_HOME}** /apigeectl init -f overrides/overrides.yaml

The `init` command installs the [Apigee deployment services](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/apigee-deployment-services) Apigee Deployment Controller and Apigee Admission Webhook.

  6. To check the status of the deployment, you can use the following commands: 
         
         **${APIGEECTL_HOME}** /apigeectl check-ready -f overrides/overrides.yaml
         
         kubectl get pods -n apigee-system
         
         kubectl get pods -n apigee

When the pods are ready, go to the next step. 

  7. Do a _dry run_ install. Execute the `apply` command with the `--dry-run` flag. 
         
         **${APIGEECTL_HOME}** /apigeectl apply -f overrides/overrides.yaml --dry-run=client

  8. If there are no errors, you can apply the [ Apigee-specific runtime components](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/what-is-hybrid#about-the-runtime-plane) to the cluster with the following command: 
         
         **${APIGEECTL_HOME}** /apigeectl apply -f overrides/overrides.yaml

  9. To check the status of the deployment, run the following command: 
         
         **${APIGEECTL_HOME}** /apigeectl check-ready -f overrides/overrides.yaml

Repeat this step until the pods are all ready. The pods may take several minutes to start up.


**Important:** Follow the steps in the [1.11.2-hotfix.3. release notes](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_1112-hotfix.3) to make sure you have installed the latest version of the hybrid runtime. **Congratulations!**

You've successfully installed and configured the Apigee hybrid runtime plane.

## GKE with Workload Identity

If you are installing Apigee hybrid on GKE and you are configuring Workload Identity to authenticate service accounts, in the next step, you will configure the associations between the Kubernetes service accounts and the Google service accounts for your cluster.

[1](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-create-cluster) [2](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-cert-manager) [3](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-apigeectl) [4](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-service-accounts) [5](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-create-tls-certificates) [6](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-configure-cluster) [7](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-enable-synchronizer-access) [8](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-check-cluster) [9](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-hybrid-runtime) [(NEXT) Step 10: Set up Workload Identity](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-workload-identity)

## All other installations

In the next step, you will configure the Apigee ingress gateway and deploy a proxy to test your installation.

[(NEXT) Step 1: Expose Apigee ingress](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-expose-apigee-ingress) [2](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-deploy-proxy)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
