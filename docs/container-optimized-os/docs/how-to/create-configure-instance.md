---
url: https://docs.cloud.google.com/container-optimized-os/docs/how-to/create-configure-instance/
title: Creating and configuring instances \u00a0|\u00a0 Container-Optimized OS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:19.101041+00:00
---

# Creating and configuring instances  |  Container-Optimized OS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/container-optimized-os/docs/how-to/create-configure-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Container-Optimized OS ](https://docs.cloud.google.com/container-optimized-os/docs)
  * [ Guides ](https://docs.cloud.google.com/container-optimized-os/docs/how-to/create-configure-instance)



Send feedback 

#  Creating and configuring instances Stay organized with collections  Save and categorize content based on your preferences. 

There are two ways to create and configure Compute Engine instances running Container-Optimized OS from Google.

For simple scenarios where you want to run a single container on a VM or on each VM in a [managed instance group](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups), you can specify a container image and optional configuration parameters when you define the instance or instance template. Compute Engine creates the instance with the latest version of Container-Optimized OS and launches the specified container when the VM starts.

**Caution:** The container startup agent (konlet) that deploys containers on VMs during VM creation is deprecated. Use the `docker run` commands in a startup script or use the `cloud-init` tool to configure and to run containers on your VMs and MIGs. For more information, see [Migrate containers that were deployed on VMs during VM creation](https://docs.cloud.google.com/compute/docs/containers/migrate-containers). 

For advanced scenarios where you can deploy multiple containers and configure Docker options using `cloud-init`, you can create a Compute Engine instance with your choice of Container-Optimized OS image, and then proceed to configure the container as needed.

## Creating a simple instance

Use this method to deploy a single container on a VM using the latest version of Container-Optimized OS. You can perform this task using the Google Cloud console or gcloud CLI.

###  Console 

**Note:** The **Deploy container** option in the Google Cloud console is deprecated. Use the equivalent `docker run` command to configure and to run the container. 

  1. Go to the VM instances page.

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

  2. Click **Create instance**.

  3. Specify a **Name** for your instance.

  4. In the **Container** section, select the **Deploy a container image to this VM instance** checkbox.

  5. Specify the **Container image** to use.

     * You can specify an image from Container Registry or Artifact Registry. For example: 
       * `gcr.io/cloud-marketplace/google/nginx1:1.15` selects an NGINX 1.15 container image from Google Cloud Marketplace.
       * `us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0` selects a sample `hello-app` image from Artifact Registry.
     * If you use a container image from Docker Hub, always specify the full Docker image name. For example, specify the following image name to deploy an Apache container image: `docker.io/httpd:2.4`.
  6. Optionally, click **Advanced container options**. For more information, see [Configuring Options to Run Your Container](https://docs.cloud.google.com/compute/docs/containers/configuring-options-to-run-containers).

  7. Click **Create** to create the instance, boot the instance, and launch the container.




###  gcloud 

**Note:** The `create-with-container` gcloud CLI command is deprecated. Use the equivalent `docker run` command to configure and to run the container. 

To create a basic VM instance, run the following command:
    
    
    gcloud compute instances create-with-container instance-name \
        --container-image image-name
    

Replace the following:

  * instance-name: the name for the new instance.
  * image-name: the name of the container image.



For example, the following command creates a new VM instance named `nginx-vm`, which will launch and run the `gcr.io/cloud-marketplace/google/nginx1:1.15` container image:
    
    
    gcloud compute instances create-with-container nginx-vm \
        --container-image gcr.io/cloud-marketplace/google/nginx1:1.15
    

Similarly, you can create a new VM instance named `hello-app` which will launch and run a sample container in Artifact Registry:
    
    
    gcloud compute instances create-with-container hello-app \
    --container-image us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0
    

When using a container image from Docker Hub, you must always specify a full Docker image name. For example, specify the following image name to deploy an Apache container image:
    
    
    docker.io/httpd:2.4
    

To run a single container on each VM in a managed instance group, specify the container image name when defining the instance template. See [Creating an instance template with a container image](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates#with-container) for more information.

## Creating an instance for advanced scenarios

Use this method to select a specific Container-Optimized OS image, to deploy multiple containers, and to use `cloud-init` for advanced configuration.

### Viewing available images

Container-Optimized OS images are available on Google Cloud console's [list of images](https://console.cloud.google.com/compute/images) with the prefix `cos`. These are hosted under the `cos-cloud` project. You can also see all currently available releases on command line by running the following command:
    
    
    gcloud compute images list --project cos-cloud --no-standard-images
    

The output is similar to the following:
    
    
    NAME                       PROJECT    FAMILY      DEPRECATED  STATUS
    cos-69-10895-385-0         cos-cloud  cos-69-lts              READY
    cos-73-11647-534-0         cos-cloud  cos-73-lts              READY
    cos-77-12371-251-0         cos-cloud  cos-77-lts              READY
    cos-81-12871-103-0         cos-cloud  cos-81-lts              READY
    cos-beta-81-12871-44-0     cos-cloud  cos-beta                READY
    cos-dev-84-13078-0-0       cos-cloud  cos-dev                 READY
    cos-stable-81-12871-103-0  cos-cloud  cos-stable              READY
    

**Note:** The most current Container-Optimized OS images are now available under the project `cos-cloud`, and use the name prefix of `cos`. These images are identical to the previous versions of Container-Optimized OS, which used the name prefix `gci` and were accessible through the `google-containers` project. The `gci` images in the `google-containers` project **are considered deprecated**.  
Newer versions of Container-Optimized OS images are now being pushed only to the `cos-cloud` project; please update your development or production workflow to use the `cos` images in `cos-cloud` to get the latest releases.

### Creating an instance

You can create an instance using the Google Cloud console, gcloud CLI, or the API.

###  Console 

**Note:** The **Deploy container** option in the Google Cloud console is deprecated. Use the equivalent `docker run` command to configure and to run the container. 

To run a Compute Engine instance with a Container-Optimized OS and Docker installed, do the following:

  1. Open the Compute Engine instance creation page on Google Cloud console.

[Create a new Compute Engine instance](https://console.cloud.google.com/compute/instancesAdd)

  2. Specify a **Name** for your instance.

  3. In the **Containers** section, clear the **Deploy a container image to this VM instance** checkbox. This option is useful if you want to deploy a single container on the VM.

  4. In the **Boot disk** section, select a Container-Optimized OS image.

  5. Click **Create** to create and boot the instance.




###  gcloud 

**Note:** The `create-with-container` gcloud CLI command is deprecated. Use the equivalent `docker run` command to configure and to run the container. 

Review the available images, then use the following command to create a `cos` node image instance:
    
    
    gcloud compute instances create instance-name \
        --image image-name \
        --image-project cos-cloud \
        --zone compute-zone \
        --machine-type machine-type-name
    

Replace the following:

  * instance-name: the name of your VM instance.
  * image-name: the name of the Container-Optimized OS image for the instance, obtained from the list of available images. From our previous example, we can use `cos-beta-81-12871-44-0`.
  * compute-zone: the [compute zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) for your instance.
  * machine-type-name: the machine type to use for this new instance. The default type is `n1-standard-1`.



For example, the following command creates an instanced named `cos-test` using the `cos-beta-67-10575-13-0` image:
    
    
    gcloud compute instances create cos-test \
        --image cos-beta-67-10575-13-0 \
        --image-project cos-cloud \
        --zone us-east1-d \
        --machine-type n1-standard-1
    

You can add the `--preemptible` flag for one-off, experimental instances.

###  API 

In the API, construct a normal request to [create an instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance#startinginstancewithimage), but include a Container-Optimized OS source [image](https://docs.cloud.google.com/compute/docs/images). For example:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/project-id/zones/compute-zone/instances
    
    {
      'machineType': 'zones/compute-zone/machineTypes/machine-type-name',
      'name': 'instance-name',
      'networkInterfaces': [
        {
          'accessConfigs': [
            {
              'type': 'ONE_TO_ONE_NAT',
              'name': 'External NAT'
            }
          ],
          'network': 'global/networks/default'
        }
      ],
      'disks': [
        {
          'type': 'PERSISTENT',
          'boot': true,
          'autoDelete': true,
          'initializeParams': {
            'sourceImage': 'projects/cos-cloud/global/images/image-name'
          }
        }
      ]
    }
    

### Configuring an instance

In some cases, you might want to do additional configuration when the instance boots. You can use the `cloud-init` tool with Container-Optimized OS to apply configuration information that you supply in a [`cloud-config` format](http://cloudinit.readthedocs.io/en/latest/topics/examples.html).

### Using cloud-init with the Cloud config format

Container-Optimized OS images include [`cloud-init`](https://cloudinit.readthedocs.org/en/latest/index.html) as a way to configure your instance when it boots up. The `cloud-init` tool expects its configuration in the value of the `user-data` key of the [instance metadata](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata). The `cloud-init` tool understands [multiple formats](https://cloudinit.readthedocs.org/en/latest/topics/format.html).

Here's an example `cloud-init` file showing how to create a user account and create a systemd service owned by this user that controls the management of a Docker busybox container:
    
    
    #cloud-config
    
    users:
    - name: cloudservice
      uid: 2000
    
    write_files:
    - path: /etc/systemd/system/cloudservice.service
      permissions: 0644
      owner: root
      content: |
        [Unit]
        Description=Start a simple docker container
    
        [Service]
        ExecStart=/usr/bin/docker run --rm -u 2000 --name=mycloudservice busybox:latest /bin/sleep 3600
        ExecStop=/usr/bin/docker stop mycloudservice
        ExecStopPost=/usr/bin/docker rm mycloudservice
    
    runcmd:
    - systemctl daemon-reload
    - systemctl start cloudservice.service
    
    # Optional once-per-boot setup. For example: mounting a PD.
    bootcmd:
    - fsck.ext4 -tvy /dev/[DEVICE_ID]
    - mkdir -p /mnt/disks/[MNT_DIR]
    - mount -t ext4 -O ... /dev/[DEVICE_ID] /mnt/disks/[MNT_DIR]
    

**Note:** Using `systemctl enable` in the `runcmd` section of cloud-init will not work as intended. This is because /etc on Container-Optimized OS is stateless, so commands such as `systemctl enable/disable`, that modify /etc, won't persist across reboots. See [Disks and Filesystem](https://docs.cloud.google.com/container-optimized-os/docs/concepts/disks-and-filesystem) for more information on Container-Optimized OS's filesystem. An alternative to `systemctl enable` is to use `systemctl start`, as in the example above. cloud-init modules such as `write_files` and `runcmd`, which are typically run once-per-instance on other distros, are run on every boot on Container-Optimized OS.**Note:** The `uid` option in the `users` section is a `cos` node image extension. This option will not work with other versions of cloud-init. This option explicitly sets the ID for the user and allows you to make sure the ID is consistent between different instances. It's recommended that you always set this option. Choose an ID from the [2000, 4999] range to avoid collision with other user accounts.

To create a Container-Optimized OS VM instance that references this `cloud-init` file, use the `--metadata-from-file` command line flag. Assuming the `cloud-init` file is called filename in the current directory, the following command creates a Container-Optimized OS instance and trigger `cloud-init` by assigning the contents of the file to the `user-data` key in the Instance Metadata:
    
    
    gcloud compute instances create instance-name \
        --image image-name \
        --image-project cos-cloud \
        **--metadata-from-file user-data= filename**
    

Replace the following:

  * instance-name: the name of your VM instance.
  * image-name: the name of the Container-Optimized OS image for the instance. For example, `--image=cos-113-18244-85-29`.
  * filename: the name of the metadata file.



It is possible to set other metadata flags when creating Container-Optimized OS instances. Because these properties are simple key-value pairs, you may use the `--metadata` flag in the `gcloud compute instances create` command to create the properties. Also, starting from [milestone 97](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m97), you can set [metadata flags](https://docs.cloud.google.com/compute/docs/metadata/overview) in project metadata using the `--metadata` flag in the [`gcloud compute project-info add-metadata`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/project-info/add-metadata#--metadata) command. Flags defined at the instance level will take precedence over flags defined at the project level.

The previous example can be expanded to collect usage statistics and crash dump collection with the following command:
    
    
    gcloud compute instances create instance-name \
        --image image-name \
        --image-project cos-cloud \
        **--metadata-from-file user-data= filename** \
        --metadata=cos-metrics-enabled=true
    

#### Other metadata flags

Metadata Key | Description | Default Behavior  
---|---|---  
`cos-update-strategy` | Specifies automatic update behavior. Value could be `update_enabled`, `update_disabled`, or unset.  
If unset, the default auto-update behavior for the milestone will be used.  
If enabled, the behavior depends on the release channel:

  * cos-dev and cos-beta: Updates from latest OS version in the corresponding image family
  * LTS milestone and cos-stable: Updates from latest OS version from the same milestone

| 

  * Milestones < 117: Enabled by default
  * Milestones >= 117: Disabled by default

  
`cos-metrics-enabled` | Enables crash dump collection. Values could be:  
`true`  
`false` (default). | Disabled by default  
**Caution:** Enabling the `cos-metrics-enabled` setting permits collection of some crash reports that help Google improve the `cos` node image. Crash reports contain a snippet of the most recent portion of the kernel log buffer at the time of the crash, and may contain user or personal information, depending on what was happening at the time of the crash. The information is sent to Google directly and is not shared outside of Google.

## Connecting to an instance

You can SSH into your VM instance running the `cos` node image the [same way](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance) you SSH into other Compute Engine instances.

For example:
    
    
    gcloud compute ssh instance-name \
        --project project-id \
        --zone compute-zone
    

## Running startup scripts

You can specify a [startup script](https://docs.cloud.google.com/compute/docs/startupscript) through the metadata server, using the `startup-script` metadata key. You can use the Google Cloud CLI, the API, or Google Cloud console to provide a startup script. Refer to [Running Startup Scripts](https://docs.cloud.google.com/compute/docs/startupscript) for details.

## Time synchronization

Before [milestone 85](https://docs.cloud.google.com/container-optimized-os/docs/release-notes#release_schedule), Container-Optimized OS uses `systemd`'s `systemd-timesyncd` service to synchronize the local system clock with a remote Network Time Protocol (NTP) server via the SNTP protocol. The following entries in `/etc/systemd/timesyncd.conf` configuration file show commented out default configuration values to help the administrator make any desired changes:
    
    
    cat /etc/systemd/timesyncd.conf
    # comments omitted for brevity
    [Time]
    #NTP=
    #FallbackNTP=metadata.google.internal
    #RootDistanceMaxSec=5
    #PollIntervalMinSec=32
    #PollIntervalMaxSec=2048
    

So the maximum acceptable root distance is 5 seconds and the minimum and maximum poll intervals for NTP messages are 32 and 2048 seconds respectively.

Starting from milestone 85, Container-Optimized OS uses `chronyd` service to synchronize the local system clock with a remote Network Time Protocol (NTP) server via the NTP protocol. The following entries in the `/etc/chrony/chrony.conf` configuration file show commented out default configuration values to help the administrator make any desired changes:
    
    
    cat /etc/chrony/chrony.conf
    # Use custom NTP servers
    server metadata.google.internal prefer iburst
    
    # Record the rate at which the system clock gains/losses time.
    driftfile /var/lib/chrony/drift
    
    # Allow the system clock to be stepped in the first three updates
    # if its offset is larger than 1 second.
    makestep 1.0 3
    
    # Enable kernel synchronization of the real-time clock (RTC).
    rtcsync
    

The NTP server is set from `eth0`'s DHCP response, which is usually the Compute Engine's metadata server:
    
    
    networkctl status eth0 | grep NTP
                 NTP: 169.254.169.254
    

## Changing the time zone

The default time zone of Container-Optimized OS from Google is UTC0. Create a symbolic link to your desired time zone as in the following example:
    
    
    sudo rm /etc/localtime
    sudo ln -s /usr/share/zoneinfo/US/Pacific /etc/localtime
    

Note that `/etc` is stateless, so the time zone will be reset to the default (UTC0) every reboot.

## Enabling or disabling automatic updates

There are two ways to enable or disable automatic updates. The preferred method is to set the `cos-update-strategy` instance metadata key to `update_enabled` or `update_disabled`, respectively. For example:
    
    
    gcloud compute instances create instance-name \
        --image image-name \
        --image-project cos-cloud \
        **--metadata cos-update-strategy=update_disabled**
    

Starting from [milestone 97](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m97), you can also disable or enable automatic updates in project metadata:
    
    
    gcloud compute project-info add-metadata \
        **--metadata cos-update-strategy=update_disabled**
    

**Note:** Metadata flags defined at instance level takes precedence over metadata flags defined at project level.

You can also disable automatic updates on a running instance with `systemctl`:
    
    
    sudo systemctl stop update-engine
    sudo systemctl mask update-engine
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
