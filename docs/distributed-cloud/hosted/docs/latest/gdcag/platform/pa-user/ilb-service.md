---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/ilb-service/
title: Configure internal load balancers \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:29:51.604516+00:00
---

# Configure internal load balancers  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/ilb-service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Configure internal load balancers Stay organized with collections  Save and categorize content based on your preferences. 

Internal load balancers (ILB) expose services within the organization from an internal IP pool assigned to the organization. An ILB service is never accessible from any endpoint outside of the organization.

By default, you can access ILB services within the same project from any cluster in the organization. The default [project network policy](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/pnp-overview) doesn't let you access any project resources from outside the project, and this restriction applies to ILB services as well. If the Platform Administrator (PA) configures project network policies that allow access to your project from other projects, then the ILB service is also accessible from those other projects in the same organization.

## Before you begin

To configure ILBs, you must:

  * Own the project you are configuring the load balancer for. For more information, see [Create a project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-a-project).
  * Have the necessary identity and access roles:

    * Ask your IAM Org Admin to grant you the Load Balancer Admin (`load-balancer-admin`) role.
    * For global ILBs, ask your IAM Org Admin to grant you the Global Load Balancer Admin (`global-load-balancer-admin`) role. For more information, see [Predefined role descriptions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/role-descriptions).
  * Know the type of cluster hosting your workloads. There are distinct instructions for setting up ILBs for shared and standard clusters.




## Create an internal load balancer for shared clusters

