---
url: https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/install/
title: Customize your AlloyDB Omni installation \u00a0|\u00a0 AlloyDB Omni for containers: 17.5.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:04:14.914706+00:00
---

# Customize your AlloyDB Omni installation  |  AlloyDB Omni for containers: 17.5.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/install/

This page documents AlloyDB Omni version **17.5.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/overview)



Send feedback 

#  Customize your AlloyDB Omni installation Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 17.5.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/install)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/install)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/install)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/install)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/install)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/install)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/install)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/install)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/install)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/install)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/install)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/install)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/install)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/install)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/install)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/install)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/install)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/install)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/install)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/install)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/install)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/install)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/install)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/install)



This page describes how to customize your AlloyDB Omni installation, which is deployed through a container image that supports different forms of customization. This page shows some common customizations.

## Enable and disable AlloyDB Omni telemetry

AlloyDB Omni telemetry implements a lightweight client agent that runs only in the AlloyDB Omni container image. This agent periodically collects a set of basic, pseudonymous metrics and sends them to a Google-managed endpoint.

**Note:** The AlloyDB Omni telemetry feature is enabled by default in the container images.

Because AlloyDB Omni is a downloadable product that's offered at no charge, this telemetry provides Google with essential, non-personally identifiable information (non-PII) metrics regarding the generic adoption and deployment environments of running instances. This data helps inform product development and support prioritization.

Collected metrics include the following:

  * Unique installation ID (pseudonymized UUID)
  * AlloyDB Omni version and PostgreSQL major version
  * Host system information like CPU count, RAM, and uptime



### Disable telemetry reporting

To prevent the telemetry agent from running and reporting usage metrics, set the PostgreSQL configuration parameter `omni_enable_telemetry` to `off`. You can disable the telemetry agent by setting the telemetry flag in the `postgresql.conf` file or by setting the flag at runtime using `ALTER SYSTEM`.

#### Set the telemetry flag in the postgresql.conf file

**Note:** To downgrade to a version of AlloyDB Omni that's earlier than PostgreSQL 16.9.0 or 17.5.0, you must remove `omni_enable_telemetry` from the `postgresql.conf` file.

To modify the PostgreSQL configuration file in your container's persistent data directory, follow these steps:

  1. Locate the `postgresql.conf` file in your database's data directory (`$PGDATA`).
  2. Disable AlloyDB Omni telemetry.
         
         omni_enable_telemetry = off
         

  3. To apply the change, restart your AlloyDB Omni container. The telemetry agent stops collecting and sending usage metrics to Google.




#### Set the telemetry flag at runtime using ALTER SYSTEM

To set the telemetry flag and persist the change across restarts, follow these steps:

  1. Connect to your AlloyDB Omni instance using `psql`:
         
         psql -h HOST -U USER -d DATABASE
         

Make the following replacements:

     * `HOST`: the hostname or IP address of your AlloyDB Omni instance—for example, `127.0.0.1`.
     * `USER`: the database user that you want to connect as—for example, `postgres`.
     * `DATABASE`: the database that you want to connect to—for example, `postgres`.
  2. Run the following command:
         
         ALTER SYSTEM SET omni_enable_telemetry = 'off';
         

  3. Reload the configuration or restart the instance. In some container setups, you might need to restart your instance to make sure that the change is fully picked up by the background worker.
         
         SELECT pg_reload_conf();
         

The telemetry agent stops collecting and sending usage metrics to Google.




### Enable telemetry reporting

If you previously disabled AlloyDB Omni telemetry, you can re-enable it by setting the `omni_enable_telemetry` flag to `on`. You enable the telemetry agent by setting the flag in the `postgresql.conf` file or by setting the flag at runtime using `ALTER SYSTEM`.

#### Set the telemetry flag in the postgresql.conf file

  1. Locate the `postgresql.conf` file in your database's data directory (`$PGDATA`).
  2. Set the following line:
         
         omni_enable_telemetry = on
         

  3. To apply the change, restart your AlloyDB Omni container.




#### Set the telemetry flag at runtime using ALTER SYSTEM

  1. Connect to your AlloyDB Omni instance using `psql`.
  2. Run the following command:
         
         ALTER SYSTEM SET omni_enable_telemetry = 'on';
         

  3. To apply the change, restart your AlloyDB Omni container.
         
         docker restart CONTAINER_NAME
         

