---
url: https://docs.cloud.google.com/stackdriver/docs/solutions/agents/logging/migrating-to-fluentd/
title: Migrate from the legacy Logging agent to upstream Fluentd \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:15.042371+00:00
---

# Migrate from the legacy Logging agent to upstream Fluentd  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/solutions/agents/logging/migrating-to-fluentd/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Reference ](https://docs.cloud.google.com/stackdriver/docs/reference/api-overview)



Send feedback 

#  Migrate from the legacy Logging agent to upstream Fluentd Stay organized with collections  Save and categorize content based on your preferences. 

If you are using the legacy Logging agent and have a highly customized configuration, then we recommend migrating to open-source [Fluentd](https://www.fluentd.org/). You can configure Fluentd to preserve the behavior of your Logging agent environment without disrupting the collection of your logs by Cloud Logging. This document describes the migration process.

## Feature comparison

The following table provides a parity comparison of key functionalities between the legacy Logging agent and upstream Fluentd.

Features | Legacy Logging agent | Upstream Fluentd  
---|---|---  
Log ingestion to Cloud Logging | Yes | Yes  
Standard system logs (syslog) | Yes | Yes  
Preconfigured third party application input | Yes | Yes †  
Structured (JSON) and unstructured (text) log handling | Yes | Yes  
Multiline exception merge | Yes | Yes  
Google Cloud metadata enrichment | Yes | Yes  
Kubernetes metadata enrichment | Yes | Yes  
Unique log entry IDs | Yes | Yes  
Log field transformation | Yes | Yes  
Severity mapping | Yes | Yes  
Authentication (ADC and Service Account Keys) | Yes | Yes  
REST and gRPC transport protocols | Yes | Yes  
Monitoring integration | Yes | Yes  
  
† Although the [google-fluentd-catch-all- config](https://github.com/GoogleCloudPlatform/fluentd-catch-all-config) package isn't included in the standard installation of upstream Fluentd and plugins, you can maintain the preconfigured input functionality by following the migration steps detailed in this guide. 

## Before you begin

Before starting the migration, make sure that you have the following:

  * A [supported VM instance](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/logging#supported_vms) in a Google Cloud project.
  * Credentials on the VM instance that authorize communication with Cloud Logging. Compute Engine VM instances generally have the correct credentials by default. To check if you have the proper credentials, run the [Authorize the Logging agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/logging/authorization) procedures.



## Migrate to Fluentd

This section outlines the steps to migrate to the upstream Fluentd version, maintaining the key functionalities provided by the legacy Logging agent.

To migrate your setup, complete the following steps:

  1. Shut down the legacy Logging agent
  2. Install a stable version of fluentd-package
  3. Install Google Cloud Platform plugins
  4. Migrate your input plugins configuration files
  5. Update syslog configuration
  6. Update your Fluentd configuration file
  7. Validate that the Fluentd agent is running correctly
  8. Uninstall the legacy Logging agent

**Note:** This section contains a Linux command example. If you use Windows, adapt the command steps to that environment.

### Shut down the legacy Logging agent

Before you install the upstream Fluentd agent, you must stop the legacy Logging agent to avoid conflicts. To avoid losing any pending logs during the migration, make sure you flush all buffered logs at shutdown.

To gracefully shut down the legacy Logging agent, do the following:

  1. Open a terminal connection to your VM instance using SSH or a similar tool and, make sure you have sudo access.
  2. To flush any buffered logs before shutting down the legacy Logging agent, enable the `flush_at_shutdown` option:

     1. Update the `/etc/google-fluentd/google-fluentd.conf` file to set the `flush_at_shutdown` flag to `true`:
            
            # Configure the agent to flush all buffer chunks on shutdown
            <match **>
              @type google_cloud
              flush_at_shutdown true
            </match>
            

     2. Restart the agent to apply the configuration changes:
            
            sudo service google-fluentd restart
            

  3. Stop the legacy Logging agent:
         
         sudo service google-fluentd stop
         




### Install a stable version of fluentd-package

Install a stable distribution of Fluentd (`fluentd-package`) in your VM instances. For instructions, see Fluentd [Install fluent-package](https://docs.fluentd.org/installation/install-fluent-package) documentation.

### Install Google Cloud Platform plugins

To enable Fluentd to interact with Cloud Logging and handle specific log formats, install the following plugins:

  1. If not already installed, install the build tools for extension compilation:

### Debian or Ubuntu

Run the following command on Debian or Ubuntu:
         
         sudo apt-get update
         sudo apt-get install -y build-essential
         

### CentOS or RHEL

Run the following command on CentOS or RHEL:
         
         sudo yum update
         sudo yum groupinstall -y "Development Tools"
         

  2. Install the `fluent-plugin-google-cloud` plugin:
         
         sudo fluent-gem install fluent-plugin-google-cloud
         

  3. Install the `fluent-plugin-detect-exceptions` plugin:
         
         sudo fluent-gem install fluent-plugin-detect-exceptions
         

  4. Optional: if your legacy Logging agent deployment collects logs from applications running within a Kubernetes cluster, then install the `fluent-plugin-kubernetes_metadata_filter` plugin:
         
         sudo fluent-gem install fluent-plugin-kubernetes_metadata_filter
         

  5. Optional: If your legacy Logging agent collects and exposes metrics in Prometheus format, then install the following gems:
         
         sudo fluent-gem install prometheus-client -v 0.9.0
         sudo fluent-gem install fluent-plugin-prometheus -v 1.4.0
         

**Warning:** Versions of `prometheus-client` that are equal or higher than 0.10.0 are incompatible, which will cause Fluentd to crash during startup.



### Migrate your input-plugin configuration files

To migrate your existing configuration and position files for your Fluentd installation, complete the following steps:

  1. Create directories for the Fluentd configuration and position files:
         
         # Create the destination directory for Fluentd configuration files
         sudo mkdir -p /etc/fluent/config.d
         
         # Create the destination directory for position files
         sudo mkdir -p /var/lib/fluent/pos
         

  2. Copy your `google-fluentd` configuration files to the configuration directory for Fluentd:
         
         sudo cp /etc/google-fluentd/config.d/* /etc/fluent/config.d/
         

  3. Copy all the position (`.pos`) files used by `google-fluentd` to the position-file directory for Fluentd:
         
         sudo cp /var/lib/google-fluentd/pos/*.pos /var/lib/fluent/pos/
         

The position files are used to track reading positions in log files. Migrating them lets Fluentd start at the same point google-fluentd was using.

  4. Update the `pos_file` path in your new Fluentd configuration files to point to the new position-file directory:
         
         sudo sed -i 's#/var/lib/google-fluentd#/var/lib/fluent#g' /etc/fluent/config.d/*.conf
         

  5. Grant the Fluentd service user ,`_fluentd`, read and write access to the `/var/lib/fluent/` directory:
         
         sudo chown -R _fluentd:_fluentd /var/lib/fluent/
         

  6. Grant the `_fluentd` user read access to syslog files:
         
         sudo usermod -a -G adm _fluentd
         




### Update syslog configuration

Upstream Fluentd runs as the unprivileged user, which can't bind to privileged ports numbered less than 1024. If your legacy Logging agent setup includes network-based syslog collection by using `@type syslog` on `port 514`, you must adjust the configuration.

To update the port configuration, do the following:

  1. Replace the entire content of the `/etc/fluent/config.d/syslog_endpoint.conf` file with the following configuration:
         
         sudo tee /etc/fluent/config.d/syslog_endpoint.conf > /dev/null <<EOF
         <source>
           @type syslog
           port 5140
           <transport tcp>
           </transport>
           bind 127.0.0.1
           tag syslog
         </source>
         EOF
         

  2. Create or modify the `/etc/rsyslog.d/40-fluentd-forward.conf` file to forward syslog messages to the new Fluentd port:
         
         sudo tee /etc/rsyslog.d/40-fluentd-forward.conf > /dev/null <<EOF
         # Forward all syslog messages to Fluentd on localhost:5140 via TCP
         *.* @@127.0.0.1:5140
         EOF
         

  3. Restart the `rsyslog` service to apply the changes:
         
         sudo systemctl restart rsyslog.service
         




### Update the main Fluentd configuration file

Configure the upstream Fluentd agent by replicating your settings from the agent's configuration file, `google-fluentd.conf`, to the main Fluentd configuration file, located at `/etc/fluent/fluentd.conf`.

**Note:** By installing the Google plugins, the upstream version of Fluentd supports all features of the legacy Logging agent. For further information, see [Configure the Logging agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/logging/configuration).

To configure upstream Fluentd agent, complete the following steps:

  1. Copy the entire contents of the `google-fluentd.conf` file to overwrite the default upstream Fluentd configuration file:
         
         sudo cp /etc/google-fluentd/google-fluentd.conf /etc/fluent/fluentd.conf
         

  2. Update the `buffer_path` in your Fluentd configuration files to point to the new Fluentd directory:
         
         sudo sed -i 's#/var/log/google-fluentd#/var/log/fluent#g' /etc/fluent/fluentd.conf
         

  3. Inspect the `fluentd.conf` file to confirm that the configuration includes the following:

     * `@include config.d/*.conf` is present to import all your input plugin configuration.
     * The `<match **> @type google_cloud` block is configured to stream logs to Cloud Logging.
     * The `buffer_path` within the output plugin now points to `/var/lib/fluent/`.
     * Any `pos_file` directive within input plugins point to `/var/lib/fluent/`.
  4. Execute a dry run to verify your Fluentd configuration:
         
         sudo fluentd -c /etc/fluent/fluentd.conf --dry-run
         

Check the resulting output for any `error` or `warn` alerts. You must resolve any identified issues prior to moving forward. For details on syntax changes, see [Configuration compatibility for upstream Fluentd](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/logging/fluentd-config-compatibility).

  5. Restart the Fluentd agent:
         
         sudo service fluentd restart
         




### Validate that the Fluentd agent is running correctly

After starting Fluentd, verify that logs are being successfully sent to Cloud Logging:

  1. Verify that Fluentd is running without errors:
         
         $ sudo service fluentd status
         

The service status should be active (running).

  2. Check Fluentd logs and ensure there are no errors or warnings:
         
         sudo tail -n 100 /var/log/fluent/fluentd.log | grep -iE "error|warn|failed|exception" || true
         

No errors or warnings should be listed.

  3. Check Cloud Logging to confirm logs are being received from your VM instance. For information on viewing your logs, see [Using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).




### Uninstall the legacy Logging agent

Only after you validate that the new Fluentd is successfully sending logs to Cloud Logging, remove the legacy Logging agent and its configuration files:

### Debian or Ubuntu
    
    
      sudo apt-get remove --purge google-fluentd
    

### CentOS or RHEL
    
    
      sudo yum remove google-fluentd
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
