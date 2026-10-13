---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/deploy-container-workloads/
title: Deploy a containerized web server app \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:22:04.436438+00:00
---

# Deploy a containerized web server app  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/deploy-container-workloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Deploy a containerized web server app Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial describes how to upload a container application in a Google Distributed Cloud (GDC) air-gapped appliance environment, and run that application in the appliance environment. You'll learn how to create Harbor projects, upload images to Harbor and create workloads as part of this tutorial. A containerized workload runs within a project namespace.

The GDC air-gapped appliance environment comes with a preconfigured Harbor registry called `tear-harbor` for you in a GDC project called `tear`. You'll use this registry in this example.

This tutorial uses a sample web server app available from the Google Cloud Artifact Registry.

## Objectives

  * Push a container image to the managed Harbor registry.
  * Deploy the sample container app to the cluster.



## Before you begin

To complete the tasks in this document, you must request the necessary permissions and prepare your environment.

### Request IAM roles

Ask your Project IAM Admin to grant you the following roles in your project namespace based on the task to perform:

  * **Namespace Admin** (`namespace-admin`): create, delete, edit, and view project resources. This role is required to deploy container workloads in your project.

  * **Harbor Instance Viewer** (`harbor-instance-viewer`): view and select a Harbor instance.

  * **Harbor Project Creator** (`harbor-project-creator`): create and view Harbor projects.