Make the following replacement:

     * `CONTAINER_NAME`: The name of your AlloyDB Omni container—for example, `my-omni-1`.



### Check AlloyDB Omni telemetry status

You can check the status of the AlloyDB Omni telemetry agent, including whether it's enabled or running. You can also check telemetry agent activity.

#### Check if the telemetry agent is enabled or disabled

To check the status of the telemetry setting, follow these steps:

  1. Connect to your instance.
  2. Run the following:


    
    
    SHOW omni_enable_telemetry;
    

The output returns `on` or `off`, depending on whether you disabled or enabled AlloyDB Omni telemetry.

#### Check if the telemetry agent is running

To check whether the telemetry agent is running, run the following command in the container host:
    
    
    docker top CONTAINER_NAME
    

Make the following replacement:

  * `CONTAINER_NAME`: The name of your AlloyDB Omni container—for example, `my-omni-1`.



If telemetry is enabled and running, the output contains a line with the text `postgres: omni telemetry worker`.

#### Check telemetry agent activity

To check the activity of the telemetry agent, run the following command in the container host:
    
    
    docker logs CONTAINER_NAME 2>&1 | grep telemetry
    

Make the following replacement:

  * `CONTAINER_NAME`: The name of your AlloyDB Omni container—for example, `my-omni-1`.



If the telemetry agent is running, the logs contain messages similar to the following:
    
    
    LOG:  [telemetry_agent_worker.cc:143]  Started telemetry worker
    LOG:  [telemetry_agent_worker.cc:161]  Running telemetry reporting agent
    telemetry_agent: Uploading telemetry data to https://cloud.google.com/log.
    

## Mount an external data directory

By default, the command in [Quickstart: Install AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/quickstart) stores the database data in an area managed by Docker or Podman. This is convenient for getting started but makes it difficult to find and use the data directory. Instead, you can set up a bind mount to map the data directory to a known location on your disk.

### Docker
    
    
    docker run -d --name CONTAINER_NAME \
    -e POSTGRES_PASSWORD=NEW_PASSWORD \
    -v DATA_DIR:/var/lib/postgresql/data \
    -p HOST_PORT:5432 \
    --restart=always \
    google/alloydbomni:IMAGE_TAG
    

### Docker
    
    
    docker run -d --name CONTAINER_NAME \
    -e POSTGRES_PASSWORD=NEW_PASSWORD \
    -v DATA_DIR:/var/lib/postgresql/data \
    -p HOST_PORT:5432 \
    --restart=always \
    google/alloydbomni:IMAGE_TAG
    

### Podman
    
    
    podman run -d --name CONTAINER_NAME \
    -e POSTGRES_PASSWORD=NEW_PASSWORD \
    -v DATA_DIR:/var/lib/postgresql/data \
    -p HOST_PORT:5432 \
    --restart=always \
    docker.io/google/alloydbomni:IMAGE_TAG
    

### Podman
    
    
    podman run -d --name CONTAINER_NAME \
    -e POSTGRES_PASSWORD=NEW_PASSWORD \
    -v DATA_DIR:/var/lib/postgresql/data \
    -p HOST_PORT:5432 \
    --restart=always \
    docker.io/google/alloydbomni:IMAGE_TAG
    

Replace the following variables: 

  * `CONTAINER_NAME`: name that you used for your container. For example, `my-omni-1`. 
  * `NEW_PASSWORD`: password assigned to the new container's `postgres` user after its creation. 
  * `DATA_DIR`: host directory path that your data is stored in. 
  * `HOST_PORT`: TCP port on the host machine that the container must publish its own port `5432` to. To use the PostgreSQL default port on the host machine as well, specify `5432`. 
  * `IMAGE_TAG`: use `17.5.0` for the latest Debian image or `17.5.0-ubi9` for the latest UBI image. 



### Mounting an external data directory when using SELinux

If SELinux is enabled and the mode is set to `enforcing`, attempting to mount an external data directory results in permission errors. To mount an external data directory when using SELinux, complete the following instructions:

### Docker

  1. If your AlloyDB Omni container is running, stop it. 
         
         docker stop CONTAINER_NAME

