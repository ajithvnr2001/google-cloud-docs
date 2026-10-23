---
url: https://docs.cloud.google.com/sql/docs/postgres/advanced-dr-logical-failover-slot/
title: Advanced disaster recovery (DR) with logical failover slot \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:13:50.596348+00:00
---

# Advanced disaster recovery (DR) with logical failover slot  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/advanced-dr-logical-failover-slot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Advanced disaster recovery (DR) with logical failover slot Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use logical failover slot to configure Cloud SQL for PostgreSQL's logical replication to work seamlessly with [advanced disaster recovery (DR)](https://docs.cloud.google.com/sql/docs/postgres/intro-to-cloud-sql-disaster-recovery#advanced-dr) operations, specifically switchover and replica failover on instances with Cloud SQL Enterprise Plus edition.

Cloud SQL's advanced disaster recovery (DR) features enable robust disaster recovery capabilities. When combined with PostgreSQL's logical replication, it is crucial that the replication stream remains unbroken after a switchover or a replica failover.

Using advanced disaster recovery (DR) with PostgreSQL's logical replication, you can make sure that your logical subscribers experience zero data loss and can automatically reconnect to the new primary instance after a disaster recovery event, thus ensuring business continuity.

You can use this functionality on Cloud SQL instances that have the following configuration:

  * PostgreSQL version 17 or later
  * Cloud SQL Enterprise Plus edition
  * Private services access

We recommend using the private services access domain name service (DNS) write endpoint to enable automatic logical subscriber reconnections.




