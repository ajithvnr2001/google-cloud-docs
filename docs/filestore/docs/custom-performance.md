---
url: https://docs.cloud.google.com/filestore/docs/custom-performance/
title: Custom performance \u00a0|\u00a0 Filestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:01:05.957540+00:00
---

# Custom performance  |  Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/custom-performance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Custom performance Stay organized with collections  Save and categorize content based on your preferences. 

Custom performance lets you define the performance settings for your Filestore instances independently of the specified capacity. This means you can optimize your Filestore instances for your workload requirements and scale your file shares to meet the demands of your applications without resizing the capacity.

If you use Google Cloud console to create Filestore zonal and regional instances, custom performance is the default mechanism for configuring performance.

## Read and write IOPS

You can use 100% of IOPS purchased for your file system for read and write operations combined. Read and write operations have different weights, with each read operation takes one operation from the purchased IOPS, while write operation takes 3.33 IOPS from the purchased IOPS. 

For example, if your file system uses 33% of its purchased IOPS for read operations, it can simultaneously use up to 67% of its purchased IOPS for write operations, utilizing the purchased IOPS according to the 3.33 ratio per write.

Custom performance supports up to 100 client connections per 1,000 purchased IOPS, regardless of the capacity range or service tier being regional or zonal.

IOPS accrued from replicated data, such as [backup](https://docs.cloud.google.com/filestore/docs/backups) operations, don't count towards user-purchased IOPS.

### Example IOPS calculation

Assuming you have purchased 4,000 IOPS:

  * If you want to use them for read IOPS, you would have access to a maximum of 4,000 read IOPS.
  * If you want to use them for write IOPS, you would have access to a maximum of 1,200 write IOPS.
  * If you want to use 900 IOPS for write operations, it will effectively use 3,000 of your IOPS budget, leaving 1,000 IOPS for read operations.



If you need more IOPS or throughput, you can increase your purchased IOPS rate.

## Configure custom performance

You can set custom performance for zonal and regional instances that already support it. Basic tiers don't support this feature.

Custom performance instances are billed differently than instances where custom performance is not configured. For details, see [Filestore pricing](https://cloud.google.com/filestore/pricing).

You have the following options to configure custom performance:

  * Set an IOPS per TiB ratio where IOPS scale linearly with the instance's size.
  * Set a fixed IOPS rate. The rate is steady, regardless of instance size.



When creating an instance in the Google Cloud console, custom performance is enabled by default, letting you configure performance based on your workload and scale. If you don't provide specific IOPS values, a recommended default rate is used. You can opt out of custom performance, but you must do it before you create the instance, as the setting is permanent and can't be changed later.

For more information about setting custom performance, see [creating instances](https://docs.cloud.google.com/filestore/docs/creating-instances#configure-performance).

For more information about custom performance in GKE, see [Filestore CSI Driver](https://docs.cloud.google.com/filestore/docs/csi-driver#custom-performance).

### Check custom performance status

If you want to check the custom performance status, follow these instructions:

###  Google Cloud console 

  1. In the Google Cloud console, go to the **Instances** page.

[Go to Instances](https://console.cloud.google.com/filestore/instances)

  2. Click the **Instance ID** to open the **Instance Details** page.

  3. Go to the **Overview** tab and look for a **Custom Performance** entry.

     * **Not supported** means that custom performance is not supported for a specific instance. For example, when you create a basic tier instance, or when the instance was created before the feature was launched.
     * **Enabled** means that custom performance is supported and active for this instance.
     * **Disabled** means that custom performance is supported but not enabled for this instance.



###  gcloud 

Get information about a Filestore instance by running the [`instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/filestore/instances/describe) command:
    
    
        gcloud filestore instances describe INSTANCE_ID --project=PROJECT_ID --location=LOCATION
    

The output might vary depending on the instance settings. The following is an example output:
    
    
        createTime: '2021-10-11T17:28:23.340943077Z'
        customPerformanceSupported: true
        fileShares:
        - capacityGb: '1024'
        name: vol1
        kmsKeyName: projects/example-project/locations/us-central1/keyRings/example-ring/cryptoKeys/example-key
        labels:
        key:val
        name: projects/yourproject/locations/us-central1/instances/nfs-server
        networks:
        - ipAddresses:
        - 10.0.0.2
        network: default
        reservedIpRange: 10.0.0.0/26
        performanceConfig:
          iopsPerTb:
            maxIopsPerTb: '17000'
        performanceLimits:
          maxIops: '17000'
          maxReadIops: '17000'
          maxReadThroughputBps: '417792000'
          maxWriteIops: '5100'
          maxWriteThroughputBps: '139264000'
        state: READY
        tier: REGIONAL
    

  * If `customPerformanceSupported` parameter is present and set to `true` it means that custom performance is supported for this instance. If the flag is not present, custom performance is not supported. 

  * If `performanceConfig` parameter is present, it means that custom performance is enabled for this instance.




###  REST API 

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [Filestore API](https://docs.cloud.google.com/filestore/docs/reference/rest/v1/projects.locations.instances/get):
         
         curl -s \
           --header "Authorization: Bearer $(gcloud auth print-access-token)" \
           --header "Content-Type: application/json" \
           GET "https://file.googleapis.com/v1beta1/projects/PROJECT/locations/LOCATION/instances/INSTANCE_NAME"

Where:

     * `PROJECT` is the name of the project where your instance is located. For example, `my-project`.
     * `LOCATION` is the location where your instance resides. For example, `us-central1-a`.
     * `INSTANCE_NAME` is the name of the instance you want to view. For example, `nfs-server`.

If custom performance is supported and configured for the provided instance, the response will include the following parameters:
    
    "customPerformanceSupported": true,
      "performanceConfig": {
        "fixedIops": {
          "maxIops": "9000"
        }
      },
      "performanceLimits": {
        "maxReadIops": "9000",
        "maxWriteIops": "2700",
        "maxReadThroughputBps": "221184000",
        "maxWriteThroughputBps": "73728000",
        "maxIops": "9000"
      }
    




## Custom performance calculations

The following table displays performance calculations based on provisioned IOPS per TiB and allocated capacity. The calculations are based on different capacity ranges to show how the values for read IOPS, write IOPS, read throughput, and write throughput change for the minimum and maximum IOPS per TiB values. 

For more information, see the [read and write IOPS](https://docs.cloud.google.com/filestore/docs/custom-performance#iops) section of this document.

Custom performance examples for the regional tier Provisioned IOPS per TiB | Capacity (GiB) | Read IOPS | Write IOPS | Read throughput (MiBps) | Write throughput (MiBps)  
---|---|---|---|---|---  
4,000 | 100 | 2,000 | 600 | 47 | 16  
600 | 2,344 | 703 | 55 | 19  
1,024 | 4,000 | 1,200 | 94 | 32  
10,239 | 39,996 | 11,999 | 940 | 320  
17,000 | 100 | 2,000 | 600 | 47 | 16  
600 | 9,961 | 2,988 | 234 | 80  
1,024 | 17,000 | 5,100 | 400 | 136  
10,239 | 169,983 | 50,995 | 3,995 | 1,360  
  
For details about performance limits when custom performance is not activated, see [performance limits](https://docs.cloud.google.com/filestore/docs/performance).

## Monitoring

To monitor instance IOPS usage, you can use the **Metrics Explorer** to view the following metrics: `read_ops_count`, `write_ops_count`, and `metadata_ops_count`.

For more information, see [monitoring instances](https://docs.cloud.google.com/filestore/docs/monitoring-instances).

## What's next

  * Learn more about [Filestore performance](https://docs.cloud.google.com/filestore/docs/performance)
  * [Test performance](https://docs.cloud.google.com/filestore/docs/testing-performance)
  * [Troubleshoot performance-related issues](https://docs.cloud.google.com/filestore/docs/troubleshooting)
  * [Scale capacity](https://docs.cloud.google.com/filestore/docs/scale)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
