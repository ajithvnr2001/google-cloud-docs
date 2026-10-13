---
url: https://docs.cloud.google.com/compute/docs/samples/compute-instances-list/
title: List VMs in a zone \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:29:15.397760+00:00
---

# List VMs in a zone  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-instances-list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  List VMs in a zone Stay organized with collections  Save and categorize content based on your preferences. 

Get a list of VMs in a specific zone in a project.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Compute Engine client libraries](https://docs.cloud.google.com/compute/docs/api/libraries)
  * [Using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries)



## Code sample

### C#

Before trying this sample, follow the C# setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Compute.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.html);
    using System;
    using System.Collections.Generic;
    using System.Threading.Tasks;
    
    public class ListZoneInstancesAsyncSample
    {
        public async Task<IList<Instance>> ListZoneInstancesAsync(
            // TODO(developer): Set your own default values for these parameters or pass different values when calling this method.
            string projectId = "your-project-id", 
            string zone = "us-central1-a")
        {
            // Initialize client that will be used to send requests. This client only needs to be created
            // once, and can be reused for multiple requests.
            [InstancesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstancesClient.html) client = await [InstancesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstancesClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstancesClient.html#Google_Cloud_Compute_V1_InstancesClient_CreateAsync_System_Threading_CancellationToken_)();
            IList<Instance> allInstances = new List<Instance>();
    
            // Make the request to list all VM instances in the given zone in the specified project.
            await foreach(var instance in client.[ListAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstancesClient.html#Google_Cloud_Compute_V1_InstancesClient_ListAsync_Google_Cloud_Compute_V1_ListInstancesRequest_Google_Api_Gax_Grpc_CallSettings_)(projectId, zone))
            {
                // The result is an Instance collection.
                Console.WriteLine($"Instance: {instance.Name}");
                allInstances.Add(instance);
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
    )
    
    // listInstances prints a list of instances created in given project in given zone.
    func listInstances(w io.Writer, projectID, zone string) error {
    	// projectID := "your_project_id"
    	// zone := "europe-central2-b"
    	ctx := context.Background()
    	instancesClient, err := compute.[NewInstancesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_InstancesClient_NewInstancesRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewInstancesRESTClient: %w", err)
    	}
    	defer instancesClient.Close()
    
    	req := &computepb.ListInstancesRequest{
    		Project: projectID,
    		Zone:    zone,
    	}
    
    	it := instancesClient.List(ctx, req)
    	fmt.Fprintf(w, "Instances found in zone %s:\n", zone)
    	for {
    		instance, err := it.Next()
    		if err == iterator.[Done](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_Operation_Done) {
    			break
    		}
    		if err != nil {
    			return err
    		}
    		fmt.Fprintf(w, "- %s %s\n", instance.GetName(), instance.GetMachineType())
    	}
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/overview). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.compute.v1.[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html);
    import com.google.cloud.compute.v1.[InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html);
    import java.io.IOException;
    
    public class ListInstance {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample
        String project = "your-project-id";
        String zone = "zone-name";
        listInstances(project, zone);
      }
    
      // List all instances in the given zone in the specified project ID.
      public static void listInstances(String project, String zone) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `instancesClient.close()` method on the client to 
        // safely clean up any remaining background resources.
        try ([InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html) instancesClient = [InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html).create()) {
          // Set the project and zone to retrieve instances present in the zone.
          System.out.printf("Listing instances from %s in %s:", project, zone);
          for ([Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html) zoneInstance : instancesClient.list(project, zone).iterateAll()) {
            System.out.println(zoneInstance.getName());
          }
          System.out.println("####### Listing instances complete #######");
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
    // const zone = 'europe-central2-b'
    
    const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    
    // List all instances in the given zone in the specified project.
    async function listInstances() {
      const instancesClient = new compute.[InstancesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      const [instanceList] = await instancesClient.list({
        project: projectId,
        zone,
      });
    
      console.log(`Instances found in zone ${zone}:`);
    
      for (const instance of instanceList) {
        console.log(` - ${instance.name} (${instance.machineType})`);
      }
    }
    
    listInstances();

### PHP

Before trying this sample, follow the PHP setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine PHP API reference documentation](https://docs.cloud.google.com/php/docs/reference/cloud-compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Compute\V1\Client\InstancesClient;
    use Google\Cloud\Compute\V1\ListInstancesRequest;
    
    /**
     * List all instances for a particular Cloud project and zone.
     *
     * @param string $projectId Your Google Cloud project ID.
     * @param string $zone Zone to list instances for (like "us-central1-a").
     *
     * @throws \Google\ApiCore\ApiException if the remote call fails.
     */
    function list_instances(string $projectId, string $zone)
    {
        // List Compute Engine instances using InstancesClient.
        $instancesClient = new InstancesClient();
        $request = (new ListInstancesRequest())
            ->setProject($projectId)
            ->setZone($zone);
        $instancesList = $instancesClient->list($request);
    
        printf('Instances for %s (%s)' . PHP_EOL, $projectId, $zone);
        foreach ($instancesList as $instance) {
            printf(' - %s' . PHP_EOL, $instance->getName());
        }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from __future__ import annotations
    
    from collections.abc import Iterable
    
    from google.cloud import compute_v1
    
    
    def list_instances(project_id: str, zone: str) -> Iterable[compute_v1.Instance]:
        """
        List all instances in the given zone in the specified project.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            zone: name of the zone you want to use. For example: “us-west3-b”
        Returns:
            An iterable collection of Instance objects.
        """
        instance_client = compute_v1.InstancesClient()
        instance_list = instance_client.list(project=project_id, zone=zone)
    
        print(f"Instances found in zone {zone}:")
        for instance in instance_list:
            print(f" - {instance.name} ({instance.machine_type})")
    
        return instance_list
    
    

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/compute/v1"
    
    # Lists all instances in the given zone in the specified project.
    #
    # @param [String] project project ID or project number of the Cloud project you want to use.
    # @param [String] zone name of the zone you want to use. For example: "us-west3-b"
    # @return [Array<::Google::Cloud::Compute::V1::Instance>] Array of instances.
    def list_instances project:, zone:
      # Initialize client that will be used to send requests. This client only needs to be created
      # once, and can be reused for multiple requests.
      client = ::Google::Cloud::Compute::V1::Instances::Rest::Client.new
    
      # Send the request to list all VM instances in the given zone in the specified project.
      instance_list = client.list project: project, zone: zone
    
      puts "Instances found in zone #{zone}:"
      instances = []
      instance_list.each do |instance|
        puts " - #{instance.name} (#{instance.machine_type})"
        instances << instance
      end
      instances
    end

### Rust
    
    
    pub async fn sample(project_id: &str) -> anyhow::Result<()> {
        use google_cloud_compute_v1::client::Instances;
        use google_cloud_gax::paginator::ItemPaginator;
    
        const ZONE: &str = "us-central1-a";
    
        let client = Instances::builder().build().await?;
        println!("Listing instances for project {project_id}");
        let mut instances = client
            .list()
            .set_project(project_id)
            .set_zone(ZONE)
            .by_item();
        while let Some(item) = instances.next().await.transpose()? {
            println!("  {:?}", item.name);
        }
        println!("DONE");
        Ok(())
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
