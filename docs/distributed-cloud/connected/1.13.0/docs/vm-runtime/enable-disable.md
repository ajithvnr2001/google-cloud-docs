---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/vm-runtime/enable-disable/
title: Enable or disable VM Runtime on Google Distributed Cloud \u00a0|\u00a0 Google Distributed Cloud connected \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:25:46.141287+00:00
---

# Enable or disable VM Runtime on Google Distributed Cloud  |  Google Distributed Cloud connected  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/vm-runtime/enable-disable/

Select versionkeyboard_arrow_down

  * [ 1.13.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.13.0 (Latest) ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)



Send feedback 

#  Enable or disable VM Runtime on Google Distributed Cloud Stay organized with collections  Save and categorize content based on your preferences. 

On Google Distributed Cloud connected, you can enable or disable VM Runtime on GDC.

VM Runtime on GDC is enabled by default on Distributed Cloud connected clusters versions 1.9.0 and higher. If you don't need to run virtual machine (VM) workloads, you can disable VM Runtime on GDC to free up resources on your nodes. You can also re-enable it if it was previously disabled.

**Note:** Don't try to enable or disable VM Runtime on GDC by directly modifying the `VMRuntime` custom resource on the cluster using `kubectl`. These changes will be overwritten by Google-managed lifecycle hooks. Use Google Cloud console or the Distributed Cloud Edge Container API to manage the VM Runtime on GDC status.

## Before you begin

To enable or disable VM Runtime on GDC, you need the following:

  * A Distributed Cloud connected cluster.
  * The Identity and Access Management permissions `roles/edgecontainer.admin` on the target project.



To use the API and to follow the verification instructions, you also need:

  * The latest version of the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) installed and initialized.
  * The Kubernetes command-line tool, [`kubectl`](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin#install-kubectl).



## Disable VM Runtime on GDC

You can disable VM Runtime on GDC using the Google Cloud console or the API.

### Console

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. Select the cluster that you want to modify.

  3. Click **Edit**.

  4. In the **System Add-ons** or **VM Service** section, disable the **VM Runtime** toggle.

  5. Click **Save** or **Update**.




### API

To disable VM Runtime on GDC, make a `PATCH` request to the [`projects.locations.clusters`](https://docs.cloud.google.com/cluster-director/docs/reference/rest/v1/projects.locations.clusters) method.

Specify the `updateMask` query parameter as `systemAddonsConfig.vmServiceConfig.vmmEnabled`.
    
    
    PATCH https://edgecontainer.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/clusters/CLUSTER_ID?updateMask=systemAddonsConfig.vmServiceConfig.vmmEnabled
    Content-Type: application/json
    
    {
          "systemAddonsConfig": {
            "vmServiceConfig": {
              "vmmEnabled": false
            }
          }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the target project
  * `REGION`: the Google Cloud region where your cluster is located
  * `CLUSTER_ID`: the ID of your cluster



## Enable VM Runtime on GDC

VM Runtime on GDC is enabled by default for Distributed Cloud connected clusters. If you previously disabled VM Runtime on GDC, you can use the following instructions to re-enable it.

### Console

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. Select the cluster that you want to modify.

  3. Click **Edit**.

  4. In the **System Add-ons** or **VM Service** section, enable the **VM Runtime** toggle.

  5. Click **Save** or **Update**.




### API

To enable VM Runtime on GDC, make a `PATCH` request to the [`projects.locations.clusters`](https://docs.cloud.google.com/cluster-director/docs/reference/rest/v1/projects.locations.clusters) method.

Specify the `updateMask` query parameter as `systemAddonsConfig.vmServiceConfig.vmmEnabled`.
    
    
    PATCH https://edgecontainer.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/clusters/CLUSTER_ID?updateMask=systemAddonsConfig.vmServiceConfig.vmmEnabled
    Content-Type: application/json
    
    {
          "systemAddonsConfig": {
            "vmServiceConfig": {
              "vmmEnabled": true
            }
          }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the target project
  * `REGION`: the Google Cloud region where your cluster is located
  * `CLUSTER_ID`: the ID of your cluster



## Check the VM Runtime on GDC status

You can check the status of VM Runtime on GDC on your cluster.

  1. To obtain credentials for your cluster, run the [`gcloud edge-cloud container clusters get-credentials`](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/get-credentials) command.
         
         gcloud edge-cloud container clusters get-credentials CLUSTER_ID \
             --project=PROJECT_ID \
             --location=REGION
         

Replace the following:

     * `CLUSTER_ID`: the ID of your cluster
     * `PROJECT_ID`: the ID of the target project
     * `REGION`: the Google Cloud region where your cluster is located
  2. To describe the `VMRuntime` custom resource, run the [`kubectl describe`](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_describe/) command:
         
         kubectl describe vmruntime vmruntime
         

     * If VM Runtime on GDC is enabled, the command returns details about the resource, and `VMRuntime.Status.Ready` shows as `true`.

     * If VM Runtime on GDC is disabled, the `VMRuntime` resource might not be found, or its status indicates that it's not ready.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
