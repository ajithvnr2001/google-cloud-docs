---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/slurm-on-gke/quickstarts/deploy-slurm-on-gke/
title: Quickstart: Deploy a Slurm cluster on GKE \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:26:18.619056+00:00
---

# Quickstart: Deploy a Slurm cluster on GKE  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/slurm-on-gke/quickstarts/deploy-slurm-on-gke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Quickstart: Deploy a Slurm cluster on GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Preview — Slurm Operator add-on for GKE**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document explains how to quickly deploy and configure a basic Slurm cluster on Google Kubernetes Engine (GKE) by using the open-source Slurm Helm chart and the Slurm Operator add-on for GKE. This setup includes a Slurm controller (`slurmctld`), REST API (`slurmrestd`), a login node for user access, and a single worker node (`slurmd`) managed by the Slurm Operator add-on for GKE.

This document is for Data administrators, Operators, and Developers who want to enable and configure the Slurm cluster on GKE.

Before reading this document, ensure that you're familiar with the [Slurm Operator add-on for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/slurm-on-gke/how-to/enable-slurm-operator-addon).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure you have already generated an SSH key pair. This key pair is required only if you want to set up OS Login.

  * Ensure you have a running GKE cluster with Slurm Operator enabled. If not, create one:
        
        gcloud container clusters create CLUSTER_NAME \
            --cluster-version=VERSION \
            --location=LOCATION \
            --project=PROJECT_ID \
            --addons=SlurmOperator
        

Replace the following:

    * `CLUSTER_NAME`: the name of the new cluster.
    * `VERSION`: the GKE version, which must be 1.35.2-gke.1842000 or later. You can also use the `--release-channel` option to select a release channel. The release channel must have a default version of 1.35.2-gke.1842000 or later.
    * `LOCATION`: the location of the cluster.
    * `PROJECT_ID`: the ID of the project.

For more information, see [enable Slurm Operator add-on for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/slurm-on-gke/how-to/enable-slurm-operator-addon).




## (Optional) Configure OS Login

OS Login simplifies SSH access management by linking your Linux user account to your IAM identity. This configuration lets you manage access to Slurm nodes by using IAM permissions.

**Warning:** OS Login is not supported for node pools that use the GKE metadata server, which includes node pools with [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) enabled. If you need both Workload Identity Federation for GKE and OS Login in your Slurm cluster consider creating a separate node pool for the loginset.

  1. Grant necessary IAM roles. Ensure your user account has the necessary IAM roles in the project:

     * `roles/compute.osLogin`: lets you manage your own OS Login profile.
     * `roles/compute.instanceAdmin.v1`: provides permissions to manage compute instances.
     * `roles/iam.serviceAccountUser`: lets users act as a service account, which is often needed for node operations.

