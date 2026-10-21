---
url: https://docs.cloud.google.com/vpc/docs/using-routes/
title: Use routes \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:27:43.633978+00:00
---

# Use routes  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/using-routes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use routes

This page describes how to create and manage routes for Virtual Private Cloud (VPC) networks in Google Cloud. This page assumes that you are familiar with the different types of Google Cloud routes and their characteristics as described in [Routes](https://docs.cloud.google.com/vpc/docs/routes).

Every new network has two types of system-generated routes: a [default route](https://docs.cloud.google.com/vpc/docs/routes#routingpacketsinternet), which you can remove or replace, and one [subnet route](https://docs.cloud.google.com/vpc/docs/routes#subnet-routes) for each of its subnets. You cannot remove a subnet route unless you delete the corresponding subnet itself.

In addition to the system-generated routes, you can create other [custom static routes](https://docs.cloud.google.com/vpc/docs/static-routes).

## List routes for a VPC network

You can use the Google Cloud CLI or the API to list and view details about the following types of routes:

  * [System-generated default routes](https://docs.cloud.google.com/vpc/docs/routes#routingpacketsinternet)
  * [Subnet routes](https://docs.cloud.google.com/vpc/docs/routes#subnet-routes)
  * [Peering subnet routes](https://docs.cloud.google.com/vpc/docs/routes#peering-subnet-routes)
  * [NCC subnet routes](https://docs.cloud.google.com/vpc/docs/routes#ncc-subnet-routes)
  * [Static routes](https://docs.cloud.google.com/vpc/docs/static-routes)



Neither the gcloud CLI commands nor the API methods show the following types of routes:

  * [Policy-based routes](https://docs.cloud.google.com/vpc/docs/routes#policy-based_routes)
  * [Dynamic routes](https://docs.cloud.google.com/vpc/docs/routes#dynamic_routes)
  * [Peering static and dynamic routes](https://docs.cloud.google.com/vpc/docs/routes#peering-custom-routes)



To see the complete route view, use the Google Cloud console. To list and describe policy-based routes, see [Use policy-based routes](https://docs.cloud.google.com/vpc/docs/use-policy-based-routes).

###  Console 

  1. In the Google Cloud console, go to the **Routes** page.

[Go to Routes](https://console.cloud.google.com/networking/routes/list)

  2. On the **Effective routes** tab, do the following:

     * Choose a VPC network.
     * Choose a region.
  3. Click **View**.

  4. You can filter on properties including [route type](https://docs.cloud.google.com/vpc/docs/routes#types_of_routes), destination IP range, and [next hop type](https://docs.cloud.google.com/vpc/docs/routes#static-route-next-hops).

  5. Optional: Click the **Show suppressed routes** toggle to the on position to view routes that are suppressed. To view the reason why a route is suppressed, point to the icon in the **Status** column.




###  gcloud 

To list and view details for [subnet routes](https://docs.cloud.google.com/vpc/docs/routes#subnet-routes) and [static routes](https://docs.cloud.google.com/vpc/docs/static-routes), use the [`gcloud compute routes` commands](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routes). These commands don't show other types of routes. To see all routes, use the Google Cloud console.

To list routes, do the following:
    
    
    gcloud compute routes list \
        --filter="network=NETWORK_NAME" \
        --project=PROJECT_ID
    

To get details for a route, do the following:
    
    
    gcloud compute routes describe ROUTE_NAME \
        --format="flattened()" \
        --project=PROJECT_ID
    

Replace the following:

  * `NETWORK_NAME`: the name of the VPC network
  * `PROJECT_ID`: the project ID that contains your VPC network
  * `ROUTE_NAME`: the name of the route



###  API 

To list and view details for [subnet routes](https://docs.cloud.google.com/vpc/docs/routes#subnet-routes) and [static routes](https://docs.cloud.google.com/vpc/docs/static-routes), use the [routes.list](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routes/list) and [routes.get](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routes/get) methods. These methods don't show other types of routes. To see all routes, use the Google Cloud console.

To list routes, do the following:
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/routes?filter=network="NETWORK_URL
    

To get details for a route, do the following:
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/routes/ROUTE_NAME
    

Replace the following:

  * `PROJECT_ID`: the project ID that contains your VPC network
  * `NETWORK_URL`: the URL of the VPC network
  * `ROUTE_NAME`: the name of the route



## List applicable routes for a VM network interface

You can use the Google Cloud console to view applicable routes for a VM's network interface. This view narrows the list of routes that you can use for egress traffic.

To view applicable routes for a specific network interface of a VM, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Locate a VM instance in the list. In the more_vert**More actions** menu at the end of the row, select **View network details**.

  3. If an instance has multiple network interfaces, in the **Network interface details** section, select the network interface that you want to view.

  4. In the **Firewall and routes details** section, click the **Routes** tab to see all the routes that apply to the network interface, sorted by route name.




## Add and remove static routes

You can add or remove static routes and policy-based routes that are local to your VPC network. This section describes how to add and delete local static routes. For more information about how to add and remove policy-based routes, see [Use policy-based routes](https://docs.cloud.google.com/vpc/docs/use-policy-based-routes).

Subnet routes are added and deleted automatically when you add or delete a subnet. For more information about how to add and remove subnets, see [Work with subnets](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#subnet-rules).

All routes in a VPC network that are connected by VPC Network Peering must be manipulated in the VPC network that exports those routes. For more information, see [Route exchange options](https://docs.cloud.google.com/vpc/docs/vpc-peering#route-exchange-options).

**Important:** Static routes cannot be modified after creation. Instead, delete the route and create a replacement route.

### Before you add a static route

Before you add a static route, consider the following:

  * Make sure you understand the different types of next hops that static routes can use. For information about the different types of static route next hops, including which ones support IPv6 destinations, see [Next hops and features](https://docs.cloud.google.com/vpc/docs/static-routes#static-route-next-hops).
  * Unless you use [hybrid subnets](https://docs.cloud.google.com/vpc/docs/hybrid-subnets), a static route cannot have a destination range that matches or is more specific than the destination range of a subnet or peering subnet route. For more details, see [Interactions with custom static routes](https://docs.cloud.google.com/vpc/docs/routes#subnet-static-interactions) in the Routes overview and [Subnet and static route interactions](https://docs.cloud.google.com/vpc/docs/vpc-peering#interaction-subnet-static) in the VPC Network Peering documentation.
  * To avoid conflicts when using an auto mode VPC network, don't create static routes whose destinations fit within `10.128.0.0/9`. Review the [auto mode IPv4 ranges](https://docs.cloud.google.com/vpc/docs/subnets#ip-ranges) for details.
  * Destinations for custom static routes can't overlap with any internal [allocated range](https://docs.cloud.google.com/vpc/docs/private-access-options).
  * Make sure you're familiar with [instances as next hops](https://docs.cloud.google.com/vpc/docs/static-routes#instance_next_hops) before you create a custom static route that uses a VM as its next hop. Google Cloud only validates that a VM exists at the time when you create the route if you choose a _next-hop instance_.
  * If you create a route using a network tag, then only VMs with that tag receive that route. However, tagged VMs still receive all routes that have no network tag.

**Note:** For next hops that use Cloud Router, you can optionally use custom learned routes as an alternative to static routes. Unlike static routes, custom learned routes are suppressed automatically if their associated BGP session is disrupted. This behavior allows alternate routes to be used in case of a network outage and might prevent your traffic from being dropped. Also, unlike static routes, custom learned routes can be used over Cloud Interconnect VLAN attachments and HA VPN tunnels. For more information, see [Custom learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes). This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

### Add a static route

Add a static route to a network. For more information about the different types of static route next hops, including which ones support IPv6 destinations, see [Next hops and features](https://docs.cloud.google.com/vpc/docs/static-routes#static-route-next-hops).

###  Console 

  1. In the Google Cloud console, go to the **Routes page**.

[Go to Routes](https://console.cloud.google.com/networking/routes/list)

  2. Click the **Route management** tab.

  3. Click **Create route**.

  4. Specify a name and a description for the route.

  5. In the **Network** list, select an existing network for the route.

  6. In the **Route type** list, select **Static route**.

  7. In the **IP version** list, select the required IP version:

     * To create an IPv4 static route, select **IPv4**.
     * To create an IPv6 static route, select **IPv6**.
  8. Specify a destination IP range. The broadest possible destination is `0.0.0.0/0` for IPv4 or `::/0` for IPv6.

  9. Specify a [priority](https://docs.cloud.google.com/vpc/docs/static-routes#individualroutes) for the route. The priority can be from `0` (the highest priority) to `65535` (the lowest priority).

  10. To make the route applicable only to select instances with matching network tags, specify those in the **Instance tags** field. Leave the field blank to make the route applicable to all instances in the network.

  11. Select a [next hop](https://docs.cloud.google.com/vpc/docs/static-routes#static-route-next-hops) for the route:

     * **Default internet gateway** : delivers packets to the internet and to Google APIs and services
     * **Specify an instance** : delivers packets to a VM instance's network interface. Specify the VM instance by name and zone. If the route destination is an IPv6 address, the VM instance must be _dual-stack_ or _IPv6-only_.
     * **Specify IP address of an instance** : specify an IP address of an _existing instance_ in the VPC network. For IPv6 static routes, the instance must be _dual-stack_ or _IPv6-only_. For important restrictions for valid next hop IP addresses, see [static route next hops](https://docs.cloud.google.com/vpc/docs/static-routes#static-route-next-hops).
     * **Specify VPN tunnel** : delivers packets to an existing [Classic VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) tunnel [using static routing](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/choosing-networks-routing#ts-tun-routing).
     * **Specify a forwarding rule of an internal passthrough Network Load Balancer** : delivers packets to an [internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal/ilb-next-hop-overview) that is specified by its internal forwarding rule name and region. The forwarding rule can have an IPv4 or IPv6 address. The IP version of the forwarding rule that you specify must match the IP version of the static route that you create.
  12. Click **Create**.




###  gcloud 

Create a new custom static route with the following gcloud CLI command:
    
    
    gcloud compute routes create ROUTE_NAME \
        --network=NETWORK \
        --destination-range=DESTINATION_RANGE \
        --priority=PRIORITY \
        NEXT_HOP_SPECIFICATION
    

Replace the following:

  * `ROUTE_NAME`: the name of the route
  * `NETWORK`: the name of the VPC network that contains the route
  * `DESTINATION_RANGE`: the destination IPv4 or IPv6 addresses to which this route applies. The broadest possible destination is `0.0.0.0/0` for IPv4 or `::/0` for IPv6.
  * `PRIORITY`: the route [priority](https://docs.cloud.google.com/vpc/docs/static-routes#individualroutes), which can be from `0` (the highest priority) to `65535` (the lowest priority)
  * `NEXT_HOP_SPECIFICATION`: the [next hop](https://docs.cloud.google.com/vpc/docs/static-routes#static-route-next-hops) for the static route. Use one of the following parameters or combination of parameters:

    * `--next-hop-gateway=default-internet-gateway`: deliver packets to the internet and to Google APIs and services.
    * `--next-hop-instance=INSTANCE_NAME` and `--next-hop-instance-zone=ZONE`: deliver packets to an existing VM instance's network interface. Specify the VM instance by name and zone. If the route destination is an IPv6 address, the VM instance must be _dual-stack_ or _IPv6-only_.
    * `--next-hop-address=ADDRESS`: specify an IP address of an _existing instance_ in the VPC network. For IPv6 static routes, the instance must be _dual-stack_ or _IPv6-only_. For important restrictions for valid next hop IP addresses, see [Next hops and features](https://docs.cloud.google.com/vpc/docs/static-routes#static-route-next-hops).
    * `--next-hop-vpn-tunnel=VPN_TUNNEL_NAME` and `--next-hop-vpn-tunnel-region=REGION`: deliver packets to an existing [Classic VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) tunnel [using static routing](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/choosing-networks-routing#ts-tun-routing).
    * `--next-hop-ilb=FORWARDING_RULE` and `--next-hop-ilb-region=REGION`: deliver packets to an [internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal/ilb-next-hop-overview). Specify the forwarding rule by its name (or IPv4 or IPv6 address) and region. The IP version of the forwarding rule that you specify must match the IP version of the static route that you create. For more information about configuring static routes to internal passthrough Network Load Balancers, see [Create static routes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/configure-static-routes#create-routes).

To make the custom static route apply to only select VMs by network tag, add the `--tags` flag and specify one or more network tags. For more information about how network tags and custom static routes work together, see [Applicable routes](https://docs.cloud.google.com/vpc/docs/routes#applicable_routes) in the Routes overview. You can use tags with any custom static route.




For more information about the gcloud CLI syntax, see the [SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routes/create).

###  API 

Create a new custom static route.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/routes
    {
      "name": "ROUTE_NAME",
      "network": "NETWORK_NAME",
      "destRange": "DESTINATION_RANGE",
      "priority": PRIORITY,
      "NEXT_HOP_SPECIFICATION"
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where your route is created
  * `ROUTE_NAME`: the name of the route
  * `NETWORK`: the name of the VPC network that contains the route.
  * `DESTINATION_RANGE`: the destination IPv4 or IPv6 address range to which this route applies. The broadest possible destination is `0.0.0.0/0` for IPv4 or `::/0` for IPv6.
  * `PRIORITY`: the route [priority](https://docs.cloud.google.com/vpc/docs/static-routes#individualroutes), which can be from `0` (the highest priority) to `65535` (the lowest priority)
  * `NEXT_HOP_SPECIFICATION`: the [next hop](https://docs.cloud.google.com/vpc/docs/static-routes#static-route-next-hops) for the static route. Use one of the following parameters or combination of parameters: 
    * `nextHopGateway: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/gateways/default-internet-gateway`: delivers packets to the internet and to Google APIs and services
    * `nextHopInstance: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME`: delivers packets to a VM instance's network interface. Specify the VM instance by name and zone. If the route destination is an IPv6 address, the VM instance must be _dual-stack_ or _IPv6-only_.
    * `nextHopIp: ADDRESS`: specify an IP address of an _existing instance_ in the VPC network. For IPv6 static routes, the instance must be _dual-stack_ or _IPv6-only_. For important restrictions for valid next hop IP addresses, see [Next hops and features](https://docs.cloud.google.com/vpc/docs/static-routes#static-route-next-hops).
    * `nextHopVpnTunnel: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/vpnTunnels/VPN_TUNNEL_NAME`: delivers packets to an existing [Classic VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) tunnel [using static routing](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/choosing-networks-routing#ts-tun-routing).
    * `nextHopIlb: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/forwardingRules/FORWARDING_RULE`: delivers packets to an [internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal/ilb-next-hop-overview). Specify the forwarding rule by its name (or IPv4 or IPv6 address) and region. The IP version of the forwarding rule that you specify must match the IP version of the static route that you create.



To make the custom static route apply to only select VMs by network tag, add the `tags` field and specify one or more network tags. For more information about how network tags and custom static routes work together, see [Applicable routes](https://docs.cloud.google.com/vpc/docs/routes#applicable_routes) in the Routes overview. You can use tags with any custom static route.

For more information, refer to the [`routes.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routes/insert) method.

### Terraform

You can create a static route by using a [Terraform module](https://github.com/terraform-google-modules/terraform-google-network).

This static route creates a default route to the internet.
    
    
    module "google_compute_route" {
      source       = "../../modules/routes" #adding local path
      project_id   = var.project_id         # Replace this with your project ID in quotes
      network_name = "default"
    
      routes = [
        {
          name              = "egress-internet"
          description       = "route through IGW to access internet"
          destination_range = "0.0.0.0/0"
          tags              = ["egress-inet"]
          next_hop_internet = true
        }
      ]
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  Go 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    	"google.golang.org/protobuf/proto"
    )
    
    // createRoute creates a route with given name inside given project.
    func createRoute(w io.Writer, projectID, name string) error {
    	// projectID := "your_project_id"
    	// name := "testname"
    
    	ctx := context.Background()
    	client, err := compute.[NewRoutesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_RoutesClient_NewRoutesRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewRoutesRESTClient: %w", err)
    	}
    	defer client.Close()
    
    	route := &computepb.Route{
    		Name:           proto.String(name),
    		Network:        proto.String("global/networks/default"),
    		DestRange:      proto.String("0.0.0.0/0"),
    		NextHopGateway: proto.String("global/gateways/default-internet-gateway"),
    	}
    
    	req := &computepb.InsertRouteRequest{
    		Project:       projectID,
    		RouteResource: route,
    	}
    	op, err := client.Insert(ctx, req)
    
    	if err != nil {
    		return fmt.Errorf("unable to insert a route: %w", err)
    	}
    
    	if err := op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Route created\n")
    
    	return nil
    }
    

###  Java 
    
    
    import com.google.cloud.compute.v1.[InsertRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRouteRequest.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import com.google.cloud.compute.v1.[Route](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Route.html);
    import com.google.cloud.compute.v1.[RoutesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RoutesClient.html);
    import java.io.IOException;
    import java.util.UUID;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateRoute {
    
      public static void main(String[] args)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Cloud project you want to use.
        String projectId = "your-project-id";
        // Route name you want to use.
        String routeName = "your-route-name";
        createRoute(projectId, routeName);
      }
    
      // Create route for a project.
      public static [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html).[Status](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Status.html) createRoute(String projectId, String routeName)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([RoutesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RoutesClient.html) routesClient = [RoutesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RoutesClient.html).create()) {
          String nextHopGateway =
                  String.format("projects/%s/global/gateways/default-internet-gateway", projectId);
    
          [Route](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Route.html) route = [Route](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Route.html).newBuilder()
                  .setName(routeName)
                  .setDestRange("10.0.0.0/16")
                  .setNetwork("global/networks/default")
                  .[setNextHopGateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Route.Builder.html#com_google_cloud_compute_v1_Route_Builder_setNextHopGateway_java_lang_String_)(nextHopGateway)
                  .build();
    
          [InsertRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRouteRequest.html) request = [InsertRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRouteRequest.html).newBuilder()
                  .setProject(projectId)
                  .setRequestId(UUID.randomUUID().toString())
                  .[setRouteResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRouteRequest.Builder.html#com_google_cloud_compute_v1_InsertRouteRequest_Builder_setRouteResource_com_google_cloud_compute_v1_Route_)(route)
                  .build();
    
          return routesClient.insertCallable().futureCall(request)
                  .get(30, TimeUnit.SECONDS).getStatus();
        }
      }
    }

###  Python 
    
    
    from __future__ import annotations
    
    import sys
    from typing import Any
    
    from google.api_core.extended_operation import ExtendedOperation
    from google.cloud import [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest)
    
    
    def wait_for_extended_operation(
        operation: ExtendedOperation, verbose_name: str = "operation", timeout: int = 300
    ) -> Any:
        """
        Waits for the extended (long-running) operation to complete.
    
        If the operation is successful, it will return its result.
        If the operation ends with an error, an exception will be raised.
        If there were any warnings during the execution of the operation
        they will be printed to sys.stderr.
    
        Args:
            operation: a long-running operation you want to wait on.
            verbose_name: (optional) a more verbose name of the operation,
                used only during error and warning reporting.
            timeout: how long (in seconds) to wait for operation to finish.
                If None, wait indefinitely.
    
        Returns:
            Whatever the operation.result() returns.
    
        Raises:
            This method will raise the exception received from `operation.exception()`
            or RuntimeError if there is no exception set, but there is an `error_code`
            set for the `operation`.
    
            In case of an operation taking longer than `timeout` seconds to complete,
            a `concurrent.futures.TimeoutError` will be raised.
        """
        result = operation.result(timeout=timeout)
    
        if operation.error_code:
            print(
                f"Error during {verbose_name}: [Code: {operation.error_code}]: {operation.error_message}",
                file=sys.stderr,
                flush=True,
            )
            print(f"Operation ID: {operation.name}", file=sys.stderr, flush=True)
            raise operation.exception() or RuntimeError(operation.error_message)
    
        if operation.warnings:
            print(f"Warnings during {verbose_name}:\n", file=sys.stderr, flush=True)
            for warning in operation.warnings:
                print(f" - {warning.code}: {warning.message}", file=sys.stderr, flush=True)
    
        return result
    
    
    def create_route(
        project_id: str,
        network: str,
        route_name: str,
        destination_range: str,
        *,
        next_hop_gateway: str | None = None,
        next_hop_ip: str | None = None,
        next_hop_instance: str | None = None,
        next_hop_vpn_tunnel: str | None = None,
        next_hop_ilb: str | None = None,
    ) -> compute_v1.Route:
        """
        Create a new route in selected network by providing a destination and next hop name.
    
        Note: The set of {next_hop_gateway, next_hop_ip, next_hop_instance, next_hop_vpn_tunnel,
            next_hop_ilb} is exclusive, you and only specify one of those parameters.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            network: name of the network the route will be created in. Available name formats:
                * https://www.googleapis.com/compute/v1/projects/{project_id}/global/networks/{network}
                * projects/{project_id}/global/networks/{network}
                * global/networks/{network}
            route_name: name of the new route.
            destination_range: range of destination IPs this route should be applied to. E.g. 10.0.0.0/16.
            next_hop_gateway: name of the gateway the traffic should be directed to.
            next_hop_ip: IP address the traffic should be directed to.
            next_hop_instance: name of the instance the traffic should be directed to. Name format:
                "projects/{project}/zones/{zone}/instances/{instance_name}"
            next_hop_vpn_tunnel: name of the VPN tunnel the traffic should be directed to. Name format:
                "projects/{project}/regions/{region}/vpnTunnels/{vpn_tunnel_name}"
            next_hop_ilb: name of a forwarding rule of the Internal Load Balancer the traffic
                should be directed to. Name format:
                "projects/{project}/regions/{region}/forwardingRules/{forwarding_rule_region}"
    
        Returns:
            A new compute_v1.Route object.
        """
        excl_args = {
            next_hop_instance,
            next_hop_ilb,
            next_hop_vpn_tunnel,
            next_hop_gateway,
            next_hop_ip,
        }
        args_set = sum(1 if arg is not None else 0 for arg in excl_args)
    
        if args_set != 1:
            raise RuntimeError("You must specify exactly one next_hop_* parameter.")
    
        route = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[Route](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.Route.html)()
        route.name = route_name
        route.network = network
        route.dest_range = destination_range
    
        if next_hop_gateway:
            route.next_hop_gateway = next_hop_gateway
        elif next_hop_ip:
            route.next_hop_ip = next_hop_ip
        elif next_hop_instance:
            route.next_hop_instance = next_hop_instance
        elif next_hop_vpn_tunnel:
            route.next_hop_vpn_tunnel = next_hop_vpn_tunnel
        elif next_hop_ilb:
            route.next_hop_ilb = next_hop_ilb
    
        route_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[RoutesClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.routes.RoutesClient.html)()
        operation = route_client.[insert](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.routes.RoutesClient.html#google_cloud_compute_v1_services_routes_RoutesClient_insert)(project=project_id, route_resource=route)
    
        wait_for_extended_operation(operation, "route creation")
    
        return route_client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.routes.RoutesClient.html#google_cloud_compute_v1_services_routes_RoutesClient_get)(project=project_id, route=route_name)
    
    

### Add an IPv4 default route

The IPv4 default static route (`0.0.0.0/0`) with the `next-hop-gateway` set to `default-internet-gateway` is automatically configured for each VPC network. Use these steps to re-create this route if necessary.

###  Console 

  1. In the Google Cloud console, go to the **Routes** page.

[Go to Routes](https://console.cloud.google.com/networking/routes/list)

  2. Click the **Route management** tab.

  3. Click **Create route**.

  4. Specify a name and a description for the route.

  5. Select an existing network for the route.

  6. For **Destination IP range** , enter `0.0.0.0/0`.

  7. Specify a priority for the route. The priority can be from `0` (the highest priority) to `65535` (the lowest priority).

  8. For **Next hop** , select **Default internet gateway**.

  9. Click **Create**.




###  gcloud 

Recreate the IPv4 default route for a network.
    
    
    gcloud compute routes create ROUTE_NAME \
        --destination-range=0.0.0.0/0 \
        --network=NETWORK \
        --next-hop-gateway=default-internet-gateway
    

Replace the following:

  * `ROUTE_NAME`: a name for the route
  * `NETWORK`: the name of the VPC network that contains the route



###  API 

Recreate the IPv4 default route for a network.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/routes
    {
      "destRange": "0.0.0.0/0",
      "name": "ROUTE_NAME",
      "network": "NETWORK_NAME",
      "nextHopGateway": "projects/PROJECT_ID/global/gateways/default-internet-gateway"
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where your route is created
  * `ROUTE_NAME`: a name for the route
  * `NETWORK_NAME`: the name of the VPC network that contains the route



### Add an IPv6 default route

The IPv6 default static route (`::/0`) with the `next-hop-gateway` set to `default-internet-gateway` is automatically configured for the VPC network when you create a subnet with the IPv6 access type set to external. You can delete the route to block all IPv6 traffic from VMs to the internet. You can also recreate the route if needed.

###  Console 

  1. In the Google Cloud console, go to the **Routes** page.

[Go to Routes](https://console.cloud.google.com/networking/routes/list)

  2. Click the **Route management** tab.

  3. Click **Create route**.

  4. Specify a name and a description for the route.

  5. Select an existing network for the route.

  6. For **Destination IP range** , enter `::/0`.

  7. Specify a [priority](https://docs.cloud.google.com/vpc/docs/static-routes#individualroutes) for the route. The priority can be from `0` (the highest priority) to `65535` (the lowest priority).

  8. For **Next hop** , select **Default internet gateway**.

  9. Click **Create**.




###  gcloud 

Recreate the IPv6 default route for a network.
    
    
    gcloud compute routes create ROUTE_NAME \
        --destination-range=::/0 \
        --network=NETWORK \
        --next-hop-gateway=default-internet-gateway
    

Replace the following:

  * `ROUTE_NAME`: a name for the route.
  * `NETWORK`: the name of the VPC network that contains the route.



###  API 

Recreate the IPv6 default route for a network.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/routes
    {
      "destRange": "::/0",
      "name": "ROUTE_NAME",
      "network": "NETWORK_NAME",
      "nextHopGateway": "projects/PROJECT_ID/global/gateways/default-internet-gateway"
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where your route is created
  * `ROUTE_NAME`: a name for the route
  * `NETWORK_NAME`: the name of the VPC network that contains the route



### Modify a static route

You cannot edit or update a static route after you create it. To modify a static route, you must delete it and create a replacement.

### Delete a static route

To delete a route, do the following.

###  Console 

  1. In the Google Cloud console, go to the **Routes** page.

[Go to Routes](https://console.cloud.google.com/networking/routes/list)

  2. Click the **Route management** tab.

  3. Select the checkbox next to the rule that you want to delete.

  4. Click delete**Delete**.

  5. Click **Delete** again to confirm.




###  gcloud 

Delete a custom static route by using the following gcloud CLI command:
    
    
    gcloud compute routes delete ROUTE_NAME
    

Replace `ROUTE_NAME` with the name of the route that you want to delete.

###  API 

Delete a custom static route to remove it from your VPC network by using the [`routes.delete` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routes/delete):
    
    
    DELETE https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/routes/ROUTE_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where your route is located.
  * `ROUTE_NAME`: the name of the route to delete.



###  Go 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    )
    
    // deleteRoute deletes a route by name in given project.
    func deleteRoute(w io.Writer, projectID, name string) error {
    	// projectID := "your_project_id"
    	// name := "testname"
    
    	ctx := context.Background()
    	client, err := compute.[NewRoutesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_RoutesClient_NewRoutesRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewRoutesRESTClient: %w", err)
    	}
    	defer client.Close()
    
    	req := &computepb.DeleteRouteRequest{
    		Project: projectID,
    		Route:   name,
    	}
    	op, err := client.Delete(ctx, req)
    
    	if err != nil {
    		return fmt.Errorf("unable to delete a route: %w", err)
    	}
    
    	if err := op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Route deleted\n")
    
    	return nil
    }
    

###  Java 
    
    
    import com.google.cloud.compute.v1.[DeleteRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRouteRequest.html);
    import com.google.cloud.compute.v1.[RoutesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RoutesClient.html);
    import java.io.IOException;
    import java.util.UUID;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class DeleteRoute {
    
      public static void main(String[] args)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Cloud project you want to use.
        String projectId = "your-project-id";
        // Route name you want to delete.
        String routeName = "your-route-name";
    
        deleteRoute(projectId, routeName);
      }
    
      // Deletes a route from a project.
      public static void deleteRoute(String projectId, String routeName)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([RoutesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RoutesClient.html) routesClient = [RoutesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RoutesClient.html).create()) {
          [DeleteRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRouteRequest.html) request = [DeleteRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRouteRequest.html).newBuilder()
                  .setProject(projectId)
                  .setRoute(routeName)
                  .setRequestId(UUID.randomUUID().toString())
                  .build();
          routesClient.deleteCallable().futureCall(request).get(30, TimeUnit.SECONDS);
        }
      }
    }

###  Python 
    
    
    from __future__ import annotations
    
    import sys
    from typing import Any
    
    from google.api_core.extended_operation import ExtendedOperation
    from google.cloud import [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest)
    
    
    def wait_for_extended_operation(
        operation: ExtendedOperation, verbose_name: str = "operation", timeout: int = 300
    ) -> Any:
        """
        Waits for the extended (long-running) operation to complete.
    
        If the operation is successful, it will return its result.
        If the operation ends with an error, an exception will be raised.
        If there were any warnings during the execution of the operation
        they will be printed to sys.stderr.
    
        Args:
            operation: a long-running operation you want to wait on.
            verbose_name: (optional) a more verbose name of the operation,
                used only during error and warning reporting.
            timeout: how long (in seconds) to wait for operation to finish.
                If None, wait indefinitely.
    
        Returns:
            Whatever the operation.result() returns.
    
        Raises:
            This method will raise the exception received from `operation.exception()`
            or RuntimeError if there is no exception set, but there is an `error_code`
            set for the `operation`.
    
            In case of an operation taking longer than `timeout` seconds to complete,
            a `concurrent.futures.TimeoutError` will be raised.
        """
        result = operation.result(timeout=timeout)
    
        if operation.error_code:
            print(
                f"Error during {verbose_name}: [Code: {operation.error_code}]: {operation.error_message}",
                file=sys.stderr,
                flush=True,
            )
            print(f"Operation ID: {operation.name}", file=sys.stderr, flush=True)
            raise operation.exception() or RuntimeError(operation.error_message)
    
        if operation.warnings:
            print(f"Warnings during {verbose_name}:\n", file=sys.stderr, flush=True)
            for warning in operation.warnings:
                print(f" - {warning.code}: {warning.message}", file=sys.stderr, flush=True)
    
        return result
    
    
    def delete_route(project_id: str, route_name: str) -> None:
        """
        Delete a route in project.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            route_name: name of the route to delete.
        """
    
        route_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[RoutesClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.routes.RoutesClient.html)()
        operation = route_client.[delete](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.routes.RoutesClient.html#google_cloud_compute_v1_services_routes_RoutesClient_delete)(project=project_id, route=route_name)
    
        wait_for_extended_operation(operation, "route deletion")
    
    

### Propagation of route changes

When you add or delete a static route, the route propagates to all regions and VM instances in your VPC network. A route operation status of `PENDING` or `RUNNING` indicates that the route change is queued.

After queueing, the route operation status changes to `DONE`. It might take an additional 30 seconds before all VM instances in your VPC network and VPC Network Peering networks use a new route or stop using an old route.

If you add or remove several static routes simultaneously, the changes can be applied in any order. There is no guarantee that the order in which you submit route changes is the order in which they are processed. Different instances might become aware of the changes at different times.

If you need to make route changes that depend on each other, you must make those changes sequentially by performing subsequent changes only after the previous change's status is `DONE` and an additional 30 seconds has elapsed.

## Enable IP forwarding for instances

By default, IP forwarding is disabled, and Google Cloud performs strict source address checking. Subject to the effective egress firewall configuration, a VM can emit packets with the following sources:

  * The primary internal IPv4 address of an instance's network interface (NIC).
  * Any configured alias IP range on an instance's NIC.
  * If an IPv6 address range is configured on the subnet, and the instance is dual-stack or IPv6-only, any of the IPv6 addresses that are assigned to the NIC.
  * An internal or external IP address associated with a forwarding rule, for pass-through load balancing or protocol forwarding, if the instance is a backend for an internal passthrough Network Load Balancer, a regional external passthrough Network Load Balancer, or is referenced by a target instance.



To use a VM as a next hop for a route, the VM needs to forward packets whose sources don't match one of the IP addresses or ranges in the preceding list. To forward packets with arbitrary source addresses, you must enable IP forwarding:

  * When you create or update a VM, you enable IP forwarding by following the directions in this section. Enabling IP forwarding applies to all of the NICs on the VM.
  * In addition to the steps in this section, you must enable IP forwarding _within the VM guest operating system_. To do this on Linux, set the value of one or both of the following kernel parameters to `1`: `net.ipv4.ip_forward` (for IPv4) or `net.ipv6.conf.all.forwarding` (for IPv6).



To enable IP forwarding when you create a VM, complete the following steps.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click **Create instance**.

  3. In the **Advanced options** section, expand **Networking, disks, security, management, sole-tenancy**.

  4. Expand the **Networking** section.

  5. In the **IP forwarding** section, select the **Enable** checkbox.




###  gcloud 

When creating an instance, add the `--can-ip-forward` flag to your command:
    
    
    gcloud compute instances create ... --can-ip-forward
    

###  API 

When creating an instance, use the `canIpForward` field to enable IP forwarding:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    {
      "canIpForward": true,
      ...other fields
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project that contains the instance
  * `ZONE`: the Google Cloud zone containing the instance



For more information, see the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert).

### Terraform

You can use the [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance) to create a VM instance with IP forwarding enabled.

In this example, the Terraform arguments have assigned values that you can change.
    
    
    resource "google_compute_instance" "default" {
      project      = var.project_id # Replace this with your project ID in quotes
      zone         = "southamerica-east1-b"
      name         = "instance-next-hop"
      machine_type = "e2-medium"
      boot_disk {
        initialize_params {
          image = "debian-cloud/debian-9"
        }
      }
      network_interface {
        network = "default"
      }
      can_ip_forward = true
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

After you enable IP forwarding, [continue with the VM creation process](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).

To enable IP forwarding on an existing VM, [update the `canIpForward` instance property](https://docs.cloud.google.com/compute/docs/instances/update-instance-properties).

## What's next

  * For information about routes, see [Routes](https://docs.cloud.google.com/vpc/docs/routes).
  * For information about Google Cloud VPC networks, see the [Virtual Private Cloud (VPC) overview](https://docs.cloud.google.com/vpc/docs/overview).
  * For instructions about creating and modifying VPC networks, see [Create and manage VPC networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
