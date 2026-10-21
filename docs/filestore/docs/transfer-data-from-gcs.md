---
url: https://docs.cloud.google.com/filestore/docs/transfer-data-from-gcs/
title: Transfer large datasets from Cloud Storage to Filestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:15:20.469718+00:00
---

# Transfer large datasets from Cloud Storage to Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/transfer-data-from-gcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Transfer large datasets from Cloud Storage to Filestore Stay organized with collections  Save and categorize content based on your preferences. 

Use [Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/cloud-storage-to-cloud-storage) to move large datasets from Cloud Storage to your Filestore file shares.

![A workflow showing data being moved from Cloud Storage to a Filestore
instance using Storage Transfer Service. The Filestore instance is mounted
to multiple Compute Engine instances.](https://docs.cloud.google.com/static/filestore/images/sts.svg)

[Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/cloud-storage-to-cloud-storage) helps you to quickly and securely transfer large datasets between [object](https://docs.cloud.google.com/architecture/storage-advisor#object-storage) and [file](https://docs.cloud.google.com/architecture/storage-advisor#file-storage) storage systems, whether your data is hosted in Cloud Storage, third-party cloud providers, or on-premises.

Storage Transfer Service supports accelerated transfers of large datasets, handling hundreds of TB of data or more. Move your large datasets to the cloud to take advantage of analytics and machine learning operations available from the underlying [Compute Engine instances](https://docs.cloud.google.com/filestore/docs/mounting-fileshares) where your Filestore instances are mounted.

With Storage Transfer Service you can create Google-managed transfers or configure self-hosted transfers for full control over network routing and bandwidth usage.

**Note:** To transfer less than 1 TB of data from Cloud Storage buckets, use the Google Cloud CLI. For more information, see [Copying data from a Cloud Storage bucket to a Filestore file share](https://docs.cloud.google.com/filestore/docs/copying-data) or [When to use Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/cloud-storage-to-cloud-storage).

## Transfer data from a Cloud Storage bucket to a Filestore file share

Transferring data from Cloud Storage to a Filestore file share using Storage Transfer Service requires the following tasks:

  1. Set up your environment.
  2. Configure Filestore.
  3. Configure Storage Transfer Service.
  4. Create and initiate the transfer job.



The following sections walk you through each task.

### Set up your environment

  1. **Select or create a project.**

For the purposes of this guide, ensure your source and destination resources reside in the same project.

In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

If you are testing out Filestore and don't plan to keep the resources that you create, we recommend that you create a project instead of selecting an existing project. Once you're done testing, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard?_ga=2.171280418.30427899.1640890668-1982243420.1634228058)

  2. **Enable billing.**

Make sure that billing is enabled for your Google Cloud project. [Learn how to confirm that billing is enabled for your project](https://docs.cloud.google.com/billing/docs/how-to/modify-project#confirm_billing_is_enabled_on_a_project).

  3. [**Enable the following APIs:**](https://docs.cloud.google.com/apis/docs/getting-started#enabling_apis)

     * Filestore API

     * Resource Manager API

     * Pub/Sub API

     * Cloud Storage API

     * Storage Transfer API

     * Cloud Logging API

     * Compute Engine API

     * Service Usage API

     * Identity and Access Management API

  4. Optional: `gcloud`, a major component of the Google Cloud SDK, is installed on every Compute Engine VM. If performing any of the following steps from your local command line, set up the Google Cloud SDK.

Install and initialize the [Google Cloud SDK](https://docs.cloud.google.com/sdk/docs/install).

If you installed Google Cloud SDK previously, make sure you have the latest available version by running:
         
         gcloud components update
         

  5. [**Create a service account.**](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#iam-service-accounts-create-console) In the **Grant this service account access to project** section, assign the following roles:

     * `Owner`

     * `Project IAM Admin`

     * `Role Administrator`

     * `Pub/Sub Editor`

     * `Cloud Filestore Editor`

     * `Storage Object Admin`

     * `Storage Transfer Admin`

     * `Storage Transfer Agent`

     1. Copy and save the name of the service account you created for a later step.

     2. [Create a service account key](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys#iam-service-account-keys-create-console) for the account you just created. For the purposes of this guide, create only one key. Download the key file and save for a later step.

**Note:** Service account keys are a security risk if not managed correctly. You should [ choose a more secure alternative to service account keys](https://docs.cloud.google.com/docs/authentication#auth-decision-tree) whenever possible. If you must authenticate with a service account key, you are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

  6. **Assign roles to a user account.** In the [IAM](https://console.cloud.google.com/iam-admin) page, find your user account and assign it the following roles:

     * `Owner`

     * `Project IAM Admin`

     * `Role Administrator`

     * `Storage Transfer Admin`

     * `Storage Admin`

For more information see [User permissions](https://docs.cloud.google.com/storage-transfer/docs/source-cloud-storage#user_permissions).




### Configure Filestore

  1. [**Create a Filestore instance.**](https://docs.cloud.google.com/filestore/docs/creating-instances) When creating the instance, apply the following specifications:

     1. Ensure the Cloud Storage bucket, client VM, and Filestore instance all [reside in the same region](https://docs.cloud.google.com/filestore/docs/performance#across-resources).

     2. Select a [regional](https://docs.cloud.google.com/filestore/docs/service-tiers#regional) or [enterprise](https://docs.cloud.google.com/filestore/docs/service-tiers#enterprise) instance type.

     3. Optional: For larger datasets, [request a quota increase](https://docs.cloud.google.com/filestore/docs/requesting-quota-increases).

     4. Copy the instance name and IP address and save for a later step.

  2. **Mount a Filestore instance on a client machine.**

This guide describes a transfer that uses four Compute Engine VMs as NFS client machines. You'll create a single service account that operates on behalf of the four client machines. Each client machine will have three Storage Transfer Service agents installed.

**Note:** For [best performance](https://docs.cloud.google.com/filestore/docs/performance#single-multiple-performance), users should employ no fewer than four Compute Engine VMs for this scenario.
     1. Create a Compute Engine VM instance with access to other Google Cloud services.

        1. [Configure a VM](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#console) with the following specifications:

           1. When specifying a location, ensure the Google Cloud bucket, client VM, and Filestore instance all [reside in the same region](https://docs.cloud.google.com/filestore/docs/performance#across-resources).

           2. Each Storage Transfer Service agent needs 4 vCPU and 8 GB RAM. For best performance, run multiple agents per VM. For the purposes of this guide, provision an [`e2-standard-32`](https://docs.cloud.google.com/compute/docs/general-purpose-machines#e2_machine_types) Compute Engine virtual machine instance.

           3. In the **Identity and API Access** section, specify the following:

              1. In the **Service accounts** drop-down, select the service account you just created.
     2. Once the Compute Engine VM instance is created, sign into the machine using SSH. From the [Compute Engine VM instance](https://console.cloud.google.com/compute/instances) page, locate the instance you created, and click **SSH**.

     3. Use a text editor such as Vim to create a copy of the service account key file and temporarily save it locally to the VM. For example, `service-account-key.json`.

     4. [Install Docker on the VM](https://docs.cloud.google.com/storage-transfer/docs/on-prem-set-up#install_docker).

     5. [`gcloud`](https://docs.cloud.google.com/sdk/docs/install#installation_instructions) is already installed on the Compute Engine VM instance. From the SSH command line, enter the following command to [authorize](https://docs.cloud.google.com/sdk/gcloud/reference/auth/activate-service-account) the service account to use `gcloud`:
            
            gcloud auth activate-service-account ACCOUNT --key-file=KEY_FILE
            

where:

        * ACCOUNT is the email address for the service account you created. For example, `my-service-account@my-project.iam.gserviceaccount.com`.

        * KEY_FILE is the relative local path to the key file you copied earlier. For example, `sa-key.json`.

     6. Still from the SSH command line, install NFS:
            
            sudo apt-get -y update && sudo apt-get install nfs-common
            

     7. Make a local directory to map to the Filestore file share. When you repeat these steps for subsequent Compute Engine VM instances, use the same name and path:
            
            sudo mkdir -p MY_DIRECTORY
            

where:

        * MY_DIRECTORY is the name of the local POSIX directory for the Compute Engine VM instance. For example, `/usr/local/my_dir`.
     8. Mount the file share associated with the Filestore instance by running the `mount` command. You can use any [NFS mount options](https://linux.die.net/man/5/nfs). For the best performance, see the NFS mount recommendations in [Mounting a file share on a Compute Engine VM instance](https://docs.cloud.google.com/filestore/docs/mounting-fileshares#mounting-fileshare-on-vm):
            
            sudo mount -o rw IP_ADDRESS:/FILE_SHARE MY_DIRECTORY
            

where:

        * IP_ADDRESS is the IP address for the Filestore instance. This can be found from the [Filestore instances](https://console.cloud.google.com/filestore/instances) page.

        * FILE_SHARE is the name of the file share on the instance. For example, `my_fs_instance`.

        * MY_DIRECTORY is the name of the directory you mapped to in the previous step. This is a directory on the Compute Engine VM instance where you want to mount the Filestore instance.

     9. Confirm the mount point:
            
            mount -l | grep nfs
            

This returns the following or similar:
            
            10.66.55.194:/my_fs_instance on /home/usr/my_dir type nfs (rw,relatime,vers=3,rsize=524288,wsize=524288,namlen=255,hard,proto=tcp,timeo=600,retrans=2,sec=sys,mountaddr=10.66.55.194,mountvers=3,mountport=2050,mountproto=udp,local_lock=none,addr=10.66.55.194)
            

Alternatively, you can also use the following command:
            
            df -h --type=nfs
            

This returns the following or similar:
            
            Filesystem                       Size  Used Avail Use% Mounted on
            10.66.55.194:/my_fs_instance  1.0T     0  1.0T   0% /home/usr/my_dir
            

     10. Make note of the local POSIX directory path and save for a later step.

     11. Repeat the previous steps to create three more Compute Engine VM instances and mount the same Filestore instance to each. Use the same service account to manage all four Compute Engine VMs. Temporarily save a local copy of the service account key to each VM.




### Configure Storage Transfer Service

  1. [**Create an agent pool.**](https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-pools#google-cloud-console)

  2. [**Authorize the service agent for all Storage Transfer Service features.**](https://docs.cloud.google.com/sdk/gcloud/reference/transfer/authorize)

     1. Enter the following command:
            
            gcloud transfer authorize --add-missing --creds-file=KEY_FILE
            

where:

        * KEY_FILE is the relative local path to the key file you copied earlier. For example, `sa-key.json`.

Note the returned notification regarding the service agent and save the associated email address for the next step.

     2. After a few minutes, you should see the service agent in the [IAM](https://console.cloud.google.com/iam-admin) page. Once propagated, verify the following roles are assigned:

        * `Pub/Sub Editor`

        * `Storage Admin`

**Note:** Permissions typically take seconds to propagate, but, in some cases, can take up to seven minutes.
  3. **Install transfer agents.**

Each Storage Transfer Service agent requires 4 vCPU and 8 GB RAM.

**Note:** Storage Transfer Service preserves POSIX attributes and symlinks during transfer. For more information, see [metadata preservation](https://docs.cloud.google.com/storage-transfer/docs/metadata-preservation#posix).
     1. We recommend installing multiple agents to maximize fault tolerance and to take advantage of the dynamic scaling offered by Storage Transfer Service. The following example shows how to install three agents on a client machine. From the SSH command line, run the following command:
            
            gcloud transfer agents install --pool=MY_AGENT_POOL --count=3 \
            --creds-file=MY_SERVICE_ACCOUNT_KEY_FILE
            

where:

        * MY_AGENT_POOL is the name of the agent pool you previously created. For example, `my-agent-pool`.

        * MY_SERVICE_ACCOUNT_KEY_FILE is the relative path to the service account key. For example, `/relative/path/to/service-account-key.json`.

     2. Repeat these steps for each client machine.




### Create and initiate the transfer job

  1. [**Create a transfer job to move data from your Cloud Storage bucket to your Filestore instance.**](https://docs.cloud.google.com/storage-transfer/docs/create-transfers#cloud-storage) Reference the local POSIX directory you saved earlier to specify the destination path. For example, `/home/usr/my_dir`.



## Monitor transfer status

### Console

Monitor the status of your transfer from the [Transfer jobs](https://console.cloud.google.com/transfer) page of the Google Cloud console.

### Command line

You can monitor status using the command line:
    
    
    gcloud transfer jobs monitor JOB_NAME
    

where:

  * JOB_NAME is the name of your transfer job. For example, `transferJobs/OPI6300379522015192941`.



The response shows the following or similar:
    
    
    Polling for latest operation name...done.
    Operation name: my-sts-project_transferJobs/OPI6300379522015192941_0000000001660692377
    Parent job: OPI6300379522015192941
    Start time: 2022-08-16T23:26:17.600981Z
    SUCCESS | 100% (731.9MiB of 731.9MiB) | Skipped: 129.8kiB | Errors: 0
    End time: 2022-08-16T23:27:23.429472Z
    

For more information, see [Monitor agent activity](https://docs.cloud.google.com/storage-transfer/docs/managing-on-prem-agents#monitor-agents) or [File system transfer details](https://docs.cloud.google.com/storage-transfer/docs/managing-on-prem-agents#file_system_transfer_details).

## What's next

  * [Improve performance across Google Cloud resources](https://docs.cloud.google.com/filestore/docs/performance#across-resources).
  * [Create a Compute Engine VM instance with access to other Google Cloud services](https://docs.cloud.google.com/compute/docs/instances/create-start-instance#creating-an-instance-with-access-to-other-google-cloud-services).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
