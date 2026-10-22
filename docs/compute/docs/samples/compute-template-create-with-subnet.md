---
url: https://docs.cloud.google.com/compute/docs/samples/compute-template-create-with-subnet/
title: Create an instance template with a subnet \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:50:15.633077+00:00
---

# Create an instance template with a subnet  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-template-create-with-subnet/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  Create an instance template with a subnet Stay organized with collections  Save and categorize content based on your preferences. 

Create an instance template that uses a specified subnetwork.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create instance templates](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates)



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
    
    // createTemplateWithSubnet creates an instance template that uses a provided subnet.
    func createTemplateWithSubnet(w io.Writer, projectID, network, subnetwork, templateName string) error {
    	// projectID := "your_project_id"
    	// network := "projects/project/global/networks/network"
    	// subnetwork := "projects/project/regions/region/subnetworks/subnetwork"
    	// templateName := "your_template_name"
    
    	ctx := context.Background()
    	instanceTemplatesClient, err := compute.[NewInstanceTemplatesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_InstanceTemplatesClient_NewInstanceTemplatesRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewInstanceTemplatesRESTClient: %w", err)
    	}
    	defer instanceTemplatesClient.Close()
    
    	req := &computepb.InsertInstanceTemplateRequest{
    		Project: projectID,
    		InstanceTemplateResource: &computepb.InstanceTemplate{
    			Name: proto.String(templateName),
    			Properties: &computepb.InstanceProperties{
    				// The template describes the size and source image of the boot disk
    				// to attach to the instance.
    				Disks: []*computepb.AttachedDisk{
    					{
    						InitializeParams: &computepb.AttachedDiskInitializeParams{
    							DiskSizeGb:  proto.Int64(250),
    							SourceImage: proto.String("projects/debian-cloud/global/images/family/debian-12"),
    						},
    						AutoDelete: proto.Bool(true),
    						Boot:       proto.Bool(true),
    					},
    				},
    				MachineType: proto.String("e2-standard-4"),
    				// The template connects the instance to the specified network and subnetwork.
    				NetworkInterfaces: []*computepb.NetworkInterface{
    					{
    						Network:    proto.String(network),
    						Subnetwork: proto.String(subnetwork),
    					},
    				},
    			},
    		},
    	}
    
    	op, err := instanceTemplatesClient.Insert(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to create instance template: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Instance template created\n")
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/overview). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.compute.v1.[AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html);
    import com.google.cloud.compute.v1.[AttachedDiskInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDiskInitializeParams.html);
    import com.google.cloud.compute.v1.[GlobalOperationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalOperationsClient.html);
    import com.google.cloud.compute.v1.[InsertInstanceTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceTemplateRequest.html);
    import com.google.cloud.compute.v1.[InstanceProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceProperties.html);
    import com.google.cloud.compute.v1.[InstanceTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplate.html);
    import com.google.cloud.compute.v1.[InstanceTemplatesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplatesClient.html);
    import com.google.cloud.compute.v1.[NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateTemplateWithSubnet {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        /*
        TODO(developer): Replace these variables before running the sample.
        projectId: project ID or project number of the Cloud project you use.
        network: the network to be used in the new template. This value uses
            the following format: "projects/{project}/global/networks/{network}"
        subnetwork: the subnetwork to be used in the new template. This value
            uses the following format: "projects/{project}/regions/{region}/subnetworks/{subnetwork}"
        templateName: name of the new template to create.
        */
        String projectId = "your-project-id";
        String network = String.format("projects/%s/global/networks/%s", projectId, "network");
        String subnetwork = String.format("projects/%s/regions/%s/subnetworks/%s", projectId, "region",
            "subnetwork");
        String templateName = "template-name";
        createTemplateWithSubnet(projectId, network, subnetwork, templateName);
      }
    
      // Create an instance template that uses a provided subnet.
      public static void createTemplateWithSubnet(String projectId, String network, String subnetwork,
          String templateName)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        try ([InstanceTemplatesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplatesClient.html) instanceTemplatesClient = [InstanceTemplatesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplatesClient.html).create();
            [GlobalOperationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalOperationsClient.html) globalOperationsClient = [GlobalOperationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalOperationsClient.html).create()) {
    
          [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html) disk = [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html).newBuilder()
              .[setInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.Builder.html#com_google_cloud_compute_v1_AttachedDisk_Builder_setInitializeParams_com_google_cloud_compute_v1_AttachedDiskInitializeParams_)([AttachedDiskInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDiskInitializeParams.html).newBuilder()
                  .setSourceImage(
                      String.format("projects/%s/global/images/family/%s", "debian-cloud", "debian-13"))
                  .setDiskSizeGb(250).build())
              .setAutoDelete(true)
              .setBoot(true)
              .build();
    
          [InstanceProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceProperties.html) instanceProperties = [InstanceProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceProperties.html).newBuilder()
              .addDisks(disk)
              .setMachineType("e2-standard-4")
              .addNetworkInterfaces([NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html).newBuilder()
                  .setNetwork(network)
                  .setSubnetwork(subnetwork).build())
              .build();
    
          [InstanceTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplate.html) instanceTemplate = [InstanceTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplate.html).newBuilder()
              .setName(templateName)
              .setProperties(instanceProperties)
              .build();
    
          [InsertInstanceTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceTemplateRequest.html) insertInstanceTemplateRequest = [InsertInstanceTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceTemplateRequest.html)
              .newBuilder()
              .setProject(projectId)
              .setInstanceTemplateResource(instanceTemplate)
              .build();
    
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) operation = instanceTemplatesClient.insertCallable()
              .futureCall(insertInstanceTemplateRequest).get(3, TimeUnit.MINUTES);
    
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) response = globalOperationsClient.wait(projectId, operation.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getName__)());
    
          if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            System.out.println("Template creation from subnet failed ! ! " + response);
            return;
          }
          System.out.printf("Template creation from subnet operation status %s: %s", templateName,
              response.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)());
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
    // const network = 'projects/project/global/networks/network';
    // const subnetwork = 'projects/project/regions/region/subnetworks/subnetwork';
    // const templateName = 'your_template_name';
    
    const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    
    // Create an instance template that uses a provided subnet.
    async function createTemplateWithSubnet() {
      const instanceTemplatesClient = new compute.[InstanceTemplatesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      const [response] = await instanceTemplatesClient.insert({
        project: projectId,
        instanceTemplateResource: {
          name: templateName,
          properties: {
            // The template describes the size and source image of the boot disk
            // to attach to the instance.
            disks: [
              {
                // The template describes the size and source image of the boot disk
                // to attach to the instance.
                initializeParams: {
                  diskSizeGb: '250',
                  sourceImage:
                    'projects/debian-cloud/global/images/family/debian-11',
                },
                autoDelete: true,
                boot: true,
              },
            ],
            machineType: 'e2-standard-4',
            // The template connects the instance to the specified network and subnetwork.
            networkInterfaces: [
              {
                network,
                subnetwork,
              },
            ],
          },
        },
      });
      let operation = response.latestResponse;
      const operationsClient = new compute.[GlobalOperationsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      // Wait for the create operation to complete.
      while (operation.status !== 'DONE') {
        [operation] = await operationsClient.wait({
          operation: operation.name,
          project: projectId,
        });
      }
    
      console.log('Instance template created.');
    }
    
    createTemplateWithSubnet();

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
    
    
    def create_template_with_subnet(
        project_id: str, network: str, subnetwork: str, template_name: str
    ) -> compute_v1.InstanceTemplate:
        """
        Create an instance template that uses a provided subnet.
    
        Args:
            project_id: project ID or project number of the Cloud project you use.
            network: the network to be used in the new template. This value uses
                the following format: "projects/{project}/global/networks/{network}"
            subnetwork: the subnetwork to be used in the new template. This value
                uses the following format: "projects/{project}/regions/{region}/subnetworks/{subnetwork}"
            template_name: name of the new template to create.
    
        Returns:
            InstanceTemplate object that represents the new instance template.
        """
        # The template describes the size and source image of the book disk to
        # attach to the instance.
        disk = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[AttachedDisk](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.AttachedDisk.html)()
        initialize_params = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[AttachedDiskInitializeParams](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.AttachedDiskInitializeParams.html)()
        initialize_params.source_image = (
            "projects/debian-cloud/global/images/family/debian-13"
        )
        initialize_params.disk_size_gb = 250
        disk.initialize_params = initialize_params
        disk.auto_delete = True
        disk.boot = True
    
        template = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[InstanceTemplate](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.InstanceTemplate.html)()
        template.name = template_name
        template.properties = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[InstanceProperties](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.InstanceProperties.html)()
        template.properties.[disks](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.html) = [disk]
        template.properties.machine_type = "e2-standard-4"
    
        # The template connects the instance to the specified network and subnetwork.
        network_interface = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[NetworkInterface](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.NetworkInterface.html)()
        network_interface.network = network
        network_interface.subnetwork = subnetwork
        template.properties.network_interfaces = [network_interface]
    
        template_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[InstanceTemplatesClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instance_templates.InstanceTemplatesClient.html)()
        operation = template_client.[insert](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instance_templates.InstanceTemplatesClient.html#google_cloud_compute_v1_services_instance_templates_InstanceTemplatesClient_insert)(
            project=project_id, instance_template_resource=template
        )
        wait_for_extended_operation(operation, "instance template creation")
    
        return template_client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instance_templates.InstanceTemplatesClient.html#google_cloud_compute_v1_services_instance_templates_InstanceTemplatesClient_get)(project=project_id, instance_template=template_name)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
