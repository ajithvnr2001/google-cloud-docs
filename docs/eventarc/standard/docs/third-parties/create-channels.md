---
url: https://docs.cloud.google.com/eventarc/standard/docs/third-parties/create-channels/
title: Create a channel and retrieve its details \u00a0|\u00a0 Eventarc Standard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:02:16.533591+00:00
---

# Create a channel and retrieve its details  |  Eventarc Standard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/standard/docs/third-parties/create-channels/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/standard/docs/overview)



Send feedback 

#  Create a channel and retrieve its details Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)

**Preview — Third-party events in Eventarc; Customer-managed encryption keys**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

A _channel_ is a resource through which a third-party provider can interact with a subscriber's project. The subscriber controls the channel, and the channel must be successfully connected so that it can receive and route events from the event provider to the subscriber. For details, see [Third-party events in Eventarc](https://docs.cloud.google.com/eventarc/standard/docs/third-parties/third-parties-overview).

After a subscriber creates a channel, an activation token can be retrieved and used to create a connection with the provider. Once the provider has initialized the connection between their ecosystem and the channel, the provider can send events to the subscriber's project.

## Prerequisites

Prior to creating a channel, ensure that you have done the following:

  1. Enable the Eventarc and Pub/Sub APIs.

###  Console 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=eventarc.googleapis.com,%20eventarcpublishing.googleapis.com,%20pubsub.googleapis.com)

