---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/event-codes/
title: Event IDs and resolutions for appliance-managed backups \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:27.742504+00:00
---

# Event IDs and resolutions for appliance-managed backups  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/event-codes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Event IDs and resolutions for appliance-managed backups Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

The Backup and DR appliance management console generates events for both successful and failed jobs. This page lists the event IDs and error messages.

The following table describes important Backup and DR event IDs, event messages, and steps to resolve them:

**Note:** In many error messages, the Backup and DR agent is referred as Actifio Connector or UDSAgent.Event ID | Event message | What to do  
---|---|---  
5022 | Actifio Connector: Failed in preparing VSS snapshot set | This issue occurs if Windows fails to create a VSS snapshot. To resolve this issue, do the following:  
  


  * Check `UDSAgent.log`
  * Check disk space on protected volumes. 300MB may not be enough.
  * Check Windows Event Logs for VSS related errors.
  * `vssadmin list writers` may show writers in a bad state.

  
Usually these errors are accompanied by VSS errors reported in the logs such as: `VSS_E_VOLUME_NOT_SUPPORTED_BY_PROVIDER`, `VSS_E_UNEXPECTED_PROVIDER_ERROR`.  
  
First check if all the VSS writers are in a stable state by going to the command line and issuing this command: `# vssadmin list writers`.  
  
Check output to confirm that all the writers are in a stable state. Restart VSS service and check if the writers are stable. If not you may have to reboot the machine.  
5024 | Actifio Connector: Failed to create VSS snapshot for backup. Insufficient storage available to create either the shadow copy storage file or other shadow copy data | This issue occurs if there is insufficient disk space to process a snapshot.  
  


  1. Ensure the drive being backed up is not full.
  2. Check if all the VSS writers are in a stable state. From the Windows command line, run: `vssadmin list providers`, `vssadmin list writers`.
  3. If these services are not running, start them and re-run the job. If the writer's State is Not Stable, restart the VSS service. If the problem continues after restarting the service, reboot the host.

  
Sometimes the message appears when internal VSS errors occur. Check the Windows Event Logs for VSS related errors. For errors related to VSS, search for related Microsoft patches. Additional VSS troubleshooting details can be found on Microsoft TechNet.  
  
Microsoft recommends at least 320MB on devices specified for saving the created VSS snapshot, plus change data that is stored there.  
  
Actifio recommends the shadow storage space be set to unbounded (unlimited) using these commands: `vssadmin list shadowstorage`, `vssadmin Resize ShadowStorage /On=[drive]: /For=[drive]: / Maxsize=[size]`.  
  
