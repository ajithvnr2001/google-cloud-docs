---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/deploy-container-workloads/
title: Deploy a containerized web server app \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:26:23.620219+00:00
---

# Deploy a containerized web server app  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/deploy-container-workloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Deploy a containerized web server app Stay organized with collections  Save and categorize content based on your preferences. 

[ Shared ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-configs#shared-cluster)

This tutorial describes how to upload a container application in an air-gapped Google Distributed Cloud (GDC) air-gapped environment, and run that application on a shared Kubernetes cluster. A containerized workload runs on a shared Kubernetes cluster within a project namespace. Shared clusters are logically separate from projects and from each other to provide different failure domains and isolation guarantees. However, you must ensure your shared cluster is attached to a project to allow for containerized workloads to be managed within a project.

This workflow is for application developers within the application operator group who are responsible for creating application workloads for their organization. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

One of the largest obstacles for deploying a container app is getting the binary for the app to your air-gapped data center. Work with your infrastructure team and administrators to transport the application to your workstation or implement this tutorial directly on your continuous integration and continuous delivery (CI/CD) server.

This tutorial uses a sample web server app available from the Google Cloud Artifact Registry.

## Objectives

  * Create a managed Harbor registry.
  * Push a container image to the managed Harbor registry.
  * Create a shared Kubernetes cluster.
  * Deploy the sample container app to the cluster.



## Costs

Because GDC is designed to run in an air-gapped data center, billing processes and information is confined only to the GDC deployment and is not managed by other Google products.

To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/billing/calculate-resource-usage).

Use the [Projected Cost dashboard](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/billing/estimate-projected-costs) to anticipate future SKU costs for your invoices.

To track storage and compute consumption, use the [Billing Usage dashboards](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/billing/track-resource-consumption).

## Before you begin

To complete the tasks in this document, you must request the necessary permissions and prepare your environment.

### Request IAM roles

You must have specific roles to get the permissions you need to complete this tutorial workflow. You must request roles scoped to your project and organization.

#### Organization roles

To create, delete, edit, or view a shared Kubernetes cluster, ask your Organization IAM Admin to grant you the **User Cluster Admin** (`user-cluster-admin`) role. This role isn't bound to a namespace.

If you don't have the permissions to create a shared cluster, ask your platform administrator to create one for you.

#### Project roles

Ask your Project IAM Admin to grant you the following roles in your project namespace based on the task to perform:

  * **Namespace Admin** (`namepspace-admin`): create, delete, edit, and view project resources. This role is required to deploy container workloads in your project.

  * **Harbor Instance Admin** (`harbor-instance-admin`): create, delete, edit, and view Harbor resources, including Harbor instances.

  * **Harbor Instance Viewer** (`harbor-instance-viewer`): view and select a Harbor instance.

  * **Harbor Project Creator** (`harbor-project-creator`): create and view Harbor projects.




### Prepare your environment

