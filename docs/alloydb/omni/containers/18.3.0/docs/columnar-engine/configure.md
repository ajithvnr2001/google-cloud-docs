---
url: https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/columnar-engine/configure/
title: Configure the columnar engine in AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni using containers: 18.3.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:43:09.481377+00:00
---

# Configure the columnar engine in AlloyDB Omni  |  AlloyDB Omni using containers: 18.3.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/columnar-engine/configure/

This page documents AlloyDB Omni version **18.3.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Containers: 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/overview)



Send feedback 

#  Configure the columnar engine in AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.3.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/columnar-engine/configure)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/columnar-engine/configure)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/columnar-engine/configure)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/columnar-engine/configure)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/columnar-engine/configure)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/columnar-engine/configure)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/columnar-engine/configure)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/columnar-engine/configure)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/columnar-engine/configure)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/columnar-engine/configure)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/columnar-engine/configure)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/columnar-engine/configure)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/columnar-engine/configure)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/columnar-engine/configure)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/columnar-engine/configure)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/columnar-engine/configure)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/columnar-engine/configure)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/columnar-engine/configure)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/columnar-engine/configure)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/columnar-engine/configure)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/columnar-engine/configure)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/columnar-engine/configure)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/columnar-engine/configure)

This page describes how to enable or disable the columnar engine on an AlloyDB Omni database cluster. It also covers how to configure an appropriate initial size for its column store. 

For a conceptual overview of the AlloyDB columnar engine, see [AlloyDB Omni columnar engine overview](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/columnar-engine/overview).

## Enable the columnar engine

To use columnar engine on an instance, set the instance's [`google_columnar_engine.enabled`](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/reference/columnar-engine-flags#enabled) flag to `on`.

###  Single-server 

