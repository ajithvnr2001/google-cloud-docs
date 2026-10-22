---
url: https://docs.cloud.google.com/compute/docs/samples/compute-firewall-patch/
title: Update a firewall rule \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:50:31.505514+00:00
---

# Update a firewall rule  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-firewall-patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  Update a firewall rule Stay organized with collections  Save and categorize content based on your preferences. 

Modify the priority of a firewall rule.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Use VPC firewall rules](https://docs.cloud.google.com/firewall/docs/using-firewalls)



## Code sample

### C#

Before trying this sample, follow the C# setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Compute.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.html);
    using System.Threading.Tasks;
    
    public class PatchFirewallRuleAsyncSample
    {
        public async Task PatchFirewallRuleAsync(
            // TODO(developer): Set your own default values for these parameters or pass different values when calling this method.
            string projectId = "your-project-id",
            string firewallRuleName = "my-test-firewall-rule",
            int newPriority = 10)
        {
            // The patch operation doesn't require the full definition of a Firewall object.
            // It will only update the values that were set in it,
            // in this case it will only change the priority.
            [Firewall](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Firewall.html) firewallRule = new [Firewall](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Firewall.html)
            {
                Priority = newPriority
            };
    
            // Initialize client that will be used to send requests. This client only needs to be created
            // once, and can be reused for multiple requests.
            [FirewallsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.FirewallsClient.html) client = await [FirewallsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.FirewallsClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.FirewallsClient.html#Google_Cloud_Compute_V1_FirewallsClient_CreateAsync_System_Threading_CancellationToken_)();
    
            // Patch the firewall rule in the specified project.
            var firewallRulePatching = await client.[PatchAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.FirewallsClient.html#Google_Cloud_Compute_V1_FirewallsClient_PatchAsync_Google_Cloud_Compute_V1_PatchFirewallRequest_Google_Api_Gax_Grpc_CallSettings_)(projectId, firewallRuleName, firewallRule);
    
            // Wait for the operation to complete using client-side polling.
            await firewallRulePatching.PollUntilCompletedAsync();
        }
    }
    

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
    
    // patchFirewallPriority modifies the priority of a given firewall rule.
    func patchFirewallPriority(w io.Writer, projectID, firewallRuleName string, priority int32) error {
    	// projectID := "your_project_id"
    	// firewallRuleName := "europe-central2-b"
    	// priority := 10
    
    	ctx := context.Background()
    	firewallsClient, err := compute.[NewFirewallsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_FirewallsClient_NewFirewallsRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewInstancesRESTClient: %w", err)
    	}
    	defer firewallsClient.Close()
    
    	firewallRule := &computepb.Firewall{
    		Priority: proto.Int32(priority),
    	}
    
    	req := &computepb.PatchFirewallRequest{
    		Project:          projectID,
    		Firewall:         firewallRuleName,
    		FirewallResource: firewallRule,
    	}
    
    	// The patch operation doesn't require the full definition of a Firewall interface. It will only update
    	// the values that were set in it, in this case it will only change the priority.
    	op, err := firewallsClient.Patch(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to patch firewall rule: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Firewall rule updated\n")
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/overview). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.compute.v1.[Firewall](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Firewall.html);
    import com.google.cloud.compute.v1.[FirewallsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallsClient.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import com.google.cloud.compute.v1.[PatchFirewallRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchFirewallRequest.html);
    import java.io.IOException;
    import java.util.UUID;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class PatchFirewallRule {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample
        // project: project ID or project number of the Cloud project you want to use.
        // firewallRuleName: name of the rule you want to modify.
        // priority: the new priority to be set for the rule.
        String project = "your-project-id";
        String firewallRuleName = "firewall-rule-name-" + UUID.randomUUID();
        int priority = 10;
    
        patchFirewallPriority(project, firewallRuleName, priority);
      }
    
      // Modifies the priority of a given firewall rule.
      public static void patchFirewallPriority(String project, String firewallRuleName, int priority)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        /* Initialize client that will be used to send requests. This client only needs to be created
           once, and can be reused for multiple requests. After completing all of your requests, call
           the `firewallsClient.close()` method on the client to safely
           clean up any remaining background resources. */
        try ([FirewallsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallsClient.html) firewallsClient = [FirewallsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallsClient.html).create()) {
    
          /* The patch operation doesn't require the full definition of a Firewall object. It will only 
             update the values that were set in it, in this case it will only change the priority. */
          [Firewall](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Firewall.html) firewall = [Firewall](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Firewall.html).newBuilder()
              .setPriority(priority).build();
    
          [PatchFirewallRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchFirewallRequest.html) patchFirewallRequest = [PatchFirewallRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchFirewallRequest.html).newBuilder()
              .setProject(project)
              .setFirewall(firewallRuleName)
              .setFirewallResource(firewall).build();
    
          OperationFuture<Operation, Operation> operation = firewallsClient.patchAsync(
              patchFirewallRequest);
          operation.get(3, TimeUnit.MINUTES);
          System.out.println("Firewall Patch applied successfully ! ");
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment and replace these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const firewallRuleName = 'FIREWALL_RULE_NAME';
    // const priority = 10;
    
    const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    const computeProtos = compute.protos.google.cloud.compute.v1;
    
    async function patchFirewallPriority() {
      const firewallsClient = new compute.[FirewallsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
      const operationsClient = new compute.[GlobalOperationsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      const firewallRule = new computeProtos.Firewall();
      firewallRule.priority = priority;
    
      // The patch operation doesn't require the full definition of a Firewall object. It will only update
      // the values that were set in it, in this case it will only change the priority.
      const [response] = await firewallsClient.patch({
        project: projectId,
        firewall: firewallRuleName,
        firewallResource: firewallRule,
      });
      let operation = response.latestResponse;
    
      // Wait for the create operation to complete.
      while (operation.status !== 'DONE') {
        [operation] = await operationsClient.wait({
          operation: operation.name,
          project: projectId,
        });
      }
    
      console.log('Firewall rule updated');
    }
    
    patchFirewallPriority();

### PHP

Before trying this sample, follow the PHP setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine PHP API reference documentation](https://docs.cloud.google.com/php/docs/reference/cloud-compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Compute\V1\Client\FirewallsClient;
    use Google\Cloud\Compute\V1\Firewall;
    use Google\Cloud\Compute\V1\PatchFirewallRequest;
    
    /**
     * Modifies the priority of a given firewall rule.
     *
     * @param string $projectId Project ID or project number of the Cloud project you want to patch a rule from.
     * @param string $firewallRuleName Name of the rule that you want to modify.
     * @param int $priority The new priority to be set for the rule.
     *
     * @throws \Google\ApiCore\ApiException if the remote call fails.
     * @throws \Google\ApiCore\ValidationException if local error occurs before remote call.
     */
    function patch_firewall_priority(string $projectId, string $firewallRuleName, int $priority)
    {
        $firewallsClient = new FirewallsClient();
        $firewallResource = (new Firewall())->setPriority($priority);
    
        // The patch operation doesn't require the full definition of a Firewall object. It will only update
        // the values that were set in it, in this case it will only change the priority.
        $request = (new PatchFirewallRequest())
            ->setFirewall($firewallRuleName)
            ->setFirewallResource($firewallResource)
            ->setProject($projectId);
        $operation = $firewallsClient->patch($request);
    
        // Wait for the operation to complete.
        $operation->pollUntilComplete();
        if ($operation->operationSucceeded()) {
            printf('Patched %s priority to %d.' . PHP_EOL, $firewallRuleName, $priority);
        } else {
            $error = $operation->getError();
            printf('Patching failed: %s' . PHP_EOL, $error?->getMessage());
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
    
    
    def patch_firewall_priority(
        project_id: str, firewall_rule_name: str, priority: int
    ) -> None:
        """
        Modifies the priority of a given firewall rule.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            firewall_rule_name: name of the rule you want to modify.
            priority: the new priority to be set for the rule.
        """
        firewall_rule = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[Firewall](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.Firewall.html)()
        firewall_rule.priority = priority
    
        # The patch operation doesn't require the full definition of a Firewall object. It will only update
        # the values that were set in it, in this case it will only change the priority.
        firewall_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[FirewallsClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.firewalls.FirewallsClient.html)()
        operation = firewall_client.[patch](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.firewalls.FirewallsClient.html#google_cloud_compute_v1_services_firewalls_FirewallsClient_patch)(
            project=project_id, firewall=firewall_rule_name, firewall_resource=firewall_rule
        )
    
        wait_for_extended_operation(operation, "firewall rule patching")
    
    

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/compute/v1"
    
    # Modifies the priority of a given firewall rule.
    #
    # @param [String] project project ID or project number of the Cloud project you want to use.
    # @param [String] name name of the rule you want to modify.
    # @param [Google::Protobuf::RepeatedField] allowed the repeated instances of the Allowed field in the rule.
    #         Compute errors out if allowed is empty.
    # @param [Integer] priority the new priority to be set for the rule.
    def patch_firewall_priority project:, name:, allowed:, priority:
      allowed_arr = allowed.map do |instance|
        {
          I_p_protocol: instance.I_p_protocol,
          ports: instance.ports.to_a
        }
      end.to_a
    
      rule = {
        priority: priority,
        allowed: allowed_arr
      }
    
      request = {
        project: project,
        firewall: name,
        firewall_resource: rule
      }
    
      # The patch operation doesn't require the full definition of a Firewall object. It will only update
      # the values that were set in it, in this case it will only change the priority.
      client = ::Google::Cloud::Compute::V1::Firewalls::Rest::Client.new
      operation = client.patch request
    
      wait_until_done operation: operation
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
