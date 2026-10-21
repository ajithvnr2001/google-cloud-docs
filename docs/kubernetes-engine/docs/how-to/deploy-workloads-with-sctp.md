---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploy-workloads-with-sctp/
title: Deploy workloads with SCTP \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:46:26.717434+00:00
---

# Deploy workloads with SCTP  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploy-workloads-with-sctp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Deploy workloads with SCTP Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page explains how to deploy workloads that use the Stream Control Transmission Protocol (SCTP) on Google Kubernetes Engine (GKE) Standard clusters.

SCTP is supported on Cilium technology. Because [GKE Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2) is implemented using Cilium, you can use SCTP only on clusters that have been enabled with GKE Dataplane V2. With SCTP support, you can enable direct SCTP communication for Pod-to-Pod and Pod-to-Service traffic. To learn more, see [SCTP support on Cilium](https://docs.cilium.io/en/latest/configuration/sctp/).

This page is for Operators and Developers who provision and configure cloud resources and deploy apps and services. To learn more about common roles and example tasks referenced in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



### Requirements and limitations

SCTP support on GKE Standard clusters has the following requirements and limitations:

  * Your cluster must run GKE version 1.32.2-gke.1297000 or later.
  * Cluster nodes must use [Ubuntu](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images#ubuntu) node images. SCTP is not supported for Container-Optimized OS images.
  * To enable SCTP support, ensure that your Ubuntu-based container images and the underlying GKE node OS is loaded with the `sctp` kernel module.
  * The setup time for an SCTP association can take longer than the setup time for a TCP connection. Design your applications to handle potential delays while associations are established.
  * To learn more about what Cilium supports and doesn't support with SCTP, see the [Cilium documentation](https://docs.cilium.io/en/latest/configuration/sctp/#limitations).



## Deploy workloads with SCTP

**Best practice** : 

Test your deployment thoroughly in a non-production environment before you deploy workloads to production.

From GKE version 1.32.2-gke.1297000, SCTP is enabled by default in clusters that use GKE Dataplane V2 and Ubuntu node images. To deploy workloads with SCTP, complete the following steps:

  1. To create a cluster with GKE Dataplane V2 and Ubuntu images, run the following command:
         
         gcloud container clusters create CLUSTER_NAME \
             --location=CONTROL_PLANE_LOCATION \
             --cluster-version=CLUSTER_VERSION \
             **--enable-dataplane-v2 \
             --image-type=ubuntu_containerd**
         

Replace the following values:

     * `CLUSTER_NAME`: the name of your cluster.
     * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.
     * `CLUSTER_VERSION`: the GKE version, which must be 1.32.2-gke.1297000 or later.
  2. To containerize the application, ensure that your container image includes an application that is configured to use SCTP. You can use any application that supports SCTP, such as a custom application.

The following is an example of a `Dockerfile` to containerize the application, assuming you use Docker:
         
         FROM ubuntu:latest
         RUN apt-get update && apt-get install -y socat
         
         # Run a simple SCTP echo server.  This command uses socat to listen for
         # incoming SCTP connections on a specified port and echo back any received data.
         # The 'fork' option ensures that a new process is created for each connection.
         # Replace "PORT" below with the desired port number.
         CMD ["socat", "PIPE", "SCTP-LISTEN:PORT,fork"]
         

[Build and push the image](https://docs.cloud.google.com/kubernetes-engine/docs/learn/containers#containerize_the_application) to a container registry like Artifact Registry. For more information about how this file works, see [Dockerfile reference](https://docs.docker.com/reference/dockerfile/) in the Docker documentation.

  3. To create a Deployment and a Service, save the following manifest as `sctp-deployment.yaml`:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
          name: sctp-app
         spec:
          replicas: 1
          selector:
            matchLabels:
              app: sctp-app
          template:
            metadata:
              labels:
                app: sctp-app
            spec:
              containers:
              - name: sctp-container
                image: CONTAINER_IMAGE
                ports:
                - containerPort: PORT
                  protocol: SCTP
         ---
         apiVersion: v1
         kind: Service
         metadata:
           name: sctp-service
         spec:
           selector:
             app: sctp-app
           ports:
           - protocol: SCTP
             port: PORT
             targetPort: PORT
           type: ClusterIP
         

Replace the following:

     * `CONTAINER_IMAGE`: the container image you built in the preceding step.
     * `PORT`: the SCTP port and target port numbers of the application. The value for `port` and `targetPort` must be the same.
**Important:** The `port` and `targetPort` values must be the same because Cilium doesn't support rewriting ports for SCTP packets.
  4. To apply the Deployment and Service, run the following command:
         
         kubectl apply -f sctp-deployment.yaml
         

  5. To verify SCTP connectivity for the Service, create a Pod within the same cluster and run the following command:
         
         kubectl run sctp-client \
          --image=ubuntu:latest \
          --namespace=default \
          -it --rm \
          --command -- bash -c 'apt-get update && apt-get install -y socat && (echo "Hello, SCTP!"; sleep 1) | socat - SCTP:sctp-service:PORT'
         

The output is similar to the following:
         
         Preparing to unpack .../socat_1.8.0.0-4build3_amd64.deb ...
         Setting up socat (1.8.0.0-4build3) ...
         **Hello, SCTP!**
         




## Troubleshooting

If you experience issues with SCTP connectivity, follow this guidance to help determine the source of the issue:

  * Check Pod logs. To check the logs of your application for any errors, run the following command:
        
        kubectl logs POD_NAME
        

These logs can help you identify what caused the Pod to crash.

  * Check the status of the SCTP Service object:
        
        kubectl describe service SCTP_SERVICE_NAME
        

  * Check your network policies. Network policies can restrict SCTP traffic. Ensure that your network policies allow the necessary SCTP traffic for your applications.

  * Check the status of GKE Dataplane V2. To verify that GKE Dataplane V2 is enabled on your cluster, run the following command:
        
        kubectl -n kube-system get pods -l k8s-app=cilium -o wide
        

Verify that the output includes Pods with the prefix `anetd-`. anetd is the networking controller for GKE Dataplane V2.

  * To improve throughput, increase the `sysctl` parameters `net.core.wmem_default` and `net.core.rmem_default` to a larger value, for example, 4194304 (4 MB). For more information, see [Sysctl configuration options](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-system-config#sysctl-options).

  * You might face issues if you use Network Address Translation (NAT) with SCTP in GKE. For more information about what Cilium supports with SCTP, see the [Cilium documentation](https://docs.cilium.io/en/latest/configuration/sctp/).

  * SCTP packets are subject to the Maximum Transmission Unit (MTU) of the network. Ensure that your network's MTU is sufficient for your SCTP traffic.

  * The performance of SCTP can be affected by factors such as network latency, packet loss, and kernel tuning. Monitor the performance of your application's SCTP and adjust the settings as needed.




## What's next

  * Learn about SCTP support in the [Cilium documentation](https://docs.cilium.io/en/latest/configuration/sctp/).
  * Learn how to [enable GKE Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dataplane-v2) on your cluster.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
