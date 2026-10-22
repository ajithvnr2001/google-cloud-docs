---
url: https://docs.cloud.google.com/deploy/docs/anthos-targets/
title: Deploy to GKE attached clusters \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:01.004028+00:00
---

# Deploy to GKE attached clusters  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/anthos-targets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback 

#  Deploy to GKE attached clusters Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to deploy your applications to [GKE attached clusters](https://docs.cloud.google.com/anthos/clusters/docs). Support for GKE attached clusters enables deployment to AWS, Azure, and on-premises clusters.

Cloud Deploy lets you deploy your container-based workloads to any GKE attached clusters that you can access using [Connect](https://docs.cloud.google.com/anthos/multicluster-management/gateway/using) gateway.

## Before you begin

  * Have a user cluster that you will deploy to.

Clusters can be created as GKE attached clusters, or you can [register an existing Kubernetes cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster). Clusters that you create as GKE attached clusters automatically receive memberships. For existing clusters that you [register to a fleet](https://docs.cloud.google.com/anthos/multicluster-management/fleets), you designate a membership name when registering. You need this membership name when you configure the target.

If you're using Google Cloud CLI version 407.0.0 or newer, you need to include the `--install-connect-agent` flag on the [`gcloud container fleet memberships register` command](https://cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/register), when you register a Google Kubernetes Engine cluster. The Connect agent is no longer installed by default.

  * Set up [Connect gateway](https://docs.cloud.google.com/anthos/multicluster-management/gateway/setup) to connect the registered cluster or clusters to Google Cloud.

Be sure to set up the gateway using the same service account that will be used as the [Cloud Deploy execution service account](https://docs.cloud.google.com/deploy/docs/cloud-deploy-service-account#execution_service_account). If you don't, then the execution service account won't have the necessary permissions to deploy to the cluster.

**Note:** Enable [Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) on the GKE clusters in order to set up Connect gateway.



## Set up your Cloud Deploy to deploy to GKE attached clusters

  1. Create your [target configuration](https://docs.cloud.google.com/deploy/docs/config-files).

The target can be configured in your delivery pipeline YAML, or can be in a separate file. Also, you can configure more than one target in the same file, but they must be in different `kind: Target` stanzas.

  2. Grant the [execution service account](https://docs.cloud.google.com/deploy/docs/execution-environment) the [roles that it needs](https://docs.cloud.google.com/anthos/multicluster-management/gateway/setup#grant_roles_to_users) so that it can interact with connected clusters through the gateway.

This grant is necessary whether you're using the default Cloud Deploy service account or a [custom service account](https://docs.cloud.google.com/deploy/docs/execution-environment#changing_from_the_default_to_custom_execution_service_account).

  3. [Set up RBAC](https://docs.cloud.google.com/anthos/multicluster-management/gateway/setup#configure_role-based_access_control_rbac_policies) for the [execution service account](https://docs.cloud.google.com/deploy/docs/execution-environment) on the underlying Kubernetes cluster.

  4. Optional: if the underlying cluster is not a GKE cluster, you might need to [configure an imagePullSecret](https://docs.cloud.google.com/artifact-registry/docs/access-control#pullsecrets) to allow your cluster to pull from Artifact Registry.

  5. In the target definition, create an `anthosCluster` stanza to point to the cluster:

The syntax for specifying GKE attached clusters is as follows:
         
         anthosCluster:
          membership: projects/[project_name]/locations/global/memberships/[membership_name]
         

This GKE attached clusters resource identifier uses the following elements:

     * [`project_name`] is the name of the Google Cloud project in which you're running this cluster.

The cluster you're deploying to, including GKE attached clusters, does _not_ need to be in the same project as your delivery pipeline.

     * [`membership_name`] is the name that you chose when you [registered the cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster) to a fleet.

For `location`, all cluster memberships are `global`, so you don't need to change `/locations/global/` in this resource identifier.




The following is an example target configuration:
    
    
          apiVersion: deploy.cloud.google.com/v1
          kind: Target
          metadata:
           name: qsdev
          description: development cluster
          anthosCluster:
           membership: projects/my-app/locations/global/memberships/my-app-dev-cluster
    

## What's next

  * Learn more about [configuring Cloud Deploy targets](https://docs.cloud.google.com/deploy/docs/config-files#target_definitions)

  * Learn about Cloud Deploy [execution environments](https://docs.cloud.google.com/deploy/docs/execution-environment).

  * Learn more about [GKE attached clusters](https://docs.cloud.google.com/anthos/docs)

  * Learn more about [Connect gateway](https://docs.cloud.google.com/anthos/multicluster-management/gateway).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