To change the storage area size in the Windows UI, refer to [Configuring Volume Shadow Copy on Windows Server 2008](http://www.techotopia.com/index.php/%20Configuring_Volume_Shadow_Copy_on_Windows_Server_2008). Re-run the backup once the VSS state is stable and shadow storage is set to unbounded.  
5046 | Backup staging LUN is not visible to the Actifio Connector | This issue occurs if the staging LUN is not visible to the UDSAgent on the application's host and the host is unable to detect the staging LUN from the backup/recovery appliance.  
5049 | Actifio Connector: Failed identifying logical volume on the backup staging lun | Actifio Connector couldn't see the staging LUN. This can be caused by a bad connection or by trouble on the LUN.  
  
Verify that FC/iSCSI connectivity is good, then make sure it works by mapping the VDisk, partitioning it, formatting it, and copying files to it. The steps for partitioning and formatting are OS specific.  
5078 | Actifio Connector: The staging disk is full | Jobs fail if a file that was modified in the source disk is copied to the staging disk, but the file is larger than the free space available in the staging disk. To fix the issue with full staging disk, increase the staging disk. Specify the size of the staging disk in the advanced settings for the application. Set the value for staging disk size such that it is greater than the sum of size of the source disk and the size of the largest file.  
Note: Changing the staging disk in advanced settings provokes a full backup.  
5087 | Actifio Connector: Failed to write files during a backup (Source File) | Anti-virus programs or third party drivers may have applied file locks that cannot be overridden.  
  
Check the UDSAgent.log to see which file couldn't be accessed. Attempt to find which process is locking the file using lsof on Unix/ Linux, or fltmc on Windows. Exclude the file from the antivirus or capture job and re-try the capture.  
  
The current processes known to Microsoft are listed at: [Allocated filter altitudes](https://learn.microsoft.com/en-gb/windows-hardware/drivers/ifs/allocated-altitudes).  
  
These errors are rarely found on Unix or Linux, but it is possible that a process such as database maintenance or patch install / update has created an exclusive lock on a file. Install the latest Actifio Connector.  
  
A file system limitation or inconsistency was detected by the host operating system. Run the Windows Disk defragmenter on the staging disk.  
  
Low I/O throughput from the hosts disks or transport medium, iSCSI or FC. Ensure there are no I/O issues in the host's disks or transport medium. The transport medium will either be iSCSI or Fibre Channel depending on out of band configuration. Consult storage and network administrators as needed.  
5131 - SQL Logs report error 3041 | SQL log backups on instance fail with error 5131 | To resolve this, enable "Don't forcefully unload the user registry at user logoff", see [User Profile Service functionality](https://learn.microsoft.com/en-us/archive/blogs/dsnotes/more-on-user-profile-service-functionality).  
5131 - SQL logs show backup/ recovery appliances error 43901 | Snapshot jobs fail with error 5131, SQL logs show backup/ recovery "Failed snapshot Job" appliances error 43901 | This is because the ODBC login for the database is failing. Fixing the ODBC login resolves the issue.  
5136 | Actifio Connector: The staging volume is not readable | Check /act/logs/UDSAgent.log for details and contact Google support for the resolution for the issue.  
5241 | Actifio Connector: Failed to mount/clone applications from mapped image (Source File) | Invalid username and password being parsed from the control file. On the source, review the UDSAgent.log to see if the source is configured with the correct username/password under Advanced Settings in the connector properties.  
5547 | Oracle: Failed to backup archivelog (Source File) | Actifio Connector failed to backup the archive log using RMAN archive backup commands. The likely causes for this failure are:  
  


  * Connector failed to establish connection to database
  * The archive logs were purged by another application
  * TNS Service name is configured incorrectly, causing backup command to be sent to a node where the staging disk isn't mounted

  
Search for ORA- or RMAN- errors in the RMAN log. This is the error received from Oracle. Use the preferred Oracle resource as these are not Backup and DR conditions, and hence cannot be resolved within Backup and DR.  
  


  * Actifio Connector logs: `/var/act/log/UDSAgent.log`
  * Oracle RMAN logs: `/var/act/log/********_rman.log`

  
10022 | Connection failure | This is a general-purpose error indicating that a network connection to a service or host couldn't be established.  
This could be due to a variety of reasons, such as: Incorrect IP address or port configuration, a firewall is blocking the connection, or the remote service is down or unreachable. To diagnose and resolve the issue:  


  * Check the appliance status in the appliance management console.
  * Verify basic network connectivity.
  * Check the IP address.
  * Verify firewall and ports.
  * If nothing works then [contact Support](https://docs.cloud.google.com/backup-disaster-recovery/docs/support).

  
10032 | Snapshot pool exceeded warning level | To reduce consumption of the snapshot pool, do the following:  
  


  * Move VMware VMs from a snapshot to a Direct-to-OnVault backup plan. Then expire all snapshots to release the space used by the staging disks and last snap. This only works for VMware VMs; other application types still use some snapshot pool space if protected by a Direct-to-OnVault policy.
  * Reduce the number of snaps kept for an application by changing the policy template. Applications that have high change rates create larger snapshots, so this has the highest benefit for high change-rate applications. This does not necessarily lead to a different RPO, an OnVault images of each snap can be created before they are expired.
  * Delete mounts, clones, and live-clones if they are not needed.

  
10038 | About to exceed VDisk warning limit | To immediately reduce VDisk consumption, do the following:  
  


  * Ensure expirations are enabled, both at the global and individual application level.
  * Group databases from a single host together into a Consistency Group. For example, if a host has 9 databases, create one Consistency Group for all 9 databases, then protect that consistency group rather than the individual databases.
  * Reduce the number of snapshots kept for an application by changing the policy template used by a backup plan.
  * Delete unwanted mounts, clones, and live-clones images.
  * Move VMware VMs from a snapshot to a Direct- OnVault backup plan. You need to expire all snapshots to release the VDisks used by the staging disks. This only lowers the VDisk count for VMware VMs, and still uses VDisks when protected by a direct-to-OnVault policy.
  * Change VMware VMDKs that don't need to be protected to independent mode as these cannot be protected by VMware snapshots.

  
If this alert repeats daily but the appliance does not reach the maximum VDisks, then modify the policies to reduce the number of VDisks used, or increase the alert threshold. During a daily snapshot window the VDisk count can fluctuate while new VDisks are created for snapshots before the old VDisks are removed as a part of snapshot expirations. The daily fluctuations varies depending on the number of applications protected.  
10039 | Network error reaching storage device | A heartbeat ping to monitored storage has failed due to hardware failure or network issue. Check the network to resolve the issue.  
10043 | A backup plan violation has been detected | Review the [backup plan best practices](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-plan-policy-best-practices) and optimize your policies. The are common causes for backup plan violations.  
  


  * Job scheduler is not enabled. See to [enable the scheduler](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/appliance-control-panel#enable_or_disable_expirations_and_schedules).
  * The first jobs for new applications can often take a long time: Long job times can occur during the first snapshot or dedup job for an application. On-ramp settings can be used to prevent ingest jobs from locking up slots and locking out ingested applications. See [Set priorities for the first new applications](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/appliance-control-panel#set_priorities_for_the_first_new_applications).
  * Applications are inaccessible due to network issues.
  * Policy windows are too small or job run times are too long: While you cannot control how long each job takes to run, you can control the schedule time for applications that are running. Jobs that run for many hours occupy job slots that could be used by other applications. Review the [backup plan best practices](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-plan-policy-best-practices) and adjust policies accordingly.
  * Replication process sends the data to a remote backup/recovery appliance. Ensure that the bandwidth & utilization of your replication link is not saturated.

  
10046 | Performance Pool exceeded safe threshold | To reduce consumption of the snapshot pool, do the following:  
  


  * Move VMware VMs from a snapshot to a Direct-to-OnVault backup plan. Then expire all snapshots to release the space used by the staging disks and last snap. This only works for VMware VMs; other application types still use some snapshot pool space if protected by a Direct-to-OnVault policy.
  * Reduce the number of snaps kept for an application by changing the policy template. Applications that have high change rates create larger snapshots, so this has the highest benefit for high change-rate applications. This does not necessarily lead to a different RPO, an OnVault images of each snap can be created before they are expired.
  * Delete mounts, clones, and live-clones if they are not needed.

  
10055 | Unable to check remote protection | Each backup/recovery appliance checks the remote appliance hourly for possible remote protection issues. The appliance communication fails due to the following issues:  
  


  * Network error (temporary or permanent). Temporary network error does not mean job to fail; jobs are retried, but the hourly check is not updated.
  

  * Certificate error. To fix the certificate error, you need to re-exchange the certificate.

  
10070 | Udppm scheduler is off for more than 30 minutes. | The scheduler is off. This may have been set for maintenance. If the maintenance is complete, you can re-enable the scheduler, see to [enable the scheduler](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/appliance-control-panel#enable_or_disable_expirations_and_schedules).  
10084 | Alert for application (app name) and policy (policyname) job did not run because of unknown reason | Review the [backup plan best practices](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-plan-policy-best-practices) and optimize your policies. The are common causes for backup plan violations.  
  


  * Job scheduler is not enabled. See to [enable the scheduler](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/appliance-control-panel#enable_or_disable_expirations_and_schedules).
  * The first jobs for new applications can often take a long time: Long job times can occur during the first snapshot or dedup job for an application. On-ramp settings can be used to prevent ingest jobs from locking up slots and locking out ingested applications. See [Set priorities for the first new applications](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/appliance-control-panel#set_priorities_for_the_first_new_applications).
  * Applications are inaccessible due to network issues.
  * Policy windows are too small or job run times are too long: While you cannot control how long each job takes to run, you can control the schedule time for applications that are running. Jobs that run for many hours occupy job slots that could be used by other applications. Review the [backup plan best practices](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-plan-policy-best-practices) and adjust policies accordingly.
  * Replication process sends the data to a remote backup/recovery appliance. Ensure that the bandwidth & utilization of your replication link is not saturated.

  
10085 | Backup Plan violation for application (app name) on host (host name) and policy (policy name). Job did not run because of unknown reason. | Review the [backup plan best practices](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-plan-policy-best-practices) and optimize your policies. The are common causes for backup plan violations.  
  


  * Job scheduler is not enabled. See to [enable the scheduler](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/appliance-control-panel#enable_or_disable_expirations_and_schedules).
  * The first jobs for new applications can often take a long time: Long job times can occur during the first snapshot or dedup job for an application. On-ramp settings can be used to prevent ingest jobs from locking up slots and locking out ingested applications. See [Set priorities for the first new applications](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/appliance-control-panel#set_priorities_for_the_first_new_applications).
  * Applications are inaccessible due to network issues.
  * Policy windows are too small or job run times are too long: While you cannot control how long each job takes to run, you can control the schedule time for applications that are running. Jobs that run for many hours occupy job slots that could be used by other applications. Review the [backup plan best practices](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-plan-policy-best-practices) and adjust policies accordingly.
  * Replication process sends the data to a remote backup/recovery appliance. Ensure that the bandwidth & utilization of your replication link is not saturated.

  
10120 | Psrv started successfully | This is an internal event and can be ignored.  
10220 | NTP Service is not running or not synchronised. | The NTP Service on the backup appliance is not running. The NTP Service is needed to ensure the backup appliance uses the correct timestamps. A Compute Engine appliance should be using metadata.google.internal. Follow how to set the NTP server [DNS and NTP method](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/appliance-network-settings#dns-ntp).  
10225 | Udp corefiles are found, filename udpengine.(file name) | Internal processes are unexpectedly logging error files. Contact Google support to get the resolution for this issue.  
10229 | Exceeded storage, System name: (device name) | This is is an internal event and normally can be ignored.  
10237 | The X job has been running for more than 3 hours. | There are many reasons why a job can run for more than 3 hours.  
11001 | Backup appliance certificate expires in X days. Power on for 24 hours to renew, or contact support. | The backup/recovery appliance's certificate last update is more than 15 days old. If the backup/recovery appliance is down, bring it up.  
11004 | System components are down. Please contact support in case backups are affected. | Contact support.  
11006 | Not able to sync with host X, regular sync with host required to avoid permanent communication loss between Backup appliance and Host. | The certificate on the host hasn't been updated for more than 7 days. Try rebooting and reconnecting to the host.  
20019 | Insufficient CPU / Memory. Minimum number of core required: (cores) Actual cores : (cores). Minimum memory size required (GB): (memory) Actual memory : (memory) | Backup/recovery appliance has been changed and is not the recommended size. Contact Google support to get the resolution for this issue.  
20025 | Swap usage exceeded | This issue occurs when the swap usage is exceeding the configured threshold limit that is set for the backup/recoevery appliance. Contact Google support to get the resolution for this issue.  
20030 | tomcat stopped successfully | This is is an internal event and can be ignored.  
20031 | tomcat started successfully | This is is an internal event and can be ignored.  
22001 | OMD started Successfully, sltname: , slpname: . | This is is an internal event and can be ignored.  
42356 | File changes have been detected no deleted files have been detected new files have been detected. | This is is an internal event and can be ignored.  
43151 | couldn't add raw device mappings to virtual machine (VM). Error: VM task failed A general system error occurred: The system returned an error. | Adding a raw device mapping to a VM "stuns" the VM until ESX has had a chance to add the new resource. To find out why the raw device mapping couldn't be added, look at the ESX logs for the VM in question (vmware.log).  
  
Refer to the VMware documentation and knowledge base for assistance on reviewing the logs for error messages. Also, review the VMware article for more information on [collecting VMware logs](https://kb.vmware.com/s/article/653).  
43155 | Error: VM task failed. An error occurred while saving the snapshot: Failed to quiesce the virtual machine. | This is a VMware issue; for additional information, refer to VMware KB article - [1015180](https://kb.vmware.com/s/article/1015180). Virtual machine quiesce issues are dependent on the OS type. Additional investigation, further VMware KBA searches or contact VMware support to resolve this issue.  
43155 - a | Error: VM task failed. Device scsi3 couldn't be hot-added. | This usually means that the SCSI device you are trying to add to the VM is already in use by another VM.  
43155 - b | Error: VM task failed. The virtual disk is either corrupted or not a supported format. | This issue occurs if the VM's CTK files are locked, unreadable, or are being committed. To fix this issue, remove and re-create these CTK files. Refer to the KB article - [2013520](https://kb.vmware.com/s/article/2013520) for more information.  
43155 - c | Error: VM task failed. The operation is not allowed in the current state of the datastore. progress ="11" status="running" | There are two options for formatting a VMware datastore: NFS and VMFS. With NFS, there are some limitations like not being able to do RDM (Raw Disk Mapping). This means that you cannot mount from the backup/recovery appliance to an NFS datastore. Refer to the following KB article - [1001856](https://kb.vmware.com/s/article/1001856) for additional information.  
43175 | UDSAgent socket connection got terminated abnormally; while waiting for the response from agent | The Actifio Connector stops responding between the appliance and a host with Backup and DR agent is installed.  
  


  1. Restart the UDSAgent Backup and DR agent service on the specified host.
  2. Telnet to tcp port 5106 (UDSAgent communication port): `Trying 10.50.100.67... Connected to dresx2.accu.local. Escape character is '^]'. Connection closed by foreign host.`
  3. Verify network connectivity between appliance and host doesn't drop. If the problem persists, network analysis will be required.

  
43604 | Failed to verify fingerprint | This occurs when an inconsistency is found between the source and target data. Contact Google support to get the resolution for this issue.  
43690 | Host doesn't have any SAN or iSCSI ports defined. | This issue occurs if the backup/recovery appliance is not configured with iSCSI connection to the target host. Ensure that the network ports are open for iSCSI and the target host has discovered the backup/recovery appliances.  
43698 | ESX host is not accessible for NBD mode data movement | The backup/recovery appliance is unable to reach the ESX host over the network or resolve the ESX hostname using DNS. Contact Google support to get the resolution for this issue.  
43702 | Backup was aborted because there are too many extra files in the home directory of the VM | This is an alert condition generated by Backup and DR and is caused by leftover delta files in the VM's datastore. Normally, the delta files are removed after Backup and DR snapshot is consolidated. In some instances, these can be left behind by the VMware consolidation, and Backup and DR begins failing jobs to prevent exacerbating the issue. This issue is caused by VMware, refer to the knowledge base article - [1002310](https://kb.vmware.com/s/article/1002310).  
43755 | Failed to open VMDK volume; check connectivity to ESX server. | This happens when the ESX server cannot be reached by the controller, usually because of a physical connection or DNS problem. To fix this issue, do the following:  
  


  * Ensure port 902 is open between the backup/recovery appliance and the ESX host.
  * Check the current DNS server and ensure it is current and valid.
  * If the vCenter is virtualized, attempt a backup after migrating the vCenter to a different ESX host.
  * Ensure SSL required is set to True on the ESX host in the advanced settings.

  
43844 | Invalid size vmdk detected for the VM | There are two possible solutions for this situation:  
  


  * If consolidation is required for some disks on VM, size is reported as zero. To fix this issue, creating and deleting a snapshot of the VM.
  * See if the VMDK can be restored from a backup image.

  
43873 | Disk space usage on datastore has grown beyond the critical threshold | This issue occurs when the remaining space on the datastore is less than the critical threshold. If more storage is not made available soon, then jobs start to fail when the remaining space is inadequate to store them.  
  
This alert is created to help you take action to prevent ESX datastores from filling with snapshot data. Increase available space by expanding the datastore, migrating some VMs, or deleting old data on the datastore. Snapshots grow as more change data is added. If a datastore fills up due to a growing snapshot, VMs may be taken offline automatically by VMware to protect the data.  
43900 | Retry pending OnVault (log) (jobname) for application (appname) on host (hostname) Error: (errorID) (Error Description) | Job retries can be caused by many errors. Each 43900 event message includes an error code and an error message.  
43901 | Job failure | Job failures can be caused by many errors. Each 43901 event message includes an error code and an error message.  
43903 | Failed expire job | This issue occurs when the image is in use at the time of the expiration. This can be due to the image is in use by another process or operation, such as a mount, clone, restore. The expiration job most likely complete successfully on the second attempt. Backup and DR does not report the successful completion of this second attempt. If you get only one error for an image, it is safe to conclude that a second attempt to expire this image was successful. If there is a legitimate reason why this image cannot be expired, you will get multiple errors related to this image. If you receive more than one error, contact Google Support.  
43905 | Failed mount job | There are many ways a mount job can fail. The error code that accompanies the event helps to identify the root cause.  
43908 | Failed restore job | Job failures can be caused by many errors. Each 43908 event message includes an error code and an error message.  
43915 | Couldn't connect to backup host. Make sure Backup and DR agent is running on (host) and network port (port) is open | To initiate backup, the Actifio Connector service must be reachable by the backup/recovery appliance. This issue occurs, when the required ports are not open, the incorrect host IP is configured, the Backup and DR agent service not running, or the host is out of physical resources. To fix this issue, do the following:  
  


  1. Ensure that the port in use between the host, backup/recovery appliance, and Actifio Connector is open. By default, the Backup and DR agent uses port 5106 for bi-directional communication from the backup/recovery appliance. Make sure your firewall permits bi-directional communication through this port.
  2. Ensure that the correct IP is configured for the host **Manage > Appliance > Configure Appliance Networking**.
  3. Ensure that the Backup and DR agent service is running on the target host and restart, if necessary.
     * On Windows, find the UDS Host Agent service in `services.msc` and click **Restart**.
     * On Linux, run the command `/etc/init.d/udsagent restart`.
  4. Retry the backup.

  
43941 | Disk space usage on datastore has grown beyond the critical threshold | This issue occurs when the remaining space on the datastore is less than the critical threshold. If more storage is not made available soon, then jobs start to fail when the remaining space is inadequate to store them. This alert is created to help you take action to prevent ESX datastores from filling with snapshot data. Increase available space by expanding the datastore, migrating some VMs, or deleting old data on the datastore. Snapshots grow as more change data is added. If a datastore fills up due to a growing snapshot, VMs may be taken offline automatically by VMware to protect the data.  
43954 | Failed OnVault job | During a mount job, the backup/recovery appliance is unable to connect to the OnVault pool. This issue can be occurred due to any of the following reasons.  
  


  * No bucket name is specified for the OnVault pool.
  * Invalid credentials-access ID or access key not specified or wrong ID for the OnVault pool.
  * Invalid bucket in the OnVault pool.
  * General authentication issues for the OnVault pool.
  * DNS server in clusters `/etc/resolv.conf` is either different or the forward and reverse DNS zones files are changed.

  
43929 | Snapshot creation of VM failed. Error: VM task failed An error occurred while saving the snapshot: Failed to quiesce the virtual machine. | VM snapshot fails if the ESX server is unable to quiesce the virtual machine - either because of too much I/O, or because VMware tools cannot quiesce the application using VSS in time. Check the event logs on the host and check the VM's ESX log (vmware.log). Crash-consistent snapshots and connector-based backups show this behavior less often. For more information, refer to the VMware knowledge base articles - [1018194](https://kb.vmware.com/s/article/1018194) and [1007696](https://kb.vmware.com/s/article/1007696).  
43933 | Failed to find VM with matching BIOS UUID | This issue occurs if the VM's UUID is modified. To fix this issue, rediscover the VM and check if it was discovered as a new UUID. You can confirm this in the appliance management console by comparing the UUID of the newly discovered VM and that of the previously discovered VM. If the UUIDs don't match, the VM might have been cloned. You can also see this error, if a large number of Backup and DR managed VMs are removed from the vCenter.  
43948 | The number of images not expired awaiting further processing is (x) images ((x) snapshots, (x) onvaults) from (x) unique applications. (x) snapshots and (x) OnVaults were added in the last (x) seconds ((x) hours (x) minutes)., sltname: No specific slt, slpname: No specific slp. | Event ID 43948 is generated when an application begins halting expirations as a part of Image Preservation. 'Image Preservation' preserves snapshot and OnVault images beyond their expiration dates to ensure that those images are properly processed by the backup/recovery appliance. When a new application enters into a preserved mode, a Warning alert will be generated. The most common cause of this is backup plan violations as documented under event ID 10085.  
43954 | Retry OnVault | An OnVault job needed to be retried. Possible issues could include: The Service Account being used has the wrong role. The Service Account does not have authority to write to the bucket. The Cloud Storage bucket no longer exists.  
43960 | Skipped backing up 6 offline applications for SqlServerWriter application. | Backup of a SQL Server Instance found some databases were offline and couldn't be backed up. This commonly occurs when the database has been deleted on the server side, but is still included on the Backup/DR side. The error message contains the names of the offline databases that should be investigated.  
43972 | Metadata upload to bucket failed. | Metadata writes to an OnVault bucket failed. Possible issues could include: The Service Account being used has the wrong role. The Service Account does not have authority to write to the bucket. The Cloud Storage bucket no longer exists.  
43973 | udppm started Successfully | This is is an internal event and can be ignored.  
43999 | Warning: VM is running on a host that is running an outdated version of ESXi , which is not supported by Google. Please upgrade it to a supported version (>=) to ensure the best results. | Upgrade the VM to a supported version (>=) to ensure the best results.  
44003 | Succeeded `Job_xx-xx-xx` for application `application ID` on host `host`, sltname: `template`, slpname: `profile`. | This is is a successful status event and can be ignored.  
62001 | Streamsnapd daemon started successfully | This is is an internal event and can be ignored.  
90003 | A new update (version X) is available for Backup Appliance | A new update is available. Update your backup/recovery appliances as soon as possible.  
90004 | New update is scheduled to be auto-installed on Backup Appliance | No action needed as this is informative message that new update is scheduled to be auto-installed on Backup Appliance, No reboot is required for this update.  
  
## What's next

  * To view the event logs created on backup/recovery appliances, see [Backup and DR event logs](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/appliance-events)
  * To configure log-based alerts for Backup and DR, based on sample queries, see [create a log-based alert](https://docs.cloud.google.com/backup-disaster-recovery/docs/configure-alerts). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
