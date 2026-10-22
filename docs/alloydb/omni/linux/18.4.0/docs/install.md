---
url: https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/install/
title: Customize your AlloyDB Omni installation \u00a0|\u00a0 AlloyDB Omni using RPM: 18.4.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:40:44.361735+00:00
---

# Customize your AlloyDB Omni installation  |  AlloyDB Omni using RPM: 18.4.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/install/

This page documents AlloyDB Omni version **18.4.0** using the **RPM** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM: 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/overview)



Send feedback 

#  Customize your AlloyDB Omni installation Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.4.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/install)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/install)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/install)
  * [ 18.1.1 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/install)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/install)



This page describes how to customize your AlloyDB Omni installation, which supports different forms of customization. This page shows some common customizations.

## Enable and disable AlloyDB Omni telemetry

AlloyDB Omni telemetry implements a lightweight client agent that collects a set of basic, pseudonymous metrics and sends them to a Google-managed endpoint.

**Note:** The AlloyDB Omni telemetry feature is enabled by default in the RPM packages.

Because AlloyDB Omni is a downloadable product that's offered at no charge, this telemetry provides Google with essential, non-personally identifiable information (non-PII) metrics regarding the generic adoption and deployment environments of running instances. This data helps inform product development and support prioritization.

Collected metrics include the following:

  * Unique installation ID (pseudonymized UUID)
  * AlloyDB Omni version and PostgreSQL major version
  * Host system information like CPU count, RAM, and uptime
  * Database configuration and feature usage information including database flags, Grand Unified Configuration or GUC parameters, and aggregated statistics related to the usage of AlloyDB Omni features and database capabilities



### Disable telemetry reporting

To prevent the telemetry agent from running and reporting usage metrics, set the PostgreSQL configuration parameter `omni_enable_telemetry` to `off`. You can disable the telemetry agent by setting the telemetry flag in the `postgresql.conf` file or by setting the flag at runtime using `ALTER SYSTEM`.

#### Set the telemetry flag in the postgresql.conf file

To modify the PostgreSQL configuration file, follow these steps:

  1. Locate the `postgresql.conf` file in your database's data directory. By default, this is `/var/lib/postgresql/MAJOR_VERSION/data`.
  2. Disable AlloyDB Omni telemetry.
         
         omni_enable_telemetry = off
         

  3. To apply the change, restart the AlloyDB Omni service. The telemetry agent stops collecting and sending usage metrics to Google.
         
         systemctl restart alloydbomniMAJOR_VERSION
         




#### Set the telemetry flag at runtime using ALTER SYSTEM

To set the telemetry flag and persist the change across restarts, follow these steps:

  1. Connect to your AlloyDB Omni instance using `psql`:
         
         /usr/lib/postgresql/18/bin/psql -h localhost -U postgres
         

  2. Run the following command:
         
         ALTER SYSTEM SET omni_enable_telemetry = 'off';
         

  3. Restart the database service to ensure the change is fully picked up by the background worker.
         
         systemctl restart alloydbomni18
         

The telemetry agent stops collecting and sending usage metrics to Google.




### Enable telemetry reporting

If you previously disabled AlloyDB Omni telemetry, you can re-enable it by setting the `omni_enable_telemetry` flag to `on`. You enable the telemetry agent by setting the flag in the `postgresql.conf` file or by setting the flag at runtime using `ALTER SYSTEM`.

#### Set the telemetry flag in the postgresql.conf file

  1. Locate the `postgresql.conf` file in your database's data directory.
  2. Set the following line:
         
         omni_enable_telemetry = on
         

  3. To apply the change, restart the AlloyDB Omni service.
         
         systemctl restart alloydbomni18
         




#### Set the telemetry flag at runtime using ALTER SYSTEM

  1. Connect to your AlloyDB Omni instance using `psql`.
  2. Run the following command:
         
         ALTER SYSTEM SET omni_enable_telemetry = 'on';
         

  3. To apply the change, restart the AlloyDB Omni service.
         
         systemctl restart alloydbomni18
         




### Check AlloyDB Omni telemetry status

You can check the status of the AlloyDB Omni telemetry agent, including whether it's enabled or disabled. You can also check telemetry agent activity.

#### Check if the telemetry agent is enabled or disabled

To check the status of the telemetry setting, follow these steps:

  1. Connect to your instance.
  2. Run the following:


    
    
    SHOW omni_enable_telemetry;
    

The output returns `on` or `off`, depending on whether you disabled or enabled AlloyDB Omni telemetry.

#### Check if the telemetry agent is running

To check whether the telemetry agent is running, run the following command in the host:
    
    
    ps -ef | grep "omni telemetry worker"
    

If telemetry is enabled and running, the output contains a line with the text `postgres: omni telemetry worker`.

#### Check telemetry agent activity

To check the activity of the telemetry agent, run the following command in the host:
    
    
    journalctl -u alloydbomni18 | grep telemetry
    

If the telemetry agent is running, the logs contain messages similar to the following:
    
    
    LOG:  [telemetry_agent_worker.cc:143]  Started telemetry worker
    LOG:  [telemetry_agent_worker.cc:161]  Running telemetry reporting agent
    telemetry_agent: Uploading telemetry data to https://cloud.google.com/log.
    

## Connect to your instance

Depending on your environment, you can connect to your AlloyDB Omni instance either locally or remotely.

### Connect locally

To connect to your AlloyDB Omni instance locally, run the following command: 
    
    
    /usr/lib/postgresql/18/bin/psql -U postgres -p HOST_PORT -h localhost
    

### Connect remotely
    
    
    /usr/lib/postgresql/18/bin/psql -U postgres -p HOST_PORT -h IP_ADDRESS_OR_FQDN
    

Replace the following variables:

  * `HOST_PORT`: TCP port you used during installation.
  * `IP_ADDRESS_OR_FQDN`: IP address or fully-qualified domain name for the host where AlloyDB Omni is running.



## Enable extensions

The list of extensions available in AlloyDB Omni is available in [Supported database extensions](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/reference/extensions). Although PostGIS and Orafce are not included with AlloyDB Omni, they can both be installed by following instructions:

  * [Install PostGIS for AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/install-postgis)
  * [Install Orafce for AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/install-orafce)



Installed extensions are enabled using standard PostgreSQL `CREATE EXTENSION` statements as detailed in [Enable an extension](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/reference/extensions#enable).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
