---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/macsec/rotate-macsec-keys/
title: Rotate MACsec keys \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:55:16.560114+00:00
---

# Rotate MACsec keys  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/macsec/rotate-macsec-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Rotate MACsec keys Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to rotate keys for MACsec for Cloud Interconnect.

To rotate keys, you complete the following:

  1. Create a new key with a start date after existing keys.
  2. Add the new key to your on-premises router.
  3. Wait for the new key's start time.
  4. Verify that the new key is active.
  5. Delete the oldest key.



You can create up to five pre-shared keys with start times that you specify. The keys' start times must be in increasing order, and not within six hours of the previous key's start time. To rotate a key that you no longer want to use, you remove the key.

Pre-shared keys don't expire. When you configure more than one key, then all keys must have a start time configured.

## Required roles

To get the permissions that you need to retrieve MACsec keys, ask your administrator to grant you the [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

If you choose to use custom roles, ensure that your custom role for administrating MACsec for Cloud Interconnect includes the `compute.interconnects.getMacsecConfig` IAM permission.

## Optional: Update existing key start time

If you have a key without a start time and attempt to create a new key, Cloud Interconnect displays an error. To fix the start time, select one of the following options to set a start time for the existing key:

###  Console 

  1. In the Google Cloud console, go to the Cloud Interconnect **Physical connections** tab.

[Go to Physical connections](https://console.cloud.google.com/hybrid/interconnects/list?tab=interconnects)

  2. Select the connection that you want to modify.

  3. On the **MACsec** tab, go to the **Pre-shared keys** section, and then click **Managed pre-shared keys**.

  4. In the **Start time** field, select or enter a new start time.

  5. Click **Submit**




###  gcloud 
    
    
    gcloud compute interconnects macsec update-key INTERCONNECT_CONNECTION_NAME \
        --key-name=KEY_NAME \
        --start-time=START_TIME
    

Replace the following:

  * `INTERCONNECT_CONNECTION_NAME`: the name of your Cloud Interconnect connection
  * `KEY_NAME`: the name of the key to update
  * `START_TIME`: the time that this key is valid from in ISO 8601 format—for example, `2023-07-01T21:00:01.000Z`



## Create a new key

  1. To add a new key, select one of the following options:

###  Console 

     1. In the Google Cloud console, go to the Cloud Interconnect **Physical connections** tab.

[Go to Physical connections](https://console.cloud.google.com/hybrid/interconnects/list?tab=interconnects)

     2. Select the connection that you want to modify.

     3. On the **MACsec** tab, go to the **Pre-shared keys** section, and then click **Managed pre-shared keys**.

     4. Click **Add key**.

     5. Specify the details of the pre-shared key:

        * **Key Name:** a name for the key. This name is displayed in the Google Cloud console and is used by the gcloud CLI to reference the key, such as `psk-2`.

        * **Start time:** the time that the key is valid from. Ensure that the new pre-shared key's start time is at least six hours after the start time of the previous key.

     6. To add additional pre-shared keys, click **Add key**. Consecutive pre-shared keys must have start times at least six hours apart.

     7. Click **Submit**.

###  gcloud 
    
    gcloud compute interconnects macsec add-key INTERCONNECT_CONNECTION_NAME \
        --key-name=KEY_NAME \
        --start-time="START_TIME"
    

Replace the following:

     * `INTERCONNECT_CONNECTION_NAME`: the name of your Cloud Interconnect connection
     * `KEY_NAME`: a name for the key
     * `START_TIME`: the time that this key is valid from in ISO 8601 format—for example, `2023-07-01T21:00:01.000Z`

As a best practice, we recommend that you set a start time for all keys that you create for MACsec for Cloud Interconnect.

  2. To list existing keys and note the new key's connectivity association key (CAK) and the connectivity association key name (CKN), select one of the following options:

###  Console 

     1. In the **Pre-shared keys** section, find the name of the pre-shared key that you added, then click **View**. A window displays the connectivity association key (**CAK**) and the connectivity association key name (**CKN**). Click content_copy**Copy** next to either value to copy the value to your computer's clipboard.

     2. Click **Close**.

###  gcloud 
    
    gcloud compute interconnects macsec get-config INTERCONNECT_CONNECTION_NAME
    

The output is similar to the following:
    
    preSharedKeys:
    - name: key1
      ckn: 0101010189abcdef...0123456789abcdef
      cak: 0123456789abcdef...0123456789abcdef
      startTime: 2023-07-01T12:12:12Z
    - name: key2
      ckn: 0202020289abcdef...0123456789abcdef
      cak: 0123456889abcdef...0123456789abcdef
      startTime: 2023-08-01T12:12:12Z
    

In this example, `key2` is the newly added key.

  3. Add the new key's start time, CAK, and CKN values to your on-premises router's configuration.




Google's edge routers use the key with the most recent start time and automatically switch to the next key as time progresses. All configured keys have infinite expiration times. This means that to complete a key rotation, you must remove the old key that you don't want used.

## Verify the active key

Complete the following steps:

  1. To list existing keys, select one of the following options:

###  Console 

     1. In the Google Cloud console, go to the Cloud Interconnect **Physical connections** tab.

[Go to Physical connections](https://console.cloud.google.com/hybrid/interconnects/list?tab=interconnects)

     2. Select the connection that you want to view.

     3. On the **MACsec** tab, the **Pre-shared keys** section lists all pre-shared keys for this connection.

###  gcloud 
    
    gcloud compute interconnects macsec get-config INTERCONNECT_CONNECTION_NAME
    

The output is similar to the following:
    
    preSharedKeys:
    - name: key1
      ckn: 0101010189abcdef...0123456789abcdef
      cak: 0123456789abcdef...0123456789abcdef
      startTime: 2023-07-01T12:12:12Z
    - name: key2
      ckn: 0202020289abcdef...0123456789abcdef
      cak: 0123456889abcdef...0123456789abcdef
      startTime: 2023-08-01T12:12:12Z
    

Note the CKN value for the key listed before the last key.

  2. To verify that the active key is listed before removing the old key, select one of the following options:

###  Console 

     * In the **Pre-shared** keys section, verify that the new key displays a **Key status** of **Active, in use**.

###  gcloud 
    
    gcloud compute interconnects get-diagnostics INTERCONNECT_CONNECTION_NAME
    

The output is similar to the following; look for `macsec`:
    
    bundleAggregationType: BUNDLE_AGGREGATION_TYPE_STATIC
    bundleOperationalStatus: BUNDLE_OPERATIONAL_STATUS_UP
    links:
    - circuitId: LOOP-0
      googleDemarc: fake-local-demarc-0
      lacpStatus:
        googleSystemId: '00:11:22:33:44:55'
        neighborSystemId: '55:44:33:22:11:00'
        state: ACTIVE
      macsec:
        ckn: 0202020289abcdef...0123456789abcdef
        operational: true
      operationalStatus: LINK_OPERATIONAL_STATUS_UP
      receivingOpticalPower:
        state: OK
        value: -2.49
      transmittingOpticalPower:
        state: OK
        value: -0.88
    macAddress: 00:11:22:33:44:55
    

The `gcloud compute interconnects get-diagnostics` command displays the active key's CKN value. If you have more than one key configured, then the key with the latest start time is selected as the active key. Google's edge routers reject any new MACsec sessions that attempt to use the older keys.




## Remove the old key

As a safety precaution, MACsec for Cloud Interconnect prevents you from removing the last active key.

To remove the old key, complete the following steps:

  1. Remove the old key from your on-premises router configuration. This ensures that the old key isn't used by your on-premises router before you delete the old key from Cloud Interconnect.

  2. To remove the old key from your Cloud Interconnect connection configuration, select one of the following options:

###  Console 

     1. In the Google Cloud console, go to the Cloud Interconnect **Physical connections** tab.

[Go to Physical connections](https://console.cloud.google.com/hybrid/interconnects/list?tab=interconnects)

     2. Select the connection that you want to view.

     3. On the **MACsec** tab, go to **Pre-shared keys** , select the key you want to delete, and then click **Delete.**

     4. In the **Pre-shared** keys section, verify that the new key displays a **Key status** of **Active, in use** and that the key you wanted to delete is no longer listed.

###  gcloud 

     1. Run the following command:
            
            gcloud compute interconnects macsec remove-key INTERCONNECT_CONNECTION_NAME \
                --key-name=KEY_NAME
            

Replace the following:

        * `INTERCONNECT_CONNECTION_NAME`: the name of your Cloud Interconnect connection
        * `KEY_NAME`: the name of your key
     2. To verify that you removed the correct key, run the following command:
            
            gcloud compute interconnects macsec get-config INTERCONNECT_CONNECTION_NAME
            

The output is similar to the following:
            
            preSharedKeys:
            - name: key2
              ckn: 0202020289abcdef...0123456789abcdef
              cak: 0123456889abcdef...0123456789abcdef
              startTime: 2023-08-01T12:12:12Z
            




## What's next?

  * [Troubleshoot MACsec](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/macsec/troubleshoot-macsec)
  * [View MACsec status](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/macsec/view-macsec-status)
  * [Get MACsec keys](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/macsec/get-macsec-keys)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
