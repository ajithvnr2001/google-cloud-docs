---
url: https://docs.cloud.google.com/storage/docs/update-ip-filter/
title: Create or update IP filtering rules on an existing bucket \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:29:30.452533+00:00
---

# Create or update IP filtering rules on an existing bucket  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/update-ip-filter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Create or update IP filtering rules on an existing bucket Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create or update the [bucket IP filtering](https://docs.cloud.google.com/storage/docs/ip-filtering-overview) rules on an existing bucket.

## Required roles

To get the required permissions for updating the IP filtering rules on a bucket, ask your administrator to grant you the Storage Admin (`roles/storage.admin`) role on the bucket. This role contains the permissions required to update bucket IP filtering rules.

To see the exact permissions that are required, expand the **Required permissions** section:

#### Required permissions

  * `storage.buckets.update`
  * `storage.buckets.setIpFilter`



You can also get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles). You might be able to get these permissions with other predefined roles as well. To see which roles are associated with which permissions, refer to [IAM roles for Cloud Storage](https://docs.cloud.google.com/iam/docs/understanding-roles).

For instructions about granting roles for buckets, see [Set and manage IAM policies on buckets](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).

## Create or update IP filtering rules on an existing bucket

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket you want to update.

  3. On the **Bucket details** page, click the **Configuration** tab.

  4. In the **Permissions** section, navigate to **IP filtering**. Then, click edit **Edit IP filtering configuration**.

  5. On the **IP filtering** page, click add_box**Configure**.

**Tip:** For a summary of the options in the navigation menu, see [IP filtering configuration options](https://docs.cloud.google.com/storage/docs/ip-filtering-overview#configurations).
  6. In the **Configure IP filtering** overlay window, depending on the IP filtering configuration you want to specify, use the appropriate navigation menu. After completing the steps in each section, click **Continue** to proceed to the next step.




#### Public IP addresses

To allow access from public IP addresses, do the following:

  1. Click **Public internet**.

  2. In the **Public internet** pane that appears, specify one or more IPv4 address ranges or IPv6 CIDR ranges in the **Allowed IP range(s)** field. For example, `192.0.2.0/24` or `2001:db8::/32`. If you specify invalid entries, an error message indicates which entries need correction.




#### VPC networks

To allow access from VPC networks, do the following:

  1. Click **VPC network(s)**.

  2. In the **VPC networks** pane that appears, do the following for each network:

     1. Click **Add VPC network**.
     2. In the **New VPC network** section, specify the following information: 
        * In the **Project ID** field, enter your project ID.
        * In the **Network name** field, enter your network name.
        * In the **Allowed IP range(s)** field, enter one or more IPv4 or IPv6 CIDR ranges, for example, `192.0.2.0/24`, 2001:db8::/32`. If you specify invalid entries, an error message indicates which entries need correction.
     3. Click **Done**.



#### Additional settings

To permit trusted Google Cloud service agents and VPC networks from other organizations to bypass your IP filtering configuration, do the following:

  1. Click **Additional settings**.

  2. In the **Additional settings** pane that appears, do the following:

  3. In the **Google Cloud service agent access** section, select one of the following radio buttons:

     * **Allow service agent access** : Enables Google Cloud services such as BigLake, Storage Insights, Vertex AI, and BigQuery to bypass the IP filtering validation when they need to access this bucket.

     * **Deny service agent access** : Enforces the IP filter rules for Google Cloud service agents.

  4. In the **(Optional) Cross-organization VPC access** section, do one of the following:

     * To permit access from specified VPC networks located in different Google Cloud organizations, click the toggle to the **Allow** position.

     * To block access from VPC networks outside of your Google Cloud organization, click the toggle to **Deny** (default state) position.




#### Review

To review the IP filtering configuration, do the following:

  1. In the **Review** pane that appears, click the expand_more expander arrow next to **Public internet** or **VPC network(s)** to review the specified IP ranges or VPC and verify the **Additional settings** configuration.

  2. If you need to modify a setting, click **Back** to return to the previous configuration steps.

  3. After you review all configurations, click **Enable** to save the IP filtering configuration.




### gcloud

  1. Verify that you have the Google Cloud CLI version 526.0.0 or later installed:
         
         gcloud version | head -n1
         

  2. If you have an earlier gcloud CLI version installed, update the version:
         
         gcloud components update --version=526.0.0
         

  3. Create a JSON file that defines rules for incoming requests. For examples and information about how to structure the bucket IP filtering rules, see [Bucket IP filtering configurations](https://docs.cloud.google.com/storage/docs/create-ip-filter#ip-filtering-configurations).
         
         {
               "mode":"MODE",
               "publicNetworkSource":{
                   "allowedIpCidrRanges":[
                     "RANGE_CIDR",
                     "..."
                   ]
               },
               "vpcNetworkSources":[
                   {
                     "network":"projects/PROJECT_ID/global/networks/NETWORK_NAME",
                     "allowedIpCidrRanges":[
                         "RANGE_CIDR",
                         "..."
                     ]
                   },
                   "..."
               ],
               "allowCrossOrgVpcs": ALLOW_CROSS_ORG_VPCS,
               "allowAllServiceAgentAccess": ALLOW_ALL_SERVICE_AGENT_ACCESS
             }
             

Where:

     * `MODE` is the mode of the bucket IP filtering configuration. Valid values are `Enabled` and `Disabled`. When set to `Enabled`, IP filtering rules are applied to a bucket. Any incoming request to the bucket is evaluated against these rules. When set to `Disabled`, all incoming requests are allowed to access the bucket.

     * `RANGE_CIDR` is a public network IPv4 or IPv6 address range that's allowed to access the bucket. You can enter one or multiple address ranges as a list.

     * `PROJECT_ID` is the project ID where the Virtual Private Cloud (VPC) network exists. To configure multiple VPC networks, you need to specify the project where each network is located.

     * `NETWORK_NAME` is the name of the VPC network that is allowed to access the bucket. To configure multiple VPC networks, you need to specify a name for each network.

     * `ALLOW_CROSS_ORG_VPCS` is a boolean value that indicates whether to allow VPC networks that are defined in `vpcNetworkSources` to originate from a different organization. This field is optional. If set to `true`, the request allows cross-organizational VPC networks. If set to `false`, the request restricts the VPC networks to the same organization as the bucket. If not specified, the default value is `false`. This field applies only if `vpcNetworkSources` is not empty.

     * `ALLOW_ALL_SERVICE_AGENT_ACCESS` is a boolean value that indicates whether to allow [service agents](https://docs.cloud.google.com/iam/docs/service-agents) to access the bucket, regardless of the IP filter configuration. If the value is `true`, other Google Cloud services can use service agents to access the bucket without IP-based validation.

  4. To update bucket IP filtering rules, run the [`gcloud storage buckets update`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/update) command in your development environment:
         
         gcloud storage buckets update gs://BUCKET_NAME --ip-filter-file=IP_FILTER_CONFIG_FILE

Where:

     * `BUCKET_NAME` is the name of your bucket. For example, `my-bucket`.
     * `IP_FILTER_CONFIG_FILE` is the JSON file you created.



### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create a JSON file that contains the settings for the bucket, which must include the `name` and the `ipFilter` configuration fields for the bucket. For examples and information about how to structure the bucket IP filtering rules, see [Bucket IP filtering configurations](https://docs.cloud.google.com/storage/docs/create-ip-filter#ip-filtering-configurations).
         
         {
           "ipFilter":{
               "mode":"MODE",
               "publicNetworkSource":{
                 "allowedIpCidrRanges":[
                     "RANGE_CIDR",
                     "..."
                 ]
               },
               "vpcNetworkSources":[
                 {
                     "network":"projects/PROJECT_ID/global/networks/NETWORK_NAME",
                     "allowedIpCidrRanges":[
                       "RANGE_CIDR",
                       "..."
                     ]
                 },
                 "..."
               ],
               "allowCrossOrgVpcs": ALLOW_CROSS_ORG_VPCS,
               "allowAllServiceAgentAccess": ALLOW_ALL_SERVICE_AGENT_ACCESS
           }
         }

Where:

     * `MODE` is the state of the IP filter configuration. Valid values are `Enabled` and `Disabled`. When set to `Enabled`, IP filtering rules are applied to a bucket and all incoming requests to the bucket are evaluated against these rules. When set to `Disabled`, all incoming requests can access the bucket and its data without any evaluation.

     * `RANGE_CIDR` is a public network IPv4 or IPv6 address range that's allowed to access the bucket. You can enter one or multiple address ranges as a list.

     * `PROJECT_ID` is the project ID where the VPC network exists. To configure multiple VPC networks, you need to specify the project where each network is located.

     * `NETWORK_NAME` is the name of the VPC network that is allowed to access the bucket. To configure multiple VPC networks, you need to specify a name for each network.

     * `ALLOW_ALL_SERVICE_AGENT_ACCESS` is a boolean value that indicates whether to allow [service agents](https://docs.cloud.google.com/iam/docs/service-agents) to access the bucket, regardless of the IP filter configuration. If the value is `true`, other Google Cloud services can use service agents to access the bucket without IP-based validation.

     * `ALLOW_CROSS_ORG_VPCS` is a boolean value that indicates whether to allow VPC networks that are defined in the `vpcNetworkSources` list to originate from a different organization. This field is optional. If set to `true`, the request allows cross-organizational VPC networks. If set to `false`, the request restricts the VPC networks to the same organization as the bucket. If not specified, the default value is `false`. This field applies only if `vpcNetworkSources` is not empty.

  3. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [PATCH bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/patch) request:
         
         curl -X PATCH --data-binary @JSON_FILE_NAME \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME?project=PROJECT_ID"

Where:

     * `JSON_FILE_NAME` is the name of the JSON file you created.
     * `BUCKET_NAME` is the name of your bucket.
     * `PROJECT_ID` is the ID of the project with which your bucket is associated. For example, `my-project`.



## Manage Google Cloud service agent access

To update the service agent access after you configure IP filtering rules on your bucket, complete the following steps:

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket you want to update.

  3. On the **Bucket details** page, click the **Configuration** tab.

  4. In the **Permissions** section, navigate to **IP filtering**. Then, click edit **Edit IP filtering configuration**.

The **IP filtering** page appears.

  5. In the **Manage Google Cloud service agent access** section, do one of the following:

     * To allow service agent access, complete the following steps:

       1. Click circle **Disabled** to change the setting to check_circle **Enabled**.

       2. To confirm that you want to allow access, type `Enable` in the **Enable** field.

     * To deny service agent access, complete the following steps:

       1. Click check_circle **Enabled** to change the setting to circle **Disabled**.

       2. To confirm that you want to deny access, type `Disable` in the **Disable** field.

A notification message confirms the change.




### gcloud

To update service agent access for your bucket, use the `gcloud storage buckets update` command and set the `allowAllServiceAgentAccess` field to either `true` to allow access or `false` to deny access. For detailed instructions, see [Create or update IP filtering rules on an existing bucket](https://docs.cloud.google.com/storage/docs/update-ip-filter#gcloud).

### JSON API

To update service agent access, you can use a `PATCH` request to update the `ipFilter` configuration for the bucket. Set the `allowAllServiceAgentAccess` field to `true` to allow access or `false` to deny access. For detailed instructions, see [Create or update IP filtering rules on an existing bucket](https://docs.cloud.google.com/storage/docs/update-ip-filter#json-api).

## Manage cross-organization VPC access

To update the cross-organization VPC access after you configure IP filtering rules on your bucket, complete the following steps:

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket you want to update.

  3. On the **Bucket details** page, click the **Configuration** tab.

  4. In the **Permissions** section, navigate to **IP filtering**. Then, click edit **Edit IP filtering configuration**.

The **IP filtering** page appears.

  5. In the **Manage cross-organization VPC access** section, do one of the following:

     * To allow cross-organization VPC access, complete the following steps:

       1. Click circle **Disabled** to change the setting to check_circle **Enabled**.

       2. To confirm that you want to allow access, type `Enable` in the **Enable** field.

     * To deny cross-organization VPC access, complete the following steps:

       1. Click check_circle **Enabled** to change the setting to circle **Disabled**.

       2. To confirm that you want to deny access, type `Disable` in the **Disable** field.

A notification message confirms the change.




### gcloud

To update cross-organization VPC access for your bucket, use the `gcloud storage buckets update` command and set the `allowCrossOrgVpcs` field to either `true` to allow access or `false` to deny access. For detailed instructions, see [Create or update IP filtering rules on an existing bucket](https://docs.cloud.google.com/storage/docs/update-ip-filter#gcloud).

### JSON API

To update cross-organization VPC access, you can use a `PATCH` request to update the `ipFilter` configuration for the bucket. Set the `allowCrossOrgVpcs` field to `true` to allow access or `false` to deny access. For detailed instructions, see [Create or update IP filtering rules on an existing bucket](https://docs.cloud.google.com/storage/docs/update-ip-filter#json-api).

## What's next

  * [List bucket IP filtering rules](https://docs.cloud.google.com/storage/docs/list-ip-filter).
  * [Disable bucket IP filtering rules](https://docs.cloud.google.com/storage/docs/disable-ip-filtering).



##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how Cloud Storage performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try Cloud Storage free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