## Before you begin

  * [Install ](https://docs.cloud.google.com/sdk/docs/install)[gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

You must use version 502.0.0 or later. To check the version of the Google Cloud SDK, run `gcloud --version`. To update the Google Cloud SDK, run `gcloud components update`.

  * [Create a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) or select an existing project.

  * Grant the required Identity and Access Management (IAM) roles and permissions.

    * To create a project: [Project Creator](https://docs.cloud.google.com/resource-manager/docs/access-control-proj#resourcemanager.projectCreator) (`roles/resourcemanager.projectCreator`)

    * To create and manage Cloud SQL instances: [Cloud SQL Admin](https://docs.cloud.google.com/sql/docs/postgres/iam-roles#roles) (`roles/cloudsql.admin`)

    * To create and manage Compute Engine VMs: [Compute Instance Admin (v1)](https://docs.cloud.google.com/compute/docs/access/iam#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) and [Compute Viewer](https://docs.cloud.google.com/compute/docs/access/iam#compute.viewer) (`roles/compute.networkViewer`)

    * To create VPC networks: [Network Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin) (`roles/compute.networkAdmin`)

[ Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)

For more information, see [Roles and permissions](https://docs.cloud.google.com/sql/docs/postgres/roles-and-permissions).

To learn how to grant IAM roles and permissions, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).




## Set up advanced disaster recovery (DR) with logical replication

The process to set up advanced disaster recovery (DR) with PostgreSQL's logical replication has the following high-level steps:

  1. Set up environment variables and bastion VM.
  2. Create and set up the primary instance.
  3. Create and designate DR replica.
  4. Create and set up a logical subscriber instance.
  5. Create a logical replication subscription.
  6. Perform a switchover or replica failover.
  7. Validate replication.
  8. Clean up orphaned replication slot on the new replica.
  9. Optional: Perform switchback.



### Set up environment variables and bastion VM

  1. Set the following environment variables.
         
         # Project
         export PROJECT="PROJECT_ID"
         
         # Instance names
         export PRIMARY_INSTANCE_NAME="PRIMARY_INSTANCE"
         export DR_REPLICA_NAME="DR_REPLICA"
         export SUBSCRIBER_INSTANCE_NAME="SUBSCRIBER_INSTANCE"
         export BASTION_VM_NAME="BASTION_VM"
         
         # Regions and zones
         export PRIMARY_REGION="PRIMARY_REGION"
         export REPLICA_REGION="REPLICA_REGION"
         export SUBSCRIBER_REGION="SUBSCRIBER_REGION"
         export VM_ZONE="VM_ZONE"
         
         # Network
         export NETWORK_NAME="NETWORK"
         
         # Credentials
         export POSTGRES_PASSWORD="PASSWORD"
         
         # Set gcloud project
         gcloud config set project PROJECT_ID
         

Replace the following:

     * PROJECT_ID: the ID of your project.
     * PRIMARY_INSTANCE: the name of the primary Cloud SQL instance.
     * DR_REPLICA: the name of the replica.
     * SUBSCRIBER_INSTANCE: the name of the subscriber instance.
     * BASTION_VM: the name of the bastion VM.
     * PRIMARY_REGION: the region where the primary instance is located.
     * REPLICA_REGION: the region where the replica is located. Replica must be in a different region than that of the primary instance.
     * SUBSCRIBER_REGION: the region where the subscriber is located.
     * VM_ZONE: the zone where the bastion VM is located.
     * NETWORK: the name of your VPC network.
     * PASSWORD: the password for the `postgres` user.
  2. Create a Compute Engine bastion VM.

Cloud SQL instances use private IP. Therefore, create a Compute Engine bastion host VM in your VPC network.
         
         gcloud compute instances create $BASTION_VM_NAME \
           --zone=$VM_ZONE \
           --machine-type=e2-small \
           --network=projects/$PROJECT_ID/global/networks/$NETWORK_NAME \
           --image-project=debian-cloud \
           --image-family=debian-11 \
           --project=$PROJECT
         

  3. Connect to the bastion VM.
         
         gcloud compute ssh $BASTION_VM_NAME \
           --zone=$VM_ZONE \
           --project=$PROJECT
         

  4. On the bastion VM, install the PostgreSQL client.
         
         sudo apt-get update
         sudo apt-get install -y postgresql-client
         exit
         




The PostgreSQL commands in the subsequent steps are to be run from the bastion VM.

### Create and set up the primary instance

  1. Create the primary Cloud SQL instance.
         
         gcloud sql instances create $PRIMARY_INSTANCE_NAME \
           --database-version=POSTGRES_17 \
           --edition=ENTERPRISE_PLUS \
           --region=$PRIMARY_REGION \
           --tier=db-perf-optimized-N-2 \
           --no-assign-ip \
           --network=projects/$PROJECT/global/networks/$NETWORK_NAME \
           --project=$PROJECT
         

  2. Enable logical decoding.
         
         gcloud sql instances patch $PRIMARY_INSTANCE_NAME \
           --database-flags=cloudsql.logical_decoding=on \
           --project=$PROJECT
         

  3. Set password for the `postgres` user on primary.
         
         gcloud sql users set-password postgres \
           --instance=$PRIMARY_INSTANCE_NAME \
           --password="$POSTGRES_PASSWORD" \
           --project=$PROJECT
         

  4. Connect to the primary instance from the bastion VM.

     1. Retrieve the private IP address of the primary instance.
            
            gcloud sql instances describe $PRIMARY_INSTANCE_NAME \
              --format="value(ipAddresses[0].ipAddress)" \
              --project=$PROJECT
            

Copy and keep the private IP address of the primary instance.

     2. SSH to your bastion VM.
            
            gcloud compute ssh $BASTION_VM_NAME --zone=$VM_ZONE --project=$PROJECT
            

     3. From the bastion VM, connect to the primary instance.
            
            psql -h PRIMARY_PRIVATE_IP -U postgres
            

Replace PRIMARY_PRIVATE_IP with the private IP of the primary instance that you retrieved in **Step 4.a** of this procedure.

     4. When prompted for password, enter the variable `$POSTGRES_PASSWORD`.

Your bastion VM is now connected to the primary instance through PostgreSQL.

  5. Grant permissions and create publication.

     1. Grant `REPLICATION` privilege to the `postgres` user.
            
            ALTER USER postgres WITH REPLICATION;
            

     2. Grant necessary privileges on the public schema and tables.
            
            GRANT SELECT ON ALL TABLES IN SCHEMA public TO postgres;
            

     3. Create the publication for all tables.
            
            CREATE PUBLICATION my_publication FOR ALL TABLES;
            

     4. Type `exit` to quit PostgreSQL, and then `exit` again to close the SSH session of the bastion VM.




### Create and designate disaster recovery replica (DR replica)

  1. Create a DR replica.
         
         gcloud sql instances create $DR_REPLICA_NAME \
           --master-instance-name=$PRIMARY_INSTANCE_NAME \
           --edition=ENTERPRISE_PLUS \
           --tier=db-perf-optimized-N-2 \
           --region=$REPLICA_REGION \
           --no-assign-ip \
           --network=projects/$PROJECT/global/networks/$NETWORK_NAME \
           --project=$PROJECT
         

  2. Designate this replica as the DR replica.
         
         gcloud sql instances patch $PRIMARY_INSTANCE_NAME \
           --failover-dr-replica-name=$DR_REPLICA_NAME \
           --project=$PROJECT
         

  3. Configure the DR replica for logical slot synchronization.
         
         gcloud sql instances patch $DR_REPLICA_NAME \
           --database-flags="^:^cloudsql.logical_decoding=on:hot_standby_feedback=on:sync_replication_slots=on:cloudsql.logical_slot_sync_dbname=postgres" \
           --project=$PROJECT
         

  4. Configure synchronous replication between the primary instance and the DR replica.

To prevent potential data loss on the logical subscriber in the event of a sudden primary instance outage and subsequent replica failover, we recommend that you configure synchronous replication between the primary instance and the DR replica.

Setting `cloudsql.synchronized_standby_replicas` on the primary instance forces the primary instance's logical replication Write-Ahead Log (WAL) sender to wait until the DR replica has received and flushed the WAL for a given transaction before sending that transaction to the logical subscriber. This makes sure that the state of the DR replica is always ahead of or equal to the state of the logical subscriber.
         
         gcloud sql instances patch $PRIMARY_INSTANCE_NAME \
           --database-flags="^:^cloudsql.logical_decoding=on:cloudsql.synchronized_standby_replicas=$DR_REPLICA_NAME" \
           --project=$PROJECT
         

**Note:** The `--database-flags="^:^cloudsql.logical_decoding=on:cloudsql.synchronized_standby_replicas=$DR_REPLICA_NAME"` is crucial for protecting against data loss during an unexpected replica failover. The planned switchover operation has its own mechanisms to make sure that the replica is fully synchronized before promoting it. Even though this flag is not mandatory for switchover, it provides an additional layer of safety for all disaster recovery scenarios.



### Create and set up a logical subscriber instance

  1. Create a subscriber instance.
         
         gcloud sql instances create $SUBSCRIBER_INSTANCE_NAME \
           --database-version=POSTGRES_17 \
           --tier=db-perf-optimized-N-2 \
           --region=$SUBSCRIBER_REGION \
           --no-assign-ip \
           --network=projects/$PROJECT/global/networks/$NETWORK_NAME \
           --project=$PROJECT
         

  2. Enable logical decoding on the subscriber.
         
         gcloud sql instances patch $SUBSCRIBER_INSTANCE_NAME \
           --database-flags=cloudsql.logical_decoding=on \
           --project=$PROJECT
         




### Create a logical replication subscription

  1. Retrieve the primary instance's private services access write endpoint.
         
         gcloud sql instances describe $PRIMARY_INSTANCE_NAME \
           --format="value(replicationCluster.psaWriteEndpoint)" \
           --project=$PROJECT
         

Copy and keep the write endpoint.

  2. Connect to the subscriber instance.

     1. Update the password for the `postgres` user of the subscriber instance.
            
            gcloud sql users set-password postgres \
              --instance=$SUBSCRIBER_INSTANCE_NAME \
              --password="$POSTGRES_PASSWORD" \
              --project=$PROJECT
            

     2. Retrieve the private IP address of the subscriber instance.
            
            gcloud sql instances describe $SUBSCRIBER_INSTANCE_NAME \
              --format="value(ipAddresses[0].ipAddress)" \
              --project=$PROJECT
            

Copy and keep the private IP address.

     3. SSH to the bastion VM.
            
            gcloud compute ssh $BASTION_VM_NAME \
              --zone=$VM_ZONE \
              --project=$PROJECT
            

     4. From the bastion VM, connect to the subscriber instance through PostgreSQL.
            
            psql -h SUBSCRIBER_PRIVATE_IP -U postgres
            

Replace SUBSCRIBER_PRIVATE_IP with the private IP of the subscriber instance that you copied in **Step 2.b** of this procedure.

     5. When prompted for password, enter the variable `$POSTGRES_PASSWORD`.

  3. Create a subscription.
         
         CREATE SUBSCRIPTION my_subscription
         CONNECTION 'host=DR_CLUSTER_PSA_DNS_WRITE_ENDPOINT port=5432 dbname=postgres user=postgres password=PASSWORD'
         PUBLICATION my_publication
         WITH (failover = true);
         

Replace the following:

     * DR_CLUSTER_PSA_DNS_WRITE_ENDPOINT: the private services access write endpoint that you copied in **Step 1** of this procedure.
     * PASSWORD: the value of the variable `${POSTGRES_PASSWORD}`.
  4. Exit PostgreSQL and the bastion VM SSH session.

  5. Optional. Verify the slot persistence on the DR replica.

This transition to persistent (`temporary = false`) typically occurs quickly, often within seconds if the primary has low activity. Under heavy write load on the primary, this process might take longer, generally around one minute. The slot should be persistent after completing these manual commands.

     1. Get the private IP address of the DR replica.
            
            gcloud sql instances describe $DR_REPLICA_NAME \
              --format="value(ipAddresses[0].ipAddress)" \
              --project=$PROJECT
            

Copy and keep the private IP address of the DR replica.

     2. SSH to the bastion VM.
            
            gcloud compute ssh $BASTION_VM_NAME \
              --zone=$VM_ZONE \
              --project=$PROJECT
            

     3. From the bastion VM, connect to the DR replica.
            
            psql -h DR_REPLICA_PRIVATE_IP -U postgres
            

Replace DR_REPLICA_PRIVATE_IP with the private IP address of the DR replica that you retrieved in **Step 5.a** of this procedure.

     4. When prompted for password, enter the variable `$POSTGRES_PASSWORD`.

     5. Check the slot status.
            
            SELECT slot_name, slot_type, temporary, failover, synced
            FROM pg_replication_slots
            WHERE slot_type = 'logical' AND failover = true;
            

Wait for the `temporary` column to become `f`. This usually takes less than a minute.

     6. Exit PostgreSQL and the bastion VM SSH session.




### Perform a switchover or replica failover

Choose the operation you want to perform based on your scenario:

  * **Switchover (planned role reversal)** : Choose this for planned maintenance, disaster recovery testing, or to switch roles when the primary instance is online and healthy. This operation ensures zero data loss for the physical replication.
        
        gcloud sql instances switchover $DR_REPLICA_NAME \
          --project=$PROJECT
        

**Note:** The operation is complete when the command returns.
  * **Replica Failover (disaster recovery)** : Choose this when the primary instance is unavailable or unresponsive. This operation promotes the DR replica to primary. To minimize the risk of data loss for the logical subscriber, make sure that the `cloudsql.synchronized_standby_replicas` was set on the primary instance as recommended in Create and designate disaster recovery replica (DR replica).
        
        gcloud sql instances promote-replica $DR_REPLICA_NAME \
          --failover \
          --project=$PROJECT
        

The promotion of `$DR_REPLICA_NAME` happens quickly. However, the original primary instance (`$PRIMARY_INSTANCE_NAME`) is only reconfigured as a replica of the new primary once it comes back online. You can track this by looking for the `RECONFIGURE_OLD_PRIMARY` operation to complete on `$PRIMARY_INSTANCE_NAME` in the operations log. Run the following command:
        
        gcloud sql operations list --instance=$PRIMARY_INSTANCE_NAME --project=$PROJECT --limit=10`
        

The disaster recovery setup is fully restored only after this phase completes.




After either operation, the subscriber automatically reconnects to the new primary `$DR_REPLICA_NAME` through the private services access write endpoint.

#### Flag management

Cloud SQL's workflows automatically manage the necessary database flags on both instances within the disaster recovery cluster during and after the switchover and replica failover operations including the following:

  * The logical slot synchronization flags (`cloudsql.logical_decoding`, `hot_standby_feedback`, `sync_replication_slots`, `cloudsql.logical_slot_sync_dbname`) are ensured to be correct on the instance that becomes the new replica.
  * The `cloudsql.synchronized_standby_replicas` flag on the instance that becomes the new primary is automatically updated to point to the name of the new DR replica.



You don't need to manually re-apply or change these flags after a switchover or replica failover operation. Cloud SQL maintains the correct configuration for the primary and replica roles.

### Validate replication

  1. Check the status of the subscriber.

     1. From the bastion VM, run the following command.
            
            psql -h SUBSCRIBER_PRIVATE_IP -U postgres
            

Replace SUBSCRIBER_PRIVATE_IP with the private IP address of the subscriber instance.

     2. On the subscriber instance, run the following command.
            
            SELECT subname, pid IS NOT NULL AS is_active
            FROM pg_stat_subscription;
            

The status should be `streaming`.

  2. Check the status of the new primary's replication slot. The new primary is the former DR replica (`$DR_REPLICA_NAME`).

     1. Get the private IP address of the new primary.
            
            gcloud sql instances describe $DR_REPLICA_NAME \
              --project=$PROJECT --format="value(ipAddresses[0].ipAddress)"
            

Copy and keep the private IP address of the new primary.

     2. SSH to the bastion VM.
            
            psql -h NEW_PRIMARY_PRIVATE_IP -U postgres
            

Replace the NEW_PRIMARY_PRIVATE_IP with the private IP address of the new primary that you copied in the previous step.

     3. On the new primary instance, run the following commands.
            
            SELECT
                slot_name,
                slot_type,
                active,
                synced,
                active_pid,
                pg_size_pretty(pg_wal_lsn_diff(pg_current_wal_lsn(), confirmed_flush_lsn)) AS replication_lag
            FROM pg_replication_slots
            WHERE slot_type = 'logical';
            

The slot (for example, `my_subscription`) should be `active = t`.
            
            SELECT
                application_name,
                state
            FROM pg_stat_replication;
            

`pg_stat_replication` should show the subscriber connected.




### Clean up orphaned replication slot on the new replica

After the switchover and failover operation complete, the original primary instance (`$PRIMARY_INSTANCE_NAME`) is now a replica. This new replica instance still retains the original logical replication slot named `my_subscription` on its disk. This `my_subscription` slot is now orphaned because the subscriber is expected to connect to the new primary (`$DR_REPLICA_NAME`) through the private services access write endpoint.

Cloud SQL doesn't automatically remove this orphaned slot from the new replica. This is because Cloud SQL can't determine if the subscriber was configured to use the instance's IP address instead of the private services access write endpoint. The subscriber might still be attempting to connect to this old slot on the new replica until the subscription is manually altered. Automatically dropping the slot could break such configurations.

The presence of this orphaned slot on the new replica (`$PRIMARY_INSTANCE_NAME`) causes the `slotsync` worker process on this instance to generate errors in the logs. You might see an error message like the following in the `postgres.log` of the new replica. This error keeps repeating as the `slotsync` worker keeps trying.
    
    
    ERROR: exiting from slot synchronization because same name slot "my_subscription" already exists on the standby
    

To prevent such errors and to let the `slotsync` worker correctly establish a new synchronized version of the `my_subscription` slot on this replica, you need to manually drop the orphaned slot. This ensures this instance is properly prepared if you intend to switchback in the future.

  1. Retrieve the private IP address of the new replica (`$PRIMARY_INSTANCE_NAME`).
         
         gcloud sql instances describe $PRIMARY_INSTANCE_NAME \
           --project=$PROJECT --format="value(ipAddresses[0].ipAddress)"
         

Copy and keep the private IP address of the new replica.

  2. SSH to the bastion VM.
         
         gcloud compute ssh $BASTION_VM_NAME \
           --zone=$VM_ZONE \
           --project=$PROJECT
         

  3. From the bastion VM, connect to the new replica.
         
         psql -h NEW_REPLICA_IP -U postgres
         

Replace the NEW_REPLICA_IP with the IP address of the new replica that you copied in **Step 1** of this procedure.

  4. When prompted for password, enter the variable `$POSTGRES_PASSWORD`.

  5. On the new replica (`$PRIMARY_INSTANCE_NAME`), drop the orphaned slot.
         
         SELECT slot_name, slot_type, temporary, failover, synced, active
         FROM pg_replication_slots
         WHERE slot_name = 'my_subscription';
         

Confirm that the slot exists with `synced = false` and `active = false`, and then drop it.
         
         SELECT pg_drop_replication_slot('my_subscription');
         

The orphaned slot is removed.




#### Automatic slot re-synchronization

Once the orphaned slot is dropped, the `slotsync` worker on the new replica (`$PRIMARY_INSTANCE_NAME`) automatically connects to the new primary (`$DR_REPLICA_NAME`) in its next cycle. It creates a new local `my_subscription` slot that is synchronized with the new primary's active slot.

You can see messages in the new replica's `postgres.log` indicating success, similar to the following:
    
    
    LOG: newly created slot "my_subscription" is sync-ready now
    

The new synced slot has `failover=true` and eventually becomes persistent (`temporary=false`), ensuring that if you switchback later, this instance is ready.

### Optional: Perform switchback

  1. Now, switch back, making `$PRIMARY_INSTANCE_NAME` the primary instance again.
         
         gcloud sql instances switchover $PRIMARY_INSTANCE_NAME \
           --project=$PROJECT
         

  2. Perform verification after switchback.

     1. Check the status of the subscriber instance.
            
            SELECT subname, pid IS NOT NULL AS is_active
            FROM pg_stat_subscription;
            

The subscription should still be active, that is, `is_active = t`.

     2. Check the status of the new primary's (`$PRIMARY_INSTANCE_NAME`) slot.
            
            SELECT slot_name, active FROM pg_replication_slots WHERE slot_type = 'logical';
            SELECT * FROM pg_stat_replication;
            

The slot should be active and the subscriber connected.




## Troubleshoot

Issue | Troubleshooting  
---|---  
Error on the new replica (that is, the old primary instance) after the switchover: `"exiting from slot synchronization because same name slot already exists on the standby"` | Follow the steps in Clean up orphaned replication slot on the new replica.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
