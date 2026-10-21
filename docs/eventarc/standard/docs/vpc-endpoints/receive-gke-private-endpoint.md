---
url: https://docs.cloud.google.com/eventarc/standard/docs/vpc-endpoints/receive-gke-private-endpoint/
title: Receive Pub/Sub events at a private HTTP endpoint in a private GKE cluster \u00a0|\u00a0 Eventarc Standard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:26:15.232053+00:00
---

# Receive Pub/Sub events at a private HTTP endpoint in a private GKE cluster  |  Eventarc Standard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/standard/docs/vpc-endpoints/receive-gke-private-endpoint/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/standard/docs/overview)



Send feedback 

#  Receive Pub/Sub events at a private HTTP endpoint in a private GKE cluster Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This tutorial shows you how to create a private HTTP endpoint in a private Google Kubernetes Engine (GKE) cluster that receives Pub/Sub message events using Eventarc. To learn more about this event destination, see [Route events to an internal HTTP endpoint in a VPC network](https://docs.cloud.google.com/eventarc/standard/docs/vpc-endpoints/route-vpc-internal-endpoint-events).

Private GKE clusters are a type of Virtual Private Cloud (VPC)-native cluster where nodes only have [internal IP addresses](https://docs.cloud.google.com/vpc/docs/ip-addresses), which means that nodes and Pods are isolated from the internet by default. You can choose to have no client access, limited access, or unrestricted access to the control plane. You can't convert an existing, non-private cluster to a private cluster. For more information, see [About private clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/private-cluster-concept).

You can run the following commands using the Google Cloud CLI in either your terminal or Cloud Shell.

## Objectives

In this tutorial, you will:

  1. Create a proxy-only subnet in the default VPC network, and create a VPC firewall rule.
  2. Create a private GKE Autopilot cluster with no client access to the public endpoint.
  3. Create a Compute Engine virtual machine (VM) instance in a specified subnet of the VPC network.
  4. Establish an SSH connection to the VM instance and deploy an event receiver service on the VM instance.
  5. Deploy a Gateway in your cluster and an `HTTPRoute` manifest to configure the routing of traffic in Kubernetes to application backends.
  6. Create a network attachment that lets a producer VPC network initiate connections to a consumer VPC network.
  7. Create an Eventarc trigger that routes Pub/Sub events to the event receiver on your VM instance.
  8. Publish a message to a Pub/Sub topic to generate an event, and view the body of the event in the application Pod logs.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Compute Engine](https://docs.cloud.google.com/compute)
  * [Eventarc](https://docs.cloud.google.com/eventarc)
  * [Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine)
  * [Pub/Sub](https://docs.cloud.google.com/pubsub)
  * [VPC](https://docs.cloud.google.com/vpc)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Cloud Resource Manager, Compute Engine, Eventarc, GKE, and Pub/Sub APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable compute.googleapis.com container.googleapis.com cloudresourcemanager.googleapis.com eventarc.googleapis.com pubsub.googleapis.com

  8. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  9. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  10. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  11. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  12. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  13. Enable the Cloud Resource Manager, Compute Engine, Eventarc, GKE, and Pub/Sub APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable compute.googleapis.com container.googleapis.com cloudresourcemanager.googleapis.com eventarc.googleapis.com pubsub.googleapis.com

  14. Update Google Cloud CLI components: 
         
         gcloud components update

  15. Sign in using your account: 
         
         gcloud auth login

  16. If you are the project creator, you are granted the [basic Owner role](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`). By default, this Identity and Access Management (IAM) role includes the permissions necessary for full access to most Google Cloud resources and you can skip this step.

If you are not the project creator, required permissions must be granted on the project to the appropriate _principal_. For example, a principal can be a Google Account (for end users) or a service account (for applications and compute workloads). For more information, see the [Roles and permissions](https://docs.cloud.google.com/eventarc/docs/all-roles-permissions) page for your event destination.

#### Required permissions

To get the permissions that you need to complete this quickstart, ask your administrator to grant you the following IAM roles on your project: 

     * [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)
     * [Compute Security Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.securityAdmin) (`roles/compute.securityAdmin`)
     * [Eventarc Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.admin) (`roles/eventarc.admin`)
     * [Kubernetes Engine Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.admin) (`roles/container.admin`)
     * [Logs View Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewAccessor) (`roles/logging.viewAccessor`)
     * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`)
     * [Pub/Sub Publisher ](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.publisher) (`roles/pubsub.publisher`)
     * [Service Account Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`)
     * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
     * [Service Usage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) (`roles/serviceusage.serviceUsageAdmin`)

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  17. Make note of the [Compute Engine default service account](https://docs.cloud.google.com/iam/docs/service-account-types#default) as you will attach it to an Eventarc trigger to represent the identity of the trigger for testing purposes. This service account is automatically created after enabling or using a Google Cloud service that uses Compute Engine, and with the following email format:
         
         PROJECT_NUMBER-compute@developer.gserviceaccount.com

Replace `PROJECT_NUMBER` with your Google Cloud project number. You can find your project number on the [Welcome](https://console.cloud.google.com/welcome) page of the Google Cloud console or by running the following command:
         
         gcloud projects describe PROJECT_ID --format='value(projectNumber)'

For production environments, we strongly recommend [creating a new service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) and granting it one or more IAM roles that contain the [minimum permissions required](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts#limit-service-account-privileges) and follow the principle of [least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege).

**Note:**

The [ `iam.automaticIamGrantsForDefaultServiceAccounts` organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants) prevents the Editor role from being automatically granted to default service accounts. If you created your organization after May 3, 2024, this constraint is enforced by default. 

We strongly recommend that you enforce this constraint to disable the automatic role grant. If you disable the automatic role grant, you must decide which roles to grant to the default service accounts, and then [grant these roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) yourself. 

If the default service account already has the Editor role, we recommend that you replace the Editor role with less permissive roles.To safely modify the service account's roles, use [Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/simulate-iam-policies) to see the impact of the change, and then [grant and revoke the appropriate roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

  18. If you enabled the Cloud Pub/Sub service agent on or before April 8, 2021, to support authenticated Pub/Sub push requests, grant the [Service Account Token Creator role](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountTokenCreator) (`roles/iam.serviceAccountTokenCreator`) to the service agent. Otherwise, this role is granted by default: 
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-pubsub.iam.gserviceaccount.com \
             --role=roles/iam.serviceAccountTokenCreator




## Create a proxy-only subnet

Unless you create an organizational policy that prohibits it, new projects start with a [default network](https://docs.cloud.google.com/vpc/docs/vpc#default-network) (an auto mode VPC network) that has one subnetwork (subnet) in each region. Each VPC network consists of one or more IP address ranges called _subnets_. Subnets are regional resources, and have IP address ranges associated with them.

  1. Use the [`gcloud compute networks subnets create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create) command to create a proxy-only subnet in the default network.
         
         gcloud compute networks subnets create proxy-only-subnet \
             --purpose=REGIONAL_MANAGED_PROXY \
             --role=ACTIVE \
             --region=us-central1 \
             --network=default \
             --range=10.10.10.0/24
         

Note that a subnet with `purpose=REGIONAL_MANAGED_PROXY` is reserved for [Envoy-based load balancers](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets) and that the `range` must provide 64 or more IP addresses.

  2. Create a firewall rule that matches the proxy-only subnet's range and that allows traffic on TCP port 8080.
         
         gcloud compute firewall-rules create allow-proxy-connection \
             --allow tcp:8080 \
             --source-ranges 10.10.10.0/24 \
             --network=default
         




## Create a private GKE cluster

Use the [`gcloud container clusters create-auto` command](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto) to create a private GKE cluster in [Autopilot mode](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters#modes) that has private nodes, and that has no client access to the public endpoint.

The following example creates a private GKE cluster named `private-cluster` and also creates a subnet named `my-subnet`:
    
    
    gcloud container clusters create-auto private-cluster \
        --create-subnetwork name=my-subnet \
        --enable-master-authorized-networks \
        --enable-private-nodes \
        --enable-private-endpoint \
        --region=us-central1
    

Note the following:

  * `--enable-master-authorized-networks` specifies that access to the public endpoint is restricted to IP address ranges that you authorize.
  * `--enable-private-nodes` indicates that the cluster's nodes don't have external IP addresses.
  * `--enable-private-endpoint` indicates that the cluster is managed using the internal IP address of the control plane API endpoint.



It might take several minutes for the creation of the cluster to complete. Once the cluster is created, the output should indicate that the status of the cluster is `RUNNING`.

## Create a VM instance in a specified subnet

A Compute Engine VM instance is a virtual machine that is hosted on Google's infrastructure. The terms _Compute Engine instance_ , _VM instance_ , and _VM_ are synonymous and are used interchangeably. VM instances include GKE clusters, App Engine flexible environment instances, and other Google Cloud products built on Compute Engine VMs.

Use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) to create a Compute Engine VM instance in the subnet you created previously. Attach a service account and set the VM's access scope to `cloud-platform`.
    
    
    gcloud compute instances create my-vm \
        --service-account=PROJECT_NUMBER-compute@developer.gserviceaccount.com \
        --scopes=https://www.googleapis.com/auth/cloud-platform \
        --zone=us-central1-a \
        --subnet=my-subnet
    

For more information, see [Create and start a VM instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).

## Deploy an event receiver on the VM

Using a prebuilt image, `us-docker.pkg.dev/cloudrun/container/hello`, deploy a service on your VM that listens on port 80, and that receives and logs events.

  1. Establish an SSH connection to your VM instance by running the following command:
         
         gcloud compute ssh my-vm --project=PROJECT_ID --zone=us-central1-a
         

After a connection to the SSH server is established, run the remaining commands on your VM instance.

  2. If necessary, [install `kubectl`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl#install_kubectl) and any required [plugins](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl#install_plugin).

  3. From your VM instance, use the [`get-credentials`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/get-credentials) command to enable `kubectl` to work with the cluster you created.
         
         gcloud container clusters get-credentials private-cluster \
             --region=us-central1 \
             --internal-ip
         

  4. Use a Kubernetes command, [`kubectl create deployment`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#create), to deploy an application to the cluster.
         
         kubectl create deployment hello-app \
             --image=us-docker.pkg.dev/cloudrun/container/hello
         

This creates a Deployment named `hello-app`. The Deployment's [Pod](https://kubernetes.io/docs/concepts/workloads/pods) runs the `hello` container image.

  5. After deploying the application, you can expose your application to traffic by creating a [Kubernetes Service](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service#what-is-a-service). Run the following [`kubectl expose`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#expose) command:
         
         kubectl expose deployment hello-app \
             --type ClusterIP \
             --port 80 \
             --target-port 8080
         

You should see `service/hello-app exposed` in the output.

You can ignore any messages similar to the following:
         
         E0418 14:15:33.970933    1129 memcache.go:287] couldn't get resource list for metrics.k8s.io/v1beta1: the server is currently unable to handle the request
         




## Configure Kubernetes traffic routing

A Gateway resource represents a data plane that routes traffic in Kubernetes. A Gateway can represent many different kinds of load balancing and routing depending on the GatewayClass it is derived from. For more information, see [Deploying Gateways](https://cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways). An `HTTPRoute` manifest is deployed to create Routes and send traffic to application backends.

  1. Deploy a Gateway in your cluster.
         
         kubectl apply -f - <<EOF
         kind: Gateway
         apiVersion: gateway.networking.k8s.io/v1beta1
         metadata:
           name: internal-http
         spec:
           gatewayClassName: gke-l7-rilb
           listeners:
           - name: http
             protocol: HTTP
             port: 80
         EOF
         

Note the following:

     * `gatewayClassName: gke-l7-rilb` specifies the GatewayClass that this Gateway is derived from. `gke-l7-rilb` corresponds to the internal Application Load Balancer.
     * `port: 80` specifies that the Gateway exposes only port 80 for listening for HTTP traffic.
  2. Validate that the Gateway has deployed correctly. It might take a few minutes for it to deploy all of its resources.
         
         kubectl describe gateways.gateway.networking.k8s.io internal-http
         

The output is similar to the following:
         
         Name:         internal-http
         Namespace:    default
         ...
         API Version:  gateway.networking.k8s.io/v1beta1
         Kind:         Gateway
         ...
         Spec:
           Gateway Class Name:  gke-l7-rilb
           Listeners:
             Allowed Routes:
               Namespaces:
                 From:  Same
             Name:      http
             Port:      80
             Protocol:  HTTP
         Status:
           Addresses:
             Type:   IPAddress
             Value:  10.36.172.5
         ...
         Events:
           Type    Reason  Age                From                   Message
           ----    ------  ----               ----                   -------
           Normal  ADD     80s                sc-gateway-controller  default/internal-http
           Normal  UPDATE  20s (x3 over 80s)  sc-gateway-controller  default/internal-http
           Normal  SYNC    20s                sc-gateway-controller  SYNC on default/internal-http was a success
         

  3. Deploy an `HTTPRoute` manifest to route HTTP traffic to the `hello-app` service at port 80.
         
         kubectl apply -f - <<EOF
         kind: HTTPRoute
         apiVersion: gateway.networking.k8s.io/v1beta1
         metadata:
           name: hello-app-route
         spec:
           parentRefs:
           - kind: Gateway
             name: internal-http
           rules:
           - backendRefs:
             - name: hello-app
               port: 80
         EOF
         




## Create a network attachment

A network attachment is a resource that lets a producer VPC network initiate connections to a consumer VPC network through a [Private Service Connect interface](https://docs.cloud.google.com/vpc/docs/about-private-service-connect-interfaces).

To publish events, Eventarc uses the network attachment to establish a connection to the internal HTTP endpoint hosted in a VPC network.

**Note:** Eventarc reserves the subnet [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) IP range `240.0.0.0/20`. The subnet used for the network attachment shouldn't overlap with this range.

You can create a network attachment that automatically accepts connections from any Private Service Connect interface that refers to the network attachment. Create the network attachment in the same network and region containing the HTTP destination service.
    
    
    gcloud compute network-attachments create my-network-attachment \
        --region=us-central1 \
        --subnets=my-subnet\
        --connection-preference=ACCEPT_AUTOMATIC

For more information, see [About network attachments](https://docs.cloud.google.com/vpc/docs/about-network-attachments).

## Create an Eventarc trigger

Create an Eventarc trigger that creates a new Pub/Sub topic and routes events to the event receiver deployed on the VM when a message is published to the Pub/Sub topic.

  1. Retrieve the Gateway address.
         
         GATEWAY_ADDRESS=$(kubectl get gateways.gateway.networking.k8s.io internal-http -o=jsonpath="{.status.addresses[0].value}")
         

  2. Create a trigger.
         
         gcloud eventarc triggers create my-trigger \
             --location=us-central1 \
             --destination-http-endpoint-uri="http://$GATEWAY_ADDRESS:80/" \
             --network-attachment="projects/PROJECT_ID/regions/us-central1/networkAttachments/my-network-attachment" \
             --event-filters="type=google.cloud.pubsub.topic.v1.messagePublished" \
             --service-account=PROJECT_NUMBER-compute@developer.gserviceaccount.com
         

Replace `PROJECT_NUMBER` with your Google Cloud project number. You can find your project number on the [Welcome](https://console.cloud.google.com/welcome) page of the Google Cloud console or by running the following command:
         
         gcloud projects describe PROJECT_ID --format='value(projectNumber)'
         




For more information about configuring your trigger, see [Route events to an internal HTTP endpoint in a VPC network](https://docs.cloud.google.com/eventarc/standard/docs/vpc-endpoints/route-vpc-internal-endpoint-events#create-trigger).

**Note:** It might take several minutes to create your trigger, and then it can take up to two minutes for the trigger to be fully functional.

## Generate and view a Pub/Sub topic event

You can generate an event by publishing a message to a Pub/Sub topic.

  1. Find and set the Pub/Sub topic as an environment variable.
         
         export MY_TOPIC=$(gcloud eventarc triggers describe my-trigger \
             --location=us-central1 \
             --format='value(transport.pubsub.topic)')
         

  2. Publish a message to the Pub/Sub topic to generate an event.
         
         gcloud pubsub topics publish $MY_TOPIC --message "Hello World"
         

The Eventarc trigger routes the event to the internal HTTP endpoint in the private GKE cluster. 

  3. Check the application Pod logs and verify the event delivery.
         
         POD_NAME=$(kubectl get pod --selector app=hello-app --output=name)
         kubectl logs $POD_NAME
         

The body of the event should be similar to the following:
         
         2024/04/18 20:31:43 Hello from Cloud Run! The container started successfully and is listening for HTTP requests on $PORT
         {"severity":"INFO","eventType":"google.cloud.pubsub.topic.v1.messagePublished","message":"Received event of type google.cloud.pubsub.topic.v1.messagePublished.
         Event data: Hello World","event":{"specversion":"1.0","id":"10935738681111260","source":"//pubsub.googleapis.com/projects/my-project/topics/eventarc-us-central1-my-trigger-224","type":"google.cloud.pubsub.topic.v1.messagePublished","datacontenttype":"application/json","time":"2024-04-18T20:40:03Z","data":
         {"message":{"data":"SGVsbG8gV29ybGQ=","messageId":"10935738681111260","publishTime":"2024-04-18T20:40:03Z"}}}}
         




You have successfully deployed an event receiver service to an internal HTTP endpoint in a private GKE cluster, created an Eventarc trigger, generated an event from Pub/Sub, and confirmed that the event was routed as expected by the trigger to the target endpoint.

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

  1. Delete the Eventarc trigger: 
         
         gcloud eventarc triggers delete my-trigger --location=us-central1

  2. Exit the VM and then delete the VM instance: 
         
         gcloud compute instances delete my-vm --zone=us-central1-a

  3. Delete the network attachment: 
         
         gcloud compute network-attachments delete my-network-attachment --region=us-central1

  4. Delete the firewall rule: 
         
         gcloud compute firewall-rules delete allow-proxy-connection

  5. Delete the cluster: 
         
         gcloud container clusters delete private-cluster --region=us-central1
           

  6. Delete the subnet: 
         
           gcloud compute networks subnets delete proxy-only-subnet --region=us-central1




## What's next

  * [Receive Pub/Sub events at an internal HTTP endpoint in a VPC network](https://docs.cloud.google.com/eventarc/standard/docs/vpc-endpoints/receive-vpc-internal-endpoint)
  * [Manage Eventarc triggers](https://docs.cloud.google.com/eventarc/docs/managing-triggers)
  * [View all event providers and destinations](https://docs.cloud.google.com/eventarc/standard/docs/event-providers-targets)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
