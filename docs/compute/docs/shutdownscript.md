---
url: https://docs.cloud.google.com/compute/docs/shutdownscript/
title: Run shutdown scripts \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:01:43.285951+00:00
---

# Run shutdown scripts  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/shutdownscript/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Run shutdown scripts Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

Create and run shutdown scripts that execute commands right before a virtual machine (VM) instance is stopped or restarted. This is useful if you rely on automated scripts to start up and shut down instances, allowing instances time to clean up or perform tasks, such as exporting logs, or syncing with other systems.

Shutdown scripts are especially useful for VMs in a [managed instance group](https://docs.cloud.google.com/compute/docs/instance-groups/manager) with an [autoscaler](https://docs.cloud.google.com/compute/docs/autoscaler). If the autoscaler shuts down a VM in the group, the shutdown script runs before the VM stops and the shutdown script performs any actions that you define. The script runs during the limited shutdown period before the VM stops. For example, your shutdown script might copy processed data to Cloud Storage or back up any logs.

Shutdown scripts function very similarly to startup scripts. Much of the documentation for [startup scripts](https://docs.cloud.google.com/compute/docs/startupscript) also applies for shutdown scripts.

For both shutdown and reboot tasks, VMs always run shutdown scripts as follows:

  * For Linux VMs, by using the `root` user.
  * For Windows VMs, by using the `System` account.

**Note:** A VM-level or zonal-level shutdown script takes precedence over a project-level shutdown script. If you configure a shutdown script either on a specific VM or on VMs in a specific zone in your project, then the project-level script isn't executed on that VM. For information about how to add a project-level shutdown script, see [`gcloud compute project-info add-metadata`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/project-info/add-metadata).

## Prerequisites

To run scripts stored in metadata on a VM instance, the [guest environment](https://docs.cloud.google.com/compute/docs/images/guest-environment) must be installed and running.

  * The guest environment includes the [guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent) (for example, google-guest-agent on Linux) that reads the script content or URL from the instance's metadata and initiates execution.
  * All public Compute Engine images come with the guest environment preinstalled.
  * If you create a custom image, you must [manually install the Google Guest Environment](https://docs.cloud.google.com/compute/docs/images/install-guest-environment) to ensure scripts from metadata and other Google Cloud features function properly.



## Before you begin

  * Learn about [Startup scripts](https://docs.cloud.google.com/compute/docs/startupscript).
  * Understand what the [metadata server](https://docs.cloud.google.com/compute/docs/metadata) is.
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

### Terraform

To use the Terraform samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development). 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions):

  * All permissions required to [create an instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance)
  * `compute.instances.setMetadata` on the instance



## Specifications

The following sections outline the specifications for shutdown scripts.

### Limitations

There are some limitations to note when using shutdown scripts:

  * Compute Engine executes shutdown scripts only on a best-effort basis. In rare cases, Compute Engine cannot guarantee that the shutdown script will complete.
  * On Windows, the Local Group Policy is used to launch the shutdown script. 
    * The installation package configures the Local Group Policy `Computer Configuration/Windows Setting/Scripts (Startup/Shutdown)` setting to launch the script upon system shutdown.



### Shutdown script invocation

Shutdown scripts are triggered when the instance shuts down after any of the following events happen:

  * You do the following:

    * [Stop](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#stop-vm-guest-os) or [reboot](https://docs.cloud.google.com/compute/docs/instances/reset-instance#reboot-instance) the instance from within the guest OS.

    * [Stop](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#stop-vm) or [delete](https://docs.cloud.google.com/compute/docs/instances/deleting-instance#delete_an_instance) the instance.

  * Compute Engine stops an instance as part of a programmed stop or delete operation.

  * Compute Engine stops a Spot VM or preemptible instance as part of the [preemption process](https://docs.cloud.google.com/compute/docs/instances/preemptible#preemption_process).




A shutdown script can be of any file type. If there is a shutdown script present in the instance, then Compute Engine does the following:

  1. Copies the script to a local file in the instance.
  2. Sets permissions on the file to make the script executable.
  3. Executes the file when the instance shuts down.



You could, for example, provide a Python script instead of a bash script. Keep in mind that Compute Engine runs the script verbatim, regardless of the type of script.

To execute a script that is not bash, add a shebang line at the top of the file to let the operating system know which interpreter to use. For example, for a Python script, you can add a shebang line like:
    
    
    #!/usr/bin/python
    

### Shutdown script running time

Your shutdown scripts start running when Compute Engine sets the instance state to `STOPPING`. Your scripts must complete before the instance is fully stopped, which is when its state changes to `TERMINATED`. The time the instance takes to reach the `TERMINATED` state varies depending on the [instance type](https://docs.cloud.google.com/compute/docs/instances/suspend-stop-reset-instances-overview#stopping-instance).

If your scripts take longer than the time it takes for the instance to stop, then Compute Engine forcefully stops the scripts, which can lead to data loss or incomplete tasks. To prevent this, [stop the instance from within its guest OS](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#stop-vm-guest-os). This approach keeps the instance state to `STOPPING` until your shutdown scripts finish running.

## Use a local shutdown script

A local shutdown script is a script that lives on your local computer. Pass in a local shutdown script either as a file or by giving the contents directly to Compute Engine.

Shutdown scripts can perform as many actions as you need, but if you are passing in the file locally, your script cannot exceed the metadata value length limit of 256 KB. To use a script that exceeds the length limit, store your file on Cloud Storage. See Use shutdown script from Cloud Storage for more information.

### Provide a shutdown script file

You can only pass in a local shutdown script file through the `gcloud` command-line tool.

###  gcloud 

To pass in a local shutdown script file, supply the `--metadata-from-file` flag, followed by a metadata key pair, `shutdown-script=PATH/TO/FILE`, where `PATH/TO/FILE` is a relative path to the shutdown script. For example:
    
    
    gcloud compute instances create example-instance \
        --metadata-from-file shutdown-script=examples/scripts/install.sh
    

###  Terraform 

To specify a shutdown script directly, use the [`google_compute_instance`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance) resource with the path to the shutdown script in the metadata.
    
    
    resource "google_compute_instance" "shutdown_content_from_file" {
      name         = "instance-name-shutdown-content-from-file"
      machine_type = "f1-micro"
      zone         = "us-central1-c"
      metadata = {
        # Shuts down Apache server
        shutdown-script = file("${path.module}/shutdown-script.sh")
      }
      boot_disk {
        initialize_params {
          image = "debian-cloud/debian-13"
        }
      }
      network_interface {
        # A default network is created for all Google Cloud projects
        network = "default"
        access_config {
        }
      }
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

### Provide shutdown script contents directly

Alternatively, you can pass in the contents of your shutdown script directly.

###  Console 

In Google Cloud console, specify a shutdown script directly using the `shutdown-script` metadata key:

  1. Go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. Specify the VM details.

  3. Expand the **Advanced options** section.

  4. Expand **Management** , and do the following:

     1. In the **Metadata** section, click **Add item**.
     2. In the **Key** field, enter `shutdown-script` for the metadata key.
     3. In the **Value** field, add the contents of your shutdown script.
  5. Continue with the VM creation process.




###  gcloud 

Using the Google Cloud CLI, use the `--metadata` flag to provide the contents of your shutdown script, followed by the `shutdown-script=CONTENTS` key pair, where `CONTENTS` is the content of your shutdown script.
    
    
    gcloud compute instances create example-instance --metadata shutdown-script="#! /bin/bash
    > # Shuts down Apache server
    > /etc/init.d/apache2 stop"
    

###  Terraform 

To specify a shutdown script directly, use the [`google_compute_instance`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance) resource with the shutdown script in the metadata.
    
    
    resource "google_compute_instance" "default" {
      name         = "instance-name-shutdown-content-directly"
      machine_type = "f1-micro"
      zone         = "us-central1-c"
      metadata = {
        # Shuts down Apache server
        shutdown-script = "#! /bin/bash /etc/init.d/apache2 stop"
      }
      boot_disk {
        initialize_params {
          image = "debian-cloud/debian-13"
        }
      }
      network_interface {
        # A default network is created for all Google Cloud projects
        network = "default"
        access_config {
        }
      }
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  REST 

In the API, provide a shutdown script as part of the metadata property in your request when you create an instance. Use `shutdown-script` as the metadata key:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/myproject/zones/us-central1-a/instances
    
    {...
      "metadata": {
        "items": [
          {
           "key": "shutdown-script",
           "value": "#! /bin/bash\n\n# Shuts down Apache server\n/etc/init.d/apache2 stop"
          }
        ]
      }...
    }
    

### Provide a shutdown script on Windows instances

Run shutdown scripts on Windows instances using the following Windows-specific metadata keys. Choose from any of the specialized keys listed below. Each key should match the type of script you want to run.

You can specify multiple shutdown scripts by passing in different keys to your instance but each key can only be specified once per virtual machine.

The following keys can be used with a local shutdown script, using the [same instructions](https://docs.cloud.google.com/compute/docs/shutdownscript#use_a_local_shutdown_script) earlier in this document.

`cmd` shutdown scripts | `bat` shutdown scripts | `ps1` shutdown scripts  
---|---|---  
`windows-shutdown-script-cmd` | `windows-shutdown-script-bat` | `windows-shutdown-script-ps1`  
  
## Use a shutdown script from Cloud Storage

You can store and use a shutdown script from Cloud Storage. Follow the instructions in the [Startup scripts](https://docs.cloud.google.com/compute/docs/startupscript#cloud-storage) documentation but replace `startup-script-url` with `shutdown-script-url`.

For Windows instances, replace `windows-startup-script-url` with `windows-shutdown-script-url`.

## Apply a shutdown script to running instances

To add a shutdown script to a running instance, follow the instructions in the [Applying a startup script to running instances](https://docs.cloud.google.com/compute/docs/startupscript#startupscriptrunninginstances) documentation but replace the metadata keys with one of the following keys:

  * `shutdown-script`: Supply the shutdown script contents directly with this key. Using the Google Cloud CLI, you can provide the path to a shutdown script file, using the `--metadata-from-file` flag and the `shutdown-script` metadata key.
  * `shutdown-script-url`: Supply a Cloud Storage URL to the shutdown script file with this key.



## Run a shutdown script during a graceful shutdown

By default, if a compute instance has [graceful shutdown](https://docs.cloud.google.com/compute/docs/instances/graceful-shutdown-overview) enabled, then any shutdown scripts that you configure in metadata keys run after the graceful shutdown ends.

To run commands during a graceful shutdown, you must use a custom watcher script that continuously polls the metadata server in the background, as shown in this section. To give your scripts enough time to complete and to avoid potential data loss or incomplete tasks, we recommend that you modify your shutdown scripts by moving your logic into this watcher script.

To run a shutdown script during a graceful shutdown, select one of the following options based on the guest OS that your compute instance uses:

###  Linux 

  1. If you haven't already, then [connect to the compute instance](https://docs.cloud.google.com/compute/docs/connect/standard-ssh).

  2. Run a watcher script, or configure it to run at boot, such as the following. Add your specific shutdown logic where indicated:
         
         #!/bin/bash
         
         # --------------------------------------------------------
         # Script for graceful shutdown based on the metadata value
         # --------------------------------------------------------
         #
         # This script monitors the metadata key `shutdown-status` and
         # waits for its value to change to `PENDING_STOP`. After the script
         # runs a series of user-defined commands, it runs `sudo shutdown -h now`
         # to signal to Compute Engine that the shutdown process is
         # complete.
         #
         # To run this script, you must have passwordless sudo privileges.
         
         METADATA_URL="http://metadata.google.internal/computeMetadata/v1/instance/attributes/shutdown-status"
         LAST_ETAG="0"
         
         echo "Starting shutdown status watcher"
         
         while true; do
           # Wait for the metadata value to change.
           # The metadata server blocks the request until a change occurs or a timeout is reached.
           RESPONSE=$(curl -H "Metadata-Flavor: Google" -s -i "${METADATA_URL}?wait_for_change=true&last_etag=${LAST_ETAG}")
           CURL_EXIT_STATUS=$?
         
           if [[ ${CURL_EXIT_STATUS} -ne 0 ]]; then
             echo "Error: curl command failed with exit status ${CURL_EXIT_STATUS}. Retrying in 5 seconds..."
             sleep 5
             continue
           fi
         
           # Strip carriage returns (\r) immediately to prevent CRLF line endings from corrupting string comparisons
           RESPONSE=$(echo "$RESPONSE" | tr -d '\r')
         
           # Extract the HTTP status code from the first line of the response
           HTTP_STATUS=$(echo "$RESPONSE" | head -n 1 | awk '{print $2}')
         
           if [[ "${HTTP_STATUS}" -eq 200 ]]; then
             # Read the new etag value to re-subscribe on the next poll.
             NEW_ETAG=$(echo "$RESPONSE" | grep -i "^ETag:" | awk '{print $2}')
             if [[ -n "${NEW_ETAG}" ]]; then
               LAST_ETAG="${NEW_ETAG}"
             fi
         
             # Extract the value of the shutdown status from the last line of the response body.
             SHUTDOWN_STATUS=$(echo "$RESPONSE" | tail -n 1)
         
             echo "Metadata changed. New ETag: ${LAST_ETAG}, shutdown-status: '${SHUTDOWN_STATUS}'"
         
             if [[ "${SHUTDOWN_STATUS}" == "PENDING_STOP" ]]; then
               echo "Shutdown signal 'PENDING_STOP' received. Exiting watcher loop."
               break
             fi
           elif [[ "${HTTP_STATUS}" -eq 503 ]]; then
             # 503 Service Unavailable: wait_for_change timed out with no change. Sleep and loop again.
             echo "Service temporarily unavailable or request timed out. Retrying in 2 seconds..."
             sleep 2
             continue
           else
             # Unexpected HTTP status
             echo "Warning: Unexpected HTTP status ${HTTP_STATUS}. Retrying in 5 seconds..."
             sleep 5
           fi
         done
         
         # --------------------------------------------------------
         # Graceful shutdown commands section
         # --------------------------------------------------------
         echo "Watcher loop exited. Starting graceful shutdown procedures..."
         
         # --- ADD YOUR GRACEFUL SHUTDOWN COMMANDS HERE ---
         
         echo "Graceful shutdown commands executed."
         
         # --------------------------------------------------------
         # Signal OS to stop
         # --------------------------------------------------------
         echo "Shutting down the guest OS to turn off the compute instance..."
         sudo shutdown -h now
         




###  Windows 

  1. If you haven't already, then connect to the compute instance by using one of the following methods:

     * [PowerShell](https://docs.cloud.google.com/compute/docs/instances/windows/connecting-powershell)

     * [Remote Desktop Protocol (RDP)](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows)

     * [Secure Shell (SSH)](https://docs.cloud.google.com/compute/docs/connect/windows-ssh)

     * [Special Administrative Console (SAC)](https://docs.cloud.google.com/compute/docs/instances/connecting-to-sac)

  2. Run a watcher script, or configure it to run at boot, such as the following. Add your specific shutdown logic where indicated:
         
         <#
         .SYNOPSIS
         pre-shutdown-script.ps1
         #>
         
         # --------------------------------------------------------
         # Script for graceful shutdown based on the metadata value
         # --------------------------------------------------------
         #
         # This script monitors the metadata key `shutdown-status` and
         # waits for its value to change to `PENDING_STOP`. After the script
         # runs a series of user-defined commands, it runs `Stop-Computer -Force`
         # to signal to Compute Engine that the shutdown process is
         # complete.
         
         $METADATA_URL = "http://metadata.google.internal/computeMetadata/v1/instance/attributes/shutdown-status"
         $LAST_ETAG = "0"
         
         Write-Host "Starting shutdown status watcher"
         
         while ($true) {
             $Response = $null
             $HTTP_STATUS = 0
         
             # Wait for the metadata value to change.
             # The metadata server blocks the request until a change occurs or a timeout is reached.
             try {
                 $Response = Invoke-WebRequest `
                     -Headers @{"Metadata-Flavor" = "Google"} `
                     -Uri "${METADATA_URL}?wait_for_change=true&last_etag=${LAST_ETAG}" `
                     -TimeoutSec 320 `
                     -ErrorAction Stop
         
                 if ($null -ne $Response) {
                     $HTTP_STATUS = [int]$Response.StatusCode
                 }
             } catch {
                 # Invoke-WebRequest throws an error for non-2xx status codes or connection failures.
                 $Exception = $_.Exception
                 if ($null -ne $Exception -and $null -ne $Exception.Response) {
                     $HTTP_STATUS = [int]$Exception.Response.StatusCode
                 } else {
                     $HTTP_STATUS = 0
                 }
             }
         
             if ($HTTP_STATUS -eq 0) {
                 Write-Host "Error: Request failed. Retrying in 5 seconds..."
                 Start-Sleep -Seconds 5
                 continue
             }
         
             if ($HTTP_STATUS -eq 200) {
                 # Read the new etag value to re-subscribe on the next poll.
                 $NEW_ETAG = $Response.Headers["ETag"]
                 if ($null -ne $NEW_ETAG) {
                     $LAST_ETAG = $NEW_ETAG
                 }
         
                 # Extract the value of the shutdown status from the response body.
                 $SHUTDOWN_STATUS = $Response.Content.Trim()
         
                 Write-Host "Metadata changed. New ETag: ${LAST_ETAG}, shutdown-status: '${SHUTDOWN_STATUS}'"
         
                 if ($SHUTDOWN_STATUS -eq "PENDING_STOP") {
                     Write-Host "Shutdown signal 'PENDING_STOP' received. Exiting watcher loop."
                     break
                 }
             } elseif ($HTTP_STATUS -eq 503) {
                 # 503 Service Unavailable: wait_for_change timed out with no change. Sleep and loop again.
                 Write-Host "Service temporarily unavailable or request timed out. Retrying in 2 seconds..."
                 Start-Sleep -Seconds 2
                 continue
             } else {
                 # Unexpected HTTP status
                 Write-Host "Warning: Unexpected HTTP status ${HTTP_STATUS}. Retrying in 5 seconds..."
                 Start-Sleep -Seconds 5
             }
         }
         
         # --------------------------------------------------------
         # Graceful shutdown commands section
         # --------------------------------------------------------
         Write-Host "Watcher loop exited. Starting graceful shutdown procedures..."
         
         # --- ADD YOUR GRACEFUL SHUTDOWN COMMANDS HERE ---
         
         Write-Host "Graceful shutdown commands executed."
         
         # --------------------------------------------------------
         # Signal OS to Halt
         # --------------------------------------------------------
         Write-Host "Shutting down the guest OS to turn off the compute instance..."
         Stop-Computer -Force
         




## Viewing the output of a shutdown script

###  Linux 

You can view the output from a Linux shutdown script by doing any of the following:

  * [Connecting to the instance](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance) and running the following command:
        
        sudo journalctl -u google-shutdown-scripts.service

  * [Viewing the output through serial port 1](https://docs.cloud.google.com/compute/docs/instances/viewing-serial-port-output#viewing_serial_port_output) in the Google Cloud console and checking for `google_metadata_script_runner` events.

  * IAP Desktop from a Windows workstation. For more information, see the [GoogleCloudPlatform/iap-desktop](https://github.com/GoogleCloudPlatform/iap-desktop) repo on GitHub.




###  Windows 

View the output from a Windows Server shutdown script by using any of the following and checking for `GCEMetadataScripts` events:

  * Serial port 1 in the Google Cloud console. For more information, see [Viewing serial port output](https://docs.cloud.google.com/compute/docs/instances/viewing-serial-port-output#viewing_serial_port_output).

  * Windows Event Viewer's Application Log.

  * IAP Desktop from a Windows workstation. For more information, see the [GoogleCloudPlatform/iap-desktop](https://github.com/GoogleCloudPlatform/iap-desktop) repo on GitHub.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
