---
url: https://docs.cloud.google.com/compute/docs/api/how-tos/api-requests-responses/
title: Creating API requests and handling responses \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:03.693767+00:00
---

# Creating API requests and handling responses  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/api/how-tos/api-requests-responses/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Creating API requests and handling responses Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to construct API requests and handle API responses from the Compute Engine API. It covers the following tasks:

  * Construct a request body.
  * Determine the resource URIs necessary for a request.
  * Handle API responses.
  * Determine whether an API request succeeded.



This document does not cover how to authenticate to the API. To learn how to authenticate to the API, read [Authenticate to Compute Engine](https://docs.cloud.google.com/compute/docs/authentication).

## Before you begin

  * Get familiar with [REST APIs](https://en.wikipedia.org/wiki/Representational_state_transfer).
  * Know how to [authenticate](https://docs.cloud.google.com/compute/docs/authentication) to the Compute Engine API.



## Create an API request

The Compute Engine API expects API request bodies to be in JSON format. To make an API request, you can either make a direct HTTP request, by using tools like `curl` or `httplib2`, or you can use one of the [available client libraries](https://docs.cloud.google.com/compute/docs/api/libraries).

When you make a direct HTTP request, you can specify the version with which the server must respond. Specifying an API version is recommended, as it provides increased stability for your application and gives you control over when to adopt new service features.

For API requests that require a request body, like a `POST`, `PUT`, or `PATCH` requests, the request body includes resource properties that you want to set in this request.

### Example API requests

The following `curl` command makes a `POST` request to the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/instances/insert) with the API version `2026-09-01`. The request creates an instance with the project and zone parameters defined in the URL and the instance's properties defined in the request body. The request body is indicated by the `-d` flag. To specify the API version, you can use the `$apiVersion` query parameter or the `X-Goog-Api-Version` header. For more information, see [AIP-184](https://google.aip.dev/184).

###  Version in query parameter 

To specify the API version in the query parameter, include the `%24apiVersion` query parameter with the selected API version.

**Caution:** When using `curl` or other HTTP clients from a command-line shell (for example, Bash or Zsh), the `$` character in `$apiVersion` is interpreted as a shell variable expansion when enclosed in double quotes ("..."). To prevent empty shell variable expansion, it is recommended to URL-encode `$` as `%24` inside double quotes (for example, `"%24apiVersion=2026-09-01"`).
    
    
    curl -X POST -H "Authorization: Bearer [OAUTH_TOKEN]" \
    -H "Content-Type: application/json" \
    "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances**?%24apiVersion=2026-09-01** " -d \
    '{
    "disks":[
      {
        "boot":"true",
        "initializeParams":{
          "sourceImage":"https://www.googleapis.com/compute/v1/projects/debian-cloud/global/images/debian-10-buster-v20210122"
        }
      }
    ],
    "machineType":"https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/machineTypes/e2-standard-2",
    "name":"VM_NAME",
    "networkInterfaces":[
      {
        "accessConfigs":[
          {
            "name":"external-nat",
            "type":"ONE_TO_ONE_NAT"
          }
        ],
        "network":"https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/default"
      }
    ]
    }'

###  Version in header 

To specify the API version in the header, include the `X-Goog-Api-Version` header with the selected API version.
    
    
    curl -X POST -H "Authorization: Bearer [OAUTH_TOKEN]" \
    -H "Content-Type: application/json" \
    **-H "X-Goog-Api-Version: 2026-09-01"** \
    "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances" -d \
    '{
    "disks":[
      {
        "boot":"true",
        "initializeParams":{
          "sourceImage":"https://www.googleapis.com/compute/v1/projects/debian-cloud/global/images/debian-10-buster-v20210122"
        }
      }
    ],
    "machineType":"https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/machineTypes/e2-standard-2",
    "name":"VM_NAME",
    "networkInterfaces":[
      {
        "accessConfigs":[
          {
            "name":"external-nat",
            "type":"ONE_TO_ONE_NAT"
          }
        ],
        "network":"https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/default"
      }
    ]
    }'

The image URI has a different project ID (`debian-cloud`) from your project ID because images belong to different projects, depending on the type of image. For example, all publicly available Debian images offered by Compute Engine are hosted on the `debian-cloud` project.

When referencing another resource, use the fully qualified resource URI. For example, the `network` property uses a fully qualified URI to the `default` network.

### API requests with client libraries

Client libraries provide a simpler way to construct API requests. They support both stable and preview versions of the API. Preview APIs are supported in some languages as pre-release client versions, with suffixes such as `-preview.1` or `-rc.1`.

###  Python 
    
    
    from __future__ import annotations
    
    import re
    import sys
    from typing import Any
    import warnings
    
    from google.api_core.extended_operation import ExtendedOperation
    from google.cloud import compute_v1
    
    
    def get_image_from_family(project: str, family: str) -> compute_v1.Image:
        """
        Retrieve the newest image that is part of a given family in a project.
    
        Args:
            project: project ID or project number of the Cloud project you want to get image from.
            family: name of the image family you want to get image from.
    
        Returns:
            An Image object.
        """
        image_client = compute_v1.ImagesClient()
        # List of public operating system (OS) images: https://cloud.google.com/compute/docs/images/os-details
        newest_image = image_client.get_from_family(project=project, family=family)
        return newest_image
    
    
    def disk_from_image(
        disk_type: str,
        disk_size_gb: int,
        boot: bool,
        source_image: str,
        auto_delete: bool = True,
    ) -> compute_v1.AttachedDisk:
        """
        Create an AttachedDisk object to be used in VM instance creation. Uses an image as the
        source for the new disk.
    
        Args:
             disk_type: the type of disk you want to create. This value uses the following format:
                "zones/{zone}/diskTypes/(pd-standard|pd-ssd|pd-balanced|pd-extreme)".
                For example: "zones/us-west3-b/diskTypes/pd-ssd"
            disk_size_gb: size of the new disk in gigabytes
            boot: boolean flag indicating whether this disk should be used as a boot disk of an instance
            source_image: source image to use when creating this disk. You must have read access to this disk. This can be one
                of the publicly available images or an image from one of your projects.
                This value uses the following format: "projects/{project_name}/global/images/{image_name}"
            auto_delete: boolean flag indicating whether this disk should be deleted with the VM that uses it
    
        Returns:
            AttachedDisk object configured to be created using the specified image.
        """
        boot_disk = compute_v1.AttachedDisk()
        initialize_params = compute_v1.AttachedDiskInitializeParams()
        initialize_params.source_image = source_image
        initialize_params.disk_size_gb = disk_size_gb
        initialize_params.disk_type = disk_type
        boot_disk.initialize_params = initialize_params
        # Remember to set auto_delete to True if you want the disk to be deleted when you delete
        # your VM instance.
        boot_disk.auto_delete = auto_delete
        boot_disk.boot = boot
        return boot_disk
    
    
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
    
    
    def create_instance(
        project_id: str,
        zone: str,
        instance_name: str,
        disks: list[compute_v1.AttachedDisk],
        machine_type: str = "n1-standard-1",
        network_link: str = "global/networks/default",
        subnetwork_link: str = None,
        internal_ip: str = None,
        external_access: bool = False,
        external_ipv4: str = None,
        accelerators: list[compute_v1.AcceleratorConfig] = None,
        preemptible: bool = False,
        spot: bool = False,
        instance_termination_action: str = "STOP",
        custom_hostname: str = None,
        delete_protection: bool = False,
    ) -> compute_v1.Instance:
        """
        Send an instance creation request to the Compute Engine API and wait for it to complete.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            zone: name of the zone to create the instance in. For example: "us-west3-b"
            instance_name: name of the new virtual machine (VM) instance.
            disks: a list of compute_v1.AttachedDisk objects describing the disks
                you want to attach to your new instance.
            machine_type: machine type of the VM being created. This value uses the
                following format: "zones/{zone}/machineTypes/{type_name}".
                For example: "zones/europe-west3-c/machineTypes/f1-micro"
            network_link: name of the network you want the new instance to use.
                For example: "global/networks/default" represents the network
                named "default", which is created automatically for each project.
            subnetwork_link: name of the subnetwork you want the new instance to use.
                This value uses the following format:
                "regions/{region}/subnetworks/{subnetwork_name}"
            internal_ip: internal IP address you want to assign to the new instance.
                By default, a free address from the pool of available internal IP addresses of
                used subnet will be used.
            external_access: boolean flag indicating if the instance should have an external IPv4
                address assigned.
            external_ipv4: external IPv4 address to be assigned to this instance. If you specify
                an external IP address, it must live in the same region as the zone of the instance.
                This setting requires `external_access` to be set to True to work.
            accelerators: a list of AcceleratorConfig objects describing the accelerators that will
                be attached to the new instance.
            preemptible: boolean value indicating if the new instance should be preemptible
                or not. Preemptible VMs have been deprecated and you should now use Spot VMs.
            spot: boolean value indicating if the new instance should be a Spot VM or not.
            instance_termination_action: What action should be taken once a Spot VM is terminated.
                Possible values: "STOP", "DELETE"
            custom_hostname: Custom hostname of the new VM instance.
                Custom hostnames must conform to RFC 1035 requirements for valid hostnames.
            delete_protection: boolean value indicating if the new virtual machine should be
                protected against deletion or not.
        Returns:
            Instance object.
        """
        instance_client = compute_v1.InstancesClient()
    
        # Use the network interface provided in the network_link argument.
        network_interface = compute_v1.NetworkInterface()
        network_interface.network = network_link
        if subnetwork_link:
            network_interface.subnetwork = subnetwork_link
    
        if internal_ip:
            network_interface.network_i_p = internal_ip
    
        if external_access:
            access = compute_v1.AccessConfig()
            access.type_ = compute_v1.AccessConfig.Type.ONE_TO_ONE_NAT.name
            access.name = "External NAT"
            access.network_tier = access.NetworkTier.PREMIUM.name
            if external_ipv4:
                access.nat_i_p = external_ipv4
            network_interface.access_configs = [access]
    
        # Collect information into the Instance object.
        instance = compute_v1.Instance()
        instance.network_interfaces = [network_interface]
        instance.name = instance_name
        instance.disks = disks
        if re.match(r"^zones/[a-z\d\-]+/machineTypes/[a-z\d\-]+$", machine_type):
            instance.machine_type = machine_type
        else:
            instance.machine_type = f"zones/{zone}/machineTypes/{machine_type}"
    
        instance.scheduling = compute_v1.Scheduling()
        if accelerators:
            instance.guest_accelerators = accelerators
            instance.scheduling.on_host_maintenance = (
                compute_v1.Scheduling.OnHostMaintenance.TERMINATE.name
            )
    
        if preemptible:
            # Set the preemptible setting
            warnings.warn(
                "Preemptible VMs are being replaced by Spot VMs.", DeprecationWarning
            )
            instance.scheduling = compute_v1.Scheduling()
            instance.scheduling.preemptible = True
    
        if spot:
            # Set the Spot VM setting
            instance.scheduling.provisioning_model = (
                compute_v1.Scheduling.ProvisioningModel.SPOT.name
            )
            instance.scheduling.instance_termination_action = instance_termination_action
    
        if custom_hostname is not None:
            # Set the custom hostname for the instance
            instance.hostname = custom_hostname
    
        if delete_protection:
            # Set the delete protection bit
            instance.deletion_protection = True
    
        # Prepare the request to insert an instance.
        request = compute_v1.InsertInstanceRequest()
        request.zone = zone
        request.project = project_id
        request.instance_resource = instance
    
        # Wait for the create operation to complete.
        print(f"Creating the {instance_name} instance in {zone}...")
    
        operation = instance_client.insert(request=request)
    
        wait_for_extended_operation(operation, "instance creation")
    
        print(f"Instance {instance_name} created.")
        return instance_client.get(project=project_id, zone=zone, instance=instance_name)
    
    

###  Java 
    
    
    public static Operation startInstance(Compute compute, String instanceName) throws IOException {
      System.out.println("================== Starting New Instance ==================");
    
      // Create VM Instance object with the required properties.
      Instance instance = new Instance();
      instance.setName(instanceName);
      instance.setMachineType(
          String.format(
              "https://www.googleapis.com/compute/v1/projects/%s/zones/%s/machineTypes/e2-standard-1",
              PROJECT_ID, ZONE_NAME));
      // Add Network Interface to be used by VM Instance.
      NetworkInterface ifc = new NetworkInterface();
      ifc.setNetwork(
          String.format(
              "https://www.googleapis.com/compute/v1/projects/%s/global/networks/default",
              PROJECT_ID));
      List<AccessConfig> configs = new ArrayList<>();
      AccessConfig config = new AccessConfig();
      config.setType(NETWORK_INTERFACE_CONFIG);
      config.setName(NETWORK_ACCESS_CONFIG);
      configs.add(config);
      ifc.setAccessConfigs(configs);
      instance.setNetworkInterfaces(Collections.singletonList(ifc));
    
      // Add attached Persistent Disk to be used by VM Instance.
      AttachedDisk disk = new AttachedDisk();
      disk.setBoot(true);
      disk.setAutoDelete(true);
      disk.setType("PERSISTENT");
      AttachedDiskInitializeParams params = new AttachedDiskInitializeParams();
      // Assign the Persistent Disk the same name as the VM Instance.
      params.setDiskName(instanceName);
      // Specify the source operating system machine image to be used by the VM Instance.
      params.setSourceImage(SOURCE_IMAGE_PREFIX + SOURCE_IMAGE_PATH);
      // Specify the disk type as Standard Persistent Disk
      params.setDiskType(
          String.format(
              "https://www.googleapis.com/compute/v1/projects/%s/zones/%s/diskTypes/pd-standard",
              PROJECT_ID, ZONE_NAME));
      disk.setInitializeParams(params);
      instance.setDisks(Collections.singletonList(disk));
    
      // Initialize the service account to be used by the VM Instance and set the API access scopes.
      ServiceAccount account = new ServiceAccount();
      account.setEmail("default");
      List<String> scopes = new ArrayList<>();
      scopes.add("https://www.googleapis.com/auth/devstorage.full_control");
      scopes.add("https://www.googleapis.com/auth/compute");
      account.setScopes(scopes);
      instance.setServiceAccounts(Collections.singletonList(account));
    
      // Optional - Add a startup script to be used by the VM Instance.
      Metadata meta = new Metadata();
      Metadata.Items item = new Metadata.Items();
      item.setKey("startup-script-url");
      // If you put a script called "vm-startup.sh" in this Google Cloud Storage
      // bucket, it will execute on VM startup.  This assumes you've created a
      // bucket named the same as your PROJECT_ID.
      // For info on creating buckets see:
      // https://cloud.google.com/storage/docs/cloud-console#_creatingbuckets
      item.setValue(String.format("gs://%s/vm-startup.sh", PROJECT_ID));
      meta.setItems(Collections.singletonList(item));
      instance.setMetadata(meta);
    
      System.out.println(instance.toPrettyString());
      Compute.Instances.Insert insert = compute.instances().insert(PROJECT_ID, ZONE_NAME, instance);
      return insert.execute();
    }
    

### Creating resource URIs

In Compute Engine API, a reference to another Google Cloud resource is given as a fully qualified URI:
    
    
    https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/RESOURCE_TYPE/SPECIFIC_RESOURCE

Whenever you specify an image, a machine type, a network, or any other resource, you must provide the URI to the resource when using the API. Client tools like the Google Cloud CLI and the Google Cloud console hide this complexity and handle creating these resource URIs for you, but when interacting with the API directly, you must create these resource URIs yourself.

There are slightly different resource URIs for different types of resources. For example, a zonal resource has the `zone` specification in the URI:
    
    
    https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/machineTypes/e2-standard-2

Regional resources replace the `zone` specification with a `region` specification:
    
    
    https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/addresses/ADDRESS_NAME

Similarly, global resources have the `global` specification:
    
    
    https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/images/VM_NAME

The Compute Engine API also accepts partial URIs because the service can infer information like the project ID. So, the following partial versions of the earlier URIs are also acceptable:
    
    
    zones/ZONE/machineTypes/e2-standard-2
    
    
    regions/REGION/addresses/ADDRESS_NAME
    
    
    project/PROJECT_ID/global/images/VM_NAME

In the partial URIs, both the zonal and regional URIs omitted the project ID but the image URI did not. This is because publicly available images offered by Compute Engine are hosted in other projects, like `debian-cloud` for all Debian images and `ubuntu-os-cloud` for all Ubuntu images. Before you can use these images, you need to provide the appropriate project ID. If you omit the project ID for images, Compute Engine attempts to find the image in your project, and the request fails because the image doesn't exist.

However, if you use a [custom image](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images) that belongs to your project (the same project you are creating this resource in), you can omit the project specification when providing an image URI.

### Determining required properties

The Compute Engine API reference documentation, available for IBV APIs and for CBV APIs v1 and beta, describes all of the possible properties you can set for a specific resource. The reference documentation makes a distinction between mutable versus immutable properties (marked by an `[Output Only]` in the property description), but to determine required properties for a resource, you need to review the documentation specific to that task.

For example, if you are creating an instance, read the [Creating an instance from an image](https://docs.cloud.google.com/compute/docs/instances/create-start-instance#startinginstancewithimage) documentation to see the API properties required for the request. If you want to create a static external IP address in the API, read the [Static external IP addresses](https://docs.cloud.google.com/compute/docs/ip-addresses#reservedaddress) documentation.

### Validating API requests

To validate your API requests:

  1. In the Compute Engine API reference, find the method your code is calling. For example, [`v1/compute.instances.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert), or [`2026-09-01/compute.instances.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/instances/insert).

  2. From the contents menu, click **Try it!** This opens the **Try this method** window.

![The Try it! button on the contents menu.](https://docs.cloud.google.com/static/compute/images/try-it-button.png)

  3. Under **Request parameters** , you don't need to provide a **project** or **zone** because validation doesn't require submitting the request.

  4. For IBV methods only, under **X-Goog-Api-Version** , select the API version.

  5. Under **Request body** , paste your request.




Malformed elements of the request are underlined in blue. Click each underlined section for more information about the issue to be addressed.

## Handling API responses

If you make a request that mutates (alters) data, Compute Engine returns an `Operation` object that you can then poll to get the status of the operations for your request. The `Operation` resource looks like this:
    
    
    {
     "kind": "compute#operation",
     "id": "7127550864823803662",
     "name": "operation-1458856416788-52ed27a803e22-1c3bd86a-9e95017b",
     "zone": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE",
     "operationType": "insert",
     "targetLink": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/EXAMPLE_VM",
     "targetId": "4132355614508179214",
     "status": "PENDING",
     "user": "user@example.com",
     "progress": 0,
     "insertTime": "2016-03-24T14:53:37.788-07:00",
     "selfLink": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/operations/operation-1458856416788-52ed27a803e22-1c3bd86a-9e95017b"
    }

If the original request is to mutate (alter) a zonal resource–for example, to snapshot a disk or to stop an instance–Compute Engine returns a [`zoneOperations`](https://docs.cloud.google.com/compute/docs/reference/latest/zoneOperations) object. Similarly, regional and global resources return a [`regionOperations`](https://docs.cloud.google.com/compute/docs/reference/latest/regionOperations) or [`globalOperations`](https://docs.cloud.google.com/compute/docs/reference/latest/globalOperations) object, respectively. You can get the status of an operation by performing a request that uses the `get` or `wait` method for the specific `Operation` resource and providing the `name` of the operation.

Your request is not complete until the `Operation` resource's status returns as `DONE`. This can take some time depending on the nature of your request. Then, after the `Operation` resource's status returns as `DONE`, you can check to see if the operation succeeded and whether there were any errors.

For example, the following response indicates that the preceding operation is now complete, specified by the `DONE` status:
    
    
    endTime: '2016-03-24T14:54:07.119-07:00'
    id: '7127550864823803662'
    insertTime: '2016-03-24T14:53:37.788-07:00'
    kind: compute#operation
    name: operation-1458856416788-52ed27a803e22-1c3bd86a-9e95017b
    operationType: insert
    progress: 100
    selfLink: https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/operations/operation-1458856416788-52ed27a803e22-1c3bd86a-9e95017b
    startTime: '2016-03-24T14:53:38.397-07:00'
    status: DONE
    targetId: '4132355614508179214'
    targetLink: https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/EXAMPLE_VM
    user: user@example.com
    zone: https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE

To confirm, make a `get` request to the resource to check that it exists and is running. For example:
    
    
    GET /compute/v1/projects/PROJECT_ID/zones/ZONE/instances/EXAMPLE_VM
    
    {
      "cpuPlatform": "Intel Haswell",
      "creationTimestamp": "2016-03-24T14:53:37.170-07:00",
      "disks": [
        ..[snip]..
      ],
      "selfLink": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/EXAMPLE_VM",
      "status": "RUNNING",
      "tags": {
        "fingerprint": "42WmSpB8rSM="
      },
      "zone": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE"
    }

### Polling operations

You can write some code to periodically poll the operation with a `get` or `wait` request that returns when the operation status is `DONE`.

With a `get` request, the operation is returned immediately, regardless of the status of the operation. You need to poll the operation periodically to know when the operation is done.

If you make a `wait` request, the request returns when the operation is `DONE` or if the request is approaching the 2 minute deadline. You can choose to use `wait` or `get` to poll your operations, but the `wait` method provides certain benefits over the `get` method:

  * You can set up your clients to poll for the operation status less frequently, reducing your QPS usage of the Compute Engine API.
  * The average latency between when the operation is done and when the client is informed that the operation is done is significantly reduced because the server responds as soon as the operation is done.
  * The method provides bounded waits. The method waits for no more than the default HTTP timeout (2 minutes) and then returns the current state of the operation, which might be `DONE` or still in progress.



The `wait` method is a _best-effort_ API. If the server is overloaded, the request might return before it reaches the default deadline, or after waiting just zero seconds. The method is also not guaranteed to return only when the operation is `DONE`. For example, if the request approaches the 2 minute deadline, the method returns even if the operation is not done. To check on your operations, we recommend that you use either the `wait` or `get` method—in a retry loop with sleep in-between—to periodically poll the operation status. The maximum retry interval shouldn't exceed the [minimum operation retention period](https://docs.cloud.google.com/compute/docs/instances/viewing-compute-operations#operation-retention-period).

### Example polling

The following examples use the `get` method. You can replace the `get` method with the `wait` method:

###  Python 
    
    
    import time
    
    from google.cloud import [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest)
    
    
    def wait_for_operation(
        operation: [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[Operation](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.Operation.html), project_id: str
    ) -> compute_v1.Operation:
        """
        This method waits for an operation to be completed. Calling this function
        will block until the operation is finished.
    
        Args:
            operation: The Operation object representing the operation you want to
                wait on.
            project_id: project ID or project number of the Cloud project you want to use.
    
        Returns:
            Finished Operation object.
        """
        kwargs = {"project": project_id, "operation": operation.name}
        if operation.zone:
            client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[ZoneOperationsClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.zone_operations.ZoneOperationsClient.html)()
            # Operation.zone is a full URL address of a zone, so we need to extract just the name
            kwargs["zone"] = operation.zone.rsplit("/", maxsplit=1)[1]
        elif operation.region:
            client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[RegionOperationsClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.region_operations.RegionOperationsClient.html)()
            # Operation.region is a full URL address of a region, so we need to extract just the name
            kwargs["region"] = operation.region.rsplit("/", maxsplit=1)[1]
        else:
            client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[GlobalOperationsClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.global_operations.GlobalOperationsClient.html)()
    
        while True:
            result = client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.global_operations.GlobalOperationsClient.html#google_cloud_compute_v1_services_global_operations_GlobalOperationsClient_get)(**kwargs)
    
            if result.status == [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[Operation](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.Operation.html).Status.DONE:
                print("Operation finished.")
                if result.error:
                    print(f"Error during operation: {result.error}")
                return result
    
            print("Waiting for operation to complete...")
            time.sleep(2)
    
    

###  Java 
    
    
    /**
     * Wait until {@code operation} is completed.
     *
     * @param compute the {@code Compute} object
     * @param operation the operation returned by the original request
     * @param timeout the timeout, in millis
     * @return the error, if any, else {@code null} if there was no error
     * @throws InterruptedException if we timed out waiting for the operation to complete
     * @throws IOException if we had trouble connecting
     */
    public static Operation.Error blockUntilComplete(
        Compute compute, Operation operation, long timeout) throws Exception {
      long start = System.currentTimeMillis();
      final long pollInterval = 5 * 1000;
      String zone = getLastWordFromUrl(operation.getZone()); // null for global/regional operations
      String region = getLastWordFromUrl(operation.getRegion());
      String status = operation.getStatus();
      String opId = operation.getName();
      while (operation != null && !status.equals("DONE")) {
        Thread.sleep(pollInterval);
        long elapsed = System.currentTimeMillis() - start;
        if (elapsed >= timeout) {
          throw new InterruptedException("Timed out waiting for operation to complete");
        }
        System.out.println("waiting...");
        if (zone != null) {
          Compute.ZoneOperations.Get get = compute.zoneOperations().get(PROJECT_ID, zone, opId);
          operation = get.execute();
        } else if (region != null) {
          Compute.RegionOperations.Get get = compute.regionOperations().get(PROJECT_ID, region, opId);
          operation = get.execute();
        } else {
          Compute.GlobalOperations.Get get = compute.globalOperations().get(PROJECT_ID, opId);
          operation = get.execute();
        }
        if (operation != null) {
          status = operation.getStatus();
        }
      }
      return operation == null ? null : operation.getError();
    }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
