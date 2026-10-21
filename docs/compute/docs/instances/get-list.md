---
url: https://docs.cloud.google.com/compute/docs/instances/get-list/
title: Get a list of VMs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:00:07.429089+00:00
---

# Get a list of VMs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/get-list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Get a list of VMs Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

To view a summary of VMs running in your project, get a list of VMs. This document shows you how to get a list of VMs in all zones or in specific zones.

## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### Go

To use the Go samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development). 

### Java

To use the Java samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development). 

### Node.js

To use the Node.js samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development). 

### Python

To use the Python samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development). 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Get a list of VMs

###  Console 

In the Google Cloud console, go to the **VM instances** page:

[Go to VM instances](https://console.cloud.google.com/compute/instances)

###  gcloud 

Get an aggregate list of all VMs in all zones for a project by using the [`gcloud compute instances list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/list):
    
    
    gcloud compute instances list
    

To narrow the list of VMs to a specific zone, use the previous command with the [`--zones` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/list#--zones).

###  Go 

The following example get a list of instances across all zones in your project:

Before trying this sample, follow the Go setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/compute/docs/authentication#client-libs). 
    
    
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
    	instancesClient, err := compute.NewInstancesRESTClient(ctx)
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
    		if err == iterator.Done {
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
    

You can also get a list instances in a specific zone:
    
    
    // Copyright 2021 Google LLC
    //
    // Licensed under the Apache License, Version 2.0 (the "License");
    // you may not use this file except in compliance with the License.
    // You may obtain a copy of the License at
    //
    //     https://www.apache.org/licenses/LICENSE-2.0
    //
    // Unless required by applicable law or agreed to in writing, software
    // distributed under the License is distributed on an "AS IS" BASIS,
    // WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    // See the License for the specific language governing permissions and
    // limitations under the License.
    
    package snippets
    
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
    	instancesClient, err := compute.NewInstancesRESTClient(ctx)
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
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return err
    		}
    		fmt.Fprintf(w, "- %s %s\n", instance.GetName(), instance.GetMachineType())
    	}
    	return nil
    }
    
    

###  Java 

The following example get a list of instances across all zones in your project:

Before trying this sample, follow the Java setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/overview). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/compute/docs/authentication#client-libs). 
    
    
    import com.google.cloud.compute.v1.AggregatedListInstancesRequest;
    import com.google.cloud.compute.v1.Instance;
    import com.google.cloud.compute.v1.InstancesClient;
    import com.google.cloud.compute.v1.InstancesClient.AggregatedListPagedResponse;
    import com.google.cloud.compute.v1.InstancesScopedList;
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
        try (InstancesClient instancesClient = InstancesClient.create()) {
    
          // Use the `setMaxResults` parameter to limit the number of results
          // that the API returns per response page.
          AggregatedListInstancesRequest aggregatedListInstancesRequest = AggregatedListInstancesRequest
              .newBuilder()
              .setProject(project)
              .setMaxResults(5)
              .build();
    
          InstancesClient.AggregatedListPagedResponse response = instancesClient
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

You can also get a list instances in a specific zone:
    
    
    /*
     * Copyright 2021 Google LLC
     *
     * Licensed under the Apache License, Version 2.0 (the "License");
     * you may not use this file except in compliance with the License.
     * You may obtain a copy of the License at
     *
     * http://www.apache.org/licenses/LICENSE-2.0
     *
     * Unless required by applicable law or agreed to in writing, software
     * distributed under the License is distributed on an "AS IS" BASIS,
     * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
     * See the License for the specific language governing permissions and
     * limitations under the License.
     */
    
    package compute;
    
    
    import com.google.cloud.compute.v1.Instance;
    import com.google.cloud.compute.v1.InstancesClient;
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
        try (InstancesClient instancesClient = InstancesClient.create()) {
          // Set the project and zone to retrieve instances present in the zone.
          System.out.printf("Listing instances from %s in %s:", project, zone);
          for (Instance zoneInstance : instancesClient.list(project, zone).iterateAll()) {
            System.out.println(zoneInstance.getName());
          }
          System.out.println("####### Listing instances complete #######");
        }
      }
    }
    

###  Node.js 

The following example get a list of instances across all zones in your project:

Before trying this sample, follow the Node.js setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/compute/docs/authentication#client-libs). 
    
    
    /**
     * TODO(developer): Uncomment and replace these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    
    const compute = require('@google-cloud/compute');
    
    // List all instances in the specified project.
    async function listAllInstances() {
      const instancesClient = new compute.InstancesClient();
    
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

You can also get a list instances in a specific zone:
    
    
    // Copyright 2021 Google LLC
    //
    // Licensed under the Apache License, Version 2.0 (the "License");
    // you may not use this file except in compliance with the License.
    // You may obtain a copy of the License at
    //
    //      http://www.apache.org/licenses/LICENSE-2.0
    //
    // Unless required by applicable law or agreed to in writing, software
    // distributed under the License is distributed on an "AS IS" BASIS,
    // WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    // See the License for the specific language governing permissions and
    // limitations under the License.
    
    /**
     * Gets a list of instances created in given project in given zone.
     *
     * @param {string} projectId - ID or number of the project you want to use.
     * @param {string} zone - Name of the zone you want to check, for example: us-west3-b
     */
    function main(projectId, zone) {
      /**
       * TODO(developer): Uncomment and replace these variables before running the sample.
       */
      // const projectId = 'YOUR_PROJECT_ID';
      // const zone = 'europe-central2-b'
    
      const compute = require('@google-cloud/compute');
    
      // List all instances in the given zone in the specified project.
      async function listInstances() {
        const instancesClient = new compute.InstancesClient();
    
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
    }
    
    main(...process.argv.slice(2));
    

###  Python 

The following example get a list of instances across all zones in your project:

Before trying this sample, follow the Python setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/compute/docs/authentication#client-libs). 
    
    
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
    
    

You can also get a list instances in a specific zone:
    
    
    #  Copyright 2022 Google LLC
    #
    #  Licensed under the Apache License, Version 2.0 (the "License");
    #  you may not use this file except in compliance with the License.
    #  You may obtain a copy of the License at
    #
    #      http://www.apache.org/licenses/LICENSE-2.0
    #
    #  Unless required by applicable law or agreed to in writing, software
    #  distributed under the License is distributed on an "AS IS" BASIS,
    #  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    #  See the License for the specific language governing permissions and
    #  limitations under the License.
    # flake8: noqa
    
    
    # This file is automatically generated. Please do not modify it directly.
    # Find the relevant recipe file in the samples/recipes or samples/ingredients
    # directory and apply your changes there.
    
    
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
    
    
    

###  REST 

Get an aggregate list of all VMs in all zones in a project by using the [`instances.aggregatedList` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/aggregatedList):
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT/aggregated/instances
    

Replace `PROJECT` with the name of the project to get a list of VMs from.

To narrow the list of VMs to a specific zone, use the [`instances.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/list):
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT/zones/ZONE/instances
    

Replace the following:

  * `PROJECT`: the name of the project to get a list of VMs from

  * `ZONE`: the zone to get a list of VMs from




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
