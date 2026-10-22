---
url: https://docs.cloud.google.com/compute/docs/containers/configuring-options-to-run-containers/
title: Configuring options to run your container \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:39:14.094745+00:00
---

# Configuring options to run your container  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/containers/configuring-options-to-run-containers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Configuring options to run your container Stay organized with collections  Save and categorize content based on your preferences. 

You can run a single container on a VM or on each VM in a managed instance group (MIG). To do this, specify a container image and configuration parameters when you create a VM instance or an instance template.

This document describes the configuration options for running containers on Compute Engine instances.

**Caution:** The container startup agent (konlet) that deploys containers on VMs during VM creation is deprecated. Use the `docker run` commands in a startup script or use the `cloud-init` tool to configure and to run containers on your VMs and MIGs. For more information, see [Migrate containers that were deployed on VMs during VM creation](https://docs.cloud.google.com/compute/docs/containers/migrate-containers). 

## Before you begin

  * If you aren't familiar with containers, read [Containers on Compute Engine](https://docs.cloud.google.com/containers).
  * If you aren't familiar with Docker, read the [Docker documentation](https://docs.docker.com/).
  * Read about [Deploying containers on Compute Engine](https://docs.cloud.google.com/compute/docs/containers/deploying-containers).
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




When you create an instance or an instance template to use for [Deploying containers on VMs and MIGs](https://docs.cloud.google.com/compute/docs/containers/deploying-containers), specify the container configuration using the Google Cloud console or the Google Cloud CLI.

The following sections describe how to configure containers on VM instances, but you can configure the following options when creating an instance template as well. Use the Google Cloud console or the Google Cloud CLI to configure options for VM instances in an instance template.

You can use the `docker run` commands to configure a container on a VM instance that is running Container-Optimized OS or specify the `docker run` command in a startup script to create and configure a VM. For more information, see [Use startup scripts to deploy containers on VMs](https://docs.cloud.google.com/compute/docs/containers/migrate-containers#startup-scripts).

## Specifying a restart policy

You can set a restart policy to specify whether to restart a container on exit. The default policy is to always restart. You can also set the policy to restart on failure or to never restart.

###  docker run 

Use the `--restart` flag of the `docker run` command. Repeated attempts to restart a container are driven by the default Docker behavior, as specified in the Docker [`--restart`](https://docs.docker.com/engine/containers/start-containers-automatically/) reference.

###  Console 

**Note:** The **Deploy container** option in the Google Cloud console is deprecated. Use the equivalent `docker run` command to configure and to run the container. 

  1. Go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. In the **Container** section, click **Deploy container**.

  3. On the **Configure container** page, do the following:

     1. Specify a container image name.
     2. In the **Restart policy** section, select the restart policy for the container.
     3. To confirm the container details, click **Select**.
  4. Continue with the VM creation process.




###  gcloud 

**Note:** The `create-with-container` gcloud CLI command is deprecated. Use the equivalent `docker run` command to configure and to run the container. 

Use the `--container-restart-policy` flag to specify container a restart policy:

  * `always` (default)
  * `on-failure`
  * `never`



The following example launches a container with `on-failure` restart policy, which means the restart only happens when the container exit code is nonzero:
    
    
    gcloud compute instances create-with-container busybox-vm \
      --container-image docker.io/busybox:1.27 \
      --container-restart-policy on-failure
    

Use the `gcloud compute instances update-container` command with the `--container-restart-policy` flag for the restart policy on a container running on a VM.

## Running a container in privileged mode

You can run a container in privileged mode to allow access to all devices on the host. Containers are run as "unprivileged" by default and aren't allowed to access any devices.

###  docker run 

Use the `--privileged` flag of the `docker run` command. For more information, see [Runtime privilege and Linux capabilities](https://docs.docker.com/engine/reference/run#runtime-privilege-and-linux-capabilities).

###  Console 

**Note:** The **Deploy container** option in the Google Cloud console is deprecated. Use the equivalent `docker run` command to configure and to run the container. 

  1. Go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. In the **Container** section, click **Deploy container**.

  3. On the **Configure container** page, do the following:

     1. Specify a container image name.
     2. Select **Run as privileged**.
     3. To confirm the container details, click **Select**.
  4. Continue with the VM creation process.




###  gcloud 

**Note:** The `create-with-container` gcloud CLI command is deprecated. Use the equivalent `docker run` command to configure and to run the container. 

Use the `--container-privileged` flag to run a container with runtime privilege. The following example launches a busybox container in privileged mode:
    
    
    gcloud compute instances create-with-container busybox-vm \
      --container-image docker.io/busybox:1.27 \
      --container-privileged
    

Use the `gcloud compute instances update-container` command with the `--container-privileged` flag to update a container on a VM. Use the `--no-container-privileged` flag to turn off privileged mode.

## Allocating a buffer for STDIN in the container runtime

You can allocate a buffer for `STDIN` in the container runtime to keep the `STDIN` stream open in a container. If this is not set, reads from `STDIN` in the container always result in `EOF`.

Along with allocating a pseudo-TTY, keeping the `STDIN` stream open is necessary for establishing an interactive shell in the container and for the container to receive its standard input from a pipe.

###  docker run 

Use the `--interactive` (`-i`) flag of the `docker run` command. For more information, see the documentation for [`--interactive`](https://docs.docker.com/engine/reference/run/#foreground) flag.

###  Console 

**Note:** The **Deploy container** option in the Google Cloud console is deprecated. Use the equivalent `docker run` command to configure and to run the container. 

  1. Go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. In the **Container** section, click **Deploy container**.

  3. On the **Configure container** page, do the following:

     1. Specify a container image name.
     2. Select **Allocate a buffer for STDIN**.
     3. To confirm the container details, click **Select**.
  4. Continue with the VM creation process.




###  gcloud 

**Note:** The `create-with-container` gcloud CLI command is deprecated. Use the equivalent `docker run` command to configure and to run the container. 

Use `--container-stdin` flag to allocate a buffer for `STDIN` in the container runtime. The following example starts a container and keeps its `STDIN` open:
    
    
    gcloud compute instances create-with-container busybox-vm \
      --container-image docker.io/busybox:1.27 \
      --container-stdin
    

Use `gcloud compute instances update-container` command with the `--container-stdin` flag to update a container on a VM. Use the `--no-container-stdin` flag to turn off allocation of a buffer for `STDIN`.

## Allocating a pseudo-TTY

Allocating a pseudo-TTY for a container is necessary for establishing an interactive shell in the container (along with allocating a buffer for STDIN).

###  docker run 

Use the `--tty (-t)` flag of the `docker run` command. For more information, see the [`--tty`](https://docs.docker.com/engine/reference/commandline/run/#assign-name-and-allocate-pseudo-tty-name--it) flag.

###  Console 

**Note:** The **Deploy container** option in the Google Cloud console is deprecated. Use the equivalent `docker run` command to configure and to run the container. 

  1. Go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. In the **Container** section, click **Deploy container**.

  3. On the **Configure container** page, do the following:

     1. Specify a container image name.
     2. Select **Allocate a pseudo-TTY**.
     3. To confirm the container details, click **Select**.
  4. Continue with the VM creation process.




###  gcloud 

**Note:** The `create-with-container` gcloud CLI command is deprecated. Use the equivalent `docker run` command to configure and to run the container. 

Use the `--container-tty` flag to allocate a pseudo-TTY. The following example starts a container and allocates a pseudo-TTY:
    
    
    gcloud compute instances create-with-container busybox-vm \
      --container-image docker.io/busybox:1.27 \
      --container-stdin \
      --container-tty
    

Use the `gcloud compute instances update-container` command with the `--container-tty` flag to update a container on a VM. Use the `--no-container-tty` flag to not allocate a pseudo-TTY.

## Overriding the default command to execute on container startup

The `ENTRYPOINT` of a container image specifies what executable to run when the container starts and lets you run the container as if it were that binary.

You can override the `ENTRYPOINT` command of the container image.

###  docker run 

Use the `--entrypoint` flag (command only, no arguments) of the `docker run` command. Learn about [`ENTRYPOINT`](https://docs.docker.com/engine/reference/builder#entrypoint) and the [`--entrypoint`](https://docs.docker.com/engine/reference/run#entrypoint-default-command-to-execute-at-runtime) flag.

###  Console 

**Note:** The **Deploy container** option in the Google Cloud console is deprecated. Use the equivalent `docker run` command to configure and to run the container. 

  1. Go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. In the **Container** section, click **Deploy container**.

  3. On the **Configure container** page, do the following:

     1. Specify a container image name.
     2. In the **Command** field, enter a single executable command without parameters—for example, `uptime`.
     3. To confirm the container details, click **Select**.
  4. Continue with the VM creation process.




###  gcloud 

**Note:** The `create-with-container` gcloud CLI command is deprecated. Use the equivalent `docker run` command to configure and to run the container. 

Use the `--container-command` flag to override the container image `ENTRYPOINT`. The following example runs the `uptime` command in a busybox container to display the time since the last boot:
    
    
    gcloud compute instances create-with-container busybox-vm \
      --container-image docker.io/busybox:1.27 \
      --container-command "uptime"
    

Use the `gcloud compute instances update-container` command with the `--container-command` flag to update a command for a container on a VM.

Use the `--clear-container-command` flag with the `update-container` command to clear the default command for the updated container.

## Passing arguments to container ENTRYPOINT command

You can pass (append) arguments to the container [`ENTRYPOINT`](https://docs.docker.com/engine/reference/builder/#entrypoint) command or override the default container [`CMD`](https://docs.docker.com/engine/reference/run#cmd-default-command-or-options) command.

**Note:** This is similar to passing arguments to an entrypoint in the `[ARG...]` section of the `docker run [OPTIONS] IMAGE [COMMAND] [ARG...]` command. Learn about [`ENTRYPOINT`](https://docs.docker.com/engine/reference/builder#entrypoint) and the [`--entrypoint`](https://docs.docker.com/engine/reference/run#entrypoint-default-command-to-execute-at-runtime) flag.

###  Console 

**Note:** The **Deploy container** option in the Google Cloud console is deprecated. Use the equivalent `docker run` command to configure and to run the container. 

  1. Go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. In the **Container** section, click **Deploy container**.

  3. On the **Configure container** page, do the following:

     1. Specify a container image name.
     2. In the **Arguments** section, click **Add argument**.
     3. Enter one command argument for each box.
     4. To confirm the container details, click **Select**.
  4. Continue with the VM creation process.




###  gcloud 

**Note:** The `create-with-container` gcloud CLI command is deprecated. Use the equivalent `docker run` command to configure and to run the container. 

Use the `--container-arg` flag to pass arguments to a container image `ENTRYPOINT` command. Use a separate flag for each argument.

The following example runs the `/bin/ash` command with the `-c 'ls -l'` arguments in a container that has been set up to automatically run busybox:
    
    
    gcloud compute instances create-with-container busybox-vm \
      --container-image docker.io/busybox:1.27 \
      --container-command "/bin/ash" \
      --container-arg="-c" \
      --container-arg="ls -l"
    

**Note:** Make sure to use the equals sign (`=`) with the `--container-arg` flag to ensure proper argument parsing. For example: `--container-arg=ARG`.

Use the `gcloud compute instances update-container` command with the `--container-arg` flags to update command arguments for a container running on a VM. The update replaces the entire argument list with the new list.

Use the `--clear-container-args` flag with the `update-container` command to remove all arguments from container declaration.

## Configuring log driver options

If you need to configure log driver options, you can create a VM [startup script](https://docs.cloud.google.com/compute/docs/instances/startup-scripts) to update your Docker configuration file with the logging options that you need. These options apply to all containers that run on the VM and that do not specify log driver options.

For example, the following startup script sets several options–including an option to limit the container's log size–then restarts Docker on the VM:
    
    
    cat <<EOF > /etc/docker/daemon.json
    {
      "live-restore": true,
      "storage-driver": "overlay2",
      "log-opts": {
        "max-size": "10m"
      }
    }
    EOF
    systemctl restart docker
    

## Setting environment variables

You can set environment variables in a container. Only the last value of `KEY` is taken when the `KEY` is repeated more than once.

###  docker run 

Use the `--env` flag of the `docker run` command. Learn how Docker engine enables [setting environment variables](https://docs.docker.com/engine/reference/commandline/run/#set-environment-variables--e-env-env-file).

###  Console 

**Note:** The **Deploy container** option in the Google Cloud console is deprecated. Use the equivalent `docker run` command to configure and to run the container. 

  1. Go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. In the **Container** section, click **Deploy container**.

  3. On the **Configure container** page, do the following:

     1. Specify a container image name.
     2. In the **Environment variables** section, click **Add variable**.
     3. Add or remove environment variables as necessary, one for each line.
     4. To confirm the container details, click **Select**.
  4. Continue with the VM creation process.




###  gcloud 

**Note:** The `create-with-container` gcloud CLI command is deprecated. Use the equivalent `docker run` command to configure and to run the container. 

Use the `--container-env` flag to set environment variables in a container. The following example sets three environment variables: `HOME`, `MODE`, and `OWNER`:
    
    
    gcloud compute instances create-with-container busybox-vm \
      --container-image docker.io/busybox:1.27 \
      --container-env HOME=/home,MODE=test,OWNER=admin
    

Use the `--container-env-file` flag to set environment variables from a local file. The following example sets the two environment variables from the `env.txt` file:
    
    
    gcloud compute instances create-with-container busybox-vm \
      --container-image docker.io/busybox:1.27 \
      --container-env-file ./env.txt
    

The contents of the `env.txt` file are:
    
    
    # this is a comment
    HOME=/home
    MODE=test
    OWNER=admin
    

Use the `gcloud compute instances update-container` command with the `--container-env` or `--container-env-file` flag to update environment variables for a container on a VM. This updates any variables present in the VM instance's container declaration. Variables that are not in the container declaration are added.

Use the `--remove-container-env` flag to remove environment variables when updating a container on a VM. The following example removes the environment variables called `MODE` and `OWNER`:
    
    
    gcloud compute instances update-container busybox-vm \
      --remove-container-env MODE,OWNER
    

If a specified environment variable does not exist, it is silently ignored.

## Mounting a host directory as a data volume

You can mount a directory from a host VM into a container.

###  docker run 

Use the `--volume` flag and the `--mount` flag with mount `type=bind` of the `docker run` command. Learn how the Docker engine [mounts a host directory](https://docs.docker.com/engine/tutorials/dockervolumes#mount-a-host-directory-as-a-data-volume) as a data volume.

###  Console 

**Note:** The **Deploy container** option in the Google Cloud console is deprecated. Use the equivalent `docker run` command to configure and to run the container. 

  1. Go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. In the **Container** section, click **Deploy container**.

  3. On the **Configure container** page, do the following:

     1. Specify a container image name.
     2. In the **Volume mounts** section, click **Add volume**.
     3. From the **Volume type** list, select **Directory** , and do the following:

        * In the **Mount path** field, specify a mount path in a container directory structure at which to mount a host directory.
        * In the **Host path** field, specify a host path to the host directory to mount.
        * In the **Mode** list, specify whether to mount the directory in read/write or read-only mode.
     4. To confirm the container details, click **Select**.

  4. Continue with the VM creation process.




###  gcloud 

**Note:** The `create-with-container` gcloud CLI command is deprecated. Use the equivalent `docker run` command to configure and to run the container. 

Use the `--container-mount-host-path` flag to mount a host VM directory into a container. The following example mounts the host directory `/tmp` into the container at `/logs` in read/write mode:
    
    
    gcloud compute instances create-with-container busybox-vm \
      --container-image docker.io/busybox:1.27 \
      --container-mount-host-path mount-path=/logs,host-path=/tmp,mode=rw
    

Specify `mode=ro` to mount a host directory in read-only mode.

Use the `gcloud compute instances update-container` command with the `--container-mount-host-path` flag to update host directory mounts on a container. Use the `--remove-container-mounts` flag to remove volume mounts with the specified mount paths. The following example removes a host path mount with `mount-path=/logs`:
    
    
    gcloud compute instances update-container busybox-vm \
      --remove-container-mounts /logs
    

If the specified mount path does not exist, it is silently ignored.

## Mounting tmpfs file system as a data volume

You can mount an empty tmpfs file system into a container.

An empty tmpfs file system is similar to a Google Kubernetes Engine [`EmptyDir`](https://kubernetes.io/docs/concepts/storage/volumes/#emptydir) volume with `medium:Memory`. Unlike Docker, where `tmpfs` data is deleted on container restarts, with `tmpfs` on a Compute Engine container, the volume and its data persist across container restarts and are deleted only on VM restart.

###  Console 

**Note:** The **Deploy container** option in the Google Cloud console is deprecated. Use the equivalent `docker run` command to configure and to run the container. 

  1. Go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. In the **Container** section, click **Deploy container**.

  3. On the **Configure container** page, do the following:

     1. Specify a container image name.
     2. In the **Volume mounts** section, click **Add volume**.
     3. From the **Volume type** list, select **TmpFS**.
     4. In the **Mount path** field, specify a mount path in a container directory structure where you would like to mount a TmpFS volume.
     5. In the **Mode** list, specify whether to mount the TmpFS volume in read/write or read-only mode.
     6. To confirm the container details, click **Select**.
  4. Continue with the VM creation process.




###  gcloud 

**Note:** The `create-with-container` gcloud CLI command is deprecated. Use the equivalent `docker run` command to configure and to run the container. 

Use the `--container-mount-tmpfs` flag to mount an empty `tmpfs` file system into a container. The following example mounts a `tmpfs` file system into the container at `/cache` in read/write mode:
    
    
    gcloud compute instances create-with-container busybox-vm \
      --container-image docker.io/busybox:1.27 \
      --container-mount-tmpfs mount-path=/cache
     

Use the `gcloud compute instances update-container` command with the `--container-mount-tmpfs` flag to update `tmpfs` mounts on a container. Use the `--remove-container-mounts`flag to remove a `tmpfs` mount with the specified mount path when updating. The following example removes the `tmpfs` mount with `mount-path=/cache`:
    
    
    gcloud compute instances update-container busybox-vm \
      --remove-container-mounts /cache
    

If the specified mount path does not exist, it is silently ignored.

## Mounting a persistent disk as a data volume

With [Container-Optimized OS 69](https://docs.cloud.google.com/container-optimized-os/docs/release-notes) or later, you can mount persistent disks from a host VM into a container.

**Note:** This is similar to using the [`gcePersistentDisk`](https://kubernetes.io/docs/concepts/storage/volumes/#gcepersistentdisk) volume type in Google Kubernetes Engine.

#### Prerequisites

  * The disk must have an `ext4` file system or have no file system. With no initial file system, the container startup agent (konlet) formats the disk to `ext4`, and only read/write attachment and mounting are supported.
  * The disk must be [attached](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk#create_disk) to the VM.
  * Both partitionless devices and partitions are supported. For partition mounts, the disk cannot be blank; it must contain an existing partition table.




###  Console 

**Note:** The **Deploy container** option in the Google Cloud console is deprecated. Use the equivalent `docker run` command to configure and to run the container. 

  1. Go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. In the **Container** section, click **Deploy container**.

  3. On the **Configure container** page, do the following:

     1. Specify a container image name.
     2. In the **Volume mounts** section, click **Add volume**.
     3. From the **Volume type** list, select **Disk**.
     4. In the **Mount path** field, specify a path in the container directory structure where you would like to mount the persistent disk.
     5. From the **Disk name** list, select an existing disk to mount.
     6. In the **Partition** field, specify the partition number to mount if the disk has a partition table. If the disk does not have partitions, leave this field blank.
     7. In the **Mode** list, specify whether to mount the directory in read/write or read-only mode.
     8. To confirm the container details, click **Select**.
  4. Continue with the VM creation process.




###  gcloud 

**Note:** The `create-with-container` gcloud CLI command is deprecated. Use the equivalent `docker run` command to configure and to run the container. 

Use the [`gcloud compute instances create-with-container`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container) command or the [`gcloud compute instances update-container`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/update-container) command with the `--container-mount-disk` flag to mount a persistent disk into a container.

The following example mounts two disks, `my-data-disk` and `my-scratch-disk`, into the container at `/disks/data-disk` and `/disks/scratch-disk` mount paths.
    
    
    gcloud compute instances create-with-container busybox-vm \
      --disk name=my-data-disk \
      --create-disk name=my-scratch-disk,auto-delete=yes,image=ubuntu-1710-artful-v20180315,image-project=ubuntu-os-cloud \
      --container-image docker.io/busybox:1.27 \
      --container-mount-disk mount-path="/disks/data-disk",name=my-data-disk,mode=ro \
      --container-mount-disk mount-path="/disks/scratch-disk",name=my-scratch-disk
    

Note that the `--disk` flag attaches `my-data-disk`, the `--create-disk` flag creates and attaches `my-scatch-disk`, and the `--container-mount-disk` flag mounts the attached disks to the container. Because a `mode` is not specified for `my-scratch-disk`, that disk is mounted to the container in read/write mode by default.

Use the `gcloud compute instances update-container` command with the `--container-mount-disk` flag to mount additional attached disks or to modify existing disk mounts.

Use the `--remove-container-mounts` flag to remove a disk volume mount with the specified mount path. The following example changes the mount mode of `my-data-disk` to read/write and removes the disk mount with `mount-path="/disks/scratch-disk"`.
    
    
    gcloud compute instances update-container busybox-vm \
      --container-mount-disk mount-path="/disks/data-disk",name=my-data-disk,mode=rw \
      --remove-container-mounts "/disks/scratch-disk"
    

If the mount path that you pass to the `--remove-container-mounts` flag does not exist, it is silently ignored.

## Publishing container ports

VMs with containers use the [host network mode](https://docs.docker.com/engine/reference/run/#network-settings), where a container shares the host's network stack and all interfaces from the host are available to the container.

Container ports have a one-to-one mapping to the host VM ports. For example, a container port 80 maps to the host VM port 80. Compute Engine does not support the port publishing (`-p`) flag, and you don't have to specify it for the mapping to work.

To publish a container's ports, [configure firewall rules](https://docs.cloud.google.com/compute/docs/vpc/using-firewalls) to enable access to the host VM's ports. The corresponding ports of the container are accessible automatically, according to the firewall rules.

**Example: Publishing port 80 for an NGINX container**

###  docker run 

Configure the `--network="host"` flag when using the `docker run` command. Learn more about [container network settings and host mode](https://docs.docker.com/engine/reference/run/#network-settings).

###  gcloud 

**Note:** The `create-with-container` gcloud CLI command is deprecated. Use the equivalent `docker run` command to configure and to run the container. 

The following example shows how to create a VM instance with an NGINX container and allow traffic to the container's port 80.

  1. Create a VM instance with an NGINX container:
         
         gcloud compute instances create-with-container nginx-vm \
         --container-image gcr.io/cloud-marketplace/google/nginx1:1.15 \
         --tags http-server
         

The container shares the host VM's network stack, and the container's port 80 is published to the host VM's port 80. The `http-server` tag is used as a target tag for the firewall rule, created in the next step.

  2. Create a firewall rule to enable connections to port 80 of the VM instance. The following firewall rule allows HTTP connections to VM instances with the `http-server` tag.
         
         gcloud compute firewall-rules create allow-http \
         --allow tcp:80 --target-tags http-server
         

The container automatically starts receiving traffic on port 80. You don't need to perform any additional configuration.

You can create firewall rules for host VM protocol:port combinations where the protocol is `tcp` or `udp`. These rules effectively govern access from outside the VM to the corresponding container ports.




## What's next

  * Learn how to [deploy Docker containers on Compute Engine](https://docs.cloud.google.com/compute/docs/containers/deploying-containers).
  * Learn about [Container-optimized OS](https://docs.cloud.google.com/container-optimized-os/docs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