Replace the following variable: 
     * `CONTAINER_NAME`: name that you used for your container. For example, `my-omni-1`. 
  2. Set SELinux's mode to `permissive`. This lets you run your container and identify details about what access is required to mount an external data directory. 
         
         setenforce 0

  3. Run your container with an external data directory. 
         
         docker run -d --name CONTAINER_NAME \
         -e POSTGRES_PASSWORD=NEW_PASSWORD \
         -v DATA_DIR:/var/lib/postgresql/data \
         -p HOST_PORT:5432 \
         --restart=always \
         google/alloydbomni:IMAGE_TAG
         

Replace the following variables: 
     * `CONTAINER_NAME`: name that you used for your container. For example, `my-omni-1`. 
     * `NEW_PASSWORD`: password assigned to the new container's `postgres` user after its creation. 
     * `DATA_DIR`: host directory path that your data is stored in. 
     * `HOST_PORT`: TCP port on the host machine that the container must publish its own port `5432` to. To use the PostgreSQL default port on the host machine as well, specify `5432`. 
     * `IMAGE_TAG`: use `17.5.0` for the latest Debian image or `17.5.0-ubi9` for the latest UBI image. 
  4. If not already installed, install `policycoreutils-python-utils` through your package manager. This package provides utilities necessary to manage SELinux policies. 
  5. For your external data directory, set the appropriate SELinux context. 
         
         semanage fcontext -a -t container_file_t "DATA_DIR"
         
         restorecon -Rv "DATA_DIR"

Replace the following variable: 
     * `DATA_DIR`: host directory path that your data is stored in. 
  6. Use `ausearch` to get information about the additional permission requirements. 
         
         ausearch -c 'postgres' --raw > postgres.avc

  7. Create a SELinux security profile based on your AlloyDB Omni container and `ausearch` permission information. 
         
         docker inspect CONTAINER_NAME | udica --append-rules postgres.avc CONTAINER_NAME

Replace the following variable: 
     * `CONTAINER_NAME`: name that you used for your container. For example, `my-omni-1`. 
  8. Load the SELinux module. 
         
         semodule -i CONTAINER_NAME.cil /usr/share/udica/templates/{base_container.cil,net_container.cil}

Replace the following variable: 
     * `CONTAINER_NAME`: name that you used for your container. For example, `my-omni-1`. 
  9. Enable `mmap`. 
         
         setsebool -P domain_can_mmap_files 1

  10. Stop and remove your AlloyDB Omni container. 
         
         docker stop CONTAINER_NAME && docker rm CONTAINER_NAME

Replace the following variable: 
     * `CONTAINER_NAME`: name that you used for your container. For example, `my-omni-1`. 
  11. Set SELinux's mode to `enforcing`. 
         
         setenforce 1

  12. Re-create your AlloyDB Omni container. 
         
         docker run -d --name CONTAINER_NAME \
         -e POSTGRES_PASSWORD=NEW_PASSWORD \
         -v DATA_DIR:/var/lib/postgresql/data \
         -p HOST_PORT:5432 \
         --restart=always \
         --security-opt label=type:CONTAINER_NAME.process \
         google/alloydbomni:IMAGE_TAG
         

Replace the following variables: 
     * `CONTAINER_NAME`: name that you used for your container. For example, `my-omni-1`. 
     * `NEW_PASSWORD`: password assigned to the new container's `postgres` user after its creation. 
     * `DATA_DIR`: host directory path that your data is stored in. 
     * `HOST_PORT`: TCP port on the host machine that the container must publish its own port `5432` to. To use the PostgreSQL default port on the host machine as well, specify `5432`. 
     * `IMAGE_TAG`: use `17.5.0` for the latest Debian image or `17.5.0-ubi9` for the latest UBI image. 



### Docker

  1. If your AlloyDB Omni container is running, stop it. 
         
         docker stop CONTAINER_NAME

Replace the following variable: 
     * `CONTAINER_NAME`: name that you used for your container. For example, `my-omni-1`. 
  2. Set SELinux's mode to `permissive`. This lets you run your container and identify details about what access is required to mount an external data directory. 
         
         sudo setenforce 0

  3. Run your container with an external data directory. 
         
         docker run -d --name CONTAINER_NAME \
         -e POSTGRES_PASSWORD=NEW_PASSWORD \
         -v DATA_DIR:/var/lib/postgresql/data \
         -p HOST_PORT:5432 \
         --restart=always \
         google/alloydbomni:IMAGE_TAG
         

