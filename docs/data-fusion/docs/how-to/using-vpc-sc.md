---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/using-vpc-sc/
title: Use VPC Service Controls with Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:58:37.344941+00:00
---

# Use VPC Service Controls with Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/using-vpc-sc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Use VPC Service Controls with Cloud Data Fusion Stay organized with collections  Save and categorize content based on your preferences. 

If you plan to create a [Cloud Data Fusion instance with a private IP address](https://docs.cloud.google.com/data-fusion/docs/how-to/create-private-ip), you can provide additional security by first establishing a security perimeter for the instance using [VPC Service Controls (VPC-SC)](https://docs.cloud.google.com/vpc-service-controls/docs/overview). The VPC-SC security perimeter around the private Cloud Data Fusion instance and other Google Cloud resources helps mitigate the risk of data exfiltration. For example, with VPC Service Controls, if a Cloud Data Fusion pipeline reads data from a [supported resource](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products), such as a BigQuery dataset, located within the perimeter, then tries to write the output to a resource outside the perimeter, the pipeline will fail.

Cloud Data Fusion resources are exposed on two API surfaces:

  1. The `datafusion.googleapis.com` control plane API surface, which allows you to perform instance-level operations, such as the creation and deletion of instances.

  2. The `datafusion.googleusercontent.com` data plane API surface (the [Cloud Data Fusion Web UI](https://docs.cloud.google.com/data-fusion/docs/concepts/overview#using_the_code-free_web_ui) in the Google Cloud console), which executes on a Cloud Data Fusion instance to create and execute data pipelines.




You set up VPC Service Controls with Cloud Data Fusion by restricting connectivity to both of these API surfaces.

Strategies:

  * Cloud Data Fusion pipelines are executed on Managed Service for Apache Spark clusters. To protect a Managed Service for Apache Spark cluster with a service perimeter, follow the instructions for [setting up private connectivity](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-private-connectivity) to allow the cluster to function inside the perimeter.

  * Don't use plugins that use Google Cloud APIs that are not [supported by VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products). If you use unsupported plugins, Cloud Data Fusion will block the API calls, resulting in pipeline preview and execution failure.

  * To use Cloud Data Fusion within a VPC Service Controls service perimeter, add or configure several DNS entries to point the following domains to the restricted VIP (Virtual IP address):

    * `datafusion.googleapis.com`
    * `*.datafusion.googleusercontent.com`
    * `*.datafusion.cloud.google.com`



Limitations:

  * Establish the VPC Service Controls security perimeter before creating your Cloud Data Fusion private instance. Perimeter protection for instances created prior to setting up VPC Service Controls is not supported.

  * Currently, the Cloud Data Fusion data plane UI does not support specifying access levels using [identity based access](https://docs.cloud.google.com/access-context-manager/docs/create-basic-access-level#members-example).




## Restricting Cloud Data Fusion API surfaces

### Restricting the control plane surface

See [Setting up private connectivity to Google APIs and services](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-private-connectivity) to restrict connectivity to the `datafusion.googleapis.com` API control plane surface.

### Restricting the data plane surface

To set up private connectivity to the API data plane, configure DNS by completing the following steps for both the `*.datafusion.googleusercontent.com` and `*.datafusion.cloud.google.com` domains.

  1. Create a new private [zone using Cloud DNS](https://console.cloud.google.com/net-services/dns/zones):

     1. Zone type: Check **private**
     2. Zone name: datafusiongoogleusercontentcom
     3. DNS name: datafusion.googleusercontent.com
     4. Network: Select the private IP network you chose when you created your Cloud Data Fusion instance.

![How to fill in the zone fields.](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/vpc-sc/dns-zone.png)
  2. From the [Cloud DNS](https://console.cloud.google.com/net-services/dns/zones) page, click your `datafusiongoogleusercontent` DNS zone name to open the **Zone details** page. Two records are listed: an NS and an SOA record. Use **Add Standard** to add the following two record sets to your datafusiongoogleusercontent DNS zone.

     1. Add a CNAME record: In the **Create record set** dialog, fill in the following fields to map DNS name `*.datafusion.googleusercontent.com.` to the canonical name `datafusion.googleusercontent.com`:

        * DNS name: "*.datafusion.googleusercontent.com"
        * Canonical name: "datafusion.googleusercontent.com"

![How to fill in the zone fields.](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/vpc-sc/fusion-dns-cname.png)
     2. Add an A record: In a new **Create record set** dialog, fill in the following fields to map DNS name `datafusion.googleusercontent.com.` to IP addresses `199.36.153.4` \- `199.36.153.7`:

        * DNS name: ".datafusion.googleusercontent.com"
        * IPv4 address:

          * 199.36.153.4
          * 199.36.153.5
          * 199.36.153.6
          * 199.36.153.7
![How to fill in the zone fields.](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/vpc-sc/fusion-dns-ip.png)

The `datafusiongoogleusercontent` **Zone details** page shows the following record sets:

![How to fill in the zone fields.](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/vpc-sc/fusion-dns-records.png)
  3. Follow the above steps to create a private DNS zone and add a record set for the `*.datafusion.cloud.google.com` domain.




## What's next

  * Learn about [Creating a private instance](https://docs.cloud.google.com/data-fusion/docs/how-to/create-private-ip).
  * Learn more about [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
