---
url: https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/manage/
title: Manage and monitor AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni using RPM: 18.1.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:21:10.902874+00:00
---

# Manage and monitor AlloyDB Omni  |  AlloyDB Omni using RPM: 18.1.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/manage/

This page documents AlloyDB Omni version **18.1.0** using the **RPM** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM: 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/overview)



Send feedback 

#  Manage and monitor AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

For information about access to this release, see the [ access request page](https://forms.gle/zxuHekMtV67Bw9Av9). 

Select a documentation version: 18.1.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/manage)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/manage)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/manage)
  * [ 18.1.1 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/manage)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/manage)

This page describes how to manage AlloyDB Omni user roles, monitor the activity of your AlloyDB Omni server, and update or remove your AlloyDB Omni installation. 

## Manage user roles

AlloyDB Omni uses the following roles:

  * AlloyDB Omni includes a superuser role named `alloydbadmin`, and a non-superuser role named `alloydbmetadata`.

  * The default `postgres` user has a superuser role.

  * All other predefined user roles have no privileges. They are reserved for potential uses in the future.




### Set up an AlloyDB Omni database

We recommend following these steps when setting up an AlloyDB Omni database:

  1. Define or import your databases using the `postgres` user role. In a new installation, this role has superuser privileges.

  2. Create new user roles that have the correct level of access to your application's tables, again using the `postgres` user role.

  3. Configure your application to connect to the database using these new, limited-access roles.




You can create and define as many new user roles as you need. Don't modify or delete any of the user roles that comes with AlloyDB Omni.

For more information, see [Manage AlloyDB Omni users and roles](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/database-users/manage-users).

## Install and start the AlloyDB Omni monitor

The AlloyDB Omni monitor is an optional component that exposes metrics at an endpoint. You can configure monitoring servers to fetch metric samples from this endpoint and integrate them into your monitoring stack.

To install and start the monitor, take the following steps on each host running the AlloyDB Omni service:

  1. Install the monitor package:
         
         sudo dnf install alloydbomni_monitor

  2. Enable and start the monitor service:
         
         sudo systemctl enable alloydbomni_monitor
          sudo systemctl start alloydbomni_monitor




## Configure the AlloyDB Omni monitor

By default, the monitor is configured to work with the standard AlloyDB Omni service name and data directory. If your installation uses custom values, you must configure the monitor using a systemd override file.

  1. Check the default configuration in `/usr/lib/systemd/system/alloydbomni_monitor.service`:

     * `OMNI_SERVICE_NAME`: The name of the AlloyDB Omni systemd service, which defaults to `alloydbomni18`.
     * `PG_DATA_DIR`: The path to the database data directory, which defaults to `/var/lib/postgresql/18/data`.

To find your database data directory, run the following command:
           
           sudo -u postgres /usr/lib/postgresql/18/bin/psql -h localhost -c "SHOW data_directory;"

  2. If your installation uses values different from the defaults, create an override directory and an `override.conf` file:
         
         sudo mkdir -p /etc/systemd/system/alloydbomni_monitor.service.d
          sudo touch /etc/systemd/system/alloydbomni_monitor.service.d/override.conf

  3. Add the following content to `/etc/systemd/system/alloydbomni_monitor.service.d/override.conf`. Replace the placeholder values with your custom configuration:
         
         [Service]
          Environment="OMNI_SERVICE_NAME=SERVICE_NAME"
          Environment="PG_DATA_DIR=PG_DATA_DIR"
         

Replace the following:

     * `SERVICE_NAME`: The name of your AlloyDB Omni systemd service (for example, `alloydbomni18`).
     * `PG_DATA_DIR`: The path to your database data directory. For example, if you installed AlloyDB Omni using the standalone RPM with `PGDATA=/data`, specify `/data`.
  4. Reload the systemd daemon:
         
         sudo systemctl daemon-reload

  5. Restart the monitor service:
         
         sudo systemctl restart alloydbomni_monitor




## Verify the AlloyDB Omni monitor

  1. Verify that the monitor service is running:
         
         sudo systemctl status alloydbomni_monitor

  2. Verify that the monitor is exposing metrics by making an HTTP call to the metrics endpoint:
         
         curl http://localhost:9187/metrics




## Monitor limitations

Metrics related to CPU and memory limits of AlloyDB Omni are visible only if your environment has set CPU and memory limits for the `alloydbomni18` systemd service. The following metrics are affected:

  * `alloydb_omni_memory_limit_byte`
  * `alloydb_omni_memory_available_byte`
  * `alloydb_omni_node_cpu_mcpu`



If you want to set CPU and memory limits, configure a systemd unit file. The following example configures `CPUQuota` to `90%` and `MemoryMax` to `90%`. For more information about systemd unit files, see [Working with systemd unit files](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/using_systemd_unit_files_to_customize_and_optimize_your_system/assembly_working-with-systemd-unit-files_working-with-systemd).

  1. Create a systemd override configuration file.

Create an `override.conf` file in the `/etc/systemd/system/alloydbomni18.service.d` directory.

  2. Add the following content to the `override.conf` file:
         
         [Service]
          CPUQuota=90%
          MemoryMax=90%
         

  3. Reload the systemd daemon:
         
         sudo systemctl daemon-reload

  4. Restart the AlloyDB Omni service:
         
         sudo systemctl restart alloydbomni18




## Monitor AlloyDB Omni

Monitoring your AlloyDB Omni installation includes fetching and analyzing AlloyDB Omni metrics.

To retrieve AlloyDB Omni logs, run:
    
    
      sudo journalctl -u alloydbomni18

### View system metrics using System Insights

You can monitor real-time and historical infrastructure metrics for your AlloyDB Omni instances using **System Insights** in the AlloyDB Omni web user interface. **System Insights** queries the Prometheus metrics exported by the AlloyDB Omni monitoring agent to display resource utilization charts.

**Note:** **System Insights** isn't supported when deploying AlloyDB Omni using containers because a containerized monitoring agent isn't available for container deployments.

To view system metrics in the web UI, complete the following steps:

  1. [Connect to the web UI](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/connect-web-ui) and select your cluster.
  2. In the navigation menu, click **System Insights**.
  3. Optional: In a multi-node cluster, use the **Filter by: Instances** list to select a specific instance endpoint (for example, `localhost:9187`).
  4. Select a time window (**1 hour** , **6 hours** , **1 day** , or **7 days**) to adjust the observation period across all charts.
  5. Review the system telemetry charts: 
     * **CPU Usage** : Displays the percentage of CPU utilization over time.
     * **Memory Usage** : Displays the percentage of allocated memory in use over time.
     * **Memory Available** : Displays the percentage of free memory available over time.
     * **Memory Limit** : Displays the configured memory quota (in GB) for the instance.
     * **Storage and disk I/O** : Displays six additional charts tracking storage usage, storage limit, number of disk reads, bytes read, number of disk writes, and bytes written.



## Uninstall AlloyDB Omni

**Caution:** Following these steps permanently deletes all AlloyDB Omni databases from your machine.

To uninstall AlloyDB Omni, run:
    
    
      sudo dnf remove alloydbomni_monitor

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