Replace the following variables: 
     * `CONTAINER_NAME`: name that you used for your container. For example, `my-omni-1`. 
     * `NEW_PASSWORD`: password assigned to the new container's `postgres` user after its creation. 
     * `DATA_DIR`: host directory path that your data is stored in. 
     * `HOST_PORT`: TCP port on the host machine that the container must publish its own port `5432` to. To use the PostgreSQL default port on the host machine as well, specify `5432`. 
     * `IMAGE_TAG`: use `17.5.0` for the latest Debian image or `17.5.0-ubi9` for the latest UBI image. 
  4. If not already installed, install `policycoreutils-python-utils` through your package manager. This package provides utilities necessary to manage SELinux policies. 
  5. If your external data directory isn't within your home directory, set the appropriate SELinux context. 
         
         sudo semanage fcontext -a -t container_file_t "DATA_DIR"
         
         sudo restorecon -Rv "DATA_DIR"

Replace the following variable: 
     * `DATA_DIR`: host directory path that your data is stored in. 
  6. Use `ausearch` to get information about the additional permission requirements. 
         
         sudo ausearch -c 'postgres' --raw > postgres.avc

  7. Create a SELinux security profile based on your AlloyDB Omni container and `ausearch` permission information. 
         
         docker inspect CONTAINER_NAME | sudo udica --append-rules postgres.avc CONTAINER_NAME

Replace the following variable: 
     * `CONTAINER_NAME`: name that you used for your container. For example, `my-omni-1`. 
  8. Load the SELinux module. 
         
         sudo semodule -i CONTAINER_NAME.cil /usr/share/udica/templates/{base_container.cil,net_container.cil}

Replace the following variable: 
     * `CONTAINER_NAME`: name that you used for your container. For example, `my-omni-1`. 
  9. Enable `mmap`. 
         
         sudo setsebool -P domain_can_mmap_files 1

  10. Stop and remove your AlloyDB Omni container. 
         
         docker stop CONTAINER_NAME && docker rm CONTAINER_NAME

Replace the following variable: 
     * `CONTAINER_NAME`: name that you used for your container. For example, `my-omni-1`. 
  11. Set SELinux's mode to `enforcing`. 
         
         sudo setenforce 1

  12. Re-create your AlloyDB Omni container. 
         
         docker run -d --name CONTAINER_NAME \
         -e POSTGRES_PASSWORD=NEW_PASSWORD \
         -v DATA_DIR:/var/lib/postgresql/data \
         -p HOST_PORT:5432 \
         --restart=always \
         --security-opt label=type:CONTAINER_NAME.process \
         google/alloydbomni:IMAGE_TAG
         

Replace the following variables: 
     * `CONTAINER_NAME`: name that you used for your container. For example, `my-omni-1`. 
     * `NEW_PASSWORD`: password assigned to the new container's `postgres` user after its creation. 
     * `DATA_DIR`: host directory path that your data is stored in. 
     * `HOST_PORT`: TCP port on the host machine that the container must publish its own port `5432` to. To use the PostgreSQL default port on the host machine as well, specify `5432`. 
     * `IMAGE_TAG`: use `17.5.0` for the latest Debian image or `17.5.0-ubi9` for the latest UBI image. 



### Podman

  1. If your AlloyDB Omni container is running, stop it. 
         
         podman stop CONTAINER_NAME

Replace the following variable: 
     * `CONTAINER_NAME`: name that you used for your container. For example, `my-omni-1`. 
  2. Set SELinux's mode to `permissive`. This lets you run your container and identify details about what access is required to mount an external data directory. 
         
         setenforce 0

  3. Run your container with an external data directory. 
         
         podman run -d --name CONTAINER_NAME \
         -e POSTGRES_PASSWORD=NEW_PASSWORD \
         -v DATA_DIR:/var/lib/postgresql/data \
         -p HOST_PORT:5432 \
         --restart=always \
         docker.io/google/alloydbomni:IMAGE_TAG
         

