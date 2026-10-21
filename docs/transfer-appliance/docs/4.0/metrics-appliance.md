---
url: https://docs.cloud.google.com/transfer-appliance/docs/4.0/metrics-appliance/
title: Monitor Transfer Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:16.100648+00:00
---

# Monitor Transfer Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/transfer-appliance/docs/4.0/metrics-appliance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Transfer Appliance ](https://docs.cloud.google.com/transfer-appliance/docs)
  * [ Guides ](https://docs.cloud.google.com/transfer-appliance/docs/4.0/procedure-guide)



Send feedback 

#  Monitor Transfer Appliance Stay organized with collections  Save and categorize content based on your preferences. 

You can use the data copy status and appliance status metrics for better observability.

## Monitor online copy status

If you've enabled [online transfer](https://docs.cloud.google.com/transfer-appliance/docs/4.0/online-transfer), you can monitor the progress of online transfers from Transfer Appliance to Cloud Storage in the **Transfer Appliance** page of the Google Cloud console.

[Go to Transfer Appliance | Monitor](https://console.cloud.google.com/transfer/jobs)

## Monitor offline copy status

While you're transferring data, you can monitor the progress of your transfer.

To monitor the progress of Transfer Appliance, [connect to the appliance](https://docs.cloud.google.com/transfer-appliance/docs/4.0/receive-appliance#connecting) and run the following command:
    
    
    ta status --verbose
    

## Enable Cloud Monitoring

Transfer Appliance uses Cloud Monitoring to report on a wide range of appliance metrics.

**Note:** The metrics are exported to the project in which the credential file `key.json` is created [in this section](https://docs.cloud.google.com/transfer-appliance/docs/4.0/prepare-online#prepare-service-account-key). This uses quota and may incur charges, depending on the usage.

The steps to enable Cloud Monitoring depend on whether you've set up [online transfer](https://docs.cloud.google.com/transfer-appliance/docs/4.0/online-transfer):

  * If you've [set up online transfer](https://docs.cloud.google.com/transfer-appliance/docs/4.0/prepare-online), and granted the `Monitoring Metric Writer` role to the service account, no further configuration is required.

  * If you've set up online transfer, but didn't add the `Monitoring Metric Writer` role, [add the role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#granting-console) to your user-managed service account at the project level. You do not need to regenerate the service account key after adding or changing roles.

  * If you haven't set up online transfer, follow the instructions to [create and configure a user-managed service account](https://docs.cloud.google.com/transfer-appliance/docs/4.0/prepare-online#create_and_configure_a_user-managed_service_account). Only the `Monitoring Metric Writer` role is required for Cloud Monitoring.




Once you've completed the required steps:

  1. [Connect to the appliance](https://docs.cloud.google.com/transfer-appliance/docs/4.0/receive-appliance#connecting).
  2. Make sure the appliance has been [configured](https://docs.cloud.google.com/transfer-appliance/docs/4.0/receive-appliance#configure-appliance).
  3. From the appliance command line, run `ta metrics start`.



## Supported metrics

Metrics Name | Collect Interval | Supported Appliances | Description  
---|---|---|---  
appliance/storage/stored_bytes | 60s | TA40/TA300 | Reports the current number of bytes stored in the storage buffer of the appliance.  
appliance/network/bytes_received | 60s | TA40/TA300 | Reports the amount of bytes received per interface.  
appliance/network/bytes_sent | 60s | TA40/TA300 | Reports the amount of bytes sent per interface.  
appliance/network/packets_received | 60s | TA40/TA300 | Reports the amount of packets received per interface.  
appliance/network/packets_sent | 60s | TA40/TA300 | Reports the amount of packets sent per interface.  
appliance/disk/partition/used_bytes | 60s | TA40/TA300 | The used space of each disk partition.  
appliance/disk/partition/total_bytes | 60s | TA40/TA300 | The total space of each disk partition.  
appliance/cpu/load_average | 60s | TA40/TA300 | CPU load average over the past sample period.  
appliance/service/state | 60s | TA40/TA300 | Reports the running status of the service.  
appliance/network/connectivity | 60s | TA40/TA300 | Reports if the interface network is reachable.  
appliance/network/dns_health | 60s | TA40/TA300 | Reports if the DNS configuration works well.  
appliance/disk/health | 1h | TA40/TA300 | Reports the health status of each disk.  
appliance/hardware/health | 1h | TA40/TA300 | Reports if the specific hardware component works properly.  
appliance/version | 60s | TA40/TA300 | Current version of the specific appliance component.  
  
## Monitor appliance state

You can monitor the state of the appliance using Cloud Monitoring. See Enable Cloud Monitoring for setup instructions.

  1. Visit the [Metrics explorer](https://console.cloud.google.com/monitoring/metrics-explorer) page in the Google Cloud console.
  2. From the **Metrics** tab, click **Select a metric**.
  3. In the filter field, enter the metrics name, for example, `Stored bytes`.
  4. From the results, select **Transfer Appliance** > **Appliance** > **Stored bytes**.
  5. Click **Apply**.



To learn about using Cloud Monitoring to view your Transfer Appliance metrics, read [Create charts with Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer).

## Disable Cloud Monitoring on the appliance

To stop reporting metrics from the appliance to Cloud Monitoring, run the following command from the Transfer Appliance command line:

`ta metrics stop`

Cloud Monitoring is also stopped when you run any of the following commands:

  * `ta finalize`
  * `ta reset`



## Troubleshooting

### `An error occurred while enabling monitoring`

If the service account key file `/tmp/key.json` is not found on the appliance, an error is returned:

`An error occurred while enabling monitoring: failed to authenticate monitoring: credential file: /tmp/key.json is missing`

Refer to [Create and configure a user-managed service account](https://docs.cloud.google.com/transfer-appliance/docs/4.0/prepare-online#create_and_configure_a_user-managed_service_account) for instructions on configuring a service account and copying the key file to your appliance.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
