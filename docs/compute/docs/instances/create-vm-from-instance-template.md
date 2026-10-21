---
url: https://docs.cloud.google.com/compute/docs/instances/create-vm-from-instance-template/
title: Create a VM from an instance template \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:17:58.379601+00:00
---

# Create a VM from an instance template  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/create-vm-from-instance-template/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create a VM from an instance template Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to use an [instance template](https://docs.cloud.google.com/compute/docs/instance-templates) to create a VM instance. An instance template is an API resource that defines the properties of VM instances. You define properties like the machine type, OS image, persistent disk configurations, metadata, startup scripts, and so on, in an instance template and then can use the instance template to create individual VM instances or [groups of managed instances](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances).

When you create a VM instance from an instance template, the default behavior is to create a VM instance that is identical to the properties specified in the template, with the exception of the VM instance name and the zone where the instance will live. Alternatively, you can also optionally override certain fields during instance creation if you want to change certain properties of the instance template for specific uses.

This document assumes that you have an instance template ready to use. If you do not have an instance template, follow the instructions to [create a new instance template](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates).

## Before you begin

  * Read the [Instance Template](https://docs.cloud.google.com/compute/docs/instance-templates) documentation.
  * Create an [instance template](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates).
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




## Create a VM instance from an instance template

You can use either a regional or a global instance template to create a VM instance. To create an instance exactly as described in the instance template, follow these instructions.

###  Console 

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. In the auto_awesome **Create VM from ...** menu, select **Instance templates**.

  3. In the **Create VM from template** window that appears, do the following:

     1. Select a template.

     2. To create and start the VM, click **Create**.




###  gcloud 

To create a VM from a regional or global instance template, use the same [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) that you would use to create a normal instance, but add the `--source-instance-template` flag:
    
    
    gcloud compute instances create VM_NAME \
        --source-instance-template INSTANCE_TEMPLATE_URL
    

Replace the following:

  * `VM_NAME`: the [name](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format) of the instance.
  * `INSTANCE_TEMPLATE_URL`: the URL of the instance template that you want to use to create instances in the MIG. The URL can contain either the [ID](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) or name of the instance template. Specify one of the following values: 
    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_ID`
    * For a global instance template: `INSTANCE_TEMPLATE_ID`



For example:
    
    
    gcloud compute instances create example-instance \
        --source-instance-template 1234567890
    

###  Go 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    	"google.golang.org/protobuf/proto"
    )
    
    // createInstanceFromTemplate creates a Compute Engine VM instance from an instance template.
    func createInstanceFromTemplate(w io.Writer, projectID, zone, instanceName, instanceTemplateUrl string) error {
    	// projectID := "your_project_id"
    	// zone := "europe-central2-b"
    	// instanceName := "your_instance_name"
    	// instanceTemplateUrl := "global/instanceTemplates/your_instance_template"
    
    	ctx := context.Background()
    	instancesClient, err := compute.[NewInstancesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_InstancesClient_NewInstancesRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewInstancesRESTClient: %w", err)
    	}
    	defer instancesClient.Close()
    
    	req := &computepb.InsertInstanceRequest{
    		Project: projectID,
    		Zone:    zone,
    		InstanceResource: &computepb.Instance{
    			Name: proto.String(instanceName),
    		},
    		SourceInstanceTemplate: &instanceTemplateUrl,
    	}
    
    	op, err := instancesClient.Insert(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to create instance: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Instance created\n")
    
    	return nil
    }
    

###  Java 
    
    
    import com.google.cloud.compute.v1.[AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html);
    import com.google.cloud.compute.v1.[AttachedDiskInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDiskInitializeParams.html);
    import com.google.cloud.compute.v1.[InsertInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceRequest.html);
    import com.google.cloud.compute.v1.[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html);
    import com.google.cloud.compute.v1.[InstanceProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceProperties.html);
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
    
    public class CreateInstanceFromTemplate {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        /*  TODO(developer): Replace these variables before running the sample.
            projectId - ID or number of the project you want to use.
            zone - Name of the zone you want to check, for example: us-west3-b
            instanceName - Name of the new instance.
            instanceTemplateURL - URL of the instance template using for creating the new instance.
            It can be a full or partial URL.
            Examples:
            - https://www.googleapis.com/compute/v1/projects/project/global/instanceTemplates/example-instance-template
            - projects/project/global/instanceTemplates/example-instance-template
            - global/instanceTemplates/example-instance-template
         */
        String projectId = "your-project-id";
        String zone = "zone-name";
        String instanceName = "instance-name";
        String instanceTemplateUrl = "instance-template-url";
        createInstanceFromTemplate(projectId, zone, instanceName, instanceTemplateUrl);
      }
    
      // Create a new instance from template in the specified project and zone.
      public static void createInstanceFromTemplate(String projectId, String zone, String instanceName,
          String instanceTemplateName)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
    
        try ([InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html) instancesClient = [InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html).create();
            [InstanceTemplatesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplatesClient.html) instanceTemplatesClient = [InstanceTemplatesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplatesClient.html).create()) {
    
          [InstanceTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplate.html) instanceTemplate = instanceTemplatesClient.get(projectId,
              instanceTemplateName);
    
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
    
          // Clear existing disks and set the reformatted disks in the instance template.
          instanceTemplate = [InstanceTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplate.html)
              .newBuilder(instanceTemplate)
              .setProperties([InstanceProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceProperties.html)
                  .newBuilder(instanceTemplate.[getProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplate.html#com_google_cloud_compute_v1_InstanceTemplate_getProperties__)())
                  .clearDisks()
                  .addAllDisks(reformattedAttachedDisks)
                  .build())
              .build();
    
          [InsertInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceRequest.html) insertInstanceRequest = [InsertInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceRequest.html).newBuilder()
              .setProject(projectId)
              .setZone(zone)
              .setInstanceResource([Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html).newBuilder().setName(instanceName).build())
              .setSourceInstanceTemplate(instanceTemplate.[getSelfLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplate.html#com_google_cloud_compute_v1_InstanceTemplate_getSelfLink__)()).build();
    
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) response = instancesClient.insertAsync(insertInstanceRequest)
              .get(3, TimeUnit.MINUTES);
    
          if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            System.out.println("Instance creation from template failed ! ! " + response);
            return;
          }
          System.out
              .printf("Instance creation from template: Operation Status %s: %s ", instanceName,
                  response.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)());
        }
      }
    }

###  Node.js 
    
    
    /**
     * TODO(developer): Uncomment and replace these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const zone = 'europe-central2-b'
    // const instanceName = 'YOUR_INSTANCE_NAME'
    // const instanceTemplateUrl = 'YOUR_INSTANCE_TEMPLATE_URL'
    
    const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    
    // Create a new instance from template in the specified project and zone.
    async function createInstanceFromTemplate() {
      const instancesClient = new compute.[InstancesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      console.log(
        `Creating the ${instanceName} instance in ${zone} from template ${instanceTemplateUrl}...`
      );
    
      const [response] = await instancesClient.insert({
        project: projectId,
        zone,
        instanceResource: {
          name: instanceName,
        },
        sourceInstanceTemplate: instanceTemplateUrl,
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
    
    createInstanceFromTemplate();

###  Python 
    
    
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
    
    
    def create_instance_from_template(
        project_id: str, zone: str, instance_name: str, instance_template_url: str
    ) -> compute_v1.Instance:
        """
        Creates a Compute Engine VM instance from an instance template.
    
        Args:
            project_id: ID or number of the project you want to use.
            zone: Name of the zone you want to check, for example: us-west3-b
            instance_name: Name of the new instance.
            instance_template_url: URL of the instance template used for creating the new instance.
                It can be a full or partial URL.
                Examples:
                - https://www.googleapis.com/compute/v1/projects/project/global/instanceTemplates/example-instance-template
                - projects/project/global/instanceTemplates/example-instance-template
                - global/instanceTemplates/example-instance-template
    
        Returns:
            Instance object.
        """
        instance_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html)()
    
        instance_insert_request = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[InsertInstanceRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.InsertInstanceRequest.html)()
        instance_insert_request.project = project_id
        instance_insert_request.zone = zone
        instance_insert_request.source_instance_template = instance_template_url
        instance_insert_request.instance_resource.name = instance_name
    
        operation = instance_client.[insert](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html#google_cloud_compute_v1_services_instances_InstancesClient_insert)(instance_insert_request)
        wait_for_extended_operation(operation, "instance creation")
    
        return instance_client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html#google_cloud_compute_v1_services_instances_InstancesClient_get)(project=project_id, zone=zone, instance=instance_name)
    
    

###  REST 

To create a VM from a regional or global instance template, construct a normal request to [create an instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance#startinginstancewithimage) but include the [`sourceInstanceTemplate`](https://docs.cloud.google.com/compute/docs/reference/latest/instances/insert#sourceInstanceTemplate) query parameter followed by a qualified path to an instance template.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/
    PROJECT_ID/zones/ZONE/
    instances?sourceInstanceTemplate=INSTANCE_TEMPLATE_URL
    

In the request body, provide a `name` for the VM instance:
    
    
    { "name": "example-instance" }
    

For example, the following snippet includes a fully-qualified path to the template: `https://compute.googleapis.com/compute/v1/projects/myproject/global/instanceTemplates/1234567890`.
    
    
    POST https://compute.googleapis.com/
    compute/v1/projects/myproject/zones/us-central1-a/instances?sourceInstanceTemplate=
    https://compute.googleapis.com/compute/v1/projects/myproject/global/
    instanceTemplates/1234567890
    
    
    
    { "name": "example-instance" }
    

## Create a VM instance from an instance template with overrides

When you use an instance template to start a VM instance, the default behavior is to create a VM instance exactly as described in the instance template with the exception of the instance name and zone.

If you want to create an instance primarily based on an instance template but with a few changes, you can use the override behavior. To use the override behavior, you pass in attributes to override for the existing instance template when creating the instance.

###  Console 

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. In the auto_awesome **Create VM from ...** menu, select **Instance templates**.

  3. In the **Create VM from template** window that appears, select a template, and then click edit **Customize**.

  4. Optional: Specify other configuration options. For more information, see [Configuration options during instance creation](https://docs.cloud.google.com/compute/docs/instances/instance-creation-overview#new-instance-configuration-options).

  5. To create and start the instance, click **Create**.




###  gcloud 

Using the gcloud CLI, make a request to create an instance with the `--source-instance-template` flag and override any property you want with the appropriate `gcloud` flag. To see a list of applicable flags, review the [`gcloud` reference](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create).

For example, provide the following flags to override the machine type, metadata, operating system, Persistent Disk boot disk, and a secondary disk of an instance template:
    
    
    gcloud compute instances create example-instance \
        --source-instance-template 1234567890 --machine-type e2-standard-2 \
        --image-family debian-9 --image-project debian-cloud \
        --metadata bread=butter --disk=boot=no,name=my-override-disk
    

###  Go 
    
    
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
    

###  Java 
    
    
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

###  Node.js 
    
    
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

###  Python 
    
    
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
    
    

###  REST 

In the API, use the [`sourceInstanceTemplate`](https://docs.cloud.google.com/compute/docs/reference/latest/instances/insert#sourceInstanceTemplate) query parameter and provide any fields you want to override in the request body when constructing a normal request to [create an instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance#startinginstancewithimage).

The override behavior in the API follows the JSON merge patch rules, described by [RFC 7396](https://tools.ietf.org/html/rfc7396).

Specifically:

  * If you override a basic field, the corresponding basic field in the instance template will be replaced with the basic field value in the request. Basic fields include `machineType`, `sourceImage`, `name`, and so on.
  * If you override a repeated field, all repeated values for that property will be replaced with the corresponding values provided in the request. Repeated fields are generally properties of type `list`. For example, `disks` and `networkInterfaces` are repeated fields.
  * If you override a `nested object`, the object in the instance template will be merged with the corresponding object specification in the request. Note that if a nested object lives within a repeated field, the field is treated according to rules for repeated fields. Labels are an exception to this rule, and are treated as a repeated field even though it is of type `object`.



For example, let's assume you have an instance template with two non-boot disks but you want to override one of the disks. You must provide the entire `disks` specification in your request, including any disks you want to keep.

The URL for this request:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/myproject/zones/us-central1-a/instances?
    sourceInstanceTemplate=https://compute.googleapis.com/compute/v1/projects/myproject/global/instanceTemplates/1234567890
    

The request body:
    
    
        {
          "disks": [
            {
              # Since you are overriding the repeated disk property, you must
              # specify a boot disk in the request, even if it is already
              # specified in the instance template
              "autoDelete": true,
              "boot": true,
              "initializeParams": {
                "sourceImage": "projects/debian-cloud/global/images/family/debian-8"
              },
              "mode": "READ_WRITE",
              "type": "PERSISTENT"
            },
            {
              # New disk you want to use
              "autoDelete": false,
              "boot": false,
              "mode": "READ_WRITE",
              "source": "zones/us-central1-f/disks/my-override-disk",
              "type": "PERSISTENT"
            },
            {
               # Assume this disk is already specified in instance template, but
               # you must specify it again since you are overriding the disks
               # property
              "autoDelete": false,
              "boot": false,
              "mode": "READ_WRITE",
    
              "source": "zones/us-central1-f/disks/my-other-disk-to-keep",
              "type": "PERSISTENT"
            }
          ],
          "machineType": "zones/us-central1-f/machineTypes/e2-standard-2",
          "name": "example-instance"
        }
        

## What's next

  * Read the [Preemptible VM instances](https://docs.cloud.google.com/compute/docs/instances/preemptible) documentation.
  * Read about [Shutdown scripts](https://docs.cloud.google.com/compute/docs/shutdownscript).
  * Refer to the [preemptible instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#e2_machine_types).
  * [Connect to your instance](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
