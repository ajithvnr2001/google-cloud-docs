---
url: https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/deploy-vm/
title: Install AlloyDB Omni on a VM \u00a0|\u00a0 AlloyDB Omni for containers: 15.7.1 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:51:09.527851+00:00
---

# Install AlloyDB Omni on a VM  |  AlloyDB Omni for containers: 15.7.1  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/deploy-vm/

This page documents AlloyDB Omni version **15.7.1** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/overview)



Send feedback 

#  Install AlloyDB Omni on a VM Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.7.1keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/deploy-vm)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/deploy-vm)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/deploy-vm)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/deploy-vm)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/deploy-vm)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/deploy-vm)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/deploy-vm)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/deploy-vm)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/deploy-vm)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/deploy-vm)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/deploy-vm)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/deploy-vm)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/deploy-vm)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/deploy-vm)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/deploy-vm)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/deploy-vm)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/deploy-vm)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/deploy-vm)

This page describes how to perform single instance installations of AlloyDB Omni on any Linux VM that supports container runtimes. If you need a multi-instance configuration of AlloyDB Omni, see [High availability and data resilience](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/high-availability/overview). 

## Before you begin

Before you install AlloyDB Omni, make sure that you meet the following requirements.

### Plan your installation

Before you install AlloyDB Omni on your VM, do the following:

  1. Read [Plan your AlloyDB Omni installation on a VM](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/plan-installation).
  2. Read Run AlloyDB Omni rootful or rootless and complete any necessary steps for rootful or rootless depending on which environment you choose.



### Choose a download or installation option

Choose one of the following download and installation options:

