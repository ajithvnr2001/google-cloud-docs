---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/decommission-region/
title: Decommission a hybrid region \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:51:16.704645+00:00
---

# Decommission a hybrid region  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/decommission-region/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Decommission a hybrid region Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.10 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.10 keyboard_arrow_down

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
         CURRENT   NAME                                                   CLUSTER                                                AUTHINFO                                               NAMESPACE
                   gke_example-org-1_us-central1_example-cluster-1        gke_example-org-1_us-central1_example-cluster-1        gke_example-org-1_us-central1_example-cluster-1        apigee
         *         gke_example-org-1_us-central1_example-cluster-2        gke_example-org-1_us-central1_example-cluster-2        gke_example-org-1_us-central1_example-cluster-2        apigee
                   gke_example-org-1_us-west1_example-cluster-2           gke_example-org-1_us-west1_example-cluster-2           gke_example-org-1_us-west1_example-cluster-2           apigee
         
         kubectl config use-context gke_example-org-1_us-west1_example-cluster-2

  2. Delete the Apigee instance in the context you just selected with the `apigeectl` command: 
         
         Apigeectl delete --all -f overrides.yaml

  3. Verify there are no pods remaining in the Apigee namespaces: 
         
         kubectl get pods -n apigee
         kubectl get pods -n apigee-system
         kubectl get pods -n cert-manager

  4. Set the context to other existing regions and make sure the cassandra datacenter is removed from the existing ring. The output should not show the removed data center details. 
         
         kubectl exec apigee-cassandra-default-0 -n apigee  -- nodetool -u JMX_USER -pw JMX_PASSWORD status

**Note:** If the entries of the deleted datacenter are still present in the Cassandra **nodetool** output, see [ Stale references to deleted secondary region pods in Cassandra cluster](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/cassandra/cassandra-pods-not-starting-secondary-region#stale-ref-deleted-region). 


Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
