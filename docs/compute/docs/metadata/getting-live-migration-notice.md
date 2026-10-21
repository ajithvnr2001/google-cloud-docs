---
url: https://docs.cloud.google.com/compute/docs/metadata/getting-live-migration-notice/
title: Query metadata server for maintenance event notices \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:30:27.002145+00:00
---

# Query metadata server for maintenance event notices  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/metadata/getting-live-migration-notice/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Query metadata server for maintenance event notices Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

The metadata server provides information about a Compute Engine instance's scheduling options and settings, through the `scheduling/` metadata directory listing and the `maintenance-event` metadata key. You can use these metadata keys to learn about a VM's scheduling options, and also to notify you of an upcoming maintenance event.

The metadata server receives maintenance event notices before a compute instance is live migrated or terminated. To learn more about maintenance events and instance behavior during the events, see [Host maintenance overview](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview).

For a specific set of VMs, your VM maintenance options are more flexible. To learn more, see [Monitor and plan for a host maintenance event](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event).

## Before you begin

  * For Windows Server VMs, use [PowerShell 3.0 or later](https://learn.microsoft.com/powershell/). We recommend that you use `ctrl+v` to paste the copied code blocks.
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

To use the Python samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  * If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  * If you're using a local shell, then create local authentication credentials for your user account: 
        
        gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development). 




## Get live migration notices

You can learn when live migration is about to happen for your instance by querying the `maintenance-event` metadata key periodically.

The `maintenance-event` metadata key is populated for maintenance events only if you have set your VM's scheduling option to `migrate` or if your VM has a GPU attached.

The value of this metadata key changes 60 seconds before a maintenance event starts, giving your application code a way to trigger any tasks you want to perform prior to a maintenance event, such as backing up data or updating logs.

Compute Engine gives the 60-second warning only if:

  * You have set the VM's [availability options](https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options#settingoptions) to live migrate during a maintenance event.

  * You have queried the `maintenance-event` metadata key at least once since the last maintenance event.

    * If you have never queried the `maintenance-event` metadata key or have not queried the metadata key since the last migration, Compute Engine assumes that the VM doesn't require advance warning of maintenance events. The maintenance event initiates immediately and skips the 60-second warning.

    * If you don't want to skip the 60-second warning, make sure your client code queries the `maintenance-event` metadata key at least once between migration events. You must query the `maintenance-event` metadata key directly for Compute Engine to determine that you are watching this metadata key. Querying a higher level metadata doesn't trigger the advance notice.