Replace the following variables: 
     * `CONTAINER_NAME`: name that you used for your container. For example, `my-omni-1`. 
     * `NEW_PASSWORD`: password assigned to the new container's `postgres` user after its creation. 
     * `DATA_DIR`: host directory path that your data is stored in. 
     * `HOST_PORT`: TCP port on the host machine that the container must publish its own port `5432` to. To use the PostgreSQL default port on the host machine as well, specify `5432`. 
     * `IMAGE_TAG`: use `17.5.0` for the latest Debian image or `17.5.0-ubi9` for the latest UBI image. 
  4. If not already installed, install `policycoreutils-python-utils` through your package manager. This package provides utilities necessary to manage SELinux policies. 
  5. For your external data directory, set the appropriate SELinux context. 
         
         semanage fcontext -a -t container_file_t "DATA_DIR"
         
         restorecon -Rv "DATA_DIR"

Replace the following variable: 
     * `DATA_DIR`: host directory path that your data is stored in. 
  6. Use `ausearch` to get information about the additional permission requirements. 
         
         ausearch -c 'postgres' --raw > postgres.avc

  7. Create a SELinux security profile based on your AlloyDB Omni container and `ausearch` permission information. 
         
         podman inspect CONTAINER_NAME | udica --append-rules postgres.avc CONTAINER_NAME

Replace the following variable: 
     * `CONTAINER_NAME`: name that you used for your container. For example, `my-omni-1`. 
  8. Load the SELinux module. 
         
         semodule -i CONTAINER_NAME.cil /usr/share/udica/templates/{base_container.cil,net_container.cil}

Replace the following variable: 
     * `CONTAINER_NAME`: name that you used for your container. For example, `my-omni-1`. 
  9. Enable `mmap`. 
         
         setsebool -P domain_can_mmap_files 1

  10. Stop and remove your AlloyDB Omni container. 
         
         podman stop CONTAINER_NAME && docker rm CONTAINER_NAME

Replace the following variable: 
     * `CONTAINER_NAME`: name that you used for your container. For example, `my-omni-1`. 
  11. Set SELinux's mode to `enforcing`. 
         
         setenforce 1

  12. Re-create your AlloyDB Omni container. 
         
         podman run -d --name CONTAINER_NAME \
         -e POSTGRES_PASSWORD=NEW_PASSWORD \
         -v DATA_DIR:/var/lib/postgresql/data \
         -p HOST_PORT:5432 \
         --restart=always \
         --security-opt label=type:CONTAINER_NAME.process \
         docker.io/google/alloydbomni:IMAGE_TAG
         

Replace the following variables: 
     * `CONTAINER_NAME`: name that you used for your container. For example, `my-omni-1`. 
     * `NEW_PASSWORD`: password assigned to the new container's `postgres` user after its creation. 
     * `DATA_DIR`: host directory path that your data is stored in. 
     * `HOST_PORT`: TCP port on the host machine that the container must publish its own port `5432` to. To use the PostgreSQL default port on the host machine as well, specify `5432`. 
     * `IMAGE_TAG`: use `17.5.0` for the latest Debian image or `17.5.0-ubi9` for the latest UBI image. 



### Podman

  1. If your AlloyDB Omni container is running, stop it. 
         
         podman stop CONTAINER_NAME

Replace the following variable: 
     * `CONTAINER_NAME`: name that you used for your container. For example, `my-omni-1`. 
  2. Set SELinux's mode to `permissive`. This lets you run your container and identify details about what access is required to mount an external data directory. 
         
         sudo setenforce 0

  3. Run your container with an external data directory. 
         
         podman run -d --name CONTAINER_NAME \
         -e POSTGRES_PASSWORD=NEW_PASSWORD \
         -v DATA_DIR:/var/lib/postgresql/data \
         -p HOST_PORT:5432 \
         --restart=always \
         docker.io/google/alloydbomni:IMAGE_TAG
         

Replace the following variables: 
     * `CONTAINER_NAME`: name that you used for your container. For example, `my-omni-1`. 
     * `NEW_PASSWORD`: password assigned to the new container's `postgres` user after its creation. 
     * `DATA_DIR`: host directory path that your data is stored in. 
     * `HOST_PORT`: TCP port on the host machine that the container must publish its own port `5432` to. To use the PostgreSQL default port on the host machine as well, specify `5432`. 
     * `IMAGE_TAG`: use `17.5.0` for the latest Debian image or `17.5.0-ubi9` for the latest UBI image. 
  4. If not already installed, install `policycoreutils-python-utils` through your package manager. This package provides utilities necessary to manage SELinux policies. 
  5. For your external data directory, set the appropriate SELinux context. 
         
         sudo semanage fcontext -a -t container_file_t "DATA_DIR"
         
         sudo restorecon -Rv "DATA_DIR"

