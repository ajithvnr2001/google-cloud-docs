---
url: https://docs.cloud.google.com/config-connector/docs/how-to/getting-started/
title: Getting started with Config Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:36:44.420835+00:00
---

# Getting started with Config Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/config-connector/docs/how-to/getting-started/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Config Connector ](https://docs.cloud.google.com/config-connector/docs)
  * [ Guides ](https://docs.cloud.google.com/config-connector/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Getting started with Config Connector

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This guide shows the basics of Config Connector resource management by teaching you how to complete the following tasks:

  * Enable a Google Cloud API.
  * Create and manage a [Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/admin).



## Before you begin

Before you start the exercises on this page, complete the following tasks:

  * Install Config Connector by completing _all_ of the steps in [Manually installing the Config Connector Operator](https://docs.cloud.google.com/config-connector/docs/how-to/install-manually).

  * Configure Config Connector [to use a default namespace](https://docs.cloud.google.com/config-connector/docs/how-to/configuring-your-client). The namespace that you set as your default should be the same namespace that you added an annotation to when you [specified where to create your resources](https://docs.cloud.google.com/config-connector/docs/how-to/install-upgrade-uninstall#specify).

  * Config Connector uses the Service Usage API to enable service APIs. To perform these steps, you need to enable the [Service Usage](https://console.cloud.google.com/apis/library/serviceusage.googleapis.com) API. You can enable this API by using the Google Cloud CLI: 
        
        gcloud services enable serviceusage.googleapis.com

**Note:** Enabling the API might take several minutes. 



## Discovering available Google Cloud resources

To see what kinds of Google Cloud resources you can create with Config Connector, run:
    
    
    kubectl get crds --selector cnrm.cloud.google.com/managed-by-kcc=true

The output is a list of all the resources your version of Config Connector can create and manage.

For example, you can view the API description for the `PubSubTopic` resource with `kubectl describe`:
    
    
    kubectl describe crd pubsubtopics.pubsub.cnrm.cloud.google.com

You can also see information on available resources in [Config Connector resources](https://docs.cloud.google.com/config-connector/docs/reference/overview).

## Enabling the Pub/Sub service

Use Config Connector to enable the Pub/Sub API by applying a YAML configuration to your cluster:

  1. Create a file named `enable-pubsub.yaml` and copy the following YAML into it:
         
         apiVersion: serviceusage.cnrm.cloud.google.com/v1beta1
         kind: Service
         metadata:
           name: pubsub.googleapis.com
         spec:
           projectRef:
             external: projects/PROJECT_ID
         

Replace `PROJECT_ID` with your Google Cloud project ID.

  2. Use [`kubectl apply`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#apply) to apply the configuration to your cluster. To enable the Pub/Sub API, run the following command:
         
         kubectl apply -f enable-pubsub.yaml


**Note:** Enabling an API might take several minutes.

## Creating a Pub/Sub instance

Create a file named `pubsub-topic.yaml` with the following content:
    
    
      apiVersion: pubsub.cnrm.cloud.google.com/v1beta1
      kind: PubSubTopic
      metadata:
        annotations:
          cnrm.cloud.google.com/project-id: PROJECT_ID
        labels:
          LABEL_KEY: LABEL_VALUE
        name: TOPIC_NAME
    

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `LABEL_KEY: LABEL_VALUE`: a key-value pair of [labels](https://docs.cloud.google.com/pubsub/docs/labels). For example, `environment: production`.
  * `TOPIC_NAME`: the Pub/Sub topic name.



When you create a resource, Config Connector creates the resource if it doesn't exist. If a Google Cloud resource already exists with the same name, then Config Connector acquires the resource and manages it. To learn more about acquiring an existing resource, see [Managing and deleting resources](https://docs.cloud.google.com/config-connector/docs/how-to/managing-deleting-resources).

Use the [`kubectl apply`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#apply) command to create resources. To create the Pub/Sub topic, run the following command:
    
    
    kubectl apply -f pubsub-topic.yaml 

## Describing a resource

Use [`kubectl describe`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#describe) to get details on a resource.

For example, to view all your Pub/Sub topic, run the following command:
    
    
    kubectl describe pubsubtopics

In this list, you should see the Pub/Sub topic you created in the previous section.

## Verifying that a resource is ready

After you have created a Pub/Sub topic, you can check its [`status.condition`](https://docs.cloud.google.com/config-connector/docs/concepts/resources#status_condition). For example, to check if your Pub/Sub topic resource is ready, run the following command:
    
    
    kubectl wait --for=condition=READY pubsubtopics TOPIC_NAME
    

Replace `TOPIC_NAME` with the name of your Pub/Sub topic.

You should see output similar to the following example:
    
    
    pubsubtopic.pubsub.cnrm.cloud.google.com/TOPIC_NAME condition met
    

## Updating a resource

You can update [metadata](https://kubernetes.io/blog/2016/03/how-container-metadata-changes-your-point-of-view/) on your resources by updating your YAML file and re-applying it with `kubectl`.

To change the label on the Pub/Sub topic you created in the previous section, complete the following steps:

  1. Modify the `metadata` section of your `pubsub-topic.yaml` file to change the label:
         
         apiVersion: pubsub.cnrm.cloud.google.com/v1beta1
           kind: PubSubTopic
           metadata:
             annotations:
               cnrm.cloud.google.com/project-id: PROJECT_ID
             labels:
               NEW_LABEL_VALUE
             name: TOPIC_NAME
         

Replace the following:

     * `PROJECT_ID`: your Google Cloud project ID.
     * `NEW_LABEL_VALUE`: an updated value for the label you added previously. For example, `environment: staging`.
     * `TOPIC_NAME`: the Pub/Sub topic name
  2. Use `kubectl apply` to update the resource. Run the following command:
         
         kubectl apply -f pubsub-topic.yaml

  3. Check the Pub/Sub instance for the change in name:
         
         kubectl describe pubsubtopics

Your topic should have the new label.




## Deleting a resource

Use [`kubectl delete`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#delete) to delete resources. For example, to delete the `PubSubTopic` you created earlier, run `kubectl delete` with your `pubsub-topic.yaml` file:
    
    
    kubectl delete -f pubsub-topic.yaml

You receive confirmation that the resource was deleted:
    
    
    pubsubtopic.pubsub.cnrm.cloud.google.com "TOPIC_NAME" deleted
    

By default, Config Connector deletes the `PubSubTopic` resource. If you prefer to keep this resource, see the instructions in [Managing and deleting resources](https://docs.cloud.google.com/config-connector/docs/how-to/managing-deleting-resources#keeping_resources_after_deletion).

## What's next

  * Learn about how Config Connector models Google Cloud resources with [Kubernetes constructs](https://docs.cloud.google.com/config-connector/docs/concepts/resources).
  * See the Google Cloud [resources](https://docs.cloud.google.com/config-connector/docs/reference/resources) Config Connector can manage.
  * Use Config Connector to [manage your existing Google Cloud resources](https://docs.cloud.google.com/config-connector/docs/how-to/managing-deleting-resources).
  * See additional examples of how to use Config Connector on the [GitHub repository](https://github.com/GoogleCloudPlatform/k8s-config-connector).
  * Learn how Kubernetes handles [declarative configuration](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/declarative-config/) of objects.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
