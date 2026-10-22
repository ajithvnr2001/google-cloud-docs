---
url: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-use-apigee/
title: Use Apigee with data residency \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:55:03.716067+00:00
---

# Use Apigee with data residency  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-use-apigee/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Use Apigee with data residency Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to use the Apigee UI, Apigee API, and MessageLogging and PublishMessage policies with data residency. 

For more information about data residency in Apigee, see [Introduction to data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts). 

## Use the Apigee UI with data residency

To access the Apigee UI with data residency, access one of the following consoles based on your data residency requirements:

  * Data residency (at rest only): [Google Cloud console](https://Google%20Cloud%20console)
  * Advanced data residency: [Jurisdictional console](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#jurisdictional-console)



The jurisdictional console alters the UI interactions with services as follows:

  * You'll only be able to select resource locations that are consistent with your selected control plane location. 
  * When creating endpoint attachments, you'll only be able to select service attachments consistent with the [Resource Location](https://cloud.google.com/resource-manager/docs/organization-policy/defining-locations) policy of your organization. This prevents access by a private target that isn't in a permitted location. 



## Use the Apigee API with data residency

To access the Apigee API with data residency, use the following regional endpoints described in [Use regional endpoints for data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#drz-regional-endpoint). 

When using the Apigee API, you will receive a `Permission Denied` error if you use a [region](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#drz-regions) that is prohibited by the control package.

## Use the MessageLogging and PublishMessage policies with data residency

The following sections describe how to update the policy definitions for the MessageLogging and PublishMessage policies to support data residency.

### Use the MessageLogging policy with data residency

When using the MessageLogging policy, to support data residency update the policy definition to add the `<Endpoint>` element to the `<CloudLogging>` element and set it to the regional endpoint to use for message logging, as follows:

`logging.CONTROL_PLANE_LOCATION.rep.googleapis.com:443`.

**Important:** When using VPC Service Controls with data residency, you must use the following regional endpoint: `CONTROL_PLANE_LOCATION-logging.googleapis.com`. 

CONTROL_PLANE_LOCATION is the physical location, specified during provisioning, where Apigee [control plane data](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#drz-regions) will be stored.

If you don't add the `<Endpoint>` element, the policy defaults to the global endpoint.

For example, the following policy definition uses the regional endpoint for message logging in the `us` region:
    
    
    <MessageLogging name="LogToCloudLogging">
        <CloudLogging>
            <LogName>projects/{organization.name}/logs/{log.id}</LogName>
            <Message contentType="application/json">{"{message.queryparam.key}": "{message.queryparam.value}"}</Message>
            <Labels>
                <Label>
                    <Key>key1</Key>
                    <Value>value1</Value>
                </Label>
                <Label>
                    <Key>key2</Key>
                    <Value>value2</Value>
                </Label>
            </Labels>
            <ResourceType>api</ResourceType>
            **< Endpoint>logging.us.rep.googleapis.com:443</Endpoint>**
        </CloudLogging>
    </MessageLogging>

For more information, see [MessageLogging policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/message-logging-policy).

### Use the PublishMessage policy with data residency

To support data residency, when using the PublishMessage policy, you must update the policy definition to add the `<Endpoint>` element to the `<CloudPubSub>` element and set it to the regional endpoint to use for Pub/Sub messaging, as follows:

`pubsub.CONTROL_PLANE_LOCATION.rep.googleapis.com:443`.

**Important:** When using VPC Service Controls with data residency, you must set the `<Endpoint>` element to the following regional endpoint: 

`CONTROL_PLANE_LOCATION-pubsub.googleapis.com`

CONTROL_PLANE_LOCATION is the physical location, specified during provisioning, where Apigee [control plane data](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#drz-regions) will be stored.

If you don't add the `<Endpoint>` element, the policy defaults to the global endpoint.

For example, the following policy definition uses the regional endpoint for Pub/Sub messaging in the `us` region:
    
    
    <PublishMessage async="false" continueOnError="false" enabled="true" name="Publish to Pub/Sub">
        <DisplayName>Publish to Pub/Sub</DisplayName>
        <Description>Publish to Pub/Sub</Description>
        <CloudPubSub>
            <Topic>projects/{organization.name}/topics/{topic.name}</Topic>
            **< Endpoint>pubsub.us.rep.googleapis.com:443</Endpoint>**
        </CloudPubSub>
    </PublishMessage>

For more information, see [PublishMessage policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/publish-message-policy).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
