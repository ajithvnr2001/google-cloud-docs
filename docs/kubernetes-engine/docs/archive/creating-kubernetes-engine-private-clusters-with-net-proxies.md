---
url: https://docs.cloud.google.com/kubernetes-engine/docs/archive/creating-kubernetes-engine-private-clusters-with-net-proxies/
title: Creating GKE private clusters with network proxies for controller access \u00a0|\u00a0 Kubernetes Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:24:15.439031+00:00
---

# Creating GKE private clusters with network proxies for controller access  |  Kubernetes Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/archive/creating-kubernetes-engine-private-clusters-with-net-proxies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Creating GKE private clusters with network proxies for controller access Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2019-07-02 UTC

Standard 

**Warning:** This page is **archived** and is not actively maintained. The commands on this page might not work and could cause disruptions to your cluster. We recommend that you create your cluster in version 1.29 and later for customizable and simplified access to the control plane and cluster network. To learn more see, [Customize your network isolation in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation).

When you create a [GKE private cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/private-clusters) with a private cluster controller endpoint, the cluster's controller node is inaccessible from the public internet, but it needs to be accessible for administration.

By default, clusters can access the controller through its private endpoint, and authorized networks can be defined within the VPC network.

To access the controller from on-premises or another VPC network, however, requires additional steps. This is because the VPC network that hosts the controller is owned by Google and cannot be accessed from resources connected through another VPC network peering connection, Cloud VPN or Cloud Interconnect.

