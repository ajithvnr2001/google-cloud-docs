---
url: https://docs.cloud.google.com/compute/docs/samples/compute-create-egress-rule-windows-activation/
title: Create a firewall rule for Windows activation host \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:43.625219+00:00
---

# Create a firewall rule for Windows activation host  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-create-egress-rule-windows-activation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  Create a firewall rule for Windows activation host Stay organized with collections  Save and categorize content based on your preferences. 

This sample creates an egress firewall rule with the highest priority for host kms.windows.googlecloud.com for Windows activation.

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
    
    // createFirewallRuleForWindowsActivationHost creates an egress firewall rule with
    // the highest priority for host kms.windows.googlecloud.com (35.190.247.13)
    // for Windows activation.
    func createFirewallRuleForWindowsActivationHost(
    	w io.Writer,
    	projectID, firewallRuleName, networkName string,
    ) error {
    	// projectID := "your_project_id"
    	// firewallRuleName := "your_firewall_rule_name"
    	// networkName := "global/networks/default"
    
    	ctx := context.Background()
    	firewallsClient, err := compute.[NewFirewallsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_FirewallsClient_NewFirewallsRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewFirewallsRESTClient: %w", err)
    	}
    	defer firewallsClient.Close()
    
    	req := &computepb.InsertFirewallRequest{
    		Project: projectID,
    		FirewallResource: &computepb.Firewall{
    			Name: proto.String(firewallRuleName),
    			Allowed: []*computepb.Allowed{
    				{
    					IPProtocol: proto.String("tcp"),
    					Ports:      []string{"1688"},
    				},
    			},
    			Direction:         proto.String("EGRESS"),
    			Network:           proto.String(networkName),
    			DestinationRanges: []string{"35.190.247.13/32"},
    			Priority:          proto.Int32(0),
    		},
    	}
    
    	op, err := firewallsClient.Insert(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to create firewall rule: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Firewall rule created\n")
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/overview). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.compute.v1.[Allowed](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Allowed.html);
    import com.google.cloud.compute.v1.[Firewall](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Firewall.html);
    import com.google.cloud.compute.v1.[FirewallsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallsClient.html);
    import com.google.cloud.compute.v1.[InsertFirewallRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertFirewallRequest.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateFirewallRuleForWindowsActivationHost {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // projectId - ID or number of the project you want to use.
        String projectId = "your-google-cloud-project-id";
    
        // firewallRuleName - Name of the firewall rule you want to create.
        String firewallRuleName = "firewall-rule-name";
    
        // networkName - Name of the network you want the new instance to use.
        //  *   For example: "global/networks/default" represents the network
        //  *   named "default", which is created automatically for each project.
        String networkName = "global/networks/default";
    
        createFirewallRuleForWindowsActivationHost(projectId, firewallRuleName, networkName);
      }
    
      // Creates a new allow egress firewall rule with the highest priority for host
      // kms.windows.googlecloud.com (35.190.247.13) for Windows activation.
      public static void createFirewallRuleForWindowsActivationHost(String projectId,
          String firewallRuleName, String networkName)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Instantiates a client.
        try ([FirewallsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallsClient.html) firewallsClient = [FirewallsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallsClient.html).create()) {
    
          [Firewall](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Firewall.html) firewall = [Firewall](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Firewall.html).newBuilder()
              .setName(firewallRuleName)
              // These are the default values for kms.windows.googlecloud.com
              // See, https://cloud.google.com/compute/docs/instances/windows/creating-managing-windows-instances#firewall_rule_requirements
              .[addAllowed](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Firewall.Builder.html#com_google_cloud_compute_v1_Firewall_Builder_addAllowed_com_google_cloud_compute_v1_Allowed_)([Allowed](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Allowed.html).newBuilder()
                  .setIPProtocol("tcp")
                  .addPorts("1688")
                  .build())
              .setDirection("EGRESS")
              .setNetwork(networkName)
              .[addDestinationRanges](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Firewall.Builder.html#com_google_cloud_compute_v1_Firewall_Builder_addDestinationRanges_java_lang_String_)("35.190.247.13/32")
              .setPriority(0)
              .build();
    
          [InsertFirewallRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertFirewallRequest.html) request = [InsertFirewallRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertFirewallRequest.html).newBuilder()
              .setProject(projectId)
              .setFirewallResource(firewall)
              .build();
    
          // Wait for the operation to complete.
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) operation = firewallsClient.insertAsync(request).get(3, TimeUnit.MINUTES);
    
          if (operation.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            System.out.println("Firewall rule creation failed ! ! " + operation.[getError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getError__)());
            return;
          }
    
          System.out.printf("Firewall rule created %s", firewallRuleName);
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
    
    
    def create_firewall_rule_for_windows_activation_host(
        project_id: str, firewall_rule_name: str, network: str = "global/networks/default"
    ) -> compute_v1.Firewall:
        """
        Creates an egress firewall rule with the highest priority for host
        kms.windows.googlecloud.com (35.190.247.13) for Windows activation.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            firewall_rule_name: name of the rule that is created.
            network: name of the network the rule will be applied to. Available name formats:
                * https://www.googleapis.com/compute/v1/projects/{project_id}/global/networks/{network}
                * projects/{project_id}/global/networks/{network}
                * global/networks/{network}
    
        Returns:
            A Firewall object.
        """
        firewall_rule = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[Firewall](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.Firewall.html)()
        firewall_rule.name = firewall_rule_name
        firewall_rule.network = network
    
        allowed = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[Allowed](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.Allowed.html)()
        allowed.ports = ["1688"]
        allowed.I_p_protocol = "tcp"
    
        firewall_rule.allowed = [allowed]
        firewall_rule.destination_ranges = ["35.190.247.13/32"]
        firewall_rule.direction = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[Firewall](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.Firewall.html).Direction.EGRESS.name
        firewall_rule.priority = 0
    
        firewall_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[FirewallsClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.firewalls.FirewallsClient.html)()
        operation = firewall_client.[insert](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.firewalls.FirewallsClient.html#google_cloud_compute_v1_services_firewalls_FirewallsClient_insert)(
            project=project_id, firewall_resource=firewall_rule
        )
    
        wait_for_extended_operation(operation, "windows KSM firewall rule creation")
    
        return firewall_client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.firewalls.FirewallsClient.html#google_cloud_compute_v1_services_firewalls_FirewallsClient_get)(project=project_id, firewall=firewall_rule_name)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
