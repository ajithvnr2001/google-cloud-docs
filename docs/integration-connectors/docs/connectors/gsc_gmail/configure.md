---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/gsc_gmail/configure/
title: Gmail \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:29:12.526750+00:00
---

# Gmail  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/gsc_gmail/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — BigQuery Connector**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

# Gmail

The Gmail connector lets you perform the read and delete operations on Gmail.

## Supported versions

This connector supports Gmail REST APIs.

## Before you begin

Before using the Gmail connector, do the following tasks:

  * In your Google Cloud project: 
    * Grant the [roles/connectors.admin](https://docs.cloud.google.com/integration-connectors/docs/connectors-access-permissions#iam-roles-for-integration-connectors) IAM role to the user configuring the connector.
    * Grant the following IAM roles to the service account that you want to use for the connector: 
      * `roles/secretmanager.viewer`
      * `roles/secretmanager.secretAccessor`

A service account is a special type of Google account intended to represent a non-human user that needs to authenticate and be authorized to access data in Google APIs. If you don't have a service account, you must create a service account. For more information, see [Creating a service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating). 

    * Enable the following services: 
      * `secretmanager.googleapis.com` (Secret Manager API)
      * `connectors.googleapis.com` (Connectors API)

To understand how to enable services, see [Enabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable#enabling).

If these services or permissions have not been enabled for your project previously, you are prompted to enable them when configuring the connector. 




## Configure the connector

A connection is specific to a data source. It means that if you have many data sources, you must create a separate connection for each data source. To create a connection, do the following:

  1. In the [Cloud console](https://console.cloud.google.com), go to the **Integration Connectors > Connections** page and then select or create a Google Cloud project. 

[ Go to the Connections page ](https://console.cloud.google.com/connectors/connections)

  2. Click **\+ CREATE NEW** to open the **Create Connection** page.
  3. In the **Location** section, complete the following: 
     1. **Region** : Select a location from the drop-down list. 

For the list of all the supported regions, see [Locations](https://docs.cloud.google.com/integration-connectors/docs/locations).

     2. Click **Next**.
  4. In the **Connection Details** section, complete the following: 
     1. **Connector** : Select **Gmail** from the list of available connectors.
     2. **Connector version** : Select the connector version from the list of available versions. 
     3. In the **Connection Name** field, enter a name for the connection instance. The connection name can contain lower-case letters, numbers, or hyphens. The name must begin with a letter and end with a letter or number and the name must not exceed 49 characters.
     4. **Description** : Enter a description for the connection instance.
     5. Optionally, enable [Cloud logging](https://docs.cloud.google.com/integration-connectors/docs/view-connector-logs), and then select a log level. By default, the log level is set to `Error`. 
     6. **Service Account** : Select a service account that has the required roles.
     7. Optionally, configure the **Connection node settings** : 

        * **Minimum number of nodes** : Enter the minimum number of connection nodes.
        * **Maximum number of nodes** : Enter the maximum number of connection nodes.

A node is a unit (or replica) of a connection that processes transactions. More nodes are required to process more transactions for a connection and conversely, fewer nodes are required to process fewer transactions. To understand how the nodes affect your connector pricing, see [ Pricing for connection nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes). If you don't enter any values, by default the minimum nodes are set to 2 (for better availability) and the maximum nodes are set to 50.

**Note:** You can customize the connection node values only if you are a Pay-as-you-go customer.
     8. **\+ ADD LABEL** : Click this to add a label to the connection in the form of a key-value pair.
     9. Click **Next**.
  5. In the **Authentication** section, enter the authentication details. 
     1. Select an **Authentication type** and enter the relevant details. 

The following authentication types are supported by the Gmail connection:

        * Service Account Authentication
        * OAuth 2.0 - JWT Bearer
        * OAuth 2.0 - Authorization code

To understand how to configure these authentication types, see Configure authentication.

     2. Click **Next**.
  6. **Review** : Review your connection and authentication details.
  7. Click **Create**.



### Configure authentication

Enter the details based on the authentication you want to use.

  * **Service Account Authentication** : No additional configuration is required for this authentication type. The service account you selected in the **Connection Details** section will be used for authentication.. 
  * **OAuth 2.0 - JWT Bearer**
    * **JWT Certificate** : Select the certificate to use for JWT authentication.
    * **Secret version** : Enter the secret version of the JWT certificate.
    * **JWT Subject** : Enter the JWT subject.
    * **Enable Authentication Override** : Enable to override the authentication.
  * **OAuth 2.0 - Authorization code**
    * **Client ID** : Enter the client ID to use for OAuth authentication.
    * **Scopes** : Enter a list of desired scopes.
    * **Client Secret** : The client secret to use for OAuth authentication.
    * **Secret version** : Enter the secret version of the client secret.
    * **Enable Authentication Override** : Enable to override the authentication.
When you configure your third-party OAuth application, use this **authorized redirect URI** (callback URL): 

`https://console.cloud.google.com//connectors/oauth?project=PROJECT_ID`

Replace `PROJECT_ID` with your Google Cloud project ID.




## Connection configuration samples

This section lists the sample values for the various fields that you configure when creating the connection.

### OAuth 2.0 - JWT bearer connection type

Field name | Details  
---|---  
Location | asia-east1  
Connector | Gmail  
Connector version | 1  
Connection Name | gmail-jwt-conn  
Enable Cloud Logging | true  
Service Account | my-service-account@my-project.iam.gserviceaccount.com  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Authentication | OAuth 2.0 - JWT Bearer  
JWT Cert | JWT certificate  
Secret version | 1  
  
### OAuth 2.0 - authorization code connection type

Field name | Details  
---|---  
Location | us-central1  
Connector | Gmail  
Connector version | 1  
Connection Name | gmail-auth-conn  
Enable Cloud Logging | Yes  
Service Account | my-service-account@my-project.iam.gserviceaccount.com  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Authentication | OAuth 2.0 - Authorization code  
Client ID | 60875425788659-mt0cm1tguyiagvst468fvaw7.apps.googleusercontent.com  
Scopes | https://mail.google.com/  
Client Secret | ygdruoX-Rtyah9gzkdZc-7CB0Eng9hyaufD0VD  
Secret version | 1  
  
## System limitations

The Gmail connector can process a maximum of 1 transaction per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Use the Gmail connection in an integration

After you create the connection, it becomes available in both Apigee Integration and Application Integration. You can use the connection in an integration through the Connectors task.

  * To understand how to create and use the connectors task in Apigee Integration, see [Connectors task](https://docs.cloud.google.com/apigee/docs/api-platform/integration/connectors-task#configure-the-connectors-task).
  * To understand how to create and use the Connectors task in Application Integration, see [connectors task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task).



## Actions

This section shows how to perform some of the [actions](https://docs.cloud.google.com/integration-connectors/docs/entities-operation-action) in this connector.

### SendMailMessages action

This action sends a Gmail message.

#### Input parameters of the SendMailMessages action

Parameter name | Data type | Required | Description  
---|---|---|---  
To | String | Yes | The primary recipient's email address. For multiple recipients, use a comma-separated list.  
AttachmentHasBytes | String | No | Set this to true if the attachment content is provided in AttachmentContentBytes (Base64-encoded), or false if the content is provided as a string in AttachmentContent. Defaults to false.  
AttachmentFileName | String | No | The name of the file to attach. This parameter is used when AttachmentHasBytes is false or not provided.  
Subject | String | Yes | The subject line of the email.  
AttachmentContent | String | No | The string content of the file to attach. This parameter is used when AttachmentHasBytes is set to false or not provided.  
BCC | String | No | The BCCed recipient's email address. For multiple recipients, use a comma-separated list.  
AttachmentContentBytes | String | No | The Base64 encoded bytes content of the file to attach. This parameter is used when AttachmentHasBytes is set to true.  
CC | String | No | The CCed recipient's email address. For multiple recipients, use a comma-separated list.  
Content | String | Yes | The main content of the email message.  
AttachmentPath | String | No | A comma-separated list of local file paths to attach to the email.  
  
For an example about how to configure the `SendMailMessages` action, see Examples.

### DownloadAttachment action

This action downloads an attachment from Gmail.

#### Input parameters of the DownloadAttachment action

Parameter name | Data type | Required | Description  
---|---|---|---  
MessageId | String | Yes | The ID of the email.  
DownloadLocation | String | No | The location where the attachment will be saved.  
FileStream | String | No | An instance of an output stream where file data is written to.  
AttachmentId | String | No | The ID of the attachment. It must be provided if the FileStream is specified.  
  
For an example about how to configure the `DownloadAttachment` action, see Examples.

## Action examples

This section shows how to perform some of the actions in this connector.

### Example - Send a Gmail message

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `SendMailMessages` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "To": "testbristleconeemail@gmail.com",
           "Subject": "Data MapperCheck",
           "Content": "Gmail",
         }
         

If the action is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
    "Id": "199334f660ff462a"
    }]
    




### Example - Send a Gmail message with a JPG attachment

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `SendMailMessages` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "To": "testbristleconeemail@gmail.com",
         "Subject": "Data Mapper Email Sep10 JPG",
         "Content": "Gmail",
         "AttachmentFileName": "TestSep10.jpg",
         "AttachmentContentBytes": "/9j/4AAQSkZJRgABAQEBLAEsAAD/2wBDAAIBAQEBAQIBAQECAgICAgQDAgICAgUEBAMEBgUGBgYFBgYGBwkIBgcJBwYGCAsICQoKCgoKBggLDAsKDAkKCgr/2wBDAQICAgICAgUDAwUKBwYHCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgr/wAARCANUBdwDAREAAhEBAxEB/8QAHgABAAAGAwEAAAAAAAAAAAAAAAEDBAcICQIFBgr/xABsEAABAwMCBAMFBQQHAwUJACMBAgMEAAURBgcIEiExCRNBChQiUWEVIzJxgUJSkaEWFzNicrHBJEPRNFOCkqIYJTlEY4O14fDxJmRzdXZ3k7PCNTY4haOytLYZN1RVV8NIVmV0eJSWpNLT4v/EAB0BAQABBAMBAAAAAAAAAAAAAAAHAQQFBgIDCAn/xABXEQABAwURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIlESiJREoiURKIv/Z",
         "AttachmentHasBytes": true
         }
         

If the action is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
      "Id": "199334f660ff462a"
    }]
    




### Example - Send a Gmail message with a PDF attachment

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `SendMailMessages` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "To": "testbristleconeemail@gmail.com",
           "Subject": "Data Mapper Email Sep10",
           "Content": "Gmail",
           "AttachmentFileName": "TestSep10.pdf",
           "AttachmentContent": "JVBERi0xLjQKJcOkw7zDtsOfCjIgMCBvYmoKPDwvTGVuZ3RoIDMgMCBSL0ZpbHRlci9GbGF0ZURlY29kZT4+CnN0cmVhbQp4nD2OywoCMQxF9/mKu3YRk7bptDAIDuh+oOAP+AAXgrOZ37etjmSTe3ISIljpDYGwwrKxRwrKGcsNlx1e31mt5UFTIYucMFiqcrlif1ZobP0do6g48eIPKE+ydk6aM0roJG/RegwcNhDr5tChd+z+miTJnWqoT/3oUabOToVmmvEBy5IoCgplbmRzdHJlYW0KZW5kb2JqCgozIDAgb2JqCjEzNAplbmRvYmoKCjUgMCBvYmoKPDwvTGVuZ3RoIDYgMCBSL0ZpbHRlci9GbGF0ZURlY29kZS9MZW5ndGgxIDIzMTY0Pj4Kc3RyZWFtCnic7Xx5fFvVlf+59z0tdrzIu7xFz1G8Kl7i2HEWE8vxQlI3iRM71A6ksSwrsYptKZYUE9omYStgloZhaSlMMbTsbSPLAZwEGgNlusxQ0mHa0k4Z8muhlJb8ynQoZVpi/b736nkjgWlnfn/8Pp9fpNx3zz33bPecc899T4oVHA55KIEOkUJO96DLvyQxM5WI/omIpbr3BbU/3J61FPBpItOa3f49g1948t/vI4rLIzL8dM/A/t3vn77ZSpT0LlH8e/0eV98jn3k0mSj7bchY2Q/EpdNXm4hyIIOW9g8Gr+gyrq3EeAPGVQM+t+uw5VrQ51yBcc6g6wr/DywvGAHegbE25Br0bFR/ezPGR4kq6/y+QPCnVBYl2ijka/5hjz95S8kmok8kEFl8wDG8xQtjZhRjrqgGo8kcF7+I/r98GY5TnmwPU55aRIhb9PWZNu2Nvi7mRM9/C2flx5r+itA36KeshGk0wf5MWfQ+y2bLaSOp9CdkyxE6S3dSOnXSXSyVllImbaeNTAWNg25m90T3Rd+ii+jv6IHoU+zq6GOY/yL9A70PC/5NZVRHm0G/nTz0lvIGdUe/Qma6nhbRWtrGMslFP8H7j7DhdrqDvs0+F30fWtPpasirp0ZqjD4b/YDK6Gb1sOGVuCfoNjrBjFF31EuLaQmNckf0J9HXqIi66Wv0DdjkYFPqBiqgy+k6+jLLVv4B0J30dZpmCXy",
           "AttachmentHasBytes": true
         }
         

If the action is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
      "Id": "1993341d558d7b07"
    }]
    




