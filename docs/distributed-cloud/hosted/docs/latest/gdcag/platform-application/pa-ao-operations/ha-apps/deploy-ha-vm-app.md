---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/ha-apps/deploy-ha-vm-app/
title: Deploy a highly available VM application \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:30:12.367434+00:00
---

# Deploy a highly available VM application  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/ha-apps/deploy-ha-vm-app/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Deploy a highly available VM application Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to deploy a highly available (HA) virtual machine (VM) application in Google Distributed Cloud (GDC) air-gapped. To ensure resilience, you must deploy your application across multiple zones and configure storage replication so the application and its data are recoverable in the case of unexpected downtime or local disaster.

This document is intended for application developers who are responsible for creating resilient VM workloads.

For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Objectives

  * Create a VM instance with attached boot disks in two or more zones in your GDC universe.
  * Configure global load balancing.
  * Configure storage replication using either block storage or object storage.



## Before you begin

To prepare for the tasks in this document, you must obtain the necessary permissions and verify your environment.

### Request IAM roles and permissions

Contact your IAM Org Admin to request the following roles:

  * **Project VirtualMachine Admin** (`project-vm-admin`): create and edit VMs in a project namespace.
  * **Project Network Policy Admin** (`global-project-networkpolicy-admin`): create and edit project network policies across zones.
  * **Global Load Balancer Admin** (`global-load-balancer-admin`): create and edit global load balancers.
  * **Bucket Project Admin** (`global-project-bucket-admin`): create and edit dual-zone storage buckets.



For more information, see [role descriptions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/role-descriptions).

### Prepare your environment

