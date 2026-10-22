---
url: https://docs.cloud.google.com/compute/docs/samples/compute-instances-create-from-template-with-overrides/
title: Create a VM instance from an instance template with overrides \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:51.494976+00:00
---

# Create a VM instance from an instance template with overrides  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-instances-create-from-template-with-overrides/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  Create a VM instance from an instance template with overrides Stay organized with collections  Save and categorize content based on your preferences. 

Create a VM instance from an instance template, then override the disk and machine type options in the template.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create a VM from an instance template](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-instance-template)



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
    
    // createInstanceFromTemplate creates a Compute Engine VM instance from an instance template, but overrides the disk and machine type options in the template.
    func createInstanceFromTemplateWithOverrides(w io.Writer, projectID, zone, instanceName, instanceTemplateName, machineType, newDiskSourceImage string) error {
    	// projectID := "your_project_id"
    	// zone := "europe-central2-b"
    	// instanceName := "your_instance_name"
    	// instanceTemplateName := "your_instance_template_name"
    	// machineType := "n1-standard-2"
    	// newDiskSourceImage := "projects/debian-cloud/global/images/family/debian-12"
    
    	ctx := context.Background()
    	instancesClient, err := compute.[NewInstancesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_InstancesClient_NewInstancesRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewInstancesRESTClient: %w", err)
    	}
    	defer instancesClient.Close()
    
    	intanceTemplatesClient, err := compute.[NewInstanceTemplatesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_InstanceTemplatesClient_NewInstanceTemplatesRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewInstanceTemplatesRESTClient: %w", err)
    	}
    	defer intanceTemplatesClient.Close()
    
    	// Retrieve an instance template by name.
    	reqGetTemplate := &computepb.GetInstanceTemplateRequest{
    		Project:          projectID,
    		InstanceTemplate: instanceTemplateName,
    	}
    
    	instanceTemplate, err := intanceTemplatesClient.Get(ctx, reqGetTemplate)
    	if err != nil {
    		return fmt.Errorf("unable to get intance template: %w", err)
    	}
    
    	for _, disk := range instanceTemplate.Properties.Disks {
    		diskType := disk.InitializeParams.GetDiskType()
    		if diskType != "" {
    			disk.InitializeParams.DiskType = proto.String(fmt.Sprintf(`zones/%s/diskTypes/%s`, zone, diskType))
    		}
    	}
    
    	reqInsertInstance := &computepb.InsertInstanceRequest{
    		Project: projectID,
    		Zone:    zone,
    		InstanceResource: &computepb.Instance{
    			Name:        proto.String(instanceName),
    			MachineType: proto.String(fmt.Sprintf(`zones/%s/machineTypes/%s`, zone, machineType)),
    			Disks: append(
    				// If you override a repeated field, all repeated values
    				// for that property are replaced with the
    				// corresponding values provided in the request.
    				// When adding a new disk to existing disks,
    				// insert all existing disks as well.
    				instanceTemplate.Properties.Disks,
    				&computepb.AttachedDisk{
    					InitializeParams: &computepb.AttachedDiskInitializeParams{
    						DiskSizeGb:  proto.Int64(10),
    						SourceImage: &newDiskSourceImage,
    					},
    					AutoDelete: proto.Bool(true),
    					Boot:       proto.Bool(false),
    					Type:       proto.String(computepb.[AttachedDisk_PERSISTENT](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1/computepb.html#cloud_google_com_go_compute_apiv1_computepb_AttachedDisk_UNDEFINED_TYPE_AttachedDisk_PERSISTENT_AttachedDisk_SCRATCH).String()),
    				},
    			),
    		},
    		SourceInstanceTemplate: instanceTemplate.SelfLink,
    	}
    
    	op, err := instancesClient.Insert(ctx, reqInsertInstance)
    	if err != nil {
    		return fmt.Errorf("unable to create instance: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Instance created\n")
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/overview). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.compute.v1.[AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html);
    import com.google.cloud.compute.v1.[AttachedDiskInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDiskInitializeParams.html);
    import com.google.cloud.compute.v1.[InsertInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceRequest.html);
    import com.google.cloud.compute.v1.[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html);
    import com.google.cloud.compute.v1.[InstanceTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplate.html);
    import com.google.cloud.compute.v1.[InstanceTemplatesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplatesClient.html);
    import com.google.cloud.compute.v1.[InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.List;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateInstanceFromTemplateWithOverrides {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        /* TODO(developer): Replace these variables before running the sample.
         * projectId - ID or number of the project you want to use.
         * zone - Name of the zone you want to check, for example: us-west3-b
         * instanceName - Name of the new instance.
         * instanceTemplateName - Name of the instance template to use when creating the new instance.
         * machineType - Machine type you want to set in following format:
         *    "zones/{zone}/machineTypes/{type_name}". For example:
         *    "zones/europe-west3-c/machineTypes/f1-micro"
         *    You can find the list of available machine types using:
         *    https://cloud.google.com/sdk/gcloud/reference/compute/machine-types/list
         * newDiskSourceImage - Path the the disk image you want to use for your new
         *    disk. This can be one of the public images
         *    (like "projects/debian-cloud/global/images/family/debian-13")
         *    or a private image you have access to.
         *    You can check the list of available public images using the doc:
         *    http://cloud.google.com/compute/docs/images
         */
        String projectId = "your-project-id";
        String zone = "zone-name";
        String instanceName = "instance-name";
        String instanceTemplateName = "instance-template-name";
    
        createInstanceFromTemplateWithOverrides(projectId, zone, instanceName, instanceTemplateName);
      }
    
      // Creates a Compute Engine VM instance from an instance template,
      // but overrides the disk and machine type options in the template.
      public static void createInstanceFromTemplateWithOverrides(String projectId, String zone,
          String instanceName, String instanceTemplateName)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
    
        try ([InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html) instancesClient = [InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html).create();
            [InstanceTemplatesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplatesClient.html) instanceTemplatesClient = [InstanceTemplatesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplatesClient.html).create()) {
    
          String machineType = "n1-standard-1";
          String newDiskSourceImage = "projects/debian-cloud/global/images/family/debian-13";
    
          // Retrieve an instance template.
          [InstanceTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplate.html) instanceTemplate = instanceTemplatesClient
              .get(projectId, instanceTemplateName);
    
          // Adjust diskType field of the instance template to use the URL formatting 
          // required by instances.insert.diskType
          // For instance template, there is only a name, not URL.
          List<AttachedDisk> reformattedAttachedDisks = new ArrayList<>();
          for ([AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html) disk : instanceTemplate.[getProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplate.html#com_google_cloud_compute_v1_InstanceTemplate_getProperties__)().getDisksList()) {
            disk = [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html).newBuilder(disk)
                .[setInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.Builder.html#com_google_cloud_compute_v1_AttachedDisk_Builder_setInitializeParams_com_google_cloud_compute_v1_AttachedDiskInitializeParams_)([AttachedDiskInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDiskInitializeParams.html)
                    .newBuilder(disk.getInitializeParams())
                    .setDiskType(
                        String.format(
                            "zones/%s/diskTypes/%s", zone, disk.getInitializeParams().getDiskType()))
                    .build())
                .build();
    
            reformattedAttachedDisks.add(disk);
          }
    
          [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html) newdisk = [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html).newBuilder()
              .[setInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.Builder.html#com_google_cloud_compute_v1_AttachedDisk_Builder_setInitializeParams_com_google_cloud_compute_v1_AttachedDiskInitializeParams_)([AttachedDiskInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDiskInitializeParams.html).newBuilder()
                  .setDiskSizeGb(10)
                  .setSourceImage(newDiskSourceImage).build())
              .setAutoDelete(true)
              .setBoot(false)
              .setType([AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html).Type.PERSISTENT.toString()).build();
    
          [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html) instance = [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html).newBuilder()
              .setName(instanceName)
              .setMachineType(String.format("zones/%s/machineTypes/%s", zone, machineType))
              // If you override a repeated field, all repeated values
              // for that property are replaced with the
              // corresponding values provided in the request.
              // When adding a new disk to existing disks,
              // insert all existing disks as well.
              .addAllDisks(reformattedAttachedDisks)
              .addDisks(newdisk)
              .build();
    
          [InsertInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceRequest.html) insertInstanceRequest = [InsertInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceRequest.html).newBuilder()
              .setProject(projectId)
              .setZone(zone)
              .setInstanceResource(instance)
              .setSourceInstanceTemplate(instanceTemplate.[getSelfLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplate.html#com_google_cloud_compute_v1_InstanceTemplate_getSelfLink__)()).build();
    
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) response = instancesClient.insertAsync(insertInstanceRequest)
              .get(3, TimeUnit.MINUTES);
    
          if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            System.out.println("Instance creation from template with overrides failed ! ! " + response);
            return;
          }
          System.out
              .printf("Instance creation from template with overrides: Operation Status %s: %s ",
                  instanceName, response.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)());
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
    // const zone = 'europe-central2-b';
    // const instanceName = 'YOUR_INSTANCE_NAME';
    // const instanceTemplateName = 'YOUR_INSTANCE_TEMPLATE_NAME';
    // const machineType = 'n1-standard-1';
    // const newDiskSourceImage = 'projects/debian-cloud/global/images/family/debian-11';
    
    const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    
    // Creates a new instance in the specified project and zone using a selected template,
    // but overrides the disk and machine type options in the template.
    async function createInstanceFromTemplateWithOverrides() {
      const instancesClient = new compute.[InstancesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
      const instanceTemplatesClient = new compute.[InstanceTemplatesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      console.log(
        `Creating the ${instanceName} instance in ${zone} from template ${instanceTemplateName}...`
      );
    
      // Retrieve an instance template by name.
      const [instanceTemplate] = await instanceTemplatesClient.get({
        project: projectId,
        instanceTemplate: instanceTemplateName,
      });
    
      // Adjust diskType field of the instance template to use the URL formatting required by instances.insert.diskType
      // For instance template, there is only a name, not URL.
      for (const disk of instanceTemplate.properties.disks) {
        if (disk.initializeParams.diskType) {
          disk.initializeParams.diskType = `zones/${zone}/diskTypes/${disk.initializeParams.diskType}`;
        }
      }
    
      const [response] = await instancesClient.insert({
        project: projectId,
        zone,
        instanceResource: {
          name: instanceName,
          machineType: `zones/${zone}/machineTypes/${machineType}`,
          disks: [
            // If you override a repeated field, all repeated values
            // for that property are replaced with the
            // corresponding values provided in the request.
            // When adding a new disk to existing disks,
            // insert all existing disks as well.
            ...instanceTemplate.properties.disks,
            {
              initializeParams: {
                diskSizeGb: '10',
                sourceImage: newDiskSourceImage,
              },
              autoDelete: true,
              boot: false,
              type: 'PERSISTENT',
            },
          ],
        },
        sourceInstanceTemplate: instanceTemplate.selfLink,
      });
      let operation = response.latestResponse;
      const operationsClient = new compute.[ZoneOperationsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      // Wait for the create operation to complete.
      while (operation.status !== 'DONE') {
        [operation] = await operationsClient.wait({
          operation: operation.name,
          project: projectId,
          zone: operation.zone.split('/').pop(),
        });
      }
    
      console.log('Instance created.');
    }
    
    createInstanceFromTemplateWithOverrides();

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
    
    
    def create_instance_from_template_with_overrides(
        project_id: str,
        zone: str,
        instance_name: str,
        instance_template_name: str,
        machine_type: str,
        new_disk_source_image: str,
    ) -> compute_v1.Instance:
        """
        Creates a Compute Engine VM instance from an instance template, changing the machine type and
        adding a new disk created from a source image.
    
        Args:
            project_id: ID or number of the project you want to use.
            zone: Name of the zone you want to check, for example: us-west3-b
            instance_name: Name of the new instance.
            instance_template_name: Name of the instance template used for creating the new instance.
            machine_type: Machine type you want to set in following format:
                "zones/{zone}/machineTypes/{type_name}". For example:
                - "zones/europe-west3-c/machineTypes/f1-micro"
                - You can find the list of available machine types using:
                  https://cloud.google.com/sdk/gcloud/reference/compute/machine-types/list
            new_disk_source_image: Path the the disk image you want to use for your new
                disk. This can be one of the public images
                (like "projects/debian-cloud/global/images/family/debian-12")
                or a private image you have access to.
                For a list of available public images, see the documentation:
                http://cloud.google.com/compute/docs/images
    
        Returns:
            Instance object.
        """
        instance_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html)()
        instance_template_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[InstanceTemplatesClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instance_templates.InstanceTemplatesClient.html)()
    
        # Retrieve an instance template by name.
        instance_template = instance_template_client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instance_templates.InstanceTemplatesClient.html#google_cloud_compute_v1_services_instance_templates_InstanceTemplatesClient_get)(
            project=project_id, instance_template=instance_template_name
        )
    
        # Adjust diskType field of the instance template to use the URL formatting required by instances.insert.diskType
        # For instance template, there is only a name, not URL.
        for disk in instance_template.properties.[disks](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.html):
            if disk.initialize_params.disk_type:
                disk.initialize_params.disk_type = (
                    f"zones/{zone}/diskTypes/{disk.initialize_params.disk_type}"
                )
    
        instance = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[Instance](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.Instance.html)()
        instance.name = instance_name
        instance.machine_type = machine_type
        instance.[disks](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.html) = list(instance_template.properties.[disks](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.html))
    
        new_disk = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[AttachedDisk](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.AttachedDisk.html)()
        new_disk.initialize_params.disk_size_gb = 50
        new_disk.initialize_params.source_image = new_disk_source_image
        new_disk.auto_delete = True
        new_disk.boot = False
        new_disk.type_ = "PERSISTENT"
    
        instance.[disks](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.html).append(new_disk)
    
        instance_insert_request = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[InsertInstanceRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.InsertInstanceRequest.html)()
        instance_insert_request.project = project_id
        instance_insert_request.zone = zone
        instance_insert_request.instance_resource = instance
        instance_insert_request.source_instance_template = instance_template.self_link
    
        operation = instance_client.[insert](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html#google_cloud_compute_v1_services_instances_InstancesClient_insert)(instance_insert_request)
        wait_for_extended_operation(operation, "instance creation")
    
        return instance_client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html#google_cloud_compute_v1_services_instances_InstancesClient_get)(project=project_id, zone=zone, instance=instance_name)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