To set the `google_columnar_engine.enabled` to `on`, do the following steps:

  1. Run [the `ALTER SYSTEM` PostgreSQL command](https://www.postgresql.org/docs/current/sql-altersystem.html):
         
         ALTER SYSTEM SET google_columnar_engine.enabled = 'on'
         

  2. If you want to adjust the columnar engine's configuration, then follow the instructions in the [next section](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/columnar-engine/configure#configure) before you restart the database server. Otherwise, complete the following step to restart the database server now.

  3. For the configuration parameters change to take effect, restart your running container with AlloyDB Omni.

###  Docker 
         
         sudo docker restart CONTAINER_NAME

###  Podman 
         
         sudo podman restart CONTAINER_NAME




## Configure the size of the column store

While the columnar engine is enabled on an instance, AlloyDB Omni allocates a portion of the instance's memory to store its columnar data. Dedicating high-speed RAM to your column store verifies that AlloyDB Omni can access the columnar data as rapidly as possible.

Memory and storage cache together represent the overall capacity of the columnar engine.

### Configure memory

**Warning:** The default value of `google_columnar_engine.memory_size_in_mb` is 1024 MB.

You can set the allocation to a fixed size using the [`google_columnar_engine.memory_size_in_mb`](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/reference/columnar-engine-flags#memory-size-in-mb) flag.

###  Single-server 

To set the `google_columnar_engine.memory_size_in_mb` flag on an instance, do the following:

  1. Configure memory by running the [`ALTER SYSTEM`](https://www.postgresql.org/docs/current/sql-altersystem.html) PostgreSQL command:
         
         ALTER SYSTEM SET google_columnar_engine.memory_size_in_mb = COLUMN_MEMORY_SIZE;
         

Replace `COLUMN_MEMORY_SIZE` with the new size of the column storage, in megabytes—for example, `256`.

  2. For the configuration parameters change to take effect, restart your running container with AlloyDB Omni.

###  Docker 
         
         sudo docker restart CONTAINER_NAME

###  Podman 
         
         sudo podman restart CONTAINER_NAME




### Configure storage cache

**Note:** This step is optional for enabling the columnar engine.

###  Single-server 

You can configure the columnar engine storage cache on either dedicated or shared devices.

#### Dedicated devices

On dedicated devices, to enable AlloyDB Omni columnar engine storage cache for a single-server container, you need to provision disks and create a file system, then mount the cache directory inside AlloyDB Omni, and finally enable the columnar storage cache.

##### Provision disks and create a file system

To provide storage for the AlloyDB Omni columnar engine storage cache, follow the instructions for your host operating system to prepare a storage medium—such as a named Docker volume or a file system on dedicated disks. 

###### Non-Linux (macOS, Windows)

On macOS or Windows, use a named Docker volume for the columnar storage cache to ensure optimal performance.

  1. Create a named volume:
         
         docker volume create COLUMNAR_CACHE_VOLUME

Replace `COLUMNAR_CACHE_VOLUME` with a name for the volume—for example, `omni-columnar-cache`.

  2. Use this volume when running your container. For more information, see Mount columnar storage cache directory.




###### Linux

To provision disks and create a file system for AlloyDB Omni columnar engine storage cache, you create a file system on a disk or multiple disks and mount it inside a container with AlloyDB Omni. Additionally, you can use utilities like `mdadm` or `lvm` to pool capacity together using multiple disks and use any file system. The following steps demonstrate using `lvm` and `ext4` on a Ubuntu Compute Engine instance using NVMe SSDs.

  1. Create a volume group from all available physical devices:
         
         nvme_prefix="STORAGE_PREFIX"
               nvme_list=$(ls "$nvme_prefix"*)
               sudo vgcreate VOLUME_GROUP ${nvme_list}

Replace the following:

     * `STORAGE_PREFIX`: the prefix of the target local disks path that are attached to a virtual machine using the nonvolatile memory express (NVMe) interface—for example, on Google Cloud, the NVMe device paths always start with `/dev/nvme0n`.
     * `VOLUME_GROUP`: the name of a volume group where your SSDs are combined—for example, `omni-disk-cache-volume`.
  2. To create a logical volume from the free capacity of the volume group from the preceding step, use the following command:
         
         sudo lvcreate -n LOGICAL_VOLUME -l 100%FREE VOLUME_GROUP

Replace `LOGICAL_VOLUME` with the name of a logical volume that is treated as a partition by the LVM—for example, `omni_disk_cache_device`.

  3. Create the `ext4` file system on the logical volume. If needed, you can specify other `ext4` options subject to data safety. 
         
         sudo mkfs.ext4 /dev/VOLUME_GROUP/LOGICAL_VOLUME

  4. To create a directory that serves as a mount point on the host machine and mount the file system, use the following command:
         
         sudo mkdir /OMNI_COLUMNAR_STORAGE_CACHE_DIRECTORY
               sudo mount /dev/VOLUME_GROUP/LOGICAL_VOLUME /OMNI_COLUMNAR_STORAGE_CACHE_DIRECTORY

Replace `OMNI_COLUMNAR_STORAGE_CACHE_DIRECTORY` with the name of the directory or a path to the directory serving as a mount point—for example, `omni_columnar_storage_cache_directory`.




##### Mount columnar storage cache directory inside AlloyDB Omni

Before enabling disk cache for AlloyDB Omni running in a container, you must mount the cache directory inside AlloyDB Omni.

To mount the cache directory inside your container, use the `-v` flag.

  * For Linux host paths:

`-v /OMNI_COLUMNAR_STORAGE_CACHE_DIRECTORY:/CACHE_DIRECTORY_PATH_INSIDE_CONTAINER`
  * For named volumes (non-Linux):

`-v COLUMNAR_CACHE_VOLUME:/CACHE_DIRECTORY_PATH_INSIDE_CONTAINER`



Example Docker command using a named volume:
    
    
      sudo docker run --name CONTAINER_NAME   
        -e POSTGRES_PASSWORD=PASSWORD   
        -e PGDATA=/var/lib/postgresql/data/pgdata   
        -v DATA_DIR:/var/lib/postgresql/data   
        -v COLUMNAR_CACHE_VOLUME:/var/lib/alloydb/columnar_cache   
        -d google/alloydbomni

For information about installing AlloyDB Omni from a [Docker image](https://registry.hub.docker.com/r/google/alloydbomni) and customizing it, see [Customize your AlloyDB Omni installation](https://docs.cloud.google.com/alloydb/omni/15-next/docs/install).

To mount the `OMNI_COLUMNAR_STORAGE_CACHE_DIRECTORY` inside your Docker container running AlloyDB Omni, use the following command:

### Docker
    
    
      sudo docker run --name CONTAINER_NAME   
        -e POSTGRES_PASSWORD=PASSWORD   
        -e PGDATA=/var/lib/postgresql/data/pgdata   
        -v DATA_DIR:/var/lib/postgresql/data   
        -v /OMNI_COLUMNAR_STORAGE_CACHE_DIRECTORY:/CACHE_DIRECTORY_PATH_INSIDE_CONTAINER   
        -d google/alloydbomni
      

Replace the following:

  * `CONTAINER_NAME`: the name to assign the new AlloyDB Omni container—for example, `my-omni`.
  * `PASSWORD`: the password for your PostgreSQL database root administrator.
  * `DATA_DIR`: the file system path that you want AlloyDB Omni to use for its data directory.
  * `CACHE_DIRECTORY_PATH_INSIDE_CONTAINER`: the cache directory inside the AlloyDB Omni container that maps to the mount point on the host machine—for example, based on the value of the cache directory inside the container, either `/omni_disk_cache_directory`, similar to `OMNI_COLUMNAR_STORAGE_CACHE_DIRECTORY`, or `/disk/cache/inside/container`.



### Podman
    
    
      podman run --name CONTAINER_NAME   
        -e POSTGRES_PASSWORD=PASSWORD   
        -e PGDATA=/var/lib/postgresql/data/pgdata   
        -v DATA_DIR:/var/lib/postgresql/data   
        -v /OMNI_COLUMNAR_STORAGE_CACHE_DIRECTORY:/CACHE_DIRECTORY_PATH_INSIDE_CONTAINER   
        -d docker.io/google/alloydbomni
      

Replace the following:

  * `CONTAINER_NAME`: the name to assign the new AlloyDB Omni container—for example, `my-omni`.
  * `PASSWORD`: the password for your PostgreSQL database root administrator.
  * `CACHE_DIRECTORY_PATH_INSIDE_CONTAINER`: the cache directory inside the AlloyDB Omni container that maps to the mount point on the host machine—for example, based on the value of the cache directory inside the container, either `/omni_columnar_storage_cache_directory`, similar to `OMNI_COLUMNAR_STORAGE_CACHE_DIRECTORY`, or `/disk/cache/inside/container`.



To grant full access permissions to the mounted `OMNI_COLUMNAR_STORAGE_CACHE_DIRECTORY`, use the following commands:

### Docker
    
    
      sudo docker exec -it CONTAINER_NAME chown postgres:postgres /CACHE_DIRECTORY_PATH_INSIDE_CONTAINER
      sudo docker exec -it CONTAINER_NAME chmod -R a+rw  /CACHE_DIRECTORY_PATH_INSIDE_CONTAINER
      

### Podman
    
    
      sudo podman exec -it CONTAINER_NAME chown postgres:postgres /CACHE_DIRECTORY_PATH_INSIDE_CONTAINER
      sudo podman exec -it CONTAINER_NAME chmod -R a+rw  /CACHE_DIRECTORY_PATH_INSIDE_CONTAINER
      

##### Enable AlloyDB Omni columnar storage cache for AlloyDB Omni running in a container

To enable AlloyDB Omni columnar storage cache on dedicated devices for your database, set the appropriate Grand Unified Configuration (GUC) parameters after verifying that the mounted cache directory is accessible from inside the Docker container.

  1. Set the columnar storage cache directory:
         
         ALTER SYSTEM SET google_columnar_engine.omni_storage_cache_directory = OMNI_COLUMNAR_STORAGE_CACHE_DIRECTORY;
         

Replace `OMNI_COLUMNAR_STORAGE_CACHE_DIRECTORY` with the absolute path to the dedicated directory where you want AlloyDB Omni to store columnar engine storage cache files. Verify this directory exists and has appropriate write permissions for the database user.

  2. Configure the storage cache size:
         
         ALTER SYSTEM SET google_columnar_engine.storage_cache_size = STORAGE_CACHE_SIZE;
         

Replace `STORAGE_CACHE_SIZE` with the size of the columnar storage cache size you want, in megabytes. By default, the entire size of the dedicated device is allocated to the columnar engine, without affecting the disk cache. The maximum allowed value for this flag is 1000 * `google_columnar_engine.memory_size_in_mb` whichever is minimum.

  3. For the configuration parameters change to take effect, restart your running container with AlloyDB Omni.

###  Docker 
         
         sudo docker restart CONTAINER_NAME

###  Podman 
         
         sudo podman restart CONTAINER_NAME




#### Shared devices

Before configuring the columnar storage cache to shared devices with disk cache, you must [enable AlloyDB Omni disk cache](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/configure-disk-cache#enable-cache).

Configure storage cache on shared devices as follows:

  1. Configure storage cache:
         
         ALTER SYSTEM SET google_columnar_engine.storage_cache_size = STORAGE_CACHE_SIZE;
         

Replace `STORAGE_CACHE_SIZE` with the size of the storage cache size you want, in megabytes. By default, 5% of the disk cache is allocated to the columnar engine. The maximum allowed value for this flag is 50% of the total disk cache or 1000 * `google_columnar_engine.memory_size_in_mb` whichever is minimum.

  2. For the configuration parameters change to take effect, restart your running container with AlloyDB Omni.

###  Docker 
         
         sudo docker restart CONTAINER_NAME

###  Podman 
         
         sudo podman restart CONTAINER_NAME




## Enable vectorized join

The columnar engine has a _vectorized join_ feature that can improve the performance of joins by applying vectorized processing to qualifying queries.

After you enable vectorized join, the AlloyDB query planner has the option to apply the vectorized join operator instead of the standard PostgreSQL hash join operator. The planner makes this decision by comparing the cost of executing the query using each method.

To enable vectorized join on an instance, set the instance's [`google_columnar_engine.enable_vectorized_join`](https://docs.cloud.google.com/alloydb/omni/16.8.0/docs/reference/columnar-engine-flags#enable-vectorized-join) flag to `on`.

To set this flag on an instance, run [the `ALTER SYSTEM` PostgreSQL command](https://www.postgresql.org/docs/current/sql-altersystem.html):
    
    
    ALTER SYSTEM SET google_columnar_engine.enable_vectorized_join = 'on';
    

AlloyDB Omni allocates one thread to the vectorized join feature by default. You can increase the number of threads available to this feature by setting the [`google_columnar_engine.vectorized_join_threads`](https://docs.cloud.google.com/alloydb/omni/current/docs/reference/columnar-engine-flags#vectorized-join-threads) flag to a larger value. The maximum value is `cpu_count * 2`.

## Manually refresh your columnar engine

By default, when the columnar engine is enabled it refreshes the column store in the background.

To manually refresh the column engine, run the following SQL query:
    
    
    SELECT google_columnar_engine_refresh(relation =>'TABLE_NAME');
    

Replace `TABLE_NAME` with the name of the table or the materialized view you want to manually refresh.

## Disable the columnar engine

To disable the columnar engine on an instance, set the `google_columnar_engine.enabled` flag to `off`.

###  Single-server 

To set the `google_columnar_engine.enabled` to `off`, do the following steps:

  1. Run [the `ALTER SYSTEM` PostgreSQL command](https://www.postgresql.org/docs/current/sql-altersystem.html):


    
    
    ALTER SYSTEM SET google_columnar_engine.enabled = 'off'
    

  1. For the configuration parameters change to take effect, restart your running container with AlloyDB Omni.



###  Docker 

To restart an AlloyDB Omni container, run [the `docker container restart` command](https://docs.docker.com/reference/cli/docker/container/restart/):
    
    
      sudo docker restart CONTAINER_NAME

Replace `CONTAINER_NAME` with the name that you assigned to the AlloyDB Omni container when you installed it.

###  Podman 

To restart an AlloyDB Omni container, run [the `podman container start` command](https://docs.podman.io/en/latest/markdown/podman-restart.1.html):
    
    
      sudo podman restart CONTAINER_NAME

Replace `CONTAINER_NAME` with the name that you assigned to the AlloyDB Omni container when you installed it.

## What's next

  * See the [complete list of columnar engine database flags](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/reference/columnar-engine-flags).

  * Try out the codelab [Accelerating analytical queries with columnar engine in AlloyDB Omni](https://codelabs.developers.google.com/alloydb-omni-columnar).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
