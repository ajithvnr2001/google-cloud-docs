---
url: https://docs.cloud.google.com/compute/docs/samples/compute-instances-list-all/
title: List all VM instances \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:33.515450+00:00
---

# List all VM instances  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-instances-list-all/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  List all VM instances Stay organized with collections  Save and categorize content based on your preferences. 

List all VM instances in a project, across all zones.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Get a list of VMs](https://docs.cloud.google.com/compute/docs/instances/get-list)
  * [Using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries)



## Code sample

### C#

Before trying this sample, follow the C# setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Compute.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.html);
    using System;
    using System.Collections.Generic;
    using System.Threading.Tasks;
    
    public class ListAllInstancesAsyncSample
    {
        public async Task<IList<Instance>> ListAllInstancesAsync(
            // TODO(developer): Set your own default values for these parameters or pass different values when calling this method.
            string projectId = "your-project-id") 
        {
            // Initialize client that will be used to send requests. This client only needs to be created
            // once, and can be reused for multiple requests.
            [InstancesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstancesClient.html) client = await [InstancesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstancesClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstancesClient.html#Google_Cloud_Compute_V1_InstancesClient_CreateAsync_System_Threading_CancellationToken_)();
            IList<Instance> allInstances = new List<Instance>();
    
            // Make the request to list all VM instances in a project.
            await foreach (var instancesByZone in client.[AggregatedListAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstancesClient.html#Google_Cloud_Compute_V1_InstancesClient_AggregatedListAsync_Google_Cloud_Compute_V1_AggregatedListInstancesRequest_Google_Api_Gax_Grpc_CallSettings_)(projectId))
            {
                // The result contains a KeyValuePair collection, where the key is a zone and the value
                // is a collection of instances in that zone.
                Console.WriteLine($"Instances for zone: {instancesByZone.Key}");
                foreach (var instance in instancesByZone.Value.[Instances](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Instances.html))
                {
                    Console.WriteLine($"-- Name: {instance.Name}");
                    allInstances.Add(instance);
                }
            }
    
            return allInstances;
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
    	"google.golang.org/protobuf/proto"
    )
    
    // listAllInstances prints all instances present in a project, grouped by their zone.
    func listAllInstances(w io.Writer, projectID string) error {
    	// projectID := "your_project_id"
    	ctx := context.Background()
    	instancesClient, err := compute.[NewInstancesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_InstancesClient_NewInstancesRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewInstancesRESTClient: %w", err)
    	}
    	defer instancesClient.Close()
    
    	// Use the `MaxResults` parameter to limit the number of results that the API returns per response page.
    	req := &computepb.AggregatedListInstancesRequest{
    		Project:    projectID,
    		MaxResults: proto.Uint32(3),
    	}
    
    	it := instancesClient.AggregatedList(ctx, req)
    	fmt.Fprintf(w, "Instances found:\n")
    	// Despite using the `MaxResults` parameter, you don't need to handle the pagination
    	// yourself. The returned iterator object handles pagination
    	// automatically, returning separated pages as you iterate over the results.
    	for {
    		pair, err := it.Next()
    		if err == iterator.[Done](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_Operation_Done) {
    			break
    		}
    		if err != nil {
    			return err
    		}
    		instances := pair.Value.Instances
    		if len(instances) > 0 {
    			fmt.Fprintf(w, "%s\n", pair.Key)
    			for _, instance := range instances {
    				fmt.Fprintf(w, "- %s %s\n", instance.GetName(), instance.GetMachineType())
    			}
    		}
    	}
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/overview). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.compute.v1.[AggregatedListInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListInstancesRequest.html);
    import com.google.cloud.compute.v1.[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html);
    import com.google.cloud.compute.v1.[InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html);
    import com.google.cloud.compute.v1.[InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html).AggregatedListPagedResponse;
    import com.google.cloud.compute.v1.[InstancesScopedList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesScopedList.html);
    import java.io.IOException;
    import java.util.Map;
    
    public class ListAllInstances {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample
        String project = "your-project-id";
        listAllInstances(project);
      }
    
      // List all instances in the specified project ID.
      public static AggregatedListPagedResponse listAllInstances(String project) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `instancesClient.close()` method on the client to
        // safely clean up any remaining background resources.
        try ([InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html) instancesClient = [InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html).create()) {
    
          // Use the `setMaxResults` parameter to limit the number of results
          // that the API returns per response page.
          [AggregatedListInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListInstancesRequest.html) aggregatedListInstancesRequest = [AggregatedListInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListInstancesRequest.html)
              .newBuilder()
              .setProject(project)
              .setMaxResults(5)
              .build();
    
          [InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html).AggregatedListPagedResponse response = instancesClient
              .aggregatedList(aggregatedListInstancesRequest);
    
          // Despite using the `setMaxResults` parameter, you don't need to handle the pagination
          // yourself. The returned `AggregatedListPager` object handles pagination
          // automatically, requesting next pages as you iterate over the results.
          for (Map.Entry<String, InstancesScopedList> zoneInstances : response.iterateAll()) {
            // Instances scoped by each zone
            String zone = zoneInstances.getKey();
            if (!zoneInstances.getValue().getInstancesList().isEmpty()) {
              // zoneInstances.getKey() returns the fully qualified address.
              // Hence, strip it to get the zone name only
              System.out.printf("Instances at %s: ", zone.substring(zone.lastIndexOf('/') + 1));
              for (Instance instance : zoneInstances.getValue().getInstancesList()) {
                System.out.println(instance.getName());
              }
            }
          }
          System.out.println("####### Listing all instances complete #######");
          return response;
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
    
    // List all instances in the specified project.
    async function listAllInstances() {
      const instancesClient = new compute.[InstancesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      //Use the `maxResults` parameter to limit the number of results that the API returns per response page.
      const aggListRequest = instancesClient.aggregatedListAsync({
        project: projectId,
        maxResults: 5,
      });
    
      console.log('Instances found:');
    
      // Despite using the `maxResults` parameter, you don't need to handle the pagination
      // yourself. The returned object handles pagination automatically,
      // requesting next pages as you iterate over the results.
      for await (const [zone, instancesObject] of aggListRequest) {
        const instances = instancesObject.instances;
    
        if (instances && instances.length > 0) {
          console.log(` ${zone}`);
          for (const instance of instances) {
            console.log(` - ${instance.name} (${instance.machineType})`);
          }
        }
      }
    }
    
    listAllInstances();

### PHP

Before trying this sample, follow the PHP setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine PHP API reference documentation](https://docs.cloud.google.com/php/docs/reference/cloud-compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Compute\V1\AggregatedListInstancesRequest;
    use Google\Cloud\Compute\V1\Client\InstancesClient;
    
    /**
     * List all instances for a particular Cloud project.
     *
     * @param string $projectId Your Google Cloud project ID.
     *
     * @throws \Google\ApiCore\ApiException if the remote call fails.
     */
    function list_all_instances(string $projectId)
    {
        // List Compute Engine instances using InstancesClient.
        $instancesClient = new InstancesClient();
        $request = (new AggregatedListInstancesRequest())
            ->setProject($projectId);
        $allInstances = $instancesClient->aggregatedList($request);
    
        printf('All instances for %s' . PHP_EOL, $projectId);
        foreach ($allInstances as $zone => $zoneInstances) {
            $instances = $zoneInstances->getInstances();
            if (count($instances) > 0) {
                printf('Zone - %s' . PHP_EOL, $zone);
                foreach ($instances as $instance) {
                    printf(' - %s' . PHP_EOL, $instance->getName());
                }
            }
        }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from __future__ import annotations
    
    from collections import defaultdict
    from collections.abc import Iterable
    
    from google.cloud import compute_v1
    
    
    def list_all_instances(
        project_id: str,
    ) -> dict[str, Iterable[compute_v1.Instance]]:
        """
        Returns a dictionary of all instances present in a project, grouped by their zone.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
        Returns:
            A dictionary with zone names as keys (in form of "zones/{zone_name}") and
            iterable collections of Instance objects as values.
        """
        instance_client = compute_v1.InstancesClient()
        request = compute_v1.AggregatedListInstancesRequest()
        request.project = project_id
        # Use the `max_results` parameter to limit the number of results that the API returns per response page.
        request.max_results = 50
    
        agg_list = instance_client.aggregated_list(request=request)
    
        all_instances = defaultdict(list)
        print("Instances found:")
        # Despite using the `max_results` parameter, you don't need to handle the pagination
        # yourself. The returned `AggregatedListPager` object handles pagination
        # automatically, returning separated pages as you iterate over the results.
        for zone, response in agg_list:
            if response.instances:
                all_instances[zone].extend(response.instances)
                print(f" {zone}:")
                for instance in response.instances:
                    print(f" - {instance.name} ({instance.machine_type})")
        return all_instances
    
    

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/compute/v1"
    
    # Returns a dictionary of all instances present in a project, grouped by their zone.
    #
    # @param [String] project project ID or project number of the Cloud project you want to use.
    # @return [Hash<String, Array<::Google::Cloud::Compute::V1::Instance>>] A hash with zone names
    #   as keys (in form of "zones/{zone_name}") and arrays of instances as values.
    def list_all_instances project:
      # Initialize client that will be used to send requests. This client only needs to be created
      # once, and can be reused for multiple requests.
      client = ::Google::Cloud::Compute::V1::Instances::Rest::Client.new
    
      # Send the request to list all VM instances in a project.
      agg_list = client.aggregated_list project: project
      all_instances = {}
      puts "Instances found:"
      # The result contains a Map collection, where the key is a zone and the value
      # is a collection of instances in that zone.
      agg_list.each do |zone, list|
        next if list.instances.empty?
        all_instances[zone] = list.instances
        puts " #{zone}:"
        list.instances.each do |instance|
          puts " - #{instance.name} (#{instance.machine_type})"
        end
      end
      all_instances
    end

### Rust
    
    
    use google_cloud_compute_v1::client::Instances;
    use google_cloud_gax::paginator::ItemPaginator;
    
    pub async fn sample(client: &Instances, project_id: &str) -> anyhow::Result<()> {
        let mut items = client.aggregated_list().set_project(project_id).by_item();
        while let Some((zone, scoped_list)) = items.next().await.transpose()? {
            for instance in scoped_list.instances {
                println!(
                    "Instance {} found in zone: {zone}",
                    instance.name.expect("name should be Some()")
                );
            }
        }
    
        Ok(())
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
