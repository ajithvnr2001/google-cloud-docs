---
url: https://docs.cloud.google.com/storage/docs/create-ip-filter/
title: Create a bucket with IP filtering rules \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:09.053244+00:00
---

# Create a bucket with IP filtering rules  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/create-ip-filter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Create a bucket with IP filtering rules Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create a bucket with IP filtering rules. By creating a bucket with IP filtering, you can control access to your buckets by examining incoming requests against the IP addresses specified in the bucket IP filtering rules. For details, see [Bucket IP filtering](https://docs.cloud.google.com/storage/docs/ip-filtering-overview).

**Caution:** It's crucial to set up your IP filtering rules accurately. Incorrectly configured rules can prevent legitimate users from reaching your bucket or even lock you out completely. If you find yourself locked out of your bucket, you can bypass the bucket IP filtering rules to regain access. For details, see [Bypass bucket IP filtering rules](https://docs.cloud.google.com/storage/docs/bypass-ip-filter).

For information about how to create or update the IP filtering rules on an existing bucket, see [Update bucket IP filtering rules](https://docs.cloud.google.com/storage/docs/update-ip-filter).

## Required roles

To get the required permissions for creating a bucket with IP filtering rules, ask your administrator to grant you the Storage Admin (`roles/storage.admin`) role on the bucket. This role contains the permissions required to create a bucket with IP filtering rules.

To see the exact permissions that are required, expand the **Required permissions** section:

#### Required permissions

  * `storage.buckets.create`
  * `storage.buckets.setIpFilter`



You can also get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles). You might be able to get these permissions with other predefined roles as well. To see which roles are associated with which permissions, refer to [IAM roles for Cloud Storage](https://docs.cloud.google.com/iam/docs/understanding-roles).

For instructions on granting roles on buckets, see [Set and manage IAM policies on buckets](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).

## Create bucket with IP filtering rules

**Note:** When you use IP filtering with gRPC direct path, you must enable [IPv6 support](https://docs.cloud.google.com/vpc/docs/ipv6-support) on the VPC network.**Caution:** When configuring IP-based access controls for Cloud Storage buckets, evaluate your Google Cloud architecture. Google Cloud services, such as [Managed Service for Apache Airflow](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview), might operate within separate, Google-managed projects that have their own VPC networks. To experience uninterrupted service, you must identify and allowlist the IP ranges from the associated VPC networks in your bucket's filter configuration. Failure to do so might result in the services being blocked from accessing your bucket. For complex Google Cloud architectures, we recommend consulting your account team for assistance in mapping all necessary IP address ranges.

###  Console 

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Click add_box **Create**.
  3. On the **Create a bucket** page, enter your bucket information. After each of the following steps, click **Continue** to proceed to the next step:

     1. In the **Get started** section, do the following:

        * Enter a globally unique name that meets the [bucket name requirements](https://docs.cloud.google.com/storage/docs/buckets#naming).

        * To add a [bucket label](https://docs.cloud.google.com/storage/docs/tags-and-labels#bucket-labels), click the expand_more expander arrow to expand the **Labels** section, click _add_box_ **Add label** , and specify a `key` and a `value` for your label.

     2. In the **Choose where to store your data** section, do the following:

        1. Select a [Location type](https://docs.cloud.google.com/storage/docs/locations).

        2. Use the location type's drop-down menu to select a [**Location**](https://docs.cloud.google.com/storage/docs/locations#available-locations) where object data within your bucket will be permanently stored.

           * If you select the [dual-region](https://docs.cloud.google.com/storage/docs/locations#location-dr) location type, you can also choose to enable [turbo replication](https://docs.cloud.google.com/storage/docs/availability-durability#turbo-replication) by using the relevant checkbox.

        3. To set up [cross-bucket replication](https://docs.cloud.google.com/storage/docs/availability-durability#cross-bucket-replication), select **Add cross-bucket replication via Storage Transfer Service** and follow the steps:

#### Set up cross-bucket replication

           1. In the **Bucket** menu, select a bucket.
           2. In the **Replication settings** section, click **Configure** to configure settings for the replication job.

The **Configure cross-bucket replication** pane appears.

              * To filter objects to replicate by object name prefix, enter a prefix with which you want to include or exclude objects, then click add **Add a prefix**.
              * To set a storage class for the replicated objects, select a storage class from the **Storage class** menu. If you skip this step, the replicated objects will use the destination bucket's storage class by default.
              * Click **Done**.

     3. In the **Choose how to store your data** section, do the following:

        1. Select a [default storage class](https://docs.cloud.google.com/storage/docs/storage-classes) for the bucket or [Autoclass](https://docs.cloud.google.com/storage/docs/autoclass) for automatic storage class management of your bucket's data.

        2. In the **Optimize storage for data-intensive workloads** section, do the following:

           * To enable [hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview), select **Enable Hierarchical namespace on this bucket**.

**Note:** Hierarchical namespace can only be enabled when you create the bucket. You can't change this setting after you create the bucket.

           * To enable [Rapid Cache](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache), select **Enable Rapid Cache** and follow the steps: 
             1. To create caches, click **Configure**.

             2. In the **Configure cache settings** dialog that appears, click the drop-down arrow next to the listed regions and select the zones where you want to create caches.

             3. Click **Done**.

**Note:** [Additional permissions](https://docs.cloud.google.com/storage/docs/rapid/use-rapid-cache#before-you-begin) are required to enable Rapid Cache.

     4. In the **Choose how to control access to objects** section, do the following:

        1. Select whether your bucket enforces [public access prevention](https://docs.cloud.google.com/storage/docs/public-access-prevention).

**Note:** If public access prevention is already enforced by your project's [organization policy](https://docs.cloud.google.com/storage/docs/org-policy-constraints#public-access-prevention), the **Prevent public access** checkbox is locked. 
        2. Select **Uniform** to enable uniform bucket-level access on the bucket.

        3. To configure [IP filtering for the bucket](https://docs.cloud.google.com/storage/docs/ip-filtering-overview), do the following:

           1. In the **IP filtering** section, click add_box **Configure**.

           2. To allow access from public IP addresses, do the following:

              1. Click **Public internet**.
              2. In the **Allowed IP range(s)** field, specify one or more IPv4 address ranges or IPv6 CIDR ranges to allow. For example, `192.0.2.0/24` or `2001:db8::/32`.

To avoid being locked out of your bucket, include your own IP address.

           3. To allow access from VPC networks, do the following:

              1. Click **VPC network(s)**.
              2. Do the following for each network:

                 1. Click **Add VPC network**.
                 2. In the **New VPC network** section, specify the following information:

                    * In the **Project ID** field, enter your project ID.
                    * In the **Network name** field, enter your network name.
                    * In the **Allowed IP range(s)** field, enter one or more IPv4 or IPv6 CIDR ranges, such as `192.0.2.0/24` or `2001:db8::/32`.

To avoid being locked out of your bucket, include your own IP address.

                 3. Click **Done**.
           4. To permit trusted Google Cloud service agents and VPC networks from other organizations to bypass your IP filtering configuration, do the following:

              1. Click **Additional settings**.
              2. In the **Google Cloud service agent access** section, select one of the following options:

                 * **Allow service agent access** : enables Google Cloud services such as BigLake, Storage Insights, Vertex AI, and BigQuery to bypass the IP filtering validation when they need to access this bucket.
                 * **Deny service agent access** : enforces the IP filter rules for Google Cloud service agents.
              3. In the **Cross-organization VPC access** section, do one of the following: 
                 * To permit access from specified VPC networks located in different Google Cloud organizations, click the toggle to the **Allow** position.
                 * To block access from VPC networks outside of your Google Cloud organization, click the toggle to **Deny** (default state) position.
           5. Click **Review** , and then click **Save**.
  4. In the **Choose how to protect object data** section, do the following:

     * Select any of the options under **Data protection** that you want to set for your bucket.

     * To change the amount of time that [soft delete](https://docs.cloud.google.com/storage/docs/soft-delete) retains objects after deletion, select the **Soft delete policy** checkbox, and then select the **Set custom retention duration** option. Then, specify how long you want to retain deleted objects.

To disable soft delete, for example if the bucket will primarily contain short-lived, temporary data, clear the **Soft delete policy** checkbox. 

     * To choose how to [encrypt](https://docs.cloud.google.com/storage/docs/encryption) your object data, click the expand_more expander arrow labeled **Data encryption** , and do the following:

       * In the **Default encryption key type** section, select the default encryption key for the bucket. If you select **Cloud KMS key** , then provide a [Cloud Key Management Service key](https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys).
       * In the **Encryption enforcement rules** section, for **Key types** , select [which encryption types to allow or restrict](https://docs.cloud.google.com/storage/docs/encryption/enforce-encryption-types) for new objects in the bucket.


* Click **Create**.

### gcloud

  1. Verify that you have the Google Cloud CLI version 526.0.0 or later installed:
         
         gcloud version | head -n1
         

  2. If you have an earlier gcloud CLI version installed, update the version:
         
         gcloud components update --version=526.0.0
         

  3. Create a JSON file that defines the rules for incoming requests. For examples and information about how to structure the bucket IP filtering rules, see Bucket IP filtering configurations.
         
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
           "allowCrossOrgVpcs":ALLOW_CROSS_ORG_VPCS,
           "allowAllServiceAgentAccess": ALLOW_ALL_SERVICE_AGENT_ACCESS
         }

Where:

     * `MODE` is the mode of the bucket IP filtering configuration. Valid values are `Enabled` and `Disabled`. When set to `Enabled`, IP filtering rules are applied to a bucket. Any incoming request to the bucket is evaluated against these rules. When set to `Disabled`, all incoming requests are allowed to access the bucket.

**Note:** To safely enable bucket IP filtering rules, start by configuring your rules with the `mode` field set to `Disabled` so that you can add and adjust rules without immediately blocking requests. After you've verified that your rules are correctly defined, update the `mode` field to `Enabled` to activate bucket IP filtering.
     * `RANGE_CIDR` is a public network IPv4 or IPv6 address range that's allowed to access the bucket. You can enter one or multiple address ranges as a list.

     * `PROJECT_ID` is the project ID where the Virtual Private Cloud (VPC) network exists. To configure multiple VPC networks, you need to specify the project where each network is located.

     * `NETWORK_NAME` is the name of the VPC network that is allowed to access the bucket. To configure multiple VPC networks, you need to specify a name for each network.

     * `ALLOW_CROSS_ORG_VPCS` is a boolean value that indicates whether to allow VPC networks that are defined in `vpcNetworkSources` to originate from a different organization. This field is optional. If set to `true`, the request allows cross-organizational VPC networks. If set to `false`, the request restricts the VPC networks to the same organization as the bucket. If not specified, the default value is `false`. This field applies only if `vpcNetworkSources` is not empty.

     * `ALLOW_ALL_SERVICE_AGENT_ACCESS` is a boolean value that indicates whether to allow [service agents](https://docs.cloud.google.com/iam/docs/service-agents) to access the bucket, regardless of the IP filter configuration. If the value is `true`, other Google Cloud services can use service agents to access the bucket without IP-based validation.

  4. To create a bucket with IP filtering rules, run the [`gcloud storage buckets create`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/create) command in your development environment:
         
         gcloud storage buckets create gs://BUCKET_NAME --ip-filter-file=IP_FILTER_CONFIG_FILE

Where:

     * `BUCKET_NAME` is the name you want to give your bucket, subject to [naming requirements](https://docs.cloud.google.com/storage/docs/buckets#naming). For example, `my-bucket`.
     * `IP_FILTER_CONFIG_FILE` is the JSON file that defines the rules for incoming requests.



### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create a JSON file that contains the settings for the bucket, which must include the `name` and `ipFilter` configuration fields for the bucket. For examples and information about how to structure the bucket IP filtering rules, see Bucket IP filtering configurations.
         
         {
           "name": "BUCKET_NAME",
           "ipFilter": {
             "mode": "MODE",
             "publicNetworkSource":
               {
                 "allowedIpCidrRanges":
                   [RANGE_CIDR,
                     ...
                   ]
               },
             "vpcNetworkSources":
               [
                 {"network": "projects/PROJECT_ID/global/networks/NETWORK_NAME",
                 "allowedIpCidrRanges":
                   [RANGE_CIDR,
                   ...
                   ]
                 },
               ...
               ],
             "allowCrossOrgVpcs": ALLOW_CROSS_ORG_VPCS,
             "allowAllServiceAgentAccess": ALLOW_ALL_SERVICE_AGENT_ACCESS
             },
         }

Where:

     * `MODE` is the state of the IP filter configuration. Valid values are `Enabled` and `Disabled`. When set to `Enabled`, IP filtering rules are applied to a bucket and all incoming requests to the bucket are evaluated against these rules. When set to `Disabled`, all incoming requests can access the bucket and its data without any evaluation if you have the required IAM permissions.

**Note:** To safely enable bucket IP filtering rules, start by configuring your rules with the `mode` field set to `Disabled` so that you can add and adjust rules without immediately blocking requests. After you've verified that your rules are correctly defined, update the `mode` field to `Enabled` to activate bucket IP filtering.
     * `RANGE_CIDR` is a public network IPv4 or IPv6 address range that's allowed to access the bucket. You can enter one or multiple address ranges as a list.

     * `PROJECT_ID` is the project ID where the VPC network exists. To configure multiple VPC networks, you need to specify the project where each network is located.

     * `NETWORK_NAME` is the name of the VPC network that is allowed to access the bucket. To configure multiple VPC networks, you need to specify a name for each network.

     * `ALLOW_ALL_SERVICE_AGENT_ACCESS` is a boolean value that indicates whether to allow [service agents](https://docs.cloud.google.com/iam/docs/service-agents) to access the bucket, regardless of the IP filter configuration. If the value is `true`, other Google Cloud services can use service agents to access the bucket without IP-based validation.

     * `ALLOW_CROSS_ORG_VPCS` is a boolean value that indicates whether to allow VPC networks that are defined in `vpcNetworkSources` to originate from a different organization. This field is optional. If set to `true`, the request allows cross-organizational VPC networks. If set to `false`, the request restricts the VPC networks to the same organization as the bucket. If not specified, the default value is `false`. This field applies only if `vpcNetworkSources` is not empty.

  3. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [POST bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/insert) request:
         
         curl -X POST --data-binary @JSON_FILE_NAME \
          -H "Authorization: Bearer $(gcloud auth print-access-token)" \
          -H "Content-Type: application/json" \
          "https://storage.googleapis.com/storage/v1/b?project=PROJECT_ID"

Where:

     * `JSON_FILE_NAME` is name of the JSON file that contains the settings for the bucket.
     * `PROJECT_ID` is the ID of the project with which your bucket is associated. For example, `my-project`.



### Bucket IP filtering configurations

This section provides examples of bucket IP filtering JSON file configurations to control access to your Cloud Storage buckets. You can grant access to incoming requests using _any_ of the following examples:

  * **Any public IP address (IPv4 or IPv6)** :

The following configuration grants access to any public IPv4 or IPv6 address, but blocks traffic originating from any VPC:

### gcloud
        
        {
          "mode": "Enabled",
          "publicNetworkSource": {
            "allowedIpCidrRanges": ["0.0.0.0/0", "::/0"]
          },
          "allowAllServiceAgentAccess": false
        }

### JSON API
        
        {
          "name": "my-bucket",
          "ipFilter": {
            "mode": "Enabled",
            "publicNetworkSource": {
              "allowedIpCidrRanges": ["0.0.0.0/0", "::/0"]
            },
            "allowAllServiceAgentAccess": false
          }
        }

  * **Specific public IP ranges** :

    * The following example configuration grants access to `192.0.2.0/24` public IPv4 address range, but blocks traffic originating from any VPC:

### gcloud
          
          {
            "mode": "Enabled",
            "publicNetworkSource": {
              "allowedIpCidrRanges": ["192.0.2.0/24"]
            },
            "allowAllServiceAgentAccess": false
          }

### JSON API
          
          {
            "name": "my-bucket",
            "ipFilter": {
              "mode": "Enabled",
              "publicNetworkSource": {
                "allowedIpCidrRanges": ["192.0.2.0/24"]
              },
              "allowAllServiceAgentAccess": false
            }
          }

    * The following example configuration grants access to `2001:db8::/32` public IPv6 address range, but blocks traffic originating from any VPC:

### gcloud
          
          {
            "mode": "Enabled",
            "publicNetworkSource": {
              "allowedIpCidrRanges": ["2001:db8::/32"]
            },
            "allowAllServiceAgentAccess": false
          }

### JSON API
          
          {
            "name": "my-bucket",
            "ipFilter": {
              "mode": "Enabled",
              "publicNetworkSource": {
                "allowedIpCidrRanges": ["2001:db8::/32"]
              },
              "allowAllServiceAgentAccess": false
            }
          }

  * **VPC networks** : Using the following configurations, you can grant access to resources within your VPC network. You can grant access to all IP addresses within the VPC or specific IP ranges within the VPC. In each of these examples, `PROJECT_ID` is the project ID where the VPC network exists and `NETWORK_NAME` is the name of the VPC network that is allowed to access the bucket.

    * The following example configuration grants access to a request from any IPv4 or IPv6 address coming from a specific VPC and blocks traffic originating from a public IP address:

### gcloud
          
          {
            "mode": "Enabled",
            "vpcNetworkSources": [
              {
                "network": "projects/PROJECT_ID/global/networks/NETWORK_NAME",
                "allowedIpCidrRanges": ["0.0.0.0/0", "::/0"]
              },
            ],
            "allowAllServiceAgentAccess": false
          }

### JSON API
          
          {
            "name": "my-bucket",
            "ipFilter": {
              "mode": "Enabled",
              "vpcNetworkSources": [
                {
                  "network": "projects/PROJECT_ID/global/networks/NETWORK_NAME",
                  "allowedIpCidrRanges": ["0.0.0.0/0", "::/0"]
                },
              ],
              "allowAllServiceAgentAccess": false
            }
          }

    * The following example configuration only grants access to a request from a VPC associated to a VM with an external IPv4 address as `192.0.2.0/24` and blocks traffic originating from a public IP address:

### gcloud
          
          {
            "mode": "Enabled",
            "vpcNetworkSources": [
              {
                "network": "projects/PROJECT_ID/global/networks/NETWORK_NAME",
                "allowedIpCidrRanges": ["192.0.2.0/24"]
              },
            ],
            "allowAllServiceAgentAccess": false
          }

### JSON API
          
          {
            "name": "my-bucket",
            "ipFilter": {
              "mode": "Enabled",
              "vpcNetworkSources": [
                {
                  "network": "projects/PROJECT_ID/global/networks/NETWORK_NAME",
                  "allowedIpCidrRanges": ["192.0.2.0/24"]
                },
              ],
              "allowAllServiceAgentAccess": false
            }
          }

    * The following example configuration only grants access to a request coming from a VPC with an internal IPv4 subnet range associated to a VM with no external IP address and blocks traffic originating from a public IP address:

### gcloud
          
          {
            "mode": "Enabled",
            "vpcNetworkSources": [
              {
                "network": "projects/PROJECT_ID/global/networks/NETWORK_NAME",
                "allowedIpCidrRanges": ["IP_ADDRESS"]
              },
            ],
            "allowAllServiceAgentAccess": false
          }

Where:

`IP_ADDRESS` is an [internal IPv4 subnet range](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges).

### JSON API
          
          {
            "name": "my-bucket",
            "ipFilter": {
              "mode": "Enabled",
              "vpcNetworkSources": [
                {
                "network": "projects/PROJECT_ID/global/networks/NETWORK_NAME",
                "allowedIpCidrRanges": ["IP_ADDRESS"]
                },
              ],
              "allowAllServiceAgentAccess": false
            }
          }

Where:

`IP_ADDRESS` is an [internal IPv4 subnet range](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges).

    * The following example configuration only grants access to a request coming from a VPC with dual-stack IPv4 and IPv6 subnet range associated to a VM with an external IPv6 address range as `2001:db8::/32` and blocks traffic originating from a public IP address:

### gcloud
          
          {
            "mode": "Enabled",
            "vpcNetworkSources": [
              {
                "network": "projects/PROJECT_ID/global/networks/NETWORK_NAME",
                "allowedIpCidrRanges": ["2001:db8::/32"]
              },
            ],
            "allowAllServiceAgentAccess": false
          }

### JSON API
          
          {
            "name": "my-bucket",
            "ipFilter": {
              "mode": "Enabled",
              "vpcNetworkSources": [
                {
                  "network": "projects/PROJECT_ID/global/networks/NETWORK_NAME",
                  "allowedIpCidrRanges": ["2001:db8::/32"]
                },
              ],
              "allowAllServiceAgentAccess": false
            }
          }




## What's next

  * [Create or update IP filtering rules on an existing bucket](https://docs.cloud.google.com/storage/docs/update-ip-filter).
  * [Get bucket IP filtering rules](https://docs.cloud.google.com/storage/docs/get-ip-filter).
  * [List bucket IP filtering rules](https://docs.cloud.google.com/storage/docs/list-ip-filter).
  * [Disable bucket IP filtering](https://docs.cloud.google.com/storage/docs/disable-ip-filtering).



##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how Cloud Storage performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try Cloud Storage free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
