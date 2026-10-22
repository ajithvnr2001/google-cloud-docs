---
url: https://docs.cloud.google.com/compute/docs/samples/compute-firewall-list/
title: List firewall rules in a project \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:16.071961+00:00
---

# List firewall rules in a project  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-firewall-list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  List firewall rules in a project Stay organized with collections  Save and categorize content based on your preferences. 

Get a list of all firewall rules defined in your project.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Use VPC firewall rules](https://docs.cloud.google.com/firewall/docs/using-firewalls)



## Code sample

### C#

Before trying this sample, follow the C# setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Compute.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.html);
    using System;
    using System.Collections.Generic;
    using System.Threading.Tasks;
    
    public class ListFirewallRulesAsyncSample
    {
        public async Task ListFirewallRulesAsync(
            // TODO(developer): Set your own default values for these parameters or pass different values when calling this method.
            string projectId = "your-project-id")
        {
            // Initialize client that will be used to send requests. This client only needs to be created
            // once, and can be reused for multiple requests.
            [FirewallsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.FirewallsClient.html) client = await [FirewallsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.FirewallsClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.FirewallsClient.html#Google_Cloud_Compute_V1_FirewallsClient_CreateAsync_System_Threading_CancellationToken_)();
    
            // Make the request to list all firewall rules.
            await foreach (var firewallRule in client.[ListAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.FirewallsClient.html#Google_Cloud_Compute_V1_FirewallsClient_ListAsync_Google_Cloud_Compute_V1_ListFirewallsRequest_Google_Api_Gax_Grpc_CallSettings_)(projectId))
            {
                // The result is a Firewall sequence that you can iterate over.
                Console.WriteLine($"Firewal Rule: {firewallRule.Name}");
            }
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
    	"google.golang.org/api/iterator"
    )
    
    // listFirewallRules prints the list of firewall names and their descriptions in specified project
    func listFirewallRules(w io.Writer, projectID string) error {
    	// projectID := "your_project_id"
    
    	ctx := context.Background()
    	firewallsClient, err := compute.[NewFirewallsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_FirewallsClient_NewFirewallsRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewInstancesRESTClient: %w", err)
    	}
    	defer firewallsClient.Close()
    
    	req := &computepb.ListFirewallsRequest{
    		Project: projectID,
    	}
    
    	it := firewallsClient.List(ctx, req)
    	for {
    		firewallRule, err := it.Next()
    		if err == iterator.[Done](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_Operation_Done) {
    			break
    		}
    		if err != nil {
    			return err
    		}
    		fmt.Fprintf(w, "- %s: %s\n", firewallRule.GetName(), firewallRule.GetDescription())
    	}
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/overview). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.compute.v1.[Firewall](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Firewall.html);
    import com.google.cloud.compute.v1.[FirewallsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallsClient.html);
    import com.google.cloud.compute.v1.[FirewallsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallsClient.html).ListPagedResponse;
    import java.io.IOException;
    
    public class ListFirewallRules {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample
        // project: project ID or project number of the Cloud project you want to use.
        String project = "your-project-id";
        listFirewallRules(project);
      }
    
      // Return a list of all the firewall rules in specified project.
      // Also prints the list of firewall names and their descriptions.
      public static ListPagedResponse listFirewallRules(String project)
          throws IOException {
        /* Initialize client that will be used to send requests. This client only needs to be created
           once, and can be reused for multiple requests. After completing all of your requests, call
           the `firewallsClient.close()` method on the client to safely
           clean up any remaining background resources. */
        try ([FirewallsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallsClient.html) firewallsClient = [FirewallsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallsClient.html).create()) {
          ListPagedResponse firewallResponse = firewallsClient.list(project);
          for ([Firewall](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Firewall.html) firewall : firewallResponse.iterateAll()) {
            System.out.println(firewall.getName());
          }
          return firewallResponse;
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
    
    const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    
    async function listFirewallRules() {
      const firewallsClient = new compute.[FirewallsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      const [firewallRules] = await firewallsClient.list({
        project: projectId,
      });
    
      for (const rule of firewallRules) {
        console.log(` - ${rule.name}: ${rule.description}`);
      }
    }
    
    listFirewallRules();

### PHP

Before trying this sample, follow the PHP setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine PHP API reference documentation](https://docs.cloud.google.com/php/docs/reference/cloud-compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Compute\V1\Client\FirewallsClient;
    use Google\Cloud\Compute\V1\ListFirewallsRequest;
    
    /**
     * Return a list of all the firewall rules in specified project. Also prints the
     * list of firewall names and their descriptions.
     *
     * @param string $projectId Project ID or project number of the Cloud project you want to list rules from.
     *
     * @throws \Google\ApiCore\ApiException if the remote call fails.
     */
    function list_firewall_rules(string $projectId)
    {
        // List all firewall rules defined for the project using Firewalls Client.
        $firewallClient = new FirewallsClient();
        $request = (new ListFirewallsRequest())
            ->setProject($projectId);
        $firewallList = $firewallClient->list($request);
    
        print('--- Firewall Rules ---' . PHP_EOL);
        foreach ($firewallList->iterateAllElements() as $firewall) {
            printf(' -  %s : %s : %s' . PHP_EOL, $firewall->getName(), $firewall->getDescription(), $firewall->getNetwork());
        }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from __future__ import annotations
    
    from collections.abc import Iterable
    
    from google.cloud import compute_v1
    
    
    def list_firewall_rules(project_id: str) -> Iterable[compute_v1.Firewall]:
        """
        Return a list of all the firewall rules in specified project. Also prints the
        list of firewall names and their descriptions.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
    
        Returns:
            A flat list of all firewall rules defined for given project.
        """
        firewall_client = compute_v1.FirewallsClient()
        firewalls_list = firewall_client.list(project=project_id)
    
        for firewall in firewalls_list:
            print(f" - {firewall.name}: {firewall.description}")
    
        return firewalls_list
    
    

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/compute/v1"
    
    # Return a list of all the firewall rules in specified project. Also prints the
    # list of firewall names and their descriptions.
    #
    # @param [String] project project ID or project number of the project you want to use.
    # @return [Array<::Google::Cloud::Compute::V1::Firewall>]
    #     A list of all firewall rules defined for the given project.
    def list_firewall_rules project:
      client = ::Google::Cloud::Compute::V1::Firewalls::Rest::Client.new
      firewalls = client.list project: project
    
      firewall_list = []
      firewalls.each do |firewall|
        puts " - #{firewall.name}: #{firewall.description}"
        firewall_list << firewall
      end
    
      firewall_list
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
