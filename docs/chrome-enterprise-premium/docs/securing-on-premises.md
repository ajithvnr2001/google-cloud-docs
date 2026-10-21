---
url: https://docs.cloud.google.com/chrome-enterprise-premium/docs/securing-on-premises/
title: Securing non-Google Cloud applications using the On-Prem Connector \u00a0|\u00a0 Chrome Enterprise Premium \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:07:44.418998+00:00
---

# Securing non-Google Cloud applications using the On-Prem Connector  |  Chrome Enterprise Premium  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chrome-enterprise-premium/docs/securing-on-premises/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Chrome Enterprise Premium ](https://docs.cloud.google.com/chrome-enterprise-premium/docs)
  * [ Guides ](https://docs.cloud.google.com/chrome-enterprise-premium/docs/overview)



Send feedback 

#  Securing non-Google Cloud applications using the On-Prem Connector Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to secure an HTTP or HTTPS based, on-premises app outside of Google Cloud with [Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/iap/docs/concepts-overview) by deploying an IAP connector.

## Before you begin

Before you begin, you need the following:

  * An HTTP or HTTPS based on-premises app.

  * A Cloud Identity member [granted the **Owner** role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant_access) on your Google Cloud project.

**Note:** [IAM basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic) are highly permissive roles that give broad access to Google Cloud resources. We recommend that you avoid granting basic roles in a production environment. You can grant basic roles in a development or test environment.
  * The [Google APIs Service Agent](https://docs.cloud.google.com/iam/docs/service-agents#google-apis-service-agent) granted with the owner role.

  * A Google Cloud project with [billing enabled](https://docs.cloud.google.com/billing/docs/how-to/modify-project).

  * The external URL to use as the ingress point for traffic to Google Cloud. For example, `hr.example.com`.

  * An SSL or TLS certificate for the DNS hostname that is used as the ingress point for traffic to Google Cloud. An existing self-managed or [Google-managed](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates#managed-certs) certificate can be used. If you don't have a certificate, create one using [Let's Encrypt](https://letsencrypt.org/).

  * If VPC Service Controls is enabled, a VPC network with an [egress policy](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#egress_rules_reference) on the `cp` action for the VM service account to the `gce-mesh` bucket in project `278958399328`. The policy grants the VPC network permission to retrieve the Envoy binary file from the gce-mesh bucket. The permission is granted by default, if VPC Service Controls is not enabled.

  * Disable an external IP by completing the following steps:

    * Enable Private Google Access on the VPC subnet that is used for the IAP connector. For more information, see [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access).

    * Verify that the firewall configuration of the VPC network lets the VMs access IP addresses of Google APIs and services. By default, this access is granted, but users can change it explicitly. For information on how to find the IP range, see [IP addresses for default domains](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#ip-addr-defaults).




## Deploy a connector for an on-premises app

  1. Go to the IAP page.

[Go to IAP](https://console.cloud.google.com/security/iap)

  2. To begin setting up your connector deployment for an on-premises app, click **Connect new application** and select **Connect via on-prem connector**.

  3. To ensure that the required APIs are enabled, click **Enable APIs and continue** in the right-side panel.

  4. Select the configuration details and click **Next** :

     * Choose whether the deployment should use a Google-managed certificate or one managed by you.

     * Select the network and subnet for the deployment (or choose to create a new one).

  5. Complete the following details for the on-premises app you want to add:

     * Enter the external URL of requests coming to Google Cloud. This URL is where traffic enters the environment.

     * Enter a name for the app, which will also serve as the name for a new [backend service](https://docs.cloud.google.com/load-balancing/docs/backend-service) behind the load balancer.

     * Select the region.

     * Provide the on-premises endpoint type and its details:

       * Fully qualified domain name (FQDN): The domain where the connector should forward the traffic.

       * IP address: One or more zones where the IAP connector should be deployed (for example, `us-central1-a`). For each zone, specify the IPv4 address of the internal destination for the on-premises app to which IAP routes traffic after a user is authorized and authenticated.

**Note:** If your on-premises endpoint is an IP address, consider using a [hybrid connectivity network endpoint group](https://cloud.google.com/load-balancing/docs/negs/hybrid-neg-concepts#use-case_routing_traffic_to_an_on-premises_location_or_another_cloud) directly with a load balancer instead of using the IAP on-premises connector.
     * Select the protocol used by the on-premises endpoint.

     * Enter the port number used by the on-premises endpoint, such as 443 for HTTPS or 80 for HTTP.

  6. To save the details for that app, click **Done**. You can also define additional on-premises apps for the deployment.

  7. To begin deployment of the apps you've defined, click **Submit**.




After the deployment is complete, your on-premises connector apps appear in the **Applications** table and you can enable IAP.

If you choose to let Google auto-generate and manage the certificates, it might take a few minutes for the certificates to provision. You can check the status at the Cloud Load Balancing detail page. For more information about the status, see [troubleshooting page](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/troubleshooting#certificate-managed-status).

## Manage a connector for an on-premises app

  * To add more apps to your deployment, click **Connect new application** and then **Connect via on-prem connector**.

  * To delete the on-premises connector by deleting the entire deployment, do the following:

    1. Go to the Deployment Manager page.

[Go to Deployment Manager](https://console.cloud.google.com/dm/deployments)

    2. In the list of deployments, select the checkbox next to the `on-prem-app-deployment` deployment.

    3. On the top of the page, click **Delete**.

  * To delete individual apps, click the delete button in the **Applications** tab. The on-premises connector must contains at least one app. To remove all apps, delete the entire deployment.




## Next steps

  * Set richer context rules by [applying access levels](https://docs.cloud.google.com/chrome-enterprise-premium/docs/access-levels).
  * See [Context-Aware Access logs in Cloud Audit Logs](https://docs.cloud.google.com/access-context-manager/docs/audit-logs).
  * Learn more about [IAP](https://docs.cloud.google.com/iap/docs/concepts-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
