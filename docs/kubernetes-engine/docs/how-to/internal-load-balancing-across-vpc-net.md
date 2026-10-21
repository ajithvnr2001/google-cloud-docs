---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing-across-vpc-net/
title: Create an internal load balancer across VPC networks \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:41:09.218441+00:00
---

# Create an internal load balancer across VPC networks  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing-across-vpc-net/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Create an internal load balancer across VPC networks Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page explains how to create an [internal passthrough Network Load Balancer](https://docs.cloud.google.com/compute/docs/load-balancing/internal) on Google Kubernetes Engine (GKE) across VPC networks.

Before reading this page, ensure that you're familiar with the following concepts:

  * [LoadBalancer Service](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer).
  * [LoadBalancer Service parameters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer-parameters).
  * [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect).



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



## Create an internal load balancer with Private Service Connect

As a service producer, you can use service attachments to make your services available to service consumers in other VPC networks using [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect). You can create, manage, and delete service attachments using a `ServiceAttachment` custom resource. The GKE Private Service Connect controller monitors your ServiceAttachment resource and automatically creates, updates, or deletes a corresponding ServiceAttachment resource in Compute Engine.

### Requirements and limitations

  * Limitations for [Private Service Connect](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#limitations) apply.
  * You can create a service attachment in GKE versions 1.21.4-gke.300 and later.
  * Your cluster must have the [`HttpLoadBalancing` add-on](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#httploadbalancing) enabled. New GKE clusters have the `HttpLoadBalancing` add-on enabled by default.
  * You cannot use the same subnet in multiple service attachment configurations.
  * You must create a GKE service that uses an internal passthrough Network Load Balancer.
  * The GKE Service must use only a single protocol. Mixed-protocol GKE Services are not supported.
  * You cannot specify a subnet in a different project (Shared VPC) for GKE versions earlier than 1.22.4-gke.100. For Shared VPC, ensure all [requirements for Shared VPC](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-shared-vpc#before_you_begin) are met.
  * After you create a service attachment, you can't update the internal load balancer. To change your load balancer configurations, you must delete and recreate the service attachment.



### Create a `ServiceAttachment`

  1. Create a subnet.

You must create a [new subnet](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer#add-subnet-psc) for each `ServiceAttachment`.
         
         gcloud compute networks subnets create SUBNET_NAME \
             --project PROJECT_ID \
             --network NETWORK_NAME \
             --region REGION \
             --range SUBNET_RANGE \
             --purpose PRIVATE_SERVICE_CONNECT
         

Replace the following:

     * `SUBNET_NAME`: the name of the new subnet. In GKE versions 1.22.4-gke.100 and later, you can specify a subnet in a different project by using the fully qualified resource URL for this field. You can get the fully qualified resource URL using the command [`gcloud compute networks subnets describe`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/describe).
     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `NETWORK_NAME`: the name of the VPC network for the subnet.
     * `REGION`: the region for the new subnet. You must use the same region as the service that you create.
     * `SUBNET_RANGE`: the IP address range to use for the subnet.
  2. Deploy a workload.

The following manifest describes a Deployment that runs a sample web application container image. Save the manifest as `my-deployment.yaml`:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: psc-ilb
         spec:
           replicas: 3
           selector:
             matchLabels:
               app: psc-ilb
           template:
             metadata:
               labels:
                 app: psc-ilb
             spec:
               containers:
               - name: whereami
                 image: us-docker.pkg.dev/google-samples/containers/gke/whereami:v1
                 ports:
                   - name: http
                     containerPort: 8080
                 readinessProbe:
                   httpGet:
                     path: /healthz
                     port: 8080
                     scheme: HTTP
                   initialDelaySeconds: 5
                   timeoutSeconds: 1
         

  3. Apply the manifest to your cluster:
         
         kubectl apply -f my-deployment.yaml
         

  4. Create a service. The following manifest describes a service that creates an internal passthrough Network Load Balancer on TCP port 8080. Save the manifest as `my-service.yaml`:
         
         apiVersion: v1
          kind: Service
          metadata:
            name: SERVICE_NAME
            annotations:
              networking.gke.io/load-balancer-type: "Internal"
          spec:
            type: LoadBalancer
            selector:
              app: psc-ilb
            ports:
            - port: 80
              targetPort: 8080
              protocol: TCP
         

Replace the following:

     * `SERVICE_NAME`: the name of the new service.
  5. Apply the manifest to your cluster:
         
         kubectl apply -f my-service.yaml
         

  6. Create `ServiceAttachment`.

The following manifest describes a `ServiceAttachment` that exposes the service that you created to service consumers. Save the manifest as `my-psc.yaml`:
         
         apiVersion: networking.gke.io/v1
         kind: ServiceAttachment
         metadata:
          name: SERVICE_ATTACHMENT_NAME
          namespace: default
         spec:
          connectionPreference: ACCEPT_AUTOMATIC
          natSubnets:
          - SUBNET_NAME
          proxyProtocol: false
          reconcileConnections: false  # set to true to enable connection reconciliation
          resourceRef:
            kind: Service
            name: SERVICE_NAME
         

**Note:** For GKE versions earlier than 1.23.3-gke.900, use `networking.gke.io/v1beta1` instead of `networking.gke.io/v1`.

Replace the following:

     * `SERVICE_ATTACHMENT_NAME`: the name of the new service attachment.
     * `SUBNET_NAME`: the name of the new subnet. In GKE versions 1.22.4-gke.100 and later, you can specify a subnet in a different project by using the fully qualified resource URL for this field. You can get the fully qualified resource URL using the command [`gcloud compute networks subnets describe`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/describe). For a Shared VPC configuration, use the following format: `projects/HOST_PROJECT_ID/regions/COMPUTE_REGION/subnetworks/SUBNET_NAME`.
**Note:** The `ServiceAttachment` resource will have error events until the GKE controller creates the internal passthrough Network Load Balancer that is defined by the service. After the internal passthrough Network Load Balancer is provisioned, the errors are no longer published.

For more information about the manifest fields, see the service attachment fields.

  7. Apply the manifest to your cluster:
         
         kubectl apply -f my-psc.yaml
         

  8. Verify that the Private Service Connect controller created the service attachment:
         
         gcloud compute service-attachments list
         

The output shows a service attachment with an automatically generated name:
         
         NAME        REGION       PRODUCER_FORWARDING_RULE          CONNECTION_PREFERENCE
         k8s1-sa-... REGION_NAME  a3fea439c870148bdba5e59c9ea9451a  ACCEPT_AUTOMATIC
         




### View a `ServiceAttachment`

You can view the details of a `ServiceAttachment` using the following command:
    
    
    kubectl describe serviceattachment SERVICE_ATTACHMENT_NAME
    

The output is similar to the following:
    
    
    Name:        <sa-name>
    Namespace:    default
    Labels:       <none>
    Annotations:  <none>
    API Version:  networking.gke.io/v1beta1
    Kind:         ServiceAttachment
    Metadata:
      ...
    Status:
      Forwarding Rule URL:      https://www.googleapis.com/compute/beta/projects/<project>/regions/<region>/forwardingRules/<fr-name>
      Last Modified Timestamp:  2021-07-08T01:32:39Z
      Service Attachment URL:   https://www.googleapis.com/compute/beta/projects/<projects>/regions/<region>/serviceAttachments/<gce-service-attachment-name>
    Events:                     <none>
    

### Consume a `ServiceAttachment`

To consume your service from another project, perform the following steps:

  1. Get the URL of the `ServiceAttachment`:
         
         kubectl get serviceattachment SERVICE_ATTACHMENT_NAME -o=jsonpath="{.status.serviceAttachmentURL}"
         

The output is similar to the following:
         
         serviceAttachmentURL: https://www.googleapis.com/compute/alpha/projects/<project>/region/<region>/serviceAttachments/k8s1-...my-sa
         

  2. [Create a Private Service Connect endpoint](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#create-endpoint) using the URL of the `ServiceAttachment`.

  3. Verify that you can connect to the Service that you deployed in the producer project by using a `curl` command from a VM in the consumer project:
         
         curl PSC_IP_ADDRESS
         

Replace `PSC_IP_ADDRESS` with the IP address of the forwarding rule in the consumer project.

The output is similar to the following:
         
         {
           "cluster_name":"cluster",
           "host_header":"10.128.15.200",
           "node_name":"gke-psc-default-pool-be9b6e0e-dvxg.c.gke_project.internal",
           "pod_name":"foo-7bf648dcfd-l5jf8",
           "pod_name_emoji":"👚",
           "project_id":"gke_project",
           "timestamp":"2021-06-29T21:32:03",
           "zone":"ZONE_NAME"
         }
         




### Update a `ServiceAttachment`

You can update a `ServiceAttachment` using the following steps:

**Note:** You cannot update the `resourceRef` field and you can only add subnets to the `natSubnets` field. You cannot remove subnets. If you need to update the `resourceRef` field or remove subnets from the `natSubnets` field, you must delete and then recreate the `ServiceAttachment`.

  1. Edit the `ServiceAttachment` manifest in `my-psc.yaml`:
         
         apiVersion: networking.gke.io/v1
         kind: ServiceAttachment
         metadata:
           name: my-sa
           namespace: default
         spec:
           connectionPreference: ACCEPT_AUTOMATIC
           natSubnets:
           - my-nat-subnet
           proxyProtocol: false
           resourceRef:
             kind: Service
             name: ilb-service
         

**Note:** For GKE versions earlier than 1.23.3-gke.900, use `networking.gke.io/v1beta1` instead of `networking.gke.io/v1`.
  2. Apply the manifest to your cluster:
         
         kubectl apply -f my-psc.yaml
         




### Delete a `ServiceAttachment`

You cannot delete an internal passthrough Network Load Balancer that is connected to a service attachment. You must delete the service attachment and GKE Service separately.

  1. Delete the service attachment:
         
         kubectl delete serviceattachment SERVICE_ATTACHMENT_NAME --wait=false
         

This command marks the service attachment for deletion, but the resource continues to exist. You can also wait for the deletion to finish by omitting the `--wait` flag.

  2. Delete the Service:
         
         kubectl delete svc SERVICE_NAME
         

  3. Delete the subnet:
         
         gcloud compute networks subnets delete SUBNET_NAME
         




## `ServiceAttachment` fields

The `ServiceAttachment` has the following fields:

  * `connectionPreference`: the connection preference that determines how customers connect to the service. You can either use automatic project approval using `ACCEPT_AUTOMATIC` or explicit project approval using `ACCEPT_MANUAL`. For more information, see [Publishing services using Private Service Connect](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer).
  * `natSubnets`: a list of subnetwork resource names to use for the service attachment.
  * `proxyProtocol`: when set to true, the consumer source IP and Private Service Connect connection ID are available in the requests. This field is optional and defaults to false if not provided.
  * `reconcileConnections` ([Preview](https://docs.cloud.google.com/products#product-launch-stages)): when set to true, changes to the service consumer accept or reject lists automatically terminate existing, unauthorized connections. When set to false, changes affect only new connections. This field is optional and defaults to false. This field is supported from GKE version 1.36.0-gke.2459000 and later.
  * `consumerAllowList`: the list of consumer projects that are allowed to connect to the `ServiceAttachment`. This field can only be used when `connectionPreference` is `ACCEPT_MANUAL`. For more information about this field, see [Publishing services using Private Service Connect](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer). 
    * `project`: the project ID or number for the consumer project.
    * `connectionLimit`: the connection limit for the consumer project. This field is optional.
    * `forceSendFields`: the field names to send to include in API requests. This field is optional.
    * `nullFields`: the field names to include in API requests with a null value. This field is optional.
  * `consumerRejectList`: the list of consumer project IDs or numbers that are not allowed to connect to the `ServiceAttachment`. This field can only be used when `connectionPreference` is `ACCEPT_MANUAL`. For more information about this field, see [Publishing services using Private Service Connect](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer).
  * `resourceRef`: a reference to the Kubernetes resource.

    * `kind`: the type of Kubernetes resource. You must use `Service`.
    * `name`: the name of the Kubernetes resource that must be in the same namespace as the internal passthrough Network Load Balancer.
**Note:** After a service attachment is connected to an internal passthrough Network Load Balancer, you cannot delete or update the internal passthrough Network Load Balancer. If you attempt to delete or update the internal passthrough Network Load Balancer, an error message appears. For more information, see Troubleshooting.



## Troubleshooting

You can view error messages using the following command:
    
    
    kubectl get events -n NAMESPACE
    

Replace `NAMESPACE` with the namespace of the internal passthrough Network Load Balancer.

### Error deleting internal passthrough Network Load Balancer

An error message similar to the following occurs if you try to delete an internal passthrough Network Load Balancer that is being used by a service attachment. You must delete the `ServiceAttachment` before you can delete the internal passthrough Network Load Balancer.
    
    
    Error syncing load balancer: failed to ensure load balancer: googleapi:
    Error 400: The forwarding_rule resource '<fwd-rule-URL>' is already being used
    by '<svc-attachment-URL>', resourceInUseByAnotherResource.
    

### Error enabling global access

You might encounter an error when you enable [global access](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer-parameters#global_access_internal_lb) for an internal passthrough Network Load Balancer that uses a Private Service Connect service attachment.

**Symptom:**

When you enable global access by updating your GKE Service manifest and setting the `networking.gke.io/internal-load-balancer-allow-global-access: "true"` annotation, the update fails when you apply the manifest. You see the following error message when you run the `kubectl get events` command:
    
    
    Error syncing load balancer: failed to ensure load balancer: googleapi: Error 400: The forwarding_rule resource '...' is already being used by '...', resourceInUseByAnotherResource
    

**Reason:**

This error occurs because the GKE control plane attempts to re-create the load balancer's forwarding rule to enable global access. However, because the forwarding rule is in use by a `ServiceAttachment`, the rule cannot be deleted and re-created, which results in the error.

**Workaround:**

To enable global access on the load balancer while minimizing downtime, you must update the GKE Service configuration _and_ manually update the forwarding rule:

  1. **Update the GKE Service manifest** : update your GKE Service manifest to include the `networking.gke.io/internal-load-balancer-allow-global-access: "true"` annotation.

  2. **Manually enable global access on the forwarding rule** : follow the steps in [Enable global access](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal#ilb-global-access) to update the load balancer's forwarding rule by using either the Google Cloud console, the Google Cloud CLI, or the Compute Engine API.




### Unsynced `ReconcileConnections` field

If you manually enabled the `ReconcileConnections` field on the Compute Engine `ServiceAttachment` resource but omitted the field from your Kubernetes manifest, the field defaults to `false`. The GKE controller then doesn't overwrite the value of the field.

**Symptom:**

The Kubernetes `ServiceAttachment` resource has the `networking.gke.io/unsynced-field: ReconcileConnections` annotation. When you run the `kubectl get events` command, you see a warning event similar to the following:
    
    
    Field "ReconcileConnections" is not specified in the ServiceAttachment CR but has a value in GCE. The controller will not overwrite this field until it is explicitly set in the CR.
    

**Workaround:**

To resolve this warning and sync the values, perform one of the following actions:

  * **Update the GKE ServiceAttachment resource** : update your GKE ServiceAttachment manifest to include `reconcileConnections: true` (or `false` if you want to disable it).
  * **Update the Compute Engine ServiceAttachment resource** : manually set the `reconcileConnections` field to `false`.



## What's next

  * [Read the GKE network overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview).
  * [Learn more about Compute Engine load balancers](https://docs.cloud.google.com/compute/docs/load-balancing).
  * [Learn how to create a VPC-native cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips).
  * [Learn about configuring authorized networks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks).
  * [Troubleshoot load balancing in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/load-balancing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
