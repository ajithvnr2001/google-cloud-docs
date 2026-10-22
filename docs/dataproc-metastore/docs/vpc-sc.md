---
url: https://docs.cloud.google.com/dataproc-metastore/docs/vpc-sc/
title: VPC Service Controls with Dataproc Metastore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:59.557739+00:00
---

# VPC Service Controls with Dataproc Metastore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataproc-metastore/docs/vpc-sc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataproc Metastore ](https://docs.cloud.google.com/dataproc-metastore/docs)
  * [ Guides ](https://docs.cloud.google.com/dataproc-metastore/docs/create-service-cluster)



Send feedback 

#  VPC Service Controls with Dataproc Metastore Stay organized with collections  Save and categorize content based on your preferences. 

To further secure your Dataproc Metastore services, you can protect them using [VPC Service Controls (VPC-SC)](https://docs.cloud.google.com/vpc-service-controls/docs).

VPC Service Controls helps mitigate the risk of data exfiltration. Using VPC Service Controls, you can add projects to service perimeters that protect resources and services from requests that cross the perimeter.

To learn more about VPC Service Controls, see [Overview of VPC Service Controls](https://cloud.google.com/vpc-service-controls/docs/overview).

Dataproc Metastore resources are exposed on the `metastore.googleapis.com` API, which lets you perform service-level operations, such as the creation and deletion of services.

You set up VPC Service Controls with Dataproc Metastore by restricting connectivity to this API surface.

## Limitations and advisories

  * Dataproc Metastore utilizes Cloud Run for connectivity when using the [gRPC endpoint protocol](https://docs.cloud.google.com/dataproc-metastore/docs/about-endpoint-protocols#grpc). The same Cloud Run [limitations and advisories](https://docs.cloud.google.com/run/docs/securing/using-vpc-service-controls#limitations) apply when using this endpoint with VPC Service Controls.
  * Cloud Run dry run request logs are only written when the Cloud Run services are invoked and the [ingress is internal](https://docs.cloud.google.com/run/docs/securing/ingress#settings). Dataproc Metastore uses internal ingress only when the perimeter is in enforced mode. You won't see dry run violations when using the Cloud Run endpoint in dry run mode.



## Configure the Virtual Private Cloud (VPC) network

You can configure the VPC network to restrict Private Google Access with respect to a service perimeter. This ensures that hosts on your VPC or on-premises network can only communicate with Google APIs and services that are supported by VPC Service Controls in ways which conform to the associated perimeter's policy.

For more information, see [Setting up private connectivity to Google APIs and services](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-private-connectivity).

## Create a service perimeter

During this procedure, you select the Dataproc Metastore projects that you want the VPC service perimeter to protect.

To create a service perimeter, follow the instructions in [Creating a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters).

### Add more projects to the service perimeter

To add existing Dataproc Metastore projects to the perimeter, follow the instructions in [Updating a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#update).

**Note:** If your Dataproc Metastore service uses a network belonging to a different project, and Compute Engine is protected by the service perimeter, then the metastore project and network project must be in the same perimeter.

### Add the Dataproc Metastore and Cloud Storage APIs to the service perimeter

To mitigate the risk of your data being exfiltrated from Dataproc Metastore, for example, when using Dataproc Metastore import or export APIs, you must restrict both the **Dataproc Metastore API** and the **Cloud Storage API**.

**Note:** You can only import or export data from a Cloud Storage bucket that is in a project that resides in the same service perimeter as the Dataproc Metastore service. If you've configured Kerberos for a service, then the Secret Manager secret and krb5.conf Cloud Storage object must belong to a project that resides in the same service perimeter as the service.

To add Dataproc Metastore and Cloud Storage APIs as restricted services:

### Console

  1. In the Google Cloud console, open the VPC Service Controls page:

[Go to the VPC Service Controls page in the Google Cloud console](https://console.cloud.google.com/security/service-perimeter)

  2. On the **VPC Service Controls** page, in the table, click the name of the service perimeter that you want to modify.

  3. Click **Edit Perimeter**.

  4. On the **Edit VPC Service Perimeter** page, click **Add Services**.

  5. Add **Dataproc Metastore API** and **Cloud Storage API**.

  6. Click **Save**.




### gcloud

Run the following `gcloud access-context-manager perimeters update` command:
    
    
     gcloud access-context-manager perimeters update PERIMETER_ID   
    
         --policy=POLICY_ID   
    
         --add-restricted-services=metastore.googleapis.com,storage.googleapis.com
     

Replace the following:

  * `PERIMETER_ID`: The ID of the perimeter or the fully qualified identifier for the perimeter.
  * `POLICY_ID`: The ID of the access policy.



## Create an access level

Optionally, to permit external access to protected resources inside a perimeter, you can use access levels. Access levels apply only to requests for protected resources coming from outside the service perimeter. You can't use access levels to give protected resources permission to access data and services outside the perimeter.

See [Allowing access to protected resources from outside a perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/use-access-levels).

## What's next

  * [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs)
  * [Service access](https://docs.cloud.google.com/dataproc-metastore/docs/access-service)
  * [Dataproc Metastore IAM and access control](https://docs.cloud.google.com/dataproc-metastore/docs/iam-and-access-control)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
