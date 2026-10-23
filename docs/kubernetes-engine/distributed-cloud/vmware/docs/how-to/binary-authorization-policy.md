---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/binary-authorization-policy/
title: Set up Binary Authorization policy enforcement \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:04.804087+00:00
---

# Set up Binary Authorization policy enforcement  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/binary-authorization-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Set up Binary Authorization policy enforcement Stay organized with collections  Save and categorize content based on your preferences. 

Binary Authorization for Google Distributed Cloud is a Google Cloud feature that extends the hosted, deploy-time enforcement of [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/overview) to your on-premises user clusters. The primary use case for Binary Authorization on Google Distributed Cloud is to secure workloads on your user clusters. Follow the steps in this guide to apply the enforcement rules of a Binary Authorization policy configured in your Google Cloud project to your user clusters. For more information about Binary Authorization policies and rules, see [ Binary Authorizationoverview](https://docs.cloud.google.com/binary-authorization/docs/key-concepts).

**Note:** If you enabled the ([Preview](https://cloud.google.com/products/#product-launch-stages)) Binary Authorization for Google Distributed Cloud, [disable it and clean up the resources](https://docs.cloud.google.com/binary-authorization/docs/setting-up-on-prem#clean_up) before you enable the GA feature. Use the instructions in this document to enable the GA feature on version 1.28 or higher clusters.

## Prerequisites

Before you can enable Binary Authorization policy enforcement for a user cluster, ensure you've met the following prerequisite criteria:

  * **Register the cluster with a fleet:** For a cluster created with `gkectl`, the cluster is registered to the Google Cloud project that you specify in the `gkeConnect.projectID` field in the cluster configuration file. This project is referred to as the [fleet host project](https://docs.cloud.google.com/anthos/fleet-management/docs/fleet-concepts#fleet-host-project). To learn more about fleets, including use cases, best practices, and examples, see the [Fleet management](https://docs.cloud.google.com/anthos/fleet-management/docs) documentation.

  * **Enable the Binary Authorization API in your Google Cloud project:** [enable the Binary Authorization service](https://docs.cloud.google.com/binary-authorization/docs/enabling) in your fleet host project.

  * **Add the Binary Authorization Policy Evaluator role to your fleet host project:** To grant the Binary Authorization Policy Evaluator (`roles/binaryauthorization.policyEvaluator`) role to the Kubernetes service account on your fleet host project, run the following command:
        
        gcloud projects add-iam-policy-binding PROJECT_ID \
            --member="serviceAccount:PROJECT_ID.svc.id.goog[binauthz-system/binauthz-agent]" \
            --role="roles/binaryauthorization.policyEvaluator"
        

If your cluster is running behind a proxy server, make sure the proxy server allows connections to the Binary Authorization API (`binaryauthorization.googleapis.com`). This API provides policy-based deployment validation and control for images deployed to your cluster. For more information about, see [Proxy and firewall rules proxy](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/firewall-rules).




Once you satisfy the prerequisites, you can enable (or disable) the Binary Authorization policy when you create a new cluster or update an existing cluster.

## Enable the Binary Authorization policy during cluster creation

You can enable the Binary Authorization policy enforcement with either `gkectl` or gcloud CLI.

###  `gkectl`

To enable Binary Authorization when you create a cluster with `gkectl`:

  1. Before you create your cluster, add `binaryAuthorization.evaluationMode` to the user cluster configuration file as shown in the following example:
         
         ...
         binaryAuthorization:
           evaluationMode: "project_singleton_policy_enforce"
         ...
         

Allowed values for `evaluationMode` are:

     * `project_singleton_policy_enforce`: enforce the rules specified in the Binary Authorization _policy_ , also known as a _project-singleton policy_ , on your Google Cloud project to govern the deployment of container images on your cluster.

     * `disabled`: disable the use of Binary Authorization for your cluster. This is the default value. If you omit `binaryAuthorization`, the feature is disabled.

  2. Make any other changes needed in the cluster configuration file and then run the `gkectl create cluster` command.




For more information about creating clusters, see [Google Distributed Cloud installation overview](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/install-overview).

## Enable or disable the Binary Authorization policy for an existing cluster

If you have an existing version 1.28 or higher cluster, you can enable or disable Binary Authorization at any time, using `gkectl` or gcloud CLI.

###  `gkectl`

  * To enable:

    1. Edit the cluster configuration file to add the `binaryAuthorization` fields:
           
           ...
           binaryAuthorization:
             evaluationMode: "project_singleton_policy_enforce"
           

    2. Update the cluster:
           
           gkectl update cluster \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
             --config USER_CLUSTER_CONFIG_FILE \
             --force

Replace the following:

       * `ADMIN_CLUSTER_KUBECONFIG`: the path of the admin cluster kubeconfig file
       * `USER_CLUSTER_CONFIG_FILE`: the path of your user cluster configuration file.
    3. Wait for the Deployment named `binauthz-module-deployment` in the `binauthz-system` namespace to become ready.

When the deployment is ready, Binary Authorization enforces the rules specified in the Binary Authorization _policy_ , also known as a _project-singleton policy_. This policy is associated with your Google Cloud project and specifies rules to govern the deployment of container images. For more information about using `gkectl` to update a cluster, see [Update clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading). For more information about Binary Authorization policies and rules, see [Binary Authorization overview](https://docs.cloud.google.com/binary-authorization/docs/key-concepts).

  * To disable:

    1. Edit the cluster configuration file and either remove the `binaryAuthorization` section or by set `evaluationMode` to `disabled`.
           
           ...
           binaryAuthorization:
             evaluationMode: "disabled"
           

    2. Update the cluster:
           
           gkectl update cluster \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
             --config USER_CLUSTER_CONFIG_FILE \
             --force

After you make this change, wait a few minutes until the Deployment named `binauthz-module-deployment` in the `binauthz-system` namespace is removed.




## Troubleshooting

If you don't complete all of the prerequisites, you may see a message like the following indicates there is a problem with the Binary Authorization configuration:
    
    
    failed to validate Binary Authorization policy
    
    (1) Ensure the Binary Authorization API is enabled for your Google Cloud project:
        gcloud services enable binaryauthorization.googleapis.com --project=PROJECT_ID
    (2) Ensure an IAM policy binding is in place granting binaryauthorization.policyEvaluator role to the binauthz-system/binauthz-agent Kubernetes service account:
        gcloud projects add-iam-policy-binding PROJECT_ID \
            --member="serviceAccount:PROJECT_ID.svc.id.goog[binauthz-system/binauthz-agent]" \
            --role=roles/binaryauthorization.policyEvaluator

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
