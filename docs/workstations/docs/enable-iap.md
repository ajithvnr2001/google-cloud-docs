---
url: https://docs.cloud.google.com/workstations/docs/enable-iap/
title: Enable IAP \u00a0|\u00a0 Cloud Workstations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:14.828658+00:00
---

# Enable IAP  |  Cloud Workstations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workstations/docs/enable-iap/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Workstations ](https://docs.cloud.google.com/workstations/docs)
  * [ Guides ](https://docs.cloud.google.com/workstations/docs/overview)



Send feedback 

#  Enable IAP Stay organized with collections  Save and categorize content based on your preferences. 

Use [Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/iap/docs) to control access to applications on your workstations. IAP establishes a central authorization layer, allowing you to manage access at the application level rather than relying on network-level firewalls.

You can control access based on user identity, group membership, device security, location, IP address, and other signals. Users access applications using their web browser and HTTPS, while IT teams centrally define and enforce access policies in one place.

This document describes how to enable IAP for applications on workstations in your cluster. The following diagram illustrates a cluster with IAP enabled:

![](https://docs.cloud.google.com/static/workstations/images/architecture-iap-enabled-cluster.svg)Figure 1. Cluster with IAP enabled

## Before you begin

Before you can enable IAP for your workstations, your cluster needs the following:

  * **A custom domain:** IAP is only supported on workstation clusters that use a custom domain.
  * **An Application Load Balancer:** This load balancer will handle all ingress HTTP traffic using a Private Service Connect (PSC) endpoint and lets you to configure the IAP.



To set up these components, see [Set up custom domains for Cloud Workstations](https://docs.cloud.google.com/workstations/docs/set-up-custom-domains-for-cloud-workstations).

## Enable the proxy

To enable IAP for your workstations, follow these steps:

  1. Enable IAP on the cluster's Application Load Balancer, by running the following command:
         
         gcloud compute backend-services update BACKEND_SERVICE_NAME \
             --iap=enabled,oauth2-client-id=CLIENT_ID,oauth2-client-secret=CLIENT_SECRET \
             --global
         

Replace the following:

     * `BACKEND_SERVICE_NAME`: the name of the backend service you created while setting up a custom domain for your cluster.
     * `CLIENT_ID`: the OAuth 2.0 client ID.
     * `CLIENT_SECRET`: the OAuth 2.0 client secret.

For more information on setting up a Application Load Balancer with IAP enabled, see [Enable IAP on a load balancer](https://docs.cloud.google.com/iap/docs/load-balancer-howto#enable-iap).

  2. Grant access to users in your domain:
         
         gcloud iap web add-iam-policy-binding \
              --resource-type=backend-services \
              --service=BACKEND_SERVICE_NAME \
              --member='PRINCIPAL' \
              --role='roles/iap.httpsResourceAccessor' \
              --condition="expression=EXPRESSION,title=TITLE,description=DESCRIPTION"
         

Replace the following:

     * `BACKEND_SERVICE_NAME`: the name of the backend service.
     * `PRINCIPAL`: the principal to grant access to. For example, `group:my-group@example.com`, `user:test-user@example.com`, or `domain:example.com`.
     * `EXPRESSION`: the condition expression, written in the Common Expression Language (CEL). For example, this expression can be used to specify [access levels](https://docs.cloud.google.com/access-context-manager/docs/overview#access-levels) to configure context-aware access.
     * `TITLE`: a title for the condition.
     * `DESCRIPTION`: an optional description for the condition. Cloud Workstations still performs the IAM checks based on the IAM policy configured on the individual workstation resources. To avoid redundancy, consider configuring the IAP policy to [grant permissions](https://docs.cloud.google.com/iam/docs/principal-identifiers#allow) to a broad group that encompasses all approved workstation users, or your entire domain. You can primarily use this policy to specify [access levels](https://docs.cloud.google.com/access-context-manager/docs/overview#access-levels) to configure context-aware access.

For more information on granting access to users, see [gcloud iap web add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/iap/web/add-iam-policy-binding). 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
