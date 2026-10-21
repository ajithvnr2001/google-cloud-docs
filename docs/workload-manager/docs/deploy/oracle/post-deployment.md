---
url: https://docs.cloud.google.com/workload-manager/docs/deploy/oracle/post-deployment/
title: Post-deployment tasks for Oracle Database workloads \u00a0|\u00a0 Workload Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:21.110212+00:00
---

# Post-deployment tasks for Oracle Database workloads  |  Workload Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workload-manager/docs/deploy/oracle/post-deployment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Workload Manager ](https://docs.cloud.google.com/workload-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/workload-manager/docs/overview)



Send feedback 

#  Post-deployment tasks for Oracle Database workloads Stay organized with collections  Save and categorize content based on your preferences. 

Before using your deployed Oracle database, we recommend that you perform the post-deployment tasks described in this document.

## Review the deployment

After successfully deploying an Oracle Database workload, you can review the deployment output and configuration on the dashboard.

### Review the deployment resources

To review the resources created during the deployment:

  1. In the Google Cloud console, go to the Workload Manager page.

[Go to Workload Manager](https://console.cloud.google.com/workloads)

  2. In the left navigation pane, click **Deployments** to open the deployment dashboard.

  3. Select the name of the deployment to open the **Deployment information** page.

  4. Click **Deployment Output** tab to view a list of all resources that were created during the deployment, the resource type, and a link to the resource (if applicable).




### Review the deployment configuration

To review the deployment configuration:

  1. In the Google Cloud console, go to the Workload Manager page.

[Go to Workload Manager](https://console.cloud.google.com/workloads)

  2. In the left navigation pane, click **Deployments** to open the deployment dashboard.

  3. Select the name of the deployment to open the **Deployment information** page.

  4. Click the **Details** tab to view the information that you've entered for the initial configuration of the deployment.




## Modify the deployment

Workload Manager doesn't support modifying a deployment that was deployed using the Google Cloud console. You must create a new deployment with the required settings and configurations. You can then [delete the deployment](https://docs.cloud.google.com/workload-manager/docs/deploy/delete) that you don't require.

You can modify a resource, such as a VM, that was created during the deployment process.

## Delete the Workload Manager service account and user-managed service account

[Workload Manager service account and user-managed service account](https://docs.cloud.google.com/workload-manager/docs/deploy/oracle/prerequisites-oracle#service-accounts-oracle) are only required for deployment. After the deployment has successfully completed, you can delete them.

**Caution:** Don't delete your [Compute Engine service account](https://docs.cloud.google.com/workload-manager/docs/deploy/oracle/prerequisites-oracle#service-accounts-oracle) because you need it to access your VMs after deployment.

Before you delete the service account, you can confirm the service account name by reviewing the **Service account** field in the **Deployment Details** tab on the **Deployment information** page.

Alternatively, you can keep these service accounts.

## Validate the Oracle Database workload deployment

After you configure and deploy the Oracle Database workload, perform the following tasks to verify that the deployment was successful:

  * Connect to the VM by using SSH
  * Run the SSH commands to validate a deployment



After you validate the deployment, connect to your Oracle database using the standard methods.

### Connect to the VM using SSH

To view additional logs or to run validation commands on the VMs created during the deployment, you must connect to the VMs using SSH.

If you have not configured external IP addresses during the deployment process, use SSH to establish a connection with a VM in the same network that has an external IP address, and then connect directly to the other VMs. For more information, see [Connect to Linux VMs using a bastion host](https://docs.cloud.google.com/compute/docs/connect/ssh-using-bastion-host#connect_to_vms).

### Run the commands to validate a deployment

To validate your Oracle Database deployment, run the following commands on the respective VM in your deployment:
    
    
    sudo su - oracle
    sqlplus -s / as sysdba <<< 'select instance_name, status from v$instance;'
    

If your database is running, the command returns `status` as `OPEN`.

## Connect to your Oracle database

This section describes how to access your deployed Oracle database.

### Access database credentials

To access your database credentials that used for the deployment, do the following:

  1. In the Google Cloud console, navigate to the **Workload Manager** page and review the deployment configuration.
  2. In the **Details** tab for the deployment, check the value displayed for **Secret name for database credentials**.
  3. Navigate to **Secret Manager** in your Google Cloud project, and then select the secret that you provided for the database and the application.
  4. To see the password, [view the secret value](https://docs.cloud.google.com/secret-manager/docs/access-secret-version#access_a_secret_version).



### Connect remotely to the Oracle database

To connect to your Oracle database, do the following:

  1. Collect the following information: 
     * Database VM hostname
     * Database name
     * Service name of your database
     * Google Cloud Project ID that contains your database VM
     * Zone of your database VM
     * Database username. If you're using Oracle Multitenant, the username is `PDBADMIN`. Otherwise, the username is `SYSTEM`.
     * Database password. You can obtain the password using the secret. See Access database credentials.
  2. Download and install a database client, such as [Oracle SQL Developer](https://www.oracle.com/database/sqldeveloper/).
  3. In your database client, create a new connection by using the following information:

     * Database type: `Oracle`
     * Username and password
     * Service name: If you're using Oracle multitenant, then the service name is `PDB`. Otherwise, it's the database name itself.

If your database client machine has direct connectivity to the database VM (such as being on the same VPC network), use the database VM hostname as the hostname.

Otherwise, set up SSH port forwarding. In this case, the hostname is `localhost`.
    
    gcloud compute ssh VM_NAME --project=PROJECT_ID --zone=ZONE -- -L 1521:localhost:1521 -N
    

Replace the following:

     * VM_NAME: the name of your database VM.
     * PROJECT_ID: the ID of your Google Cloud project which contains your database VM.
     * ZONE: the zone of your database VM.
  4. Click **Connect**.

  5. To open a SQL worksheet, in the left pane, double-click on the database name.


**Note:** By default, the `PDBADMIN` user in Oracle 19c has only `CREATE SESSION` and `CREATE PLUGGABLE DATABASE` privileges.

## Develop a regular update plan.

To ensure security, you must implement a process to regularly update your [Oracle Database and applications](https://www.oracle.com/security-alerts/), and [Oracle Linux](https://docs.oracle.com/en/operating-systems/oracle-linux/software-management/sfw-mgmt-UpdateSoftwareonEnterpriseLinux.html).

  * For Oracle Database and applications: Database patches (Release Updates or RUs) are applied using the `opatch` utility, not `DNF`. Your update plan must account for the following:

    * Scheduling downtime to apply these patches using `opatch`.
    * Patching regularly (for example, quarterly) to keep the database aligned with Oracle's recommended patch levels.
  * For Oracle Linux (OS): Define a regular maintenance window (for example, monthly or quarterly) to run `dnf update` on your VMs.




The Artifact Registry repository that the Workload Manager created during the deployment lets you download updates without requiring the internet access for your database VMs.

## View Oracle database metrics

If you enabled monitoring on your database during the deployment process, you can view the [supported metrics](https://docs.cloud.google.com/workload-manager/docs/evaluate/set-up-agent-for-oracle#supported-oracle-metrics). See [View the metrics](https://docs.cloud.google.com/workload-manager/docs/evaluate/set-up-agent-for-oracle#view-oracle-metrics).

## Next steps after deployment

The next steps after initial deployment depends on your use case and standard procedures. You might want to perform some of the following tasks before using your Oracle database:

  * Create additional users and grant appropriate privileges for database client access. [Oracle documentation](https://docs.oracle.com/en/database/oracle/oracle-database/19/admin/managing-users-and-securing-the-database.html)
  * Create tablespaces for application data, and configure user default tablespaces. [Oracle documentation](https://docs.oracle.com/en/database/oracle/oracle-database/19/admin/managing-tablespaces.html)
  * Enable auditing to track and log database actions for security and compliance purposes [Oracle documentation](https://docs.oracle.com/en/database/oracle/oracle-database/19/dbseg/introduction-to-auditing.html)
  * Migrate data from existing databases. [Oracle white paper](https://www.oracle.com/a/tech/docs/upgrade-migrate-oracle-database-2021.pdf)
  * Configure network-level connectivity for database clients. Consider tools such as [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering), [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc), [Network Connectivity Center](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center), and [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn).
  * Implement a robust backup and recovery strategy. [Oracle documentation](https://docs.oracle.com/en/database/oracle/oracle-database/19/bradv/index.html)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
