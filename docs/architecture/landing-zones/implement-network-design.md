---
url: https://docs.cloud.google.com/architecture/landing-zones/implement-network-design/
title: Implement your Google Cloud landing zone network design \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:25:39.235904+00:00
---

# Implement your Google Cloud landing zone network design  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/landing-zones/implement-network-design/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Implement your Google Cloud landing zone network design Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-01-02 UTC

This document provides steps and guidance to implement your chosen network design after you review [Decide the network design for your Google Cloud landing zone](https://docs.cloud.google.com/architecture/landing-zones/decide-network-design). If you have not already done so, review [Landing zone design in Google Cloud](https://docs.cloud.google.com/architecture/landing-zones) before you choose an option.

These instructions are intended for network engineers, architects, and technical practitioners who are involved in creating the network design for your organization's landing zone.

## Network design options

Based on your chosen network design, complete one of the following:

  * Create option 1: Shared VPC network for each environment
  * Create option 2: Hub-and-spoke topology with centralized appliances
  * Create option 3: Hub-and-spoke topology without appliances
  * Create option 4: Expose services in a consumer-producer model with Private Service Connect



## Create option 1: Shared VPC network for each environment

If you have chosen to create the [Shared VPC network for each environment](https://docs.cloud.google.com/architecture/landing-zones/decide-network-design#option-1) in "Decide the network design for your Google Cloud landing zone", follow this procedure.

The following steps create a single instance of a VPC. When you need multiple instances of a VPC, such as for development and production environments, repeat the steps for each VPC.

### Limit external access by using an organization policy

We recommend that you limit direct access to the internet to only the resources that need it. Resources without external addresses can still access many Google APIs and services through Private Google Access. Private Google Access is enabled at the subnet level and lets resources interact with key Google services, while isolating them from the public internet.

For usability, the default functionality of Google Cloud lets users create resources in all projects, as long as they have the correct IAM permissions. For improved security, we recommend that you restrict the default permissions for resource types that can cause unintended internet access. You can then authorize specific projects only to allow the creation of these resources. Use the instructions at [Creating and managing organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies) to set the following constraints.

#### Restrict Protocol Forwarding Based on type of IP Address

Protocol forwarding establishes a forwarding rule resource with an external IP address and lets you direct the traffic to a VM.

The **Restrict Protocol Forwarding Based on type of IP Address** constraint prevents the creation of forwarding rules with external IP addresses for the entire organization. For projects authorized to use external forwarding rules, you can modify the constraint at the folder or project level.

Set the following values to configure this constraint:

  * _Applies to:_ Customize
  * _Policy enforcement:_ Replace
  * _Policy values:_ Custom
  * _Policy type:_ Deny
  * _Custom value:_ `IS:EXTERNAL`



#### Define allowed external IPs for VM instances

By default, individual VM instances can acquire external IP addresses, which allows both outbound and inbound connectivity with the internet.

Enforcing the **Define allowed external IPs for VM instances** constraint prevents the use of external IP addresses with VM instances. For workloads that require external IP addresses on individual VM instances, modify the constraint at a folder or project level to specify the individual VM instances. Or, override the constraint for the relevant projects.

  * _Applies to:_ Customize
  * _Policy enforcement:_ Replace
  * _Policy values:_ Deny All



#### Disable VPC External IPv6 usage

The **Disable VPC External IPv6 usage** constraint, when set to `True`, prevents the configuration of VPC subnets with external IPv6 addresses for VM instances.

  * _Applies to:_ Customize
  * _Enforcement:_ On



#### Disable default network creation

When a new project is created, a default VPC is automatically created. This is useful for quick experiments that don't require specific network configuration or integration with a larger enterprise networking environment.

Configure the **Skip default network creation** constraint to disable default VPC creation for new projects. You can manually create the default network within a project, if needed.

  * _Applies to:_ Customize
  * _Enforcement:_ On



### Design firewall rules

Firewall rules let you allow or deny traffic to or from your VMs based on a configuration you define. [Hierarchical firewall policies](https://docs.cloud.google.com/vpc/docs/firewall-policies) are implemented at the organization and folder levels, and network firewall policies are implemented at the VPC network level in the resource hierarchy. Together, these provide an important capability to help secure your workloads.

Regardless of where the firewall policies are applied, use the following guidelines when designing and evaluating your firewall rules:

  * Implement least-privilege (also referred to as microsegmentation) principles. Block all traffic by default and only allow the specific traffic you need. This includes limiting the rules to only the protocols and ports you need for each workload.
  * Enable firewall rules logging for visibility into firewall behavior and to use Firewall Insights.
  * Define a numbering methodology for allocating firewall rule priorities. For example, it's best practice to reserve a range of low numbers in each policy for rules needed during incident response. We also recommend that you prioritize more specific rules higher than more general rules, to ensure that the specific rules aren't shadowed by the general rules. The following example shows a possible approach for firewall rule priorities:

  
Firewall rule priority range |   
Purpose  
---|---  
  
0-999 |   
Reserved for incident response  
  
1000-1999 |   
Always blocked traffic  
  
2000-1999999999 |   
Workload-specific rules  
  
2000000000-2100000000 |   
Catch-all rules  
  
2100000001-2147483643 |   
Reserved  
  
#### Configure hierarchical firewall policies

[Hierarchical firewall policies](https://docs.cloud.google.com/vpc/docs/firewall-policies) let you create and enforce a consistent firewall policy across your organization. For examples of using hierarchical firewall policies, see [Hierarchical firewall policy examples](https://docs.cloud.google.com/vpc/docs/firewall-policies-examples).

Define hierarchical firewall policies to implement the following network access controls:

  * **Identity-Aware Proxy (IAP) for TCP forwarding.** IAP for TCP forwarding is allowed through a security policy that permits ingress traffic from IP range 35.235.240.0/20 for TCP ports 22 and 3389.
  * **Health checks for Cloud Load Balancing.** The well-known ranges that are used for health checks are allowed. 
    * For most Cloud Load Balancing instances (including Internal TCP/UDP Load Balancing, Internal HTTP(S) Load Balancing, External TCP Proxy Load Balancing, External SSL Proxy Load Balancing, and HTTP(S) Load Balancing), a security policy is defined that allows ingress traffic from the IP ranges 35.191.0.0/16 and 130.211.0.0/22 for ports 80 and 443.
    * For Network Load Balancing, a security policy is defined that enables legacy health checks by allowing ingress traffic from IP ranges 35.191.0.0/16, 209.85.152.0/22, and 209.85.204.0/22 for ports 80 and 443.



### Configure your Shared VPC environment

Before implementing a Shared VPC design, decide how to share subnets with service projects. You attach a service project to a host project. To determine which subnets are available for the service project, you assign IAM permissions to the host project or individual subnets. For example, you can choose to dedicate a different subnet to each service project, or share the same subnets between service projects.

  1. [Create a new project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) for the Shared VPC. Later in this process, this project becomes the host project and contains the networks and networking resources to be shared with the service projects.
  2. [Enable the Compute Engine API](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api) for the host project.
  3. [Configure Shared VPC](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc) for the project.
  4. Create the [custom-mode VPC network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#creating_networks) in the host project.
  5. [Create subnets](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#subnet-rules) in the [region](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) where you plan to deploy workloads. For each subnet, enable Private Google Access to allow VM instances without external IP addresses to reach Google services.



### Configure Cloud NAT

Follow these steps if the workloads in specific regions require outbound internet access—for example, to download software packages or updates.

  1. [Create a Cloud NAT gateway](https://docs.cloud.google.com/nat/docs/set-up-manage-network-address-translation) in the [regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) where workloads require outbound internet access. You can customize the Cloud NAT configuration to only allow outbound connectivity from specific subnets, if needed.
  2. At a minimum, [enable Cloud NAT logging](https://docs.cloud.google.com/nat/docs/monitoring) for the gateway to log `ERRORS_ONLY`. To include logs for translations performed by Cloud NAT, configure each gateway to log `ALL`.



### Configure hybrid connectivity

You can use Dedicated Interconnect, Partner Interconnect, or Cloud VPN to provide hybrid connectivity to your landing zone. The following steps create the initial hybrid connectivity resources required for this design option: 

  1. If you're using Dedicated Interconnect, do the following. If you're using Partner Interconnect or Cloud VPN, you can skip these steps. 
     1. Create a [separate project for the physical interconnect ports](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/best-practices#provision_physical_interconnect_connections_in_a_separate_project).
     2. [Enable the Compute Engine API](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api) for the project.
     3. [Create Dedicated Interconnect connections](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/provisioning-overview).
  2. For each [region](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) where you're terminating hybrid connectivity in the VPC network, do the following: 
     1. Create two Dedicated or Partner [VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments), one for each edge availability zone. As part of this process, you select Cloud Routers and create BGP sessions.
     2. Configure the peer network (on-premises or other cloud) routers. 



### Configure workload projects

Create a separate service project for each workload:

  1. [Create a new project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) to function as one of the service projects for the Shared VPC.
  2. [Enable the Compute Engine API](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api) for the service project.
  3. [Attach the project to the host project](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#create-shared).
  4. Configure access to [all subnets in the host project](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#networkuseratproject) or [some subnets in the host project](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#networkuseratsubnet).



### Configure observability

Network Intelligence Center provides a cohesive way to monitor, troubleshoot, and visualize your cloud networking environment. Use it to ensure that your design functions with the desired intent.

The following configurations support the analysis of logging and metrics enabled.

  * You must [enable the Network Management API](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview) before you can run Connectivity Tests. Enabling the API is required to use the API directly, the Google Cloud CLI, or the Google Cloud console.
  * You must [enable the Firewall Insights API](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/enable-api-features) before you can perform any tasks using Firewall Insights.



### Next steps

The initial configuration for this network design option is now complete. You can now either repeat these steps to configure an additional instance of the landing zone environment, such as a staging or production environment, or continue to [Decide the security for your Google Cloud landing zone](https://docs.cloud.google.com/architecture/landing-zones/decide-security).

## Create option 2: Hub-and-spoke topology with centralized appliances

If you have chosen to create the [hub-and-spoke topology with centralized appliances](https://docs.cloud.google.com/architecture/landing-zones/decide-network-design#option-2) in "Decide the network design for your Google Cloud landing zone", follow this procedure.

The following steps create a single instance of a VPC. When you need multiple instances of a VPC, such as for development and production environments, repeat the steps for each VPC.

### Limit external access by using an organization policy

We recommend that you limit direct access to the internet to only the resources that need it. Resources without external addresses can still access many Google APIs and services through Private Google Access. Private Google Access is enabled at the subnet level and lets resources interact with key Google services, while isolating them from the public internet.

For usability, the default functionality of Google Cloud lets users create resources in all projects, as long as they have the correct IAM permissions. For improved security, we recommend that you restrict the default permissions for resource types that can cause unintended internet access. You can then authorize specific projects only to allow the creation of these resources. Use the instructions at [Creating and managing organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies) to set the following constraints.

#### Restrict Protocol Forwarding Based on type of IP Address

Protocol forwarding establishes a forwarding rule resource with an external IP address and lets you direct the traffic to a VM.

The **Restrict Protocol Forwarding Based on type of IP Address** constraint prevents the creation of forwarding rules with external IP addresses for the entire organization. For projects authorized to use external forwarding rules, you can modify the constraint at the folder or project level.

Set the following values to configure this constraint:

  * _Applies to:_ Customize
  * _Policy enforcement:_ Replace
  * _Policy values:_ Custom
  * _Policy type:_ Deny
  * _Custom value:_ `IS:EXTERNAL`



#### Define allowed external IPs for VM instances

By default, individual VM instances can acquire external IP addresses, which allows both outbound and inbound connectivity with the internet.

Enforcing the **Define allowed external IPs for VM instances** constraint prevents the use of external IP addresses with VM instances. For workloads that require external IP addresses on individual VM instances, modify the constraint at a folder or project level to specify the individual VM instances. Or, override the constraint for the relevant projects.

  * _Applies to:_ Customize
  * _Policy enforcement:_ Replace
  * _Policy values:_ Deny All



#### Disable VPC External IPv6 usage

The **Disable VPC External IPv6 usage** constraint, when set to `True`, prevents the configuration of VPC subnets with external IPv6 addresses for VM instances.

  * _Applies to:_ Customize
  * _Enforcement:_ On



#### Disable default network creation

When a new project is created, a default VPC is automatically created. This is useful for quick experiments that don't require specific network configuration or integration with a larger enterprise networking environment.

Configure the **Skip default network creation** constraint to disable default VPC creation for new projects. You can manually create the default network within a project, if needed.

  * _Applies to:_ Customize
  * _Enforcement:_ On



### Design firewall rules

Firewall rules let you allow or deny traffic to or from your VMs based on a configuration you define. [Hierarchical firewall policies](https://docs.cloud.google.com/vpc/docs/firewall-policies) are implemented at the organization and folder levels, and network firewall policies are implemented at the VPC network level in the resource hierarchy. Together, these provide an important capability to help secure your workloads.

Regardless of where the firewall policies are applied, use the following guidelines when designing and evaluating your firewall rules:

  * Implement least-privilege (also referred to as microsegmentation) principles. Block all traffic by default and only allow the specific traffic you need. This includes limiting the rules to only the protocols and ports you need for each workload.
  * Enable firewall rules logging for visibility into firewall behavior and to use Firewall Insights.
  * Define a numbering methodology for allocating firewall rule priorities. For example, it's best practice to reserve a range of low numbers in each policy for rules needed during incident response. We also recommend that you prioritize more specific rules higher than more general rules, to ensure that the specific rules aren't shadowed by the general rules. The following example shows a possible approach for firewall rule priorities:

  
Firewall rule priority range |   
Purpose  
---|---  
  
0-999 |   
Reserved for incident response  
  
1000-1999 |   
Always blocked traffic  
  
2000-1999999999 |   
Workload-specific rules  
  
2000000000-2100000000 |   
Catch-all rules  
  
2100000001-2147483643 |   
Reserved  
  
#### Configure hierarchical firewall policies

[Hierarchical firewall policies](https://docs.cloud.google.com/vpc/docs/firewall-policies) let you create and enforce a consistent firewall policy across your organization. For examples of using hierarchical firewall policies, see [Hierarchical firewall policy examples](https://docs.cloud.google.com/vpc/docs/firewall-policies-examples).

Define hierarchical firewall policies to implement the following network access controls:

  * **Identity-Aware Proxy (IAP) for TCP forwarding.** IAP for TCP forwarding is allowed through a security policy that permits ingress traffic from IP range 35.235.240.0/20 for TCP ports 22 and 3389.
  * **Health checks for Cloud Load Balancing.** The well-known ranges that are used for health checks are allowed. 
    * For most Cloud Load Balancing instances (including Internal TCP/UDP Load Balancing, Internal HTTP(S) Load Balancing, External TCP Proxy Load Balancing, External SSL Proxy Load Balancing, and HTTP(S) Load Balancing), a security policy is defined that allows ingress traffic from the IP ranges 35.191.0.0/16 and 130.211.0.0/22 for ports 80 and 443.
    * For Network Load Balancing, a security policy is defined that enables legacy health checks by allowing ingress traffic from IP ranges 35.191.0.0/16, 209.85.152.0/22, and 209.85.204.0/22 for ports 80 and 443.



### Configure your VPC environment

The transit and hub VPC networks provide the networking resources to enable connectivity between workload spoke VPC networks and on-premises or multi-cloud networks.

  1. [Create a new project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) for transit and hub VPC networks. Both VPC networks are part of the same project to support connectivity through the virtual network appliances.
  2. [Enable the Compute Engine API](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api) for the project.
  3. [Create the transit custom mode VPC network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#creating_networks).
  4. In the transit VPC network, [create a subnet](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#subnet-rules) in the regions where you plan to deploy the virtual network appliances.
  5. [Create the hub custom mode VPC network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#creating_networks).
  6. In the hub VPC network, [create a subnet](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#subnet-rules) in the regions where you plan to deploy the virtual network appliances.
  7. Configure [global or regional network firewall policies](https://docs.cloud.google.com/vpc/docs/firewall-policies-overview) to allow ingress and egress traffic for the network virtual appliances.
  8. [Create a managed instance group](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances) for the virtual network appliances.
  9. [Configure the internal TCP/UDP load balancing resources](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal) for the transit VPC. This load balancer is used for routing traffic from the transit VPC to the hub VPC through the virtual network appliances.
  10. [Configure the internal TCP/UDP load balancing resources](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-ilb-next-hop) for the hub VPC. This load balancer is used for routing traffic from the hub VPC to the transit VPC through the virtual network appliances.
  11. [Configure Private Service Connect for Google APIs](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-apis) for the hub VPC.
  12. [Modify VPC routes](https://docs.cloud.google.com/vpc/docs/using-routes#adding_and_removing_routes) to send all traffic through the network virtual appliances: 
     1. Delete the `0.0.0.0/0` route with next-hop `default-internet-gateway` from the hub VPC.
     2. Configure a new route with destination `0.0.0.0/0` and a next-hop of the forwarding rule for the load balancer in the hub VPC.



### Configure Cloud NAT

Follow these steps if the workloads in specific regions require outbound internet access—for example, to download software packages or updates.

  1. [Create a Cloud NAT gateway](https://docs.cloud.google.com/nat/docs/set-up-manage-network-address-translation) in the [regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) where workloads require outbound internet access. You can customize the Cloud NAT configuration to only allow outbound connectivity from specific subnets, if needed.
  2. At a minimum, [enable Cloud NAT logging](https://docs.cloud.google.com/nat/docs/monitoring) for the gateway to log `ERRORS_ONLY`. To include logs for translations performed by Cloud NAT, configure each gateway to log `ALL`.



### Configure hybrid connectivity

You can use Dedicated Interconnect, Partner Interconnect, or Cloud VPN to provide hybrid connectivity to your landing zone. The following steps create the initial hybrid connectivity resources required for this design option: 

  1. If you're using Dedicated Interconnect, do the following. If you're using Partner Interconnect or Cloud VPN, you can skip these steps. 
     1. Create a [separate project for the physical interconnect ports](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/best-practices#provision_physical_interconnect_connections_in_a_separate_project).
     2. [Enable the Compute Engine API](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api) for the project.
     3. [Create Dedicated Interconnect connections](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/provisioning-overview).
  2. For each [region](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) where you're terminating hybrid connectivity in the VPC network, do the following: 
     1. Create two Dedicated or Partner [VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments), one for each edge availability zone. As part of this process, you select Cloud Routers and create BGP sessions.
     2. Configure the peer network (on-premises or other cloud) routers. 
     3. Configure custom advertised routes in the Cloud Routers for the subnet ranges in the hub and workload VPCs. 



### Configure workload projects

Create a separate spoke VPC for each workload:

  1. [Create a new project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) to host your workload.
  2. [Enable the Compute Engine API](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api) for the project.
  3. [Configure VPC Network Peering](https://docs.cloud.google.com/vpc/docs/using-vpc-peering) between the workload spoke VPC and hub VPC with the following settings: 
     * Enable custom route export on the hub VPC.
     * Enable custom route import on the workload spoke VPC.
  4. [Create subnets](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#subnet-rules) in the regions where you plan to deploy workloads. For each subnet, enable Private Google Access to allow VM instances with _only_ internal IP addresses to reach Google services.
  5. [Configure Private Service Connect for Google APIs](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-apis).
  6. To route all traffic through the virtual network appliances in the hub VPC, delete the `0.0.0.0/0` route with next-hop `default-internet-gateway` from the workload spoke VPC.
  7. Configure [global or regional network firewall policies](https://docs.cloud.google.com/vpc/docs/firewall-policies-overview) to allow ingress and egress traffic for your workload.



### Configure observability

Network Intelligence Center provides a cohesive way to monitor, troubleshoot, and visualize your cloud networking environment. Use it to ensure that your design functions with the desired intent.

The following configurations support the analysis of logging and metrics enabled.

  * You must [enable the Network Management API](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview) before you can run Connectivity Tests. Enabling the API is required to use the API directly, the Google Cloud CLI, or the Google Cloud console.
  * You must [enable the Firewall Insights API](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/enable-api-features) before you can perform any tasks using Firewall Insights.



### Next steps

The initial configuration for this network design option is now complete. You can now either repeat these steps to configure an additional instance of the landing zone environment, such as a staging or production environment, or continue to [Decide the security for your Google Cloud landing zone](https://docs.cloud.google.com/architecture/landing-zones/decide-security).

## Create option 3: Hub-and-spoke topology without appliances

If you have chosen to create the [hub-and-spoke topology without appliances](https://docs.cloud.google.com/architecture/landing-zones/decide-network-design#option-3) in "Decide the network design for your Google Cloud landing zone", follow this procedure.

The following steps create a single instance of a VPC. When you need multiple instances of a VPC, such as for development and production environments, repeat the steps for each VPC.

### Limit external access by using an organization policy

We recommend that you limit direct access to the internet to only the resources that need it. Resources without external addresses can still access many Google APIs and services through Private Google Access. Private Google Access is enabled at the subnet level and lets resources interact with key Google services, while isolating them from the public internet.

For usability, the default functionality of Google Cloud lets users create resources in all projects, as long as they have the correct IAM permissions. For improved security, we recommend that you restrict the default permissions for resource types that can cause unintended internet access. You can then authorize specific projects only to allow the creation of these resources. Use the instructions at [Creating and managing organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies) to set the following constraints.

#### Restrict Protocol Forwarding Based on type of IP Address

Protocol forwarding establishes a forwarding rule resource with an external IP address and lets you direct the traffic to a VM.

The **Restrict Protocol Forwarding Based on type of IP Address** constraint prevents the creation of forwarding rules with external IP addresses for the entire organization. For projects authorized to use external forwarding rules, you can modify the constraint at the folder or project level.

Set the following values to configure this constraint:

  * _Applies to:_ Customize
  * _Policy enforcement:_ Replace
  * _Policy values:_ Custom
  * _Policy type:_ Deny
  * _Custom value:_ `IS:EXTERNAL`



#### Define allowed external IPs for VM instances

By default, individual VM instances can acquire external IP addresses, which allows both outbound and inbound connectivity with the internet.

Enforcing the **Define allowed external IPs for VM instances** constraint prevents the use of external IP addresses with VM instances. For workloads that require external IP addresses on individual VM instances, modify the constraint at a folder or project level to specify the individual VM instances. Or, override the constraint for the relevant projects.

  * _Applies to:_ Customize
  * _Policy enforcement:_ Replace
  * _Policy values:_ Deny All



#### Disable VPC External IPv6 usage

The **Disable VPC External IPv6 usage** constraint, when set to `True`, prevents the configuration of VPC subnets with external IPv6 addresses for VM instances.

  * _Applies to:_ Customize
  * _Enforcement:_ On



#### Disable default network creation

When a new project is created, a default VPC is automatically created. This is useful for quick experiments that don't require specific network configuration or integration with a larger enterprise networking environment.

Configure the **Skip default network creation** constraint to disable default VPC creation for new projects. You can manually create the default network within a project, if needed.

  * _Applies to:_ Customize
  * _Enforcement:_ On



### Design firewall rules

Firewall rules let you allow or deny traffic to or from your VMs based on a configuration you define. [Hierarchical firewall policies](https://docs.cloud.google.com/vpc/docs/firewall-policies) are implemented at the organization and folder levels, and network firewall policies are implemented at the VPC network level in the resource hierarchy. Together, these provide an important capability to help secure your workloads.

Regardless of where the firewall policies are applied, use the following guidelines when designing and evaluating your firewall rules:

  * Implement least-privilege (also referred to as microsegmentation) principles. Block all traffic by default and only allow the specific traffic you need. This includes limiting the rules to only the protocols and ports you need for each workload.
  * Enable firewall rules logging for visibility into firewall behavior and to use Firewall Insights.
  * Define a numbering methodology for allocating firewall rule priorities. For example, it's best practice to reserve a range of low numbers in each policy for rules needed during incident response. We also recommend that you prioritize more specific rules higher than more general rules, to ensure that the specific rules aren't shadowed by the general rules. The following example shows a possible approach for firewall rule priorities:

  
Firewall rule priority range |   
Purpose  
---|---  
  
0-999 |   
Reserved for incident response  
  
1000-1999 |   
Always blocked traffic  
  
2000-1999999999 |   
Workload-specific rules  
  
2000000000-2100000000 |   
Catch-all rules  
  
2100000001-2147483643 |   
Reserved  
  
#### Configure hierarchical firewall policies

[Hierarchical firewall policies](https://docs.cloud.google.com/vpc/docs/firewall-policies) let you create and enforce a consistent firewall policy across your organization. For examples of using hierarchical firewall policies, see [Hierarchical firewall policy examples](https://docs.cloud.google.com/vpc/docs/firewall-policies-examples).

Define hierarchical firewall policies to implement the following network access controls:

  * **Identity-Aware Proxy (IAP) for TCP forwarding.** IAP for TCP forwarding is allowed through a security policy that permits ingress traffic from IP range 35.235.240.0/20 for TCP ports 22 and 3389.
  * **Health checks for Cloud Load Balancing.** The well-known ranges that are used for health checks are allowed. 
    * For most Cloud Load Balancing instances (including Internal TCP/UDP Load Balancing, Internal HTTP(S) Load Balancing, External TCP Proxy Load Balancing, External SSL Proxy Load Balancing, and HTTP(S) Load Balancing), a security policy is defined that allows ingress traffic from the IP ranges 35.191.0.0/16 and 130.211.0.0/22 for ports 80 and 443.
    * For Network Load Balancing, a security policy is defined that enables legacy health checks by allowing ingress traffic from IP ranges 35.191.0.0/16, 209.85.152.0/22, and 209.85.204.0/22 for ports 80 and 443.



### Configure the hub VPC environment

The hub VPC provides the networking resources to enable connectivity between workload spoke VPC networks and on-premises or multi-cloud networks.

  1. [Create a new project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) for the hub VPC network.
  2. [Enable the Compute Engine API](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api) for the project.
  3. Create the hub [custom mode VPC network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#creating_networks).
  4. [Configure Private Service Connect for Google APIs](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-apis) for the hub VPC.



### Configure hybrid connectivity

You can use Dedicated Interconnect, Partner Interconnect, or Cloud VPN to provide hybrid connectivity to your landing zone. The following steps create the initial hybrid connectivity resources required for this design option: 

  1. If you're using Dedicated Interconnect, do the following. If you're using Partner Interconnect or Cloud VPN, you can skip these steps. 
     1. Create a [separate project for the physical interconnect ports](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/best-practices#provision_physical_interconnect_connections_in_a_separate_project).
     2. [Enable the Compute Engine API](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api) for the project.
     3. [Create Dedicated Interconnect connections](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/provisioning-overview).
  2. For each [region](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) where you're terminating hybrid connectivity in the VPC network, do the following: 
     1. Create two Dedicated or Partner [VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments), one for each edge availability zone. As part of this process, you select Cloud Routers and create BGP sessions.
     2. Configure the peer network (on-premises or other cloud) routers. 
     3. Configure custom advertised routes in the Cloud Routers for the subnet ranges in the hub and workload VPCs. 



### Configure workload projects

Create a separate spoke VPC for each workload:

  1. [Create a new project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) to host your workload.
  2. [Enable the Compute Engine API](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api) for the project.
  3. [Configure VPC Network Peering](https://docs.cloud.google.com/vpc/docs/using-vpc-peering) between the workload spoke VPC and hub VPC, with the following settings: 
     * Enable custom route export on the hub VPC.
     * Enable custom route import on the workload spoke VPC.
  4. [Create subnets](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#subnet-rules) in the regions where you plan to deploy workloads. For each subnet, enable Private Google Access to allow VM instances with _only_ internal IP addresses to reach Google services.
  5. [Configure Private Service Connect for Google APIs](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-apis).



### Configure Cloud NAT

Follow these steps if the workloads in specific regions require outbound internet access—for example, to download software packages or updates.

  1. [Create a Cloud NAT gateway](https://docs.cloud.google.com/nat/docs/set-up-manage-network-address-translation) in the [regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) where workloads require outbound internet access. You can customize the Cloud NAT configuration to only allow outbound connectivity from specific subnets, if needed.
  2. At a minimum, [enable Cloud NAT logging](https://docs.cloud.google.com/nat/docs/monitoring) for the gateway to log `ERRORS_ONLY`. To include logs for translations performed by Cloud NAT, configure each gateway to log `ALL`.



### Configure observability

Network Intelligence Center provides a cohesive way to monitor, troubleshoot, and visualize your cloud networking environment. Use it to ensure that your design functions with the desired intent.

The following configurations support the analysis of logging and metrics enabled.

  * You must [enable the Network Management API](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview) before you can run Connectivity Tests. Enabling the API is required to use the API directly, the Google Cloud CLI, or the Google Cloud console.
  * You must [enable the Firewall Insights API](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/enable-api-features) before you can perform any tasks using Firewall Insights.



### Next steps

The initial configuration for this network design option is now complete. You can now either repeat these steps to configure an additional instance of the landing zone environment, such as a staging or production environment, or continue to [Decide the security for your Google Cloud landing zone](https://docs.cloud.google.com/architecture/landing-zones/decide-security).

## Create option 4: Expose services in a consumer-producer model with Private Service Connect

If you have chosen to [expose services in a consumer-producer model with Private Service Connect](https://docs.cloud.google.com/architecture/landing-zones/decide-network-design#option-4) for your landing zone, as described in "Decide the network design for your Google Cloud landing zone", follow this procedure.

The following steps create a single instance of a VPC. When you need multiple instances of a VPC, such as for development and production environments, repeat the steps for each VPC.

### Limit external access by using an organization policy

We recommend that you limit direct access to the internet to only the resources that need it. Resources without external addresses can still access many Google APIs and services through Private Google Access. Private Google Access is enabled at the subnet level and lets resources interact with key Google services, while isolating them from the public internet.

For usability, the default functionality of Google Cloud lets users create resources in all projects, as long as they have the correct IAM permissions. For improved security, we recommend that you restrict the default permissions for resource types that can cause unintended internet access. You can then authorize specific projects only to allow the creation of these resources. Use the instructions at [Creating and managing organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies) to set the following constraints.

#### Restrict Protocol Forwarding Based on type of IP Address

Protocol forwarding establishes a forwarding rule resource with an external IP address and lets you direct the traffic to a VM.

The **Restrict Protocol Forwarding Based on type of IP Address** constraint prevents the creation of forwarding rules with external IP addresses for the entire organization. For projects authorized to use external forwarding rules, you can modify the constraint at the folder or project level.

Set the following values to configure this constraint:

  * _Applies to:_ Customize
  * _Policy enforcement:_ Replace
  * _Policy values:_ Custom
  * _Policy type:_ Deny
  * _Custom value:_ `IS:EXTERNAL`



#### Define allowed external IPs for VM instances

By default, individual VM instances can acquire external IP addresses, which allows both outbound and inbound connectivity with the internet.

Enforcing the **Define allowed external IPs for VM instances** constraint prevents the use of external IP addresses with VM instances. For workloads that require external IP addresses on individual VM instances, modify the constraint at a folder or project level to specify the individual VM instances. Or, override the constraint for the relevant projects.

  * _Applies to:_ Customize
  * _Policy enforcement:_ Replace
  * _Policy values:_ Deny All



#### Disable VPC External IPv6 usage

The **Disable VPC External IPv6 usage** constraint, when set to `True`, prevents the configuration of VPC subnets with external IPv6 addresses for VM instances.

  * _Applies to:_ Customize
  * _Enforcement:_ On



#### Disable default network creation

When a new project is created, a default VPC is automatically created. This is useful for quick experiments that don't require specific network configuration or integration with a larger enterprise networking environment.

Configure the **Skip default network creation** constraint to disable default VPC creation for new projects. You can manually create the default network within a project, if needed.

  * _Applies to:_ Customize
  * _Enforcement:_ On



### Design firewall rules

Firewall rules let you allow or deny traffic to or from your VMs based on a configuration you define. [Hierarchical firewall policies](https://docs.cloud.google.com/vpc/docs/firewall-policies) are implemented at the organization and folder levels, and network firewall policies are implemented at the VPC network level in the resource hierarchy. Together, these provide an important capability to help secure your workloads.

Regardless of where the firewall policies are applied, use the following guidelines when designing and evaluating your firewall rules:

  * Implement least-privilege (also referred to as microsegmentation) principles. Block all traffic by default and only allow the specific traffic you need. This includes limiting the rules to only the protocols and ports you need for each workload.
  * Enable firewall rules logging for visibility into firewall behavior and to use Firewall Insights.
  * Define a numbering methodology for allocating firewall rule priorities. For example, it's best practice to reserve a range of low numbers in each policy for rules needed during incident response. We also recommend that you prioritize more specific rules higher than more general rules, to ensure that the specific rules aren't shadowed by the general rules. The following example shows a possible approach for firewall rule priorities:

  
Firewall rule priority range |   
Purpose  
---|---  
  
0-999 |   
Reserved for incident response  
  
1000-1999 |   
Always blocked traffic  
  
2000-1999999999 |   
Workload-specific rules  
  
2000000000-2100000000 |   
Catch-all rules  
  
2100000001-2147483643 |   
Reserved  
  
#### Configure hierarchical firewall policies

[Hierarchical firewall policies](https://docs.cloud.google.com/vpc/docs/firewall-policies) let you create and enforce a consistent firewall policy across your organization. For examples of using hierarchical firewall policies, see [Hierarchical firewall policy examples](https://docs.cloud.google.com/vpc/docs/firewall-policies-examples).

Define hierarchical firewall policies to implement the following network access controls:

  * **Identity-Aware Proxy (IAP) for TCP forwarding.** IAP for TCP forwarding is allowed through a security policy that permits ingress traffic from IP range 35.235.240.0/20 for TCP ports 22 and 3389.
  * **Health checks for Cloud Load Balancing.** The well-known ranges that are used for health checks are allowed. 
    * For most Cloud Load Balancing instances (including Internal TCP/UDP Load Balancing, Internal HTTP(S) Load Balancing, External TCP Proxy Load Balancing, External SSL Proxy Load Balancing, and HTTP(S) Load Balancing), a security policy is defined that allows ingress traffic from the IP ranges 35.191.0.0/16 and 130.211.0.0/22 for ports 80 and 443.
    * For Network Load Balancing, a security policy is defined that enables legacy health checks by allowing ingress traffic from IP ranges 35.191.0.0/16, 209.85.152.0/22, and 209.85.204.0/22 for ports 80 and 443.



### Configure the VPC environment

The transit VPC provides the networking resources to enable connectivity between workload spoke VPC networks and on-premises or multi-cloud networks.

  1. [Create a new project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) for the transit VPC network.
  2. [Enable the Compute Engine API](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api) for the project.
  3. Create the transit [custom mode VPC network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#creating_networks).
  4. [Create a Private Service Connect subnet ](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer#add-subnet-psc)in each region where you plan to publish services running in your hub VPC or on-premises environment. Consider [Private Service Connect subnet sizing](https://docs.cloud.google.com/vpc/docs/private-service-connect#psc-subnets) when deciding your IP addressing plan.
  5. For each on-premises service you want to expose to workloads running in Google Cloud, create an internal HTTP(S) or TCP proxy load balancer and [expose the services using Private Service Connect](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-hybrid#publish).
  6. [Configure Private Service Connect for Google APIs](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-apis) for the transit VPC.



### Configure hybrid connectivity

You can use Dedicated Interconnect, Partner Interconnect, or Cloud VPN to provide hybrid connectivity to your landing zone. The following steps create the initial hybrid connectivity resources required for this design option: 

  1. If you're using Dedicated Interconnect, do the following. If you're using Partner Interconnect or Cloud VPN, you can skip these steps. 
     1. Create a [separate project for the physical interconnect ports](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/best-practices#provision_physical_interconnect_connections_in_a_separate_project).
     2. [Enable the Compute Engine API](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api) for the project.
     3. [Create Dedicated Interconnect connections](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/provisioning-overview).
  2. For each [region](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) where you're terminating hybrid connectivity in the VPC network, do the following: 
     1. Create two Dedicated or Partner [VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments), one for each edge availability zone. As part of this process, you select Cloud Routers and create BGP sessions.
     2. Configure the peer network (on-premises or other cloud) routers. 



### Configure workload projects

Create a separate VPC for each workload:

  1. [Create a new project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) to host your workload.
  2. [Enable the Compute Engine API](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api) for the project.
  3. Create a [custom-mode VPC network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#creating_networks).
  4. [Create subnets](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#subnet-rules) in the regions where you plan to deploy workloads. For each subnet, enable Private Google Access to allow VM instances with _only_ internal IP addresses to reach Google services.
  5. [Configure Private Service Connect for Google APIs](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-apis).
  6. For each workload you're consuming from a different VPC or your on-premises environment, [create a Private Service Connect consumer endpoint](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services).
  7. For each workload you're producing for a different VPC or your on-premises environment, [create an internal load balancer and service attachment for the service](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer). Consider [Private Service Connect subnet sizing](https://docs.cloud.google.com/vpc/docs/private-service-connect#psc-subnets) when deciding your IP addressing plan.
  8. If the service should be reachable from your on-premises environment, [create a Private Service Connect consumer endpoint](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services) in the transit VPC.



### Configure Cloud NAT

Follow these steps if the workloads in specific regions require outbound internet access—for example, to download software packages or updates.

  1. [Create a Cloud NAT gateway](https://docs.cloud.google.com/nat/docs/set-up-manage-network-address-translation) in the [regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) where workloads require outbound internet access. You can customize the Cloud NAT configuration to only allow outbound connectivity from specific subnets, if needed.
  2. At a minimum, [enable Cloud NAT logging](https://docs.cloud.google.com/nat/docs/monitoring) for the gateway to log `ERRORS_ONLY`. To include logs for translations performed by Cloud NAT, configure each gateway to log `ALL`.



### Configure observability

Network Intelligence Center provides a cohesive way to monitor, troubleshoot, and visualize your cloud networking environment. Use it to ensure that your design functions with the desired intent.

The following configurations support the analysis of logging and metrics enabled.

  * You must [enable the Network Management API](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview) before you can run Connectivity Tests. Enabling the API is required to use the API directly, the Google Cloud CLI, or the Google Cloud console.
  * You must [enable the Firewall Insights API](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/enable-api-features) before you can perform any tasks using Firewall Insights.



### Next steps

The initial configuration for this network design option is now complete. You can now either repeat these steps to configure an additional instance of the landing zone environment, such as a staging or production environment, or continue to [Decide the security for your Google Cloud landing zone](https://docs.cloud.google.com/architecture/landing-zones/decide-security).

## What's next

  * [Decide the security for your Google Cloud landing zone](https://docs.cloud.google.com/architecture/landing-zones/decide-security) (next document in this series).
  * Read [Best practices for VPC network design](https://docs.cloud.google.com/solutions/best-practices-vpc-design).
  * Read more about [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-02 UTC."],[],[]] 
