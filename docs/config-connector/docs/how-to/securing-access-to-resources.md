---
url: https://docs.cloud.google.com/config-connector/docs/how-to/securing-access-to-resources/
title: Securing access to resources with IAM \u00a0|\u00a0 Config Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:28:18.895739+00:00
---

# Securing access to resources with IAM  |  Config Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/config-connector/docs/how-to/securing-access-to-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Config Connector ](https://docs.cloud.google.com/config-connector/docs)
  * [ Guides ](https://docs.cloud.google.com/config-connector/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Securing access to resources with IAM

Kubernetes users and service accounts need permissions to manage Config Connector resources. With Config Connector, your project's [control plane](https://kubernetes.io/docs/concepts/#kubernetes-control-plane) can be managed by identities that use Kubernetes [Role-Based Access Control](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) (RBAC). You can also reference Identity and Access Management (IAM) Policies.

Resources that can reference IAMPolicy and IAMPolicyMember are listed in the [Resource reference](https://docs.cloud.google.com/config-connector/docs/reference/resources). These resources have the property "Can Be Referenced by IAMPolicy/IAMPolicyMember".

This topic explains how to secure access to Google Cloud resources using Identity and Access Management.

## Before you begin

[Install Config Connector on your cluster](https://docs.cloud.google.com/config-connector/docs/concepts/installation-types).

## Securing control plane access with RBAC

In this example, you will create a service account and grant it permissions to manage a `PubSubTopic`. This service account cannot manage other types of Config Connector resources.

  1. Create a file named `pubsub-topic-service-account.yaml` with the following contents:
         
         apiVersion: v1
         kind: ServiceAccount
         metadata:
           name: pubsub-topic-service-account
           namespace: default
         

Apply this to create the `pubsub-topic-service-account` service account:
         
         kubectl apply -f pubsub-topic-service-account.yaml --namespace CC_NAMESPACE

Replace `CC_NAMESPACE` with the namespace Config Connector manages resources from.

  2. Confirm `pubsub-topic-service-account` cannot create `PubSubTopic` resources by verifying the output of the following command contains `no`:
         
         kubectl auth can-i get pubsubtopics --as=system:serviceaccount:default:pubsub-topic-service-account

  3. Next, create a [`ClusterRole`](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/access-control#rbac) that allows Pub/Sub topic creation.

The ClusterRole can only manage resources that have values specified in `rules.apiGroups` and `rules.resources`. To find values for `apiGroups` and `resources`, see the [reference](https://docs.cloud.google.com/config-connector/docs/reference/overview) for your resources.

Create a file named `pubsub-topic-editor-role.yaml` with the following contents:
         
         apiVersion: rbac.authorization.k8s.io/v1
         kind: ClusterRole
         metadata:
           creationTimestamp: null
           name: pubsub-topic-editor
         rules:
         - apiGroups:
           - pubsub.cnrm.cloud.google.com
           resources:
           - pubsubtopics
           verbs:
           - get
           - list
           - watch
           - create
           - update
           - patch
           - delete
         

Apply `pubsub-topic-editor.yaml` to create the `ClusterRole`:
         
         kubectl apply -f pubsub-topic-editor-role.yaml --namespace CC_NAMESPACE

Replace `CC_NAMESPACE` with the namespace Config Connector manages resources from.

  4. Next, create a RoleBinding between the ClusterRole and your service account. Create a file named `pubsub-topic-editor-rolebinding.yaml` with the following contents:
         
         apiVersion: rbac.authorization.k8s.io/v1
         kind: RoleBinding
         metadata:
           name: pubsub-topic-editor-rolebinding.
         subjects:
         - kind: ServiceAccount
           name: pubsub-topic-service-account
         roleRef:
           apiGroup: rbac.authorization.k8s.io
           kind: ClusterRole
           name: pubsub-topic-editor
         

  5. Apply `pubsub-topic-editor-rolebinding.yaml` to your cluster.
         
         kubectl apply -f pubsub-topic-editor-rolebinding.yaml --namespace CC_NAMESPACE

Replace `CC_NAMESPACE` with the namespace Config Connector manages resources from.

  6. Confirm the `pubsub-topic-service-account` is allowed to create `PubSubTopic` resources by confirming the output of the following command is `yes`:
         
         kubectl auth can-i get pubsubtopics \
           --as=system:serviceaccount:default:pubsub-topic-service-account




### Cleaning up

Use `kubectl delete` to remove the Service Account, IAM Role and Rolebinding.
    
    
    kubectl delete -f pubsub-topic-editor-rolebinding.yaml --namespace CC_NAMESPACE
    kubectl delete -f pubsub-topic-editor-role.yaml --namespace CC_NAMESPACE
    kubectl delete -f pubsub-topic-service-account.yaml --namespace CC_NAMESPACE
    

Replace `CC_NAMESPACE` with the namespace Config Connector manages resources from.

## Securing the data plane with IAM Policies

In this example, you use the permissions granted earlier to create a `PubSubTopic` and limit access to it with an `IAMPolicyMember` resource.

  1. Create a file named `pubsub-topic-sample.yaml` with the following content:
         
         apiVersion: pubsub.cnrm.cloud.google.com/v1beta1
         kind: PubSubTopic
         metadata:
           name: pubsubtopic-sample
         

Apply `pubsub-topic-sample.yaml` with `kubectl`:
         
         kubectl apply -f pubsub-topic-sample.yaml --namespace CC_NAMESPACE

Replace `CC_NAMESPACE` with the namespace Config Connector manages resources from.

  2. Create a file named `iampolicymember.yaml` with the following content, replacing `EMAIL_ADDRESS` with your Google Cloud account's email address:
         
         apiVersion: iam.cnrm.cloud.google.com/v1beta1
         kind: IAMPolicyMember
         metadata:
           name: iampolicymember-sample
         spec:
           resourceRef:
             apiVersion: pubsub.cnrm.cloud.google.com/v1beta1
             kind: PubSubTopic
             name: pubsubtopic-sample
           role: roles/pubsub.admin
           member: "user:EMAIL_ADDRESS"
         

  3. Apply the `iampolicymember.yaml`.
         
         kubectl apply -f iampolicymember.yaml  --namespace CC_NAMESPACE 

Replace `CC_NAMESPACE` with the namespace Config Connector manages resources from.

  4. Confirm the policy has been applied to Google Cloud by running this command and looking for your email address in the output, replacing `PROJECT_ID` with your project ID:
         
         gcloud beta pubsub topics get-iam-policy projects/PROJECT_ID/topics/pubsubtopic-sample




Access to your Pub/Sub topics is now protected with an `IAMPolicyMember`.

### Cleaning up

Use `kubectl delete` to remove the Pub/Sub topic and IAMPolicyMember from your Google Cloud Project.
    
    
    kubectl delete -f iampolicymember.yaml --namespace CC_NAMESPACE
    kubectl delete -f pubsub-topic-sample.yaml --namespace CC_NAMESPACE
    

## What's next

Use [Secrets](https://docs.cloud.google.com/config-connector/docs/how-to/secrets) to pass information securely to Google Cloud resources.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
