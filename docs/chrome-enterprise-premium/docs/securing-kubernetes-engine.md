---
url: https://docs.cloud.google.com/chrome-enterprise-premium/docs/securing-kubernetes-engine/
title: Securing GKE apps and resources with IAP \u00a0|\u00a0 Chrome Enterprise Premium \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:31:16.167279+00:00
---

# Securing GKE apps and resources with IAP  |  Chrome Enterprise Premium  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chrome-enterprise-premium/docs/securing-kubernetes-engine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Chrome Enterprise Premium ](https://docs.cloud.google.com/chrome-enterprise-premium/docs)
  * [ Guides ](https://docs.cloud.google.com/chrome-enterprise-premium/docs/overview)



Send feedback 

#  Securing GKE apps and resources with IAP Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to secure a Google Kubernetes Engine (GKE) instance with [Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/iap/docs/concepts-overview).

To secure resources not on Google Cloud, see [Securing on-premises apps and resources](https://docs.cloud.google.com/chrome-enterprise-premium/docs/securing-on-premises).

## Overview

IAP is integrated through [Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress) for GKE. This integration lets you control resource-level access for employees instead of using a VPN.

In a GKE cluster, incoming traffic is handled by [HTTP(S) Load Balancing](https://docs.cloud.google.com/load-balancing/docs/https), a component of [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview). The HTTP(S) load balancer is typically configured by the [Kubernetes Ingress controller](https://github.com/kubernetes/ingress-gce). The Ingress controller gets configuration information from a Kubernetes [Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress) object that is associated with one or more [Service](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service) objects. Each Service object holds routing information that is used to direct an incoming request to a particular Pod and port. 

Beginning with Kubernetes version 1.10.5-gke.3, you can add configuration for the load balancer by associating a Service with a [BackendConfig](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/backendconfig) object. BackendConfig is a [custom resource definition](https://docs.cloud.google.com/chrome-enterprise-premium/docs/CRD) that is defined in the [kubernetes/ingress-gce](https://github.com/kubernetes/ingress-gce/tree/master/pkg/apis/backendconfig) repository.

The Kubernetes Ingress controller reads configuration information from the BackendConfig and sets up the load balancer accordingly. A BackendConfig holds configuration information that is specific to Cloud Load Balancing, and lets you define a separate configuration for each HTTP(S) Load Balancing backend service. 

## Before you begin

To enable IAP for GKE, you need the following:

  * A Google Cloud console project with billing enabled. 
  * A group of one or more GKE instances, served by an HTTPS load balancer. The load balancer should be created automatically when you create an Ingress object in a GKE cluster. 
    * Learn about [creating an Ingress for HTTPS](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/http-balancer).
  * A domain name registered to the address of your load balancer.
  * App code to verify that all requests have an identity. 
    * Learn about [getting the user's identity](https://docs.cloud.google.com/iap/docs/identity-howto).

IAP uses a Google-managed OAuth client to authenticate users. Only users within the organization can access the IAP-enabled application. If you want to allow access to users outside of your organization, see [Enable IAP for external applications](https://docs.cloud.google.com/iap/docs/custom-oauth-configuration). 

## Enabling IAP

If you haven't configured your project's OAuth consent screen, you'll be prompted to do so. To configure your OAuth consent screen, see [Setting up your OAuth consent screen](https://support.google.com/cloud/answer/10311615).

If you are running GKE version 1.24 or later, you can configure IAP and GKE by using the Kubernetes Gateway API. To do so, complete the following steps and then follow the instructions in [Configure IAP](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gateway-resources#configure_iap). Do not configure `BackendConfig`.

### Setting up IAP access

  1. Go to the [Identity-Aware Proxy page](https://console.cloud.google.com/security/iap).   
[Go to the Identity-Aware Proxy page](https://console.cloud.google.com/security/iap)
  2. Select the project you want to secure with IAP.
  3. Select the checkbox next to the resource you want to grant access to.

If you don't see a resource, ensure that the resource is created and that the BackendConfig and Compute Engine ingress controller are synced.

To verify that the backend service is available, run the following gcloud command:

`gcloud compute backend-services list`
  4. On the right side panel, click **Add principal**. 
  5. In the **Add principals** dialog that appears, enter the email addresses of groups or individuals who should have the **IAP-secured Web App User** role for the project. 

The following kinds of principals can have this role:

     * **Google Account** : user@gmail.com 
     * **Google Group** : admins@googlegroups.com 
     * **Service account** : server@example.gserviceaccount.com 
     * **Google Workspace domain** : example.com 

Make sure to add a Google Account that you have access to.

  6. Select **Cloud IAP > IAP-secured Web App User** from the **Roles** drop-down list. 
  7. Click **Save**. 



### Configuring BackendConfig

You can configure a BackendConfig for IAP by adding an `iap` block. 

#### Adding an `iap` block to the BackendConfig

To configure the BackendConfig for IAP, you need to specify the `enabled` value. [Ensure that you have the `compute.backendServices.update` permission](https://docs.cloud.google.com/iap/docs/managing-access#turning_on_and_off) and add the `iap` block to BackendConfig. 

**Note:** You can't enable both IAP and Cloud CDN (Cloud CDN) in a BackendConfig. If the BackendConfig doesn't have a IAP block, then any existing IAP settings on the backend service are inherited. 

For GKE versions 1.16.8-gke.3 and higher, use the `cloud.google.com/v1` API version. If you are using an earlier GKE version, use `cloud.google.com/v1beta1`. 
    
    
    apiVersion: cloud.google.com/v1
    kind: BackendConfig
    metadata:
      name: CONFIG_DEFAULT
      namespace: my-namespace
    spec:
      iap:
        enabled: true

#### Associate a service port with a BackendConfig

You also need to [associate Service ports with your BackendConfig](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/backendconfig#associating_a_service_port_with_a_backendconfig) to trigger turning on IAP. One way to make this association is to make all ports for the service default to your BackendConfig, which you can do by adding the following annotation to your Service resource: 
    
    
    metadata:
      annotations:
        cloud.google.com/backend-config: '{"default": "CONFIG_DEFAULT"}'

#### Verify the BackendConfig

To test the configuration, run `kubectl get event`. If you see the message "`no BackendConfig for service port exists`", then you successfully associated a service port with your BackendConfig, but the BackendConfig resource wasn't found. This error can occur if you haven't created the BackendConfig resource, created it in the wrong namespace, or misspelled the reference in the Service annotation. 

**Note:** IAP adds the `gcp-iap-mode=AUTHENTICATING` query parameter to the redirected request that occurs after OAuth authentication, so be sure to check your ingress load balancer's [routing configuration](https://cloud.google.com/load-balancing/docs/url-map) to ensure that redirected requests are going to the correct backend service after a user authenticates through OAuth. **Note:** You might get an `Add firewall rule` warning message on the IAP configuration page for network endpoint group (NEG) based backends even though the correct firewall rule exists. The firewall rule warning is informational and can be safely ignored. 

## Turning IAP off

To turn IAP off, you must set `enabled` to `false` in the BackendConfig. If you delete the IAP block from BackendConfig, the settings will persist. For example, if IAP is enabled and you delete the block, then IAP will still be turned on. 

## Next steps

  * Set richer context rules by [applying access levels](https://docs.cloud.google.com/chrome-enterprise-premium/docs/access-levels).
  * See [Context-Aware Access logs in Cloud Audit Logs](https://docs.cloud.google.com/access-context-manager/docs/audit-logs).
  * Learn more about [IAP](https://docs.cloud.google.com/iap/docs/concepts-overview).
  * [Learn how to set up Cloud CDN on GKE][cdn].
  * [Learn how to configure Cloud Armor for GKE][armor].
  * [Learn more about the BackendConfig resource](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/backendconfig).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