### Example - Send a Gmail message with a TXT attachment

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `SendMailMessages` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "To": "testbristleconeemail@gmail.com",
           "Subject": "Data Mapper Email Sep10",
           "Content": "Gmail",
           "AttachmentFileName": "TestSep10.txt",
           "AttachmentContent": "TestingwithAttachment",
           "AttachmentHasBytes": true
         }
         

If the action is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
        "Id": "1993341d558d7b07"
    }]
    




### Example - Download an attachment from Gmail

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DownloadAttachment` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "MessageId": "198acdcde5c09ce5"
         }
         

If the action is successful, the connector task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    [{
        "Success": "true",
        "MessageId": "198acdcde5c09ce5",
        "AttachmentId": "1",
        "Size": "58005",
        "Data": "JVBERi0xLjQKJdPr6eEKMSAwIG9iago8PC9UaXRsZSAoYWJvdXQ6YmxhbmspCi9DcmVhdG9yIChNb3ppbGxhLzUuMCBcKFgxMTsgTGludXggeDg2XzY0XCkgQXBwbGVXZWJLaXQvNTM3LjM2IFwoS0hUTUwsIGxpa2UgR2Vja29cKSBIZWFkbGVzc0Nocm9tZS8xMzguMC4wLjAgU2FmYXJpLzUzNy4zNikKL1Byb2R1Y2VyIChTa2lhL1BERiBtMTM4KQovQ3JlYXRpb25EYXRlIChEOjIwMjUwODE1MDgwMDE2KzAwJzAwJykKL01vZERhdGUgKEQ6MjAyNTA4MTUwODAwMTYrMDAnMDAnKT4-CmVuZG9iagozIDAgb2JqCjw8L2NhIDEKL0JNIC9Ob3JtYWw-PgplbmRvYmo",
        "Filename": "My_Store_404672162.pdf",
        "@isoutervalue": null
    }]
    




## Entity operation examples

This section shows how to perform some of the entity operations in this connector.

### Example - List all the Gmail messages

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Messages` from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.
  4. In the **Task Input** section of the **Connectors** task, you can set the **filterClause** as per the customer requirement.

