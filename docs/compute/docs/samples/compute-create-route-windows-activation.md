---
url: https://docs.cloud.google.com/compute/docs/samples/compute-create-route-windows-activation/
title: Create a route to Windows activation host \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:19:15.158297+00:00
---

# Create a route to Windows activation host  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-create-route-windows-activation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  Create a route to Windows activation host Stay organized with collections  Save and categorize content based on your preferences. 

If you have Windows instances without external IP addresses, you must also enable Private Google Access so that instances with only internal IP addresses can send traffic to the external IP address.

## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    	"google.golang.org/protobuf/proto"
    )
    
    // createRouteToWindowsActivationHost creates a new route to
    // kms.windows.googlecloud.com (35.190.247.13) for Windows activation.
    func createRouteToWindowsActivationHost(
    	w io.Writer,
    	projectID, routeName, networkName string,
    ) error {
    	// projectID := "your_project_id"
    	// routeName := "your_route_name"
    	// networkName := "global/networks/default"
    
    	ctx := context.Background()
    	routesClient, err := compute.[NewRoutesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_RoutesClient_NewRoutesRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewRoutesRESTClient: %w", err)
    	}
    	defer routesClient.Close()
    
    	// If you have Windows instances without external IP addresses,
    	// you must also enable Private Google Access so that instances
    	// with only internal IP addresses can send traffic to the external
    	// IP address for kms.windows.googlecloud.com.
    	// More infromation: https://cloud.google.com/vpc/docs/configure-private-google-access#enabling
    	req := &computepb.InsertRouteRequest{
    		Project: projectID,
    		RouteResource: &computepb.Route{
    			Name:      proto.String(routeName),
    			DestRange: proto.String("35.190.247.13/32"),
    			Network:   proto.String(networkName),
    			NextHopGateway: proto.String(
    				fmt.Sprintf("projects/%s/global/gateways/default-internet-gateway", projectID),
    			),
    		},
    	}
    
    	op, err := routesClient.Insert(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to create route: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Route created\n")
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/overview). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.compute.v1.[InsertRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRouteRequest.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import com.google.cloud.compute.v1.[Route](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Route.html);
    import com.google.cloud.compute.v1.[RoutesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RoutesClient.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateRouteToWindowsActivationHost {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // projectId - ID or number of the project you want to use.
        String projectId = "your-google-cloud-project-id";
    
        // routeName - Name of the route you want to create.
        String routeName = "route-name";
    
        // networkName - Name of the network you want the new instance to use.
        //  *   For example: "global/networks/default" represents the network
        //  *   named "default", which is created automatically for each project.
        String networkName = "global/networks/default";
    
        createRouteToWindowsActivationHost(projectId, routeName, networkName);
      }
    
      // Creates a new route to kms.windows.googlecloud.com (35.190.247.13) for Windows activation.
      public static void createRouteToWindowsActivationHost(String projectId, String routeName,
          String networkName)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Instantiates a client.
        try ([RoutesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RoutesClient.html) routesClient = [RoutesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RoutesClient.html).create()) {
    
          // If you have Windows instances without external IP addresses,
          // you must also enable Private Google Access so that instances
          // with only internal IP addresses can send traffic to the external
          // IP address for kms.windows.googlecloud.com.
          // More information: https://cloud.google.com/vpc/docs/configure-private-google-access#enabling
          [Route](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Route.html) route = [Route](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Route.html).newBuilder()
              .setName(routeName)
              .setDestRange("35.190.247.13/32")
              .setNetwork(networkName)
              .[setNextHopGateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Route.Builder.html#com_google_cloud_compute_v1_Route_Builder_setNextHopGateway_java_lang_String_)(
                  String.format("projects/%s/global/gateways/default-internet-gateway", projectId))
              .build();
    
          [InsertRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRouteRequest.html) request = [InsertRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRouteRequest.html).newBuilder()
              .setProject(projectId)
              .[setRouteResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRouteRequest.Builder.html#com_google_cloud_compute_v1_InsertRouteRequest_Builder_setRouteResource_com_google_cloud_compute_v1_Route_)(route)
              .build();
    
          // Wait for the operation to complete.
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) operation = routesClient.insertAsync(request).get(3, TimeUnit.MINUTES);
    
          if (operation.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            System.out.printf("Error in creating route %s", operation.[getError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getError__)());
            return;
          }
    
          System.out.printf("Route created %s", routeName);
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    
    
    def create_route_to_windows_activation_host(
        project_id: str, network: str, route_name: str
    ) -> compute_v1.Route:
        """
        If you have Windows instances without external IP addresses,
        you must also enable Private Google Access so that instances
        with only internal IP addresses can send traffic to the external
        IP address for kms.windows.googlecloud.com.
        More infromation: https://cloud.google.com/vpc/docs/configure-private-google-access#enabling
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            network: name of the network the route will be created in. Available name formats:
                * https://www.googleapis.com/compute/v1/projects/{project_id}/global/networks/{network}
                * projects/{project_id}/global/networks/{network}
                * global/networks/{network}
            route_name: name of the new route.
    
        Returns:
            A new compute_v1.Route object.
        """
        return create_route(
            project_id=project_id,
            network=network,
            route_name=route_name,
            destination_range="35.190.247.13/32",
            next_hop_gateway=f"projects/{project_id}/global/gateways/default-internet-gateway",
        )
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
