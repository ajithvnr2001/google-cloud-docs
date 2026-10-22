---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/decommission-org/
title: Decommission a hybrid org \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:44:57.858258+00:00
---

# Decommission a hybrid org  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/decommission-org/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Decommission a hybrid org Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.17 (latest)keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/decommission-org.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/decommission-org.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/decommission-org.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/decommission-org.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/decommission-org.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/decommission-org.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/decommission-org.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/decommission-org.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/decommission-org.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/decommission-org.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/decommission-org.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/decommission-org.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/decommission-org.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/decommission-org.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/decommission-org.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/decommission-org.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/decommission-org.html)



This document outlines the steps to decommission an org from a hybrid deployment. Decommissioning an org means deleting all data related to the org across all Cassandra pods in all Kubernetes clusters. 

Please ensure there is no live traffic going to the org you plan to remove.

## Limitations

Only one org can be decommissioned at a time. Decommissioning multiple orgs simultaneously is not supported. 

## Get the org name

Some commands in these instructions require you to use a properly formatted org name.

To get the org name for use in commands on this page:

  1. Retrieve the org name from the org's `overrides.yaml` file.
  2. If the org name contains any dashes ("-"), replace them with underscores ("_").



## Instructions

Follow these instructions to decommission an org from a hybrid deployment.

  1. Back up the org 
     1. If it's not already enabled, enable backups on the hybrid deployment. In multi-region setups, use the hybrid deployment operating in the primary region. See [Cassandra backup overview](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/cassandra-backup-overview) for information on hybrid backups. 
     2. Trigger a hybrid backup job using the following command: 
            
            kubectl create job -n APIGEE_NAMESPACE --from=cronjob/apigee-cassandra-backup BACKUP_JOB_NAME

The BACKUP_JOB_NAME can be any valid container name. 

     3. Once the backup job completes, use the "Check the status of the backup job" and "Check the backup logs" instructions in [Monitoring backups](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/monitor-cassandra-backups) to verify the backup was successful. 

  2. **(Optional)** If you have configured Apigee Telemetry (Metrics and Logger) on the org to be deleted, follow these steps to reconfigure them so that the metrics and log data apply to a new org/project.
     1. Run this command for the org where you want to send the data. Be sure to use the `overrides.yaml` file for the org. For example, if the org to be decommissioned is "test-dev" the `overrides.yaml` file should contain an `org: test-dev` org field. 
            
            helm upgrade telemetry apigee-telemetry/ \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f OVERRIDES_FILE.yaml
            

**Note:** If you see an error saying `Error: UPGRADE FAILED: "_ORG_NAME_ " has no deployed releases`, replace `upgrade` with `install` and try the command again.
     2. Run this command, making sure to use the correct org/project: 
            
            kubectl -n APIGEE_NAMESPACE get apigeetelemetry apigee-telemetry -oyaml | grep `gcpProjectID:`

  3. Delete the org's Kubernetes resources from the hybrid deployment. 
     1. Verify the current context is the correct context for the source Kubernetes cluster: 
            
            kubectl config current-context

If needed, set the Kubernetes context.

List your current contexts to see the context name for each cluster: 
            
            kubectl config get-contexts

Set the context to the cluster and region you want to decommission: 
            
            kubectl config use-context CONTEXT_NAME

Where CONTEXT_NAME is the context name for the cluster and region. 

For example: 
            
            kubectl config get-contexts
                CURRENT   NAME                                                   CLUSTER                                                AUTHINFO                                               NAMESPACE
                          gke_example-org-1_us-central1_example-cluster-1        gke_example-org-1_us-central1_example-cluster-1        gke_example-org-1_us-central1_example-cluster-1        apigee
                *         gke_example-org-1_us-central1_example-cluster-2        gke_example-org-1_us-central1_example-cluster-2        gke_example-org-1_us-central1_example-cluster-2        apigee
                          gke_example-org-1_us-west1_example-cluster-2           gke_example-org-1_us-west1_example-cluster-2           gke_example-org-1_us-west1_example-cluster-2           apigee
            
                kubectl config use-context gke_example-org-1_us-west1_example-cluster-2

     2. Delete the virtualhost. 

Repeat this for each environment group:
            
            helm -n APIGEE_NAMESPACE delete ENV_GROUP_NAME
            

     3. Delete the environments. Repeat this for each environment: 
            
            helm -n APIGEE_NAMESPACE delete ENV_NAME
            

     4. Delete the Apigee org. 
            
            helm -n APIGEE_NAMESPACE delete ORG_NAME
            

  4. Delete the org data from the hybrid deployment. **Once this step is complete all org data will be gone from the hybrid deployment.**
     1. Exec into the `apigee-cassandra-default-0` pod: 
            
            kubectl exec -it -n APIGEE_NAMESPACE apigee-cassandra-default-0 -- /bin/bash
            

     2. Execute the following command. Copy the list of all the names that are shown in the output. This list will be needed later. 
            
            find /opt/apigee/data/apigee-cassandra/ -iname '*ORG_NAME_hybrid' -type d -maxdepth 2 -printf "%f\n"

See Get org name for instructions on how to find and prepare the ORG_NAME. 

Exit from the `apigee-cassandra-default-0` pod.

     3. Create a Cassandra debug client pod as described in [Create a client container for debugging](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/cassandra/ts-cassandra#create-a-client-container-for-debugging). Move on to the next step after getting a `cqlsh` prompt. 
     4. Execute the following commands in the `cqlsh` prompt: 
            
            desc keyspaces;

Make sure this command returns no errors.

For each name in the list created earlier from the `apigee apigee-cassandra-default-0`, run the following commands:
            
            drop keyspace KEYSPACE_NAME;

Exit from the Cassandra debug client pod.

     5. Perform a rolling restart of all Cassandra pods. Restarting the Cassandra pods can be done in any order as long as only one Cassandra pod is restarted at a time. For multi-region deployments, perform a rolling restart on all Cassandra pods in each hybrid region. 

Run the following command and verify the state shows "Running":
            
            kubectl get apigeeds -n APIGEE_NAMESPACE

Restart a single Cassandra pod with the following command:
            
            kubectl delete pod -n APIGEE_NAMESPACE CASSANDRA_POD_NAME

Wait for the pod to reach `Running` state using:
            
            kubectl get pods -n APIGEE_NAMESPACE

Restart the next Cassandra pod.

     6. After executing the `cqlsh` commands, run the following commands on all Cassandra pods in the hybrid deployment. For multi-region hybrid deployments, run the commands on all Cassandra pods in all hybrid regions. 
            
            kubectl exec -it -n APIGEE_NAMESPACE CASSANDRA_POD_NAME -- /bin/bash
            
            find /opt/apigee/data/apigee-cassandra/ -iname '*ORG_NAME_hybrid' -type d -maxdepth 2

See Get org name for instructions on how to find and prepare the ORG_NAME.
            
            find /opt/apigee/data/apigee-cassandra/ -iname '*ORG_NAME_hybrid' -type d -maxdepth 2 -exec rm -rf {} +

     7. Exit from the Cassandra pod.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
