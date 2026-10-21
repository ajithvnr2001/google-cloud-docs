---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/concurrent-operations/
title: Troubleshoot concurrent operations \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:53:04.990900+00:00
---

# Troubleshoot concurrent operations  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/concurrent-operations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Troubleshoot concurrent operations Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

When you try to modify your Google Kubernetes Engine (GKE) cluster or its node pools, your action might be temporarily blocked because another operation is running. This issue can delay critical updates, cluster administration, and application deployments.

Use this page to learn how to identify the operation that's running. Understanding the active operation helps you estimate the delay and determine when to retry your action.

This information is important for both Application developers, who might encounter these limits when deploying or modifying applications, and for Platform admins and operators, who manage the overall cluster lifecycle, upgrades, and need to troubleshoot blocked administrative tasks. For more information about the common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Understand concurrent operation errors

In GKE, a cluster operation is an action that modifies the state of your cluster's control plane or its node pools. These operations are managed by GKE and can be initiated by you or by GKE for maintenance purposes. Common cluster operations include the following:

  * Creating or deleting the cluster.
  * Upgrading the cluster's control plane version.
  * Creating, updating, resizing, or deleting node pools.
  * Modifying cluster-level settings, such as enabling or disabling features.
  * Automatic control plane repairs initiated by GKE.



When you perform operations on your clusters, you might see error messages similar to the following:
    
    
    Cluster is running incompatible operation OPERATION_NAME
    
    
    
    Cluster is currently being created, deleted, updated or repaired and cannot be updated
    
    
    
    Operation OPERATION_NAME is currently ACTIONING cluster CLUSTER_NAME. Please wait and try again once it is done
    

These errors can include the following values:

  * `OPERATION_NAME`: the unique ID for an operation that's already running on your cluster. Use this name to track the status of this pre-existing operation that's blocking your new operation from starting.
  * `ACTIONING`: the action that is being performed on the cluster. For example, `Creating` or `Updating`.
  * `CLUSTER_NAME`: the name of the cluster that the operation is targeting.



These errors occur because GKE limits how many operations can run at the same time to prevent conflicts. Generally, GKE permits only one operation at the cluster level or one operation per node pool to run concurrently. GKE also performs its own automatic actions, such as control plane upgrades, which count toward this limit and can temporarily block you from starting a new task.

## Resolve concurrent operation errors

If you receive an error that indicates that another operation is in progress, identify the ongoing task and wait for it to finish:

  1. If you don't know the name of the blocking operation, list all ongoing and pending operations for your cluster:
         
         gcloud container operations list \
              --location=LOCATION \
              --filter '(targetLink~/clusters/CLUSTER_NAME$ OR targetLink~/clusters/CLUSTER_NAME/) AND status!=DONE' \
              --format json
         

Replace the following:

     * `LOCATION`: the Compute Engine region or zone (for example, `us-central1` or `us-central1-a`) for the cluster, depending on whether your cluster is regional or zonal.
     * `CLUSTER_NAME`: the name of the cluster with the failing operation.

The output is similar to the following:
           
           {
              "name": "operation-0978307200000-00112233-4455-6677-8899-aabbccddeeff",
              "operationType": "UPDATE_CLUSTER",
              "selfLink": "https://container.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/operations/operation-0978307200000-00112233-4455-6677-8899-aabbccddeeff",
              "startTime": "2001-01-01T00:00:00.000000000Z",
              "status": "RUNNING",
              "targetLink": "https://container.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_NAME/nodePools/NODE_POOL_NAME",
              "zone": "LOCATION"
           }
           

In the output, review the `name` field for each operation. This value is the name of the operation that's blocking your new operation from starting. You need this value for the next step.

For more information about the other fields in the output, see the API documentation for [`projects.locations.operations`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.operations).

  2. Wait for the operation to complete:
         
         gcloud container operations wait OPERATION_NAME \
             --location=LOCATION
         

Replace `OPERATION_NAME` with the name of a blocking operation from an error message or the preceding step.

This command actively monitors the operation and exits when the operation is complete.

  3. After the blocking operation has a status of `DONE`, retry the operation that caused the error.




## What's next

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further help, including advice on the following topics:

    * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
    * Getting support from the community by [asking questions on StackOverflow](http://stackoverflow.com/questions/tagged/google-kubernetes-engine) and using the `google-kubernetes-engine` tag to search for similar issues. You can also join the [`#kubernetes-engine` Slack channel](https://googlecloud-community.slack.com/messages/C0B9GKTKJ/) for more community support.
    * Opening issues or feature requests by using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
