---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/elb-service/
title: Configure external load balancers \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:03:58.315526+00:00
---

# Configure external load balancers  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/elb-service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Configure external load balancers Stay organized with collections  Save and categorize content based on your preferences. 

External load balancers (ELB) expose services to access from outside the organization from a pool's IP addresses assigned to the organization from the larger instance-external IP pool.

ELB Virtual IP (VIP) addresses don't conflict between organizations and are unique across all organizations. For this reason, you must use ELB services only for services that clients outside the organization need to access.

Workloads running inside the organization can access ELB services as long as you enable the workloads to exit the organization. This traffic pattern effectively requires outbound traffic from the organization before returning to the internal service.

There are distinct instructions for setting up ELBs for shared and standard clusters.

## Create an external load balancer for shared clusters

You can create global or zonal ELBs. The scope of global ELBs span across a GDC universe. The scope of zonal ELBs is limited to the zone specified at the time of creation. For more information, see [Global and zonal load balancers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/expose-services#global-and-zonal-load-balancers).

### Before you begin

To configure ELB services, you must:

  * Own the project you are configuring the load balancer for. For more information, see [Create a project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-a-project).
  * Have a customized `ProjectNetworkPolicy` (PNP) ingress policy to allow traffic to this ELB service. For more information, see Configure PNP to allow traffic to ELB.
  * Have the necessary identity and access roles:

    * Project NetworkPolicy Admin: has access to manage project network policies in the project namespace. Ask your Organization IAM Admin to grant you the Project NetworkPolicy Admin (`project-networkpolicy-admin`) role.
    * Load Balancer Admin: Ask your Organization IAM Admin to grant you the Load Balancer Admin (`load-balancer-admin`) role.
    * Global Load Balancer Admin: For global ELBs, ask your Organization IAM Admin to grant you the Global Load Balancer Admin (`global-load-balancer-admin`) role. For more information, see [Predefined role descriptions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/role-descriptions).



### Configure PNP to allow traffic to ELB

For ELB services to function, you must configure and apply your own customized `ProjectNetworkPolicy` ingress policy to allow traffic to the workloads of this ELB service. Network policies control access to your workloads, not the load balancer itself. ELBs expose workloads to your customer network, requiring explicit network policies to allow external traffic to the workload port, such as `8080`.

Specify the external CIDR address to allow traffic to the workloads of this ELB:
    
    
    kubectl --kubeconfig MANAGEMENT_API_SERVER apply -f - <<EOF
    apiVersion: networking.gdc.goog/v1
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

  * `MANAGEMENT_API_SERVER`: the kubeconfig path of the Management API server's kubeconfig path. If you have not yet generated a kubeconfig file for the API server in your targeted zone, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#cli) for details.
  * `PROJECT`: the name of your GDC project.
  * `CIDR`: the external CIDR that the ELB needs to be accessed from. This policy is required as the external load balancer uses Direct Server Return (DSR), which preserves the source external IP address and bypasses the load balancer on the return path. For more information, see [Create a global ingress firewall rule for organization-external traffic](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/organization-external-traffic#global-org-external-ingress).
  * `PORT`: the backend port on the pods behind the load balancer. This value is found in the `.spec.ports[].targetPort`field of the manifest for the `Service` resource. This field is optional.

**Note:** This configuration provides all of the resources inside projects access to the specified CIDR range.

Create ELBs using three different methods in GDC:

  * Use the [gdcloud CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-overview) to create global or zonal ELBs.
  * Use the [Networking Kubernetes Resource Model (KRM) API](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/networking/networking-api-overview) to create global or zonal ELBs.
  * Use the Kubernetes Service directly in the Kubernetes cluster. This method is only available for zonal ELBs.



You can target pod or VM workloads using the KRM API and gdcloud CLI. You can only target workloads in the cluster where the `Service` object is created when you use the Kubernetes Service directly in Kubernetes cluster.

### Create a zonal ELB

Create a zonal ELB using the gdcloud CLI, the KRM API, or the Kubernetes Service in the Kubernetes cluster:

###  gdcloud 

Create an ELB that targets pod or VM workloads using the gdcloud CLI.

This ELB targets all of the workloads in the project matching the label defined in the `Backend` object.

To create an ELB using the gdcloud CLI, follow these steps:

  1. Create a `Backend` resource to define the endpoint for the ELB:
         
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
     * `CLUSTER_NAME`: the cluster that the scope of the defined selectors is limited to. If this field is not specified, all of the endpoints with the given label are selected. This field is optional.
  2. Skip this step if this ELB is for pod workloads. If you are configuring an ELB for VM workloads, define the type of [health check](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/health-checks) for the ELB. For example, to create a TCP Health Check, define it as follows:
         
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
     * `HEALTHY_THRESHOLD`: the number of sequential probes that must pass for the endpoint to be considered healthy.. Defaults to `5` when omitted or set to 0.
     * `TIMEOUT`: the amount of time in seconds to wait before claiming failure. Defaults to `5` when omitted or set to 0. It is discouraged to set timeout longer than checkInterval.
     * `UNHEALTHY_THRESHOLD`: the number of sequential probes that must fail for the endpoint to be considered unhealthy. Defaults to `2` when omitted or set to 0.
     * `PORT`: the port on which the health check is performed. The default value is `80`. This field is optional.
     * `ZONE`: the zone you are creating this ELB in.
  3. Create a `BackendService` resource and add to it the previously created `Backend` resource:
         
         gdcloud compute backend-services create BACKEND_SERVICE_NAME \
           --project=PROJECT_NAME \
           --target-ports=TARGET_PORTS \
           --zone=ZONE \
           --health-check=HEALTH_CHECK_NAME
         

Replace the following:

     * `BACKEND_SERVICE_NAME`: the chosen name for this backend service.
     * `TARGET_PORT`: a comma-separated list of target ports that this backend service translates, where each target port specifies the protocol, the port on the forwarding rule, and the port on the backend instance. You can specify multiple target ports. This field must be in the format `protocol:port:targetport`, such as `TCP:80:8080`. This field is optional.
     * `HEALTH_CHECK_NAME`: the name of the health check resource. This field is optional. Only include this field if you are configuring an ELB for VM workloads.
  4. Add the `BackendService` resource to the previously created `Backend` resource:
         
         gdcloud compute backend-services add-backend BACKEND_SERVICE_NAME \
           --backend=BACKEND_NAME \
           --project=PROJECT_NAME \
           --zone=ZONE
         

  5. Optional: Use session affinity for ELBs to ensure that requests from the same client are consistently routed to the same backend. To enable session affinity for load balancers, create a backend service policy using `gdcloud compute load-balancer-policy create` command:
         
         gdcloud compute load-balancer-policy create POLICY_NAME
          --session-affinity=MODE
          --selectors=RESOURCE_LABEL
         

Replace the following:

     * `POLICY_NAME`: your chosen name for the backend service policy.
     * `MODE`: the session affinity mode. Two modes are supported:

       * `NONE`: Session affinity is disabled. Requests are routed to any available backend. This is the default mode.
       * `CLIENT_IP_DST_PORT_PROTO`: Requests from the same four-tuple (source IP address, destination IP address, destination port, and protocol) are routed to the same backend.
     * `RESOURCE_LABEL`: the label selector that selects which backend service the `BackendServicePolicy` resource is applied to in the project namespace. If multiple `BackendServicePolicy` resources match the same backend service, and at least one of these policies has session affinity enabled, then session affinity for this `BackendService` resource becomes enabled.

  6. Create an external `ForwardingRule` resource that defines the VIP the service is available at:
         
         gdcloud compute forwarding-rules create FORWARDING_RULE_EXTERNAL_NAME \
           --backend-service=BACKEND_SERVICE_NAME \
           --cidr=CIDR \
           --ip-protocol-port=PROTOCOL_PORT \
           --load-balancing-scheme=EXTERNAL \
           --zone=ZONE \
           --project=PROJECT_NAME
         

Replace the following:

     * `BACKEND_SERVICE_NAME`: the name of your backend service.
     * `FORWARDING_RULE_EXTERNAL_NAME`: your chosen name for the forwarding rule.
     * `CIDR`: this field is optional. If not specified, an `IPv4/32` CIDR is automatically reserved from the zonal IP pool. Specify the name of a `Subnet` resource in the same namespace as this forwarding rule. A `Subnet` resource represents the request and allocation information of a zonal subnet. For more information on `Subnet` resources, see [Example custom resources](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/ipam/overview#example-resource).
     * `PROTOCOL_PORT`: the protocol and port to expose on the forwarding rule. This field must be in the format `ip-protocol=TCP:80`. The exposed port must be the same as what the actual application is exposing inside of the container.
  7. To verify the configured ELB, confirm the `Ready` condition on each of the created objects. To get the assigned IP address of the load balancer, describe the forwarding rule:
         
         gdcloud compute forwarding-rules describe FORWARDING_RULE_EXTERNAL_NAME
         

  8. To validate the configured ELB, confirm the `Ready` condition on each of the created objects. Verify the traffic with a `curl` request to the VIP:

     1. To get the assigned VIP, describe the forwarding rule:
            
            gdcloud compute forwarding-rules describe FORWARDING_RULE_EXTERNAL_NAME
            

     2. Verify the traffic with a `curl` request to the VIP at the port specified in the `PROTOCOL_PORT` field in the forwarding rule:
            
            curl http://FORWARDING_RULE_VIP:PORT
            

Replace the following:

        * `FORWARDING_RULE_VIP`: the VIP of the forwarding rule.
        * `PORT`: the port number of the `PROTOCOL_PORT` field in the forwarding rule.



### API

Create an ELB that targets pod or VM workloads using the KRM API. This ELB targets all of the workloads in the project matching the label defined in the `Backend` object.

To create a zonal ELB using the KRM API, follow these steps:

  1. Create a `Backend` resource to define the endpoints for the ELB. Create `Backend` resources for each zone the workloads are placed in:
         
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
  2. Skip this step if this ELB is for pod workloads. If you are configuring an ELB for VM workloads, define a health check for the ELB:
         
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
  3. Create a `BackendService` object using the previously created `Backend` resource. If you are configuring an ELB for VM workloads, include the `HealthCheck` resource.
         
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
     * `HEALTH_CHECK_NAME`: the name of your previously created `HealthCheck` resource. Don't include this field if you are configuring an ELB for pod workloads.
  4. Optional: Use session affinity for ELBs to ensure that requests from the same client are consistently routed to the same backend. To enable session affinity for load balancers, create a `BackendServicePolicy` resource. This resource defines session affinity settings and applies the `BackendServicePolicy` resource to the `BackendService` resource. Create and apply the `BackendServicePolicy` resource:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER apply -f - <<EOF
          apiVersion: networking.global.gdc.goog/v1
          kind: BackendServicePolicy
          metadata:
              namespace: PROJECT_NAME
              name: POLICY_NAME
          spec:
              sessionAffinity: MODE
              selector:
                  matchLabels:
                    RESOURCE_LABEL
         

Replace the following:

     * `POLICY_NAME`: your chosen name for the backend service policy.
     * `MODE`: the session affinity mode. Two modes are supported:

       * `NONE`: Session affinity is disabled. Requests are routed to any available backend. This is the default mode.
       * `CLIENT_IP_DST_PORT_PROTO`: Requests from the same four-tuple (source IP address, destination IP address, destination port, and protocol) are routed to the same backend.
     * `RESOURCE_LABEL`: the label selector that selects which backend service the `BackendServicePolicy` resource is applied to in the project namespace. If multiple `BackendServicePolicy` resources match the same backend service, and at least one of these policies has session affinity enabled, then session affinity for this `BackendService` resource becomes enabled.

  5. Create an external `ForwardingRule` resource defining the VIP the service is available at.
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER apply -f - <<EOF
         apiVersion: networking.gdc.goog/v1
         kind: ForwardingRuleExternal
         metadata:
           namespace: PROJECT_NAME
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

     * `BACKEND_SERVICE_NAME`: the name of your `BackendService` resource.
     * `FORWARDING_RULE_EXTERNAL_NAME`: your chosen name for your `ForwardingRuleExternal` resource.
     * `CIDR_NAME`: the `cidrRef` field is optional. If not specified, an `IPv4/32` CIDR is automatically reserved from the zonal IP pool. Specify the name of a `Subnet` resource in the same namespace as this forwarding rule. A `Subnet` resource represents the request and allocation information of a zonal subnet. For more information on `Subnet` resources, see [Example custom resources](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/ipam/overview#example-resource).
     * `PORT`: Use the `ports` field to specify an array of L4 ports for which packets are forwarded to the backends configured with this forwarding rule. At least one port must be specified. Use the `port` field to specify a port number. The exposed port must be the same as what the actual application is exposing inside of the container.
     * `PROTOCOL`: the protocol to use for the forwarding rule, such as `TCP`. An entry in the `ports` array must look like the following:
           
           ports:
           - port: 80
             protocol: TCP
           

  6. To validate the configured ELB, confirm the `Ready` condition on each of the created objects. Verify the traffic with a `curl` request to the VIP:

     1. To get the VIP, use `kubectl get`:
            
            kubectl get forwardingruleexternal -n PROJECT_NAME
            

The output looks like the following:
            
            NAME           BACKENDSERVICE                               CIDR              READY
            elb-name       BACKEND_SERVICE_NAME        10.200.32.59/32   True
            

     2. Verify the traffic with a `curl` request to the VIP at the port specified in the `PORT` field in the forwarding rule:
            
            curl http://FORWARDING_RULE_VIP:PORT
            

Replace `FORWARDING_RULE_VIP` with the VIP of the forwarding rule.




### Kubernetes Service

You can create ELBs in GDC by creating a Kubernetes `Service` of type `LoadBalancer` in a Kubernetes cluster.

To create an ELB service, do the following:

  1. Create a YAML file for the `Service` definition of type `LoadBalancer`.

**Note:** Contrary to the process for [internal load balancers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/ilb-service), don't add annotations on the file. If you don't specify the `internal` annotation, then the service is external-facing by default.

The following `Service` object is an example of an ELB service:
         
         apiVersion: v1
         kind: Service
         metadata:
           name: ELB_SERVICE_NAME
           namespace: PROJECT_NAME
         spec:
           ports:
           - port: 1235
             protocol: TCP
             targetPort: 1235
           selector:
             k8s-app: my-app
           type: LoadBalancer
         

Replace the following:

     * `ELB_SERVICE_NAME`: the name of the ELB service.
     * `PROJECT_NAME`: the namespace of your project that contains the backend workloads.

The `port` field configures the frontend port you expose on the VIP address. The `targetPort` field configures the backend port to which you want to forward the traffic on the backend workloads. The load balancer supports Network Address Translation (NAT). The frontend and backend ports can be different.

  2. On the `selector` field of the `Service` definition, specify pods or virtual machines as the backend workloads.

The selector defines which workloads to take as backend workloads for this service, based on matching the labels you specify with labels on the workloads. The `Service` can only select backend workloads in the same project and same cluster where you define the `Service`.

For more information about service selection, see <https://kubernetes.io/docs/concepts/services-networking/service/>.

  3. Save the `Service` definition file in the same project as the backend workloads.

  4. Apply the `Service` definition file to the cluster:
         
         kubectl apply -f ELB_FILE
         

Replace `ELB_FILE` with the name of the `Service` definition file for the ELB service.

When you create an ELB, the service gets two IP addresses. One is an internal IP address accessible only from within the same cluster. The other is the external IP address, accessible from inside and outside the organization. You can obtain the IP addresses of the ELB service by viewing the service status:
         
         kubectl -n PROJECT_NAME get svc ELB_SERVICE_NAME
         

Replace the following:

     * `PROJECT_NAME`: the namespace of your project that contains the backend workloads.
     * `ELB_SERVICE_NAME`: the name of the ELB service.

You must obtain an output similar to the following example:
    
    NAME                    TYPE           CLUSTER-IP    EXTERNAL-IP     PORT(S)          AGE
    elb-service             LoadBalancer   10.0.0.1      20.12.1.11      1235:31931/TCP   22h
    

The `EXTERNAL-IP` is the IP address of the service that is accessible from outside the organization.

If you don't obtain an output, ensure that you created the ELB service successfully.




### Create a global ELB

Create a global ELB using the gdcloud CLI or the KRM API.

###  gdcloud 

Create an ELB that targets pod or VM workloads using the gdcloud CLI.

This ELB targets all of the workloads in the project matching the label defined in the `Backend` object. The `Backend` custom resource must be scoped to a zone.

To create an ELB using the gdcloud CLI, follow these steps:

  1. Create a `Backend` resource to define the endpoint for the ELB:
         
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
  2. Skip this step if this ELB is for pod workloads. If you are configuring an ELB for VM workloads, define a health check for the ELB:
         
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
     * `HEALTH_CHECK_NAME`: the name of the health check resource. This field is optional. Only include this field if you are configuring an ELB for VM workloads.
  4. Add the `BackendService` resource to the previously created `Backend` resource:
         
         gdcloud compute backend-services add-backend BACKEND_SERVICE_NAME \
           --backend=BACKEND_NAME \
           --backend-zone BACKEND_ZONE \
           --project=PROJECT_NAME \
           --global
         

  5. Optional: Use session affinity for ELBs to ensure that requests from the same client are consistently routed to the same backend. To enable session affinity for load balancers, create a backend service policy using `gdcloud compute load-balancer-policy create` command:
         
         gdcloud compute load-balancer-policy create POLICY_NAME
          --session-affinity=MODE
          --selectors=RESOURCE_LABEL
         

Replace the following:

     * `POLICY_NAME`: your chosen name for the backend service policy.
     * `MODE`: the session affinity mode. Two modes are supported:

       * `NONE`: Session affinity is disabled. Requests are routed to any available backend. This is the default mode.
       * `CLIENT_IP_DST_PORT_PROTO`: Requests from the same four-tuple (source IP address, destination IP address, destination port, and protocol) are routed to the same backend.
     * `RESOURCE_LABEL`: the label selector that selects which backend service the `BackendServicePolicy` resource is applied to in the project namespace. If multiple `BackendServicePolicy` resources match the same backend service, and at least one of these policies has session affinity enabled, then session affinity for this `BackendService` resource becomes enabled.

  6. Create an external `ForwardingRule` resource that defines the VIP the service is available at:
         
         gdcloud compute forwarding-rules create FORWARDING_RULE_EXTERNAL_NAME \
           --backend-service=BACKEND_SERVICE_NAME \
           --cidr=CIDR \
           --ip-protocol-port=PROTOCOL_PORT \
           --load-balancing-scheme=EXTERNAL \
           --project=PROJECT_NAME \
           --global
         

Replace the following:

     * `BACKEND_SERVICE_NAME`: the name of your backend service.
     * `FORWARDING_RULE_EXTERNAL_NAME`: your chosen name for the forwarding rule.
     * `CIDR`: this field is optional. If not specified, an `IPv4/32` CIDR is automatically reserved from the global IP pool. Specify the name of a `Subnet` resource in the same namespace as this forwarding rule. A `Subnet` resource represents the request and allocation information of a global subnet. For more information on `Subnet` resources, see [Example custom resources](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/ipam/overview#example-resource).
     * `PROTOCOL_PORT`: the protocol and port to expose on the forwarding rule. This field must be in the format `ip-protocol=TCP:80`. The exposed port must be the same as what the actual application is exposing inside of the container.
  7. To verify the configured ELB, confirm the `Ready` condition on each of the created objects. To get the assigned IP address of the load balancer, describe the forwarding rule:
         
         gdcloud compute forwarding-rules describe FORWARDING_RULE_EXTERNAL_NAME
         

  8. To validate the configured ELB, confirm the `Ready` condition on each of the created objects. Verify the traffic with a `curl` request to the VIP:

     1. To get the assigned VIP, describe the forwarding rule:
            
            gdcloud compute forwarding-rules describe FORWARDING_RULE_EXTERNAL_NAME --global
            

     2. Verify the traffic with a `curl` request to the VIP at the port specified in the `PROTOCOL_PORT` field in the forwarding rule:
            
            curl http://FORWARDING_RULE_VIP:PORT
            

Replace the following:

        * `FORWARDING_RULE_VIP`: the VIP of the forwarding rule.
        * `PORT`: the port number from of the `PROTOCOL_PORT` field in the forwarding rule.



### API

Create an ELB that targets pod or VM workloads using the KRM API. This ELB targets all of the workloads in the project matching the label defined in the Backend object. To create a zonal ELB using the KRM API, follow these steps:

  1. Create a `Backend` resource to define the endpoints for the ELB. Create `Backend` resources for each zone the workloads are placed in:
         
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

     * `MANAGEMENT_API_SERVER`: the kubeconfig path of the global Management API server's kubeconfig path. For more information, see [Switch to the global context](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/access-zones#switch-global-context).
     * `PROJECT_NAME`: the name of your project.
     * `BACKEND_NAME`: the name of the `Backend` resource.
     * `CLUSTER_NAME`: This is an optional field. This field specifies the cluster to which the scope of the defined selectors are limited to. This field does not apply to VM workloads. If a `Backend` resource doesn't have the `clusterName` field included, the specified labels apply to all of the workloads in the project.
  2. Skip this step if this ELB is for pod workloads. If you are configuring an ELB for VM workloads, define a health check for the ELB:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER apply -f - <<EOF
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
         EOF
         

Replace the following:

     * `HEALTH_CHECK_NAME`: your chosen name for the health check resource, such as `my-health-check`.
     * `PORT`: the port on which the health check is performed. The default value is to `80`.
     * `TIMEOUT`: the amount of time in seconds to wait before claiming failure. Defaults to `5` when omitted or set to 0. It is discouraged to set timeout longer than checkInterval.
     * `CHECK_INTERVAL`: the amount of time in seconds from the start of one probe to the start of the next one. Defaults to `5` when omitted or set to 0. It is discouraged to set timeout longer than checkInterval.
     * `HEALTHY_THRESHOLD`: the number of sequential probes that must pass for the endpoint to be considered healthy. Defaults to `2` when omitted or set to 0.
     * `UNHEALTHY_THRESHOLD`: the number of sequential probes that must fail for the endpoint to be considered unhealthy. Defaults to `2` when omitted or set to 0.

Since this is a global ELB, create the health check in the global API.

  3. Create a `BackendService` object using the previously created `Backend` resource. If you are configuring an ELB for VM workloads, include the `HealthCheck` resource.
         
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
     * `HEALTH_CHECK_NAME`: the name of your previously created `HealthCheck` resource. Don't include this field if you are configuring an ELB for pod workloads.
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
             

  4. Optional: Use session affinity for ELBs to ensure that requests from the same client are consistently routed to the same backend. To enable session affinity for load balancers, create a `BackendServicePolicy` resource. This resource defines session affinity settings and applies the `BackendServicePolicy` resource to the `BackendService` resource. Create and apply the `BackendServicePolicy` resource:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER apply -f - <<EOF
          apiVersion: networking.global.gdc.goog/v1
          kind: BackendServicePolicy
          metadata:
              namespace: PROJECT_NAME
              name: POLICY_NAME
          spec:
              sessionAffinity: MODE
              selector:
                  matchLabels:
                    RESOURCE_LABEL
         

Replace the following:

     * `POLICY_NAME`: your chosen name for the backend service policy.
     * `MODE`: the session affinity mode. Two modes are supported:

       * `NONE`: Session affinity is disabled. Requests are routed to any available backend. This is the default mode.
       * `CLIENT_IP_DST_PORT_PROTO`: Requests from the same four-tuple (source IP address, destination IP address, destination port, and protocol) are routed to the same backend.
     * `RESOURCE_LABEL`: the label selector that selects which backend service the `BackendServicePolicy` resource is applied to in the project namespace. If multiple `BackendServicePolicy` resources match the same backend service, and at least one of these policies has session affinity enabled, then session affinity for this `BackendService` resource becomes enabled.

  5. Create an external `ForwardingRule` resource defining the VIP the service is available at.
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER apply -f - <<EOF
         apiVersion: networking.global.gdc.goog/v1
         kind: ForwardingRuleExternal
         metadata:
           namespace: PROJECT_NAME
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
     * `CIDR_NAME`: The `cidrRef` field is optional. If not specified, an `IPv4/32` CIDR is automatically reserved from the global IP pool. Specify the name of a `Subnet` resource in the same namespace as this forwarding rule. A `Subnet` resource represents the request and allocation information of a global subnet. For more information on `Subnet` resources, see [Example custom resources](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/ipam/overview#example-resource).
     * `PORT`: Use the `ports` field to specify an array of L4 ports for which packets are forwarded to the backends configured with this forwarding rule. At least one port has to be specified. Use the `port` field to specify a port number. The exposed port must be the same as what the actual application is exposing inside of the container.
     * `PROTOCOL`: the protocol to use for the forwarding rule, such as `TCP`. An entry in the `ports` array must look like the following:
           
           ports:
           - port: 80
             protocol: TCP
           

  6. To validate the configured ELB, confirm the `Ready` condition on each of the created objects. Verify the traffic with a `curl` request to the VIP:

     1. To get the VIP, use `kubectl get`:
            
            kubectl get forwardingruleexternal -n PROJECT_NAME
            

The output looks like the following:
            
            NAME           BACKENDSERVICE                               CIDR              READY
            elb-name       BACKEND_SERVICE_NAME        10.200.32.59/32   True
            

     2. Verify the traffic with a `curl` request to the VIP at the port specified in the `PORT` field in the forwarding rule:
            
            curl http://FORWARDING_RULE_VIP:PORT
            

Replace `FORWARDING_RULE_VIP` with the VIP of the forwarding rule.




## Create an external load balancer for standard clusters

An Application Owner (AO) can create a Kubernetes service of type LoadBalancer to expose services externally. This service can only select the backends within the standard cluster in which the service is created. This is equivalent to a Zonal Cluster Scoped ELB. Global ELB is not supported for standard clusters. For more information, see [Global and zonal load balancers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/expose-services#global-and-zonal-load-balancers).

### Before you begin

To configure ELB services, you must:

  * Own the project you are configuring the load balancer for. For more information, see [Create a project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-a-project).
  * Have a customized `ProjectNetworkPolicy` (PNP) ingress policy to allow traffic to this ELB service. For more information, see Configure PNP to allow traffic to ELB for standard clusters.
  * Have the necessary identity and access roles:

    * Project NetworkPolicy Admin: has access to manage project network policies in the project namespace Ask your Organization IAM Admin to grant you the Project NetworkPolicy Admin (`project-networkpolicy-admin`) role.
    * Load Balancer Admin: Ask your Organization IAM Admin to grant you the Load Balancer Admin (`load-balancer-admin`) role.



### Configure PNP to allow traffic to ELB for standard clusters

For ELB services to function, you must configure and apply your own customized `ProjectNetworkPolicy` ingress policy to allow traffic to the workloads of this ELB service. Network policies control access to your workloads, not the load balancer itself. ELBs expose workloads to your customer network, requiring explicit network policies to allow external traffic to the workload port, such as `8080`.

The following example project network policy YAML file allows traffic from a workload in another project to access a workload in the current Project through the ELB.
    
    
    apiVersion: networking.gdc.goog/v1
    kind: ProjectNetworkPolicy
    metadata:
      name: allow-ingress-from-client-to-server
      namespace: ${VANILLA_CLUSTER_PROJECT}
    spec:
      policyType: Ingress
      subject:
        subjectType: UserWorkload
        userWorkloadSelector:
        labelSelector:
          clusters:
            matchLabels:
              kubernetes.io/metadata.name: my-sc-1
          namespaces:
            matchLabels:
              kubernetes.io/metadata.name: my-app-ns
          workloads:
            matchLabels:
              app: my-internal-app
      ingress:
      - from:
        - projectSelector:
            projects:
              matchNames:
              - "$PROJECT_2"
            workloadSelector:
              workloads:
                matchLabels:
                  app: my-client
        ports:
        - protocol: TCP
          port: 8080
    

### Create a zonal ELB for standard clusters

You can create ELBs in GDC by creating a Kubernetes `Service` of type `LoadBalancer` in the standard Kubernetes cluster.

To create an ELB service, do the following:

  1. Create a YAML file for the `Service` definition of type `LoadBalancer`.

**Note:** Contrary to the process for [internal load balancers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/ilb-service), don't add annotations on the file. If you don't specify the `internal` annotation, then the service is external-facing by default.

The following `Service` object is an example of an ELB service:
         
         apiVersion: v1
         kind: Service
         metadata:
           name: ELB_SERVICE_NAME
           namespace: ELB_SERVICE_NAMESPACE
         spec:
           ports:
           - port: PORT
             protocol: TCP
             targetPort: TARGET_PORT
           selector:
             k8s-app: my-app # Example selector, replace with your workload's labels
           type: LoadBalancer
         

Replace the following:

     * `ELB_SERVICE_NAME`: the name of the ELB service.
     * `ELB_SERVICE_NAMESPACE`: the namespace in your standard cluster that contains the backend workloads.
     * `PORT`: the port exposed by the Kubernetes Service itself. Other services or external clients within the cluster will connect to this port on the Service's IP address.
     * `TARGET_PORT`: the port inside the container of your pod where your application is actively running and listening for incoming connections. This can be a numerical port or a named port defined in the Pod's container specification.

The `port` field configures the frontend port you expose on the VIP address. The `targetPort` field configures the backend port to which you want to forward the traffic on the backend workloads. The load balancer supports Network Address Translation (NAT). The frontend and backend ports can be different.

  2. On the `selector` field of the `Service` definition, specify key-value pairs to match the backend workloads. For standard clusters, only pods are supported as workloads.

selector that you define, based on matching the labels you specify with labels on the workloads. The `Service` can only select backend workloads in the same project and same cluster where you define the `Service`.

For more information about service selection, see [https://kubernetes.io/docs/concepts/services-networking/service/](https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer).

  3. Save the `Service` specification in a YAML file. Substitute the filename for ELB_FILE in the following command.

  4. Apply the `Service` definition file to the cluster:
         
         export KUBECONFIG=KUBECONFIG_PATH
         kubectl apply -f ELB_FILE
         

Replace the following:

     * `ELB_FILE`:the name of the `Service` definition file for the ELB service.
     * `KUBECONFIG_PATH`: the path to the kubeconfig file for the standard cluster.

You can obtain the IP addresses of the ELB service by viewing the service status:
    
    kubectl -n ELB_SERVICE_NAMESPACE get svc ELB_SERVICE_NAME
    

Replace the following:

     * `ELB_SERVICE_NAMESPACE`: the namespace that contains the backend workloads.
     * `ELB_SERVICE_NAME`: the name of the ELB service.

You must obtain an output similar to the following example:
    
    NAME                    TYPE           CLUSTER-IP    EXTERNAL-IP     PORT(S)          AGE
    elb-service             LoadBalancer   10.0.0.1      203.0.1.11      1235:31931/TCP   22h
    

The `EXTERNAL-IP` is the IP address of the service that is accessible from outside the organization.




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

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