### Prepare your environment

  1. Make sure you have a project to manage your containerized deployments. [Create a project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/create-a-project) if you don't have one.

  2. Set your project namespace as an environment variable:
         
         export NAMESPACE=PROJECT_NAMESPACE
         

  3. [Download and install the gdcloud CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-overview).

  4. [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/sign-in#kubernetes-cluster-kubeconfig) to the Kubernetes cluster and generate its kubeconfig file with a user identity. Make sure that you set the kubeconfig path as an environment variable:
         
         export KUBECONFIG=CLUSTER_KUBECONFIG
         




## Create Harbor project in registry

GDC provides Harbor as a Service, which is a fully managed service that lets you store and manage container images using Harbor.

To use Harbor as a Service, you must create a Harbor project within the `tear-harbor` registry instance to manage your container images:

  1. You need `tear-harbor`'s URL. List the instance`s URL:
         
         gdcloud harbor instances describe tear-harbor --project=tear
         

The output is similar to `harbor-1.org-1.zone1.google.gdc.test`.

  2. Set the instance URL as a variable to use later in the tutorial:
         
         export INSTANCE_URL=INSTANCE_URL
         

Enter the instance URL without the `https://` prefix.

  3. Before you create the project, you must sign in into Harbor using the URL from the previous step. Use a browser to open this URL and sign in into the Harbor instance.

  4. Create the Harbor project:
         
         gdcloud harbor harbor-projects create HARBOR_PROJECT \
             --project=tear \
             --instance=tear-harbor
         

Replace `HARBOR_PROJECT` with the name of the Harbor project to create. You can't create the Harbor project in any project namespace. You must use the `tear` project.

  5. Set the Harbor project name as a variable to use later in the tutorial:
         
         export HARBOR_PROJECT=HARBOR_PROJECT
         




### Configure Docker

To use Docker in your Harbor registry, complete the following steps:

  1. Configure Docker to trust Harbor as a Service. For more information, see [Configure Docker to trust Harbor root CA](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/configure-docker-trust).

  2. Configure Docker authentication to Harbor. For more information, see [Configure Docker authentication to Harbor registry instances](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/configure-docker-authentication).

  3. Since `tear-harbor` is a preconfigured Harbor registry, you must trust the certificate signed by Google Distributed Cloud air-gapped internal CA:

     1. Ask your IO for the following information:

        1. the external URL of the Harbor cluster.
        2. the `.crt` file of the Google Distributed Cloud air-gapped internal CA. The file is generally stored in the control plane as a secret by the `trust-store-internal-only` name in the `anthos-creds` namespace.
     2. Similar to the previous step, create a folder by the name of the external URL of the Harbor cluster and keep the `.crt` file inside the folder.




### Create Kubernetes image pull secret

Since you're using a private Harbor project, you must create a Kubernetes image pull secret.

**Important:** To access the URLs on this page, you must connect to the internet. The URLs are provided for use when you have such access.

  1. Add a Harbor project robot account. Follow the steps in the Harbor UI to create the robot account and copy the robot secret token: <https://goharbor.io/docs/2.8.0/working-with-projects/project-configuration/create-robot-accounts/#add-a-robot-account>.

  2. Note the new robot project account name, which has the following syntax:
         
         <PREFIX><PROJECT_NAME>+<ACCOUNT_NAME>
         

For example, the robot project account name format resembles `harbor@library+artifact-account`.

For more information on finding your robot project account name in Harbor, see Harbor's documentation: <https://goharbor.io/docs/2.8.0/working-with-projects/project-configuration/create-robot-accounts/#view-project-robot-accounts>.

  3. Sign in to Docker with your Harbor project robot account and secret token:
         
         docker login ${INSTANCE_URL}
         

When prompted, insert the robot project account name for the `Username` and the secret token for the `Password`.

  4. Set an arbitrary name for the image pull secret:
         
         export SECRET=SECRET
         

  5. Create the secret that is required for the image pull:
         
         kubectl create secret docker-registry ${SECRET}  \
             --from-file=.dockerconfigjson=DOCKER_CONFIG \
             -n NAMESPACE
         

Replace the following:

     * `DOCKER_CONFIG`: the path to the `.docker/config.json` file.
     * `NAMESPACE`: the namespace for the secret you create.



## Push container image to managed Harbor registry

For this tutorial, you will download and push the `nginx` web server image to the managed Harbor registry, and use it to deploy a sample nginx web server app to a Kubernetes cluster. The nginx web server app is available from the public Google Cloud Artifact Registry.

**Important:** To pull the `nginx` web server app from the Google Cloud Artifact Registry, you must have internet access.

  1. Pull the `nginx` image from the Google Cloud Artifact Registry to your local workstation using an external network:
         
         docker pull gcr.io/cloud-marketplace/google/nginx:1.25
         

  2. Set the name of the image. The format of a full image name is the following:
         
         ${INSTANCE_URL}/${HARBOR_PROJECT}/nginx
         

  3. Tag the local image with the repository name:
         
         docker tag gcr.io/cloud-marketplace/google/nginx:1.25 ${INSTANCE_URL}/${HARBOR_PROJECT}/nginx:1.25
         

  4. Push the `nginx` container image to your managed Harbor registry:
         
         docker push ${INSTANCE_URL}/${HARBOR_PROJECT}/nginx:1.25
         




## Deploy the sample container app

You are now ready to deploy the `nginx` container image to the appliance cluster.

Kubernetes represents applications as `Pod` resources, which are scalable units holding one or more containers. The pod is the smallest deployable unit in Kubernetes. Usually, you deploy pods as a set of replicas that can be scaled and distributed together across your cluster. One way to deploy a set of replicas is through a Kubernetes `Deployment`.

In this section, you create a Kubernetes `Deployment` to run the `nginx` container app on your cluster. This Deployment has replicas, or pods. One `Deployment` pod contains only one container: the `nginx` container image. You also create a `Service` resource that provides a stable way for clients to send requests to the pods of your `Deployment`.

Deploy the nginx web server:

  1. Create and deploy the Kubernetes `Deployment` and `Service` custom resources:
         
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
         

  2. Verify the pods were created by the deployment:
         
         kubectl get pods -l app=nginx -n ${NAMESPACE}
         

The output is similar to the following:
         
         NAME                                READY     STATUS    RESTARTS   AGE
         nginx-deployment-1882529037-6p4mt   1/1       Running   0          1h
         nginx-deployment-1882529037-p29za   1/1       Running   0          1h
         nginx-deployment-1882529037-s0cmt   1/1       Running   0          1h
         

  3. Create a network policy to allow all network traffic to the namespace:
         
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
         

  4. Export the IP address for the `nginx` service:
         
         export IP=`kubectl --kubeconfig=${KUBECONFIG} get service nginx-service \
               -n ${NAMESPACE} -o jsonpath='{.status.loadBalancer.ingress[*].ip}'`
         

  5. Test the `nginx` server IP address using `curl`:
         
         curl http://$IP
         




## What's next

  * Read the [containers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/containers/containers-intro) documentation for information on how to manage containers.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