Replace the following variable: 
     * `DATA_DIR`: host directory path that your data is stored in. 
  6. Use `ausearch` to get information about the additional permission requirements. 
         
         sudo ausearch -c 'postgres' --raw > postgres.avc

  7. Create a SELinux security profile based on your AlloyDB Omni container and `ausearch` permission information. 
         
         podman inspect CONTAINER_NAME | sudo udica --append-rules postgres.avc CONTAINER_NAME

Replace the following variable: 
     * `CONTAINER_NAME`: name that you used for your container. For example, `my-omni-1`. 
  8. Load the SELinux module. 
         
         sudo semodule -i CONTAINER_NAME.cil /usr/share/udica/templates/{base_container.cil,net_container.cil}

Replace the following variable: 
     * `CONTAINER_NAME`: name that you used for your container. For example, `my-omni-1`. 
  9. Enable `mmap`. 
         
         sudo setsebool -P domain_can_mmap_files 1

  10. Stop and remove your AlloyDB Omni container. 
         
         podman stop CONTAINER_NAME && docker rm CONTAINER_NAME

Replace the following variable: 
     * `CONTAINER_NAME`: name that you used for your container. For example, `my-omni-1`. 
  11. Set SELinux's mode to `enforcing`. 
         
         sudo setenforce 1

  12. Re-create your AlloyDB Omni container. 
         
         podman run -d --name CONTAINER_NAME \
         -e POSTGRES_PASSWORD=NEW_PASSWORD \
         -v DATA_DIR:/var/lib/postgresql/data \
         -p HOST_PORT:5432 \
         --restart=always \
         --security-opt label=type:CONTAINER_NAME.process \
         docker.io/google/alloydbomni:IMAGE_TAG
         

Replace the following variables: 
     * `CONTAINER_NAME`: name that you used for your container. For example, `my-omni-1`. 
     * `NEW_PASSWORD`: password assigned to the new container's `postgres` user after its creation. 
     * `DATA_DIR`: host directory path that your data is stored in. 
     * `HOST_PORT`: TCP port on the host machine that the container must publish its own port `5432` to. To use the PostgreSQL default port on the host machine as well, specify `5432`. 
     * `IMAGE_TAG`: use `17.5.0` for the latest Debian image or `17.5.0-ubi9` for the latest UBI image. 



## Enable ulimits

The [ulimit](https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/x4733.html) parameters specify process limits that the Docker or Podman container can use. For optimal performance, we recommend that you set the following ulimits:

  * `nice=-20:-20`: AlloyDB Omni adjusts process priorities to allow critical PostgreSQL processes to run with higher priority. The higher priority gives the processes a bigger allocation of available CPUs. To adjust process priorities, specify `--ulimit=nice=-20:-20`, which removes limitations for the AlloyDB Omni container.

  * `memlock=-1:-1`: AlloyDB Omni performs [automatic memory management](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/automatic-memory-management). Setting `--ulimit=memlock=-1:-1` allows the database to better control how memory pages are swapped in and out, which can result in better performance.




### Docker
    
    
    docker run -d --name CONTAINER_NAME \
    -e POSTGRES_PASSWORD=NEW_PASSWORD \
    --ulimit=nice=-20:-20 --ulimit=memlock=-1:-1 \
    -p HOST_PORT:5432 \
    --restart=always \
    google/alloydbomni:IMAGE_TAG
    

### Docker
    
    
    docker run -d --name CONTAINER_NAME \
    -e POSTGRES_PASSWORD=NEW_PASSWORD \
    --ulimit=nice=-20:-20 --ulimit=memlock=-1:-1 \
    -p HOST_PORT:5432 \
    --restart=always \
    google/alloydbomni:IMAGE_TAG
    

