---
url: https://docs.cloud.google.com/gemini/docs/configure-vpc-service-controls/
title: Configure VPC Service Controls for Gemini \u00a0|\u00a0 Gemini for Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:56:44.277597+00:00
---

# Configure VPC Service Controls for Gemini  |  Gemini for Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/docs/configure-vpc-service-controls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Guides ](https://docs.cloud.google.com/gemini/docs/overview)



Send feedback 

#  Configure VPC Service Controls for Gemini Stay organized with collections  Save and categorize content based on your preferences. 

[VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) helps you protect [Gemini products in Google Cloud](https://docs.cloud.google.com/gemini/docs/overview) by isolating resources within a security perimeter and reducing data exfiltration risks. Adding products to your [service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters) lets you manage API communication exclusively through authorized VPC networks and trusted endpoints.

## Before you begin

  1. [Ensure that Gemini Code Assist is set up for your Google Cloud user account and project.](https://docs.cloud.google.com/gemini/docs/codeassist/set-up-gemini)

  2. Make sure that you have the [required Identity and Access Management (IAM) roles](https://docs.cloud.google.com/vpc-service-controls/docs/access-control) to set up and administer VPC Service Controls.

  3. Ensure that you have a service perimeter at the organization level that you can use to set up Gemini. If you don't have a service perimeter at this level, you can [create one](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters).




## Add Gemini to your service perimeter

To use VPC Service Controls with Gemini, you add Gemini to the service perimeter at the organization level. The service perimeter must include all the services that you use with Gemini and other Google Cloud services that you want to protect.

To add Gemini to your service perimeter, follow these steps:

  1. In the Google Cloud console, go to the **VPC Service Controls** page.

[Go to VPC Service Controls](https://console.cloud.google.com/security/service-perimeter)

  2. Select your organization.

  3. On the **VPC Service Controls** page, click the name of your perimeter.

  4. Click **Add Resources** and do the following:

     1. For each project in which you have enabled Gemini, in the **Add resources** pane, click **Add project** , and then do the following:

     2. In the **Add projects** dialog, select the projects that you want to add.

If you're using [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc), add the host project and service projects to the service perimeter.

     3. Click **Add selected resources**. The added projects appear in the **Projects** section.

     4. For each VPC network in your projects, in the **Add resources** pane, click **Add VPC network** , and then do the following:

     5. From the list of projects, click the project that contains the VPC network.

     6. In the **Add resources** dialog, select the VPC network's checkbox.

     7. Click **Add selected resources**. The added network appears in the **VPC networks** section.

  5. Click **Restricted Services** and do the following:

     1. In the **Restricted Services** pane, click **Add services**.

     2. In the **Specify services to restrict** dialog, select **Gemini for Google Cloud API** and **Gemini Code Assist API** as the services that you want to secure within the perimeter.

     3. If you're planning to use [code customization](https://docs.cloud.google.com/gemini/docs/codeassist/code-customization-overview), select **Developer Connect API** as well. For more information about Developer Connect, see [Developer Connect overview](https://docs.cloud.google.com/developer-connect/docs/overview).

To learn how to use Organization Policy Service custom constraints to restrict specific operations on `developerconnect.googleapis.com/Connection` and `developerconnect.googleapis.com/GitRepositoryLink`, see [Create custom organization policies](https://docs.cloud.google.com/developer-connect/docs/custom-constraints).

**Note:** We recommend that you restrict all services when you create a perimeter to mitigate the risk of data exfiltration from Google Cloud services.
     1. Click **Add n services**, where n is the number of services you selected in the previous step.
  6. Optional: If your developers need to use Gemini within the perimeter from the Cloud Code plugin in their IDEs, then you'll need to configure the [ingress policy](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules).

Enabling VPC Service Controls for Gemini prevents all access from outside the perimeter, including running Gemini Code Assist IDE extensions from machines not in the perimeter, such as company laptops. Therefore, these steps are necessary if you want to use Gemini with the Gemini Code Assist plugin.

     1. Click **Ingress policy**.

     2. In the **Ingress rules** pane, click **Add rule**.

     3. In **From attributes of the API client** , specify the sources from outside the perimeter that require access. You can specify projects, access levels, and VPC networks as sources.

     4. In **To attributes of Google Cloud resources/services** , specify the service name of Gemini and Gemini Code Assist API.

For a list of ingress rule attributes, see [Ingress rules reference](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#ingress-rules-reference).

  7. Optional: If your organization uses [Access Context Manager](https://docs.cloud.google.com/access-context-manager/docs) and you want to provide developers access to protected resources from outside the perimeter, then set access levels:

     1. Click **Access Levels**.

     2. In the **Ingress Policy: Access Levels** pane, select the **Choose Access Level** field.

     3. Select the checkboxes corresponding to the access levels that you want to apply to the perimeter.

  8. Click **Save**.




After you complete these steps, VPC Service Controls checks all calls to the Gemini for Google Cloud API to ensure that they originate from within the same perimeter.

## Configure VPC networks

You need to configure your VPC networks so that the requests sent to the regular `googleapis.com` virtual IP are automatically routed to the [restricted virtual IP (VIP) range](https://docs.cloud.google.com/vpc/docs/private-access-options#domain-vips), `199.36.153.4/30` (`restricted.googleapis.com`), where your Gemini service is serving. You don't need to change any configurations in the Gemini Code Assist IDE extensions.

For each VPC network in your project, follow these steps to block outbound traffic except for traffic to the restricted VIP range:

  1. Enable [Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access) on the subnets hosting your VPC network resources.

  2. [Configure firewall rules](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-private-connectivity#configure-firewall) to prevent data from leaving the VPC network.

**Caution:** Failure to properly configure firewall rules can leave your services vulnerable to data exfiltration.
     1. Create a deny egress rule that blocks all outbound traffic.
**Note:** Ensure that the deny all egress firewall rule has a priority after `1000`. Otherwise, traffic from the Serverless VPC Access connector to your service are blocked.
     1. Create an allow egress rule that permits traffic to `199.36.153.4/30` on TCP port `443`. Ensure that the allow egress rule has a priority before the deny egress rule that you have just created—this allows egress only to the restricted VIP range.
  3. [Create a Cloud DNS response policy](https://docs.cloud.google.com/dns/docs/zones/manage-response-policies#creating-response-policy).

  4. [Create a rule for the response policy](https://docs.cloud.google.com/dns/docs/zones/manage-response-policies#create-response-policy-rule) to resolve `*.googleapis.com` to `restricted.googleapis.com` with the following values:

     * DNS name: `*.googleapis.com.`

     * Local data: `restricted.googleapis.com.`

     * Record type: `A`

     * TTL: `300`

     * RR data: `199.36.153.4|199.36.153.5|199.36.153.6|199.36.153.7`

The IP address range for `restricted.googleapis.com` is `199.36.153.4/30`.




After you complete these steps, the requests that originate from within the VPC network are unable to leave the VPC network, preventing egress outside the service perimeter. These requests can only reach Google APIs and services that check VPC Service Controls, preventing exfiltration through Google APIs.

## Additional configurations

Depending on the Google Cloud products that you use with Gemini, you must consider the following:

  * **Client machines connected to the perimeter.** Machines that are inside the VPC Service Controls perimeter can access all Gemini experiences. You can also extend the perimeter to an authorized [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) or [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect) from an external network.

  * **Client machines outside the perimeter.** When you have client machines outside the service perimeter, you can grant controlled access to the restricted Gemini service.

    * For more information, see [Allow access to protected resources from outside a perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/use-access-levels).

    * For an example of how to create an access level on a corporate network, see [Limit access on a corporate network](https://docs.cloud.google.com/access-context-manager/docs/create-basic-access-level#corporate-network-example).

    * Review the [limitations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_duetai) when using VPC Service Controls with Gemini.

  * **Gemini Code Assist.** For compliance with VPC Service Controls, make sure the IDE or workstation you're using doesn't have access to `https://www.google.com/tools/feedback/mobile` through firewall policies.

    * **Gemini Code Assist on GitHub.** If you want to enable [improve response quality](https://docs.cloud.google.com/gemini/docs/code-review/customize-repo-review#bulk-config), you shouldn't place your Google Cloud project within a [VPC Service Controls service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters).
  * **Cloud Workstations.** If you use Cloud Workstations, follow the instructions in [Configure VPC Service Controls and private clusters](https://docs.cloud.google.com/workstations/docs/configure-vpc-service-controls-private-clusters).




## What's next

  * For information about the compliance offerings in Google Cloud, see [Compliance resource center](https://cloud.google.com/security/compliance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
