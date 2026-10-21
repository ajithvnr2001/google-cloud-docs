---
url: https://docs.cloud.google.com/compute/docs/instances/startup-scripts/linux/
title: Use startup scripts on Linux VMs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T10:51:38.577553+00:00
---

# Use startup scripts on Linux VMs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/startup-scripts/linux/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Use startup scripts on Linux VMs Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

A startup script is a file that performs tasks during the startup process of a virtual machine (VM) instance. Startup scripts can apply to all VMs in a project or to a single VM. Startup scripts specified by VM-level metadata override startup scripts specified by project-level metadata, and startup scripts only run when a network is available. This document describes how to use startup scripts on Linux VM instances. For information about how to add a project-level startup script, see [`gcloud compute project-info add-metadata`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/project-info/add-metadata).

For Linux startup scripts, you can use bash or non-bash file. To use a non-bash file, designate the interpreter by adding a `#!` to the top of the file. For example, to use a Python 3 startup script, add `#! /usr/bin/python3` to the top of the file.

If you specify a startup script by using one of the procedures in this document, Compute Engine does the following:

  1. Copies the startup script to the VM

  2. Sets run permissions on the startup script

  3. Runs the startup script as the `root` user when the VM boots




For information about the various tasks related to startup scripts and when to perform each one, see the [Overview](https://docs.cloud.google.com/compute/docs/instances/startup-scripts).

## Prerequisites

To run scripts stored in metadata on a VM instance, the [guest environment](https://docs.cloud.google.com/compute/docs/images/guest-environment) must be installed and running.

  * The guest environment includes the [guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent) (for example, google-guest-agent on Linux) that reads the script content or URL from the instance's metadata and initiates execution.
  * All public Compute Engine images come with the guest environment preinstalled.
  * If you create a custom image, you must [manually install the Google Guest Environment](https://docs.cloud.google.com/compute/docs/images/install-guest-environment) to ensure scripts from metadata and other Google Cloud features function properly.



## Before you begin

  * Read the [overview of startup scripts](https://docs.cloud.google.com/compute/docs/instances/startup-scripts). 
  * Read about the [metadata server](https://docs.cloud.google.com/compute/docs/metadata). 
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




## Metadata keys for Linux startup scripts

A startup script is passed to a VM from a location that is specified by a metadata key. A metadata key specifies whether the startup script is stored locally, stored in Cloud Storage, or passed directly to the VM. The metadata key that you use might also depend on the size of the startup script.

The following table shows the metadata keys that you can use for Linux startup scripts, and provides information about which key to use based on the storage location and size of the startup script.

Metadata key | Use for  
---|---  
`startup-script` | Passing a bash or non-bash startup script that is stored locally or added directly and that is up to 256 KB in size  
`startup-script-url` | Passing a bash or non-bash startup script that is stored in Cloud Storage and that is greater than 256 KB in size. The string you enter here is used as-is to run `gcloud storage`. If your `startup-script-url` contains space characters, then don't replace the spaces with `%20` or add double quotes (`""`) to the `startup-script-url` string.  
  
## Order of execution of Linux startup scripts

You can use multiple startup scripts. Startup scripts stored locally or added directly execute before startup scripts that are stored in Cloud Storage. The following table shows, based on the metadata key, the order of execution of Linux startup scripts.

Metadata key | Order of execution  
---|---  
`startup-script` | First during each boot after the initial boot  
`startup-script-url` | Second during each boot after the initial boot  
  
## Passing a Linux startup script directly

You can add the contents of a startup script directly to a VM when you create the VM. The following procedures show how to create a VM with a startup script that installs Apache and creates a basic web page.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * All permissions required to [create a new VM](https://docs.cloud.google.com/compute/docs/instances/create-start-instance). 
  * `compute.instances.setMetadata` on the VM. 



###  Console 

**Passing a Linux startup script directly to a new VM**

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. To use a Linux operating system, do the following:

     1. In the navigation menu, click **OS and storage**. 

     2. Click **Change**.

     3. In the **Boot disk** pane that appears, select a Linux operating system.

  3. To directly add a Linux startup script, do the following:

     1. In the navigation menu, click **Advanced**.

     2. In the **Automation** section, enter the following in the **Startup script** field:
            
            #! /bin/bash
            apt update
            apt -y install apache2
            cat <<EOF > /var/www/html/index.html
            <html><body><p>Linux startup script added directly.</p></body></html>
            EOF
            

  4. Optional: Specify other configuration options. For more information, see [Configuration options during instance creation](https://docs.cloud.google.com/compute/docs/instances/instance-creation-overview#new-instance-configuration-options).

  5. To create and start the instance, click **Create**.




**Passing a Linux startup script directly to an existing VM**

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the **Name** of the instance.

  3. Click **Edit**.

  4. Under **Automation** , add the contents of your startup script.




**Verifying the startup script**

After the instance starts, view the external IP in a web browser to verify that the startup script created the website. You might have to wait about 1 minute for the sample startup script to finish.

###  gcloud 

**Passing a Linux startup script directly to a new VM**

Pass the contents of a startup script directly to a VM when creating it by using the following [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create).
    
    
    gcloud compute instances create VM_NAME \
      --image-project=debian-cloud \
      --image-family=debian-10 \
      --metadata=startup-script='#! /bin/bash
      apt update
      apt -y install apache2
      cat <<EOF > /var/www/html/index.html
      <html><body><p>Linux startup script added directly.</p></body></html>
      EOF'
    

Replace VM_NAME with the name of the VM.

**Passing a Linux startup script directly to an existing VM**

Add the startup script directly to an existing VM by using the following [`gcloud compute instances add-metadata` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/add-metadata):
    
    
    gcloud compute instances add-metadata VM_NAME \
        --zone=ZONE \
        --metadata=startup-script='#! /bin/bash
        apt update
        apt -y install apache2
        cat <<EOF > /var/www/html/index.html
        <html><body><p>Linux startup script added directly.</p></body></html>
        EOF'
    

Replace the following:

  * VM_NAME: the name of the VM

  * ZONE: the zone of the VM




**Verifying the startup script**

After the VM starts, view the external IP in a web browser to verify that the startup script created the web site. You might have to wait about 1 minute for the sample startup script to finish.

###  REST 

**Passing a Linux startup script directly to a new VM**

Pass the contents of a startup script directly to a VM when creating it by using the following [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    
    {
      ...
      "networkInterfaces": [
        {
          "accessConfigs": [
            {
              "type": "ONE_TO_ONE_NAT"
            }
          ]
        }
      ],
      "metadata": {
        "items": [
          {
            "key": "startup-script",
            "value": "#! /bin/bash\napt update\napt -y install apache2\ncat <<EOF > /var/www/html/index.html\n<html><body><p>Linux startup script added directly.</p></body></html>\nEOF"
          }
        ]
      },
      ...
    }
    

Replace the following:

  * PROJECT_ID: the ID of the project where the VM exists.

  * ZONE: the zone to create the VM in.




**Passing a Linux startup script directly to an existing VM**

  1. Get the `metadata.fingerprint` value of the VM by using the [`instances.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/get):
         
         GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME
         

Replace the following:

     * PROJECT_ID: the ID of the project where the VM exists.

     * ZONE: the zone of the VM.

     * VM_NAME: the name of the VM.

  2. Pass the startup script by using the `fingerprint` value, along with the metadata key and value for the startup script, in a call to the [`instances.setMetadata` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/setMetadata):
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/setMetadata
         
         {
           "fingerprint": FINGERPRINT,
           "items": [
             {
               "key": "startup-script",
               "value": "#! /bin/bash\napt update\napt -y install apache2\ncat <<EOF > /var/www/html/index.html\n<html><body><p>Linux startup script added directly.</p></body></html>\nEOF"
             }
           ],
           ...
         }
         

Replace the following:

     * PROJECT_ID: the ID of the project where the VM exists.

     * ZONE: the zone of the VM.

     * VM_NAME: the name of the VM.

     * FINGERPRINT: the `metadata.fingerprint` value obtained by using the [`instances.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/get).




**Verifying the startup script**

After the VM starts, view the external IP in a web browser to verify that the startup script created the web site. You might have to wait about 1 minute for the sample startup script to finish.

## Passing a Linux startup script from a local file

You can store a startup script in a local file on your workstation and pass the local file as metadata to a VM when you create it. You cannot use files stored on VMs as startup scripts.

Before passing a Linux startup script from a local file to a VM, do the following:

  1. Create a local file to store the startup script.

  2. Note the relative path from gcloud CLI to the startup script.

  3. Add the following startup script to the file:
         
         #! /bin/bash
         apt update
         apt -y install apache2
         cat <<EOF > /var/www/html/index.html
         <html><body><p>Linux startup script from a local file.</p></body></html>
         EOF
         




#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * All permissions required to [create a new VM](https://docs.cloud.google.com/compute/docs/instances/create-start-instance). 
  * `compute.instances.setMetadata` on the VM. 



###  gcloud 

**Passing a Linux startup script from a local file to a new VM**

Create a VM and pass the contents of a local file to be used as the startup script by using the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) with the `--metadata-from-file` flag.
    
    
    gcloud compute instances create VM_NAME \
      --image-project=debian-cloud \
      --image-family=debian-10 \
      --metadata-from-file=startup-script=FILE_PATH
    

Replace the following:

  * VM_NAME: the name of the VM

  * FILE_PATH: the relative path to the startup script file




**Passing a Linux startup script from a local file to an existing VM**

Pass a startup script to an existing VM from a local file by using the following [`gcloud compute instances add-metadata` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/add-metadata):
    
    
    gcloud compute instances add-metadata VM_NAME \
      --zone=ZONE \
      --metadata-from-file startup-script=FILE_PATH
    

Replace the following:

  * VM_NAME: the name of the VM

  * ZONE: the zone of the VM

  * FILE_PATH: the relative path to the startup script file




**Verifying the startup script**

View the external IP in a web browser to verify that the startup script created the web site. You might have to wait about 1 minute for the sample startup script to finish.

## Passing a Linux startup script from Cloud Storage

You can store a startup script in Cloud Storage and pass it to a VM when you create it. After you add a startup script to Cloud Storage, you have a URL that you can use to reference the startup script when you create a VM.

Before adding a startup script from a Cloud Storage bucket, do the following:

  1. Create a file to store the startup script. This example uses a bash (`.sh`) file.

  2. Add the following to the bash file, which installs Apache and creates a simple web page:
         
         #! /bin/bash
         apt update
         apt -y install apache2
         cat <<EOF > /var/www/html/index.html
         <html><body><p>Linux startup script from Cloud Storage.</p></body></html>
         EOF
         

  3. [Create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).

  4. [Add the file to the Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/uploading-objects).




### Security implications

  * By default, project owners and project editors can access Cloud Storage files in the same project, unless there are explicit access controls that disallow it.

  * If the Cloud Storage bucket or object is less secure than metadata, there is a risk of privilege escalation if the startup script is modified and the VM reboots. This is because after the VM reboots, the startup script runs as `root` and can then use the permissions of the attached service account to access other resources.




### Limitations

  * [Container-Optimized OS has limited or no support for some features](https://docs.cloud.google.com/container-optimized-os/docs/concepts/features-and-benefits#limitations).



#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * All permissions required to [create a new VM](https://docs.cloud.google.com/compute/docs/instances/create-start-instance). 
  * `compute.instances.setMetadata` on the VM. 
  * Permission to access the bucket and script file in Cloud Storage. Check the [access control](https://docs.cloud.google.com/storage/docs/access-control) settings on the bucket and file to ensure you have permission. 



###  Console 

**Passing a startup script that is stored in Cloud Storage to a new VM**

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. To use a Linux operating system, do the following:

     1. In the navigation menu, click **OS and storage**.

     2. In the **Operating system and storage** section, click **Change**. Then, select a Linux operating system.

  3. To allow the instance to access the Cloud Storage bucket that contains the Linux startup script, do the following:

     1. In the navigation menu, click **Security**.

     2. In the **Service account** list, select a service account that has the [Storage Object Viewer (`roles/storage.objectViewer`) IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) on the Cloud Storage bucket.

  4. To add a Linux startup script by specifying a file in Cloud Storage, do the following:

     1. In the navigation menu, click **Advanced**.

     2. In the **Metadata** section, click Add **Add item**. The **Key** and **Value** fields appear.

     3. In the **Key** field, enter `startup-script-url`.

     4. In the **Value** field, enter the Cloud Storage location of the startup script file using one of the following formats:

        * **Authenticated URL** : `https://storage.googleapis.com/BUCKET/FILE`
        * **gcloud storage URI** : `gs://BUCKET/FILE`

Replace the following:

        * BUCKET: the name of the bucket that contains the startup script file

        * FILE: the name of the startup script file

  5. Optional: Specify other configuration options. For more information, see [Configuration options during instance creation](https://docs.cloud.google.com/compute/docs/instances/instance-creation-overview#new-instance-configuration-options).

  6. To create and start the instance, click **Create**.




**Passing a startup script that is stored in Cloud Storage to an existing VM**

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the **Name** of the instance.

  3. Click **Edit**.

  4. Under **Metadata** , add the following values:

     * **Key** : `startup-script-url`

     * **Value** : the Cloud Storage location of the startup script file using one of the following formats:

       * **Authenticated URL** : `https://storage.googleapis.com/BUCKET/FILE`
       * **gcloud storage URI** : `gs://BUCKET/FILE`



**Verifying the startup script**

View the external IP in a web browser to verify that the startup script created the web site. You might have to wait about 1 minute for the sample startup script to finish.

###  gcloud 

**Passing a startup script that is stored in Cloud Storage to a new VM**

Pass a startup script stored in Cloud Storage to a VM when you create it by using the following [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create). For the value of the `--scope` flag, use `storage-ro` so the VM can access Cloud Storage.
    
    
    gcloud compute instances create VM_NAME \
      --image-project=debian-cloud \
      --image-family=debian-10 \
      --scopes=storage-ro \
      --metadata=startup-script-url=CLOUD_STORAGE_URL
    

Replace the following:

  * VM_NAME: the name of the VM.

  * CLOUD_STORAGE_URL: the metadata value. Set to the Cloud Storage location of the startup script file using one of the following formats:

    * **Authenticated URL** : `https://storage.googleapis.com/BUCKET/FILE`
    * **gcloud storage URI** : `gs://BUCKET/FILE`



**Passing a startup script that is stored in Cloud Storage to an existing VM**

Pass a startup script that is stored in Cloud Storage to an existing VM by using the following [`gcloud compute instances add-metadata` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/add-metadata):
    
    
    gcloud compute instances add-metadata VM_NAME \
        --zone=ZONE \
        --metadata startup-script-url=CLOUD_STORAGE_URL
    

Replace the following:

  * VM_NAME: the name of the VM.

  * ZONE: the zone of the VM.

  * CLOUD_STORAGE_URL: the metadata value. Set to the Cloud Storage location of the startup script file using one of the following formats:

    * **Authenticated URL** : `https://storage.googleapis.com/BUCKET/FILE`
    * **gcloud storage URI** : `gs://BUCKET/FILE`



**Verifying the startup script**

View the external IP in a web browser to verify that the startup script created the web site. You might have to wait about 1 minute for the sample startup script to finish.

###  REST 

**Passing a startup script that is stored in Cloud Storage to a new VM**

Pass a startup script that is stored in Cloud Storage to a VM when you create it by using the following [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert). To the `scopes` field, add `https://www.googleapis.com/auth/devstorage.read_only` so the VM can access Cloud Storage.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    
    {
      ...
      "networkInterfaces": [
        {
          "accessConfigs": [
            {
              "type": "ONE_TO_ONE_NAT"
            }
          ]
        }
      ],
      "serviceAccounts": [
        {
          "email": "default",
          "scopes": [
            "https://www.googleapis.com/auth/devstorage.read_only"
          ]
        }
      ],
      "metadata": {
        "items": [
          {
            "key": "startup-script-url",
            "value": "CLOUD_STORAGE_URL"
          }
        ]
      },
      ...
    }
    

Replace the following:

  * PROJECT_ID: the project ID.

  * ZONE: the zone to create the VM in.

  * CLOUD_STORAGE_URL: the metadata value. Set to the Cloud Storage location of the startup script file using one of the following formats:

    * **Authenticated URL** : `https://storage.googleapis.com/BUCKET/FILE`
    * **gcloud storage URI** : `gs://BUCKET/FILE`



**Passing a startup script that is stored in Cloud Storage to an existing VM**

  1. Get the `metadata.fingerprint` value of the VM by using the [`instances.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/get):
         
         GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME
         

Replace the following:

     * PROJECT_ID: the project ID

     * ZONE: the zone of the VM

     * VM_NAME: the name of the VM

  2. Pass the startup script by using the `fingerprint` value, along with the metadata key and value for the startup script, in a call to the [`instances.setMetadata` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/setMetadata):
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/setMetadata
         
         {
           "fingerprint": FINGERPRINT,
           "items": [
             {
                 "key": "startup-script-url",
                 "value": "CLOUD_STORAGE_URL"
             }
           ],
           ...
         }
         

Replace the following:

     * PROJECT_ID: the project ID.

     * ZONE: the zone of the VM.

     * VM_NAME: the name of the VM.

     * FINGERPRINT: the `metadata.fingerprint` value obtained by using the [`instances.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/get).

     * CLOUD_STORAGE_URL: the metadata value. Set to the Cloud Storage location of the startup script file using one of the following formats:

       * **Authenticated URL** : `https://storage.googleapis.com/BUCKET/FILE`
       * **gcloud storage URI** : `gs://BUCKET/FILE`



**Verifying the startup script**

View the external IP in a web browser to verify that the startup script created the web site. You might have to wait about 1 minute for the sample startup script to finish.

## Accessing metadata from a Linux startup script

In a startup script you can access metadata values. For example, you can use the same script for multiple VMs, and parameterize each script individually by passing different metadata values to each VM.

To access a custom metadata value from a startup script, do the following:

  1. Create a startup script that queries the value of a metadata key. For example, the following bash file (`.sh`) startup script queries the value of the `foo` metadata key.
         
         #! /bin/bash
         METADATA_VALUE=$(curl http://metadata.google.internal/computeMetadata/v1/instance/attributes/foo -H "Metadata-Flavor: Google")
         apt update
         apt -y install apache2
         cat <<EOF > /var/www/html/index.html
         <html><body><p>Accessing metadata value of foo: $METADATA_VALUE</p></body></html>
         EOF
         

  2. Set the value of the `foo` metadata key when creating a VM by using the following [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create). For this example, the startup script is passed to the VM from a local file.

###  gcloud 
         
         gcloud compute instances create VM_NAME \
           --image-project=debian-cloud \
           --image-family=debian-10 \
           --metadata-from-file=startup-script=FILE_PATH \
           --metadata=foo=bar
         

Replace the following:

     * VM_NAME: the name of the VM

     * FILE_PATH: the relative path to the startup script file

For more information about how to specify a metadata key/value pair, see [Setting custom metadata](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata#custom).

  3. From your local workstation, view the external IP in a web browser to verify that the startup script outputs the value of `foo`. You might have to wait about 1 minute for the sample startup script to finish.




## Rerunning a Linux startup script

Rerun a startup script by doing the following:

  1. [Connecting to the VM](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance).

  2. Running the following command:
         
         sudo google_metadata_script_runner startup




## Viewing the output of a Linux startup script

You can view the output from a Linux startup script by doing any of the following:

  * [Connecting to the instance](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance) and running the following command:
        
        sudo journalctl -u google-startup-scripts.service

  * [Viewing the output through serial port 1](https://docs.cloud.google.com/compute/docs/instances/viewing-serial-port-output#viewing_serial_port_output) in the Google Cloud console and checking for `google_metadata_script_runner` events.




## What's next

  * Learn how to [use startup scripts on Windows VMs](https://docs.cloud.google.com/compute/docs/instances/startup-scripts/windows).

  * Learn how to [troubleshoot VM startup](https://docs.cloud.google.com/compute/docs/troubleshooting/vm-startup).

  * Learn how to [add a shutdown script](https://docs.cloud.google.com/compute/docs/shutdownscript).

  * Learn more about [storing and retrieving metadata](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