You can create global or zonal ILBs for shared clusters. The scope of global ILBs span across a GDC universe. The scope of zonal ILBs is limited to the zone specified at the time of creation. For more information, see [Global and zonal load balancers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/expose-services#global-and-zonal-load-balancers).

Create ILBs using three different methods in GDC:

  * Use the [gdcloud CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-overview) to create global or zonal ILBs.
  * Use the [Networking Kubernetes Resource Model (KRM) API](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/networking/networking-api-overview) to create global or zonal ILBs.
  * Use the Kubernetes Service directly in the Kubernetes cluster. This method is only available for zonal ILBs.



You can target pod or VM workloads using the KRM API and gdcloud CLI. You can only target workloads in the cluster where the `Service` object is created when you use the Kubernetes Service directly from the Kubernetes cluster.

### Create a zonal ILB

Create a zonal ILB using the gdcloud CLI, the KRM API, or the Kubernetes Service in the Kubernetes cluster:

###  gdcloud 

Create an ILB that targets pod or VM workloads using the gdcloud CLI.

This ILB targets all of the workloads in the project matching the label defined in the `Backend` object.

To create an ILB using the gdcloud CLI, follow these steps:

  1. Create a `Backend` resource to define the endpoint for the ILB:
         
         gdcloud compute backends create BACKEND_NAME \
           --labels=LABELS \
           --project=PROJECT_NAME \
           --zone=ZONE \
           --cluster-name=CLUSTER_NAME
         

Replace the following:

     * `BACKEND_NAME`: your chosen name for the backend resource, such as `my-backend`.
     * `LABELS`: A selector defining which endpoints between pods and VMs to use for this backend resource. For example, `app=web`.
     * `PROJECT_NAME`: the name of your project.
     * `ZONE`: the zone to use for this invocation. To preset the zone flag for all commands that require it, run: `gdcloud config set core/zone ZONE`. The zone flag is available only in multi-zone environments. This field is optional.
     * `CLUSTER_NAME`: the cluster to that the scope of the defined selectors is limited to. If this field is not specified, all of the endpoints with the given label are selected. This field is optional.
  2. Skip this step if this ILB is for pod workloads. If you are configuring an ILB for VM workloads, define the type of [health check](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/health-checks) for the ILB. For example, to create a TCP Health Check, define it as follows:
         
         gdcloud compute health-checks create tcp HEALTH_CHECK_NAME \
           --check-interval=CHECK_INTERVAL \
           --healthy-threshold=HEALTHY_THRESHOLD \
           --timeout=TIMEOUT \
           --unhealthy-threshold=UNHEALTHY_THRESHOLD \
           --port=PORT \
           --zone=ZONE
         

Replace the following:

     * `HEALTH_CHECK_NAME`: your chosen name for the health check resource, such as `my-health-check`.
     * `CHECK_INTERVAL`: the amount of time in seconds from the start of one probe to the start of the next one. Defaults to `5` when omitted or set to 0. It is discouraged to set timeout longer than checkInterval.
     * `HEALTHY_THRESHOLD`: the number of sequential probes that must pass for the endpoint to be considered healthy. Defaults to `5` when omitted or set to 0.
     * `TIMEOUT`: the amount of time in seconds to wait before claiming failure. Defaults to `5` when omitted or set to 0. It is discouraged to set timeout longer than checkInterval.
     * `UNHEALTHY_THRESHOLD`: the number of sequential probes that must fail for the endpoint to be considered unhealthy. Defaults to `2` when omitted or set to 0.
     * `PORT`: the port on which the health check is performed. The default value is `80`. This field is optional.
     * `ZONE`: the zone you are creating this ILB in.
  3. Create a `BackendService` resource and add to it the previously created `Backend` resource:
         
         gdcloud compute backend-services create BACKEND_SERVICE_NAME \
           --project=PROJECT_NAME \
           --target-ports=TARGET_PORTS \
           --zone=ZONE \
           --health-check=HEALTH_CHECK_NAME
         

Replace the following:

     * `BACKEND_SERVICE_NAME`: the chosen name for this backend service.
     * `TARGET_PORTS`: a comma-separated list of target ports that this backend service translates, where each target port specifies the protocol, the port on the forwarding rule, and the port on the backend instance. You can specify multiple target ports. This field must be in the format `protocol:port:targetport`, such as `TCP:80:8080`. This field is optional.
     * `HEALTH_CHECK_NAME`: the name of the health check resource. This field is optional. Only include this field if you are configuring an ILB for VM workloads.
  4. Add the `BackendService` resource to the previously created `Backend` resource:
         
         gdcloud compute backend-services add-backend BACKEND_SERVICE_NAME \
           --backend=BACKEND_NAME \
           --project=PROJECT_NAME \
           --zone=ZONE
         

  5. Create an internal `ForwardingRule` resource that defines the VIP the service is available at:
         
         gdcloud compute forwarding-rules create FORWARDING_RULE_INTERNAL_NAME \
           --backend-service=BACKEND_SERVICE_NAME \
           --cidr=CIDR \
           --ip-protocol-port=PROTOCOL_PORT \
           --load-balancing-scheme=INTERNAL \
           --zone=ZONE \
           --project=PROJECT_NAME
         

Replace the following:

     * `BACKEND_SERVICE_NAME`: the name of your backend service.
     * `FORWARDING_RULE_INTERNAL_NAME` with your chosen name for the forwarding rule.
     * `CIDR`: this field is optional. If not specified, an `IPv4/32` CIDR is automatically reserved from the zonal IP pool. Specify the name of a `Subnet` resource in the same namespace as this forwarding rule. A `Subnet` resource represents the request and allocation information of a zonal subnet. For more information on `Subnet` resources, see [Example custom resources](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/ipam/overview#example-resource).
     * `PROTOCOL_PORT`: the protocol and port to expose on the forwarding rule. This field must be in the format `ip-protocol=TCP:80`. The exposed port must be the same as what the actual application is exposing inside the container.
  6. To validate the configured ILB, confirm the `Ready` condition on each of the created objects. Verify the traffic with a `curl` request to the VIP:

     1. To get the assigned VIP, describe the forwarding rule:
            
            gdcloud compute forwarding-rules describe FORWARDING_RULE_INTERNAL_NAME
            

     2. Verify the traffic with a `curl` request to the VIP at the port specified in the `PROTOCOL_PORT` field in the forwarding rule:
            
            curl http://FORWARDING_RULE_VIP:PORT
            

Replace the following:

        * `FORWARDING_RULE_VIP`: the VIP of the forwarding rule.
        * `PORT`: the port number from of the `PROTOCOL_PORT` field in the forwarding rule.



### API

Create an ILB that targets pod or VM workloads using the KRM API. This ILB targets all of the workloads in the project matching the label defined in the `Backend` object.

To create a zonal ILB using the KRM API, follow these steps:

  1. Create a `Backend` resource to define the endpoints for the ILB. Create `Backend` resources for each zone the workloads are placed in:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER apply -f - <<EOF
         apiVersion: networking.gdc.goog/v1
         kind: Backend
         metadata:
           namespace: PROJECT_NAME
           name: BACKEND_NAME
         spec:
           clusterName: CLUSTER_NAME
           endpointsLabels:
             matchLabels:
               app: server
         EOF
         

Replace the following:

     * `MANAGEMENT_API_SERVER`: the kubeconfig path of the zonal Management API server's kubeconfig path. For more information, see [Switch to a zonal context](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/access-zones#switch-zonal-context).
     * `PROJECT_NAME`: the name of your project.
     * `BACKEND_NAME`: the name of the `Backend` resource.
     * `CLUSTER_NAME`: This is an optional field. This field specifies the cluster to which the scope of the defined selectors are limited to. This field does not apply to VM workloads. If a `Backend` resource doesn't have the `clusterName` field included, the specified labels apply to all of the workloads in the project.

You can use the same `Backend` resource for each zone, or create `Backend` resources with different label sets for each zone.

  2. Skip this step if this ILB is for pod workloads. If you are configuring an ILB for VM workloads, define a health check for the ILB:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER apply -f - <<EOF
         apiVersion: networking.gdc.goog/v1
         kind: HealthCheck
         metadata:
           namespace: PROJECT_NAME
           name: HEALTH_CHECK_NAME
         spec:
           tcpHealthCheck:
             port: PORT
           timeoutSec: TIMEOUT
           checkIntervalSec: CHECK_INTERVAL
           healthyThreshold: HEALTHY_THRESHOLD
           unhealthyThreshold: UNHEALTHY_THRESHOLD
         EOF
         

Replace the following:

     * `HEALTH_CHECK_NAME`: your chosen name for the health check resource, such as `my-health-check`.
     * `PORT`: the port on which the health check is performed. The default value is to `80`.
     * `TIMEOUT`: the amount of time in seconds to wait before claiming failure. Defaults to `5` when omitted or set to 0. It is discouraged to set timeout longer than checkInterval.
     * `CHECK_INTERVAL`: the amount of time in seconds from the start of one probe to the start of the next one. Defaults to `5` when omitted or set to 0. It is discouraged to set timeout longer than checkInterval.
     * `HEALTHY_THRESHOLD`: the number of sequential probes that must pass for the endpoint to be considered healthy. Defaults to `2` when omitted or set to 0.
     * `UNHEALTHY_THRESHOLD`: the number of sequential probes that must fail for the endpoint to be considered unhealthy. Defaults to `2` when omitted or set to 0.
  3. Create a `BackendService` object using the previously created `Backend` resource. If you are configuring an ILB for VM workloads, include the `HealthCheck` resource.
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER apply -f - <<EOF
         apiVersion: networking.gdc.goog/v1
         kind: BackendService
         metadata:
           namespace: PROJECT_NAME
           name: BACKEND_SERVICE_NAME
         spec:
           backendRefs:
           - name: BACKEND_NAME
           healthCheckName: HEALTH_CHECK_NAME
         EOF
         

Replace the following:

     * `BACKEND_SERVICE_NAME`: the chosen name for your `BackendService` resource.
     * `HEALTH_CHECK_NAME`: the name of your previously created `HealthCheck` resource. Don't include this field if you are configuring an ILB for pod workloads.
  4. Create an internal `ForwardingRule` resource defining the VIP the service is available at.
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER apply -f - <<EOF
         apiVersion: networking.gdc.goog/v1
         kind: ForwardingRuleInternal
         metadata:
           namespace: PROJECT_NAME
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

     * `FORWARDING_RULE_INTERNAL_NAME`: the chosen name for your `ForwardingRuleInternal` resource.
     * `CIDR_NAME`: the `cidrRef` field is optional. If not specified, an `IPv4/32` CIDR is automatically reserved from the zonal IP pool. Specify the name of a `Subnet` resource in the same namespace as this forwarding rule. A `Subnet` resource represents the request and allocation information of a zonal subnet. For more information on `Subnet` resources, see [Example custom resources](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/ipam/overview#example-resource).
     * `PORT`: Use the `ports` field to specify an array of L4 ports for which packets are forwarded to the backends configured with this forwarding rule. At least one port must be specified. Use the `port` field to specify a port number. The exposed port must be the same as what the actual application is exposing inside of the container.
     * `PROTOCOL`: the protocol to use for the forwarding rule, such as `TCP`. An entry in the `ports` array must look like the following:
           
           ports:
           - port: 80
             protocol: TCP
           

  5. To validate the configured ILB, confirm the `Ready` condition on each of the created objects. Verify the traffic with a `curl` request to the VIP:

     1. To get the VIP, use `kubectl get`:
            
            kubectl get forwardingruleinternal -n PROJECT_NAME
            

The output looks like the following:
            
            NAME           BACKENDSERVICE                               CIDR              READY
            ilb-name       BACKEND_SERVICE_NAME        10.200.32.59/32   True
            

     2. Verify the traffic with a `curl` request to the VIP at the port specified in the `PORT` field in the forwarding rule:
            
            curl http://FORWARDING_RULE_VIP:PORT
            

Replace `FORWARDING_RULE_VIP` with the VIP of the forwarding rule.




### Kubernetes Service

You can create ILBs in GDC by creating a Kubernetes `Service` object of type `LoadBalancer` in a Kubernetes cluster. This ILB only targets workloads in the cluster where the `Service` object is created.

To create an ILB with the `Service` object, follow these steps:

  1. Create a YAML file for the `Service` definition of type `LoadBalancer`. You must design the ILB service as internal using the `networking.gke.io/load-balancer-type: internal` annotation.

The following `Service` object is an example of an ILB service:
         
         apiVersion: v1
         kind: Service
         metadata:
           annotations:
             networking.gke.io/load-balancer-type: internal
           name: ILB_SERVICE_NAME
           namespace: PROJECT_NAME
         spec:
           ports:
           - port: 1234
             protocol: TCP
             targetPort: 1234
           selector:
             k8s-app: my-app
           type: LoadBalancer
         

Replace the following:

     * `ILB_SERVICE_NAME`: the name of the ILB service.
     * `PROJECT_NAME`: the namespace of your project that contains the backend workloads.

The `port` field configures the frontend port you expose on the VIP address. The `targetPort` field configures the backend port to which you want to forward the traffic on the backend workloads. The load balancer supports Network Address Translation (NAT). The frontend and backend ports can be different.

  2. On the `selector` field of the `Service` definition, specify pods or virtual machines as the backend workloads.

The selector defines which workloads to take as backend workloads for this service, based on matching the labels you specify with labels on the workloads. The `Service` can only select backend workloads in the same project and same cluster where you define the `Service`.

For more information about service selection, see <https://kubernetes.io/docs/concepts/services-networking/service/>.

  3. Save the `Service` definition file in the same project as the backend workloads. The ILB service can only select workloads that are in the same cluster as the `Service` definition.

  4. Apply the `Service` definition file to the cluster:
         
         kubectl apply -f ILB_FILE
         

Replace `ILB_FILE` with the name of the `Service` definition file for the ILB service.

When you create an ILB service, the service gets an IP address. You can obtain the IP address of the ILB service by viewing the service status:
         
         kubectl -n PROJECT_NAME get svc ILB_SERVICE_NAME
         

Replace the following:

     * `PROJECT_NAME`: the namespace of your project that contains the backend workloads.
     * `ILB_SERVICE_NAME`: the name of the ILB service.

You must obtain an output similar to the following example:
    
    NAME                    TYPE           CLUSTER-IP    EXTERNAL-IP     PORT(S)          AGE
    ilb-service             LoadBalancer   10.0.0.1      10.0.0.1        1234:31930/TCP   22h
    

The `CLUSTER-IP` and `EXTERNAL-IP` fields must show the same value, which is the IP addressof the ILB service. This IP address is now accessible from other clusters in the organization, in accordance with [the project network policies](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/pnp-overview) that the project has.

If you don't obtain an output, ensure that you created the ILB service successfully.

GDC supports Domain Name System (DNS) names for services. However, those names only work in the same cluster for ILB services. From other clusters, you must use the IP address to access the ILB service.

**Important:** If the `CLUSTER-IP` and `EXTERNAL-IP` values are not the same, then you configured the service as an external load balancer (ELB) service. Ensure that the `networking.gke.io/load-balancer-type: internal` annotation is correct on the `Service` definition. Annotation keys and values are case sensitive.



### Create a global ILB

Create a global ILB using the gdcloud CLI or the KRM API.

###  gdcloud 

Create an ILB that targets pod or VM workloads using the gdcloud CLI.

This ILB targets all of the workloads in the project matching the label defined in the `Backend` object. The `Backend` custom resource must be scoped to a zone.

To create an ILB using the gdcloud CLI, follow these steps:

  1. Create a `Backend` resource to define the endpoint for the ILB:
         
         gdcloud compute backends create BACKEND_NAME \
           --labels=LABELS \
           --project=PROJECT_NAME \
           --cluster-name=CLUSTER_NAME \
           --zone=ZONE
         

Replace the following:

     * `BACKEND_NAME`: your chosen name for the backend resource, such as `my-backend`.
     * `LABELS`: A selector defining which endpoints between pods and VMs to use for this backend resource. For example, `app=web`.
     * `PROJECT_NAME`: the name of your project.
     * `CLUSTER_NAME`: the cluster to which the scope of the defined selectors is limited to. If this field is not specified, all of the endpoints with the given label are selected. This field is optional.
     * `ZONE`: the zone to use for this invocation. To preset the zone flag for all commands that require it, run: `gdcloud config set core/zone ZONE`. The zone flag is available only in multi-zone environments. This field is optional.
  2. Skip this step if this ILB is for pod workloads. If you are configuring an ILB for VM workloads, define a health check for the ILB:
         
         gdcloud compute health-checks create tcp HEALTH_CHECK_NAME \
           --check-interval=CHECK_INTERVAL \
           --healthy-threshold=HEALTHY_THRESHOLD \
           --timeout=TIMEOUT \
           --unhealthy-threshold=UNHEALTHY_THRESHOLD \
           --port=PORT \
           --global
         

Replace the following:

     * `HEALTH_CHECK_NAME`: your chosen name for the health check resource, such as `my-health-check`.
     * `CHECK_INTERVAL`: the amount of time in seconds from the start of one probe to the start of the next one. Defaults to `5` when omitted or set to 0. It is discouraged to set timeout longer than checkInterval.
     * `HEALTHY_THRESHOLD`: the time to wait before claiming failure. Defaults to `5` when omitted or set to 0.
     * `TIMEOUT`: the amount of time in seconds to wait before claiming failure. Defaults to `5` when omitted or set to 0. It is discouraged to set timeout longer than checkInterval.
     * `UNHEALTHY_THRESHOLD`: the number of sequential probes that must fail for the endpoint to be considered unhealthy. Defaults to `2` when omitted or set to 0.
     * `PORT`: the port on which the health check is performed. The default value is to `80`. This field is optional.
  3. Create a `BackendService` resource and add to it the previously created `Backend` resource:
         
         gdcloud compute backend-services create BACKEND_SERVICE_NAME \
           --project=PROJECT_NAME \
           --target-ports=TARGET_PORTS \
           --health-check=HEALTH_CHECK_NAME \
           --global
         

Replace the following:

     * `BACKEND_SERVICE_NAME`: the chosen name for this backend service.
     * `TARGET_PORTS`: a comma-separated list of target ports that this backend service translates, where each target port specifies the protocol, the port on the forwarding rule, and the port on the backend instance. You can specify multiple target ports. This field must be in the format `protocol:port:targetport`, such as `TCP:80:8080`. This field is optional.
     * `HEALTH_CHECK_NAME`: the name of the health check resource. This field is optional. Only include this field if you are configuring an ILB for VM workloads.
  4. Add the `BackendService` resource to the previously created `Backend` resource:
         
         gdcloud compute backend-services add-backend BACKEND_SERVICE_NAME \
           --backend-zone BACKEND_ZONE \
           --backend=BACKEND_NAME \
           --project=PROJECT_NAME \
           --global
         

  5. Create an internal `ForwardingRule` resource that defines the VIP the service is available at:
         
         gdcloud compute forwarding-rules create FORWARDING_RULE_INTERNAL_NAME \
           --backend-service=BACKEND_SERVICE_NAME \
           --cidr=CIDR \
           --ip-protocol-port=PROTOCOL_PORT \
           --load-balancing-scheme=INTERNAL \
           --project=PROJECT_NAME \
           --global
         

Replace the following:

     * `FORWARDING_RULE_INTERNAL_NAME`: your chosen name for the forwarding rule.
     * `CIDR`: the name of a `Subnet` resource in the same namespace as this forwarding rule. A `Subnet` resource represents the request and allocation information of a global subnet. For more information on `Subnet` resources, see [Example custom resources](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/ipam/overview#example-resource). If not specified, an `IPv4/32` CIDR is automatically reserved from the global IP pool. This field is optional.
     * `PROTOCOL_PORT`: the protocol and port to expose on the forwarding rule. This field must be in the format `ip-protocol=TCP:80`. The exposed port must be the same as what the actual application is exposing inside of the container.
  6. To validate the configured ILB, confirm the `Ready` condition on each of the created objects. Verify the traffic with a `curl` request to the VIP:

     1. To get the assigned VIP, describe the forwarding rule:
            
            gdcloud compute forwarding-rules describe FORWARDING_RULE_INTERNAL_NAME --global
            

     2. Verify the traffic with a `curl` request to the VIP at the port specified in the `PROTOCOL_PORT` field in the forwarding rule:
            
            curl http://FORWARDING_RULE_VIP:PORT
            

Replace the following:

        * `FORWARDING_RULE_VIP`: the VIP of the forwarding rule.
        * `PORT`: the port number of the `PROTOCOL_PORT` field in the forwarding rule.



### API

Create an ILB that targets pod or VM workloads using the KRM API. This ILB targets all of the workloads in the project matching the label defined in the Backend object. To create a zonal ILB using the KRM API, follow these steps:

  1. Create a `Backend` resource to define the endpoints for the ILB. Create `Backend` resources for each zone the workloads are placed in:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER apply -f - <<EOF
         apiVersion: networking.global.gdc.goog/v1
         kind: Backend
         metadata:
           namespace: PROJECT_NAME
           name: BACKEND_NAME
         spec:
           clusterName: CLUSTER_NAME
           endpointsLabels:
             matchLabels:
               app: server
         EOF
         

Replace the following:

     * `MANAGEMENT_API_SERVER`: the kubeconfig path of the global Management API server's kubeconfig path. For more information, see [Switch to the global context](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/access-zones#switch-global-context).
     * `PROJECT_NAME`: the name of your project.
     * `BACKEND_NAME`: the name of the `Backend` resource.
     * `CLUSTER_NAME`: This is an optional field. This field specifies the cluster to which the scope of the defined selectors are limited to. This field does not apply to VM workloads. If a `Backend` resource doesn't have the `clusterName` field included, the specified labels apply to all of the workloads in the project.

You can use the same `Backend` resource for each zone, or create `Backend` resources with different label sets for each zone.

  2. Skip this step if this ILB is for pod workloads. If you are configuring an ILB for VM workloads, define a health check for the ILB:
         
         apiVersion: networking.global.gdc.goog/v1
         kind: HealthCheck
         metadata:
           namespace: PROJECT_NAME
           name: HEALTH_CHECK_NAME
         spec:
           tcpHealthCheck:
             port: PORT
           timeoutSec: TIMEOUT
           checkIntervalSec: CHECK_INTERVAL
           healthyThreshold: HEALTHY_THRESHOLD
           unhealthyThreshold: UNHEALTHY_THRESHOLD
         

Replace the following:

     * `HEALTH_CHECK_NAME`: your chosen name for the health check resource, such as `my-health-check`.
     * `PORT`: the port on which the health check is performed. The default value is to `80`.
     * `TIMEOUT`: the amount of time in seconds to wait before claiming failure. Defaults to `5` when omitted or set to 0. It is discouraged to set timeout longer than checkInterval.
     * `CHECK_INTERVAL`: the amount of time in seconds from the start of one probe to the start of the next one. Defaults to `5` when omitted or set to 0. It is discouraged to set timeout longer than checkInterval.
     * `HEALTHY_THRESHOLD`: the number of sequential probes that must pass for the endpoint to be considered healthy. Defaults to `2` when omitted or set to 0.
     * `UNHEALTHY_THRESHOLD`: the number of sequential probes that must fail for the endpoint to be considered unhealthy. Defaults to `2` when omitted or set to 0.

Since this is a global ILB, create the health check in the global API.

  3. Create a `BackendService` object using the previously created `Backend` resource. If you are configuring an ILB for VM workloads, include the `HealthCheck` resource.
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER apply -f - <<EOF
         apiVersion: networking.global.gdc.goog/v1
         kind: BackendService
         metadata:
           namespace: PROJECT_NAME
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

     * `BACKEND_SERVICE_NAME`: the chosen name for your `BackendService` resource.
     * `HEALTH_CHECK_NAME`: the name of your previously created `HealthCheck` resource. Don't include this field if you are configuring an ILB for pod workloads.
     * `ZONE`: the zone in which the `Backend` resource is created. You can specify multiple backends in `backendRefs` field. For example:
           
           - name: my-be
             zone: Zone-A
           - name: my-be
             zone: Zone-B
           

     * The `targetPorts` field is optional. This resource lists ports that this `BackendService` resource translates. If you are using this object, provide values for the following:

       * `PORT`: the port exposed by the service.
       * `PROTOCOL`: the Layer-4 protocol which traffic must match. Only TCP and UDP are supported.
       * `TARGET_PORT`: the port to which the `PORT` value is translated to, such as `8080`. The value of `TARGET_PORT` can't be repeated in a given object. An example for `targetPorts` might look like the following:
             
             targetPorts:
             - port: 80
               protocol: TCP
               targetPort: 8080
             

  4. Create an internal `ForwardingRule` resource defining the VIP the service is available at.
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER apply -f - <<EOF
         apiVersion: networking.global.gdc.goog/v1
         kind: ForwardingRuleInternal
         metadata:
           namespace: PROJECT_NAME
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

     * `FORWARDING_RULE_INTERNAL_NAME`: the chosen name for your `ForwardingRuleInternal` resource.
     * `CIDR_NAME`: the name of a `Subnet` resource in the same namespace as this forwarding rule. A `Subnet` resource represents the request and allocation information of a global subnet. For more information on `Subnet` resources, see [Example custom resources](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/ipam/overview#example-resource). If not specified, an `IPv4/32` CIDR is automatically reserved from the global IP pool. This field is optional.
     * `PORT`: Use the `ports` field to specify an array of L4 ports for which packets are forwarded to the backends configured with this forwarding rule. At least one port has to be specified. Use the `port` field to specify a port number. The exposed port must be the same as what the actual application is exposing inside of the container.
     * `PROTOCOL`: the protocol to use for the forwarding rule, such as `TCP`. An entry in the `ports` array must look like the following:
           
           ports:
           - port: 80
             protocol: TCP
           

  5. To validate the configured ILB, confirm the `Ready` condition on each of the created objects. Verify the traffic with a `curl` request to the VIP:

     1. To get the VIP, use `kubectl get`:
            
            kubectl get forwardingruleinternal -n PROJECT_NAME
            

The output looks like the following:
            
            NAME           BACKENDSERVICE                               CIDR              READY
            ilb-name       BACKEND_SERVICE_NAME        10.200.32.59/32   True
            

     2. Test the traffic with a `curl` request to the VIP at the port specified in the `PORT` field in the forwarding rule:
            
            curl http://FORWARDING_RULE_VIP:PORT
            

Replace `FORWARDING_RULE_VIP` with the VIP of the forwarding rule.




## Create an internal load balancer for standard clusters

You can create zonal ILBs for standard clusters; global ILBs are not supported. The scope of zonal ILBs is limited to the zone specified at the time of creation. For more information, see [Global and zonal load balancers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/expose-services#global-and-zonal-load-balancers).

Create zonal ILBs for standard clusters by using the Kubernetes Service directly in the Kubernetes cluster. You can only target workloads in the cluster where the `Service` object is created when you use the Kubernetes Service directly from the Kubernetes cluster.

### Create a zonal ILB for standard clusters

You can create ILBs in GDC by creating a Kubernetes `Service` object of type `LoadBalancer` in a Kubernetes cluster. This ILB only targets workloads in the cluster where the `Service` object is created.

To create an ILB with the `Service` object, follow these steps:

  1. Create a YAML file for the `Service` definition of type `LoadBalancer`. You must design the ILB service as internal using the `networking.gke.io/load-balancer-type: internal` annotation.

The following `Service` object is an example of an ILB service:
         
         apiVersion: v1
         kind: Service
         metadata:
           annotations:
             networking.gke.io/load-balancer-type: internal
           name: ILB_SERVICE_NAME
           namespace: ILB_SERVICE_NAMESPACE
         spec:
           ports:
           - port: 1234
             protocol: TCP
             targetPort: 1234
           selector:
             k8s-app: my-app
           type: LoadBalancer
         

Replace the following:

     * `ILB_SERVICE_NAME`: the name of the ILB service.
     * `ILB_SERVICE_NAMESPACE`: the namespace that contains the backend workloads.

The `port` field configures the frontend port you expose on the VIP address. The `targetPort` field configures the backend port to which you want to forward the traffic on the backend workloads. The load balancer supports Network Address Translation (NAT). The frontend and backend ports can be different.

  2. On the `selector` field of the `Service` definition, specify the pods that will serve as the backend workloads.

The selector defines which workloads to take as backend workloads for this service, based on matching the labels you specify with labels on the workloads. The `Service` can only select backend workloads in the same project and same cluster where you define the `Service`.

For more information about service selection, see <https://kubernetes.io/docs/concepts/services-networking/service/>.

  3. Save the `Service` specification in a YAML file. Substitute the filename for ILB_FILE in the following command. The ILB service can only select workloads that are in the same cluster as the `Service` definition.

  4. Apply the `Service` definition file to the cluster:
         
         export KUBECONFIG=KUBECONFIG_PATH
         kubectl apply -f ILB_FILE
         

Replace the following:

     * `ILB_FILE`:the name of the `Service` definition file for the ILB service.
     * `KUBECONFIG_PATH`: the path to the kubeconfig file for the standard cluster.

When you create an ILB service, the service gets an IP address. You can obtain the IP address of the ILB service by viewing the service status:
    
    kubectl -n ILB_SERVICE_NAMESPACE get svc ILB_SERVICE_NAME
    

Replace the following:

     * `ILB_SERVICE_NAMESPACE`: the namespace that contains the backend workloads.
     * `ILB_SERVICE_NAME`: the name of the ILB service.
     * `KUBECONFIG_PATH`: the path to the kubeconfig file for the standard cluster.

You will obtain an output similar to the following example:
    
    NAME                    TYPE           CLUSTER-IP    EXTERNAL-IP     PORT(S)          AGE
    ilb-service             LoadBalancer   10.0.0.1      198.51.0.1        1234:31930/TCP   22h
    

This IP address is now accessible from other clusters in the organization, in accordance with [the project network policies](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/pnp-overview) that the project has.




## Select a VM as a backend for a load balancer

To link a VM to the load balancer:

  1. Make sure that the VM has a label matching the label selector used in the load balancer configuration.

For example, if your VM does not have an appropriate label, you can add the specified label from the backend object of the corresponding zone to the VM:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER label virtualmachine VM_NAME -n PROJECT_NAMELABEL
         

Replace the following:

     * `LABEL`: a label matching the `LabelSelector` in the load balancer configuration, such as `app=server`.
     * `VM_NAME`: the name of the virtual machine being linked.
     * `PROJECT_NAME`: the name of your project.
  2. Ensure that the server is listening on the same port as specified in the `HealthCheck` object.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