For VMs with attached GPUs, the value changes 60 minutes before the VMs are stopped to give you time to shutdown and restart again on another host. VMs with attached GPUs are not live migrated and are instead stopped and optionally restarted. To learn more, see [Handling GPU host maintenance events](https://docs.cloud.google.com/compute/docs/gpus/gpu-host-maintenance).

## Query the maintenance event metadata key

###  Linux VMs 

To query the `maintenance-event` metadata key on Linux VMs, run the following command:
    
    
    user@myinst:~$ curl http://metadata.google.internal/computeMetadata/v1/instance/maintenance-event -H "Metadata-Flavor: Google"
    

The output is similar to the following:
    
    
    NONE

You can also use the [`wait-for-change`](https://docs.cloud.google.com/compute/docs/metadata/querying-metadata#waitforchange) option. With this option specified, the request only returns an output when a maintenance event is about to start and end.
    
    
    user@myinst:~$ curl http://metadata.google.internal/computeMetadata/v1/instance/maintenance-event?wait_for_change=true -H "Metadata-Flavor: Google"
    

**Note:** For Shielded VM, you can query the metadata by using the [HTTPS metadata server endpoint](https://docs.cloud.google.com/compute/docs/metadata/querying-metadata#query-https-mds).

###  Windows VMs 

To query the `maintenance-event` metadata key on Windows VMs, run the following command:
    
    
    PS C:\> 
    $value = (Invoke-RestMethod `
             -Headers @{'Metadata-Flavor' = 'Google'} `
             -Uri "http://metadata.google.internal/computeMetadata/v1/instance/maintenance-event")
    $value
    

The output is similar to the following:
    
    
    NONE

You can also use the [`wait-for-change`](https://docs.cloud.google.com/compute/docs/metadata/querying-metadata#waitforchange) option. With this option specified, the request only returns an output when a maintenance event is about to start and end.
    
    
    PS C:\> 
    $value = (Invoke-RestMethod `
             -Headers @{'Metadata-Flavor' = 'Google'} `
             -Uri "http://metadata.google.internal/computeMetadata/v1/instance/maintenance-event?wait_for_change=true")
    $value
    

**Note:** For Shielded VM, you can query the metadata by using the [HTTPS metadata server endpoint](https://docs.cloud.google.com/compute/docs/metadata/querying-metadata#query-https-mds).

###  Python 

You can use the `maintenance-event` metadata key with the [waiting for updates](https://docs.cloud.google.com/compute/docs/metadata/querying-metadata#waitforchange) feature to notify your scripts and applications when a maintenance event is about to start and end. This lets you automate any actions that you might want to run before or after the event.

The following Python sample provides an example of how you might implement these two features together.
    
    
    import time
    from typing import Callable, NoReturn, Optional
    
    import requests
    
    
    METADATA_URL = "http://metadata.google.internal/computeMetadata/v1/"
    METADATA_HEADERS = {"Metadata-Flavor": "Google"}
    
    
    def wait_for_maintenance(callback: Callable[[Optional[str]], None]) -> NoReturn:
        """Start an infinite loop waiting for maintenance signal.
    
        Args:
            callback: Function to be called when a maintenance is scheduled.
    
        Returns:
            Never returns, unless there's an error.
        """
        url = METADATA_URL + "instance/maintenance-event"
        last_maintenance_event = None
        last_etag = "0"
    
        while True:
            r = requests.get(
                url,
                params={"last_etag": last_etag, "wait_for_change": True},
                headers=METADATA_HEADERS,
            )
    
            # During maintenance the service can return a 503, so these should
            # be retried.
            if r.status_code == 503:
                time.sleep(1)
                continue
            r.raise_for_status()
    
            last_etag = r.headers["etag"]
    
            if r.text == "NONE":
                maintenance_event = None
            else:
                maintenance_event = r.text
    
            if maintenance_event != last_maintenance_event:
                last_maintenance_event = maintenance_event
                callback(maintenance_event)
    
    
    def maintenance_callback(event: Optional[str]) -> None:
        """Example callback function to handle the maintenance event.
    
        Args:
            event: details about scheduled maintenance.
        """
        if event:
            print(f"Undergoing host maintenance: {event}")
        else:
            print("Finished host maintenance")
    
    
    def main():
        wait_for_maintenance(maintenance_callback)
    
    
    if __name__ == "__main__":
        main()

## Review the outputs

The initial and default value of the `maintenance-event` metadata key is `NONE`.

  * For VMs with attached GPUs, bare metal instances, or other instances that don't support live migration, [maintenance event](https://docs.cloud.google.com/compute/docs/gpus/gpu-host-maintenance) the value changes from `NONE` to `TERMINATE_ON_HOST_MAINTENANCE`. This value is updated 60 minutes before the stopping event starts.

  * For non-GPU VMs with a scheduling option of `migrate`, the `maintenance-event` value changes as follows:

    1. At the start of the migration event, the value changes from `NONE` to `MIGRATE_ON_HOST_MAINTENANCE`. This value is updated 60 seconds before the stopping event starts.
    2. Throughout the duration of the event and while your VM instance is being live migrated, the value remains as `MIGRATE_ON_HOST_MAINTENANCE`.
    3. After the maintenance event ends, the value returns to `NONE`.
  * For sole-tenant VMs, during a host maintenance event, the `maintenance-event` metadata key value doesn't change and remains `NONE` from the start to the end of the event.




For machine series that support [advanced maintenance capabilities](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event), prior to a maintenance event you can query the metadata key `upcoming-maintenance`. If there is a notification available for your instance you should see values similar to the following:
    
    
    {
       "maintenanceType":"SCHEDULED"
       "canReschedule": "true"
       "latestWindowStartTime": "2025-08-28T21:56:21Z"
       "maintenanceStatus": "PENDING"
       "windowEndTime": "2025-08-29T01:56:20Z"
       "windowStartTime": "2025-08-28T21:56:26Z"
    }
    

To determine how long before a maintenance event the `upcoming-maintenance` metadata key is populated, see the "Maintenance experience" documentation for the machine series. For example, for Z3 machine types, see [Maintenance experience for Z3 instances](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z3_maintenance).

**Note:** During the maintenance event, the metadata server might briefly return a `503 Service Unavailable` code. If your application receives a 503 error code, you should retry your request.

## What's next

  * Learn about [setting instance availability policies](https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options).
  * Learn how to [simulate a host maintenance event](https://docs.cloud.google.com/compute/docs/instances/simulating-host-maintenance).
  * Learn more about [live migration](https://docs.cloud.google.com/compute/docs/instances/live-migration-process).
  * Learn more about [VM metadata](https://docs.cloud.google.com/compute/docs/metadata/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
