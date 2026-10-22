---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/viewing-serial-port-output/
title: Viewing serial port output \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:26.163714+00:00
---

# Viewing serial port output  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/viewing-serial-port-output/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Viewing serial port output Stay organized with collections  Save and categorize content based on your preferences. 

A Compute Engine instance has four virtual serial ports. The instance's operating system, BIOS, and other system-level entities often write output to the serial ports, which makes serial port output useful for troubleshooting crashes, failed boots, startup issues, or shutdown issues.

This page describes methods to _view_ serial port output, including using Cloud Logging to retain serial port output even after an instance is stopped. If you need to _send_ commands to a serial port while an instance is running, see [Interacting with the serial console](https://docs.cloud.google.com/compute/docs/instances/interacting-with-serial-console).

To view the serial port output for a compute instance that is running, use the Google Cloud console, the gcloud CLI, or REST. These methods only provide the most recent 1 MB of output per port. To view output exceeding 1 MB per port, or to view output from stopped instances, use Cloud Logging.

## Before you begin

  * If you want to log serial port output in Cloud Logging, familiarize yourself with [Cloud Logging](https://docs.cloud.google.com/logging).
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

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Networking requirements and limitations

To view serial port output using the Google Cloud console or to interact with the console, your client-side network and environment must meet the following requirements:

  * **TCP Port 9600** : If you use the **Serial port 1 (console)** link in the Google Cloud console, your network must allow outbound traffic on TCP port 9600 to connect to the serial console gateway.
  * **VPC Service Controls** : The interactive serial console isn't supported within VPC Service Controls perimeters.
  * **Private Google Access** : Private Google Access VIPs (`private.googleapis.com` or `restricted.googleapis.com`) don't support the SSH traffic required for the serial console. These VIPs only support HTTP-based protocols.



If your network restricts these ports or protocols, use Cloud Logging to view serial port logs instead, because it uses standard HTTPS (port 443).

### Troubleshooting SSH failures

If you're viewing serial port logs because you can't connect to your VM using SSH, see the [SSH troubleshooting guide](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-ssh-errors) for a list of common errors and remediation steps.

## Enabling and disabling serial port output logging

You can control whether your instances send serial port output to Cloud Logging by setting project- or instance-level metadata. You can also disable the feature for all of the users in your organization by setting an organization policy.

By default, serial port output logging to Cloud Logging is disabled. If you enable serial port output logging, Cloud Logging [provides the first 50 gibibytes (GiB) per month of logging for free](https://cloud.google.com/stackdriver/pricing) and retains logs for [30 days](https://docs.cloud.google.com/logging/quotas#logs_retention_periods).

**Note:** Serial port output is useful for troubleshooting VM crashes, failed boots, and startup or shutdown issues. Disabling these logs might limit Google's ability to troubleshoot such issues.

### Setting project and instance metadata

If serial port output logging to Cloud Logging isn't constrained for your organization, then you can enable or disable it for projects and for individual compute instances by setting the `serial-port-logging-enable` metadata entry to `true` or `false`.

If you set a project-wide metadata entry, all compute instances in the project inherit that setting implicitly. If you set an instance metadata entry, the metadata entry is enabled for that compute instance only, regardless of the project setting.

You can set a metadata entry by using the Google Cloud console, the gcloud CLI, or the Compute Engine API. For more information, see [Setting custom metadata](https://docs.cloud.google.com/compute/docs/metadata/setting-custom-metadata).

For example, the following gcloud CLI command enables serial port output logging to Cloud Logging for your project:
    
    
    gcloud compute project-info add-metadata \
        --metadata serial-port-logging-enable=true

Similarly, the following gcloud CLI command enables serial port output logging to Cloud Logging for a specific instance instead:
    
    
    gcloud compute instances add-metadata INSTANCE_NAME \
        --metadata serial-port-logging-enable=true

To disable serial port output logging to Cloud Logging, set `serial-port-logging-enable` to `false`:
    
    
    gcloud compute instances add-metadata INSTANCE_NAME \
        --metadata serial-port-logging-enable=false

#### Exclusion filters

From within Cloud Logging, you can [create an exclusion filter](https://docs.cloud.google.com/logging/docs/exclusions#exclusion-filters) to remove specific serial port entries from the Logs Explorer. For example, with a project-wide metadata entry that is set to `serial-port-logging-enable=true`, you can disable serial port output logging for specific compute instances by using an advanced filter:
    
    
    logName = "projects/PROJECT_ID/logs/serialconsole.googleapis.com%2Fserial_port_1_output"
    resource.type = "gce_instance"
    resource.labels.instance_id != "INSTANCE_1_ID"
    resource.labels.instance_id != "INSTANCE_2_ID"

### Setting an organization policy

You can disable serial port output logging to Cloud Logging for your entire organization by setting an [Organization Policy](https://docs.cloud.google.com/resource-manager/reference/rest/v1/Policy), which constrains certain configurations of Google Cloud resources. Specifically, set the following boolean constraint: `constraints/compute.disableSerialPortLogging`. For more information, see [Creating and managing organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies#creating_and_editing_policies).

Disabling serial port logging by setting `constraints/compute.disableSerialPortLogging` to `true` is not retroactive. Existing compute instances with a metadata entry that enables serial port logging to Cloud Logging continue to log to Cloud Logging unless you reset the metadata for those instances.

After setting this organization constraint to `true`, you cannot set instance or project metadata to enable serial port output logging to Cloud Logging for any instances within the organization.

## View serial port output

Use the Google Cloud console, the gcloud CLI, or REST to view the most recent 1 MB of output per serial port from running instances. To view output exceeding 1 MB per port, or to view output from stopped instances, use Cloud Logging.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

  2. Select the compute instance for which you want to view serial port output.

  3. Under **Logs** , click **Serial port 1 (console)** , **Serial port 2 (console)** , **Serial port 3** , or **Serial port 4**.

System-level entities typically use **Serial port 1** , which is also known as the [serial console](https://docs.cloud.google.com/compute/docs/instances/interacting-with-serial-console).




###  gcloud 

To view serial port output from a running compute instance, use the [`gcloud compute instances get-serial-port-output` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/get-serial-port-output).
    
    
    gcloud compute instances get-serial-port-output INSTANCE_NAME \
      --port PORT \
      --start START \
      --zone ZONE
    

Replace the following:

  * `INSTANCE_NAME`: the name of the instance.
  * `PORT`: the number of the port (`1`, `2`, `3`, or `4`) for which you want to view output. System-level entities typically use the first serial port (port 1), which is also known as the serial console. By default, the output of the first serial port is returned.
  * `START`: the byte index (zero-based) of the first byte you want returned. Use this flag if you want to continue getting the output from a previous request that was too long to return in one attempt.
  * `ZONE`: the zone of your instance.



###  REST 

In the API, create a `get` request to the [`instances.getSerialPortOutput` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/getSerialPortOutput).
    
    
    GET https://compute.googleapis.com/compute/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/serialPort

###  Cloud Logging 

Before you can view these logs, you must send serial port output to Cloud Logging.

  1. In the Google Cloud console, go to the **Logs Explorer** page. 

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. In the **Query** pane, enter the following query, then click **Run query** :
         
         resource.type="gce_instance"
         logName="projects/PROJECT_ID/logs/serialconsole.googleapis.com%2Fserial_port_1_output"
         resource.labels.instance_id="INSTANCE_ID"
         

Replace the following:

     * `PROJECT_ID`: the ID of the project that contained the instance.
     * `INSTANCE_ID`: the ID of the compute instance.



For more information about filtering in Logs Explorer, see [View logs by using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

## Handling non-UTF8 characters

Serial port output is escaped by using the open source [Abseil](https://github.com/abseil) C++ library's [`CHexEscape()` method](https://github.com/abseil/abseil-cpp/blob/master/absl/strings/escaping.h#L92), so non-UTF8 characters are encoded as hex strings. You can use the corresponding [`CUnescape()` method](https://github.com/abseil/abseil-cpp/blob/master/absl/strings/escaping.h#L38) to get the exact output that was sent to the serial port.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
