---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/migrate-org/
title: Migrating an org to another cluster \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:56:37.814181+00:00
---

# Migrating an org to another cluster  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/migrate-org/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Migrating an org to another cluster Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.9 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.9 (unsupported)keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/migrate-org.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/migrate-org.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/migrate-org.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/migrate-org.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/migrate-org.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/migrate-org.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/migrate-org.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/migrate-org.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/migrate-org.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/migrate-org.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/migrate-org.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/migrate-org.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/migrate-org.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/migrate-org.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/migrate-org.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/migrate-org.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/migrate-org.html)



This page describes how to migrate an Apigee hybrid org from one Kubernetes cluster to another. Some cases in which you might need to migrate an org to another cluster are the following:

  * The data center hosting the existing cluster has no more capacity, or is being decommissioned.
  * The cluster is running old infrastructure or an old version of Kubernetes, and you want to migrate to a cluster with newer infrastructure.
  * You want to move orgs from multi-org clusters into separate clusters.



Note that there are risks and limitations when migrating an org to another hybrid cluster. Read the details in the Limitations section before performing a migration.

## Limitations

The following limitations apply when migrating a hybrid org to another Kubernetes cluster:

  * There is a risk of data loss when moving org data to a new Kubernetes cluster. You should back up the data for all orgs in the Kubernetes cluster, using the [hybrid backup instructions](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/cassandra-backup-overview), before migrating an org.
  * The maximum data size supported for org migration is 5GB across all keyspaces of an org, excluding cache and quota.
  * Cache data will not be migrated. Hybrid rebuilds cache data.
  * Quota data will not be migrated. Hybrid resets quota data.
  * You can only migrate orgs to a Kubernetes cluster that contains no existing hybrid deployment. Migrating to a cluster with an existing hybrid deployment is not supported.
  * The org being migrated can only be moved to a new cluster with a single region deployment. After the single region deployment is up and running, you can follow the region expansion process, described in [Multi-region deployment](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/multi-region), to expand to other regions. 
  * The Cassandra cluster should be operating in good health across all regions.



## Migrating an org

Follow the instructions below to migrate a hybrid org from one Kubernetes cluster to another:

  1. If not already enabled, enable backups on the Kubernetes cluster containing the hybrid org to be migrated. See [Cassandra backup overview](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/cassandra-backup-overview) for information on hybrid backups.
  2. Start a hybrid backup job using the following command: 
         
         kubectl create job -n apigee --from=cronjob/apigee-cassandra-backup <backup job name>

The `<backup job name>` can be any valid container name.

  3. Once the backup job is completed, use the instructions in the following sections of [Monitoring backups](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/monitor-cassandra-backups) to verify that the backup has successfully completed: 
     * "Check the status of the backup job"
     * "Check the backup logs"
  4. After verifying that the backup was successful, make a note of the ID number at the end of the backup log. For example, a successful backup log should contain a line like the following: 
         
         INFO: completed upload for 20230207004250

Make a note of the multi-digit number at the end of the line. You will need this number later.
  5. Switch the Kubernetes context to the destination Kubernetes cluster: 
         
         kubectl config use-context <destination cluster name> # <destination cluster name>

