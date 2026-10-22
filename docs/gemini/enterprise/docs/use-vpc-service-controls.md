---
url: https://docs.cloud.google.com/gemini/enterprise/docs/use-vpc-service-controls/
title: Secure your app with VPC Service Controls \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:42:39.616769+00:00
---

# Secure your app with VPC Service Controls  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/use-vpc-service-controls/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Secure your app with VPC Service Controls Stay organized with collections  Save and categorize content based on your preferences. 

To properly secure a Gemini Enterprise app and mitigate the risk of data exfiltration, you must configure a VPC Service Controls perimeter. Using [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) and [Access Context Manager](https://docs.cloud.google.com/access-context-manager/docs/overview), you can protect and control access to your Gemini Enterprise app and connected enterprise data.

**Note:** When using VPC Service Controls with Gemini Enterprise, creating new data stores is blocked until an administrator adds the required data sources and egress domains to the corresponding managed organization policy constraints. Existing data stores — including any that were previously enabled by request through a Google representative — continue to work without any further action. For more information, see Create data stores after enabling VPC Service Controls.

## Set up VPC Service Controls with Gemini Enterprise

To protect your Gemini Enterprise resources using VPC Service Controls, do the following:

  1. Ensure that you have a VPC Service Controls perimeter configured. You can create a new perimeter specifically for your Gemini Enterprise app, or use an existing perimeter that houses related resources.

For information about service perimeters, see [Service perimeter details and configuration](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters).

  2. Add the Google Cloud project that contains your Gemini Enterprise app to the list of protected resources within the service perimeter.

  3. Add the following APIs to the list of restricted services for the perimeter:

     * Discovery Engine API: `discoveryengine.googleapis.com`

**Tip:** We recommend using [dry run mode](https://docs.cloud.google.com/vpc-service-controls/docs/dry-run-mode) to test your service perimeter before enforcing it.

After the service perimeter is enabled and the Discovery Engine API is listed as a restricted service, VPC Service Controls enacts the following security measures:

  * The `discoveryengine.googleapis.com` API can no longer be accessed from the public internet.

  * Access to the Gemini Enterprise user interface is blocked, except where allowed by ingress rules.

  * Creating new data stores (which back [Gemini Enterprise actions](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-use-actions)) is blocked until an administrator adds the required data sources and egress domains to the corresponding [managed organization policy constraints](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/managed-policy-constraints-overview). Existing data stores — including any that were previously enabled by request through a Google representative — continue to work without any further action. For more information, see Create data stores after enabling VPC Service Controls.




## Restrict public access using Access Context Manager

Gemini Enterprise applications are made publicly accessible to the public internet. By default, Gemini Enterprise requires users to authenticate and requires authorization for access. VPC Service Controls and Access Context Manager provide additional controls that you can use to gate access.

Using Access Context Manager, you can define fine-grained, attribute-based access control for projects and resources in Google Cloud. To do this, you must define an [access policy](https://docs.cloud.google.com/access-context-manager/docs/overview#access-policies), which is an organization-wide container for [access levels](https://docs.cloud.google.com/access-context-manager/docs/overview#access-levels) and service perimeters.

Access levels describe the requirements that must be met in order for a request to be honored. For example, you can restrict requests based on the following:

  * Device type and operating system (requires a [Chrome Enterprise Premium](https://docs.cloud.google.com/chrome-enterprise-premium/docs/overview) license)
  * IP address
  * User identity

![Reference architecture using VPC Service Controls.](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/vpcsc-ref-arch.png)Reference architecture using VPC Service Controls to protect Gemini Enterprise.

In this reference architecture, a public IP subnetwork access level is used to build the VPC Service Controls access policy.

To gate access to Gemini Enterprise using Access Context Manager, follow the instructions in [Creating a basic access level](https://docs.cloud.google.com/access-context-manager/docs/create-basic-access-level) to create a basic access level. Specify the following options:

  1. For **Create conditions in** , choose **Basic mode**.

  2. In the **Access level title** field, enter `corp-public-block`.

  3. In the **Conditions** section, for **When condition is met, return** , select **TRUE**.

  4. For **IP Subnetworks** , select **Public IP**.

  5. For the IP address range, specify your external IP address.




## Apply VPC Service Controls to existing data stores

Enforcing a VPC Service Controls perimeter on a project with existing data stores is not supported.

To enforce VPC Service Controls on an existing data store:

  1. Delete and then recreate the data store.

This applies the service controls and lets traffic flow correctly.




## Create data stores after enabling VPC Service Controls

VPC Service Controls primarily aims to prevent data exfiltration by creating a secure service perimeter around your projects and resources. New data stores (which back Gemini Enterprise actions, such as sending an email or creating a Jira ticket) are potential paths for data to leave this perimeter, so VPC Service Controls blocks the creation of new data stores until an administrator explicitly permits them through managed organization policy constraints.

When you enable VPC Service Controls on a Google Cloud project containing an Gemini Enterprise app, the UI prevents you from creating new data stores. Data stores created before the perimeter was enabled — and any services that were previously enabled by request through a Google representative — continue to work; only creating new ones is gated.

To let administrators create a new data store inside the perimeter:

  1. Add the data source to the [**Restrict allowed data sources for data connectors**](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/configure-allowed-data-sources) managed organization policy constraint. Adding a data source to this constraint automatically permits its well-known essential domains (for example, `graph.microsoft.com` and `api.atlassian.com`).

  2. If the data store needs domains unique to your organization (for example, `cymbal.atlassian.net` or `cymbal.com`), add those domains to the [**Restrict egress domains for data connectors**](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/configure-allowed-egress-fqdns) managed organization policy constraint.




For an overview of these constraints, see [Managed policy constraints](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/managed-policy-constraints-overview).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