Confirm you have the following tools and configurations present in your air-gapped environment:

  * Install and configure the gdcloud CLI and set your zonal and global contexts. For more information, see [Access zones with your tools](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/access-zones).

  * [Install the kubectl CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/get-started/kubectl) and set appropriate kubeconfig files for the global API server and management API server. For more information, see [Manually generate kubeconfig file](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#generate-kubeconfig-file).

  * Verify that your GDC universe has multiple zones available. For more information, see [List zones in a universe](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/access-zones#list-zones-in-universe).




## Create a VM instance in multiple zones

To create a highly available VM application, you must create a separate VM instance in each zone of your GDC universe.

The following steps use a GDC-provided OS image and attach a boot disk to the VM. For more information about creating VM instances and using custom images, see [Create and start a VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/create-a-vm/create-and-start).

By default, all GDC projects can create VMs from GDC-provided OS images.

###  Console 

  1. In the navigation menu, select **Virtual Machines > Instances**.
  2. Click **Create Instance**.
  3. In the **Name** field, specify a name for the VM.
  4. Select the zone in which to create the VM.
  5. Click **Add Labels** to assign any labels to the VM to help organize your VM instances.
  6. Select the machine configuration to use for the VM. Verify that the machine type aligns with your workload, depending on your requirements.
  7. Click **Next**.
  8. Enable external access for your VM instance.
  9. Click **Next**.
  10. Select **Add New Disk**.
  11. Assign your VM disk a name.
  12. Configure your disk size and attachment settings.
  13. Click **Save**.
  14. Click **Create** to create the VM instance.
  15. Repeat the previous steps for each zone in your GDC universe. Make sure a VM instance resides in every zone that you want for your HA strategy.



###  gdcloud 

  1. Sign in to the zone that you want to host your VM instance:
         
         gdcloud config set core/zone ZONE
         

  2. Create the VM instance in the zone using a GDC-provided image:
         
         gdcloud compute instances create VM_NAME \
             --machine-type=MACHINE_TYPE \
             --image=BOOT_DISK_IMAGE_NAME
             --image-project=vm-system \
             --boot-disk-size=BOOT_DISK_SIZE \
             --no-boot-disk-auto-delete=NO_BOOT_DISK_AUTO_DELETE
         

Replace the following:

     * `VM_NAME`: the name of the new VM. The name must only contain alphanumeric characters and dashes, and be no longer than 53 characters.
     * `MACHINE_TYPE`: the predefined machine type for the new VM. To select an available machine type, run `gdcloud compute machine-types list`.
     * `BOOT_DISK_IMAGE_NAME`: the name of the image to use for the new VM boot disk.
     * `BOOT_DISK_SIZE`: the size of the boot disk, such as `20GB`. This value must always be greater than or equal to the `minimumDiskSize` of the boot disk image.
     * `NO_BOOT_DISK_AUTO_DELETE`: whether the boot disk is automatically deleted when the VM instance gets deleted.
  3. Repeat the previous steps for each zone in your GDC universe. Make sure a VM instance resides in every zone that you want for your HA strategy.




###  API 

  1. Create the VM instance in the zone using a GDC-provided image:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER apply -f - <<EOF
         apiVersion: virtualmachine.gdc.goog/v1
         kind: VirtualMachineDisk
         metadata:
           name: VM_BOOT_DISK_NAME
           namespace: PROJECT
         spec:
           source:
             image:
               name: BOOT_DISK_IMAGE_NAME
               namespace: vm-system
           size: BOOT_DISK_SIZE
         ---
         apiVersion: virtualmachine.gdc.goog/v1
         kind: VirtualMachine
         metadata:
           name: VM_NAME
           namespace: PROJECT
         spec:
           compute:
             virtualMachineType: MACHINE_TYPE
           disks:
             - virtualMachineDiskRef:
                 name: VM_BOOT_DISK_NAME
               boot: true
               autoDelete: BOOT_DISK_AUTO_DELETE
         ---
         apiVersion: virtualmachine.gdc.goog/v1
         kind: VirtualMachineExternalAccess
         metadata:
           name: VM_NAME
           namespace: PROJECT
         spec:
           enabled: true
           ports:
           - name: port-80
             port: 80
             protocol: TCP
         EOF
         

Replace the following:

     * `MANAGEMENT_API_SERVER`: the Management API server kubeconfig file for the zone in which to create the VM instance. If you have not yet generated a kubeconfig file for the Management API server, see [Manually generate kubeconfig file](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#zonal-resources-kubeconfig) for details.
     * `VM_BOOT_DISK_NAME`: the name of the new VM boot disk.
     * `PROJECT`: the GDC project to create the VM.
     * `BOOT_DISK_IMAGE_NAME`: the name of the image to use for the new VM boot disk.
     * `BOOT_DISK_SIZE`: the size of the boot disk, such as `20Gi`. This value must always be greater than or equal to the `minimumDiskSize` of the boot disk image.
     * `VM_NAME`: the name of the new VM. The name must only contain alphanumeric characters and dashes, and be no longer than 53 characters.
     * `MACHINE_TYPE`: the predefined machine type for the new VM. To select an available machine type, run `gdcloud compute machine-types list`.
     * `BOOT_DISK_AUTO_DELETE`: whether the boot disk is automatically deleted when the VM instance gets deleted.
  2. Verify that the VM is available and wait for the VM to show the `Running` state. The `Running` state does not indicate that the OS is fully ready and accessible.
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
             get virtualmachine.virtualmachine.gdc.goog VM_NAME -n PROJECT
         

Replace `VM_NAME` and `PROJECT` with the name and project of the VM.

  3. Repeat the previous steps for each zone in your GDC universe. Make sure a VM instance resides in every zone that you want for your HA strategy.




## Configure load balancers

To distribute traffic between your VMs in different zones, create load balancers. You can configure both internal and external load balancers globally to ensure that client requests are routed to healthy zones.

### Create a global internal load balancer

Internal load balancers (ILB) expose services within the organization from an internal IP address pool assigned to the organization. An ILB service is never accessible from any endpoint outside of the organization.

Complete the following steps to create a global ILB for your VM workloads.

###  gdcloud 

Create an ILB that targets VM workloads using the gdcloud CLI.

This ILB targets all of the workloads in the project matching the label defined in the `Backend` object. The `Backend` custom resource must be scoped to a zone.

To create an ILB using the gdcloud CLI, follow these steps:

  1. Create a zonal `Backend` resource in each zone where your VMs are running to define the endpoint for the ILB:
         
         gdcloud compute backends create BACKEND_NAME \
             --labels=LABELS \
             --project=PROJECT \
             --zone=ZONE
         

Replace the following:

     * `BACKEND_NAME`: the chosen name for the backend resource, such as `my-backend`.
     * `LABELS`: the selector defining which endpoints between VMs to use for this backend resource, such as `app=web`.
     * `PROJECT`: the name of your project.
     * `ZONE`: the zone to use for this invocation. To preset the zone flag for all commands that require it, run `gdcloud config set core/zone ZONE`. The zone flag is available only in multi-zone environments. This field is optional.

Repeat this step for each zone in your GDC universe.

  2. Define a global health check for the ILB:
         
         gdcloud compute health-checks create tcp HEALTH_CHECK_NAME \
             --check-interval=CHECK_INTERVAL \
             --healthy-threshold=HEALTHY_THRESHOLD \
             --timeout=TIMEOUT \
             --unhealthy-threshold=UNHEALTHY_THRESHOLD \
             --port=PORT \
             --global
         

Replace the following:

     * `HEALTH_CHECK_NAME`: the name for the health check resource, such as `my-health-check`.
     * `CHECK_INTERVAL`: the amount of time in seconds from the start of one probe to the start of the next one. The default value is `5`. This field is optional.
     * `HEALTHY_THRESHOLD`: the time to wait before claiming failure. The default value is `5`. This field is optional.
     * `TIMEOUT`: the amount of time in seconds to wait before claiming failure. The default value is `5`. This field is optional.
     * `UNHEALTHY_THRESHOLD`: the number of sequential probes that must fail for the endpoint to be considered unhealthy. The default value is `2`. This field is optional.
     * `PORT`: the port on which the health check is performed. The default value is `80`. This field is optional.
  3. Create a global `BackendService` resource:
         
         gdcloud compute backend-services create BACKEND_SERVICE_NAME \
             --project=PROJECT \
             --target-ports=TARGET_PORTS \
             --health-check=HEALTH_CHECK_NAME \
             --global
         

Replace the following:

     * `BACKEND_SERVICE_NAME`: the name for the backend service.
     * `PROJECT`: the name of your project.
     * `TARGET_PORTS`: a comma-separated list of target ports that this backend service translates, where each target port specifies the protocol, the port on the forwarding rule, and the port on the backend instance. You can specify multiple target ports. This field must be in the format `protocol:port:targetport`, such as `TCP:80:8080`. This field is optional.
     * `HEALTH_CHECK_NAME`: the name of the health check resource. This field is optional.
  4. Add the `BackendService` resource to the previously created `Backend` resource in each zone:
         
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

  5. Create an internal `ForwardingRule` resource that defines the virtual IP address (VIP) the service is available at:
         
         gdcloud compute forwarding-rules create FORWARDING_RULE_INTERNAL_NAME \
             --backend-service=BACKEND_SERVICE_NAME \
             --cidr=CIDR \
             --ip-protocol-port=PROTOCOL_PORT \
             --load-balancing-scheme=INTERNAL \
             --project=PROJECT \
             --global
         

Replace the following:

     * `FORWARDING_RULE_INTERNAL_NAME`: the name for the forwarding rule.
     * `CIDR`: the CIDR to use for your forwarding rule. This field is optional. If not specified, an `IPv4/32` CIDR is automatically reserved from the global IP address pool. Specify the name of a `Subnet` resource in the same namespace as this forwarding rule. A `Subnet` resource represents the request and allocation information of a global subnet. For more information on `Subnet` resources, see [Manage subnets](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/manage-subnets).
     * `PROTOCOL_PORT`: the protocol and port to expose on the forwarding rule. This field must be in the format `ip-protocol=TCP:80`. The exposed port must be the same as what the actual application is exposing inside of the VM.
  6. To validate the configured ILB, confirm the `Ready` condition on each of the created objects. Verify the traffic with a `curl` request to the VIP:

     1. To get the assigned VIP, describe the forwarding rule:
            
            gdcloud compute forwarding-rules describe FORWARDING_RULE_INTERNAL_NAME --global
            

     2. Verify the traffic with a `curl` request to the VIP at the port specified in the field in the forwarding rule:
            
            curl http://FORWARDING_RULE_VIP:PORT
            

Replace the following:

     * `FORWARDING_RULE_VIP`: the VIP of the forwarding rule.
     * `PORT`: the port number of the forwarding rule.



###  API 

Create an ILB that targets VM workloads using the KRM API. This ILB targets all of the workloads in the project matching the label defined in the `Backend` object. To create a global ILB using the KRM API, follow these steps:

  1. Create a `Backend` resource to define the endpoints for the ILB. Create `Backend` resources for each zone the VM workloads are placed in:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER apply -f - <<EOF
         apiVersion: networking.gdc.goog/v1
         kind: Backend
         metadata:
           namespace: PROJECT
           name: BACKEND_NAME
         spec:
           endpointsLabels:
             matchLabels:
               app: APP_NAME
         EOF
         

Replace the following:

     * `MANAGEMENT_API_SERVER`: the kubeconfig path of the zonal Management API server's kubeconfig path. For more information, see [Switch to a zonal context](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/access-zones#switch-zonal-context).
     * `PROJECT`: the name of your project.
     * `BACKEND_NAME`: the name of the `Backend` resource.
     * `APP_NAME`: the name of your VM application.

You can use the same `Backend` resource for each zone, or create `Backend` resources with different label sets for each zone.

  2. Define a global health check for the ILB:
         
         kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
         apiVersion: networking.global.gdc.goog/v1
         kind: HealthCheck
         metadata:
           namespace: PROJECT
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

     * `GLOBAL_API_SERVER`: the kubeconfig path of the global API server's kubeconfig path. For more information, see [Switch to a global context](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/access-zones#switch-global-context).
     * `PROJECT`: the name of your project.
     * `HEALTH_CHECK_NAME`: the name of the health check resource, such as `my-health-check`.
     * `PORT`: the port on which to perform the health check. The default value is `80`.
     * `TIMEOUT`: the amount of time in seconds to wait before claiming failure. The default value is `5`.
     * `CHECK_INTERVAL`: the amount of time in seconds from the start of one probe to the start of the next one. The default value is `5`.
     * `HEALTHY_THRESHOLD`: the number of sequential probes that must pass for the endpoint to be considered healthy. The default value is `2`.
     * `UNHEALTHY_THRESHOLD`: the number of sequential probes that must fail for the endpoint to be considered unhealthy. The default value is `2`.
  3. Create a `BackendService` object using the previously created `Backend` resource. Make sure to include the `HealthCheck` resource:
         
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
           

  4. Create an internal `ForwardingRule` resource defining the virtual IP address (VIP) the service is available at.
         
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
     * `CIDR_NAME`: the name of the CIDR to use for your forwarding rule. This field is optional. If not specified, an `IPv4/32` CIDR is automatically reserved from the global IP address pool. Specify the name of a `Subnet` resource in the same namespace as this forwarding rule. A `Subnet` resource represents the request and allocation information of a global subnet. For more information on `Subnet` resources, see [Manage subnets](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/manage-subnets).
     * `PORT`: the port to expose on the forwarding rule. Use the `ports` field to specify an array of L4 ports for which packets are forwarded to the backends configured with this forwarding rule. At least one port must be specified. Use the `port` field to specify a port number. The exposed port must be the same as what the actual application is exposing inside of the container.
     * `PROTOCOL`: the protocol to use for the forwarding rule, such as `TCP`. An entry in the `ports` array must look like the following:
           
           ports:
           - port: 80
             protocol: TCP
           

  5. To validate the configured ILB, confirm the `Ready` condition on each of the created objects. Verify the traffic with a `curl` request to the VIP:

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

Complete the following steps to create a global ELB for your VM workloads.

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
     * `PORT`: the backend port on the VMs behind the load balancer. This value is found in the `.spec.ports[].targetPortfield` field of the manifest for the `Service` resource. This field is optional.

This configuration provides all of the resources inside of projects access to the specified CIDR range.

**Note:** The gdcloud CLI does not support a command for creating a global project network policy, so you must use the KRM API instead.
  2. Create a `Backend` resource in each zone to define the endpoint for the ELB:
         
         gdcloud compute backends create BACKEND_NAME \
           --labels=LABELS \
           --project=PROJECT
         

Replace the following:

     * `BACKEND_NAME`: the name for the backend resource, such as `my-backend`.
     * `LABELS`: a selector defining which endpoints between VMs to use for this backend resource, such as `app=web`.
     * `PROJECT`: the name of your project.

You can use the same `Backend` resource for each zone, or create `Backend` resources with different label sets for each zone.

  3. Define a global health check for the ELB:
         
         gdcloud compute health-checks create tcp HEALTH_CHECK_NAME \
           --check-interval=CHECK_INTERVAL \
           --healthy-threshold=HEALTHY_THRESHOLD \
           --timeout=TIMEOUT \
           --unhealthy-threshold=UNHEALTHY_THRESHOLD \
           --port=PORT \
           --global
         

Replace the following:

     * `HEALTH_CHECK_NAME`: the name for the health check resource, such as `my-health-check`.
     * `CHECK_INTERVAL`: the amount of time in seconds from the start of one probe to the start of the next one. The default value is `5`. This field is optional.
     * `HEALTHY_THRESHOLD`: the time to wait before claiming failure. The default value is `5`. This field is optional.
     * `TIMEOUT`: the amount of time in seconds to wait before claiming failure. The default value is `5`. This field is optional.
     * `UNHEALTHY_THRESHOLD`: the number of sequential probes that must fail for the endpoint to be considered unhealthy. The default value is `2`. This field is optional.
     * `PORT`: the port on which to perform the health check. The default value is `80`. This field is optional.
  4. Create a global `BackendService` resource:
         
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
  5. Add the global `BackendService` resource to the previously created zonal `Backend` resource:
         
         gdcloud compute backend-services add-backend BACKEND_SERVICE_NAME \
           --backend=BACKEND_NAME \
           --backend-zone BACKEND_ZONE \
           --project=PROJECT \
           --global
         

Complete this step for each zonal backend you created previously.

  6. Create an external `ForwardingRule` resource that defines the VIP the service is available at:
         
         gdcloud compute forwarding-rules create FORWARDING_RULE_EXTERNAL_NAME \
           --backend-service=BACKEND_SERVICE_NAME \
           --cidr=CIDR \
           --ip-protocol-port=PROTOCOL_PORT \
           --load-balancing-scheme=EXTERNAL \
           --project=PROJECT \
           --global
         

Replace the following:

     * `FORWARDING_RULE_EXTERNAL_NAME`: the name for the forwarding rule.
     * `CIDR`: the CIDR to use for your forwarding rule. This field is optional. If not specified, an `IPv4/32` CIDR is automatically reserved from the global IP address pool. Specify the name of a `Subnet` resource in the same namespace as this forwarding rule. A `Subnet` resource represents the request and allocation information of a global subnet. For more information on `Subnet` resources, see [Manage subnets](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/manage-subnets).
     * `PROTOCOL_PORT`: the protocol and port to expose on the forwarding rule. This field must be in the format `ip-protocol=TCP:80`. The exposed port must be the same as what the actual application is exposing inside of the VM.
     * `PROJECT`: the name of your project.
  7. To validate the configured ELB, confirm the `Ready` condition on each of the created objects. Verify the traffic with a `curl` request to the VIP:

     1. To get the assigned VIP, describe the forwarding rule:
            
            gdcloud compute forwarding-rules describe FORWARDING_RULE_EXTERNAL_NAME
            

     2. Verify the traffic with a `curl` request to the VIP at the port specified in the `PROTOCOL_PORT` field in the forwarding rule:
            
            curl http://FORWARDING_RULE_VIP:PORT
            

Replace the following:

        * `FORWARDING_RULE_VIP`: the VIP of the forwarding rule.
        * `PORT`: the port number from the `PROTOCOL_PORT` field in the forwarding rule.



### API

Create an ELB that targets VM workloads using the KRM API. This ELB targets all of the workloads in the project matching the label defined in the `Backend` object. To create a zonal ELB using the KRM API, follow these steps:

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
     * `PORT`: the backend port on the VMs behind the load balancer. This value is found in the `.spec.ports[].targetPortfield` field of the manifest for the `Service` resource. This field is optional.
**Note:** This configuration provides all of the resources inside of projects access to the specified CIDR range.
  2. Create a `Backend` resource to define the endpoints for the ELB. Create `Backend` resources for each zone the workloads are placed in:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER apply -f - <<EOF
         apiVersion: networking.gdc.goog/v1
         kind: Backend
         metadata:
           namespace: PROJECT
           name: BACKEND_NAME
         spec:
           endpointsLabels:
             matchLabels:
               app: server
         EOF
         

Replace the following:

     * `MANAGEMENT_API_SERVER`: the kubeconfig path of the zonal Management API server's kubeconfig path. If you have not yet generated a kubeconfig file for the API server in your targeted zone, see [Manually generate kubeconfig file](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#generate-kubeconfig-file) for details.
     * `PROJECT`: the name of your project.
     * `BACKEND_NAME`: the name of the `Backend` resource.

You can use the same `Backend` resource for each zone, or create `Backend` resources with different label sets for each zone.

  3. Define a global health check for the ELB:
         
         kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
         apiVersion: networking.global.gdc.goog/v1
         kind: HealthCheck
         metadata:
           namespace: PROJECT
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

     * `HEALTH_CHECK_NAME`: the name for the health check resource, such as `my-health-check`.
     * `PORT`: the port on which to perform the health check. The default value is `80`.
     * `TIMEOUT`: the amount of time in seconds to wait before claiming failure. The default value is `5`.
     * `CHECK_INTERVAL`: the amount of time in seconds from the start of one probe to the start of the next one. The default value is `5`.
     * `HEALTHY_THRESHOLD`: the number of sequential probes that must pass for the endpoint to be considered healthy. The default value is `2`.
     * `UNHEALTHY_THRESHOLD`: the number of sequential probes that must fail for the endpoint to be considered unhealthy. The default value is `2`.

Since this is a global ELB, create the health check in the global API.

  4. Create a `BackendService` object using the previously created `Backend` resource:
         
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
    

  5. Create an external `ForwardingRule` resource defining the VIP the service is available at.
         
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
     * `CIDR_NAME`: the name of the CIDR to use for your forwarding rule. This field is optional. If not specified, an `IPv4/32` CIDR is automatically reserved from the global IP address pool. Specify the name of a `Subnet` resource in the same namespace as this forwarding rule. A `Subnet` resource represents the request and allocation information of a global subnet. For more information on `Subnet` resources, see [Manage subnets](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/manage-subnets).
     * `PORT`: the port to expose on the forwarding rule. Use the `ports` field to specify an array of L4 ports for which packets are forwarded to the backends configured with this forwarding rule. At least one port must be specified. Use the `port` field to specify a port number. The exposed port must be the same as what the actual application is exposing inside of the container.
     * `PROTOCOL`: the protocol to use for the forwarding rule, such as `TCP`. An entry in the `ports` array must look like the following:
    
    ports:
    - port: 80
      protocol: TCP
    

  6. To validate the configured ELB, confirm the `Ready` condition on each of the created objects. Try and test the traffic with a `curl` request to the VIP.

     1. Retrieve the VIP for the project:
            
            kubectl get forwardingruleexternal -n PROJECT
            

The output looks like the following:
            
            NAME           BACKENDSERVICE                  CIDR              READY
            elb-name       BACKEND_SERVICE_NAME            192.0.2.0/32      True
            

     2. Verify the traffic with a curl request to the VIP at the port specified in the `PORT` field in the forwarding rule:
            
            curl http://FORWARDING_RULE_VIP:PORT
            

Replace `FORWARDING_RULE_VIP:PORT` with the VIP and port of the forwarding rule, such as `192.0.2.0:80`.




## Configure storage replication

GDC multi-zone universes support storage replication for disaster recovery. This strategy provides data replication between any two zones in the same region, ensuring that your application data remains accessible even if a zone becomes unavailable.

Choose one of the following storage replication types for your VM application:

  * Object replication
  * Asynchronous block replication



### Create a dual-zone bucket for object storage

Object storage data is written to a single bucket whose data is stored in both zones. Unlike volume replication, replicated buckets are writable during zone partitions. Each write to an object produces a different version, and the latest version across either zone will be the final state after connectivity is restored.

  1. Verify with your Infrastructure Operator (IO) that all zones in the universe are online and reachable.

  2. Verify your Infrastructure Operator (IO) has created the `BucketLocationConfig` custom resource, which is required for replication across zones for object storage. This resource must be deployed to the root global API server.

  3. Create the dual-zone `Bucket` custom resource:
         
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

You must deploy a `VolumeReplicationRelationship` custom resource to the global API server to create replicated data that is available for failover if the source zone data becomes unavailable.

Before beginning, verify that your Infrastructure Operator (IO) has created and configured the `StorageClusterPeering` and `StorageVirtualMachinePeering` custom resources to allow for block storage replication across zones. This resource must be deployed to the root global API server.

###  gdcloud 

  1. Set the asynchronous replication volume relationship between the primary zone and secondary zones:
         
         gdcloud compute disks start-async-replication PRIMARY_DISK_NAME \
             --project PROJECT \
             --zone PRIMARY_ZONE \
             --secondary-disk SECONDARY_DISK_NAME \
             --secondary-zone SECONDARY_ZONE
         

Replace the following:

     * `PRIMARY_DISK_NAME`: the name of the source disk being replicated.
     * `PROJECT`: the GDC project of the primary disk.
     * `PRIMARY_ZONE`: the zone where the primary disk resides.
     * `SECONDARY_DISK_NAME`: the name of the destination disk to replicate to.
     * `SECONDARY_ZONE`: the zone where the secondary disk must reside.
  2. Create a `VolumeFailover` custom resource in the destination zone, which stops replication to the destination zone if the source zone is unavailable for any reason:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER apply -f - <<EOF
         apiVersion: storage.gdc.goog/v1
         kind: VolumeFailover
         metadata:
           name: FAILOVER_NAME
           namespace: PROJECT
         spec:
           volumeReplicationRelationshipRef: REPL_NAME
         EOF
         

Replace the following:

     * `MANAGEMENT_API_SERVER`: the kubeconfig file for the Management API server.
     * `FAILOVER_NAME`: the name of the failover.
     * `PROJECT`: the project where the storage infrastructure resides.
     * `REPL_NAME`: the name of the volume replication relationship.
**Note:** The gdcloud CLI does not support volume failover creation, so you must create it using the kubectl CLI.

For more information on managing asynchronous replication for VM workloads, see [Replicate volumes asynchronously](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/async-block-replication).




###  API 

  1. Create a `VolumeReplicationRelationship` custom resource YAML file and deploy it to the global API server:
         
         kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
         apiVersion: storage.global.gdc.goog/v1
         kind: VolumeReplicationRelationship
         metadata:
           name: VRR_NAME
           namespace: PROJECT
         spec:
           source:
             virtualMachineDisk:
               virtualMachineDiskRef: PRIMARY_DISK_NAME
             zoneRef: PRIMARY_ZONE
           destination:
             volumeOverrideName: SECONDARY_DISK_NAME
             zoneRef: SECONDARY_ZONE
         EOF
         

Replace the following:

     * `GLOBAL_API_SERVER`: the kubeconfig file for the global management API server.
     * `VRR_NAME`: the name of the volume replication relationship. The same name must be used when stopping asynchronous replication.
     * `PROJECT`: the GDC project of the primary disk.
     * `PRIMARY_DISK_NAME`: the name of the source disk being replicated.
     * `PRIMARY_ZONE`: the zone where the primary disk resides.
     * `SECONDARY_DISK_NAME`: the name of the destination disk to replicate to.
     * `SECONDARY_ZONE`: the zone where the secondary disk must reside.
  2. Create a `VolumeFailover` custom resource in the destination zone, which stops replication to the destination zone if the source zone is unavailable for any reason:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER apply -f - <<EOF
         apiVersion: storage.gdc.goog/v1
         kind: VolumeFailover
         metadata:
           name: FAILOVER_NAME
           namespace: PROJECT
         spec:
           volumeReplicationRelationshipRef: REPL_NAME
         EOF
         

Replace the following:

     * `MANAGEMENT_API_SERVER`: the kubeconfig file for the Management API server.
     * `FAILOVER_NAME`: the name of the failover.
     * `PROJECT`: the project where the storage infrastructure resides.
     * `REPL_NAME`: the name of the volume replication relationship.



For more information on managing asynchronous replication for VM workloads, see [Replicate volumes asynchronously](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/async-block-replication).

## What's next

  * [VMs overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/vm-introduction)
  * [Multi-zone overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/mz-overview)
  * [Design access boundaries](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/access-boundaries)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
