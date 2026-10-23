---
url: https://docs.cloud.google.com/workload-manager/docs/deploy/sap/post-deployment/
title: Post-deployment tasks for SAP S/4HANA \u00a0|\u00a0 Workload Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:27.873131+00:00
---

# Post-deployment tasks for SAP S/4HANA  |  Workload Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workload-manager/docs/deploy/sap/post-deployment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Workload Manager ](https://docs.cloud.google.com/workload-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/workload-manager/docs/overview)



Send feedback 

#  Post-deployment tasks for SAP S/4HANA Stay organized with collections  Save and categorize content based on your preferences. 

Before using your deployed SAP S/4HANA system, we recommend that you perform the post-deployment tasks described in this document.

## Review the deployment

After successful deployment of an SAP S/4HANA application, you can review the deployment output and configuration on the dashboard.

### Review the deployment resources

To review the resources created during the deployment:

  1. Go to the Workload Manager page in the Google Cloud console.

[Go to Workload Manager](https://console.cloud.google.com/workloads)

  2. In the left navigation pane, click **Deployments** to open the deployment dashboard.

  3. Select the name of the deployment to open the **Deployment information** page.

  4. Click **Deployment Output** tab to view a list of all resources that were created during the deployment, the resource type, and a link to the resource (if applicable).




### Review the deployment configuration

To review the deployment configuration:

  1. Go to the Workload Manager page in the Google Cloud console.

[Go to Workload Manager](https://console.cloud.google.com/workloads)

  2. In the left navigation pane, click **Deployments** to open the deployment dashboard.

  3. Select the name of the deployment to open the **Deployment information** page.

  4. Click the **Details** tab to view the information that you've entered for the initial configuration of the deployment.




## Delete the Ansible Runner VM

During the deployment process, a VM is deployed as an Ansible Runner to orchestrate the configuration and installation of the system using Ansible. After deployment, you can [delete the Ansible Runner VM](https://docs.cloud.google.com/compute/docs/instances/deleting-instance) to avoid incurring cost for this resource.

Before you delete the VM, you can confirm the VM name by reviewing details in the **Deployment Output** tab on the **Deployment information** page. The VM name format is `DEPLOYMENT_NAME-ansible-runner`.

Alternatively, you can keep the Ansible Runner VM and repurpose it as a Bastion Host as it is already configured to have access to the internet and access to other VMs that were deployed in your network. Note that the VM is attached to the deployed system and gets deleted if the system is later deleted using Workload Manager.

## Validate the SAP S/4HANA deployment

After you configure and deploy the SAP S/4HANA system using Workload Manager, perform the following tasks to verify that the deployment was successful:

  * Connect to the VM by using SSH
  * Run the SSH commands to validate a deployment



After you validate the deployment, connect to your SAP system using the standard tools such as SAP HANA Studio or HANA Cockpit.

### Connect to the VM using SSH

To view additional logs or to run validation commands on the VMs created during the deployment, you must connect to the VMs using SSH.

If you have not configured external IP addresses during the deployment process, use SSH to establish a connection with a VM in the same network that has an external IP address, and then connect directly to the other VMs. For more information, see [Connect to Linux VMs using a bastion host](https://docs.cloud.google.com/compute/docs/connect/ssh-using-bastion-host#connect_to_vms).

### Run the commands to validate a deployment

To validate the SAP S/4HANA deployment on Google Cloud, run the commands listed in the following table. You must run the command on the respective VM instance in your deployment. Depending on the operating system running on your VM, the command might be different.

VM instance | Activity | Command | Validation  
---|---|---|---  
HANA | HANA Basic Check | 
    
    
          sudo su - SID_LCadm -c "HDB info" | grep "indexserver"
          

For example:
    
    
    sudo su - ed1adm -c "HDB info" | grep "indexserver"

| Index server processes are active.  
HANA | Check landscape detail | 
    
    
          sudo su - SID_LCadm -c "cdpy && python landscapeHostConfiguration.py"
          

| "Overall host status" says "OK".  
HANA Primary (HA Only) | Check HANA replication status | 
    
    
          sudo su - SID_LCadm -c "cdpy && python systemReplicationStatus.py"
          

| Replication status shows no `ERROR`.  
HANA Primary & Secondary (HA Only) | Check cluster resources |  RHEL: 
    
    
    sudo pcs status

SLES: 
    
    
    sudo crm status

| Verify that the command returns the following information:  

* All cluster nodes appear as "online" inside "Node List".
* All cluster resources appear as "Started" in the primary or secondary.  
HANA | Check HANA config | 
    
    
          sudo su - SID_LCadm -c "cdcoc && cat global.ini"
          

| Verify that the file exists.  
If HA, verify that [ha_dr_provider_SAPHanaSR] exists.  
ASCS | NetWeaver instance list | 
    
    
          sudo su - SID_LCadm -c "/usr/sap/hostctrl/exe/sapcontrol -nr ASCS_INSTANCE_NUMBER
          -function GetSystemInstanceList"

For example:
    
    
    sudo su - ed1adm -c "/usr/sap/hostctrl/exe/sapcontrol -nr 12
          -function GetSystemInstanceList"

| Check for GREEN status for each deployed VM aside from HANA servers.  
For ASCS status: One entry with `MESSAGESERVER|ENQUE`  
For App Server status: Multiple entries (one per app server deployed), `ABAP|GATEWAY`  
If HA, ERS Status: One entry with `ENQREP`  
ERS (HA Only) | ERS Status | 
    
    
          sudo su - SID_LCadm -c "/usr/sap/hostctrl/exe/sapcontrol -nr ERS_INSTANCE_NUMBER
          -function GetSystemInstanceList"

| All GREEN  
ERS has the `ENQREP` process.  
NetWeaver Cluster Status (HA Only) | Check cluster resources |  RHEL: 
    
    
    sudo pcs status

SLES: 
    
    
    sudo crm status

| Verify the command returns the following information:  

* All cluster nodes appear as "online" inside "Node List".
* All cluster resources appear as "Started" in the primary or secondary.  
NetWeaver Cluster Status (HA Only) | NetWeaver Cluster Status |  RHEL: 
    
    
    sudo pcs config show | grep SAPInstance

SLES: 
    
    
    sudo crm config show | grep SAPInstance

| SAP Instance config shows in cluster outputs.  
ALL | Google Cloud's Agent for SAP | 
    
    
    sudo systemctl status google-cloud-sap-agent

| The output contains "active (running)".  
  
Replace the following:

  * `SID_LC`: the system ID (SID) in lowercase letters.
  * `ASCS_INSTANCE_NUMBER`: the ASCS instance number, which is a two-digit number between `00` and `99`.
  * `ERS_INSTANCE_NUMBER`: the ERS instance number, which is a two-digit number between `00` and `99`.



### Test failover for your high-availability clusters

You can test your high-availability clusters by simulating a failure on the primary host. To test failover on both the SAP HANA database and SAP NetWeaver clusters, follow these instructions:

For the SAP HANA cluster:

  * RHEL: [Test failover](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-rhel#test_failover)
  * SLES: [Test failover](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-sles#test_failover)



For the SAP NetWeaver Cluster:

  * RHEL: [Simulate a failover](https://docs.cloud.google.com/sap/docs/netweaver-ha-config-rhel#simulate_a_failover)
  * SLES: [Simulate a failover](https://docs.cloud.google.com/sap/docs/netweaver-ha-config-sles#simulate_a_failover)



## Connect to your SAP S/4HANA system

This section describes how to access your deployed SAP S/4HANA system.

For detailed instructions about accessing a newly deployed SAP system, see the [relevant SAP documentation](https://help.sap.com/docs/) for the SAP tool.

### Access system credentials

During the configuration process, a Secret must be assigned for the SAP HANA database credentials and application layer credentials.

To access the credentials used for the deployment, do the following:

  1. Navigate to the Workload Manager page in the Google Cloud console and review the deployment configuration.
  2. In the **Details** tab for the deployment, check the value displayed for either **Secret name for database credentials** or **Secret name for application credentials**.
  3. Navigate to Secret Manager in your Google Cloud project and then select the **Secret** that you provided for the database and the application.
  4. To see the password, [view the secret value](https://docs.cloud.google.com/secret-manager/docs/access-secret-version#access_a_secret_version).



### Connect to the SAP HANA database

You can connect to your HANA database by using the standard SAP tools such as SAP HANA Cockpit or SAP HANA Studio. The following information might be required for connecting to the database:

  * Hostname or IP address: Find the corresponding hostname and IP address on the Google Cloud interface for the VM instance that contains the SAP HANA database that is acting as primary or active node in the SAP HANA cluster. The VM instance name is one of the parameters configured during the deployment.

You can also connect using the DNS entry for the `CNAME` that points to the SAP HANA cluster. You can find the DNS entry on the Cloud DNS page on the Google Cloud console. Select the zone name created during the deployment or an existing zone. The `CNAME` record for SAP HANA looks similar to `db.DEPLOYMENT_NAME.gcp.sapcloud.goog`, if you create a new Cloud DNS zone for the deployment.

  * SQL Port:

    * SAP HANA system database: 3`INSTANCE_NUMBER`13
    * SAP HANA tenant database: 3`INSTANCE_NUMBER`15
    * S/4HANA tenant database: 3`INSTANCE_NUMBER`40
  * Credentials: Database users and their passwords stored in the Secret Manager. See Access system credentials.




### Connect to the SAP application

You can connect to your SAP application by using your SAP credentials. You can either connect to the SAP Message Server or directly to one of the App Servers by using the SAP Web Dispatcher.

The following information might be required for connecting to the application:

  * Hostname or IP address: Find the corresponding hostname or IP address on the Google Cloud interface for the VM instance that contains the ASCS or one of the App Servers. \- ASCS: The VM instance name is one of the parameters configured during the deployment. \- App Servers: All the application servers follow the same naming pattern, VM_PREFIXappNN. For example, ed1app11, ed1app12, and ed2app34.

You can also connect using the DNS entry for the `CNAME` that points to the active cluster node that host the message server. You can find the DNS entry on the Cloud DNS page on the Google Cloud console. Select the zone name created during the deployment or an existing zone. The `CNAME` record for SAP looks similar to `alidascs11.DEPLOYMENT_NAME.gcp.sapcloud.goog`, if you create a new Cloud DNS zone for the deployment.

  * Port:

    * Message Server: 36`INSTANCE_NUMBER`
    * App Server dispatcher: 32`INSTANCE_NUMBER`



### Verify the SAP Host Agent is receiving metrics

To verify that the Agent for SAP collects the infrastructure metrics and sends correctly to the SAP Host Agent, follow these steps:

  1. In your SAP system, enter transaction `ST06`.
  2. In the overview pane, check the availability and content of the following fields for the correct end-to-end setup of the SAP and Google monitoring infrastructure: 
     * **Cloud Provider** : `Google Cloud Platform`
     * **Enhanced Monitoring Access** : `TRUE`
     * **Enhanced Monitoring Details** : `ACTIVE`



## Next steps after deployment

The next steps after initial deployment depends on your use case and standard procedures. You might want to perform some of the following tasks before using using SAP S/4HANA instance:

  * Update licenses: newly installed systems have a temporary license that expires in 30 days. Before expiration, follow the standard SAP procedures and update the licenses in your system.
  * Update software with the latest patches
  * Configure your application and database profile parameters and configuration
  * Import configuration and data into the system
  * Install other SAP products such as SAP Fiori or SAP Solution Manager
  * Configure and back up your new SAP system 
    * [Configure Backint based backup and recovery for SAP HANA](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-backint-backup-recovery)
    * [Back up SAP HANA with disk snapshots](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/disk-snapshot-based-backup-recovery)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