To access the controller from on-premises or from another VPC network connected by Cloud VPN or Cloud Interconnect, [enable route export](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/private-clusters#master-on-prem-routing) from your VPC network to the Google-owned VPC network.

To enable access to the controller from another VPC network or from on-premises connected through another VPC network peering (such as in hub-and-spoke designs), create a proxy hosted in authorized IP address space, because VPC network peering is non-transitive.

This tutorial shows you how to configure a proxy within your GKE private cluster. 

## Objectives

  * Create a GKE private cluster with no external access.
  * Create and deploy a Docker image to run the proxy.
  * Create a Kubernetes Service to access the proxy.
  * Test access to the proxy.



## Costs

This tutorial uses billable components of Google Cloud Platform, including: 

  * [Compute Engine](https://cloud.google.com/compute/pricing)
  * [GKE](https://cloud.google.com/kubernetes-engine/pricing)



You can use the [pricing calculator](https://cloud.google.com/products/calculator) to generate a cost estimate based on your projected usage.

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

  4. Enable the Compute Engine and Google Kubernetes Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute_component,container,cloudresourcemanager.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Compute Engine and Google Kubernetes Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute_component,container,cloudresourcemanager.googleapis.com)




## Setting up your environment

In this tutorial, you use [Cloud Shell](https://docs.cloud.google.com/shell/docs/overview) to enter commands. Cloud Shell gives you access to the command line in the Google Cloud console, and includes the Google Cloud CLI and other tools that you need to develop in Google Cloud. Cloud Shell appears as a window at the bottom of the Google Cloud console. It can take several minutes to initialize, but the window appears immediately.

To use Cloud Shell to set up your environment:

  1. In the Google Cloud console, open Cloud Shell.

[OPEN Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. Make sure you are working in the project that you created or selected. Replace `[YOUR_PROJECT_ID]` with your Google Cloud project.
         
         gcloud config set project [YOUR_PROJECT_ID]
         export PROJECT_ID=`gcloud config list --format="value(core.project)"`
         

  3. Set the default compute zone. For the purposes of this tutorial, it is `us-central1-c`. If you are deploying to a production environment, deploy to [a region of your choice](https://cloud.google.com/about/locations/#products-available-by-location).
         
         gcloud config set compute/region us-central1
         gcloud config set compute/zone us-central1-c
         export REGION=us-central1
         export ZONE=us-central1-c
         
         




## Creating a VPC network and client VM

Create a VPC network and subnet that will host the resources.

  1. Create a VPC network:
         
         gcloud compute networks create k8s-proxy --subnet-mode=custom
         

  2. Create a custom subnet in the newly created VPC network:
         
         gcloud compute networks subnets create subnet-cluster \
             --network=k8s-proxy --range=10.50.0.0/16
         

  3. Create a client VM which you will use to deploy resources in the Kubernetes cluster:
         
         gcloud compute instances create --subnet=subnet-cluster \
             --scopes cloud-platform proxy-temp
         

  4. Save the internal IP address of the newly created instance in an environment variable:
         
         export CLIENT_IP=`gcloud compute instances describe proxy-temp \
             --format="value(networkInterfaces[0].networkIP)"`
         

  5. Create a firewall rule to allow SSH access to the VPC network:
         
         gcloud compute firewall-rules create k8s-proxy-ssh --network k8s-proxy \
             --allow tcp:22
         




## Creating a private cluster

Now create a private cluster to use for this tutorial.

If you already have a cluster that you prefer to use, you can skip the step for creating the cluster, but you must configure some initial form of access on your client machine.

  * In Cloud Shell, create a cluster:
        
        gcloud container clusters create frobnitz  \
            --master-ipv4-cidr=172.16.0.64/28 \
            --network k8s-proxy \
            --subnetwork=subnet-cluster \
            --enable-ip-alias \
            --enable-private-nodes \
            --enable-private-endpoint \
            --master-authorized-networks $CLIENT_IP/32 \
            --enable-master-authorized-networks
        

The command creates a GKE private cluster named `frobnitz` with `master-authorized-networks` set to allow only the client machine to have access.




## Creating the Docker image

Use the following steps to build a Kubernetes API proxy image called `k8s-api-proxy,` which acts as a forward proxy to the Kubernetes API server.

  1. In Cloud Shell, create a directory and change to that directory:
         
         mkdir k8s-api-proxy && cd k8s-api-proxy

  2. Create the `Dockerfile`. The following configuration creates a container from [Alpine](https://hub.docker.com/_/alpine/), which is a lightweight container distribution that has a Privoxy proxy. The `Dockerfile` also installs `curl` and `jq` for container initialization, adds the necessary configuration files, exposes port 8118 to GKE internally, and adds a startup script.
         
         FROM alpine  
         
         RUN apk add -U curl privoxy jq && \
             mv /etc/privoxy/templates /etc/privoxy-templates && \
             rm -rf /var/cache/apk/* /etc/privoxy/* && \
             mv /etc/privoxy-templates /etc/privoxy/templates
         ADD --chown=privoxy:privoxy config \
             /etc/privoxy/
         ADD --chown=privoxy:privoxy k8s-only.action \
             /etc/privoxy/
         ADD --chown=privoxy:privoxy k8s-rewrite-internal.filter \
             /etc/privoxy/
         ADD k8s-api-proxy.sh /  
         
         EXPOSE 8118/tcp  
         
         ENTRYPOINT ["./k8s-api-proxy.sh"]
         

  3. In the `k8s-api-proxy` directory, create the `config` file and add the following content to it:
         
         #config directory
         confdir /etc/privoxy
         # Allow Kubernetes API access only
         actionsfile /etc/privoxy/k8s-only.action
         # Rewrite https://CLUSTER_IP to https://kubernetes.default
         filterfile /etc/privoxy/k8s-rewrite-internal.filter
         # Don't show the pod name in errors
         hostname k8s-privoxy
         # Bind to all interfaces, port :8118
         listen-address  :8118
         # User cannot click-through a block
         enforce-blocks 1
         # Allow more than one outbound connection
         tolerate-pipelining 1
         

  4. In the same directory, create the `k8s-only.action` file and add the following content to it. Note that `CLUSTER_IP` will be replaced when `k8s-api-proxy.sh` runs.
         
         # Block everything...
         {+block{Not Kubernetes}}
         /  
         
         # ... except the internal k8s endpoint, which you rewrite (see
         # k8s-rewrite-internal.filter).
         {+client-header-filter{k8s-rewrite-internal} -block{Kubernetes}}
         CLUSTER_IP/
         

  5. Create the `k8s-rewrite-internal.filter` file and add the following content to it. Note that `CLUSTER_IP` will be replaced when `k8s-api-proxy.sh` runs.
         
         CLIENT-HEADER-FILTER: k8s-rewrite-internal\
          Rewrite https://CLUSTER_IP/ to https://kubernetes.default/
         s@(CONNECT) CLUSTER_IP:443\
          (HTTP/\d\.\d)@$1 kubernetes.default:443 $2@ig
         

  6. Create the `k8s-api-proxy.sh` file and add the following content to it.
         
         #!/bin/sh
         
         set -o errexit
         set -o pipefail
         set -o nounset
         
         # Get the internal cluster IP
         export TOKEN=$(cat /run/secrets/kubernetes.io/serviceaccount/token)
         INTERNAL_IP=$(curl -H "Authorization: Bearer $TOKEN" -k -SsL https://kubernetes.default/api |
         jq -r '.serverAddressByClientCIDRs[0].serverAddress')
         
         # Replace CLUSTER_IP in the rewrite filter and action file
         sed -i "s/CLUSTER_IP/${INTERNAL_IP}/g"\
          /etc/privoxy/k8s-rewrite-internal.filter
         sed -i "s/CLUSTER_IP/${INTERNAL_IP}/g"\
          /etc/privoxy/k8s-only.action
         
         # Start Privoxy un-daemonized
         privoxy --no-daemon /etc/privoxy/config
         

**Note:** For this tutorial, you don't install and verify the certificate of the Kubernetes API server. Instead, you run the `curl` command with the `-k` (insecure) option. In a production environment, you should properly install and verify TLS certificates. For more information, see [manage TLS certificates in Kubernetes clusters](https://kubernetes.io/docs/tasks/tls/managing-tls-in-a-cluster/).
  7. Make `k8s-api-proxy.sh` executable:
         
         chmod +x k8s-api-proxy.sh

  8. Build and push the container to your project.
         
         docker build -t gcr.io/$PROJECT_ID/k8s-api-proxy:0.1 .
         docker push gcr.io/$PROJECT_ID/k8s-api-proxy:0.1
         




## Deploying the image and Service

  1. In Cloud Shell, log in to the client VM you created earlier:
         
         gcloud compute ssh proxy-temp
         

  2. Install the `kubectl` tool:
         
         sudo apt-get install kubectl
         

  3. Save the project ID as an environment variable:
         
         export PROJECT_ID=`gcloud config list --format="value(core.project)"`
         

  4. Get the cluster credentials:
         
         gcloud container clusters get-credentials frobnitz \
         --zone us-central1-c --internal-ip
         

  5. Create a Kubernetes deployment that exposes the container that you just created:
         
         kubectl run k8s-api-proxy \
             --image=gcr.io/$PROJECT_ID/k8s-api-proxy:0.1 \
             --port=8118
         

  6. Create the `ilb.yaml` file for the internal load balancer and copy the following into it:
         
         apiVersion: v1
         kind: Service
         metadata:
           labels:
             run: k8s-api-proxy
           name: k8s-api-proxy
           namespace: default
           annotations:
             cloud.google.com/load-balancer-type: "Internal"
         spec:
           ports:
           - port: 8118
             protocol: TCP
             targetPort: 8118
           selector:
             run: k8s-api-proxy
           type: LoadBalancer
         

  7. Deploy the internal load balancer:
         
         kubectl create -f ilb.yaml

  8. Check for the Service and wait for an IP address:
         
         kubectl get service/k8s-api-proxy

The output will look like the following. When you see an external IP, the proxy is ready.
         
         NAME            TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
         k8s-api-proxy   LoadBalancer   10.24.13.129   10.24.24.3    8118:30282/TCP   2m
         

The external IP address from this step is your proxy address.

  9. Save the IP address of the ILB as an environment variable:
         
         export LB_IP=`kubectl get  service/k8s-api-proxy \
         -o jsonpath='{.status.loadBalancer.ingress[].ip}'`
         

  10. Save the cluster's controller IP address in an environment variable:
         
         export CONTROLLER_IP=`gcloud container clusters describe frobnitz \
         --zone=us-central1-c \
         --format="get(privateClusterConfig.privateEndpoint)"`
         

  11. Verify that the proxy is usable by accessing the Kubernetes API through it:
         
         curl -k -x $LB_IP:8118 https://$CONTROLLER_IP/version
         

The output will look like the following (your output might be different): 
         
         {
           "major": "1",
           "minor": "15+",
           "gitVersion": "v1.15.11-gke.5",
           "gitCommit": "a5bf731ea129336a3cf32c3375317b3a626919d7",
           "gitTreeState": "clean",
           "buildDate": "2020-03-31T02:49:49Z",
           "goVersion": "go1.12.17b4",
           "compiler": "gc",
           "platform": "linux/amd64"
         }
         

**Note:** For this tutorial, you don't protect the proxy with a valid certificate. Instead, you run the `curl` command with the `-k` (insecure) flag. In a production environment, you should properly install and verify a TLS certificate for the proxy. You can get it signed by the cluster root Certificate Authority (CA). For more information, see [manage TLS certificates in Kubernetes clusters](https://kubernetes.io/docs/tasks/tls/managing-tls-in-a-cluster/)
  12. Set the `https_proxy` environment variable to the HTTP(S) proxy so that the `kubectl` command can reach the internal load balancer from anywhere:
         
         export https_proxy=$LB_IP:8118

**Note:** After you've set the `https_proxy` environment variable, all traffic uses the proxy you set up earlier. However, the proxy allows traffic only to the Kubernetes API server and blocks all traffic to other destinations. This means internet traffic and traffic to Google properties, including traffic that originates from the `gcloud` command. Therefore, set the `https_proxy` variable only when access to the Kubernetes API server is required. You can reverse the effect of this command by running `unset https_proxy`.
  13. Test your proxy and `https_proxy` variable by running the `kubectl` command:
         
         kubectl get pods

You will get an output that looks like the following, which means that you successfully connected to the Kubernetes API through the proxy:
         
         NAME                             READY   STATUS    RESTARTS   AGE
         k8s-api-proxy-766c69dd45-mfqf4   1/1     Running   0          6m15s
         

  14. Exit the client VM:
         
         exit




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 
  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete the GKE cluster

If you don't want to delete the project, delete the GKE cluster:
    
    
    gcloud container clusters delete frobnitz

## What's next

  * [Hardening Your Cluster's Security](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster) to further secure your cluster
  * [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access) to access Google services without a public IP



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2019-07-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2019-07-02 UTC."],[],[]] 
