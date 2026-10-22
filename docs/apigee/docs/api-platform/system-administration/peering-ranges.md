---
url: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/peering-ranges/
title: Understanding peering ranges \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:28:46.064668+00:00
---

# Understanding peering ranges  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/peering-ranges/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Understanding peering ranges Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** , but not to **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

**Important:** This topic only applies to organizations that were created with VPC peering enabled. See also [Apigee networking options](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/networking-options).

Apigee facilitates communications between client API requests and Apigee and Cloud services through a connection between two networks: the Apigee VPC (or _runtime plane_) and the Customer VPC. These two networks are tethered together using [a private connection](https://docs.cloud.google.com/vpc/docs/configure-private-services-access) in a process known as _VPC peering_.

The following example shows how VPC peering enables communication between the Apigee VPC and the Customer VPC:

![VPC peering between Apigee VPC and Customer VPC](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/ng-saas/vpc-peering-arch.png)

VPC peering enables the Apigee VPC to process requests and responses sent to the Customer VPC:

  * **Northbound traffic:** API proxy requests sent from clients to the Customer VPC that are passed through to the Apigee runtime plane for processing. Additional services such as logging, identity management, and metrics are also accessible to the runtime plane.

  * **Southbound traffic:** API proxy requests that must access target APIs or other backend services on the Customer VPC constitute the southbound route. These southbound services process the responses before returning them to the Customer VPC for further processing by the Apigee runtime before a response is sent to the client.




The Apigee provisioning step, [Configure service networking](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli#service-networking), performs the VPC peering and allocates an IP Address Range (a CIDR range) to Apigee. 

## Network sizing

Each [ Apigee instance](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/instances) requires a non-overlapping CIDR range of /22. The Apigee runtime plane (aka data plane) is assigned IP addresses from within the CIDR range. As a result, it's important that the range is reserved for Apigee and not used by other applications in the customer VPC network. 

**Note:** In addition to the /22 range that is created, Apigee requires a non-overlapping, available /28 CIDR range. This /28 range is used by Apigee to access the instance for troubleshooting purposes and cannot be customized or changed. See also [Creating instances](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/instances).

An instance is created when: 

  1. An Apigee organization is first provisioned, either through the [UI wizard](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/overview) or the [command-line interface](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli) (CLI).
  2. When expanding Apigee to a new Cloud region for an existing organization. See also [Expanding Apigee to multiple regions](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/multi-region).

**Note:** You must have the role of Apigee Organization Admin or Apigee Operator to create an instance.

When you create an instance, there are two options for specifying a network IP range: 

  * **Auto-allocate the range** \- When you create an Apigee instance, allow Apigee to allocate any available, non-overlapping range from the larger range allocated to Google. Each time an instance is re-created, the IP range is auto-allocated. In such cases, it is possible that the new instance may use a new IP range, if one is available and is non-overlapping with other products or services.
  * **Specify an IP range** \- You can specify the IP range that Apigee will use. This IP range must be from the non-overlapping range that is peered with Apigee. This option is useful when you want to allocate a larger IP range for multiple Cloud products, such as Cloud SQL, Cloud Memorystore, Apigee, and others, and you also want to be able to specify actual IP ranges for each of these products. This range could be a non-RFC 1918 IP range as long as the range is not a privately used public IP address (PUPI)). .



After you create an instance, you _cannot_ change the CIDR range. To change the CIDR range, you must delete the instance and reconfigure a new one. Be careful if you have only one instance in an organization. 

##  Considerations 

Before allocating CIDR ranges, refer to [Considerations](https://cloud.google.com/vpc/docs/configure-private-services-access#considerations) in the Virtual Private Cloud documentation. 

When creating a peering connection with Google, ensure that public IPs are not exchanged. To check: 

  1. In the Google Cloud console, go to the **VPC Network Peering** page. See also [ Using VPC Network Peering](https://cloud.google.com/vpc/docs/using-vpc-peering#console_1). 

[Go to VPC network peering](https://console.cloud.google.com/networking/vpc-connectivity/peering)

  2. Select your VPC network peering connection.
  3. In the Peering connection details, make sure that **Exchange subnet routes with public IP** is set to **None** , as shown in the following screenshot. 

![View peering connection details in the Cloud console.](https://docs.cloud.google.com/static/apigee/docs/api-platform/system-administration/images/peering-connection-details.png)

**Note:** Apigee uses _privately used public IP_ (PUPI) addresses, so setting **Exchange subnet routes with public IP** to something other than **None** could potentially cause an IP conflict.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
  *[VPC]: Virtual Private Cloud