###  gcloud 
         
         gcloud services enable eventarc.googleapis.com \
             eventarcpublishing.googleapis.com \
             pubsub.googleapis.com
         

  2. If you are [enabling a customer-managed encryption key (CMEK)](https://docs.cloud.google.com/eventarc/docs/use-cmek#enable-cmek-thirdparty-channel) for a channel, enable the Cloud Key Management Service API.

###  Console 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudkms.googleapis.com)

###  gcloud 
         
         gcloud services enable cloudkms.googleapis.com
         




## Create a channel

Create a channel to support events from a third-party provider:

###  Console 

  1. In the Google Cloud console, go to the **Eventarc** > **Channels** page.

[Go to Channels](https://console.cloud.google.com/eventarc/channels)

  2. Click add_box **Create channel**.

  3. In the **Channel name** field, enter a name for the channel.

  4. In the **Provider** list, select a provider.

  5. In the **Region** list, select a supported Eventarc [region](https://docs.cloud.google.com/eventarc/docs/locations).

Note that for this Pre-GA feature, the following locations are supported:

     * `asia-northeast1`
     * `europe-west4`
     * `us-central1`
     * `us-west1`

You cannot create a channel in any other location.

  6. For **Encryption** , accept the default **Google-managed encryption key** or select **Cloud KMS key**. For more information, see [Use customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/eventarc/docs/use-cmek).

  7. If you select **Cloud KMS key** , do the following:

     1. In the **Key type** list, select a method to manage your keys.

You can manage your keys manually or you can use [Autokey](https://docs.cloud.google.com/kms/docs/autokey-overview) which lets you generate key rings and keys on-demand. If the **Cloud KMS with Autokey** option is disabled, it isn't yet integrated with the current resource type.

     2. In the **Select a Cloud KMS key** , select a key.

Note that you must select a region before you can view your customer-managed keys.

     3. Optionally, to manually enter the resource name of the key, in the **Select a Cloud KMS key** list, click **Enter key manually** , and enter the key name in the specified format.

     4. If prompted, grant the [`cloudkms.cryptoKeyEncrypterDecrypter` role](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.cryptoKeyEncrypterDecrypter) to the [Eventarc Service Agent](https://docs.cloud.google.com/iam/docs/service-agents#eventarc-service-agent).

  8. Optionally, to add a label, click add **Add label**. Labels are key-value pairs that help you organize your Google Cloud resources. For more information, see [What are labels?](https://docs.cloud.google.com/resource-manager/docs/labels-overview#what-are-labels)

  9. Click **Create**.




###  gcloud 
    
    
    gcloud eventarc channels create CHANNEL_NAME \
      --provider PROVIDER_NAME \
      --project PROJECT_ID \
      --location LOCATION \
      --crypto-key=KEY

Replace the following:

  * `CHANNEL_NAME`: a name for the channel
  * `PROVIDER_NAME`: the provider's name; see [List event providers](https://docs.cloud.google.com/eventarc/docs/list-providers)
  * `PROJECT_ID`: the Google Cloud project ID
  * `LOCATION`: a supported Eventarc [region](https://docs.cloud.google.com/eventarc/docs/locations)

Note that for this Pre-GA feature, the following locations are supported:

    * `asia-northeast1`
    * `europe-west4`
    * `us-central1`
    * `us-west1`

You cannot create a channel in any other location.

  * `KEY`: the fully qualified Cloud KMS key name in the format `projects/PROJECT_NAME/locations/LOCATION/keyRings/RING_NAME/cryptoKeys/KEY_NAME`

For more information, see [Use customer-managed encryption keys](https://docs.cloud.google.com/eventarc/docs/use-cmek).




## Retrieve channel properties

After creating a channel, you can retrieve specific channel properties:

###  Console 

  1. In the Google Cloud console, go to the **Eventarc** > **Channels** page.

[Go to Channels](https://console.cloud.google.com/eventarc/channels)

  2. From the list of channels, click a channel to view its details.




If the channel status is **`Pending`** , you can copy the Channel full name and Activation token value to convey to a provider.

###  gcloud 
    
    
    gcloud eventarc channels describe CHANNEL_NAME \
      --project PROJECT_ID \
      --location LOCATION

The output is similar to the following:
    
    
    **activationToken: aS7dXs1b79AcXsf**
    createTime: '2021-11-15T15:20:31.582356065Z'
    **name: projects/your-project-123/locations/us-central1/channels/your-channel**
    provider: projects/your-project-123/locations/us-central1/providers/provider-name
    pubsubTopic: projects/your-project-123/topics/eventarc-channel-us-central1-your-channel-q1w2
    state: PENDING
    uid: c6703a91-ccd3-4c32-a729-967393f23a29
    updateTime: '2021-11-15T15:21:03.689597653Z'
    

If the channel state is `PENDING`, note the `activationToken` value and the channel `name` to convey to a provider.

### Channel state

The channel state indicates the channel's current status. It can be one of the following:

  * **PENDING** —The channel has been created successfully and there is an activation token available to create a connection with the provider. To change the state of the channel from PENDING to ACTIVE, the token must be given to the provider and used to connect the channel within 24 hours of the channel's creation.
  * **ACTIVE** —The channel has been successfully connected with the provider. An ACTIVE channel is ready to receive and route events from the provider.
  * **INACTIVE** —The channel cannot receive events nor be reactivated. There are two possible reasons:

    * The provider is disconnected from this channel.
    * The channel activation token has expired and the provider isn't connected.

To re-establish a connection with a provider, you must create a new channel for the provider.




### Activation token

An activation token is a single-use, time-restricted token, used to create a connection between a provider and a subscriber's project. Only a specific provider, selected during the channel creation process can use the token. The token is valid for 24 hours after the channel's creation. After 24 hours, the channel becomes INACTIVE.

## Send channel details to the provider

To determine how best to convey the channel details, consult the provider's documentation. For instructions related to a specific provider, see the list of [third-party providers that offer an Eventarc source](https://docs.cloud.google.com/eventarc/standard/docs/third-parties/third-party-entities).

The following information must be given to the provider:

  * **Full channel name**

The channel name, including the Google Cloud project ID and location of the resource. For example: `projects/your-project-123/locations/us-central1/channels/your-channel`

  * **Activation token**

The token is valid for 24 hours after the channel's creation. After 24 hours, the channel becomes INACTIVE. For example: `aS7dXs1b79AcXsf`




Once the provider receives the required information, and has initialized the connection between their ecosystem and the channel, the state of the channel changes from PENDING to ACTIVE. The provider can now send events to the subscriber's project and the subscriber can start consuming the events.

## Edit a channel

You can edit a channel to enable a customer-managed encryption key (CMEK). For more information, see [Enable CMEK for a third-party channel](https://docs.cloud.google.com/eventarc/docs/use-cmek#enable-cmek-thirdparty-channel).

## Delete a channel

You can delete a channel:

###  Console 

  1. In the Google Cloud console, go to the **Eventarc** > **Channels** page.

[Go to Channels](https://console.cloud.google.com/eventarc/channels)

  2. Select the checkbox for the channel you want to delete.

  3. Click delete **Delete**.

  4. Confirm the deletion and then click **Delete**.




###  gcloud 
    
    
    gcloud eventarc channels delete CHANNEL_NAME \
      --location LOCATION

Replace the following:

  * `CHANNEL_NAME`: the name of the channel
  * `LOCATION`: the location of the channel



## What's next

  * [Create an Eventarc trigger for third-party events](https://docs.cloud.google.com/eventarc/standard/docs/third-parties/create-trigger-thirdparty)
  * [Learn more about Eventarc](https://docs.cloud.google.com/eventarc/standard/docs/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
