---
url: https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/troubleshooting/
title: Google Cloud's Agent for SAP troubleshooting guide \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:11:47.720166+00:00
---

# Google Cloud's Agent for SAP troubleshooting guide  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Support ](https://docs.cloud.google.com/sap/docs/getting-support)



Send feedback 

#  Google Cloud's Agent for SAP troubleshooting guide Stay organized with collections  Save and categorize content based on your preferences. 

This guide shows you how to resolve issues with **version 3.15 (latest)** of Google Cloud's Agent for SAP.

For troubleshooting and support information from SAP, see the following SAP Notes:

  * [1642148 - FAQ: SAP HANA Database Backup & Recovery](https://launchpad.support.sap.com/#/notes/1642148)
  * [2031547 - Overview of SAP-certified 3rd party backup tools and associated support process](https://launchpad.support.sap.com/#/notes/2031547)
  * [2705632 - Support Process for Google Cloud Storage](https://launchpad.support.sap.com/#/notes/2705632)



## Logging

Check the logs in the directory that is specific to your operating system.

To view the logs for Google Cloud's Agent for SAP, navigate to the following paths:

### Linux
    
    
    /var/log/google-cloud-sap-agent.log

### Windows
    
    
    C:\Program Files\Google\google-cloud-sap-agent\logs\google-cloud-sap-agent.log

### View Backint related logs

If you've enabled the [Backint feature](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery) of Google Cloud's Agent for SAP, then review the following logs:

  * The SAP HANA `backup.log` file, which contains information about the SAP HANA backup and recovery operations.
  * The SAP HANA `backint.log` file, which contains the calls to the backup interface that is used by the Backint feature of the agent and other external backup tools.
  * The Backint log file of Google Cloud's Agent for SAP: `/var/log/google-cloud-sap-agent/backint.log`. This file includes information about when the Backint feature was enabled, related operational events, and indications of communication errors with Cloud Storage and related configuration or permissions issues.
  * The Google Cloud logs in Cloud Logging, which can contain errors related to the service account used by Google Cloud's Agent for SAP. To view these logs, in the Google Cloud console, go to the [Logs explorer](https://console.cloud.google.com/logs/query) page.



## Common issues

The following sections provide information about common issues related to using Google Cloud's Agent for SAP, their causes and resolution.

### Issue: Insufficient IAM permissions

**Issue:** Google Cloud's Agent for SAP logs show insufficient IAM permissions error.

**Cause:** The service account used by the agent does not have the required IAM permissions to access the Cloud Monitoring API, or the Workload Manager API, or if you're using the [Backint feature](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery) of the agent, then insufficient permissions to access the Cloud Storage bucket.

**Resolution:** To resolve this issue, perform the following steps:

  1. Establish an SSH connection with the Compute Engine instance or Bare Metal Solution server that hosts your SAP workload.

  2. Check the status and configuration of the agent:
         
         sudo /usr/bin/google_cloud_sap_agent status
         

  3. Review the **IAM Permissions** field in the output for each agent feature that you're using. You can see the IAM permissions that are missing, and other necessary setup as well.

For information about the IAM roles or permissions that you need to run the agent and its features, see the following installation or configuration guides:

     * [Install Google Cloud's Agent for SAP on a Compute Engine instance](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-config-on-vm) by using package manager
     * [Install and manage Google Cloud's Agent for SAP on a fleet of VMs](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-manage-on-vm-fleet) by using VM Extension Manager
     * [Install Google Cloud's Agent for SAP on a Bare Metal Solution server](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-config-on-bms)
     * [Configure Process Monitoring metrics collection](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-process-monitoring)
     * [Configure agent health metrics collection](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-agent-health-metrics)
     * [Configure Workload Manager evaluation metrics collection](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-workload-manager-evaluation)
     * [Configure SAP HANA Monitoring metrics collection](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-sap-hana-monitoring)
     * [Configure Backint based backup and recovery for SAP HANA](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-backint-backup-recovery)
     * [Back up and recover SAP HANA by using disk snapshots](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/perform-disk-snapshot-backup-recovery)
  4. Note the IAM roles or permissions that are missing to run the agent and the features you need.

  5. Note the name of the service account that the agent is using. For example: `sap-example@example-project-123456.iam.gserviceaccount.com`.

     * If your SAP workload is running on a Compute Engine instance, then in [Google Cloud console](https://console.cloud.google.com/), go to the VM instance details page and note the name of the service account.
     * If your SAP workload is running on a Bare Metal Solution server, then note the name of the service account that you created for it.
  6. Go to the [IAM & Admin](https://console.cloud.google.com/iam-admin/iam) page, and for the noted service account, add the IAM roles that you noted.




For more information about the authentication required for Google Cloud's Agent for SAP, see [Authentication and access](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning#authentication_access).

To confirm the permissions that the Cloud Monitoring agent requires, see the following Monitoring documentation:

  * [Authorize the Monitoring agent](https://docs.cloud.google.com/monitoring/agent/authorization)
  * [Access control](https://docs.cloud.google.com/monitoring/access-control)



### Issue: Incorrect access scopes for the service account of the Compute Engine instance

**Issue:** If you limit the access scopes on your host compute instance, then Google Cloud's Agent for SAP logs might show insufficient IAM permissions error.

**Cause:** Google Cloud's Agent for SAP requires minimum Cloud API access scopes on the host compute instance. This error occurs when the service account does not have the required access scopes.

**Resolution:** [Access scopes](https://docs.cloud.google.com/compute/docs/access/service-accounts#accesscopesiam) are the legacy method of specifying permissions for your compute instance. Compute Engine recommends configuring your compute instances to allow all access scopes to all Cloud APIs and using only the IAM permissions of the service account to control access to Google Cloud resources.

To resolve this issue, as a best practice, set the all `cloud-platform` access scope on the compute instance, then securely limit the service account's API access with IAM roles. For example:

  * `https://www.googleapis.com/auth/cloud-platform`



If you do limit the access scopes of your compute instance, then you must ensure that the host compute instance has the following access scopes:

  * `https://www.googleapis.com/auth/source.read_write`
  * `https://www.googleapis.com/auth/compute`
  * `https://www.googleapis.com/auth/servicecontrol`
  * `https://www.googleapis.com/auth/service.management.readonly`
  * `https://www.googleapis.com/auth/logging.admin`
  * `https://www.googleapis.com/auth/monitoring`
  * `https://www.googleapis.com/auth/trace.append`
  * `https://www.googleapis.com/auth/devstorage.full_control`



If you have enabled the collection of the Process Monitoring metrics or the SAP HANA monitoring metrics, then the access scopes of the host compute instance must also have write access to publish metric data to your Google Cloud project:

  * `https://www.googleapis.com/auth/monitoring.write`



To change the access scopes, you need to stop your compute instance, make the changes, and then restart the compute instance. For information about how to change the access scopes, see the [Compute Engine documentation](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#changeserviceaccountandscopes). You don't need to make any changes to permissions for IAM roles for this issue.

Once you've updated the access scopes, you can validate the agent setup by running the `status` command:

  1. Establish an SSH connection with the Compute Engine instance or Bare Metal Solution server hosting your SAP workload.

  2. Check the agent's status and configuration:
         
         sudo /usr/bin/google_cloud_sap_agent status
         

  3. Review the **Cloud API Full Scopes** field in the output.




### Issue: Missing or incorrect SAP Host Agent

**Issue:** Google Cloud's Agent for SAP logs show missing or incorrect SAP Host Agent error.

**Cause:** SAP Host Agent or the required minimum patch level for the SAP Host Agent is not installed. For Google Cloud's Agent for SAP to work, your SAP system must have the SAP Host Agent installed and the required minimum patch level for the Host Agent is maintained.

**Resolution:** To resolve this issue, install the required version of the SAP Host Agent. For instructions to install the SAP Host Agent, see the [SAP documentation](https://help.sap.com/saphelp_nw74/helpdata/en/21/98c443122744efae67c0352033691d/frameset.htm).

For version requirements for the SAP Host Agent, see the following SAP Notes:

  * Linux: SAP Note [2460297 - SAP on Linux on Google Cloud Platform: Enhanced Monitoring](https://launchpad.support.sap.com/#/notes/2460297)
  * Windows: SAP Note [1409604 - Virtualization on Windows: Enhanced Monitoring](https://launchpad.support.sap.com/#/notes/0001409604)



### Issue: Installation of Google Cloud's Agent for SAP failed

**Issue:** Installation of the agent fails when you run the package manager install command such as `yum`, `zypper`, or `googet`, or you see the following error message: `Package matching google-cloud-sap-agent-VERSION_NUMBER already installed. Checking for update.`.

**Cause:** Installation of the agent fails for one of the following reasons:

  * You're downgrading the agent to a non-latest version and your compute instance runs on an older version of RHEL for SAP, such as 7.9.
  * The compute instance that hosts the agent has been created without an external IP address.



**Resolution:** To resolve this issue, perform one of the following, as appropriate to your scenario:

  * If you want to downgrade your agent instance to a non-latest version and your compute instance runs on an older version of RHEL for SAP, such as 7.9, then run the following command:

### RHEL
        
        sudo tee /etc/yum.repos.d/google-cloud-sap-agent.repo << EOM
        [google-cloud-sap-agent]
        name=Google Cloud Agent for SAP
        baseurl=https://packages.cloud.google.com/yum/repos/google-cloud-sap-agent-el$(cat /etc/redhat-release | cut -d . -f 1 | tr -d -c 0-9)-x86_64
        enabled=1
        gpgcheck=1
        repo_gpgcheck=0
        gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
        EOM
        sudo yum downgrade google-cloud-sap-agent-VERSION_NUMBER.x86_64

### SLES15
        
        sudo zypper addrepo --refresh https://packages.cloud.google.com/yum/repos/google-cloud-sap-agent-sles15-x86_64 google-cloud-sap-agent
        sudo zypper install google-cloud-sap-agent-VERSION_NUMBER.x86_64

### SLES 12
        
        sudo zypper addrepo --refresh https://packages.cloud.google.com/yum/repos/google-cloud-sap-agent-sles12-x86_64 google-cloud-sap-agent
        sudo zypper install google-cloud-sap-agent-VERSION_NUMBER.x86_64

Replace `VERSION_NUMBER` with the agent's version number that you want to install, such as `3.1-606637668`. For information about the agent versions that you can install, see [List all available versions of the agent](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/operations#list_all_available_versions_of_the_agent).

  * If the compute instance hosting the agent doesn't have an external IP address, then set up a NAT gateway that gives the host server outbound access to the internet. For information about how to set up a NAT gateway, see the deployment guide for your SAP system. For example, for SAP NetWeaver, see:

    * [Access internet by using a Compute Engine VM and Cloud NAT](https://docs.cloud.google.com/bare-metal/docs/bms-setup#bms-access-internet-vm-nat)
    * [SAP NetWeaver on Linux Deployment Guide](https://docs.cloud.google.com/sap/docs/netweaver-deployment-guide-linux)
    * [SAP NetWeaver on Windows Deployment Guide](https://docs.cloud.google.com/sap/docs/netweaver-deployment-guide-windows)



### Issue: Collection of the SAP HANA monitoring metrics failed

**Issue:** While upgrading from the monitoring agent for SAP HANA, after you install Google Cloud's Agent for SAP, you see an error message similar to the following:
    
    
    tls: failed to verify certificate: x509: certificate relies on legacy Common Name field, use SANs instead

**Cause:** Google Cloud's Agent for SAP cannot start the collection of the SAP HANA monitoring metrics because the target SAP HANA instances use SSL certificates that are specified with Common Name (CN).

**Resolution:** To resolve this issue, complete the following steps:

  1. For the SAP HANA instances that you want to monitor using Google Cloud's Agent for SAP, you must switch to using a Subject Alternate Name (SAN) SSL certificate instead of SSL certificates that are specified with Common Name (CN).

  2. Establish an SSH connection with your host Compute Engine instance or Bare Metal Solution server.

  3. Open the configuration file of Google Cloud's Agent for SAP:
         
         /etc/google-cloud-sap-agent/configuration.json

  4. In the `hana_monitoring_configuration` section, set the parameter `enabled` to `true`.

  5. In the `hana_monitoring_configuration.hana_instances` section, perform the following for each SAP HANA instance that uses the TLS/SSL protocol for secure communication:

     1. Specify the parameter `enable_ssl` and set its value to `true`.

     2. Specify the parameter `host_name_in_certificate` and set the SAP HANA hostname, as specified in the TLS/SSL certificate, as its value.

     3. Specify the parameter `tls_root_ca_file` and set the path, where the TLS/SSL certificate is stored, as its value.

  6. Save the configuration file.

  7. If you're using version 3.6 or earlier of the agent, then restart Google Cloud's Agent for SAP for the new settings to take effect:
         
         sudo systemctl restart google-cloud-sap-agent

From version 3.7 of the agent, updated configuration of the agent automatically takes effect within the next 30 seconds.

  8. Verify that the agent is collecting the SAP HANA monitoring metrics. For instructions, see [View the other metrics](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/operations#view_other_metrics).

  9. Uninstall the monitoring agent for SAP HANA.




### Issue: Connection refused error

**Issue:** SAP Host Agent logs show the connection refused error.

**Cause:** Google Cloud's Agent for SAP cannot start up because the port `18181` is not available. Google Cloud's Agent for SAP listens for requests on port `18181`. This port must be available for the agent to start up.

**Resolution:** To resolve this issue, make sure that the port `18181` is available for Google Cloud's Agent for SAP. If another service is using port `18181`, then you might need to restart that other service or otherwise reconfigure it to use another port.

### Issue: For the OS images SLES 15 SP4 for SAP and later, Google Cloud's Agent for SAP is not running

**Issue:** When you use the SLES "for SAP" OS images, Google Cloud's Agent for SAP is preinstalled for you. But, for the OS images SLES 15 SP4 for SAP and later, the preinstalled Agent for SAP does not start on its own.

To verify that the agent is running or not, perform the following steps:

  1. Connect to your host Compute Engine instance or Bare Metal Solution server.
  2. Run the following command: 
         
         systemctl status google-cloud-sap-agent

If the agent is not running, then the output contains `inactive (dead)`. For example: 
         
         google-cloud-sap-agent.service - Google Cloud Agent for SAP
          Loaded: loaded (/usr/lib/systemd/system/google-cloud-sap-agent.service; disabled; vendor preset: disabled)
          Active: **inactive (dead)**
         




**Cause:** The Agent for SAP doesn't start on its own because of a problem with the OS packaging.

**Resolution:** To resolve the issue, perform the following steps:

  1. Connect to your host Compute Engine instance or Bare Metal Solution server.
  2. Run the following commands:
         
         sudo sed -i 's~ /usr/sap~ -/usr/sap~g' /usr/lib/systemd/system/google-cloud-sap-agent.service
         sudo systemctl restart google-cloud-sap-agent

  3. Verify that the agent is running: 
         
         systemctl status google-cloud-sap-agent

You should see an output similar to the following:
         
         google-cloud-sap-agent.service - Google Cloud Agent for SAP
           Loaded: loaded (/usr/lib/systemd/system/google-cloud-sap-agent.service; disabled; vendor preset: disabled)
           Active: **active (running)** since Wed 2023-07-12 03:07:23 UTC; 7s ago
         Main PID: 6117 (google_cloud_sa)
            Tasks: 6
           Memory: 8.8M (max: 1.0G limit: 1.0G available: 1015.1M)
           CGroup: /system.slice/google-cloud-sap-agent.service
                    └─ 6117 /usr/bin/google_cloud_sap_agent startdaemon
         




### Issue: System discovery fails due to lack of execute permission for the `/usr/sap` directory

**Issue:** In the Google Cloud's Agent for SAP logs, you see a warning `No execute permission for /usr/sap directory, some of the discovery operations will fail. Please ensure that the root user has execute permission for /usr/sap directory.`

**Cause:** The root user does not have the execute permission for the `/usr/sap/` directory. This stops the root user from accessing the SAP system profile and SAP tools located in the `/usr/sap` directory. This can restrict the agent from discovering the SAP systems running on the host compute instance, and consequently restrict the expected behavior of the agent's features.

**Resolution:** To resolve this issue, ensure that the root user has execute permission for the `/usr/sap/` directory. You can do this by running the following command:
    
    
    chmod +x /usr/sap

### Issue: Low throughput

**Issue:** You experience a lower than expected throughput.

**Cause:** For the Backint feature of Google Cloud's Agent for SAP, you might have enabled compression using the `compress` configuration parameter.

**Resolution:** To resolve this issue, verify that compression is not enabled. To do so, perform the following steps:

  1. Connect to your SAP HANA host by using SSH.

  2. Open your Backint configuration file:
         
         /usr/sap/SID/SYS/global/hdb/opt/backint/backint-gcs/parameters.json

Replace `SID` with the SID of the system where you installed the Backint related files.

  3. Verify that the `compress` parameter is set to `false`.

  4. If you make any change, then save the configuration file.




### Issue: Multistreaming errors

**Issue:** You get errors while [multistreaming data backups](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery#multistreaming_data_backups).

**Cause:** For the Backint feature of Google Cloud's Agent for SAP, you might have specified a higher number of parallel streams.

**Resolution:** To resolve this issue, perform the following steps:

  1. Connect to your SAP HANA host by using SSH.

  2. Open your Backint configuration file:
         
         /usr/sap/SID/SYS/global/hdb/opt/backint/backint-gcs/parameters.json

Replace `SID` with the SID of the system where you installed the Backint related files.

  3. If you've set a value for the `parallel_streams` parameter, then lower it to `1`.

If this doesn't resolve the error, then contact Customer Care.




### Issue with connecting to Cloud Storage

**Issue:** You're facing a connectivity issue with your Cloud Storage bucket.

**Cause:** This can be caused by the following:

  * A temporary connectivity issue.
  * The service account used by Google Cloud's Agent for SAP doesn't have the permissions required to access your Cloud Storage.
  * There's an issue with your configuration.



**Resolution:** To troubleshoot a connectivity issue with Cloud Storage bucket, check the following:

  * Retry the failed backup or recovery to make sure that the error wasn't just a momentary connectivity issue.
  * If Google Cloud's Agent for SAP is using your compute instance's service account, then make sure that the compute instance has access to all cloud scopes, or if you're limiting access, then make sure that the compute instance has access to `storage.googleapis.com`. For more information, see [Enable access to Cloud APIs and metadata servers](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-backint-backup-recovery#enable_api_ip_access).
  * If you created a service account for use with Google Cloud's Agent for SAP, then ensure the following: 
    * The service account is assigned the **Storage Object Admin** role.
    * The service account is assigned the **Cloud KMS CryptoKey Encrypter/Decrypter** role if you're using a customer-managed encryption key to encrypt backups in Cloud Storage. For more information, see [Encryption options for backups](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery#encryption_options_for_backups).
  * Make sure that you've correctly specified the parameters in the Backint configuration file, `PARAMETERS.json`, and the SAP HANA `global.ini` file.



You can test access to your Cloud Storage bucket using the self-diagnosis feature built into Google Cloud's Agent for SAP. For more information, see [Self diagnostics](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery#self_diagnostics).

### Issue: Backint backup fails with Write Pipe Channel error when using Workload Identity Federation

**Issue:** For the Backint feature of Google Cloud's Agent for SAP, you experience backup failures, and you see an error similar to the following in the `backup.log` file of SAP HANA:
    
    
    Generic stream error: $msg$ - , rc=$sysrc$: $sysmsg$. Failed to process item 0x0000123456a00000 - WritePipeChannel pipeAddress: <PIPE_ADDRESS>
    

In the backint.log file, you also see the following errors:
    
    
    "err":"failed to init multipart upload, err: multipart upload failed, err: <?xml version='1.0' encoding='UTF-8'?><Error><Code>AccessDenied</Code><Message>Access denied.</Message><Details>Provided scope(s) are not authorized</Details></Error>;
    

**Cause:** The error occurs because the `GOOGLE_APPLICATION_CREDENTIALS` environment variable is not being provided to the application, which prevents the Agent for SAP from properly authenticating using Workload Identity Federation. This results in the process defaulting to the Compute Engine service account, which might not have the correct permissions or scopes configured for the buckets you intend to use.

**Resolution:** To resolve this issue, set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable when invoking the Google Cloud's Agent for SAP using Backint. You can do this by exporting the variable within the script executed for backint operations. For example:
    
    
    #!/bin/bash
    export GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/wlif_credentials.json
    
    /usr/bin/google_cloud_sap_agent backint "$@"
    exit $?
    

### Issue with a disk snapshot based backup or recovery operation

**Issue:** A backup or recovery operation performed for SAP HANA by using the agent's `hanadiskbackup` or `hanadiskrestore` command is not successful.

**Cause:** This issue can occur due to any of the following reasons:

  * The agent experiences an error and exits the backup or recovery operation.
  * The agent takes more time than expected to create the disk snapshot or upload it to Cloud Storage due to an issue with an underlying Google Cloud service.
  * The agent crashes with no clear error or success message.
  * The backup or recovery operation fails because of an issue at the operating system level.
  * The agent is made to wait longer than expected by your SAP HANA database, which might be because your database is experiencing a very heavy workload.



**Resolution:** To resolve this issue, use the following information:

  * If it's a backup operation that is not successful, then do the following:

    1. [Verify that the agent is running](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/operations#verify-that-the-agent-is-running). If it's not, then [restart the agent](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/operations#agent4sap-restart), and then retry the backup operation.

    2. If the agent is running as expected, then check the status of the snapshot creation:
           
           gcloud compute snapshots list
             --filter="sourceDisk:projects/PROJECT_ID/zones/ZONE_ID/disks/DISK_NAME"
           

Replace the following:

       * `PROJECT_ID`: the Google Cloud project where the source disk is deployed
       * `ZONE_ID`: the Compute Engine [zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) where the source disk is deployed, for example, `us-central1-a`
       * `DISK_NAME`: the name of the source disk

The output status can be one of the following: `CREATING`, `UPLOADING`, or `READY`.

    3. If the status of the snapshot creation is `CREATING` or `UPLOADING`, then we recommend that you wait for this operation to complete, especially if this is the first snapshot that you're creating for the disk hosting your `/hana/data` volume.

If this operation fails, then the agent automatically exits the procedure and updates logs. You can retry creating the backup by running the `hanadiskbackup` command. The agent takes care of finishing the unsuccessful backup operation in the SAP HANA database and it creates a new snapshot based backup.

If you used the `-confirm-data-snapshot-after-create` argument with the `hanadiskbackup` command, and the snapshot upload operation fails, then you need to manually delete the snapshot's entry in your SAP HANA backup catalog and retry snapshot creation. To delete the entry in the SAP HANA backup catalog, you can use the [`BACKUP CATALOG DELETE` statement](https://help.sap.com/docs/SAP_HANA_PLATFORM/4fe29514fd584807ac9f2a04f6754767/22275913eb9e4a5bb539fc8df3da77f1.html). For information about the `-confirm-data-snapshot-after-create` argument, see its description in [Create a disk snapshot based backup](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/perform-disk-snapshot-backup-recovery#create_snapshot_based_backup).

    4. If the status of the snapshot creation is `READY` but the `hanadiskbackup` command still appears to be running, then this indicates that the agent is waiting on SAP HANA to do its part of the backup procedure.

    5. If the `hanadiskbackup` command appears to be running longer than expected, then do the following to resume normal operations for your SAP HANA database:

       1. Unfreeze the XFS file system that contains the `/hana/data` volume:
              
              xfs_freeze -u PATH_TO_HANA_DATA_VOLUME

       2. From your SAP HANA database, get the backup ID of the failed storage snapshot:
              
              SELECT BACKUP_ID, STATE_NAME, COMMENT FROM M_BACKUP_CATALOG WHERE ENTRY_TYPE_NAME = 'data snapshot' and STATE_NAME = 'prepared'

       3. In SAP HANA, update the entry for the failed snapshot as unsuccessful:
              
              BACKUP DATA FOR FULL SYSTEM CLOSE SNAPSHOT BACKUP_ID UNSUCCESSFUL 'Do not use - manually terminated';
              

Replace `BACKUP_ID` with the `BACKUP_ID` that you fetched in the preceding step.

    6. To resolve the issue of the unsuccessful backup operation, contact Customer Care with the agent's [support bundle](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/getting-support-diag-info#support_bundle).

  * If it's a recovery operation that is unsuccessful, then complete the following steps:

    1. Verify that the original disk hosting the `/hana/data` volume is attached to your host compute instance. If it's not, then attach it by using the [`gcloud compute instances attach-disk` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/attach-disk).

    2. Rescan your volume groups and logical volumes:
           
           sudo /sbin/dmsetup remove_all
           sudo /sbin/vgscan -v --mknodes
           sudo /sbin/vgchange -ay
           sudo /sbin/lvscan
           sudo mount -av
           

    3. If the rescan is unsuccessful, then restart your host compute instance. This makes the operating system rescan the volume groups.

    4. In SAP HANA, verify that the `/hana/data` volume is live.

    5. If the `/hana/data` volume is still not live, then contact Customer Care with the agent's [support bundle](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/getting-support-diag-info#support_bundle) to resolve the issue.




### Metrics based on SAP HANA monitoring views are missing

**Issue** : SAP HANA monitoring metrics that are based on the monitoring views in your SAP HANA database are missing, and you can see the following error in the logs of Google Cloud's Agent for SAP:
    
    
    {sql: Scan error on column index 0, name \"MEM_USED\": converting NULL to int64 is unsupported"}
    

**Cause** : The SAP HANA database user, which you've specified in the agent's configuration file for the `hana_monitoring_configuration.hana_instances.user` parameter, doesn't have the permission to read the monitoring views in your SAP HANA database. Consequently, the queries that the agent sends to the monitoring views are returned with no data.

**Resolution** : To resolve this issue, grant the specified database user the `CATALOG READ` system privilege or the `MONITORING` role in your SAP HANA database. To grant this privilege, you run the [`GRANT` statement](https://help.sap.com/docs/SAP_HANA_PLATFORM/4fe29514fd584807ac9f2a04f6754767/20f674e1751910148a8b990d33efbdc5.html) using an administrative user, such as `SYSTEM`. For example:

  * To grant the `MONITORING` role, run the following:
        
        GRANT MONITORING TO DB_USERNAME

  * To grant the `CATALOG READ` system privilege, run the following:
        
        GRANT CATALOG READ TO DB_USERNAME

Replace `DB_USERNAME` with the SAP HANA database username that you've specified in the agent configuration file for the `hana_monitoring_configuration.hana_instances.user` parameter. For information about this configuration parameter, see [Configuration parameters](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-sap-hana-monitoring#configuration_parameters).




### Issue: Exceeding the `Filtered list cost overhead` quota

**Issue:** You observe that you're exceeding one of the following quotas in the Google Cloud project where you're running your SAP system:

  * 'Filtered list cost overhead'
  * `Filtered list cost overhead per minute per region`



**Cause:** Version 3.7 or earlier of Google Cloud's Agent for SAP frequently calls the `compute.zoneOperations.list` API to determine if the Compute Engine instance has undergone a [live migration](https://docs.cloud.google.com/compute/docs/instances/live-migration-process) event. In Google Cloud projects with a high number of operations, these frequent calls can lead to quota exhaustion.

**Resolution:** To resolve this issue, update your agent instance to version 3.8 or later. From version 3.8, the agent no longer calls the `compute.zoneOperations.list` API for live migration checks, which avoids this quota issue.

For information about how to update Google Cloud's Agent for SAP, see [Update Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/operations#agent4sap-update).

## Getting support for Google Cloud's Agent for SAP

If you need help resolving a problem with Google Cloud's Agent for SAP, then gather the required diagnostic information and contact Cloud Customer Care. For more information, see [Google Cloud's Agent for SAP diagnostic information](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/getting-support-diag-info).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
