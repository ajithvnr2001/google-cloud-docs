---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/decommission-region/
title: Decommission a hybrid region \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:37:20.024858+00:00
---

# Decommission a hybrid region  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/decommission-region/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Decommission a hybrid region Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.12 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.12 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/decommission-region.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/decommission-region.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/decommission-region.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/decommission-region.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/decommission-region.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/decommission-region.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/decommission-region.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/decommission-region.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/decommission-region.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/decommission-region.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/decommission-region.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/decommission-region.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/decommission-region.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/decommission-region.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/decommission-region.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/decommission-region.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/decommission-region.html)



This guide explains the procedure to decommission a region in a multi region environment. 

Please ensure there is no live traffic going to the region you plan to delete.

##  Decommission a hybrid region 

  1. Set the kubernetes contexts to the region that needs to be decommissioned. 

List your current contexts to see the context name for each cluster: 
         
         kubectl config get-contexts

Set the context to the cluster and region you want to decommission: 
         
         kubectl config use-context CONTEXT_NAME

Where CONTEXT_NAME is the context name for the cluster and region. 

For example: 
         
         kubectl config get-contexts
           CURRENT  NAME                                                CLUSTER                                             AUTHINFO                                           NAMESPACE
                    gke_example-org-1_us-central1_example-cluster-1     gke_example-org-1_us-central1_example-cluster-1     gke_example-org-1_us-central1_example-cluster-1    apigee
           *        gke_example-org-1_us-central1_example-cluster-2     gke_example-org-1_us-central1_example-cluster-2     gke_example-org-1_us-central1_example-cluster-2    apigee
                    gke_example-org-1_us-west1_example-cluster-2        gke_example-org-1_us-west1_example-cluster-2        gke_example-org-1_us-west1_example-cluster-2       apigee
         
         kubectl config use-context gke_example-org-1_us-west1_example-cluster-2

  2. Validate all the pods in the region are in a running or completed state: 
         
         kubectl get pods -n apigee
         
         kubectl get pods -n apigee-system

  3. Validate the release of components using helm: 
         
         helm -n apigee list
         
         helm -n apigee-system list

For example:
         
         helm -n apigee list
           NAME              NAMESPACE REVISION  UPDATED                                 STATUS    CHART                         APP VERSION
           datastore         apigee    2         2024-03-29 17:08:07.917848253 +0000 UTC	deployed  apigee-datastore-1.12.0       **1.12.0**
           ingress-manager   apigee    2         2024-03-29 17:21:02.917333616 +0000 UTC	deployed  apigee-ingress-manager-1.12.0 **1.12.0**
           redis             apigee    2         2024-03-29 17:19:51.143728084 +0000 UTC	deployed  apigee-redis-1.12.0           **1.12.0**
           telemetry         apigee    2         2024-03-29 17:16:09.883885403 +0000 UTC	deployed  apigee-telemetry-1.12.0       **1.12.0**
           exampleor         apigee    2         2024-03-29 17:21:50.899855344 +0000 UTC	deployed  apigee-org-1.12.0             **1.12.0**

  4. Validate the status of the Cassandra cluster. 

List the cassandra pods:
         
         kubectl get pods -n APIGEE_NAMESPACE -l app=apigee-cassandra

For example:
         
         kubectl get pods -n apigee -l app=apigee-cassandra
           NAME                          READY    STATUS     RESTARTS    AGE
           apigee-cassandra-default-0    1/1      Running    0           2h
           apigee-cassandra-default-1    1/1      Running    0           2h
           apigee-cassandra-default-2    1/1      Running    0           2h
           apigee-cassandra-default-3    1/1      Running    0           16m
           apigee-cassandra-default-4    1/1      Running    0           14m
           apigee-cassandra-default-5    1/1      Running    0           13m
           apigee-cassandra-default-6    1/1      Running    0           9m
           apigee-cassandra-default-7    1/1      Running    0           9m
           apigee-cassandra-default-8    1/1      Running    0           8m

  5. Delete the Apigee instance in the context you just selected: 

Delete the components one at a time.

**Note:** In the following `helm delete` commands, the names given for the compnents are the release names, the names specified for the component when they were installed. For example, if you installed the datastore component with the helm command `helm install **datastore** apigee-datastore`, the release name for the component is `datastore`. If you used different release names when installing the components, specify those names when deleting them. 

For example: `helm -n apigee delete my-datastore-region-1`
         
         helm -n apigee delete datastore
         
         
         helm -n apigee delete telemetry
         
         
         helm -n apigee delete ingress-manager
         
         
         helm -n apigee delete redis
         
         
         helm -n apigee delete ORG_NAME
         

Repeat the following command for every environment:
         
         helm -n apigee delete ENV_NAME
         

Repeat the following command for every environment group:
         
         helm -n apigee delete ENV_GROUP_NAME
         
         
         helm -n apigee-system delete operator
         

  6. Verify there are no pods remaining in the Apigee namespaces: 
         
         kubectl get pods -n apigee
         kubectl get pods -n apigee-system
         

  7. Set the context to other existing regions and make sure the cassandra datacenter is removed from the existing ring. The output should not show the removed data center details. 
         
         kubectl exec apigee-cassandra-default-0 -n apigee  -- nodetool -u JMX_USER -pw JMX_PASSWORD status

**Note:** If the entries of the deleted datacenter are still present in the Cassandra **nodetool** output, see [ Stale references to deleted secondary region pods in Cassandra cluster](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/cassandra/cassandra-pods-not-starting-secondary-region#stale-ref-deleted-region). 


Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