To complete this document, you must have the following resources:

  1. Make sure you have a project to manage your containerized deployments. [Create a project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-a-project) if you don't have one.

  2. Set your project namespace as an environment variable:
         
         export NAMESPACE=PROJECT_NAMESPACE
         

  3. [Download and install the gdcloud CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-overview).

  4. [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#zonal-resources-kubeconfig) to the zonal management API server and generate its kubeconfig file with a user identity. Set the kubeconfig path as an environment variable:
         
         export MANAGEMENT_API_SERVER=MANAGEMENT_API_SERVER_KUBECONFIG_PATH
         




## Create managed Harbor registry

GDC air-gapped provides Harbor as a Service, which is a fully managed service that lets you store and manage container images using Harbor.

To use Harbor as a Service, you must first create a Harbor registry instance and Harbor project.

### Create Harbor registry instance

To create a Harbor container registry instance, complete the following steps:

###  Console 

  1. In the navigation menu, select **Harbor Container Registry** from the **CI/CD** section.

  2. Select the zone in which to create your Harbor instance. A Harbor instance is a zonal resource and must be created in each zone manually to ensure high availability.

  3. Click **Create Instance**.

  4. Enter the name of the instance and accept the Harbor managed Terms of Service.

  5. Click **Create Instance**.

  6. Confirm your new Harbor instance exists in the **Harbor Instance** section.

  7. Click the **Go to Harbor Instance** external link and note the instance URL. For example, the instance URL format resembles `harbor-1.org-1.zone1.google.gdc.test`. The instance URL must not include the `https://` prefix.

  8. Set the instance URL as a variable to use later in the tutorial:
         
         export INSTANCE_URL=INSTANCE_URL
         

Replace INSTANCE_URL with the URL of the Harbor registry instance.

For example:
         
         export INSTANCE_URL=harbor-1.org-1.zone1.google.gdc.test
         




###  gdcloud 

  1. Create the new Harbor container registry instance:
         
         gdcloud harbor instances create INSTANCE_NAME \
             --project=PROJECT \
         

Replace the following:

     * `INSTANCE_NAME`: the name of the Harbor instance.
     * `PROJECT`: the name of the GDC project.
  2. List the instance's URL:
         
         gdcloud harbor instances describe INSTANCE_NAME \
             --project=PROJECT
         

The output looks similar to the following:
         
         # Several lines of code are omitted here.
         status:
           url: https://harbor-1.org-1.zone1.google.gdc.test
         

  3. Set the instance URL as a variable to use later in the tutorial:
         
         export INSTANCE_URL=INSTANCE_URL
         

Replace INSTANCE_URL with the URL of the Harbor registry instance. Make sure the instance URL does not include the `https://` prefix.

For example:
         
         export INSTANCE_URL=harbor-1.org-1.zone1.google.gdc.test
         




### Create Harbor project in registry

You must create a Harbor project within the Harbor registry instance to manage your container images:

###  Console 

  1. Click **Create A Harbor Project** from the **Harbor Container Registry** page.

  2. Enter the name of the project.

  3. Click **Create**.

  4. Set the Harbor project name as a variable to use later in the tutorial:
         
         export HARBOR_PROJECT=HARBOR_PROJECT
         




###  gdcloud 

  1. Create the new Harbor project:
         
         gdcloud harbor harbor-projects create HARBOR_PROJECT \
             --project=PROJECT \
             --instance=INSTANCE_NAME
         

Replace the following:

     * `HARBOR_PROJECT`: the name of the Harbor project to create.
     * `PROJECT`: the name of the GDC project.
     * `INSTANCE_NAME`: the name of the Harbor instance.
  2. Set the Harbor project name as a variable to use later in the tutorial:
         
         export HARBOR_PROJECT=HARBOR_PROJECT
         




### Configure Docker

To use Docker in your Harbor registry, complete the following steps:

  1. Configure Docker to trust Harbor as a Service. For more information, see [Configure Docker to trust Harbor root CA](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/configure-docker-trust).

  2. Configure Docker authentication to Harbor. For more information, see [Configure Docker authentication to Harbor registry instances](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/configure-docker-authentication).




### Create Kubernetes image pull secret

Since you're using a private Harbor project, you must create a Kubernetes image pull secret.

  1. Add a Harbor project robot account to serve as your service account.

     1. From the Harbor console, select your Harbor project.

     2. Click **Robot Accounts**.

     3. Select **New Robot Account**.

     4. Give your new robot account a name and define any additional settings.

     5. Click **Add**.

     6. The robot account name and secret are displayed on the success screen. Keep this screen open for reference in the next step.

For more information, see Harbor's documentation: <https://goharbor.io/docs/2.8.0/working-with-projects/project-configuration/create-robot-accounts/#add-a-robot-account>.

  2. In a new terminal window, sign in to Docker with your Harbor project robot account and secret token:
         
         docker login ${INSTANCE_URL}
         

When prompted, insert the robot project name for the **Username** and the secret token for the **Password** that were provided in the previous step from the Harbor console success screen.

  3. Set an arbitrary name for the image pull secret:
         
         export SECRET=SECRET
         

  4. Create the secret that is required for the image pull:
         
         kubectl create secret docker-registry ${SECRET}  \
             --from-file=.dockerconfigjson=DOCKER_CONFIG \
             -n ${NAMESPACE}
         

Replace `DOCKER_CONFIG` with the path to the `.docker/config.json` file.

  5. Confirm that your secret exists in your GDC project namespace:
         
         kubectl get secrets -n ${NAMESPACE}
         

The output is similar to the following:
         
         NAME          TYPE                               DATA     AGE
         my-secret     kubernetes.io/dockerconfigjson     1        23s
         




## Push container image to managed Harbor registry

For this tutorial, you will download and push the `nginx` web server image to the managed Harbor registry, and use it to deploy a sample nginx web server app to a shared Kubernetes cluster. The nginx web server app is available from the public Docker Hub repository.

**Important:** To pull the `nginx` web server app from Docker Hub, you must have internet access.

  1. Pull the `nginx` image from Docker Hub to your local workstation using an external network:
         
         docker pull nginx
         

  2. Tag the local image with the repository name:
         
         docker tag nginx ${INSTANCE_URL}/${HARBOR_PROJECT}/nginx:1.25
         

  3. Push the `nginx` container image to your managed Harbor registry:
         
         docker push ${INSTANCE_URL}/${HARBOR_PROJECT}/nginx:1.25
         




## Create a Kubernetes cluster

Now that you have the `nginx` container image stored in the managed Harbor registry and can access it, create a shared Kubernetes cluster to run the nginx web server.

###  Console 

  1. In the navigation menu, select **Kubernetes Engine > Clusters**.

  2. Click **Create Cluster**.

  3. In the **Name** field, specify a name for the cluster.

  4. Select the zone in which to create your Kubernetes cluster. A Kubernetes cluster is a zonal resource and must be created in each zone manually to ensure high availability.

  5. Click **Attach Project** and select a project to attach to your cluster. Then click **Save**.

  6. Click **Create**.

  7. Wait for the cluster to be created. When the cluster is available to use, the status `READY` appears next to the cluster name.




###  API 

  1. Create a `Cluster` custom resource and save it as a YAML file, such as `cluster.yaml`:
         
         apiVersion: cluster.gdc.goog/v1
         kind: Cluster
         metadata:
           name: CLUSTER_NAME
           namespace: platform
         

Replace the `CLUSTER_NAME` value with the name of the cluster.

  2. Apply the custom resource to your GDC instance:
         
         kubectl create -f cluster.yaml --kubeconfig ${MANAGEMENT_API_SERVER}
         

  3. [Attach a project to your Kubernetes cluster](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/manage-projects#add-cluster-to-project) using the GDC console. You can't attach a project to the cluster using the API at this time.




For more information about creating a shared Kubernetes cluster, see [Create a shared cluster](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-user-cluster). For more information about available cluster configuration options, see [Kubernetes cluster configurations](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-configs).

## Deploy the sample container app

You are now ready to deploy the `nginx` container image to your Kubernetes cluster.

Kubernetes represents applications as `Pod` resources, which are scalable units holding one or more containers. The pod is the smallest deployable unit in Kubernetes. Usually, you deploy pods as a set of replicas that can be scaled and distributed together across your cluster. One way to deploy a set of replicas is through a Kubernetes `Deployment`.

In this section, you create a Kubernetes `Deployment` to run the `nginx` container app on your cluster. This Deployment has replicas, or pods. One `Deployment` pod contains only one container: the `nginx` container image. You also create a `Service` resource that provides a stable way for clients to send requests to the pods of your `Deployment`.

Deploy the nginx web server to your Kubernetes cluster:

  1. [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#zonal-cluster-kubeconfig) to the Kubernetes cluster and generate its kubeconfig file with a user identity. Set the kubeconfig path as an environment variable:
         
         export KUBECONFIG=CLUSTER_KUBECONFIG_PATH
         

  2. Create and deploy the Kubernetes `Deployment` and `Service` custom resources:
         
         kubectl --kubeconfig ${KUBECONFIG} -n ${NAMESPACE} \
         create -f - <<EOF
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: nginx-deployment
           labels:
             app: nginx
         spec:
           replicas: 2
           selector:
             matchLabels:
               app: nginx
           template:
             metadata:
               labels:
                 app: nginx
             spec:
               containers:
               - name: nginx
                 image: ${INSTANCE_URL}/${HARBOR_PROJECT}/nginx:1.25
                 ports:
                 - containerPort: 80
               imagePullSecrets:
               - name: ${SECRET}
         ---
         apiVersion: v1
         kind: Service
         metadata:
           name: nginx-service
         spec:
           selector:
             app: nginx
           ports:
             - port: 80
               protocol: TCP
           type: LoadBalancer
         EOF
         

  3. Verify the pods were created by the deployment:
         
         kubectl get pods -l app=nginx -n ${NAMESPACE}
         

The output is similar to the following:
         
         NAME                                READY     STATUS    RESTARTS   AGE
         nginx-deployment-1882529037-6p4mt   1/1       Running   0          1h
         nginx-deployment-1882529037-p29za   1/1       Running   0          1h
         nginx-deployment-1882529037-s0cmt   1/1       Running   0          1h
         

  4. Create a network policy to allow all network traffic to the namespace:
         
         kubectl --kubeconfig ${KUBECONFIG} -n ${NAMESPACE} \
         create -f - <<EOF
         apiVersion: networking.k8s.io/v1
         kind: NetworkPolicy
         metadata:
           annotations:
           name: allow-all
         spec:
           ingress:
           - from:
             - ipBlock:
                 cidr: 0.0.0.0/0
           podSelector: {}
           policyTypes:
           - Ingress
         EOF
         

  5. Export the IP address for the `nginx` service:
         
         export IP=`kubectl --kubeconfig=${KUBECONFIG} get service nginx-service \
               -n ${NAMESPACE} -o jsonpath='{.status.loadBalancer.ingress[*].ip}'`
         

  6. Test the `nginx` server IP address using `curl`:
         
         curl http://$IP
         




## Clean up

To avoid incurring charges to your GDC account for the resources used in this tutorial, you must delete the resources you created.

### Delete the container image

To delete the container image from your GDC air-gapped environment, either delete the Harbor instance that contains the image, or keep the Harbor instance and delete the individual container image.

To delete the container image from the managed Harbor registry, use the GDC console:

  1. In the navigation menu, select **Harbor Container Registry** from the **CI/CD** section.

  2. Click the **Go to Harbor Instance** external link.

  3. Delete the container image using the Harbor UI. For more information, see [Delete Harbor registry instances](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/manage-harbor-instances#delete-harbor-registry-instances).




### Delete the container app

To delete the deployed container app, either [delete the GDC project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/delete-a-project) that contains the resources, or keep the GDC project and delete the individual resources.

To delete the individual resources, complete the following steps:

  1. Delete the `Service` object for your container app:
         
         kubectl delete service nginx-service -n ${NAMESPACE}
         

  2. Delete the `Deployment` object for your container app:
         
         kubectl delete deployment nginx-deployment -n ${NAMESPACE}
         

  3. If you created a test Kubernetes cluster solely for this tutorial, delete it:
         
         kubectl delete clusters.cluster.gdc.goog/USER_CLUSTER_NAME \
             -n platform --kubeconfig ${MANAGEMENT_API_SERVER}
         

This deletes the resources that make up the Kubernetes cluster, such as the compute instances, disks, and network resources:




## What's next

  * Explore the [resource hierarchy](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/resource-hierarchy) and details around resource isolation.

  * Learn about the [cluster architecture](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/clusters).

  * Read the [Kubernetes containers for GDC](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/containers/containers-intro) documentation for information on how to manage containers deployed to your Kubernetes clusters.

  * Learn how to [manage your Kubernetes clusters](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster) after your container workloads have been deployed.

  * Explore [best practices](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/workload-separation) for setting up your container workloads and other service resources.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
