---
url: https://docs.cloud.google.com/compute/docs/samples/compute-template-create-from-instance/
title: Create an instance template based on an existing instance \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:50:31.759176+00:00
---

# Create an instance template based on an existing instance  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-template-create-from-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  Create an instance template based on an existing instance Stay organized with collections  Save and categorize content based on your preferences. 

Use the configuration of an existing VM to create an instance template.

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
    
    // createTemplateFromInstance creates a new instance template based on an existing instance.
    // This new template specifies a different boot disk.
    func createTemplateFromInstance(w io.Writer, projectID, instance, templateName string) error {
    	// projectID := "your_project_id"
    	// instance := "projects/project/zones/zone/instances/instance"
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
    			Name:           proto.String(templateName),
    			SourceInstance: proto.String(instance),
    			SourceInstanceParams: &computepb.SourceInstanceParams{
    				DiskConfigs: []*computepb.DiskInstantiationConfig{
    					{
    						// Device name must match the name of a disk attached to the instance
    						// your template is based on.
    						DeviceName: proto.String("disk-1"),
    						// Replace the original boot disk image used in your instance with a Rocky Linux image.
    						InstantiateFrom: proto.String(computepb.[DiskInstantiationConfig_CUSTOM_IMAGE](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1/computepb.html#cloud_google_com_go_compute_apiv1_computepb_DiskInstantiationConfig_UNDEFINED_INSTANTIATE_FROM_DiskInstantiationConfig_ATTACH_READ_ONLY_DiskInstantiationConfig_BLANK_DiskInstantiationConfig_CUSTOM_IMAGE_DiskInstantiationConfig_DEFAULT_DiskInstantiationConfig_DO_NOT_INCLUDE_DiskInstantiationConfig_SOURCE_IMAGE_DiskInstantiationConfig_SOURCE_IMAGE_FAMILY).String()),
    						CustomImage:     proto.String("projects/rocky-linux-cloud/global/images/family/rocky-linux-8"),
    						// Override the auto_delete setting.
    						AutoDelete: proto.Bool(true),
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
    
    
    import com.google.cloud.compute.v1.[DiskInstantiationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DiskInstantiationConfig.html);
    import com.google.cloud.compute.v1.[DiskInstantiationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DiskInstantiationConfig.html).[InstantiateFrom](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DiskInstantiationConfig.InstantiateFrom.html);
    import com.google.cloud.compute.v1.[GlobalOperationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalOperationsClient.html);
    import com.google.cloud.compute.v1.[InsertInstanceTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceTemplateRequest.html);
    import com.google.cloud.compute.v1.[InstanceTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplate.html);
    import com.google.cloud.compute.v1.[InstanceTemplatesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplatesClient.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import com.google.cloud.compute.v1.[SourceInstanceParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SourceInstanceParams.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateTemplateFromInstance {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // projectId: project ID or project number of the Cloud project you use.
        // instance: the instance to base the new template on. This value uses the following format:
        // **NOTE**: "projects/{project}/zones/{zone}/instances/{instance_name}"
        // templateName: name of the new template to create.
        String projectId = "your-project-id";
        String templateName = "template-name";
        String instance = String.format("projects/%s/zones/%s/instances/%s", projectId, "zone",
            "instanceName");
        createTemplateFromInstance(projectId, templateName, instance);
      }
    
      // Create a new instance template based on an existing instance.
      // This new template specifies a different boot disk.
      public static void createTemplateFromInstance(String projectId, String templateName,
          String instance)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        try ([InstanceTemplatesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplatesClient.html) instanceTemplatesClient = [InstanceTemplatesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplatesClient.html).create();
            [GlobalOperationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalOperationsClient.html) globalOperationsClient = [GlobalOperationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalOperationsClient.html).create()) {
    
          [SourceInstanceParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SourceInstanceParams.html) sourceInstanceParams = [SourceInstanceParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SourceInstanceParams.html).newBuilder()
              .[addDiskConfigs](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SourceInstanceParams.Builder.html#com_google_cloud_compute_v1_SourceInstanceParams_Builder_addDiskConfigs_com_google_cloud_compute_v1_DiskInstantiationConfig_)([DiskInstantiationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DiskInstantiationConfig.html).newBuilder()
                  // Device name must match the name of a disk attached to the instance you are
                  // basing your template on.
                  .setDeviceName("disk-1")
                  // Replace the original boot disk image used in your instance
                  // with a Rocky Linux image.
                  .[setInstantiateFrom](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DiskInstantiationConfig.Builder.html#com_google_cloud_compute_v1_DiskInstantiationConfig_Builder_setInstantiateFrom_java_lang_String_)([InstantiateFrom](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DiskInstantiationConfig.InstantiateFrom.html).CUSTOM_IMAGE.toString())
                  .[setCustomImage](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DiskInstantiationConfig.Builder.html#com_google_cloud_compute_v1_DiskInstantiationConfig_Builder_setCustomImage_java_lang_String_)(
                      String.format("projects/%s/global/images/family/%s", "rocky-linux-cloud",
                          "rocky-linux-8"))
                  // Override the AutoDelete setting.
                  .setAutoDelete(true).build())
              .build();
    
          [InstanceTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplate.html) instanceTemplate = [InstanceTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplate.html).newBuilder()
              .setName(templateName)
              .setSourceInstance(instance)
              .[setSourceInstanceParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplate.Builder.html#com_google_cloud_compute_v1_InstanceTemplate_Builder_setSourceInstanceParams_com_google_cloud_compute_v1_SourceInstanceParams_)(sourceInstanceParams)
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
            System.out.println("Instance Template creation failed ! ! " + response);
            return;
          }
          System.out.printf("Instance Template creation operation status %s: %s", templateName,
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
    // const instance = 'projects/project/zones/zone/instances/instance';
    // const templateName = 'your_template_name';
    
    const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    
    // Create a new instance template based on an existing instance.
    // This new template specifies a different boot disk.
    async function createTemplateFromInstance() {
      const instanceTemplatesClient = new compute.[InstanceTemplatesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      const [response] = await instanceTemplatesClient.insert({
        project: projectId,
        instanceTemplateResource: {
          name: templateName,
          sourceInstance: instance,
          sourceInstanceParams: {
            diskConfigs: [
              {
                // Device name must match the name of a disk attached to the instance
                // your template is based on.
                deviceName: 'disk-1',
                // Replace the original boot disk image used in your instance with a Rocky Linux image.
                instantiateFrom: 'CUSTOM_IMAGE',
                customImage:
                  'projects/rocky-linux-cloud/global/images/family/rocky-linux-8',
                // Override the auto_delete setting.
                autoDelete: true,
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
    
    createTemplateFromInstance();

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
    
    
    def create_template_from_instance(
        project_id: str, instance: str, template_name: str
    ) -> compute_v1.InstanceTemplate:
        """
        Create a new instance template based on an existing instance.
        This new template specifies a different boot disk.
    
        Args:
            project_id: project ID or project number of the Cloud project you use.
            instance: the instance to base the new template on. This value uses
                the following format: "projects/{project}/zones/{zone}/instances/{instance_name}"
            template_name: name of the new template to create.
    
        Returns:
            InstanceTemplate object that represents the new instance template.
        """
        disk = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[DiskInstantiationConfig](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.DiskInstantiationConfig.html)()
        # Device name must match the name of a disk attached to the instance you are
        # basing your template on.
        disk.device_name = "disk-1"
        # Replace the original boot disk image used in your instance with a Rocky Linux image.
        disk.instantiate_from = "CUSTOM_IMAGE"
        disk.custom_image = "projects/rocky-linux-cloud/global/images/family/rocky-linux-8"
        # Override the auto_delete setting.
        disk.auto_delete = True
    
        template = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[InstanceTemplate](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.InstanceTemplate.html)()
        template.name = template_name
        template.source_instance = instance
        template.source_instance_params = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[SourceInstanceParams](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.SourceInstanceParams.html)()
        template.source_instance_params.disk_configs = [disk]
    
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
