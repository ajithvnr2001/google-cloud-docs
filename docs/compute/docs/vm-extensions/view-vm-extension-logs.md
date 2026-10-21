---
url: https://docs.cloud.google.com/compute/docs/vm-extensions/view-vm-extension-logs/
title: View VM extension logs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:27:48.659940+00:00
---

# View VM extension logs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/vm-extensions/view-vm-extension-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  View VM extension logs Stay organized with collections  Save and categorize content based on your preferences. 

When you use VM Extension Manager to manage extensions on your Compute Engine instances (VMs), the guest agent on each VM logs events about the extension enforcement. Use [Cloud Logging](https://docs.cloud.google.com/logging/docs) to view these logs in the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface) to monitor and troubleshoot any issues with your VM extensions.

## Before you begin

  * Read the [VM Extension Manager](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager) documentation.
  * Read how to use the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).
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




## View VM extension logs

To view VM extension logs, use the Google Cloud console, the Google Cloud CLI, or REST.

###  Console 

  1. In the Google Cloud console, go to the **Logs Explorer** page. 

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. In the **Query** field, enter the following query:
         
         resource.type="gce_instance"
         resource.labels.instance_id="INSTANCE_ID"
         jsonPayload.@type="type.googleapis.com/google.compute.logging.agentcontrolplane.v1.VmExtensionEvent"
         jsonPayload.extensionName="EXTENSION_NAME"
         timestamp >= START_TIME
         timestamp <= END_TIME
         

Replace the following:

     * `INSTANCE_ID`: the ID of the VM instance.
     * `EXTENSION_NAME`: the name of the extension (for example, `ops-agent`).
     * `START_TIME`: the beginning of the time range (for example, `2024-01-01T00:00:00Z`).
     * `END_TIME`: the end of the time range (for example, `2024-02-01T00:00:00Z`).

**Example query** :
    
    resource.type="gce_instance"
    resource.labels.instance_id="123456"
    jsonPayload.@type="type.googleapis.com/google.compute.logging.agentcontrolplane.v1.VmExtensionEvent"
    jsonPayload.extensionName="ops-agent"
    timestamp >= "2024-01-01T00:00:00Z"
    timestamp <= "2024-02-01T01:00:00Z"
    

  3. Click **Run query**.




###  gcloud 

To look up VM extension logs, use the [`logging read` command](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read). For example:
    
    
    gcloud logging read 'resource.type="gce_instance" AND \
        resource.labels.instance_id="INSTANCE_ID" AND \
        jsonPayload.@type="type.googleapis.com/google.compute.logging.agentcontrolplane.v1.VmExtensionEvent" AND \
        jsonPayload.extensionName="YOUR_EXTENSION_NAME" AND \
        timestamp >= "START_TIME" AND \
        timestamp <= "END_TIME"'
    

Replace the following:

  * `INSTANCE_ID`: the ID of the VM instance.
  * `YOUR_EXTENSION_NAME`: the name of the extension (for example, `ops-agent`).
  * `START_TIME`: the beginning of the time range (for example, `2024-01-01T00:00:00Z`).
  * `END_TIME`: the end of the time range (for example, `2024-02-01T00:00:00Z`).



###  REST 

Make a request to the [Logging V2 API](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/list). The request body must contain the `filter` parameter. For example:
    
    
    POST https://logging.googleapis.com/v2/entries:list
    
    {
      "filter": "resource.type="gce_instance" AND
                "resource.labels.instance_id="INSTANCE_ID" AND
                "jsonPayload.@type="type.googleapis.com/google.compute.logging.agentcontrolplane.v1.VmExtensionEvent" AND
                "jsonPayload.extensionName="EXTENSION_NAME" AND
                "timestamp >= "START_TIME" AND
                "timestamp <= "END_TIME",
      "pageSize": 10,
      "resourceNames": [
        "projects/PROJECT_ID"
      ]
    }
    

Replace the following:

  * `INSTANCE_ID`: the ID of the VM instance.
  * `EXTENSION_NAME`: the name of the extension (for example, `ops-agent`).
  * `START_TIME`: the beginning of the time range (for example, `2024-01-01T00:00:00Z`).
  * `END_TIME`: the end of the time range (for example, `2024-02-01T00:00:00Z`).
  * `PROJECT_ID`: your Google Cloud project ID.



### VM extension event log entry

The following is an example of a log entry for a VM extension event:
    
    
    {
      "insertId": "rsiudxbck",
      "jsonPayload": {
        "eventMessage": "Enforcement State: Installing ops-agent@4bda61add3e5c989.; Extension Health: Plugin is running ok",
        "timestamp": "2026-03-23T16:13:40.496755675Z",
        "extensionName": "ops-agent",
        "revisionId": "4bda61add3e5c989",
        "@type": "type.googleapis.com/google.compute.logging.agentcontrolplane.v1.VmExtensionEvent",
        "eventType": "INSTALLED"
      },
      "resource": {
        "type": "gce_instance",
        "labels": {
          "project_id": "27654321",
          "instance_id": "1234567",
          "zone": "us-west1-a"
        }
      },
      "timestamp": "2026-03-23T16:13:40.496854498Z",
      "severity": "INFO",
      "logName": "projects/my-project/logs/compute.googleapis.com%2Fvm_extension_policies",
      "receiveTimestamp": "2026-03-23T16:13:40.906133199Z"
    }
    

### Log entry details

The following table describes the parameters that you can find in the VM extension logs:

Field | Description | `eventMessage` | A message that describes the event, including the enforcement state and extension health.  
---|---  
`extensionName` | The name of the extension (for example, `ops-agent`). For a list of supported extensions and their names, see [supported extensions](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager#supported-extensions).  
`extensionVersion` | The version of the extension that's been selected for installation. This version is either the version pinned in the extension policy or the latest version if no version was pinned.  
`revisionId` | A specific binary of an extension version. Each extension version can have multiple revisions to support different operating systems, and Google automatically chooses the correct one for a specific VM. Providing this revision ID to the Google support team can help debug whether the correct binary was chosen for the VM.  
`eventType` | The type of event. It can be one of the following values:  


  * `CRASHED`: The extension crashed. This value indicates that the extension was once installed and started successfully, but then stopped running.
  * `INSTALL_FAILED`: The extension installation failed.
  * `INSTALLED`: The extension is installed and started successfully.
  * `ROLLBACK_FAILED`: The extension rollback failed.
  * `ROLLED_BACK`: The extension rollback succeeded.
  * `INCOMPATIBLE`: None of the extension revision candidates satisfy the installation requirements (for example, operating system or architecture).
  * `SERVICE_DISABLED`: The service requiring this extension is disabled.

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
