---
url: https://docs.cloud.google.com/eventarc/standard/docs/gke/troubleshooting/
title: Troubleshoot Eventarc for Google Kubernetes Engine (GKE) \u00a0|\u00a0 Eventarc Standard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:01:13.146542+00:00
---

# Troubleshoot Eventarc for Google Kubernetes Engine (GKE)  |  Eventarc Standard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/standard/docs/gke/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/standard/docs/overview)



Send feedback 

#  Troubleshoot Eventarc for Google Kubernetes Engine (GKE) Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page shows you how to resolve issues that you might encounter when using Eventarc for GKE, including the public endpoints of private and public services running in a GKE cluster.

For other issues that you might also encounter, refer to troubleshooting for:

  * [Issues common to all destinations](https://docs.cloud.google.com/eventarc/docs/troubleshooting)
  * [Eventarc for Cloud Run](https://docs.cloud.google.com/eventarc/standard/docs/run/troubleshoot)
  * [Eventarc for Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/troubleshoot)



## Trigger creation fails with resource creation permission errors

You receive error messages similar to one of the following: 
    
    
    Error applying IAM policy for service account 'projects/PROJECT_ID/serviceAccounts/SERVICE_ACCOUNT':
    Error setting IAM policy for service account 'projects/PROJECT_ID/serviceAccounts/SERVICE_ACCOUNT':
    googleapi: Error 403: Permission iam.serviceAccounts.setIamPolicy is required to perform this
    operation on service account SERVICE_ACCOUNT., forbidden
    
    
    
    Error when reading or editing Container Cluster "cluster": googleapi:
    Error 403: Required "container.clusters.get" permission(s) for "..."., forbidden
    
    
    
    Error reading instance group manager returned as an instance group URL:
    "googleapi: Error 403: Required 'compute.instanceGroupManagers.get' permission
    for '...', forbidden"
    

This error occurs when you have not correctly set up the Eventarc service account that is required by Eventarc to manage resources in the Google Kubernetes Engine (GKE) cluster.

To resolve the issue, ensure that the Eventarc service account has been configured correctly with the appropriate permissions to create resources. For more information, follow the instructions for a [specific provider, event type, and GKE destination](https://docs.cloud.google.com/eventarc/standard/docs/event-providers-targets#triggers).

## Trigger creation fails because target cluster cannot be found or does not have Workload Identity Federation for GKE enabled

You receive error messages similar to one of the following:
    
    
    ERROR: (gcloud.eventarc.triggers.create) NOT_FOUND: Not found: projects/PROJECT_ID/locations/
    LOCATION/clusters/CLUSTER_NAME.
    ...
    
    
    
    ERROR: (gcloud.eventarc.triggers.create) INVALID_ARGUMENT: workload identity is not enabled on
    cluster CLUSTER_NAME in LOCATION
    ...
    

This error occurs when Eventarc cannot find the target GKE cluster or the cluster does not have Workload Identity Federation for GKE enabled.

To resolve the issue, ensure that the target cluster exists and has [Workload Identity enabled](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity).

## Trigger creation fails because of invalid resource state

You receive an error message similar to the following:
    
    
    ERROR: (gcloud.eventarc.triggers.create) Invalid resource state for projects/PROJECT_ID/locations/LOCATION/triggers/TRIGGER_ID.
    Ensure that you have enabled your GKE destination and assigned required permissions to the service account.

This error can occur when: 

  * Your GKE destination hasn't been enabled.
  * The service account hasn't been granted the required roles and permissions that enables Eventarc to manage events for GKE destinations.
  * Workload Identity Federation for GKE hasn't been enabled on the node pool.



To resolve this issue:

  1. Ensure that you have enabled GKE destinations: 
         
         gcloud eventarc gke-destinations init

For more information, follow the instructions for a [specific provider and event type](https://docs.cloud.google.com/eventarc/standard/docs/event-providers-targets#triggers) in the "Enable GKE destinations" section.
  2. Ensure that the Eventarc service account has been configured with the appropriate permissions to create resources. For more information on how to grant the appropriate roles to the service account, follow the instructions for a [specific provider and event type](https://docs.cloud.google.com/eventarc/standard/docs/event-providers-targets#triggers) in the "Prepare to create a trigger" section.
  3. If you see readiness probe failures for the [event forwarder](https://docs.cloud.google.com/eventarc/standard/docs/gke/route-trigger-eventarc#event-forwarder), it means that the kubelet on the node couldn't connect to the event forwarder container port. This can occur when Workload Identity Federation for GKE isn't enabled on the node pool. You can [manually enable Workload Identity Federation for GKE on existing node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#option_2_node_pool_modification). Enabling this ensures that the event forwarder pod uses the correct service account with the necessary permissions.
  4. If the error persists, [contact support](https://docs.cloud.google.com/eventarc/docs/getting-support).



## Trigger is created successfully but target is not receiving events

Check that enough time has elapsed since creating the trigger. It can take up to two minutes before events are sent.

  1. If events are not being delivered at the target, events sent from Pub/Sub to the target might be getting dropped:

To ensure that events aren't dropped, set up a [Pub/Sub subscription retry policy](https://docs.cloud.google.com/pubsub/docs/handling-failures#subscription_retry_policy) or [forward undelivered messages to a dead-letter topic](https://docs.cloud.google.com/pubsub/docs/handling-failures#forwarding_to) (also known as a dead-letter queue).

Before setting the dead-letter topic, retrieve the trigger's topic and subscription:
         
         gcloud eventarc triggers describe TRIGGER \
           --location=LOCATION

Replace the following:

     * `TRIGGER`: the ID of the trigger or a fully qualified identifier.
     * `LOCATION`: the location of the Eventarc trigger.

  2. If the trigger still doesn't work, check the status of Eventarc's event forwarder component to see if it has been deployed properly:

     1. Identify the cluster namespaces by listing all pods that have `event-forwarder` in their name: 
            
            kubectl get pods --all-namespaces | grep event-forwarder

The output is similar to the following: 
            
            event-forwarder-namespace-hash1   event-forwarder-hash1   1/1   Running   0   5d2h
            event-forwarder-namespace-hash2   event-forwarder-hash2   1/1   Running   0   2d2h
            

The first 30 characters of the namespaces should match the name of the Eventarc trigger you created, followed by a hash to disambiguate any triggers with the same initial 30 characters.
     2. Retrieve the deployment details: 
            
            kubectl get deployments -n EVENT_FORWARDER_NAMESPACE event-forwarder

     3. Retrieve the pod details: 
            
            kubectl describe pod -n EVENT_FORWARDER_NAMESPACE EVENT_FORWARDER_HASH

     4. Print the pod logs to investigate why or where the failure has occurred: 
            
            kubectl logs -f -n EVENT_FORWARDER_NAMESPACE EVENT_FORWARDER_HASH

For example, in the following log, the service account has had the `Pub/Sub Subscriber` role revoked: 
            
            {"error":"generic::permission_denied: missing 'pubsub.subscriptions.consume' permission",
            "message":"Permissions check failed","severity":"fatal","timestamp":"2021-07-07T14:57:49.038877483Z"}
            




## Related information

  * Learn more about [Eventarc for GKE](https://docs.cloud.google.com/eventarc/standard/docs/overview#gke).
  * To get additional help, see [Get support](https://docs.cloud.google.com/eventarc/docs/getting-support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