where `<destination cluster name>` is the name of the destination Kubernetes cluster.

  6. Restore the backup data into the destination Kubernetes cluster using the instructions in [ Restoring in a single region](https://cloud.google.com/apigee/docs/hybrid/v1.9/restore-cassandra-single-region). 
     * Use the overrides.yaml file for the org that is being migrated to the destination hybrid deployment.
     * Remember to set the `restore:snapshotTimestamp` value to the multi-digit number shown by the backup log in step 4. See [ Restoring in a single region](https://cloud.google.com/apigee/docs/hybrid/v1.9/restore-cassandra-single-region).
  7. Once the restoration is complete, delete any org data, other than the data for the org being migrated, from the destination Kubernetes cluster. Hybrid backup files contain the data for all orgs, including ones you may not want to migrate. After the destination hybrid deployment is restored, you need to remove any extra org data that was copied to the deployment, using the following steps: 
     1. Verify that the current context is the correct context for the destination Kubernetes cluster: 
            
            kubectl config current-context

     2. Exec into the `apigee-cassandra-default-0` pod: 
            
            kubectl exec -it -n apigee apigee-cassandra-default-0 -- /bin/bash

     3. Execute the following command: 
            
            find /opt/apigee/data/apigee-cassandra/ -iname '*_hybrid' -not -iname '*<migrated org name>*' -type d -maxdepth 2 -printf "%f\n"

See Get the name of the migrated org for instructions on finding `<migrated org name>`.

Copy the list of all names that are shown in the output. You will need this list in step 7. f.

     4. Exit the `apigee-cassandra-default-0` pod.
     5. Create a Cassandra debug client pod using the instructions in [ Create a client container for debugging](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/cassandra/ts-cassandra#create-a-client-container-for-debugging). Move on to the next step after getting a `cqlsh` prompt.
     6. Execute the following commands in the `cqlsh` prompt: 
        * desc keyspaces;

Make sure this command returns no errors.

        * For each name in the list created in step 7. c., run the following command: 
              
              drop keyspace <name>

     7. Exit the Cassandra debug client pod.
     8. After executing the `cqlsh` commands, run the following commands on all Cassandra pods in the destination Kubernetes cluster: 
        * kubectl exec -it -n apigee  -- /bin/bash

        * find /opt/apigee/data/apigee-cassandra/ -iname '*_hybrid' -not -iname '*<migrated org name>*' -type d -maxdepth 2

See Get the name of the migrated org for instructions on finding `<migrated org name>`.

        * find /opt/apigee/data/apigee-cassandra/ -iname '*_hybrid' -not -iname '**' -type d -maxdepth 2 -exec rm -rf {} +

     9. Exit the Cassandra pod.
  8. Switch the Kubernetes context to the source Kubernetes cluster: 
         
         kubectl config use-context <source cluster name>

where `<source cluster name>` is the name of the source Kubernetes cluster.

  9. Delete the migrated org from the source Kubernetes cluster. Be sure to use the `overrides.yaml` file for the org in the delete command: 
     1. Verify the current context is the correct context for the source Kubernetes cluster: 
            
            kubectl config current-context

     2. apigeectl delete --settings virtualhost -f 

     3. apigeectl delete --all-envs -f <overrides.yaml>

     4. apigeectl delete -f <overrides.yaml> --org

     5. Exec into the apigee-cassandra-default-0 pod: 
            
            kubectl exec -it -n apigee apigee-cassandra-default-0 -- /bin/bash

     6. Execute the following command: 
            
            find /opt/apigee/data/apigee-cassandra/ -iname '*<migrated org name>_hybrid' -type d -maxdepth 2 -printf "%f\n"

See Get the name of the migrated org for instructions on finding `<migrated org name>`.

Copy the list of all the names that are shown in the output. You will need this list in step 9. j.

     7. Exit the `apigee-cassandra-default-0` pod.
     8. Create a Cassandra debug client pod using the instructions in [ Create a client container for debugging](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/cassandra/ts-cassandra#create-a-client-container-for-debugging). Move on to the next step after getting a `cqlsh` prompt.
     9. Execute the following commands at the `cqlsh` prompt: 
            
            desc keyspaces;

Make sure this command returns no errors.

     10. For each name in the list created in step 10. f., run the following command: 
            
            drop keyspace <name>;

     11. Exit the Cassandra debug client pod.
After executing the `cqlsh` commands, run the following commands on all Cassandra pods in the source Kubernetes cluster: 
     * kubectl exec -it -n apigee <cassandra pod name> -- /bin/bash

     * find /opt/apigee/data/apigee-cassandra/ -iname '*<migrated org name>_hybrid' -type d -maxdepth 2

See Get the name of the migrated org for instructions on finding `<migrated org name>`.

     * find /opt/apigee/data/apigee-cassandra/ -iname '*<migrated org name>_hybrid' -type d -maxdepth 2 -exec rm -rf {} +

  10. Exit the Cassandra pod.



### Get the name of the migrated org

Several of the steps in the procedure described in the previous section require the name of the migrated org. To get the migrated org name, do the following:

  1. Get the org name from the org's overrides.yaml file. Make sure to check the overrides.yaml file for the org being migrated.
  2. If the org name contains any dashes "-", replace all dashes "-" with underscores "_".



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
