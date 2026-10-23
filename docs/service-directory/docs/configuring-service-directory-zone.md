---
url: https://docs.cloud.google.com/service-directory/docs/configuring-service-directory-zone/
title: Configure a DNS zone \u00a0|\u00a0 Service Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:33:14.730673+00:00
---

# Configure a DNS zone  |  Service Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-directory/docs/configuring-service-directory-zone/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Service Directory ](https://docs.cloud.google.com/service-directory/docs)
  * [ Guides ](https://docs.cloud.google.com/service-directory/docs/overview)



Send feedback 

#  Configure a DNS zone Stay organized with collections  Save and categorize content based on your preferences. 

You can create a Service Directory zone that allows your Google Cloud-based services to query your Service Directory namespace using Cloud DNS.

These instructions require that you already have a Service Directory namespace in place. If you do not, first create a namespace using the procedure in [Configuring Service Directory](https://docs.cloud.google.com/service-directory/docs/configuring-service-directory).

Once you have attached a Service Directory zone to the namespace, all services and endpoints within the namespace become available over DNS on the private network. All service and endpoint updates are immediately reflected in their DNS records. However, the service and the endpoint are not available over DNS.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `servicedirectory.namespaces.associatePrivateZone`



**Roles**

  * `servicedirectory.admin`
  * `servicedirectory.editor`

**Note:** Service visibility (_who_ is authorized to look up a service) changes once a Service Directory private zone is assigned to a namespace. The network, not IAM, determines the access when responding to DNS queries. For more details, see [Roles and permissions](https://docs.cloud.google.com/dns/docs/access-control).

## Limitations

Service Directory integration with Cloud DNS has the following limitations:

  * You can only associate a Service Directory zone with a namespace when you create the zone.
  * A Service Directory zone must be in the same project as the Service Directory namespace that it is associated with.
  * A Service Directory zone cannot also be a forwarding zone, a regular private zone, or a public zone.



## Create a Service Directory zone backed by a namespace

You can only associate a Service Directory zone with a namespace when you create the zone. A Service Directory zone cannot also be a forwarding zone, a regular private zone, or a public zone.

###  Console 

  1. Go to the Cloud DNS page in the Google Cloud console.   
[Go to Cloud DNS ](https://console.cloud.google.com/net-services/dns/zones)
  2. Click **Create zone**.
  3. In the **Zone type** section, click **Private**.
  4. Enter a name for the zone.
  5. Enter a DNS name for the zone.
  6. Under **Options** , select **Use a service directory namespace**.
  7. Under **Networks** , select one or more networks that can use the Service Directory zone.
  8. Select the **Region** where the namespace that you want to link lives.
  9. Select the **Namespace** that you want to link.
  10. Click **Create**.



###  gcloud 
    
    
    gcloud dns managed-zones create SD_ZONE \
       --dns-name DNS_NAME \
       --description DESCRIPTION \
       --visibility private \
       --networks https://www.googleapis.com/compute/v1/projects/project_ID/global/networks/network \
       --service-directory-namespace https://servicedirectory.googleapis.com/v1/projects/project_ID/locations/region/namespaces/namespace-name
    

Replace the following values:

  * `SD_ZONE`: the name of the Service Directory zone that you are creating.
  * `DNS_NAME`: the DNS name, such as `us-east1.example.com.`, for the new zone.
  * `DESCRIPTION`: a description of the zone, such as `this zone is backed by Service Directory`.
  * https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/NETWORK: the FQDN of the networks that can use the zone.
  * https://www.servicedirectory.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/registries/NAMESPACE_NAME: the FQDN of the namespace that you are linking.



**Note:** You can associate only one Service Directory zone with a given namespace, and you cannot associate a given zone with multiple namespaces. You must create the Cloud DNS zone and the Service Directory namespace in the same project.

## Delete the Service Directory zone

At any point, you can delete a Service Directory zone. This deletion happens through Cloud DNS and has no effect on any associated Service Directory namespaces. The associated namespace continues to be available for look up through HTTP and gRPC. For more information, see [Delete a managed zone](https://docs.cloud.google.com/dns/docs/zones#delete_a_managed_zone).

You can [delete a service](https://docs.cloud.google.com/service-directory/docs/configuring-service-directory#deleting_a_service_from_a_namespace) or namespace that has a Service Directory zone pointing to it without deleting the zone. If you do, any further DNS queries for that service return `NXDOMAIN`.

## What's next

  * To learn how to secure Service Directory in a service perimeter, see [Service Directory and VPC Service Controls](https://docs.cloud.google.com/service-directory/docs/securing-with-vpc-sc).
  * To get an overview of Service Directory, see the [Service Directory overview](https://docs.cloud.google.com/service-directory/docs/overview).
  * To find solutions for common issues that you might encounter when using Service Directory, see [Troubleshooting](https://docs.cloud.google.com/service-directory/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