### Podman
    
    
    podman run -d --name CONTAINER_NAME \
    -e POSTGRES_PASSWORD=NEW_PASSWORD \
    --ulimit=nice=-20:-20 --ulimit=memlock=-1:-1 \
    -p HOST_PORT:5432 \
    --restart=always \
    docker.io/google/alloydbomni:IMAGE_TAG
    

### Podman
    
    
    podman run -d --name CONTAINER_NAME \
    -e POSTGRES_PASSWORD=NEW_PASSWORD \
    --ulimit=nice=-20:-20 --ulimit=memlock=-1:-1 \
    -p HOST_PORT:5432 \
    --restart=always \
    docker.io/google/alloydbomni:IMAGE_TAG
    

Replace the following variables:

  * `CONTAINER_NAME`: Name you used for your container. For example, `my-omni-1`.
  * `NEW_PASSWORD`: Password assigned to the new container's `postgres` user after its creation.
  * `HOST_PORT`: TCP port on the host machine that the container should publish its own port `5432` to. To use the PostgreSQL default port on the host machine as well, specify `5432`.
  * `IMAGE_TAG`: Use `AlloyDB Omni` for the latest Debian image or `AlloyDB Omni-ubi` for the latest UBI image.



## Specify a logging driver

By default, Docker and Podman don't perform log rotations. This can use up a lot of disk space, and eventually lead to disk space exhaustion. To use a different logging driver, you can specify the `--log-driver` field. For example, to log to `journald`:

### Docker
    
    
    docker run -d --name CONTAINER_NAME \
    -e POSTGRES_PASSWORD=NEW_PASSWORD \
    --log-driver=journald \
    -p HOST_PORT:5432 \
    --restart=always \
    google/alloydbomni:IMAGE_TAG
    

### Docker
    
    
    docker run -d --name CONTAINER_NAME \
    -e POSTGRES_PASSWORD=NEW_PASSWORD \
    --log-driver=journald \
    -p HOST_PORT:5432 \
    --restart=always \
    google/alloydbomni:IMAGE_TAG
    

### Podman
    
    
    podman run -d --name CONTAINER_NAME \
    -e POSTGRES_PASSWORD=NEW_PASSWORD \
    --log-driver=journald \
    -p HOST_PORT:5432 \
    --restart=always \
    docker.io/google/alloydbomni:IMAGE_TAG
    

### Podman
    
    
    podman run -d --name CONTAINER_NAME \
    -e POSTGRES_PASSWORD=NEW_PASSWORD \
    --log-driver=journald \
    -p HOST_PORT:5432 \
    --restart=always \
    docker.io/google/alloydbomni:IMAGE_TAG
    

Replace the following variables:

  * `CONTAINER_NAME`: Name you used for your container. For example, `my-omni-1`.
  * `NEW_PASSWORD`: Password assigned to the new container's `postgres` user after its creation.
  * `HOST_PORT`: TCP port on the host machine that the container should publish its own port `5432` to. To use the PostgreSQL default port on the host machine as well, specify `5432`.
  * `IMAGE_TAG`: Use `17.5.0` for the latest Debian image or use `17.5.0-ubi` for the latest UBI image.