**Media** | **Download locations and installation guides** | **Deployment to**  
---|---|---  
**Debian image** | [DockerHub](https://hub.docker.com/r/google/alloydbomni/tags) (tags) | 

  * [Docker](https://www.docker.com/), [Podman](https://podman.io/). You can run these containerization tools as a container in any virtual machine (VM).


  * [Google Cloud Marketplace](https://console.cloud.google.com/marketplace/product/click-to-deploy-images/alloydb-omni)


  * [AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-sne7ttiby7nxi)


  * [Azure Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/google-cloud-alloydb-omni.alloydbomni?tab=overview)

  
**UBI Image (Red Hat)** | [Red Hat Ecosystem Catalog](https://catalog.redhat.com/software/container-stacks/detail/67d88bd7ce4ca47642c2a072) | 

  * Red Hat environment. Run this as a container.


  * [Red Hat Marketplace](https://catalog.redhat.com/software/containers/google/alloydbomni/681daa13362cef4fe8a0115f) (UBI)

  
  
## Run AlloyDB Omni rootful or rootless

**Note:** If you want to deploy AlloyDB Omni in your production environment, see [Run AlloyDB Omni in production](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/run-alloydb-omni-production).

You can run AlloyDB Omni using either Docker or Podman. Both of these container engines can be run as rootful or rootless. Rootful refers to running Docker or Podman as the root user, while rootless refers to running them as a non-root, or unprivileged, user.

The mode you choose depends on the requirements and preferences you have for the environment. If simplicity is important, then rootful might be right for you. If you need the security of an unprivileged user, then rootless might be the right choice.

If you decide to run a rootful environment, you need to decide how to manage the user mapping between the container and your host machine. In practice, AlloyDB Omni runs processes as the `postgres` user, which has a UID and GID of `999`. This means that you have two options to manage the user mapping:

  * Do nothing. `postgres` will continue to _not_ map to any user on your host machine.
  * Create a user and user group with UID and GID of `999` so that `postgres` maps to that user and user group.



For rootless environments, `postgres` maps to a sub-UID and sub-GID that the host user and user group have access to (as defined in your `/etc/subuid` and `/etc/subgid` files). This means that you don't need to manage the user mapping.

**Tip:** For Linux command examples, `#` indicates running the command as root, while `$` indicates running the command as an unprivileged user.

### (Rootless) Configure sub-UID and sub-GID ranges

If your Linux image doesn't already have sub-UID and sub-GID ranges configured for your unprivileged user, then you must configure them to run AlloyDB Omni rootless.

  1. If you are on a Debian system, install `newuidmap` and `newgidmap` binaries.
         
         apt-get install -y uidmap
         

  2. Add a `subuid` entry for your rootless user.
         
         echo "ROOTLESS_USER:SUB_UID_RANGE_START:SUB_UID_RANGE_COUNT" >> /etc/subuid
         

Replace the following variables:

     * `ROOTLESS_USER`: User that you want to run AlloyDB Omni as.
     * `SUB_UID_RANGE_START`: Lower number of the range of sub-UIDs you want to register for your user.
     * `SUB_UID_RANGE_COUNT`: Amount of sub-UIDs you want to register for your user. This value must be at least 999.
  3. Add a `subgid` entry for your rootless user.
         
         echo "ROOTLESS_USER:SUB_GID_RANGE_START:SUB_GID_RANGE_COUNT" >> /etc/subgid
         

Replace the following variables:

     * `ROOTLESS_USER`: User that you want to run AlloyDB Omni as.
     * `SUB_GID_RANGE_START`: Lower number of the range of sub-GIDs you want to register for your user.
     * `SUB_GID_RANGE_COUNT`: Amount of sub-GIDs you want to register for your user. This value must be at least 999.
  4. If you want your AlloyDB Omni instance to run while your user isn't logged in, run the following command.
         
         loginctl enable-linger ROOTLESS_USER
         

Replace the following variable:

     * `ROOTLESS_USER`: User that you want to run AlloyDB Omni as.
  5. If you are using Docker, run the following command as ROOTLESS_USER.
         
         /usr/bin/dockerd-rootless-setuptool.sh install 
         

  6. Open a new shell so that the sub-UID and sub-GID changes take effect.




## Create directory where AlloyDB Omni stores data

If you're using a storage system that does more than just run AlloyDB Omni, you can create the AlloyDB Omni directory on your device's existing file system. Otherwise, you can create a new file system on your dedicated device.

### Existing file system

### Docker
    
    
    mkdir -p DATA_DIR
    

### Docker
    
    
    mkdir -p DATA_DIR

### Podman
    
    
    mkdir -p DATA_DIR
    

### Podman
    
    
    mkdir -p DATA_DIR

Replace the following variables:

  * `DATA_DIR`: Host directory path that your data is stored in.



### Dedicated device

  1. Create a directory on the host where the disk will be mounted.
         
         mkdir -p MOUNT_POINT
         

Replace the following variable:

     * `MOUNT_POINT`: Top-level directory path that should contain your AlloyDB Omni instance.
  2. Create a gpt partition table with a single partition on the disk device.
         
         parted -s DEVICE_PATH mklabel gpt
         parted -s DEVICE_PATH mkpart primary 0% 100%

Replace the following variable:

     * `DEVICE_PATH`: Path assigned by the operating system to the disk device.
  3. Create a file system on the disk device. We recommend using the `ext4` file system for AlloyDB Omni.
         
         mkfs.ext4 -q -m 1 -L FS_LABEL -F PARTITION_PATH
         

Replace the following variables:

     * `FS_LABEL`: Label for the file system. The maximum length of an `ext4` file system label is 16 characters.
     * `PARTITION_PATH`: Path for the disk partition used to store the container's data.
  4. Mount the device and create an entry in the `/etc/fstab` file so that the disk is mounted after a reboot.
         
         echo -e "LABEL=FS_LABEL\tMOUNT_POINT\text4\tdefaults\t0 0" | tee -a /etc/fstab
         systemctl daemon-reload
         mount MOUNT_POINT

Replace the following variables:

     * `FS_LABEL`: Label for the file system. The maximum length of an `ext4` file system label is 16 characters.
     * `MOUNT_POINT`: Top-level directory path that should contain your AlloyDB Omni instance.
  5. Create a data directory in the container specific file system.

### Rootful
         
         mkdir -p DATA_DIR
         

### Rootless
         
         mkdir -p DATA_DIR
         chown ROOTLESS_USER:ROOTLESS_GROUP DATA_DIR

Replace the following variables:

     * `DATA_DIR`: Host directory path that your data is stored in.
     * `ROOTLESS_USER`: If you're using a rootless environment, then this is the user that you want to own the directory.
     * `ROOTLESS_GROUP`: If you're using a rootless environment, then this is the group that you want to own the directory.



## Create the container

### Docker
    
    
    docker run -d --name CONTAINER_NAME \
    -e POSTGRES_PASSWORD=NEW_PASSWORD \
    -v DATA_DIR:/var/lib/postgresql/data \
    -p HOST_PORT:5432 \
    --restart=always \
    google/alloydbomni:latest
    

### Docker
    
    
    docker run -d --name CONTAINER_NAME \
    -e POSTGRES_PASSWORD=NEW_PASSWORD \
    -v DATA_DIR:/var/lib/postgresql/data \
    -p HOST_PORT:5432 \
    --restart=always \
    google/alloydbomni:latest
    

### Podman
    
    
    podman run -d --name CONTAINER_NAME \
    -e POSTGRES_PASSWORD=NEW_PASSWORD \
    -v DATA_DIR:/var/lib/postgresql/data \
    -p HOST_PORT:5432 \
    --restart=always \
    docker.io/google/alloydbomni:latest
    

### Podman
    
    
    podman run -d --name CONTAINER_NAME \
    -e POSTGRES_PASSWORD=NEW_PASSWORD \
    -v DATA_DIR:/var/lib/postgresql/data \
    -p HOST_PORT:5432 \
    --restart=always \
    docker.io/google/alloydbomni:latest
    

Replace the following variables:

  * `CONTAINER_NAME`: Name you used for the directory in Create directory where AlloyDB Omni stores data.
  * `NEW_PASSWORD`: Password assigned to the new container's `postgres` user after its creation.
  * `DATA_DIR`: Host directory path that your data is stored in.
  * `HOST_PORT`: TCP port on the host machine that the container should publish its own port `5432` to. To use the PostgreSQL default port on the host machine as well, specify `5432`.



## Connect to your instance

Depending on your environment, you can connect to your AlloyDB Omni instance either locally or remotely.

### Connect locally

### Docker
    
    
    docker exec -it CONTAINER_NAME psql -U postgres
    

### Docker
    
    
    docker exec -it CONTAINER_NAME psql -U postgres
    

### Podman
    
    
    podman exec -it CONTAINER_NAME psql -U postgres
    

### Podman
    
    
    podman exec -it CONTAINER_NAME psql -U postgres
    

Replace the following variable:

  * `CONTAINER_NAME`: Name you used for the directory in Create directory where AlloyDB Omni stores data.



### Connect remotely
    
    
    psql -U postgres -p HOST_PORT -h IP_ADDRESS_OR_FQDN
    

Replace the following variables:

  * `HOST_PORT`: TCP port you used in Create the container.
  * `IP_ADDRESS_OR_FQDN`: IP address or fully-qualified domain name for the host where AlloyDB Omni is running.



After running this command, you're asked for the password of the `postgres` account. Enter the password you used in Create the container.

## What's next

  * [Customize your AlloyDB Omni installation](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/install)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
