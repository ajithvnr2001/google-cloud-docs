---
url: https://docs.cloud.google.com/application-integration/docs/configure-hl7-trigger/
title: HL7 trigger \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:17:38.686774+00:00
---

# HL7 trigger  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/configure-hl7-trigger/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# HL7 trigger

**Preview — HL7 trigger**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The **HL7 trigger** is a [Connector Event trigger](https://docs.cloud.google.com/application-integration/docs/triggers#event-triggers) that lets you invoke an integration based on the HL7 events that you've subscribed to in your HL7 connection.

**Important:** Integration Connectors is a billable component of Google Cloud. For information about the costs and charges of using Integration Connectors, see [Integration Connectors pricing](https://docs.cloud.google.com/integration-connectors/docs/pricing).

## Before you begin

  * Create a [Pub/Sub topic](https://cloud.google.com/pubsub/docs/create-topic).
  * Create an [HL7 store](https://cloud.google.com/healthcare-api/docs/how-tos/hl7v2).
  * To receive HL7 messages over TCP/IP connections using the minimal lower layer protocol (MLLP), you must configure an MLLP adapter. You don't need to configure an MLLP adapter if you receive HL7 messages over REST (Google Cloud HealthCare API). To run the adapter, do the following:

    1. Set the project and region in the gcloud CLI: 
           
           gcloud config set project PROJECT_ID \
           gcloud config set compute/region LOCATION

For more information, see [Set properties](https://cloud.google.com/sdk/gcloud/reference/config/set).

    2. Create a [VM instance](https://cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#using). 
           
           gcloud compute instances create VM_NAME \
                  --service-account=SERVICE_ACCOUNT_EMAIL \
                  --scopes=https://www.googleapis.com/auth/cloud-platform
              

Replace the following:

       * `SERVICE_ACCOUNT_EMAIL`: the email address for the service account that you created.
       * `VM_NAME`: The name of the VM instance.
    3. Add a [tag](https://cloud.google.com/vpc/docs/add-remove-network-tags#adding_new_tags_to_vm_instances) to the newly created VM instance. 
           
           gcloud compute instances add-tags INSTANCE_NAME \
              --zone ZONE \
              --tags TAGS
              

Replace the following:

       * `INSTANCE_NAME`: The name of the VM instance.
       * `ZONE`: The zone of the VM instance.
       * `TAGS`: The tags to add to the VM instance.
    4. Add a [firewall rule](https://cloud.google.com/firewall/docs/using-firewalls#common-use-cases-allow-internal) to expose the port on which the MLLP adapter is running. 
           
           gcloud compute firewall-rules create FIREWALL_RULE \
              --action=ALLOW \
              --direction=INGRESS \
              --priority=1000 \
              --rules=tcp:PORT\
              --network=default \
              --source-ranges=0.0.0.0/0
           

Replace the following:

       * `FIREWALL_RULE`: The name of the firewall rule.
       * `PORT`: The port on which the MLLP adapter is running.
    5. [SSH](https://cloud.google.com/compute/docs/connect/standard-ssh#gcloud) into the VM instance. 
           
           gcloud compute ssh VM_NAME --zone ZONE
            

Replace the following:

       * `VM_NAME`: The name of the VM instance.
       * `ZONE`: The zone of the VM instance.
    6. Install the docker in the VM using the following command: 
           
           sudo apt-get update && sudo apt-get install -y docker.io
              

    7. Start the docker service by running the following commands: 
           
           sudo systemctl start docker
              sudo systemctl enable docker
              

    8. Pull the [docker image](https://cloud.google.com/healthcare-api/docs/how-tos/mllp-adapter#pulling_the_pre-built_docker_image) in the container registry. 
           
           docker pull gcr.io/cloud-healthcare-containers/mllp-adapter:latest
              

    9. [Run MLLP adapter](https://cloud.google.com/healthcare-api/docs/how-tos/mllp-adapter#testing_the_mllp_adapter_locally_as_a_receiver) on the VM instance. 
           
           docker run \
              --network=host \
              -v ~/.config:/root/.config \
              gcr.io/cloud-healthcare-containers/mllp-adapter \
              /usr/mllp_adapter/mllp_adapter \
              --hl7_v2_project_id=PROJECT_ID \
              --hl7_v2_location_id=LOCATION \
              --hl7_v2_dataset_id=DATASET_ID \
              --hl7_v2_store_id=HL7V2_STORE_ID \
              --export_stats=false \
              --receiver_ip=0.0.0.0 \
              --port=PORT \
              --api_addr_prefix=https://healthcare.googleapis.com:443/v1 \
              --logtostderr
            

Replace the following:

       * `PROJECT_ID`: The project ID of the Google Cloud project.
       * `LOCATION`: The location of the HL7 store.
       * `DATASET_ID`: The ID of the dataset that holds the HL7 store.
       * `HL7V2_STORE_ID`: The ID of the HL7 store.
       * `PORT`: The port on which the MLLP adapter is running.
    10. Run the following command to ensure that the container is running: 
           
           sudo docker ps
              

    11. To check the container logs, run the following command: 
           
           sudo docker logs CONTAINER_ID
              




## Required roles

If you plan to create or configure a new connection for the **HL7 trigger** , make sure that you have the following IAM role on the project:

  * Connector Admin (`roles/connectors.admin`) 

For information about granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).




Grant the following IAM roles or Permissions to the service account that you want to use for the **HL7 trigger** :

  * Application Integration Invoker (`roles/integrations.integrationInvoker`) 
  * Healthcare HL7v2 Message Consumer (`roles/healthcare.hl7V2Consumer`) 
  * Healthcare HL7v2 Message Ingest (`roles/healthcare.hl7V2Ingest`) 
  * Permission (`healthcare.hl7V2Stores.update`) 
  * Pub/Sub Editor (`roles/pubsub.editor`) 

For information about granting roles to a service account, see [Manage access to service accounts](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts).




## Add the HL7 trigger

To add a **HL7 trigger** to your integration, perform the following steps: 

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. In the navigation menu, click **Integrations**

The **Integrations List** page appears listing all the integrations available in the Google Cloud project. 

  3. Select an existing integration or click **Create integration** to create a new one. 

If you are creating a new integration: 

     1. Enter a name and description in the **Create Integration** pane.
     2. Select a region for the integration. **Note:** The **Regions** dropdown only lists the regions provisioned in your Google Cloud project. To provision a new region, Click **Enable Region**. See [Enable new region](https://docs.cloud.google.com/application-integration/docs/enable-new-region) for more information. 
     3. Select a service account for the integration. You can change or update the service account details of an integration any time from the info **Integration summary** pane in the integration toolbar. **Note:** The option to select a service account is displayed only if you have enabled integration governance for the selected region. 
     4. Click **Create**.

The newly created integration opens in the _integration editor_. 

  4. In the _integration editor_ navigation bar, click **Triggers** to view the list of available triggers. 
  5. Click and place the **HL7 trigger** element in the integration editor.

To configure the **HL7 trigger** , you can either use an existing HL7 connection with REST (Cloud HealthCare API) as the destination protocol available in Integration Connectors, or create a new HL7 REST(Google Cloud HealthCare API) connection using the inline connection creation option.




## Configure HL7 trigger using an existing connection

You can configure the **HL7 trigger** using an existing HL7 connection with REST (Cloud HealthCare API) as the destination protocol in Integration Connectors. The **HL7 trigger** is an [Connector Event trigger](https://docs.cloud.google.com/application-integration/docs/triggers#event-triggers), therefore you can only use a HL7 REST(Google Cloud HealthCare API) connection with event subscription enabled to configure the trigger. 

For information about how to configure a **HL7 trigger** using a new HL7 REST(Google Cloud HealthCare API) connection, see Configure HL7 trigger using a new HL7 REST(Google Cloud HealthCare API) connection.

To configure a **HL7 trigger** using an existing HL7 connection with REST (Cloud HealthCare API) as the destination protocol, perform the following steps:

  1. Click the **HL7 trigger** element in the integration editor to open the trigger configuration pane.
  2. Click **Configure trigger**.
  3. Provide the following configuration details in the **Connector Event Trigger Editor** page: 
     1. **Region:** Select the region of your HL7 REST(Google Cloud HealthCare API) connection.
     2. **Connection:** Select the HL7 REST(Google Cloud HealthCare API) connection that you want to use. 

Application Integration only displays those HL7 REST(Google Cloud HealthCare API) connections that are active and have an event subscription enabled. 

     3. Select **HL7 Message Content Type** : text or bytes from the dropdown menu.
     4. Enter the HL7 message type. For example, `ADT_A01` or `ADT_02`.
  4. Click **Done** to complete the trigger configuration and close the page.



## Configure HL7 trigger using a new connection

To configure the **HL7 trigger** using a new HL7 REST(Google Cloud HealthCare API) connection, perform the following steps:

  1. Click the **HL7 trigger** element in the integration editor to open the trigger configuration pane.
  2. Click **Configure trigger**.
  3. Select the **Region** for the HL7 trigger.
  4. Click **Connection** and select the **Create Connection** option from the drop-down menu.
  5. Complete the following steps in the **Create Connection** pane:
  6. In the **Connection Details** step, provide details about the new HL7 connection: 
     1. **Connector version:** Choose an available version of the HL7 connector from the drop-down list. 
     2. **Connection Name:** Enter a name for the HL7 connection. **Note:** Connection names must meet the following criteria: 
        * Connection names can use letters, numbers, or hyphens.
        * Letters must be lower-case.
        * Connection names must begin with a letter and end with a letter or number.
        * Connection names cannot exceed 49 characters.
     3. (Optional) **Description:** Enter a description for the connection.
     4. Optionally, enable [Cloud logging](https://docs.cloud.google.com/integration-connectors/docs/view-connector-logs), and then select a log level. By default, the log level is set to `Error`. 
     5. **Service Account** : Select a service account with the required IAM roles for the HL7 connection.
     6. **Enable event subscription:** Select this option to enable the event subscription for the HL7 connection. **Note:** This connector doesn't support the `Enable only event subscription` option.
     7. (Optional) Enter **Receive Timeout** : The SO_TIMEOUT value (in milliseconds) is used when waiting for the start of an frame. The default value is 15000 milliseconds.
     8. **Destination Protocol** : Select HL7 REST(Google Cloud HealthCare API) destination protocol and then specify the following: 
        1. **Project ID** : The Google Cloud project ID where the HL7 store is located. 
        2. **Location** : The location of your dataset and the HL7v2 store.
        3. **Dataset ID** : The ID for the dataset that holds the HL7v2 store.
        4. **HL7 Store ID** : The ID for the HL7v2 store where you store the HL7v2 message. 
     9. Optionally, configure the **Connection node settings** : 

        * **Minimum number of nodes** : Enter the minimum number of connection nodes.
        * **Maximum number of nodes** : Enter the maximum number of connection nodes.

A node is a unit (or replica) of a connection that processes transactions. More nodes are required to process more transactions for a connection and conversely, fewer nodes are required to process fewer transactions. To understand how the nodes affect your connector pricing, see [ Pricing for connection nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes). If you don't enter any values, by default the minimum nodes are set to 2 (for better availability) and the maximum nodes are set to 50.

**Note:** You can customize the connection node values only if you are a Pay-as-you-go customer.
     10. Optionally, click **\+ Add label** to add a label to the Connection in the form of a key/value pair. 
     11. Optionally, if you want to use SSL, select **Enable SSL**. This displays the SSL configuration details. 
        1. Select a trust store type. It can be either **Public** , **Private** , or **Insecure Connection**. 
        2. Select the certificates as displayed based on your trust store selection.
        3. If you are using mTLS, select the key store certificates in the **Key Store** section.
        4. Optionally, select the TLS version.
        5. Enter the supported cipher suite. Enter multiple cipher suites, as comma separated values. For more information, see Supported cipher suites. 
**Note:**
        * All your certificates must be X.509 certificates and must be in PEM (Privacy Enhanced Mail) format.
        * You can't directly select a certificate when configuring SSL. You must store all your certificates and private keys as a Secret Manager Secret, and then select the required secret during SSL configuration.
     12. Click **Next**.
  7. Skip the **Destinations** section. 
  8. Click **Next**.
  9. In the **Authentication** section, you don't need to specify any authentication details because the HL7 connection doesn't require any authentication. 
  10. In the **Event Subscription Details** section, configure the event related details. 
     * **Project Name** : The Google Cloud project where the Pub/Sub instance resides.
     * **Pub/Sub Topic Name** : The Pub/Sub topic name to be associated with the HL7v2 store to which the notification messages will be sent.
  11. **Review** : Review your connection and authentication details.
  12. Click **Create**.



### Supported cipher suites

TLS version | Supported cipher suites  
---|---  
1.2 | 

  * TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
  * TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
  * TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256
  * TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384
  * TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
  * TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
  * TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
  * TLS_DHE_RSA_WITH_AES_128_GCM_SHA256
  * TLS_DHE_RSA_WITH_AES_256_GCM_SHA384
  * TLS_DHE_RSA_WITH_AES_128_CBC_SHA
  * TLS_DHE_RSA_WITH_AES_256_CBC_SHA
  * TLS_DHE_RSA_WITH_AES_128_CBC_SHA256
  * TLS_DHE_RSA_WITH_AES_256_CBC_SHA256

  
1.3 | 

  * TLS_AES_256_GCM_SHA384
  * TLS_CHACHA20_POLY1305_SHA256
  * TLS_AES_128_GCM_SHA256

  
  
## Trigger output

The **HL7 trigger** takes a couple of minutes to complete the event subscription configuration. You can view the status of your event subscription in the trigger configuration pane under **Event Subscription details**.

The **HL7 trigger** indicates the status of an event subscription using the following states:

  * restart_alt `Creating`: Indicates that the trigger is subscribing to the event subscription. 
  * check_circle `Active`: Indicates that the trigger is successfully subscribed to an event subscription.
  * error `Error`: Indicates that the there is an issue with the configured event subscription. 



In addition to the event subscription status, the **Event Subscription details** section also displays other details such as connection region, connection name, and event subscription name.

### Trigger output variable

For each event, the **HL7 trigger** generates a `ConnectorEventPayload` output variable (in JSON format) which you can use in your downstream tasks. The output variable will have the payload from your HL7 event. For example: 
    
    
     {
     "messageType": "ADT_A01",
     "message": "MSH|^~\\&|SendingApp|SendingFacility|ReceivingApp|ReceivingFacility|20240209120000||ADT^A01|123456789|P|2.3|||NE|AL|||||\rEVN|A02222221|20240209120000|||\rPID|1||123456789|^^^Hospital^MR||Doe^John^^^Mr.||19800101|M|||123 Main St^^New York^NY^10001^USA||(555)555-1234|(555)555-1235\rPV1|1|I|2000^2012^01||||123^Doe^John|||SUR||||ADM|A0||\r",
     "contentType": "text/plain"
    }

### View event subscriptions

To view and manage all the event subscriptions associated with a connection in Integration Connectors, do the following:

  1. Go to **Integration Connectors > Connections** page. 

[ Go to the Connections page](https://console.cloud.google.com/connectors/connections)

  2. Click the connection for which you want to view the subscriptions.
  3. Click the **Event subscriptions** tab. 

This displays all the event subscriptions for the connection.




## Edit HL7 trigger

You can edit a **HL7 trigger** to change or update the connection configuration and event subscription details.

**Important:** When you edit or modify a HL7 trigger, you can either retain the previously configured event subscription that is attached to the trigger, or you can delete it. Deleting an event subscription will affect all the published integrations using that event subscription. 

To edit a HL7 trigger, perform the following steps:

  1. Click the **HL7 trigger** element in the integration editor to open the trigger configuration pane.
  2. Click **Configure HL7 trigger**.
  3. Do the following in the **Connector Event Trigger Editor** page: 
     1. To retain the previously configured event subscription, click **Retain** , else click **Delete**. **Warning:** Deleting an event subscription will affect all the published integrations using the event subscription. This task cannot be undone.
     2. Update the connection configuration and event subscription details as desired.
     3. Click **Done**.

You can view the updated connection and event subscription details in the trigger configuration pane under **Event Subscription details**.




## Quotas and limits

For information about quotas and limits, see [Quotas and limits](https://docs.cloud.google.com/application-integration/docs/quotas).

## What's next

  * Learn about [all tasks and triggers](https://docs.cloud.google.com/application-integration/docs/all-triggers-tasks).
  * Learn how to [test and publish an integration](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations).
  * Learn about [error handling](https://docs.cloud.google.com/application-integration/docs/error-handling-strategy).
  * Learn about [integration execution logs](https://docs.cloud.google.com/application-integration/docs/introduction-logs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