For more information about logging drivers, refer to Docker's [Configure logging drivers](https://docs.docker.com/config/containers/logging/configure/) and Podman's [`podman-run`](https://docs.podman.io/en/v5.1.1/markdown/podman-run.1.html#log-driver-driver) documentation.

## Mount a shared memory volume

If you plan to use the AlloyDB [columnar engine](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/columnar-engine/configure) with AlloyDB Omni, we recommend making shared memory available to the AlloyDB Omni container. The method for doing this differs depending upon your host operating system, as shown in the following examples.

### Linux

To make shared memory available to the container, mount `/dev/shm`:

### Docker
    
    
    docker run -d --name CONTAINER_NAME \
    -e POSTGRES_PASSWORD=NEW_PASSWORD \
    -v /dev/shm:/dev/shm \
    -p HOST_PORT:5432 \
    --restart=always \
    google/alloydbomni:IMAGE_TAG
    

### Docker
    
    
    docker run -d --name CONTAINER_NAME \
    -e POSTGRES_PASSWORD=NEW_PASSWORD \
    -v /dev/shm:/dev/shm \
    -p HOST_PORT:5432 \
    --restart=always \
    google/alloydbomni:IMAGE_TAG
    

### Podman
    
    
    podman run -d --name CONTAINER_NAME \
    -e POSTGRES_PASSWORD=NEW_PASSWORD \
    -v /dev/shm:/dev/shm \
    -p HOST_PORT:5432 \
    --restart=always \
    docker.io/google/alloydbomni:IMAGE_TAG
    

### Podman
    
    
    podman run -d --name CONTAINER_NAME \
    -e POSTGRES_PASSWORD=NEW_PASSWORD \
    -v /dev/shm:/dev/shm \
    -p HOST_PORT:5432 \
    --restart=always \
    docker.io/google/alloydbomni:IMAGE_TAG
    

Replace the following variables:

  * `CONTAINER_NAME`: Name you used for your container. For example, `my-omni-1`.
  * `NEW_PASSWORD`: Password assigned to the new container's `postgres` user after its creation.
  * `HOST_PORT`: TCP port on the host machine that the container should publish its own port `5432` to. To use the PostgreSQL default port on the host machine as well, specify `5432`.
  * `IMAGE_TAG`: Use `17.5.0` for the latest Debian image or use `17.5.0-ubi` for the latest UBI image.



### macOS

To make shared memory available to the container, include the `--shm-size` flag:

### Docker
    
    
    docker run -d --name CONTAINER_NAME \
    -e POSTGRES_PASSWORD=NEW_PASSWORD \
    --shm-size=SHARED_MEMORY_SIZE \
    -p HOST_PORT:5432 \
    --restart=always \
    google/alloydbomni:IMAGE_TAG
    

### Docker
    
    
    docker run -d --name CONTAINER_NAME \
    -e POSTGRES_PASSWORD=NEW_PASSWORD \
    --shm-size=SHARED_MEMORY_SIZE \
    -p HOST_PORT:5432 \
    --restart=always \
    google/alloydbomni:IMAGE_TAG
    

### Podman
    
    
    podman run -d --name CONTAINER_NAME \
    -e POSTGRES_PASSWORD=NEW_PASSWORD \
    --shm-size=SHARED_MEMORY_SIZE \
    -p HOST_PORT:5432 \
    --restart=always \
    docker.io/google/alloydbomni:IMAGE_TAG
    

### Podman
    
    
    podman run -d --name CONTAINER_NAME \
    -e POSTGRES_PASSWORD=NEW_PASSWORD \
    --shm-size=SHARED_MEMORY_SIZE \
    -p HOST_PORT:5432 \
    --restart=always \
    docker.io/google/alloydbomni:IMAGE_TAG
    

Replace the following variables:

  * `CONTAINER_NAME`: Name you used for your container. For example, `my-omni-1`.
  * `NEW_PASSWORD`: Password assigned to the new container's `postgres` user after its creation.
  * `SHARED_MEMORY_SIZE`: Size to set for `/dev/shm` on the container, in the format described on [Running containers](https://docs.docker.com/engine/reference/run/). For example, to specify one gigabyte, use the value `1g`.
  * `HOST_PORT`: TCP port on the host machine that the container should publish its own port `5432` to. To use the PostgreSQL default port on the host machine as well, specify `5432`.
  * `IMAGE_TAG`: Use `17.5.0` for the latest Debian image or `17.5.0-ubi` for the latest UBI image.



We recommend that you set the shared memory size to a number of megabytes equal to at least your database's value of the [`google_job_scheduler.max_parallel_workers_per_job` flag](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/reference/columnar-engine-flags#max-parallel-workers-per-job), times 250. For more information about the columnar engine, see [Configure the columnar engine in AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/columnar-engine/configure).

For example, if the `google_job_scheduler.max_parallel_workers_per_job` database flag is set to its default value of `2`, consider adding a flag of `--shm-size=500m` or greater when starting your database server.

For more information about the `--shm-size` flag, see [Running containers](https://docs.docker.com/engine/reference/run/).

## Enable extensions

The list of extensions available in AlloyDB Omni is available in [Supported database extensions](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/reference/extensions). Although PostGIS and Orafce are not included with AlloyDB Omni, they can both be installed by following instructions:

  * [Install PostGIS for AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/install-postgis)
  * [Install Orafce for AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/install-orafce)



Installed extensions are enabled using standard PostgreSQL `CREATE EXTENSION` statements as detailed in [Enable an extension](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/reference/extensions#enable).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
