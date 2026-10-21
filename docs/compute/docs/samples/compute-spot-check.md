---
url: https://docs.cloud.google.com/compute/docs/samples/compute-spot-check/
title: Check if a given instance is Spot VM or not \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:14:08.754504+00:00
---

# Check if a given instance is Spot VM or not  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-spot-check/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  Check if a given instance is Spot VM or not Stay organized with collections  Save and categorize content based on your preferences. 

This sample checks if a given instance is Spot VM or not.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create and use Spot VMs](https://docs.cloud.google.com/compute/docs/instances/create-use-spot)



## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	"cloud.google.com/go/compute/apiv1/computepb"
    )
    
    // isSpotVM checks if a given instance is a Spot VM or not.
    func isSpotVM(w io.Writer, projectID, zone, instanceName string) (bool, error) {
    	// projectID := "your_project_id"
    	// zone := "europe-central2-b"
    	// instanceName := "your_instance_name"
    	ctx := context.Background()
    	client, err := compute.[NewInstancesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_InstancesClient_NewInstancesRESTClient)(ctx)
    	if err != nil {
    		return false, fmt.Errorf("NewInstancesRESTClient: %w", err)
    	}
    	defer client.Close()
    
    	req := &computepb.GetInstanceRequest{
    		Project:  projectID,
    		Zone:     zone,
    		Instance: instanceName,
    	}
    
    	instance, err := client.Get(ctx, req)
    	if err != nil {
    		return false, fmt.Errorf("GetInstance: %w", err)
    	}
    
    	isSpot := instance.GetScheduling().GetProvisioningModel() == computepb.[Scheduling_SPOT](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1/computepb.html#cloud_google_com_go_compute_apiv1_computepb_Scheduling_UNDEFINED_PROVISIONING_MODEL_Scheduling_FLEX_START_Scheduling_RESERVATION_BOUND_Scheduling_SPOT_Scheduling_STANDARD).String()
    
    	var isSpotMessage string
    	if !isSpot {
    		isSpotMessage = " not"
    	}
    	fmt.Fprintf(w, "Instance %s is%s spot\n", instanceName, isSpotMessage)
    
    	return instance.GetScheduling().GetProvisioningModel() == computepb.[Scheduling_SPOT](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1/computepb.html#cloud_google_com_go_compute_apiv1_computepb_Scheduling_UNDEFINED_PROVISIONING_MODEL_Scheduling_FLEX_START_Scheduling_RESERVATION_BOUND_Scheduling_SPOT_Scheduling_STANDARD).String(), nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/overview). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.compute.v1.[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html);
    import com.google.cloud.compute.v1.[InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html);
    import com.google.cloud.compute.v1.[Scheduling](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Scheduling.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeoutException;
    
    public class CheckIsSpotVm {
      public static void main(String[] args)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Google Cloud project you want to use.
        String projectId = "your-project-id";
        // Name of the virtual machine to check.
        String instanceName = "your-route-name";
        // Name of the zone you want to use. For example: "us-west3-b"
        String zone = "your-zone";
    
        boolean isSpotVm = isSpotVm(projectId, instanceName, zone);
        System.out.printf("Is %s spot VM instance - %s", instanceName, isSpotVm);
      }
    
      // Check if a given instance is Spot VM or not.
      public static boolean isSpotVm(String projectId, String instanceName, String zone)
              throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html) client = [InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html).create()) {
          [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html) instance = client.get(projectId, zone, instanceName);
    
          return instance.[getScheduling](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html#com_google_cloud_compute_v1_Instance_getScheduling__)().getProvisioningModel()
                  .equals([Scheduling](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Scheduling.html).ProvisioningModel.SPOT.name());
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest)
    
    
    def is_spot_vm(project_id: str, zone: str, instance_name: str) -> bool:
        """
        Check if a given instance is Spot VM or not.
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            zone: name of the zone you want to use. For example: "us-west3-b"
            instance_name: name of the virtual machine to check.
        Returns:
            The Spot VM status of the instance.
        """
        instance_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html)()
        instance = instance_client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html#google_cloud_compute_v1_services_instances_InstancesClient_get)(
            project=project_id, zone=zone, instance=instance_name
        )
        return (
            instance.scheduling.provisioning_model
            == [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[Scheduling](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.Scheduling.html).ProvisioningModel.SPOT.name
        )
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