You must use single quotes (') to enclose the value for a **filterClause**. You can use the **filterClause** to filter records based on the columns.




### Example - Get a Gmail message details from inbox

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Inbox` from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. Set the **entityId** to `1` which is the key to be passed. To set the entityId, in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `1` in the **Input Value** field and choose the entityId as local variable.

The value for **entityId** must be passed directly, such as `"1"`. Here, `"1"` is the unique primary key value, which is passed.

In some cases, passing a single **entityId** may cause an error because the entity has two composite keys. In such cases, you can use the **filterClause** and pass the value, such as `id='1'`.




### Example - Delete a Gmail message

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select `Messages` from the `Entity` list.
  3. Select the `Delete` operation, and then click **Done**.
  4. Set the **entityId** to `1` which is the key to be passed.
  5. To set the **entityId** , in the **Data Mapper** section of the **Data Mapping** , click **Open Data Mapping Editor** and then enter `1` in the **Input Value** field and choose the **entityId** as local variable. 

If entity has two composite business or primary keys instead of specifying the **entityId** , you can also set the **filterClause** to `id='1'`.




## Get help from the Google Cloud community

You can post your questions and discuss this connector in the Google Cloud community at [Cloud Forums](https://www.googlecloudcommunity.com/gc/Integration-Services/bd-p/cloud-integration-services). 

## What's next

  * Understand how to [suspend and resume a connection](https://docs.cloud.google.com/integration-connectors/docs/suspend-resume-connection).
  * Understand how to [monitor connector usage](https://docs.cloud.google.com/integration-connectors/docs/cloud-monitoring).
  * Understand how to [view connector logs](https://docs.cloud.google.com/integration-connectors/docs/view-connector-logs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
