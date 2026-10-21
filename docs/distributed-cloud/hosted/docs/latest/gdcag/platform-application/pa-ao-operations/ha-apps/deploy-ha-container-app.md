---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/ha-apps/deploy-ha-container-app/
title: Deploy a highly available container application \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:43:22.171145+00:00
---

# Deploy a highly available container application  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/ha-apps/deploy-ha-container-app/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Deploy a highly available container application Stay organized with collections  Save and categorize content based on your preferences. 

[ Shared ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-configs#shared-cluster)

This document describes how to deploy a highly available (HA) Kubernetes container application in Google Distributed Cloud (GDC) air-gapped. To ensure resilience, you must deploy your application across multiple zones and configure storage replication so the application and its data are recoverable in the case of unexpected downtime or local disaster.

This document is intended for application developers who are responsible for creating resilient container workloads.

For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Objectives

  * Create a Kubernetes cluster in two or more zones in your GDC universe.
  * Configure global load balancing.
  * Deploy container workloads to each zonal Kubernetes cluster.
  * Provision storage and attach it to your pods.
  * Configure storage replication, using either block storage or object storage.



## Before you begin

To prepare for the tasks in this document, you must obtain the necessary permissions and verify your environment.

### Request IAM roles and permissions

Contact your Organization IAM Admin to request the following roles:

  * **Namespace Admin** (`namespace-admin`): create and edit container workloads in a shared cluster.
  * **User Cluster Admin** (`user-cluster-admin`): create and edit shared clusters.
  * **User Cluster Developer** (`user-cluster-developer`): create and edit node pools in a shared cluster.
  * **Harbor Instance Admin** (`harbor-instance-admin`): create and edit Harbor instances, Harbor projects, and container images.
  * **Project Network Policy Admin** (`global-project-networkpolicy-admin`): create and edit project network policies across zones.
  * **Global Load Balancer Admin** (`global-load-balancer-admin`): create and edit global load balancers.
  * **Volume Replication Global Admin** (`app-volume-replication-admin-global`): administer the volume replication relationship for block storage resources.
  * **Bucket Project Admin** (`global-project-bucket-admin`): create and edit dual-zone storage buckets.



For more information, see [role descriptions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/role-descriptions).

### Prepare your environment

Confirm you have the following tools and configurations present in your air-gapped environment:

  * Install and configure the gdcloud CLI and set your zonal and global contexts. For more information, see [Access zones with your tools](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/access-zones).

  * [Install the kubectl CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/get-started/kubectl) and set appropriate kubeconfig files for the global API server, management API server, and Kubernetes cluster. For more information, see [Manually generate kubeconfig file](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#generate-kubeconfig-file).

  * Verify that your GDC universe has multiple zones available. For more information, see [List zones in a universe](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/access-zones#list-zones-in-universe).




## Create a Kubernetes cluster in multiple zones

To create a highly available container application, you must create a separate shared Kubernetes cluster in each zone of your GDC universe.

For more information about available cluster configuration options, see [Kubernetes cluster configurations](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-configs).

###  Console 

  1. In the navigation menu, select **Kubernetes Engine > Clusters**.

**Important:** Notice you cannot select a project in the scope picker while creating a Kubernetes cluster. This is because the cluster is organization-scoped. For more information, see the [resource hierarchy](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/resource-hierarchy#cluster).
  2. Click **Create Cluster**.

  3. In the **Name** field, specify a name for the cluster.

  4. Select the Kubernetes version for the cluster.

  5. Select the zone in which to create the cluster.

  6. Click **Attach Project** and select an existing project to attach to your cluster. Then click **Save**. You can attach or detach projects after creating the cluster from the **Project details** page. You must have a project attached to your cluster before deploying container workloads it.

  7. Click **Next**.

  8. Configure the network settings for your cluster. You can't change these network settings after you create the cluster. The default and only supported Internet Protocol for Kubernetes clusters is Internet Protocol version 4 (IPv4).

     1. Specify the Load Balancer IP address pool size, such as `20`.

     2. Select the Service CIDR (Classless Inter-Domain Routing) to use. Your deployed services, such as load balancers, are allocated IP addresses from this range.

**Important:** The range can be any RFC 1918 range that doesn't conflict with other IP address ranges in the cluster and node pool resources. For more information, see [RFC 1918](https://tools.ietf.org/html/rfc1918).
     3. Select the pod CIDR to use. The cluster allocates IP addresses from this range to your pods and VMs.

     4. Click **Next**.

  9. Review the details of the auto-generated default node pool for the cluster. Click _edit_ **Edit** to modify the default node pool.

**Important:** If you intend the cluster to run graphics processing unit (GPU) workloads, you must provision a GPU machine type in your cluster. For more information, see [Cluster node machine types](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-node-machines).
  10. To create additional node pools, select **Add node pool**. When editing the default node pool or adding a new node pool, you customize it with the following options:

     1. Assign a name for the node pool. You cannot modify the name after you create the node pool.
     2. Specify the number of worker nodes to create in the node pool.
     3. Select your machine class that best suits your workload requirements. View the list of the following settings:

        * Machine type
        * CPU
        * Memory
     4. Click **Save**.

     5. Click **Create** to create the cluster.

  11. Repeat these steps for each zone in your GDC universe. Make sure a Kubernetes cluster resides in every zone that you want for your HA strategy.




###  API 

To create a new Kubernetes cluster using the API directly, apply a custom resource to each GDC zone.

  1. Create a `Cluster` custom resource and deploy it to the Management API server for your zone:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER apply -f - <<EOF
         apiVersion: cluster.gdc.goog/v1
         kind: Cluster
         metadata:
           name: CLUSTER_NAME
           namespace: platform
         spec:
           clusterNetwork:
             podCIDRSize: POD_CIDR
             serviceCIDRSize: SERVICE_CIDR
           initialVersion:
             kubernetesVersion: KUBERNETES_VERSION
           nodePools:
           - machineTypeName: MACHINE_TYPE
             name: NODE_POOL_NAME
             nodeCount: NUMBER_OF_WORKER_NODES
             taints: TAINTS
             labels: LABELS
             acceleratorOptions:
               gpuPartitionScheme: GPU_PARTITION_SCHEME
           releaseChannel:
             channel: UNSPECIFIED
         EOF
         

Replace the following:

     * `MANAGEMENT_API_SERVER`: the kubeconfig path of the zonal Management API server. For more information, see [Switch to the zonal context](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/access-zones#switch-zonal-context).
     * `CLUSTER_NAME`: the name of the cluster. The cluster name must not end with `-system`. The `-system` suffix is reserved for clusters created by GDC.
     * `POD_CIDR`: the size of network ranges from which pod virtual IP addresses (VIP) are allocated. If unset, the default value `21` is used.
     * `SERVICE_CIDR`: the size of network ranges from which service VIPs are allocated. If unset, the default value `23` is used.
     * `KUBERNETES_VERSION`: the Kubernetes version of the cluster, such as `1.26.5-gke.2100`. To list the available Kubernetes versions to configure, see [List available Kubernetes versions for a cluster](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-user-cluster#available-kubernetes-versions).
     * `MACHINE_TYPE`: the machine type for the worker nodes of the node pool. View the [available machine types](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-node-machines#available-machine-types) for what is available to configure.
     * `NODE_POOL_NAME`: the name of the node pool.
     * `NUMBER_OF_WORKER_NODES`: the number of worker nodes to provision in the node pool.
     * `TAINTS`: the taints to apply to the nodes of this node pool. This is an optional field.
     * `LABELS`: the labels to apply to the nodes of this node pool. It contains a list of key-value pairs. This is an optional field.
     * `GPU_PARTITION_SCHEME`: the GPU partitioning scheme, if you're running GPU workloads, such as `mixed-2`. The GPU is not partitioned if this field is not set. For available Multi-Instance GPU (MIG) profiles, see [Supported MIG profiles](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-node-machines#mig-profiles).
**Note:** You cannot edit node configurations, such as GPU partitioning, after a cluster node pool is created.
  2. Repeat the previous step for each zone that you want hosting your container application for your HA strategy.




## Configure load balancers

To distribute traffic between your pods in different zones, create load balancers. You can configure both internal and external load balancers globally to ensure that client requests are routed to healthy zones.

### Create a global internal load balancer

Internal load balancers (ILB) expose services within the organization from an internal IP address pool assigned to the organization. An ILB service is never accessible from any endpoint outside of the organization.

Complete the following steps to create a global ILB for your container workloads.

###  gdcloud 

Create an ILB that targets pod workloads using the gdcloud CLI.

This ILB targets all of the workloads in the project matching the label defined in the `Backend` object. The `Backend` custom resource must be scoped to a zone.

To create an ILB using the gdcloud CLI, follow these steps:

  1. Create a zonal `Backend` resource in each zone where your pods are running to define the endpoint for the ILB:
         
         gdcloud compute backends create BACKEND_NAME \
             --labels=LABELS \
             --project=PROJECT \
             --cluster-name=CLUSTER_NAME \
             --zone=ZONE
         

Replace the following:

     * `BACKEND_NAME`: the chosen name for the backend resource, such as `my-backend`.
     * `LABELS`: the selector defining which endpoints between pods to use for this backend resource, such as `app=web`.
     * `PROJECT`: the name of your project.
     * `CLUSTER_NAME`: the Kubernetes cluster to which the scope of the defined selectors is limited to. If this field is not specified, all of the endpoints with the given label are selected. This field is optional.
     * `ZONE`: the zone to use for this invocation. To preset the zone flag for all commands that require it, run `gdcloud config set core/zone ZONE`. The zone flag is available only in multi-zone environments. This field is optional.

Repeat this step for each zone in your GDC universe.

  2. Create a global `BackendService` resource:
         
         gdcloud compute backend-services create BACKEND_SERVICE_NAME \
             --project=PROJECT \
             --target-ports=TARGET_PORTS \
             --global
         

Replace the following:

     * `BACKEND_SERVICE_NAME`: the name for the backend service.
     * `PROJECT`: the name of your project.
     * `TARGET_PORTS`: a comma-separated list of target ports that this backend service translates, where each target port specifies the protocol, the port on the forwarding rule, and the port on the backend instance. You can specify multiple target ports. This field must be in the format `protocol:port:targetport`, such as `TCP:80:8080`. This field is optional.
  3. Add the `BackendService` resource to the previously created `Backend` resource in each zone:
         
         gdcloud compute backend-services add-backend BACKEND_SERVICE_NAME \
             --backend-zone=ZONE \
             --backend=BACKEND_NAME \
             --project=PROJECT \
             --global
         

Replace the following:

     * `BACKEND_SERVICE_NAME`: the name of the global backend service.
     * `ZONE`: the zone of the backend.
     * `BACKEND_NAME`: the name of the zonal backend.
     * `PROJECT`: the name of your project.

Complete this step for each zonal backend you created previously.

  4. Create an internal `ForwardingRule` resource that defines the virtual IP address (VIP) the service is available at:
         
         gdcloud compute forwarding-rules create FORWARDING_RULE_INTERNAL_NAME \
             --backend-service=BACKEND_SERVICE_NAME \
             --cidr=CIDR \
             --ip-protocol-port=PROTOCOL_PORT \
             --load-balancing-scheme=INTERNAL \
             --project=PROJECT \
             --global
         

Replace the following:

     * `FORWARDING_RULE_INTERNAL_NAME`: the name for the forwarding rule.
     * `CIDR`: the CIDR to use for your forwarding rule. This field is optional. If not specified, an `IPv4/32` CIDR is automatically reserved from the global IP address pool. Specify the name of a `Subnet` resource in the same namespace as this forwarding rule. A `Subnet` resource represents the request and allocation information of a global subnet. For more information about `Subnet` resources, see [Manage subnets](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/manage-subnets).
     * `PROTOCOL_PORT`: the protocol and port to expose on the forwarding rule. This field must be in the format `ip-protocol=TCP:80`. The exposed port must be the same as what the actual application is exposing inside of the container.
  5. To validate the configured ILB, confirm the `Ready` condition on each of the created objects. Verify the traffic with a `curl` request to the VIP:

     1. To get the assigned VIP, describe the forwarding rule:
            
            gdcloud compute forwarding-rules describe FORWARDING_RULE_INTERNAL_NAME --global
            

     2. Verify the traffic with a `curl` request to the VIP at the port specified in the field in the forwarding rule:
            
            curl http://FORWARDING_RULE_VIP:PORT
            

Replace the following:

     * `FORWARDING_RULE_VIP`: the VIP of the forwarding rule.
     * `PORT`: the port number of the forwarding rule.



###  API 

Create an ILB that targets container workloads using the KRM API. This ILB targets all of the workloads in the project matching the label defined in the `Backend` object. To create a global ILB using the KRM API, follow these steps:

  1. Create a `Backend` resource to define the endpoints for the ILB. Create `Backend` resources for each zone the container workloads are placed in:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER apply -f - <<EOF
         apiVersion: networking.gdc.goog/v1
         kind: Backend
         metadata:
           namespace: PROJECT
           name: BACKEND_NAME
         spec:
           clusterName: CLUSTER_NAME
           endpointsLabels:
             matchLabels:
               app: APP_NAME
         EOF
         

Replace the following:

     * `MANAGEMENT_API_SERVER`: the kubeconfig path of the zonal Management API server's kubeconfig path. For more information, see [Switch to a zonal context](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/access-zones#switch-zonal-context).
     * `PROJECT`: the name of your project.
     * `BACKEND_NAME`: the name of the `Backend` resource.
     * `CLUSTER_NAME`: the Kubernetes cluster to which the scope of the defined selectors is limited to. If this field is not specified, all of the endpoints with the given label are selected. This field is optional.
     * `APP_NAME`: the name of your container application.

You can use the same `Backend` resource for each zone, or create `Backend` resources with different label sets for each zone.

  2. Create a `BackendService` object using the previously created `Backend` resource. Make sure to include the `HealthCheck` resource:
         
         kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
         apiVersion: networking.global.gdc.goog/v1
         kind: BackendService
         metadata:
           namespace: PROJECT
           name: BACKEND_SERVICE_NAME
         spec:
           backendRefs:
           - name: BACKEND_NAME
             zone: ZONE
           healthCheckName: HEALTH_CHECK_NAME
           targetPorts:
           - port: PORT
             protocol: PROTOCOL
             targetPort: TARGET_PORT
         EOF
         

Replace the following:

     * `GLOBAL_API_SERVER`: the kubeconfig path of the global API server's kubeconfig path.
     * `PROJECT`: the name of your project.
     * `BACKEND_SERVICE_NAME`: the chosen name for your `BackendService` resource.
     * `HEALTH_CHECK_NAME`: the name of your previously created `HealthCheck` resource.
     * `BACKEND_NAME`: the name of the zonal `Backend` resource.
     * `ZONE`: the zone in which the `Backend` resource resides. You can specify multiple backends in the `backendRefs` field. For example:
           
           - name: my-backend-1
             zone: us-east1-a
           - name: my-backend-2
             zone: us-east1-b
           

The `targetPorts` field is optional. This resource lists ports that this `BackendService` resource translates. If you are using this object, provide values for the following:

     * `PORT`: the port exposed by the service.

     * `PROTOCOL`: the Layer-4 protocol which traffic must match. Only TCP and UDP are supported.

     * `TARGET_PORT`: the port to which the value is translated to, such as `8080`. The value can't be repeated in a given object.

An example for `targetPorts` might look like the following:
           
           targetPorts:
             - port: 80
               protocol: TCP
               targetPort: 8080
           

  3. Create an internal `ForwardingRule` resource defining the virtual IP address (VIP) the service is available at.
         
         kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
         apiVersion: networking.global.gdc.goog/v1
         kind: ForwardingRuleInternal
         metadata:
           namespace: PROJECT
           name: FORWARDING_RULE_INTERNAL_NAME
         spec:
           cidrRef:
             name: CIDR_NAME
           ports:
           - port: PORT
             protocol: PROTOCOL
           backendServiceRef:
             name: BACKEND_SERVICE_NAME
         EOF
         

Replace the following:

     * `GLOBAL_API_SERVER`: the kubeconfig path of the global API server's kubeconfig path.
     * `PROJECT`: the name of your project.
     * `FORWARDING_RULE_INTERNAL_NAME`: the chosen name for your `ForwardingRuleInternal` resource.
     * `CIDR_NAME`: the name of the CIDR to use for your forwarding rule. This field is optional. If not specified, an `IPv4/32` CIDR is automatically reserved from the global IP address pool. Specify the name of a `Subnet` resource in the same namespace as this forwarding rule. A `Subnet` resource represents the request and allocation information of a global subnet. For more information about `Subnet` resources, see [Manage subnets](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/manage-subnets).
     * `PORT`: the port to expose on the forwarding rule. Use the `ports` field to specify an array of L4 ports for which packets are forwarded to the backends configured with this forwarding rule. At least one port must be specified. Use the `port` field to specify a port number. The exposed port must be the same as what the actual application is exposing inside of the container.
     * `PROTOCOL`: the protocol to use for the forwarding rule, such as `TCP`. An entry in the `ports` array must look like the following:
           
           ports:
           - port: 80
             protocol: TCP
           

  4. To validate the configured ILB, confirm the `Ready` condition on each of the created objects. Verify the traffic with a `curl` request to the VIP:

     1. Retrieve the VIP:
            
            kubectl get forwardingruleinternal -n PROJECT
            

The output looks like the following:
            
            NAME           BACKENDSERVICE                  CIDR              READY
            ilb-name       BACKEND_SERVICE_NAME            192.0.2.0/32      True
            

     2. Test the traffic with a `curl` request to the VIP at the port specified in the field in the forwarding rule:
            
            curl http://FORWARDING_RULE_VIP:PORT
            

Replace the following:

        * `FORWARDING_RULE_VIP`: the VIP of the forwarding rule.
        * `PORT`: the port number of the field in the forwarding rule.



### Create a global external load balancer

External load balancers (ELB) expose services to access from outside the organization from a pool's IP addresses assigned to the organization from the larger instance-external IP address pool.

Complete the following steps to create a global ELB for your container workloads.

###  gdcloud 

Use the gdcloud CLI to create a global ELB that targets all of the workloads in the project matching the label defined in the `Backend` object. The `Backend` custom resource must be scoped to a zone.

  1. For ELB services to function, you must configure and apply your own customized `ProjectNetworkPolicy` data transfer in policy to allow traffic to the workloads of this ELB service. Network policies control access to your workloads, not the load balancer itself. ELBs expose workloads to your customer network, requiring explicit network policies to allow external traffic to the workload port, such as `8080`.

Specify the external CIDR address to allow traffic to the workloads of this ELB:
         
         kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
         apiVersion: networking.global.gdc.goog/v1
         kind: ProjectNetworkPolicy
         metadata:
           namespace: PROJECT
           name: allow-inbound-traffic-from-external
         spec:
           policyType: Ingress
           subject:
             subjectType: UserWorkload
           ingress:
           - from:
             - ipBlock:
                 cidr: CIDR
             ports:
             - protocol: TCP
               port: PORT
         EOF
         

Replace the following:

     * `GLOBAL_API_SERVER`: the kubeconfig path of the global API server's kubeconfig path. If you have not yet generated a kubeconfig file for the global API server, see [Manually generate kubeconfig file](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#global-resources-kubeconfig) for details.
     * `PROJECT`: the name of your project.
     * `CIDR`: the external CIDR that the ELB needs to be accessed from. This policy is required as the external load balancer uses Direct Server Return (DSR), which preserves the source external IP address and bypasses the load balancer on the return path. For more information, see [Create a global ingress firewall rule for organization-external traffic](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/organization-external-traffic#global-org-external-ingress).
     * `PORT`: the backend port on the pods behind the load balancer. This value is found in the `.spec.ports[].targetPortfield` field of the manifest for the `Service` resource. This field is optional.

This configuration provides all of the resources inside of projects access to the specified CIDR range.

**Note:** The gdcloud CLI does not support a command for creating a global project network policy, so you must use the KRM API instead.
  2. Create a `Backend` resource in each zone to define the endpoint for the ELB:
         
         gdcloud compute backends create BACKEND_NAME \
           --labels=LABELS \
           --project=PROJECT \
           --cluster-name=CLUSTER_NAME \
           --zone=ZONE
         

Replace the following:

     * `BACKEND_NAME`: the name for the backend resource, such as `my-backend`.
     * `LABELS`: a selector defining which endpoints between pods to use for this backend resource, such as `app=web`.
     * `PROJECT`: the name of your project.
     * `CLUSTER_NAME`: the Kubernetes cluster to which the scope of the defined selectors is limited to. If this field is not specified, all of the endpoints with the given label are selected. This field is optional.
     * `ZONE`: the zone to use for this invocation. To preset the zone flag for all commands that require it, run `gdcloud config set core/zone ZONE`. The zone flag is available only in multi-zone environments. This field is optional.

You can use the same `Backend` resource for each zone, or create `Backend` resources with different label sets for each zone.

  3. Create a global `BackendService` resource:
         
         gdcloud compute backend-services create BACKEND_SERVICE_NAME \
           --project=PROJECT \
           --target-ports=TARGET_PORTS \
           --health-check=HEALTH_CHECK_NAME \
           --global
         

Replace the following:

     * `BACKEND_SERVICE_NAME`: the chosen name for this backend service.
     * `PROJECT`: the name of your project.
     * `TARGET_PORTS`: a comma-separated list of target ports that this backend service translates, where each target port specifies the protocol, the port on the forwarding rule, and the port on the backend instance. You can specify multiple target ports. This field must be in the format `protocol:port:targetport`, such as `TCP:80:8080`. This field is optional.
     * `HEALTH_CHECK_NAME`: the name of the health check resource. This field is optional.
  4. Add the global `BackendService` resource to the previously created zonal `Backend` resource:
         
         gdcloud compute backend-services add-backend BACKEND_SERVICE_NAME \
           --backend=BACKEND_NAME \
           --backend-zone=ZONE \
           --project=PROJECT \
           --global
         

Complete this step for each zonal backend you created previously.

  5. Create an external `ForwardingRule` resource that defines the VIP the service is available at:
         
         gdcloud compute forwarding-rules create FORWARDING_RULE_EXTERNAL_NAME \
           --backend-service=BACKEND_SERVICE_NAME \
           --cidr=CIDR \
           --ip-protocol-port=PROTOCOL_PORT \
           --load-balancing-scheme=EXTERNAL \
           --project=PROJECT \
           --global
         

Replace the following:

     * `FORWARDING_RULE_EXTERNAL_NAME`: the name for the forwarding rule.
     * `CIDR`: the CIDR to use for your forwarding rule. This field is optional. If not specified, an `IPv4/32` CIDR is automatically reserved from the global IP address pool. Specify the name of a `Subnet` resource in the same namespace as this forwarding rule. A `Subnet` resource represents the request and allocation information of a global subnet. For more information about `Subnet` resources, see [Manage subnets](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/manage-subnets).
     * `PROTOCOL_PORT`: the protocol and port to expose on the forwarding rule. This field must be in the format `ip-protocol=TCP:80`. The exposed port must be the same as what the actual application is exposing inside of the container.
     * `PROJECT`: the name of your project.
  6. To validate the configured ELB, confirm the `Ready` condition on each of the created objects. Verify the traffic with a `curl` request to the VIP:

     1. To get the assigned VIP, describe the forwarding rule:
            
            gdcloud compute forwarding-rules describe FORWARDING_RULE_EXTERNAL_NAME
            

     2. Verify the traffic with a `curl` request to the VIP at the port specified in the `PROTOCOL_PORT` field in the forwarding rule:
            
            curl http://FORWARDING_RULE_VIP:PORT
            

Replace the following:

        * `FORWARDING_RULE_VIP`: the VIP of the forwarding rule.
        * `PORT`: the port number from the `PROTOCOL_PORT` field in the forwarding rule.



### API

Create an ELB that targets pod workloads using the KRM API. This ELB targets all of the workloads in the project matching the label defined in the `Backend` object. To create a zonal ELB using the KRM API, follow these steps:

  1. For ELB services to function, you must configure and apply your own customized `ProjectNetworkPolicy` data transfer in policy to allow traffic to the workloads of this ELB service. Network policies control access to your workloads, not the load balancer itself. ELBs expose workloads to your customer network, requiring explicit network policies to allow external traffic to the workload port, such as `8080`.

Specify the external CIDR address to allow traffic to the workloads of this ELB:
         
         kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
         apiVersion: networking.global.gdc.goog/v1
         kind: ProjectNetworkPolicy
         metadata:
           namespace: PROJECT
           name: allow-inbound-traffic-from-external
         spec:
           policyType: Ingress
           subject:
             subjectType: UserWorkload
           ingress:
           - from:
             - ipBlock:
                 cidr: CIDR
             ports:
             - protocol: TCP
               port: PORT
         EOF
         

Replace the following:

     * `GLOBAL_API_SERVER`: the kubeconfig path of the global API server's kubeconfig path. If you have not yet generated a kubeconfig file for the global API server, see [Manually generate kubeconfig file](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#global-resources-kubeconfig) for details.
     * `PROJECT`: the name of your project.
     * `CIDR`: the external CIDR that the ELB needs to be accessed from. This policy is required as the external load balancer uses Direct Server Return (DSR), which preserves the source external IP address and bypasses the load balancer on the return path. For more information, see [Create a global ingress firewall rule for organization-external traffic](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/organization-external-traffic#global-org-external-ingress).
     * `PORT`: the backend port on the pods behind the load balancer. This value is found in the `.spec.ports[].targetPortfield` field of the manifest for the `Service` resource. This field is optional.
**Note:** This configuration provides all of the resources inside of projects access to the specified CIDR range.
  2. Create a `Backend` resource to define the endpoints for the ELB. Create `Backend` resources for each zone the workloads are placed in:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER apply -f - <<EOF
         apiVersion: networking.gdc.goog/v1
         kind: Backend
         metadata:
           namespace: PROJECT
           name: BACKEND_NAME
         spec:
           clusterName: CLUSTER_NAME
           endpointsLabels:
             matchLabels:
               app: APP_NAME
         EOF
         

Replace the following:

     * `MANAGEMENT_API_SERVER`: the kubeconfig path of the zonal Management API server's kubeconfig path. If you have not yet generated a kubeconfig file for the API server in your targeted zone, see [Manually generate kubeconfig file](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#generate-kubeconfig-file) for details.
     * `PROJECT`: the name of your project.
     * `BACKEND_NAME`: the name of the `Backend` resource.
     * `CLUSTER_NAME`: the Kubernetes cluster to which the scope of the defined selectors is limited to. If this field is not specified, all of the endpoints with the given label are selected. This field is optional.
     * `APP_NAME`: the name of your container application.

You can use the same `Backend` resource for each zone, or create `Backend` resources with different label sets for each zone.

  3. Create a `BackendService` object using the previously created `Backend` resource:
         
         kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
         apiVersion: networking.global.gdc.goog/v1
         kind: BackendService
         metadata:
           namespace: PROJECT
           name: BACKEND_SERVICE_NAME
         spec:
           backendRefs:
           - name: BACKEND_NAME
             zone: ZONE
           healthCheckName: HEALTH_CHECK_NAME
         EOF
         

Replace the following:

     * `BACKEND_SERVICE_NAME`: the chosen name for your `BackendService` resource.
     * `HEALTH_CHECK_NAME`: the name of your previously created `HealthCheck` resource. Don't include this field if you are configuring an ELB for pod workloads.
     * `ZONE`: the zone in which the `Backend` resource resides. You can specify multiple backends in `backendRefs` field. For example:
    
    - name: my-backend-1
      zone: us-east1-a
    - name: my-backend-2
      zone: us-east1-b
    

  4. Create an external `ForwardingRule` resource defining the VIP the service is available at.
         
         kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
         apiVersion: networking.global.gdc.goog/v1
         kind: ForwardingRuleExternal
         metadata:
           namespace: PROJECT
           name: FORWARDING_RULE_EXTERNAL_NAME
         spec:
           cidrRef:
             name: CIDR_NAME
           ports:
           - port: PORT
             protocol: PROTOCOL
           backendServiceRef:
             name: BACKEND_SERVICE_NAME
         EOF
         

Replace the following:

     * `FORWARDING_RULE_EXTERNAL_NAME`: the chosen name for your `ForwardingRuleExternal` resource.
     * `CIDR_NAME`: the name of the CIDR to use for your forwarding rule. This field is optional. If not specified, an `IPv4/32` CIDR is automatically reserved from the global IP address pool. Specify the name of a `Subnet` resource in the same namespace as this forwarding rule. A `Subnet` resource represents the request and allocation information of a global subnet. For more information about `Subnet` resources, see [Manage subnets](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/manage-subnets).
     * `PORT`: the port to expose on the forwarding rule. Use the `ports` field to specify an array of L4 ports for which packets are forwarded to the backends configured with this forwarding rule. At least one port must be specified. Use the `port` field to specify a port number. The exposed port must be the same as what the actual application is exposing inside of the container.
     * `PROTOCOL`: the protocol to use for the forwarding rule, such as `TCP`. An entry in the `ports` array must look like the following:
    
    ports:
    - port: 80
      protocol: TCP
    

  5. To validate the configured ELB, confirm the `Ready` condition on each of the created objects. Try and test the traffic with a `curl` request to the VIP.

     1. Retrieve the VIP for the project:
            
            kubectl get forwardingruleexternal -n PROJECT
            

The output looks like the following:
            
            NAME           BACKENDSERVICE                  CIDR              READY
            elb-name       BACKEND_SERVICE_NAME            192.0.2.0/32      True
            

     2. Verify the traffic with a curl request to the VIP at the port specified in the `PORT` field in the forwarding rule:
            
            curl http://FORWARDING_RULE_VIP:PORT
            

Replace `FORWARDING_RULE_VIP:PORT` with the VIP and port of the forwarding rule, such as `192.0.2.0:80`.




## Deploy container workloads to each zonal cluster

Container workloads are not a global resource, which means you must deploy each of your container applications separately into the zonal Kubernetes clusters.

  1. Sign in to the zone that hosts your Kubernetes cluster:
         
         gdcloud config set core/zone ZONE
         

  2. Verify that your container image is available from the managed Harbor registry. For more information, see the [Deploy a container app](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/deploy-container-workloads#create-managed-registry) tutorial.

  3. Create a manifest file for your container workload and deploy it to your zonal Kubernetes cluster:
         
         kubectl --kubeconfig KUBERNETES_CLUSTER -n PROJECT apply -f - <<EOF
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: DEPLOYMENT_NAME
         spec:
           replicas: NUMBER_OF_REPLICAS
           selector:
             matchLabels:
               run: APP_NAME
           template:
             metadata:
               labels:
                 run: APP_NAME
             spec:
               containers:
               - name: CONTAINER_NAME
                 image: HARBOR_INSTANCE_URL/HARBOR_PROJECT_NAME/IMAGE:TAG
         EOF
         

Replace the following:

     * `KUBERNETES_CLUSTER`: the kubeconfig file for the zonal Kubernetes cluster to which you are deploying container workloads. If you have not yet generated a kubeconfig file for your zonal Kubernetes cluster, see [Manually generate kubeconfig file](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#zonal-cluster-kubeconfig) for details.
     * `PROJECT`: the project namespace in which to deploy the container workloads.
     * `DEPLOYMENT_NAME`: the name of your container deployment.
     * `NUMBER_OF_REPLICAS`: the number of replicated `Pod` objects that the deployment manages.
     * `APP_NAME`: the name of the application to run within the deployment.
     * `CONTAINER_NAME`: the name of the container.
     * `HARBOR_INSTANCE_URL`: the URL of the Harbor instance, such as `harbor-1.org-1.zone1.google.gdc.test.` To retrieve the URL of the Harbor instance, see [View Harbor registry instances](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/manage-harbor-instances#view-harbor-registry-instances).
     * `HARBOR_PROJECT_NAME`: the name of the Harbor project, such as `my-project`.
     * `IMAGE`: the image's name, such as `nginx`.
     * `TAG`: the tag for the image version that you want to pull, such as `1.0`.
  4. Repeat the previous steps for each zone in your GDC universe. Make sure your container application resides in every zone that you want for your HA strategy.




## Expose your container application using Kubernetes

You must expose your container application to allow access to it from other resources in your GDC universe.

  1. Create a `Service` resource of `type: LoadBalancer`. This resource exposes your application's pods over a network.
         
         kubectl --kubeconfig KUBERNETES_CLUSTER -n PROJECT apply -f - <<EOF
         apiVersion: v1
         kind: Service
         metadata:
           name: SERVICE_NAME
         spec:
           selector:
             app: APP_NAME
           ports:
             - port: 80
               protocol: TCP
           type: LoadBalancer
         EOF
         

Replace the following:

     * `KUBERNETES_CLUSTER`: the kubeconfig file for the zonal Kubernetes cluster to which you are deploying container workloads.
     * `PROJECT`: the project namespace in which your container workloads reside.
     * `SERVICE_NAME`: the name of the load balancer service.
     * `APP_NAME`: the label you applied for your container application.
  2. Create a `NetworkPolicy` custom resource to allow all network traffic to the default namespace:
         
         kubectl --kubeconfig KUBERNETES_CLUSTER -n PROJECT apply -f - <<EOF
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
         




## Provision persistent storage for your pods

You must create a `PersistentVolumeClaim` resource (PVC) to supply application pods with persistent storage.

The following instructions show how to create a volume using the GDC `standard-rwo` `StorageClass`.

  1. Create a `PersistentVolumeClaim` resource. For example, configure it with a `ReadWriteOnce` access mode and a `standard-rwo` storage class:
         
         kubectl --kubeconfig KUBERNETES_CLUSTER -n PROJECT apply -f - <<EOF
         apiVersion: v1
         kind: PersistentVolumeClaim
         metadata:
           name: PVC_NAME
         spec:
           accessModes:
             - ReadWriteOnce
           resources:
             requests:
               storage: 10Gi
           storageClassName: standard-rwo
         EOF
         

Replace the following:

     * `KUBERNETES_CLUSTER`: the kubeconfig file for the Kubernetes cluster.
     * `PROJECT`: the project namespace in which to create the PVC.
     * `PVC_NAME`: the name of the `PersistentVolumeClaim` object.
  2. The `PersistentVolume` (PV) objects are dynamically provisioned. Check the status of the new PVs in your Kubernetes cluster:
         
         kubectl get pv --kubeconfig KUBERNETES_CLUSTER
         

The output is similar to the following:
         
         NAME       CAPACITY   ACCESS MODES   STATUS      CLAIM     STORAGECLASS   AGE
         pvc-uuidd  10Gi       RWO            Bound       pvc-name  standard-rwo   60s
         

  3. Configure your container workloads to use the PVC. The following is an example pod manifest that uses a `standard-rwo` PVC:
         
         kubectl --kubeconfig KUBERNETES_CLUSTER -n PROJECT apply -f - <<EOF
         apiVersion: apps/v1
         kind: Pod
         metadata:
           name: web-server-deployment
           labels:
             app: APP_LABEL
         spec:
           containers:
           - name: CONTAINER_NAME
             image: HARBOR_INSTANCE_URL/HARBOR_PROJECT_NAME/IMAGE:TAG
             volumeMounts:
             - mountPath: MOUNT_PATH
               name: data
           volumes:
           - name: data
             persistentVolumeClaim:
               claimName: PVC_NAME
         EOF
         

Replace the following:

     * `KUBERNETES_CLUSTER`: the kubeconfig file for the Kubernetes cluster to which you're deploying container workloads.
     * `PROJECT`: the project namespace in which the PVC resides.
     * `APP_LABEL`: the label you applied for your container application.
     * `CONTAINER_NAME`: the name of the container.
     * `HARBOR_INSTANCE_URL`: the URL of the Harbor instance, such as `harbor-1.org-1.zone1.google.gdc.test.` To retrieve the URL of the Harbor instance, see [View Harbor registry instances](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/manage-harbor-instances#view-harbor-registry-instances).
     * `HARBOR_PROJECT_NAME`: the name of the Harbor project, such as `my-project`.
     * `IMAGE`: the image's name, such as `nginx`.
     * `TAG`: the tag for the image version that you want to pull, such as `1.0`.
     * `MOUNT_PATH`: the path inside the pod to mount your volume.
     * `PVC_NAME`: the PVC you created.



## Configure storage replication

GDC multi-zone universes support storage replication for disaster recovery. This strategy provides data replication between any two zones in the same region, ensuring that your application data remains accessible even if a zone becomes unavailable.

Choose one of the following storage replication types for your container application:

  * Object replication
  * Asynchronous block replication



### Create a dual-zone bucket for object storage

Object storage data is written to a single bucket whose data is stored in both zones. Unlike volume replication, replicated buckets are writable during zone partitions. Each write to an object produces a different version, and the latest version across either zone will be the final state after connectivity is restored.

  1. Verify that your Infrastructure Operator (IO) has created the `BucketLocationConfig` custom resource, which is required for replication across zones for object storage. This resource must be deployed to the root global API server.

  2. Create the dual-zone `Bucket` custom resource:
         
         kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
         apiVersion: object.global.gdc.goog/v1
         kind: Bucket
         metadata:
           name: BUCKET_NAME
           namespace: PROJECT
         spec:
           location: LOCATION_NAME
           description: Sample DZ Bucket
           storageClass: Standard
         EOF
         

Replace the following:

     * `GLOBAL_API_SERVER`: the kubeconfig file for the global API server.
     * `BUCKET_NAME`: the name of the storage bucket.
     * `PROJECT`: the name of the project where the bucket resides.
     * `LOCATION_NAME`: the physical place where object data in the bucket resides. This must map to the name of an existing `BucketLocation` resource. To query the global API server of your organization for a list of available `BucketLocation` resources, run `kubectl --kubeconfig GLOBAL_API_SERVER bucketlocations`. If there are no `BucketLocation` resources, reach out to your IO to verify that they have enabled replication.



### Configure asynchronous block storage replication across zones

Replicated block storage provides asynchronously replicated volumes (PVs), which maintain block equivalence between the primary and secondary volumes. Due to the asynchronous nature, the secondary volume reflects the state of the primary zone at some point in the past (non-zero RPO). The secondary volume is not mountable while it remains the target of replication, requiring manual intervention to terminate the relationship and enable writes to occur.

You must configure a storage replication relationship across zones to create replicated data that is available for failover if the source zone data becomes unavailable. This is relevant if you are using block storage for your container application.

Before beginning, verify that your Infrastructure Operator (IO) has created and configured the `StorageClusterPeering` and `StorageVirtualMachinePeering` custom resources to allow for block storage replication across zones. This resource must be deployed to the root global API server.

  1. Create a `VolumeReplicationRelationship` custom resource YAML file and deploy it to the global API server:
         
         kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
         apiVersion: storage.global.gdc.goog/v1
         kind: VolumeReplicationRelationship
         metadata:
           name: PVC_REPL_NAME
           namespace: PROJECT
         spec:
           source:
             pvc:
               clusterRef: SOURCE_PVC_CLUSTER
               pvcRef: SOURCE_PVC
             zoneRef: SOURCE_ZONE
         destination:
             pvc:
               clusterRef: DEST_PVC_CLUSTER
             zoneRef: DEST_ZONE
         EOF
         

Replace the following:

     * `GLOBAL_API_SERVER`: the kubeconfig file for the global API server.
     * `PVC_REPL_NAME`: the name of the volume replication relationship.
     * `PROJECT`: the project where the storage infrastructure resides.
     * `SOURCE_PVC_CLUSTER`: the Kubernetes cluster where the PVC is hosted.
     * `SOURCE_PVC`: the PVC in the source zone to replicate.
     * `SOURCE_ZONE`: the source zone where the PVC is hosted.
     * `DEST_PVC_CLUSTER`: the destination Kubernetes cluster to replicate the PVC to.
     * `DEST_ZONE`: the destination zone to replicate the PVC to.
  2. Create a `VolumeFailover` custom resource in the destination zone, which stops replication to the destination zone if the source zone is unavailable for any reason:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER apply -f - <<EOF
         apiVersion: storage.gdc.goog/v1
         kind: VolumeFailover
         metadata:
           name: PVC_FAILOVER_NAME
           namespace: PROJECT
         spec:
           volumeReplicationRelationshipRef: PVC_REPL_NAME
         EOF
         

Replace the following:

     * `MANAGEMENT_API_SERVER`: the kubeconfig file of the zonal Management API server.
     * `PVC_FAILOVER_NAME`: the name of the PVC failover.
     * `PROJECT`: the project where the storage infrastructure resides.
     * `PVC_REPL_NAME`: the name of the volume replication relationship.



## What's next

  * [Kubernetes workloads for high availability](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/ha-apps/enhance-kubernetes-ha)
  * [Container workloads in GDC](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/containers/containers-intro)
  * [Multi-zone overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/mz-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