For more information about the required roles, see [the guide to set up OS Login](https://docs.cloud.google.com/compute/docs/oslogin/set-up-oslogin#assign_os_login_iam_roles).

  2. Add your SSH key to OS Login by uploading your public SSH key:
         
         gcloud compute os-login ssh-keys add --key-file=PATH_TO_PUBLIC_KEY --project=PROJECT_ID
         

Alternatively, you can add a key that's loaded in your `ssh-agent`:
         
         gcloud compute os-login ssh-keys add --key="$(ssh-add -L | grep publickey | head -n 1)" --project=PROJECT_ID
         

  3. Enable OS Login in your project metadata:
         
         gcloud compute project-info add-metadata --metadata enable-oslogin=TRUE --project=PROJECT_ID
         

  4. Get your OS Login username:
         
         gcloud compute os-login describe-profile | grep username
         

The output is similar to the following:
         
         username: OSLOGIN_USERNAME
         

The output includes the `OSLOGIN_USERNAME` value. You use this value later in this document.


**Best practice** : 

For managing OS Login across multiple projects in an organization, consider enforcing OS Login by using an Organization Policy Service constraint (`compute.requireOsLogin`). This is a recommended security best practice. For more information, see [Enable and configure OS Login in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/enable-oslogin).

## (Optional) Add a compute node pool

If you want to run Slurm compute workloads on separate nodes, you can create a dedicated node pool for them.
    
    
    gcloud container node-pools create NODE_POOL_NAME \
        --cluster=CLUSTER_NAME \
        --machine-type=MACHINE_TYPE \
        --num-nodes=NUM_NODES \
        --node-taints=slurm-worker=true:NoSchedule
    

Replace the following:

  * `NODE_POOL_NAME`: the name of the new node pool.
  * `CLUSTER_NAME`: the name of your cluster.
  * `MACHINE_TYPE`: the machine type for the nodes (for example: `n2-standard-4`).
  * `NUM_NODES`: the number of nodes in the node pool.



## Deploy Slurm using Helm

This section guides you through deploying the Slurm cluster components by using the Slurm Helm chart. The Helm chart deploys `slurmctld`, `slurmrestd`, and `slurmd` components within the GKE cluster.

  1. Configure `kubectl` to communicate with your cluster:
         
         gcloud container clusters get-credentials CLUSTER_NAME
         

Replace CLUSTER_NAME with your cluster name.

  2. Verify that you are running Helm 3.8.0 or later.
         
         helm version
         

The output is similar to the following:
         
         version.BuildInfo{Version:"v3.17.3", GitCommit:"e4da49785aa6e6ee2b86efd5dd9e43400318262b", GitTreeState:"clean", GoVersion:"go1.23.7"}
         

If needed, you can install Helm by following the [official Helm documentation](https://helm.sh/docs/intro/install/).

  3. Find an available image tag:

     1. In the Google Cloud console, go to the **Artifact Registry repository** page that includes the `slinky/slurmd` package.

[Go to Artifact Registry repository](https://console.cloud.google.com/artifacts/docker/gke-release/us/gcr.io/slinky%2Fslurmd)

     2. Annotate one of the image tag value, for example `25.11-ubuntu24.04-gke.4`. You use this tag in the IMAGE_TAG placeholder in the following configuration file.

  4. Save the following configuration to a new file named `values.yaml`:
         
         controller:
             slurmctld:
                 image:
                     repository: gcr.io/gke-release/slinky/slurmctld
                     tag: IMAGE_TAG
             reconfigure:
                 image:
                     repository: gcr.io/gke-release/slinky/slurmctld
                     tag: IMAGE_TAG
         
         restapi:
             replicas: 1
             slurmrestd:
                 image:
                     repository: gcr.io/gke-release/slinky/slurmrestd
                     tag: IMAGE_TAG
         
         nodesets:
             slinky:
                 replicas: 1
                 slurmd:
                     image:
                         repository: gcr.io/gke-release/slinky/slurmd
                         tag: IMAGE_TAG
         
                 # The podSpec block is optional and only required when using
                 # a dedicated node pool for compute nodes.
                 podSpec:
                     nodeSelector:
                         cloud.google.com/gke-nodepool: NODE_POOL_NAME
                     tolerations:
                         - key: "slurm-worker"
                           operator: "Equal"
                           value: "true"
                           effect: "NoSchedule"
         
         loginsets:
             slinky:
                 enabled: true
                 replicas: 1
                 login:
                     image:
                         repository: gcr.io/gke-release/slinky/login
                         tag: IMAGE_TAG
         

Replace IMAGE_TAG with the tag that you copied in the previous step. For example, use `25.11-ubuntu24.04-gke.4`.

**Warning:** Enabling the loginset in your configuration automatically creates a Kubernetes Service of type LoadBalancer. By default, this provisions an external, public IP address that exposes the Slurm login node (port 22) to the internet, which can pose security risks.
  5. Install the Slurm Helm chart by using the `values.yaml` file:
         
         helm install slurm oci://ghcr.io/slinkyproject/charts/slurm \
             --namespace=slurm --create-namespace --version 1.0.2 -f values.yaml
         




## Verify the Slurm installation

You can verify that Slurm is deployed on the cluster by using `kubectl`.

  1. Check Pod status:
         
         kubectl get pods --namespace slurm
         

The output should be similar to the following, and show the `Running` status for all Pods:
         
         NAME                                  READY   STATUS    RESTARTS   AGE
         slurm-controller-0                    3/3     Running   0          60s
         slurm-login-slinky-5d79cd755c-mf62z   1/1     Running   0          60s
         slurm-restapi-6b4ccb479f-njlp9        1/1     Running   0          60s
         slurm-worker-slinky-0                 2/2     Running   0          60s
         

  2. To see the registered nodes, execute the `sinfo` command on the login node:
         
         kubectl exec -it deployment/slurm-login-slinky -n slurm -- sinfo
         

The output should list the `slinky` partition and the worker node.




## Run a Slurm Job

  1. To run a job, you need to access the Slurm login node. The way you access the login node depends on whether you have configured OS Login in the previous section.

     1. If you configured OS Login in the preceding section, access the login node by using SSH. To do this, get the`external IP address of`slurm-login-slinky` Service:
            
            kubectl get service --namespace slurm slurm-login-slinky
            

The output looks like this:
            
            NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP     PORT(S)        AGE
            slurm-login-slinky   LoadBalancer   10.X.X.X        X.X.X.X        22:30171/TCP   5m
            

Copy the value of the `EXTERNAL-IP` column.
            
            ssh OSLOGIN_USERNAME@EXTERNAL_IP
            

Replace the following:

        * `EXTERNAL_IP`: the IP address obtained in the previous step.
        * `OSLOGIN_USERNAME`: your [OS Login username](https://docs.cloud.google.com/compute/docs/oslogin#user_account_configuration).
     2. If you did not configure OS Login, you can still access the login node by using the `kubectl exec` command:
            
            kubectl exec -it deployment/slurm-login-slinky -n slurm -- bash
            

**Caution:** By entering the login node this way, you sign in as a root user, which can pose security risks.
  2. Run an interactive job: After you're in the login node, you can run a command on a compute node by using the `srun` command line utility.
         
         srun hostname
         

The output includes the hostname of the `slurm-worker-slinky-0` Pod.




## Clean up

To avoid incurring charges, clean up the resources created in this document.

  1. Uninstall the Helm deployment: This command removes all Kubernetes resources deployed by the Helm chart.
         
         helm uninstall slurm --namespace slurm
         

  2. Delete the Slurm namespace:
         
         kubectl delete namespace slurm
         

  3. Delete the GKE cluster:
         
         gcloud container clusters delete CLUSTER_NAME  \
             --location=LOCATION \
         

Replace the following:

     * `CLUSTER_NAME`: the name of the new cluster.
     * `LOCATION`: the region of cluster.



## What's next

  * Learn how to [autoscale a Slurm cluster](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/slurm-on-gke/how-to/autoscale-slurm-cluster-metrics).
  * Explore the [Slurm Project on GitHub](https://github.com/SlinkyProject/slurm-operator).
  * Learn [Slurm basics](https://slurm.schedmd.com/quickstart.html).
  * Learn how to [enable or disable the Slurm Operator add-on for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/slurm-on-gke/how-to/enable-slurm-operator-addon).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
