---
url: https://docs.cloud.google.com/kubernetes-engine/networking/docs/restrict-egress-control-plane/
title: Restrict egress traffic from the API server \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:45.427546+00:00
---

# Restrict egress traffic from the API server  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/networking/docs/restrict-egress-control-plane/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Restrict egress traffic from the API server Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

You can improve the security of your Google Kubernetes Engine (GKE) control plane by disabling the external IP addresses of the control plane virtual machine (VM) instances. This document shows security engineers how to control egress traffic from the Kubernetes API server and how to avoid potential disruptions to admission webhooks.

You should already be familiar with the following:

  * [Access to external sources from the API server](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation#access-external-sources-api-server)
  * [GKE networking overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview)
  * [GKE cluster architecture](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture)



## Levels of restriction

You can specify one of the following restriction levels when you create or update a cluster:

  * **No traffic (`NONE`)**: disable the external IP address of each control plane VM instance and route all API server egress traffic to a [black hole](https://en.wikipedia.org/wiki/Black_hole_\(networking\)#Black_hole_filtering). This level of restriction has the following effects: 
    * GKE blocks direct egress traffic from the API server to [admission webhook servers](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/#contacting-the-webhook) that run outside of the cluster. Any admission webhooks that use a URL or IP address to contact the webhook server are affected.
    * GKE blocks any direct egress traffic from the API server to external services, including the internet and Google Cloud services. Traffic for GKE authentication and to system components like the metadata server is unaffected.
    * Any other types of egress traffic, such as critical system traffic or traffic from your nodes, aren't affected.
    * GKE uses a ValidatingAdmissionPolicy to reject the creation of, or updates to, ValidatingWebhookConfigurations or MutatingWebhookConfigurations that use the `clientConfig.url` field.
  * **All traffic (`VIA_CONTROL_PLANE`)**: retain the external IP address of each control plane instance and let the API server use the IP address for egress traffic. This option is the default in GKE.



## Limitations

If you disable egress traffic by setting the level of restriction to `NONE`, the cluster can't use privately used public IP (PUPI) addresses.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure that you have a GKE Autopilot or Standard cluster that runs version 1.35.1-gke.1396000 or later. You can also [create an Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster).
  * If you have any external webhook servers, verify that you use a [Service reference](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/#service-reference) to contact those servers. When you disable egress traffic from the API server, any of your webhooks that use a URL to contact the webhook server fail. GKE-managed webhooks aren't affected.



## Customize egress traffic from the API server

You can customize the level of restriction for egress traffic from the API server when you create or update a cluster. To update an existing cluster, use the `--control-plane-egress` flag:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --control-plane-egress=CONTROL_PLANE_EGRESS_MODE
    

Replace the following:

  * `CLUSTER_NAME`: the name of your cluster.
  * `CONTROL_PLANE_LOCATION`: the region or zone of your cluster control plane, such as `us-central1` or `us-central1-a`.
  * `CONTROL_PLANE_EGRESS_MODE`: the level of restriction for egress traffic from your API server. Use one of the following values: 
    * `NONE`: disable the external IP address of your control plane VM instances and block all non-critical egress traffic from the API server. GKE prevents the creation of new webhook configurations that use the `clientConfig.url` field.
    * `VIA_CONTROL_PLANE`: retain the external IP address of the control plane VM instances and allow egress traffic from the API server. This is the default value.



## Verify the egress traffic restriction

To check whether GKE blocks egress traffic from your API server, use any of the following methods:

  * Check your cluster configuration:
        
        gcloud container clusters describe CLUSTER_NAME \
            --location=CONTROL_PLANE_LOCATION \
            --format='value(controlPlaneEgress)'
        

The output is one of the following:

    * `NONE`: egress traffic is restricted.
    * `VIA_CONTROL_PLANE`: egress traffic isn't restricted.
  * To verify the effect of your changes on new webhooks, try to create a webhook configuration that uses the `clientConfig.url` field:
        
        cat <<EOF | kubectl apply -f -
        apiVersion: admissionregistration.k8s.io/v1
        kind: MutatingWebhookConfiguration
        metadata:
          name: test-webhook-config
        webhooks:
        - name: my-webhook.example.com
          clientConfig:
            url: "https://my-webhook.example.com:9443/my-webhook-path"
        

The output is similar to the following:
        
        ValidatingAdmissionPolicy 'gke-restrict-webhook-url' denied request: Egress
        traffic from the API server through the control plane is disabled. As a
        result, direct API server calls to external webhook servers are blocked.
        To connect to external webhooks, update any webhook configurations that use
        clientConfig.url to use clientConfig.service instead.
        

This output indicates that a GKE ValidatingAdmissionPolicy prevents you from creating or updating webhook configurations with the `clientConfig.url` field. If you delete the ValidatingAdmissionPolicy, you can create or update the configuration, but admission requests won't reach the webhook server.

  * To verify the effect of your changes on existing webhooks in the cluster, try to send a direct request to an IP address outside of the cluster:

    1. Enable [`API_SERVER` logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-logs#available-logs) for your cluster.
    2. Delete the `gke-restrict-webhook-url` ValidatingAdmissionPolicy:
           
           kubectl delete validatingadmissionpolicy gke-restrict-webhook-url
           

When you delete the ValidatingAdmissionPolicy, you can create or update webhook configurations with the `clientConfig.url` field. The cluster automatically recreates the ValidatingAdmissionPolicy, so this bypass is temporary.

    3. In the `clientConfig.url` field of a ValidatingWebhookConfiguration or MutatingWebhookConfiguration, specify an IP address or URL to send requests to. You can use an example value, such as `http://example.com` or `203.0.113.100`.

    4. Check the API server logs for an error message like the following:
           
           Error from server (InternalError): error when creating "STDIN":
             Internal error occurred: failed calling webhook
             WEBHOOK_NAME": failed to call
             webhook: Post "WEBHOOK_URL":
             proxyconnect tcp: dial tcp: lookup master-internet-access-unavailable.localhost
             on 169.254.169.254:53: no such host
           

This output indicates that even though the ValidatingAdmissionPolicy is deleted, admission requests can't reach a webhook server by using the server IP address or URL.




After you disable the external IP addresses of your control plane VM instances, GKE blocks traffic to any webhooks that use a URL to contact external webhook servers. You must use the `clientConfig.service` field in your webhook configuration to set up an alternative route for your API server to use. For more information, see [External webhook configuration](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation#external-webhook-configuration).

## What's next

  * [Customize access to the control plane](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation)
  * [GKE networking best practices](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/networking)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
