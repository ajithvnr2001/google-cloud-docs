---
url: https://docs.cloud.google.com/compute/docs/samples/compute-template-create/
title: Create an instance template \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:14:19.487836+00:00
---

# Create an instance template  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-template-create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  Create an instance template Stay organized with collections  Save and categorize content based on your preferences. 

Use the specified machine type, boot disk and network to create an instance template.

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
    
    // createTemplate creates a new instance template with the provided name and a specific instance configuration.
    func createTemplate(w io.Writer, projectID, templateName string) error {
    	// projectID := "your_project_id"
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
    				// The template connects the instance to the `default` network,
    				// without specifying a subnetwork.
    				NetworkInterfaces: []*computepb.NetworkInterface{
    					{
    						Name: proto.String("global/networks/default"),
    						// The template lets the instance use an external IP address.
    						AccessConfigs: []*computepb.AccessConfig{
    							{
    								Name:        proto.String("External NAT"),
    								Type:        proto.String(computepb.[AccessConfig_ONE_TO_ONE_NAT](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1/computepb.html#cloud_google_com_go_compute_apiv1_computepb_AccessConfig_UNDEFINED_TYPE_AccessConfig_DIRECT_IPV6_AccessConfig_ONE_TO_ONE_NAT).String()),
    								NetworkTier: proto.String(computepb.[AccessConfig_PREMIUM](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1/computepb.html#cloud_google_com_go_compute_apiv1_computepb_AccessConfig_UNDEFINED_NETWORK_TIER_AccessConfig_FIXED_STANDARD_AccessConfig_PREMIUM_AccessConfig_STANDARD_AccessConfig_STANDARD_OVERRIDES_FIXED_STANDARD).String()),
    							},
    						},
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
    
    
    import com.google.cloud.compute.v1.[AccessConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AccessConfig.html);
    import com.google.cloud.compute.v1.[AccessConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AccessConfig.html).NetworkTier;
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
    
    public class CreateInstanceTemplate {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // projectId: project ID or project number of the Cloud project you use.
        // templateName: name of the new template to create.
        String projectId = "your-project-id";
        String templateName = "template-name";
        createInstanceTemplate(projectId, templateName);
      }
    
      /*
        Create a new instance template with the provided name and a specific
        instance configuration.
       */
      public static void createInstanceTemplate(String projectId, String templateName)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        try ([InstanceTemplatesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplatesClient.html) instanceTemplatesClient = [InstanceTemplatesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplatesClient.html).create()) {
    
          String machineType = "e2-standard-4";
          String sourceImage = "projects/debian-cloud/global/images/family/debian-13";
    
          // The template describes the size and source image of the boot disk
          // to attach to the instance.
          [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html) attachedDisk = [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html).newBuilder()
              .[setInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.Builder.html#com_google_cloud_compute_v1_AttachedDisk_Builder_setInitializeParams_com_google_cloud_compute_v1_AttachedDiskInitializeParams_)([AttachedDiskInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDiskInitializeParams.html).newBuilder()
                  .setSourceImage(sourceImage)
                  .setDiskType("pd-balanced")
                  .setDiskSizeGb(250).build())
              .setAutoDelete(true)
              .setBoot(true).build();
    
          // The template connects the instance to the `default` network,
          // without specifying a subnetwork.
          [NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html) networkInterface = [NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html).newBuilder()
              .setName("global/networks/default")
              // The template lets the instance use an external IP address.
              .[addAccessConfigs](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.Builder.html#com_google_cloud_compute_v1_NetworkInterface_Builder_addAccessConfigs_com_google_cloud_compute_v1_AccessConfig_)([AccessConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AccessConfig.html).newBuilder()
                  .setName("External NAT")
                  .setType([AccessConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AccessConfig.html).Type.ONE_TO_ONE_NAT.toString())
                  .setNetworkTier(NetworkTier.PREMIUM.toString()).build()).build();
    
          [InstanceProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceProperties.html) instanceProperties = [InstanceProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceProperties.html).newBuilder()
              .addDisks(attachedDisk)
              .setMachineType(machineType)
              .addNetworkInterfaces(networkInterface).build();
    
          [InsertInstanceTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceTemplateRequest.html) insertInstanceTemplateRequest = [InsertInstanceTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceTemplateRequest.html)
              .newBuilder()
              .setProject(projectId)
              .setInstanceTemplateResource([InstanceTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplate.html).newBuilder()
                  .setName(templateName)
                  .setProperties(instanceProperties).build()).build();
    
          // Create the Instance Template.
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) response = instanceTemplatesClient.insertAsync(insertInstanceTemplateRequest)
              .get(3, TimeUnit.MINUTES);
    
          if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            System.out.println("Instance Template creation failed ! ! " + response);
            return;
          }
          System.out
              .printf("Instance Template Operation Status %s: %s", templateName, response.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)());
        }
      }
    
      public static void createInstanceTemplateWithDiskType(String projectId, String templateName)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        try ([InstanceTemplatesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplatesClient.html) instanceTemplatesClient = [InstanceTemplatesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplatesClient.html).create();
            [GlobalOperationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalOperationsClient.html) globalOperationsClient = [GlobalOperationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalOperationsClient.html).create()) {
    
          [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html) disk = [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html).newBuilder()
              .[setInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.Builder.html#com_google_cloud_compute_v1_AttachedDisk_Builder_setInitializeParams_com_google_cloud_compute_v1_AttachedDiskInitializeParams_)([AttachedDiskInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDiskInitializeParams.html).newBuilder()
                  .setDiskSizeGb(10)
                  .setDiskType("pd-balanced")
                  .setSourceImage("projects/debian-cloud/global/images/family/debian-13").build())
              .setAutoDelete(true)
              .setBoot(true)
              .setType([AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html).Type.PERSISTENT.toString()).build();
    
          [InstanceTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplate.html) instanceTemplate = [InstanceTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplate.html).newBuilder()
              .setName(templateName)
              .setProperties([InstanceProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceProperties.html).newBuilder()
                  .setMachineType("n1-standard-1")
                  .addDisks(disk)
                  .addNetworkInterfaces([NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html).newBuilder()
                      .setName("global/networks/default").build()).build()).build();
    
          [InsertInstanceTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceTemplateRequest.html) insertInstanceTemplateRequest = [InsertInstanceTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceTemplateRequest.html)
              .newBuilder()
              .setProject(projectId)
              .setInstanceTemplateResource(instanceTemplate).build();
    
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) response = instanceTemplatesClient.insertAsync(insertInstanceTemplateRequest)
              .get(3, TimeUnit.MINUTES);
    
          if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            System.out.println("Instance Template creation failed ! ! " + response);
            return;
          }
          System.out
              .printf("Instance Template Operation Status %s: %s", templateName, response.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)());
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
    // const templateName = 'your_template_name';
    
    const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    
    // Create a new instance template with the provided name and a specific instance configuration.
    async function createTemplate() {
      const instanceTemplatesClient = new compute.[InstanceTemplatesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      const [response] = await instanceTemplatesClient.insert({
        project: projectId,
        instanceTemplateResource: {
          name: templateName,
          properties: {
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
            // The template connects the instance to the `default` network,
            // without specifying a subnetwork.
            networkInterfaces: [
              {
                // Use the network interface provided in the networkName argument.
                name: 'global/networks/default',
                // The template lets the instance use an external IP address.
                accessConfigs: [
                  {
                    name: 'External NAT',
                    type: 'ONE_TO_ONE_NAT',
                    networkTier: 'PREMIUM',
                  },
                ],
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
    
    createTemplate();

### Python

Before trying this sample, follow the Python setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from __future__ import annotations
    
    import sys
    from typing import Any
    
    from google.api_core.extended_operation import ExtendedOperation
    from google.cloud import compute_v1
    
    
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
    
    
    def create_template(project_id: str, template_name: str) -> compute_v1.InstanceTemplate:
        """
        Create a new instance template with the provided name and a specific
        instance configuration.
    
        Args:
            project_id: project ID or project number of the Cloud project you use.
            template_name: name of the new template to create.
    
        Returns:
            InstanceTemplate object that represents the new instance template.
        """
        # The template describes the size and source image of the boot disk
        # to attach to the instance.
        disk = compute_v1.AttachedDisk()
        initialize_params = compute_v1.AttachedDiskInitializeParams()
        initialize_params.source_image = (
            "projects/debian-cloud/global/images/family/debian-13"
        )
        initialize_params.disk_size_gb = 250
        disk.initialize_params = initialize_params
        disk.auto_delete = True
        disk.boot = True
    
        # The template connects the instance to the `default` network,
        # without specifying a subnetwork.
        network_interface = compute_v1.NetworkInterface()
        network_interface.name = "global/networks/default"
    
        # The template lets the instance use an external IP address.
        access_config = compute_v1.AccessConfig()
        access_config.name = "External NAT"
        access_config.type_ = "ONE_TO_ONE_NAT"
        access_config.network_tier = "PREMIUM"
        network_interface.access_configs = [access_config]
    
        template = compute_v1.InstanceTemplate()
        template.name = template_name
        template.properties.disks = [disk]
        template.properties.machine_type = "e2-standard-4"
        template.properties.network_interfaces = [network_interface]
    
        template_client = compute_v1.InstanceTemplatesClient()
        operation = template_client.insert(
            project=project_id, instance_template_resource=template
        )
    
        wait_for_extended_operation(operation, "instance template creation")
    
        return template_client.get(project=project_id, instance_template=template_name)
    
    

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    resource "google_compute_instance_template" "foobar" {
      name         = "my-instance-template"
      machine_type = "e2-standard-4"
    
      disk {
        source_image = "debian-cloud/debian-13"
        disk_size_gb = 250
      }
    
      network_interface {
        network = "default"
    
        # default access config, defining external IP configuration
        access_config {
          network_tier = "PREMIUM"
        }
      }
    
      # To avoid embedding secret keys or user credentials in the instances, Google recommends that you use custom service accounts with the following access scopes.
      service_account {
        scopes = [
          "https://www.googleapis.com/auth/cloud-platform"
        ]
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
