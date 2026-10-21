---
url: https://docs.cloud.google.com/compute/docs/instances/reservations-prevent-consumption/
title: Prevent compute instances from consuming reservations \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:28:47.307957+00:00
---

# Prevent compute instances from consuming reservations  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/reservations-prevent-consumption/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Prevent compute instances from consuming reservations Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to prevent Compute Engine instances from consuming reservations. To learn more about reservations, see [Reservations of Compute Engine zonal resources](https://docs.cloud.google.com/compute/docs/instances/reservations-overview).

[_Automatically consumed_ reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#consumption-type) allow instances with properties that match the reservations to automatically consume them. To prevent instances from consuming a reservation, do one of the following:

  * Configure instances to not consume reservations, as described in this document.

  * Create or update instances with properties that don't match the reservation.




You can avoid consuming reservations when you want to use your instances for tasks like testing, debugging, or isolated deployments.

## Limitations

You can only update an existing instance to not consume reservations if the instance is configured to automatically consume matching reservations.

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




### Required roles

To get the permissions that you need to prevent a compute instance from consuming reservations, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to prevent a compute instance from consuming reservations. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to prevent a compute instance from consuming reservations:

  * To create reservations: `compute.reservations.create` on the project 
  * To create instances: 
    * `compute.instances.create` on the project
    * To use a custom image to create the VM: `compute.images.useReadOnly` on the image
    * To use a snapshot to create the VM: `compute.snapshots.useReadOnly` on the snapshot
    * To use an instance template to create the VM: `compute.instanceTemplates.useReadOnly` on the instance template
    * To assign a [legacy network](https://docs.cloud.google.com/vpc/docs/legacy) to the VM: `compute.networks.use` on the project
    * To specify a static IP address for the VM: `compute.addresses.use` on the project
    * To assign an external IP address to the VM when using a legacy network: `compute.networks.useExternalIp` on the project
    * To specify a subnet for the VM: `compute.subnetworks.use` on the project or on the chosen subnet
    * To assign an external IP address to the VM when using a VPC network: `compute.subnetworks.useExternalIp` on the project or on the chosen subnet
    * To set VM instance metadata for the VM: `compute.instances.setMetadata` on the project
    * To set tags for the VM: `compute.instances.setTags` on the VM
    * To set labels for the VM: `compute.instances.setLabels` on the VM
    * To set a service account for the VM to use: `compute.instances.setServiceAccount` on the VM
    * To create a new disk for the VM: `compute.disks.create` on the project
    * To attach an existing disk in read-only or read-write mode: `compute.disks.use` on the disk
    * To attach an existing disk in read-only mode: `compute.disks.useReadOnly` on the disk
  * To create instance templates: `compute.instanceTemplates.create` on the project 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Prevent reservation consumption

To prevent a compute instance from consuming reservations, set its reservation affinity (`reservationAffinity`) property to not consume reservations. This property controls if an instance can consume matching reservations, a specific reservation, or no reservations.

To prevent one or more instances from consuming reservations, use one of the following methods:

  * Prevent consumption in an existing instance

  * Prevent consumption while creating an instance

  * Prevent consumption while creating instances in bulk

  * Prevent consumption while creating an instance template




### Prevent consumption in an existing instance

You can update a running instance so that it no longer automatically consumes reservations. You must restart the instance to make the changes effective, as described in this section.

To prevent an existing instance from consuming reservations, select one of the following options:

###  gcloud 

  1. Create an empty YAML file.

  2. To export the properties of an instance into the YAML file that you've just created, use the [`gcloud compute instances export` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/export):
         
         gcloud compute instances export INSTANCE_NAME \
             --destination=YAML_FILE \
             --zone=ZONE
         

Replace the following:

     * `INSTANCE_NAME`: the name of the instance.

     * `YAML_FILE`: the path to the empty YAML file that you created in the previous step.

     * `ZONE`: the zone where the instance exists.

  3. In the `reservationAffinity` section of the YAML configuration file, set the `consumeReservationType` field to `NO_RESERVATION`. If the YAML file doesn't contain a `reservationAffinity` section, then add the following block at the end of the file:
         
         reservationAffinity:
           consumeReservationType: NO_RESERVATION
         

**Tip:** To avoid getting an error such as `"ERROR: (gcloud.compute.instances.update-from-file) Cannot parse YAML: [Expected type  for field value, found True (type )]"`, add quotes (`' '`) around any label values of `yes` or `no` in the exported instance configuration file. This indicates the values are strings, not Boolean values.
  4. To update the instance and restart it, use the [`gcloud compute instances update-from-file` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/update-from-file) with the `--most-disruptive-allowed-action` flag set to `RESTART`:
         
         gcloud compute instances update-from-file INSTANCE_NAME \
             --most-disruptive-allowed-action=RESTART \
             --source=YAML_FILE \
             --zone=ZONE
         

Replace the following:

     * `INSTANCE_NAME`: the name of the instance.

     * `YAML_FILE`: the path to the YAML file with the configuration data that you modified in the previous step.

     * `ZONE`: the zone where the instance exists.




###  REST 

  1. To view the properties of an existing instance, make a `GET` request to the [`instances.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/get):
         
         GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME
         

Replace the following:

     * `PROJECT_ID`: the ID of the project where you created the instance.

     * `ZONE`: the zone where the instance exists.

     * `INSTANCE_NAME`: the name of the instance.

  2. Store the output from the `GET` request in a file or text editor. In the `reservationAffinity` object, set the `consumeReservationType` field to `NO_RESERVATION`. If the output doesn't contain a `reservationAffinity` object, then add the following object at the end of the JSON file:
         
         {
           ...
           "reservationAffinity": {
             "consumeReservationType": "NO_RESERVATION"
           }
         }
         

  3. To update the instance and restart it, make a `PUT` request to the [`instances.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/update). In the request, do the following:

     * In the request URL, include the `mostDisruptiveAllowedAction` query parameter set to `RESTART`.

     * For the request body, use the output from the `GET` request that you edited in a previous step.

The request is similar to the following example:
    
    PUT https://compute.googleapis.com/compute/v1/projects/example-project/zones/us-central-1/instances/instance-01?mostDisruptiveAllowedAction=RESTART
    
    {
      ...
      "reservationAffinity": {
        "consumeReservationType": "NO_RESERVATION"
      },
      ...
    }
    




For more information about updating an instance, see [Update instance properties](https://docs.cloud.google.com/compute/docs/instances/update-instance-properties#update).

### Prevent consumption while creating an instance

To create a compute instance that can't consume reservations, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. In the **Name** field, enter a name for the instance.

  3. In the **Region** and **Zone** lists, select the region and zone in which to create the instance.

  4. Specify the machine type to use for the instance.

  5. In the navigation menu, click **Advanced**.

  6. In the **Reservations** section, select **Don't use a reservation**.

  7. Click **Create**.




###  gcloud 

To create an instance that can't consume reservations, use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) with the `--reservation-affinity` flag set to `none`:
    
    
    gcloud compute instances create INSTANCE_NAME \
        --machine-type=MACHINE_TYPE \
        --reservation-affinity=none \
        --zone=ZONE
    

Replace the following:

  * `INSTANCE_NAME`: the name of the instance.

  * `MACHINE_TYPE`: the machine type to use for the instance.

  * `ZONE`: the zone in which to create the instance.




###  Go 

To create an instance that can't consume reservations, use the following code sample:
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    	"google.golang.org/protobuf/proto"
    )
    
    // createInstanceNotConsumeReservation creates VM, without consuming reservation
    func createInstanceNotConsumeReservation(w io.Writer, projectID, zone, instanceName string) error {
    	ctx := context.Background()
    	machineType := fmt.Sprintf("zones/%s/machineTypes/%s", zone, "n2-standard-32")
    	sourceImage := "projects/debian-cloud/global/images/family/debian-12"
    
    	instancesClient, err := compute.[NewInstancesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_InstancesClient_NewInstancesRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewInstancesRESTClient: %w", err)
    	}
    	defer instancesClient.Close()
    
    	req := &computepb.InsertInstanceRequest{
    		Project: projectID,
    		Zone:    zone,
    		InstanceResource: &computepb.Instance{
    			Disks: []*computepb.AttachedDisk{
    				{
    					InitializeParams: &computepb.AttachedDiskInitializeParams{
    						DiskSizeGb:  proto.Int64(10),
    						SourceImage: proto.String(sourceImage),
    					},
    					AutoDelete: proto.Bool(true),
    					Boot:       proto.Bool(true),
    					Type:       proto.String(computepb.[AttachedDisk_PERSISTENT](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1/computepb.html#cloud_google_com_go_compute_apiv1_computepb_AttachedDisk_UNDEFINED_TYPE_AttachedDisk_PERSISTENT_AttachedDisk_SCRATCH).String()),
    				},
    			},
    			MachineType:    proto.String(machineType),
    			MinCpuPlatform: proto.String("Intel Cascade Lake"),
    			Name:           proto.String(instanceName),
    			NetworkInterfaces: []*computepb.NetworkInterface{
    				{
    					Network: proto.String("global/networks/default"),
    				},
    			},
    			ReservationAffinity: &computepb.ReservationAffinity{
    				ConsumeReservationType: proto.String("NO_RESERVATION"),
    			},
    		},
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

To create an instance that can't consume reservations, use the following code sample:
    
    
    import static com.google.cloud.compute.v1.[ReservationAffinity](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationAffinity.html).[ConsumeReservationType](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationAffinity.ConsumeReservationType.html).[NO_RESERVATION](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationAffinity.ConsumeReservationType.html#com_google_cloud_compute_v1_ReservationAffinity_ConsumeReservationType_NO_RESERVATION);
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.compute.v1.[AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html);
    import com.google.cloud.compute.v1.[AttachedDiskInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDiskInitializeParams.html);
    import com.google.cloud.compute.v1.[InsertInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceRequest.html);
    import com.google.cloud.compute.v1.[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html);
    import com.google.cloud.compute.v1.[InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html);
    import com.google.cloud.compute.v1.[NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import com.google.cloud.compute.v1.[ReservationAffinity](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationAffinity.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateInstanceWithoutConsumingReservation {
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Cloud project you want to use.
        String projectId = "YOUR_PROJECT_ID";
        // Name of the zone you want to use.
        String zone = "us-central1-a";
        // Name of the VM instance you want to query.
        String instanceName = "YOUR_INSTANCE_NAME";
        // machineType: machine type of the VM being created.
        // *   This value uses the format zones/{zone}/machineTypes/{type_name}.
        // *   For a list of machine types, see https://cloud.google.com/compute/docs/machine-types
        String machineTypeName = "n1-standard-1";
        // sourceImage: path to the operating system image to mount.
        // *   For details about images you can mount, see https://cloud.google.com/compute/docs/images
        String sourceImage = "projects/debian-cloud/global/images/family/debian-13";
        // diskSizeGb: storage size of the boot disk to attach to the instance.
        long diskSizeGb = 10L;
        // networkName: network interface to associate with the instance.
        String networkName = "default";
    
        createInstanceWithoutConsumingReservationAsync(projectId, zone, instanceName,
            machineTypeName, sourceImage, diskSizeGb, networkName);
      }
    
      // Create a virtual machine that explicitly doesn't consume reservations
      public static [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html) createInstanceWithoutConsumingReservationAsync(
          String project, String zone, String instanceName,
          String machineTypeName, String sourceImage, long diskSizeGb, String networkName)
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
        String machineType = String.format("zones/%s/machineTypes/%s", zone, machineTypeName);
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html) instancesClient = [InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html).create()) {
          [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html) disk =
              [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html).newBuilder()
                  .setBoot(true)
                  .setAutoDelete(true)
                  .setType([AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html).Type.PERSISTENT.toString())
                  .setDeviceName("disk-1")
                  .[setInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.Builder.html#com_google_cloud_compute_v1_AttachedDisk_Builder_setInitializeParams_com_google_cloud_compute_v1_AttachedDiskInitializeParams_)(
                      [AttachedDiskInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDiskInitializeParams.html).newBuilder()
                          .setSourceImage(sourceImage)
                          .setDiskSizeGb(diskSizeGb)
                          .build())
                  .build();
    
          [NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html) networkInterface = [NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html).newBuilder()
              .setName(networkName)
              .build();
    
          [ReservationAffinity](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationAffinity.html) reservationAffinity =
              [ReservationAffinity](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationAffinity.html).newBuilder()
                  .[setConsumeReservationType](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationAffinity.Builder.html#com_google_cloud_compute_v1_ReservationAffinity_Builder_setConsumeReservationType_java_lang_String_)([NO_RESERVATION](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationAffinity.ConsumeReservationType.html#com_google_cloud_compute_v1_ReservationAffinity_ConsumeReservationType_NO_RESERVATION).toString())
                  .build();
    
          [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html) instanceResource =
              [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html).newBuilder()
                  .setName(instanceName)
                  .setMachineType(machineType)
                  .addDisks(disk)
                  .addNetworkInterfaces(networkInterface)
                  .setReservationAffinity(reservationAffinity)
                  .build();
    
          [InsertInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceRequest.html) insertInstanceRequest = [InsertInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceRequest.html).newBuilder()
              .setProject(project)
              .setZone(zone)
              .setInstanceResource(instanceResource)
              .build();
    
          OperationFuture<Operation, Operation> operation = instancesClient.insertAsync(
              insertInstanceRequest);
    
          // Wait for the operation to complete.
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) response = operation.get(3, TimeUnit.MINUTES);
    
          if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            return null;
          }
          return instancesClient.get(project, zone, instanceName);
        }
      }
    }

###  Node.js 

To create an instance that can't consume reservations, use the following code sample:
    
    
    // Import the Compute library
    const computeLib = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    const compute = computeLib.protos.google.cloud.compute.v1;
    
    // Instantiate a reservationsClient
    const instancesClient = new computeLib.[InstancesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    // Instantiate a zoneOperationsClient
    const zoneOperationsClient = new computeLib.[ZoneOperationsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
    /**
     * TODO(developer): Update/uncomment these variables before running the sample.
     */
    // The ID of the project where you want to create instance.
    const projectId = await instancesClient.getProjectId();
    // The zone in which to create instance.
    const zone = 'us-central1-a';
    // The name of the instance to create.
    // const instanceName = 'instance-01';
    // Machine type to use for VM.
    const machineType = 'n1-standard-4';
    
    // Create a VM that explicitly doesn't consume reservations
    async function callCreateInstanceToNotConsumeReservation() {
      // Describe the size and source image of the boot disk to attach to the instance.
      const disk = new compute.Disk({
        boot: true,
        autoDelete: true,
        type: 'PERSISTENT',
        initializeParams: {
          diskSizeGb: '10',
          sourceImage: 'projects/debian-cloud/global/images/family/debian-12',
        },
      });
    
      //  Define networkInterface
      const networkInterface = new compute.NetworkInterface({
        name: 'global/networks/default',
      });
    
      // Define reservationAffinity
      const reservationAffinity = new compute.ReservationAffinity({
        consumeReservationType: 'NO_RESERVATION',
      });
    
      // Create an instance
      const instance = new compute.Instance({
        name: instanceName,
        machineType: `zones/${zone}/machineTypes/${machineType}`,
        minCpuPlatform: 'Intel Skylake',
        disks: [disk],
        networkInterfaces: [networkInterface],
        reservationAffinity,
      });
    
      const [response] = await instancesClient.insert({
        project: projectId,
        instanceResource: instance,
        zone,
      });
    
      let operation = response.latestResponse;
    
      // Wait for the create instance operation to complete.
      while (operation.status !== 'DONE') {
        [operation] = await zoneOperationsClient.wait({
          operation: operation.name,
          project: projectId,
          zone: operation.zone.split('/').pop(),
        });
      }
    
      console.log(`Instance ${instanceName} created.`);
    }
    
    await callCreateInstanceToNotConsumeReservation();

###  Python 

To create an instance that can't consume reservations, use the following code sample:
    
    
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
    
    
    def create_vm_not_consume_reservation(
        project_id: str, zone: str, instance_name: str, machine_type: str = "n2-standard-2"
    ) -> compute_v1.Instance:
        """Creates a VM that explicitly doesn't consume reservations
        Args:
            project_id (str): The ID of the Google Cloud project.
            zone (str): The zone where the VM will be created.
            instance_name (str): The name of the instance to create.
            machine_type (str, optional): The machine type for the instance.
        Returns:
            compute_v1.Instance: The created instance.
        """
        instance = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[Instance](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.Instance.html)()
        instance.name = instance_name
        instance.machine_type = f"zones/{zone}/machineTypes/{machine_type}"
        instance.zone = zone
    
        instance.[disks](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.html) = [
            [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[AttachedDisk](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.AttachedDisk.html)(
                boot=True,  # Indicates that this is a boot disk
                auto_delete=True,  # The disk will be deleted when the instance is deleted
                initialize_params=[compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[AttachedDiskInitializeParams](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.AttachedDiskInitializeParams.html)(
                    source_image="projects/debian-cloud/global/images/family/debian-13",
                    disk_size_gb=10,
                ),
            )
        ]
    
        instance.network_interfaces = [
            [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[NetworkInterface](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.NetworkInterface.html)(
                network="global/networks/default",  # The network to use
                access_configs=[
                    [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[AccessConfig](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.AccessConfig.html)(
                        name="External NAT",  # Name of the access configuration
                        type="ONE_TO_ONE_NAT",  # Type of access configuration
                    )
                ],
            )
        ]
    
        # Set the reservation affinity to not consume any reservation
        instance.reservation_affinity = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[ReservationAffinity](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.ReservationAffinity.html)(
            consume_reservation_type="NO_RESERVATION",  # Prevents the instance from consuming reservations
        )
    
        # Create a request to insert the instance
        request = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[InsertInstanceRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.InsertInstanceRequest.html)()
        request.zone = zone
        request.project = project_id
        request.instance_resource = instance
    
        vm_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html)()
        operation = vm_client.[insert](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html#google_cloud_compute_v1_services_instances_InstancesClient_insert)(request)
        wait_for_extended_operation(operation, "Instance creation")
    
        print(f"Creating the {instance_name} instance in {zone}...")
    
        return vm_client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html#google_cloud_compute_v1_services_instances_InstancesClient_get)(project=project_id, zone=zone, instance=instance_name)
    
    

###  REST 

To create an instance that can't consume reservations, make a `POST` request to the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert). In the request body, include the `consumeReservationType` field set to `NO_RESERVATION`:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    
    {
      "name": "INSTANCE_NAME",
      "machineType": "zones/ZONE/machineTypes/MACHINE_TYPE",
      "disks": [
        {
          "boot": true,
          "initializeParams": {
            "sourceImage": "projects/IMAGE_PROJECT/global/images/IMAGE"
          }
        }
      ],
      "networkInterfaces": [
        {
          "network": "global/networks/default"
        }
      ],
      "reservationAffinity": {
        "consumeReservationType": "NO_RESERVATION"
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where you want to create the instance.

  * `ZONE`: the zone in which to create the instance.

  * `INSTANCE_NAME`: the name of the instance.

  * `MACHINE_TYPE`: the machine type to use for the instance.

  * `IMAGE_PROJECT`: the image project that contains the OS image; for example, `debian-cloud`. For more information about the supported image projects, see [Public images](https://docs.cloud.google.com/compute/docs/images#os-compute-support).

  * `IMAGE`: specify one of the following:

    * A specific version of the OS image; for example, `debian-12-bookworm-v20240617`.

    * An [image family](https://docs.cloud.google.com/compute/docs/images/os-details), which must be formatted as `family/IMAGE_FAMILY`. This specifies the most recent, non-deprecated OS image. For example, if you specify `family/debian-12`, the latest version in the Debian 12 image family is used. For more information about using image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).




For more information about creating an instance, see [Create and start a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).

### Prevent consumption while creating instances in bulk

To create compute instances in bulk that can't consume reservations, select one of the following options:

###  gcloud 

To create instances in bulk that can't consume reservations, use the [`gcloud compute instances bulk create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/bulk/create) with the `--reservation-affinity` flag set to `none`.

For example, to create instances in bulk in a single zone and specify a name pattern, run the following command:
    
    
    gcloud compute instances bulk create \
        --count=COUNT \
        --machine-type=MACHINE_TYPE \
        --name-pattern="NAME_PATTERN" \
        --reservation-affinity=none \
        --zone=ZONE
    

Replace the following:

  * `COUNT`: the number of instances to create.

  * `MACHINE_TYPE`: the machine type to use for the instances.

  * `NAME_PATTERN`: the name pattern for the instances. To replace a sequence of numbers in an instance name, use a sequence of hash (`#`) characters. For example, using `instance-#` for the name pattern generates instances with names starting with `instance-1`, `instance-2`, and continuing up to the number of instances specified by `COUNT`.

  * `ZONE`: the zone in which to create instances in bulk.




###  REST 

To create instances in bulk that can't consume reservations, make a `POST` request to the [`instances.bulkInsert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/bulkInsert). In the request body, include the `consumeReservationType` field set to `NO_RESERVATION`.

For example, to create instances in bulk in a single zone and specify a name pattern, make a request as follows:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/bulkInsert
    
    {
      "count": COUNT,
      "namePattern": "NAME_PATTERN",
      "instanceProperties": {
        "machineType": "MACHINE_TYPE",
        "disks": [
          {
            "boot": true,
            "initializeParams": {
              "sourceImage": "projects/IMAGE_PROJECT/global/images/IMAGE"
            }
          }
        ],
        "networkInterfaces": [
          {
            "network": "global/networks/default"
          }
        ],
        "reservationAffinity": {
          "consumeReservationType": "NO_RESERVATION"
        }
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project in which to create instances in bulk.

  * `ZONE`: the zone in which to create instances in bulk.

  * `COUNT`: the number of instances to create.

  * `NAME_PATTERN`: the name pattern for the instances. To replace a sequence of numbers in an instance name, use a sequence of hash (`#`) characters. For example, using `instance-#` for the name pattern generates instances with names starting with `instance-1`, `instance-2`, and continuing up to the number of instances specified by `COUNT`.

  * `MACHINE_TYPE`: the machine type to use for the instances.

  * `IMAGE_PROJECT`: the image project that contains the OS image; for example, `debian-cloud`. For more information about the supported image projects, see [Public images](https://docs.cloud.google.com/compute/docs/images#os-compute-support).

  * `IMAGE`: specify one of the following:

    * A specific version of the OS image; for example, `debian-12-bookworm-v20240617`.

    * An [image family](https://docs.cloud.google.com/compute/docs/images/os-details), which must be formatted as `family/IMAGE_FAMILY`. This specifies the most recent, non-deprecated OS image. For example, if you specify `family/debian-12`, the latest version in the Debian 12 image family is used. For more information about using image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).




For more information about creating instances in bulk, see [Create VMs in bulk](https://docs.cloud.google.com/compute/docs/instances/multiple/create-in-bulk).

### Prevent consumption while creating an instance template

After you create an instance template that configures instances to not consume reservations, you can use the template to do the following:

  * Prevent the compute instances in a managed instance group (MIG) from consuming reservations when you do the following:

    * [Create a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#create_managed_group)

    * [Apply new instance configurations in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs)

  * [Create an instance that doesn't consume reservations](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-instance-template)




To create an instance template that configures instances to not consume reservations, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Create an instance template** page.

[Go to Create an instance template](https://console.cloud.google.com/compute/instanceTemplates/add)

  2. In the **Name** field, enter a name for the instance template.

  3. In the **Location** section, specify whether you want to create a regional (default) or global instance template.

  4. In the **Machine configuration** section, specify the machine type to use for the instances created using the template.

  5. Expand the **Advanced options** section, and then do the following:

     1. Expand the **Management** section.

     2. In the **Reservations** section, select **Don't use a reservation**.

  6. Click **Create**.




###  gcloud 

To create an instance template that configures instances to not consume reservations, use the [`gcloud compute instances-templates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create) with the `--reservation-affinity` flag set to `none`.

To create a regional instance template that configures instances to not consume reservations, run the following command. If you want to create a global instance template, then use the same command without the `--instance-template-region` flag.
    
    
    gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME \
        --instance-template-region=REGION \
        --machine-type=MACHINE_TYPE \
        --reservation-affinity=none
    

Replace the following:

  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.

  * `REGION`: the region in which to create the instance template.

  * `MACHINE_TYPE`: the machine type to use for the instances created using the instance template.




###  Go 

To create an instance template that configures instances to not consume reservations, use the following code sample:
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    	"google.golang.org/protobuf/proto"
    )
    
    // createInstanceNotConsumeReservation creates a new instance template, which won't consume reservations
    func createTemplateNotConsumeReservation(w io.Writer, projectID, templateName string) error {
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
    						Network: proto.String("global/networks/default"),
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
    				ReservationAffinity: &computepb.ReservationAffinity{
    					ConsumeReservationType: proto.String("NO_RESERVATION"),
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
    

###  Java 

To create an instance template that configures instances to not consume reservations, use the following code sample:
    
    
    import static com.google.cloud.compute.v1.[ReservationAffinity](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationAffinity.html).[ConsumeReservationType](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationAffinity.ConsumeReservationType.html).[NO_RESERVATION](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationAffinity.ConsumeReservationType.html#com_google_cloud_compute_v1_ReservationAffinity_ConsumeReservationType_NO_RESERVATION);
    
    import com.google.cloud.compute.v1.[AccessConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AccessConfig.html);
    import com.google.cloud.compute.v1.[AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html);
    import com.google.cloud.compute.v1.[AttachedDiskInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDiskInitializeParams.html);
    import com.google.cloud.compute.v1.[InsertInstanceTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceTemplateRequest.html);
    import com.google.cloud.compute.v1.[InstanceProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceProperties.html);
    import com.google.cloud.compute.v1.[InstanceTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplate.html);
    import com.google.cloud.compute.v1.[InstanceTemplatesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplatesClient.html);
    import com.google.cloud.compute.v1.[NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import com.google.cloud.compute.v1.[ReservationAffinity](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationAffinity.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateTemplateWithoutConsumingReservation {
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Cloud project you want to use.
        String projectId = "YOUR_PROJECT_ID";
        // Name of the template you want to query.
        String templateName = "YOUR_INSTANCE_TEMPLATE_NAME";
        String machineType = "e2-standard-4";
        String sourceImage = "projects/debian-cloud/global/images/family/debian-13";
    
        createTemplateWithoutConsumingReservationAsync(
            projectId, templateName, machineType, sourceImage);
      }
    
    
      // Create a template that explicitly doesn't consume any reservations.
      public static [InstanceTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplate.html) createTemplateWithoutConsumingReservationAsync(
          String projectId, String templateName, String machineType, String sourceImage)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([InstanceTemplatesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplatesClient.html) instanceTemplatesClient = [InstanceTemplatesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplatesClient.html).create()) {
          [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html) attachedDisk = [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html).newBuilder()
              .[setInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.Builder.html#com_google_cloud_compute_v1_AttachedDisk_Builder_setInitializeParams_com_google_cloud_compute_v1_AttachedDiskInitializeParams_)([AttachedDiskInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDiskInitializeParams.html).newBuilder()
                  .setSourceImage(sourceImage)
                  .setDiskType("pd-balanced")
                  .setDiskSizeGb(250)
                  .build())
              .setAutoDelete(true)
              .setBoot(true)
              .build();
    
          [NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html) networkInterface = [NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html).newBuilder()
              .setName("global/networks/default")
              .[addAccessConfigs](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.Builder.html#com_google_cloud_compute_v1_NetworkInterface_Builder_addAccessConfigs_com_google_cloud_compute_v1_AccessConfig_)([AccessConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AccessConfig.html).newBuilder()
                  .setName("External NAT")
                  .setType([AccessConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AccessConfig.html).Type.ONE_TO_ONE_NAT.toString())
                  .setNetworkTier([AccessConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AccessConfig.html).NetworkTier.PREMIUM.toString())
                  .build())
              .build();
    
          [ReservationAffinity](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationAffinity.html) reservationAffinity =
              [ReservationAffinity](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationAffinity.html).newBuilder()
                  .[setConsumeReservationType](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationAffinity.Builder.html#com_google_cloud_compute_v1_ReservationAffinity_Builder_setConsumeReservationType_java_lang_String_)([NO_RESERVATION](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationAffinity.ConsumeReservationType.html#com_google_cloud_compute_v1_ReservationAffinity_ConsumeReservationType_NO_RESERVATION).toString())
                  .build();
    
          [InstanceProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceProperties.html) instanceProperties = [InstanceProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceProperties.html).newBuilder()
              .addDisks(attachedDisk)
              .setMachineType(machineType)
              .setReservationAffinity(reservationAffinity)
              .addNetworkInterfaces(networkInterface)
              .build();
    
          [InsertInstanceTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceTemplateRequest.html) insertInstanceTemplateRequest = [InsertInstanceTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceTemplateRequest.html)
              .newBuilder()
              .setProject(projectId)
              .setInstanceTemplateResource([InstanceTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplate.html).newBuilder()
                  .setName(templateName)
                  .setProperties(instanceProperties)
                  .build())
              .build();
    
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) response = instanceTemplatesClient.insertAsync(insertInstanceTemplateRequest)
              .get(3, TimeUnit.MINUTES);
    
          if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            return null;
          }
          return instanceTemplatesClient.get(projectId, templateName);
        }
      }
    }

###  Node.js 

To create an instance template that configures instances to not consume reservations, use the following code sample:
    
    
    // Import the Compute library
    const computeLib = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    const compute = computeLib.protos.google.cloud.compute.v1;
    
    // Instantiate an instanceTemplatesClient
    const instanceTemplatesClient = new computeLib.[InstanceTemplatesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    // Instantiate a globalOperationsClient
    const globalOperationsClient = new computeLib.[GlobalOperationsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
    /**
     * TODO(developer): Update/uncomment these variables before running the sample.
     */
    // The ID of the project where you want to create template.
    const projectId = await instanceTemplatesClient.getProjectId();
    // The name of the template to create.
    // const templateName = 'instance-01';
    
    // Create an instance template that creates VMs that don't explicitly consume reservations
    async function callCreateTemplateToNotConsumeReservation() {
      // Define the boot disk for the instance template
      const disk = new compute.AttachedDisk({
        initializeParams: new compute.AttachedDiskInitializeParams({
          sourceImage:
            'projects/debian-cloud/global/images/debian-12-bookworm-v20240815',
          diskSizeGb: '100',
          diskType: 'pd-balanced',
        }),
        autoDelete: true,
        boot: true,
        type: 'PERSISTENT',
      });
    
      // Define the network interface for the instance template
      const network = new compute.NetworkInterface({
        network: `projects/${projectId}/global/networks/default`,
      });
    
      // Define reservationAffinity
      const reservationAffinity = new compute.ReservationAffinity({
        consumeReservationType: 'NO_RESERVATION',
      });
    
      // Define instance template
      const instanceTemplate = new compute.InstanceTemplate({
        name: templateName,
        properties: {
          disks: [disk],
          machineType: 'e2-medium',
          // The template connects the instance to the `default` network,
          // without specifying a subnetwork.
          networkInterfaces: [network],
          reservationAffinity,
        },
      });
    
      const [response] = await instanceTemplatesClient.insert({
        project: projectId,
        instanceTemplateResource: instanceTemplate,
      });
    
      let operation = response.latestResponse;
    
      // Wait for the create instance operation to complete.
      while (operation.status !== 'DONE') {
        [operation] = await globalOperationsClient.wait({
          operation: operation.name,
          project: projectId,
        });
      }
    
      console.log(`Template ${templateName} created.`);
    }
    
    await callCreateTemplateToNotConsumeReservation();

###  Python 

To create an instance template that configures instances to not consume reservations, use the following code sample:
    
    
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
    
    
    def create_instance_template_not_consume_reservation(
        project_id: str,
        template_name: str,
        machine_type: str = "n1-standard-1",
    ) -> compute_v1.InstanceTemplate:
        """
        Creates an instance template that creates VMs that don't explicitly consume reservations
    
        Args:
            project_id: project ID or project number of the Cloud project you use.
            template_name: name of the new template to create.
            machine_type: machine type for the instance.
        Returns:
            InstanceTemplate object that represents the new instance template.
        """
    
        template = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[InstanceTemplate](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.InstanceTemplate.html)()
        template.name = template_name
        template.properties.machine_type = machine_type
        # The template describes the size and source image of the boot disk
        # to attach to the instance.
        template.properties.[disks](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.html) = [
            [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[AttachedDisk](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.AttachedDisk.html)(
                boot=True,
                auto_delete=True,  # The disk will be deleted when the instance is deleted
                initialize_params=[compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[AttachedDiskInitializeParams](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.AttachedDiskInitializeParams.html)(
                    source_image="projects/debian-cloud/global/images/family/debian-13",
                    disk_size_gb=10,
                ),
            )
        ]
        # The template connects the instance to the `default` network,
        template.properties.network_interfaces = [
            [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[NetworkInterface](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.NetworkInterface.html)(
                network="global/networks/default",
                access_configs=[
                    [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[AccessConfig](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.AccessConfig.html)(
                        name="External NAT",
                        type="ONE_TO_ONE_NAT",
                    )
                ],
            )
        ]
        # The template doesn't explicitly consume reservations
        template.properties.reservation_affinity = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[ReservationAffinity](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.ReservationAffinity.html)(
            consume_reservation_type="NO_RESERVATION"
        )
    
        template_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[InstanceTemplatesClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instance_templates.InstanceTemplatesClient.html)()
        operation = template_client.[insert](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instance_templates.InstanceTemplatesClient.html#google_cloud_compute_v1_services_instance_templates_InstanceTemplatesClient_insert)(
            project=project_id, instance_template_resource=template
        )
    
        wait_for_extended_operation(operation, "instance template creation")
    
        return template_client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instance_templates.InstanceTemplatesClient.html#google_cloud_compute_v1_services_instance_templates_InstanceTemplatesClient_get)(project=project_id, instance_template=template_name)
    
    

###  REST 

To create an instance template that configures instances to not consume reservations, make a `POST` request to one of the following methods:

  * To create a global instance template: [`instanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates/insert).

  * To create a regional instance template: [`regionInstanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates/insert).




In the request body, include the `consumeReservationType` field and set it to `NO_RESERVATION`.

For example, to create a regional instance template and specify to not consume reservations, make a request as follows:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/InstanceTemplates
    
    {
      "name": "INSTANCE_TEMPLATE_NAME",
      "properties": {
        "machineType": "MACHINE_TYPE",
        "disks": [
          {
            "boot": true,
            "initializeParams": {
              "sourceImage": "projects/IMAGE_PROJECT/global/images/IMAGE"
            }
          }
        ],
        "networkInterfaces": [
          {
            "network": "global/networks/default"
          }
        ],
        "reservationAffinity": {
          "consumeReservationType": "NO_RESERVATION"
        }
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project in which to create the instance template.

  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.

  * `MACHINE_TYPE`: the machine type to use for the instances created using the instance template.

  * `IMAGE_PROJECT`: the image project that contains the OS image; for example, `debian-cloud`. For more information about the supported image projects, see [Public images](https://docs.cloud.google.com/compute/docs/images#os-compute-support).

  * `IMAGE`: specify one of the following:

    * A specific version of the OS image; for example, `debian-12-bookworm-v20240617`.

    * An [image family](https://docs.cloud.google.com/compute/docs/images/os-details), which must be formatted as `family/IMAGE_FAMILY`. This specifies the most recent, non-deprecated OS image. For example, if you specify `family/debian-12`, the latest version in the Debian 12 image family is used. For more information about using image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).




For more information about creating instance templates, see [Create instance templates](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates).

## What's next

  * [Modify reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-modify)

  * [Delete reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-delete)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
