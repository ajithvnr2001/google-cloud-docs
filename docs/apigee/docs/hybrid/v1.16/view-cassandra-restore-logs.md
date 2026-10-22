---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/view-cassandra-restore-logs/
title: Viewing restore logs \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:47:41.553046+00:00
---

# Viewing restore logs  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/view-cassandra-restore-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Viewing restore logs Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.16 of the Apigee hybrid documentation. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.16 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/view-cassandra-restore-logs.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/view-cassandra-restore-logs.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/view-cassandra-restore-logs.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/view-cassandra-restore-logs.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/view-cassandra-restore-logs.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/view-cassandra-restore-logs.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/view-cassandra-restore-logs.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/view-cassandra-restore-logs.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/view-cassandra-restore-logs.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/view-cassandra-restore-logs.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/view-cassandra-restore-logs.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/view-cassandra-restore-logs.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/view-cassandra-restore-logs.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/view-cassandra-restore-logs.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/view-cassandra-restore-logs.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/view-cassandra-restore-logs.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/view-cassandra-restore-logs.html)



This page describes how you can check the restore job logs to confirm completion and validate the restore.

##  Verifying completion 

To verify that the restore operation completed successfully: 

  1. Use the following command to check if the restore operation completed without error: 
         
         kubectl get pods -n -l job-name=apigee-cassandra-restore
         

The output is similar to the following: 
         
         NAME                               READY     STATUS      RESTARTS   AGE
         apigee-cassandra-restore-6tttv     0/1       Completed   0          23m

  2. Use the following command to check if the cassandra replicas are up and running: 
         
         kubectl get pods -n APIGEE_NAMESPACE -l app=apigee-cassandra
         

The output is similar to the following: 
         
         NAME                           READY     STATUS      RESTARTS   AGE
         apigee-cassandra-default-0     1/1       Running     0          24m
         apigee-cassandra-default-1     1/1       Running     0          23m
         apigee-cassandra-default-2     1/1       Running     0          22m




##  Viewing restore logs 

To view the restore logs of a Kubernetes pod, run the `kubectl logs -f <pod_name> -n <namespace>` command: 
    
    
    kubectl logs -f CASSANDRA_POD_NAME -n APIGEE_NAMESPACE
    

For example:
    
    
    kubectl logs -f apigee-cassandra-restore-b4lgf -n apigee
    

##  Validating restore 

Upon completing the restore operation, you can use the control plane to confirm that your organization's developers, apps, and API products were restored correctly.

To view the restored data: 

  1. On the command line, get or refresh your gcloud authentication credentials, as the following example shows: 
         
         TOKEN=$(gcloud auth print-access-token)

  2. Use the following command to validate your organization's data, where APIGEE_ORG is an Apigee organization deployed in the cluster: 
     * For developer data: 

### No data residency
           
           curl -s -H "Authorization: Bearer $TOKEN" https://apigee.googleapis.com/v1/organizations/APIGEE_ORG/developers

### Data residency
           
           curl -s -H "Authorization: Bearer $TOKEN" https://CONTROL_PLANE_LOCATION-apigee.googleapis.com/v1/organizations/APIGEE_ORG/developers

     * For apps data: 

### No data residency
           
           curl -s -H "Authorization: Bearer $TOKEN" https://apigee.googleapis.com/v1/organizations/APIGEE_ORG/apps

### Data residency
           
           curl -s -H "Authorization: Bearer $TOKEN" https://CONTROL_PLANE_LOCATION-apigee.googleapis.com/v1/organizations/APIGEE_ORG/apps

     * For API product data: 

### No data residency
           
           curl -s -H "Authorization: Bearer $TOKEN" https://apigee.googleapis.com/v1/organizations/APIGEE_ORG/apiproducts

### Data residency
           
           curl -s -H "Authorization: Bearer $TOKEN" https://CONTROL_PLANE_LOCATION-apigee.googleapis.com/v1/organizations/APIGEE_ORG/apiproducts


**Note** : Confirm that your APIs are working as expected before adding a restored cluster to your traffic.

##  DNS Configuration for new cluster and traffic cutover 

Once you are satisfied with validation, redirect the traffic to the new cluster and change the dns entry to new ingress `EXTERNAL-IP` address. 

Get the `EXTERNAL-IP` with the following command: 
    
    
    kubectl get svc -n istio-system
    
    
    NAME                       TYPE           CLUSTER-IP     **EXTERNAL-IP**    PORT(S)                                                                      AGE
    istio-ingressgateway       LoadBalancer   10.11.123.45   **34.56.78.90**   15021:32225/TCP,80:32208/TCP,443:31942/TCP,15012:32689/TCP,15443:31936/TCP   1d

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
