---
url: https://docs.cloud.google.com/compute/docs/samples/compute-preemptible-history/
title: List preemption history of a Google Compute Engine instance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:44.067439+00:00
---

# List preemption history of a Google Compute Engine instance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-preemptible-history/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  List preemption history of a Google Compute Engine instance Stay organized with collections  Save and categorize content based on your preferences. 

This sample lists all preemption operations that happened in a given zone in a project. Optionally, you can filter the results to only include operations for a specific instance.

## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"strings"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    	"google.golang.org/api/iterator"
    	"google.golang.org/protobuf/proto"
    )
    
    // preemptionHisory gets a list of preemption operations from given zone in a project.
    // Optionally limit the results to instance name.
    func preemptionHisory(w io.Writer, projectID, zone, instanceName, customFilter string) error {
    	// projectID := "your_project_id"
    	// zone := "europe-central2-b"
    	// instanceName := "your_instance_name"
    	// customFilter := "operationType=\"compute.instances.preempted\""
    
    	ctx := context.Background()
    	operationsClient, err := compute.[NewZoneOperationsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_ZoneOperationsClient_NewZoneOperationsRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewZoneOperationsRESTClient: %w", err)
    	}
    	defer operationsClient.Close()
    
    	filter := ""
    
    	if customFilter != "" {
    		filter = customFilter
    	} else {
    		filter = "operationType=\"compute.instances.preempted\""
    
    		if instanceName != "" {
    			filter += fmt.Sprintf(
    				` AND targetLink="https://www.googleapis.com/compute/v1/projects/%s/zones/%s/instances/%s"`,
    				projectID, zone, instanceName,
    			)
    		}
    	}
    
    	req := &computepb.ListZoneOperationsRequest{
    		Project: projectID,
    		Zone:    zone,
    		Filter:  proto.String(filter),
    	}
    
    	it := operationsClient.List(ctx, req)
    	for {
    		operation, err := it.Next()
    		if err == iterator.[Done](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_Operation_Done) {
    			break
    		}
    		if err != nil {
    			return err
    		}
    
    		ss := strings.Split(operation.GetTargetLink(), "/")
    		curInstName := ss[len(ss)-1]
    		if curInstName == instanceName {
    			// The filter used is not 100% accurate, it's `contains` not `equals`
    			// So we need to check the name to make sure it's the one we want.
    			fmt.Fprintf(w, "- %s %s\n", instanceName, operation.GetInsertTime())
    		}
    	}
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/overview). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.compute.v1.[ListZoneOperationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListZoneOperationsRequest.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import com.google.cloud.compute.v1.[ZoneOperationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ZoneOperationsClient.html);
    import com.google.cloud.compute.v1.[ZoneOperationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ZoneOperationsClient.html).ListPagedResponse;
    import java.io.IOException;
    import java.time.Instant;
    import java.time.format.DateTimeFormatter;
    import java.util.ArrayList;
    import java.util.Arrays;
    import java.util.List;
    
    public class ListZoneOperations {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        // projectId: project ID or project number of the Cloud project you want to use.
        // zone: name of the zone you want to use. For example: “us-west3-b”
        // instanceName: name of the virtual machine to look for.
        String projectId = "your-project-id-or-number";
        String zone = "zone-name";
        String instanceName = "instance-name";
    
        preemptionHistory(projectId, zone, instanceName);
      }
    
    
      // List all recent operations that happened in given zone in a project. Optionally filter those
      // operations by providing a filter. More about using the filter can be found here:
      // https://cloud.google.com/compute/docs/reference/rest/v1/zoneOperations/list
      public static ListPagedResponse listZoneOperations(String projectId, String zone, String filter)
          throws IOException {
    
        try (Zone[ZoneOperationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ZoneOperationsClient.html)eOperationsClient = Zone[ZoneOperationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ZoneOperationsClient.html)ate()) {
          List[ListZoneOperationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListZoneOperationsRequest.html)uest = List[ListZoneOperationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListZoneOperationsRequest.html)Builder()
              .setProject(projectId)
              .setZone(zone)
              .setFilter(filter)
              .build();
    
          return zoneOperationsClient.list(request);
        }
      }
    
    
      // Get a list of preemption operations from given zone in a project. Optionally limit
      // the results to instance name.
      private static void preemptionHistory(String projectId, String zone, String instanceName)
          throws IOException {
    
        String filter;
        String thisInstanceName;
        String targetLink;
        List<List<String>> history = new ArrayList<>();
    
        if (instanceName != null && instanceName.length() != 0) {
          filter = String.format(
              "operationType=\"compute.instances.preempted\" AND targetLink:instances/%s",
              instanceName);
        } else {
          filter = "operationType=\"compute.instances.preempted\"";
        }
    
        for (Oper[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html)ration : listZoneOperations(projectId, zone, filter).iterateAll()) {
          targetLink = operation.getTargetLink();
          thisInstanceName = targetLink.substring(targetLink.lastIndexOf("/") + 1);
    
          // The filter used above performs a 'contains' operation instead of 'equals'
          // So, the result (thisInstanceName) might not be tightly coupled with instanceName.
          // Hence, we need to check the name to make sure it's the one we want.
          if (thisInstanceName.equalsIgnoreCase(instanceName)) {
            Instant instant = Instant.from(
                DateTimeFormatter.ISO_INSTANT.parse(operation.getInsertTime()));
            history.add(new ArrayList<>(Arrays.asList(instanceName, instant.toString())));
          }
        }
    
        System.out.println("Retrieved preemption history: " + history);
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment and replace these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const zone = 'europe-central2-b';
    // const instanceName = 'YOUR_INSTANCE_NAME';
    // const customFilter = 'operationType="compute.instances.preempted"';
    
    const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    
    async function preemptionHistory() {
      const zoneOperationsClient = new compute.[ZoneOperationsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      let filter;
    
      if (customFilter !== '') {
        filter = customFilter;
      } else {
        filter = 'operationType="compute.instances.preempted"';
    
        if (instanceName !== '') {
          filter += ` AND targetLink="https://www.googleapis.com/compute/v1/projects/${projectId}/zones/${zone}/instances/${instanceName}"`;
        }
      }
    
      const [operationsList] = await zoneOperationsClient.list({
        project: projectId,
        zone,
        filter,
      });
    
      for (const operation of operationsList) {
        const thisInstanceName = operation.targetLink.split('/').pop();
        if (thisInstanceName === instanceName) {
          // The filter used is not 100% accurate, it's `contains` not `equals`
          // So we need to check the name to make sure it's the one we want.
          console.log(`- ${instanceName} ${operation.insertTime}`);
        }
      }
    }
    
    preemptionHistory();

### Python

Before trying this sample, follow the Python setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from __future__ import annotations
    
    import datetime
    
    from google.cloud import compute_v1
    from google.cloud.compute_v1.services.zone_operations import pagers
    
    
    def list_zone_operations(
        project_id: str, zone: str, filter: str = ""
    ) -> pagers.ListPager:
        """
        List all recent operations the happened in given zone in a project. Optionally filter those
        operations by providing a filter. More about using the filter can be found here:
        https://cloud.google.com/compute/docs/reference/rest/v1/zoneOperations/list
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            zone: name of the zone you want to use. For example: "us-west3-b"
            filter: filter string to be used for this listing operation.
        Returns:
            List of preemption operations in given zone.
        """
        operation_client = compute_v1.ZoneOperationsClient()
        request = compute_v1.ListZoneOperationsRequest()
        request.project = project_id
        request.zone = zone
        request.filter = filter
    
        return operation_client.list(request)
    
    
    def preemption_history(
        project_id: str, zone: str, instance_name: str = None
    ) -> list[tuple[str, datetime.datetime]]:
        """
        Get a list of preemption operations from given zone in a project. Optionally limit
        the results to instance name.
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            zone: name of the zone you want to use. For example: "us-west3-b"
            instance_name: name of the virtual machine to look for.
        Returns:
            List of preemption operations in given zone.
        """
        if instance_name:
            filter = (
                f'operationType="compute.instances.preempted" '
                f"AND targetLink:instances/{instance_name}"
            )
        else:
            filter = 'operationType="compute.instances.preempted"'
    
        history = []
    
        for operation in list_zone_operations(project_id, zone, filter):
            this_instance_name = operation.target_link.rsplit("/", maxsplit=1)[1]
            if instance_name and this_instance_name == instance_name:
                # The filter used is not 100% accurate, it's `contains` not `equals`
                # So we need to check the name to make sure it's the one we want.
                moment = datetime.datetime.fromisoformat(operation.insert_time)
                history.append((instance_name, moment))
    
        return history
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
