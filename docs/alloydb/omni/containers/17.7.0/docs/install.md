---
url: https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/install/
title: Customize your AlloyDB Omni installation \u00a0|\u00a0 AlloyDB Omni using containers: 17.7.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:47:03.822346+00:00
---

# Customize your AlloyDB Omni installation  |  AlloyDB Omni using containers: 17.7.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/install/

This page documents AlloyDB Omni version **17.7.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Containers: 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/overview)



Send feedback 

#  Customize your AlloyDB Omni installation Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 17.7.0keyboard_arrow_down

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



This page describes how to customize your AlloyDB Omni installation, which supports different forms of customization. This page shows some common customizations.

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

  * `CONTAINER_NAME`: Name of your AlloyDB Omni container—for example, `my-omni-1`.



### Connect remotely
    
    
    /usr/lib/postgresql/17/bin/psql -U postgres -p HOST_PORT -h IP_ADDRESS_OR_FQDN
    

Replace the following variables:

  * `HOST_PORT`: TCP port you used during installation.
  * `IP_ADDRESS_OR_FQDN`: IP address or fully-qualified domain name for the host where AlloyDB Omni is running.



## Enable extensions

The list of extensions available in AlloyDB Omni is available in [Supported database extensions](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/reference/extensions). Although PostGIS and Orafce are not included with AlloyDB Omni, they can both be installed by following instructions:

  * [Install PostGIS for AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/install-postgis)
  * [Install Orafce for AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/install-orafce)



Installed extensions are enabled using standard PostgreSQL `CREATE EXTENSION` statements as detailed in [Enable an extension](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/reference/extensions#enable).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
