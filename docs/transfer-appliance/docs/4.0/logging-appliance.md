---
url: https://docs.cloud.google.com/transfer-appliance/docs/4.0/logging-appliance/
title: Logging \u00a0|\u00a0 Transfer Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:16.670229+00:00
---

# Logging  |  Transfer Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/transfer-appliance/docs/4.0/logging-appliance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Transfer Appliance ](https://docs.cloud.google.com/transfer-appliance/docs)
  * [ Guides ](https://docs.cloud.google.com/transfer-appliance/docs/4.0/procedure-guide)



Send feedback 

#  Logging Stay organized with collections  Save and categorize content based on your preferences. 

## Enable Logging

Transfer Appliance uses logging to export certain system logs generated on the appliance to Google Cloud Observability making it easier to access them.

The steps to enable logging depend on whether you've set up [online transfer](https://docs.cloud.google.com/transfer-appliance/docs/4.0/online-transfer):

  * If you've [set up online transfer](https://docs.cloud.google.com/transfer-appliance/docs/4.0/prepare-online), and granted the `Logging Log Writer` role to the service account, no further configuration is required.

  * If you've set up online transfer, but didn't add the `Logging Log Writer` role, [add the role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#granting-console) to your user-managed service account at the project level. No need to regenerate the service account key after adding or changing roles.

  * If you haven't set up online transfer, follow the instructions to [create and configure a user-managed service account](https://docs.cloud.google.com/transfer-appliance/docs/4.0/prepare-online#user_sa). Only the `Logging Log Writer` role is required for logging.




Once you've completed the required steps:

  1. [Connect to the appliance](https://docs.cloud.google.com/transfer-appliance/docs/4.0/receive-appliance#connecting).
  2. Start reporting logs from the appliance



`ta logging start`

## Disable logging on the appliance

To stop reporting logs from the appliance run the following command from the Transfer Appliance command line:

`ta logging stop`

## View logs

To query for logs, you can use the `label.sessionID` field in the Google Cloud's Google Cloud Observability.
    
    
    labels.sessionID={sessionID}
    

The following are some of the logs that are exported:

  * Fluent Bit

  * Docker

  * Kernel

  * Metadata partition

    * capture

    * ta_check

    * activation_service




You can view the logs in Cloud Logging by using the Google Cloud console, the Google Cloud CLI, or the Logging API.

## Troubleshooting

`An error occurred while enabling logging`

If the service account key file `/tmp/key.json` is not found on the appliance, an error is returned.

Refer to [Create and configure a user-managed service account](https://docs.cloud.google.com/transfer-appliance/docs/4.0/prepare-online#user_sa) for instructions on configuring a service account and copying the key file to your appliance.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
