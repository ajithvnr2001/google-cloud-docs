---
url: https://docs.cloud.google.com/vpc/docs/manage-private-service-connect-services/
title: Manage published services \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:32.087037+00:00
---

# Manage published services  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/manage-private-service-connect-services/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage published services

This page describes how to manage published services, including handling requests for access to a published service, configuring connection reconciliation, and updating a service attachment to refer to a new target service.

Each service attachment has a connection preference that controls whether connections are automatically accepted.

  * **Automatically accept all connections.** The service attachment automatically accepts all inbound connection requests from any consumer. 
  * **Explicitly accept connections from selected consumers.** The service attachment only accepts inbound connection requests if the consumer is on the service attachment's consumer accept list. You can specify consumers by project, VPC network, or individual Private Service Connect endpoint. You can't include different types of consumers in the same consumer accept or reject list. 



For either connection preference, connections that are accepted can be overridden and rejected by an [organization policy](https://docs.cloud.google.com/vpc/docs/manage-security-private-service-connect-producers#block-consumers) that blocks incoming connections. 

We recommend that you explicitly accept connections for selected consumers. Automatically accepting all connections might be appropriate if you control consumer access through other means and want to enable permissive access to your service.

For more information about publishing a service, see [Publish a service](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer#publish-service).

## Roles

The following [IAM role](https://docs.cloud.google.com/iam/docs/understanding-roles) provides the permissions needed to perform the tasks in this guide.

  * [Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)



## Manage access to a published service

If you have published a service with explicit approval, you can accept or reject connections by updating your consumer lists. To accept a connection, you add the requesting consumer's project, VPC network, or individual Private Service Connect endpoint to a service's consumer accept list. You can explicitly reject connections by updating the consumer reject list in the same way.

You can add projects or VPC networks to the consumer lists before or after the consumer requests a connection. You can only add endpoints after a connection request, because an endpoint's URI isn't known until after the endpoint is created.

All values in the consumer lists must be of the same type. For example, you can't accept some connections based on consumer project and some based on individual endpoints. If you add the same value to both the accept list and the reject list, connection requests from that consumer are rejected.

By default, changes to consumer lists only affect new or pending connections. Previously accepted connections are not terminated unless you have enabled [connection reconciliation](https://docs.cloud.google.com/vpc/docs/about-controlling-access-published-services#connection-reconciliation).

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.serviceAttachments.update`



**Roles**

See Roles for role information.

###  Console 

You can manage access for a service with explicit approval by either accepting or rejecting existing connection requests, or by updating the consumer accept and reject lists. Both methods have the same result and update the same consumer lists.

**View details for a published service**

  1. In the Google Cloud console, go to the **Private Service Connect** page.

[Go to Private Service Connect](https://console.cloud.google.com/net-services/psc)

  2. Click the **Published services** tab.

  3. Click the service that you want to manage.




**Accept or reject connection requests**

  * If your service is configured to accept connections based on consumer project, the projects that have attempted to connect to this service are listed in the **Connected projects** section. Select the checkbox next to one or more projects, and then click **Accept project** or **Reject project**.
  * If your service is configured to accept individual Private Service Connect endpoints, click **Awaiting approval** to view the endpoints that have attempted to connect to this service. Select the checkbox next to one or more endpoints, and then click **Accept endpoint** or **Reject endpoint**.
  * If your service is configured to accept consumers based on VPC network, you can only accept or reject connections by updating your consumer accept and reject lists, as described in the following section.



**Update consumer accept and reject lists**

  1. Click **Edit service details**.
  2. Optional: Select a new connection preference.
  3. Complete the following applicable step. You can repeat this step for each consumer that you want to add.

     * For **Accept connections for selected projects** , click **Add accepted project** , and then enter the project and connection limit.
     * For **Accept connections for selected networks** , click **Add accepted network** , and then enter the project, VPC network, and connection limit.
     * For **Accept connections for selected endpoints** , click **Add accepted endpoint** , and then enter the project and the endpoint's ID.

You can find an endpoint's ID by viewing the published service and checking the **Awaiting approval** section for the value of **Endpoint ID**.




###  gcloud 

  1. To view existing and pending connections for the service attachment that you want to modify, use the [`gcloud compute service-attachments describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/service-attachments/describe).
         
         gcloud compute service-attachments describe ATTACHMENT_NAME \
             --region=REGION
         

Replace the following:

     * `ATTACHMENT_NAME`: the name of the service attachment.
     * `REGION`: the region of the service attachment.

The output is similar to the following example. If there are any pending consumer connections, they are listed with status `PENDING`. The Private Service Connect endpoint's ID-based URI that you can use to accept or reject individual endpoints is displayed in the `endpointWithId` field.

In this example output, the project `CONSUMER_PROJECT_1` is in the accept list, so `ENDPOINT_1` is accepted and can connect to the service. The project `CONSUMER_PROJECT_2` is not on the accept list, and so `ENDPOINT_2` is pending. After `CONSUMER_PROJECT_2` is added to the accept list, the status of `ENDPOINT_2` changes to `ACCEPTED`, and the endpoint can connect to the service.
    
    connectedEndpoints:
    - consumerNetwork: https://www.googleapis.com/compute/v1/projects/CONSUMER_PROJECT_1/global/networks/CONSUMER_NETWORK_1
      endpoint: https://www.googleapis.com/compute/v1/projects/CONSUMER_PROJECT_1/regions/REGION_1/forwardingRules/ENDPOINT_1
      endpointWithId: https://www.googleapis.com/compute/v1/projects/CONSUMER_PROJECT_1/regions/REGION_1/forwardingRules/RESOURCE_ID_1
      pscConnectionId: 'ENDPOINT_1_ID'
      status: ACCEPTED
    - consumerNetwork: https://www.googleapis.com/compute/v1/projects/CONSUMER_PROJECT_2/global/networks/CONSUMER_NETWORK_2
      endpoint: https://www.googleapis.com/compute/v1/projects/CONSUMER_PROJECT_2/regions/REGION_2/forwardingRules/ENDPOINT_2
      endpointWithId: https://www.googleapis.com/compute/v1/projects/CONSUMER_PROJECT_2/regions/REGION_2/forwardingRules/RESOURCE_ID_2
      pscConnectionId: 'ENDPOINT_2_ID'
      status: PENDING
    connectionPreference: ACCEPT_MANUAL
    consumerAcceptLists:
    - connectionLimit: LIMIT_1
      projectIdOrNum: CONSUMER_PROJECT_1
    creationTimestamp: 'TIMESTAMP'
    description: 'DESCRIPTION'
    enableProxyProtocol: false
    fingerprint: FINGERPRINT
    id: 'ID'
    kind: compute#serviceAttachment
    name: NAME
    natSubnets:
    - https://www.googleapis.com/compute/v1/projects/PRODUCER_PROJECT/regions/REGION/subnetworks/PSC_SUBNET
    pscServiceAttachmentId:
      high: 'PSC_ATTACH_ID_HIGH'
      low: 'PSC_ATTACH_ID_LOW'
    region: https://www.googleapis.com/compute/v1/projects/PRODUCER_PROJECT/regions/REGION
    selfLink: https://www.googleapis.com/compute/v1/projects/projects/PRODUCER_PROJECT/regions/REGION/serviceAttachments/ATTACHMENT_NAME
    targetService: https://www.googleapis.com/compute/v1/projects/PRODUCER_PROJECT/regions/REGION/forwardingRules/PRODUCER_FWD_RULE
    

  2. To accept or reject consumer connections, do the following.

     * To accept or reject consumers based on project or VPC network, use the [`gcloud compute service-attachments update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/service-attachments/update).

You can specify `--consumer-accept-list` or `--consumer-reject-list`, or both. You can specify multiple values in `--consumer-accept-list` and `--consumer-reject-list`. You can include VPC projects or networks, but not a mix of both projects and networks.
           
           gcloud compute service-attachments update ATTACHMENT_NAME \
               --region=REGION \
               --consumer-accept-list=ACCEPTED_PROJECT_OR_NETWORK_1=LIMIT_1,ACCEPTED_PROJECT_OR_NETWORK_2=LIMIT_2 \
               --consumer-reject-list=REJECTED_PROJECT_OR_NETWORK_1,REJECTED_PROJECT_OR_NETWORK_2
           

Replace the following:

       * `ATTACHMENT_NAME`: the name of the service attachment.

       * `REGION`: the region where the service attachment is located.

       * `ACCEPTED_PROJECT_OR_NETWORK_1` and `ACCEPTED_PROJECT_OR_NETWORK_2`: the project IDs, project names, or network URLs to accept. `--consumer-accept-list` is optional and can contain one or more projects or networks, but not a mix of both types.

       * `LIMIT_1` and `LIMIT_2`: the connection limits for the projects or networks. The connection limit is the number of consumer endpoints that can connect to this service.

       * `REJECTED_PROJECT_OR_NETWORK_1` and `REJECTED_PROJECT_OR_NETWORK_2`: the project IDs, project names, or network URLs to reject. `--consumer-reject-list` is optional and can contain one or more projects or networks, but not a mix of both types.

     * To accept or reject individual Private Service Connect endpoints, use the [`gcloud compute service-attachments update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/service-attachments/update).
           
           gcloud compute service-attachments update ATTACHMENT_NAME \
               --region=REGION \
               --consumer-accept-list=ACCEPTED_ENDPOINT_URI_1,ACCEPTED_ENDPOINT_URI_2 \
               --consumer-reject-list=REJECTED_ENDPOINT_URI_1,REJECTED_ENDPOINT_URI_2
           

Replace the following:

       * `ACCEPTED_ENDPOINT_URI_1` and `ACCEPTED_ENDPOINT_URI_2`: the ID-based URIs of one or more Private Service Connect endpoints to accept. To find a Private Service Connect endpoint's ID-based URI, describe a connected service attachment and check the `endpointWithId` field, or describe the Private Service Connect endpoint and check the `selfLinkWithId` field. `--consumer-accept-list` is optional.

For example, the ID-based URI of the pending Private Service Connect endpoint in the example output at the beginning of this section is `https://www.googleapis.com/compute/v1/projects/CONSUMER_PROJECT_2/regions/REGION_2/forwardingRules/RESOURCE_ID_2`

       * `REJECTED_ENDPOINT_URI_1` and `REJECTED_ENDPOINT_URI_2`: the ID-based URIs of one or more Private Service Connect endpoints to reject. `--consumer-reject-list` is optional.




###  API 

  1. To describe the service attachment you want to modify, send a request to the [`serviceAttachments.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/serviceAttachments/get).

HTTP method and URL:
         
         GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/serviceAttachments/ATTACHMENT_NAME
         

Replace the following:

     * `PROJECT_ID`: the project for the service attachment.
     * `REGION`: the region for the service attachment.
     * `ATTACHMENT_NAME`: the name of the service attachment.

If there are any pending consumer connections, they are listed with status `PENDING`. The Private Service Connect endpoint's ID-based URI that you can use to accept or reject individual endpoints is displayed in the `endpointWithId` field.

Note the `fingerprint` value, which you use in the next step.

  2. To accept or reject consumer projects or networks, send a request to the [`serviceAttachments.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/serviceAttachments/patch).

You can change between accepting and rejecting consumers by project or VPC network, but you can't include a mix of both projects and networks in the same request.

     * To accept or reject consumers based on project, send the following request.

HTTP method and URL:
           
           PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/serviceAttachments/ATTACHMENT_NAME
           

Request JSON body:
           
           {
             "consumerAcceptLists": [
               {
                 "projectIdOrNum": "ACCEPTED_PROJECT_1",
                 "connectionLimit": "LIMIT_1"
               },
               {
                 "projectIdOrNum": "ACCEPTED_PROJECT_2",
                 "connectionLimit": "LIMIT_2"
               }
             ],
             "consumerRejectLists": [
               "REJECTED_PROJECT_1",
               "REJECTED_PROJECT_2"
             ],
             "fingerprint" : "FINGERPRINT"
           }
           

Replace the following:

       * `PROJECT_ID`: the project for the service attachment.
       * `REGION`: the region for the service attachment.
       * `ATTACHMENT_NAME`: the name of the service attachment.
       * `ACCEPTED_PROJECT_1` and `ACCEPTED_PROJECT_2`: the project IDs or numbers of the projects to accept. `consumerAcceptList` is optional and can contain one or more projects.
       * `LIMIT_1` and `LIMIT_2`: the connection limits for the projects. The connection limit is the number of consumer endpoints that can connect to this service.
       * `REJECTED_PROJECT_1` and `REJECTED_PROJECT_2`: the project IDs or numbers of the projects to reject. `consumerRejectList` is optional and can contain one or more projects.
       * `FINGERPRINT`: the up-to-date fingerprint for the service attachment that you found in the previous step.
     * To accept or reject consumers based on VPC network, send the following request.

HTTP method and URL:
           
           PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/serviceAttachments/ATTACHMENT_NAME
           

Request JSON body:
           
           {
             "consumerAcceptLists": [
               {
                 "networkUrl": "projects/ACCEPTED_PROJECT_ID_1/global/network/ACCEPTED_NETWORK_1",
                 "connectionLimit": "LIMIT_1"
               },
               {
                 "networkUrl": "projects/ACCEPTED_PROJECT_ID_2/global/network/ACCEPTED_NETWORK_2",
                 "connectionLimit": "LIMIT_2"
               }
             ],
             "consumerRejectLists": [
               "projects/REJECTED_PROJECT_ID_1/global/networks/REJECTED_NETWORK_1",
               "projects/REJECTED_PROJECT_ID_2/global/network/REJECTED_NETWORK_2"
             ],
             "fingerprint": "FINGERPRINT"
           }
           

Replace the following:

       * `ACCEPTED_PROJECT_ID_1` and `ACCEPTED_PROJECT_ID_2`: the IDs of the parent projects of the networks that you want to accept. `consumerAcceptLists` is optional and can contain one or more networks.
       * `ACCEPTED_NETWORK_1` and `ACCEPTED_NETWORK_2`: the names of the networks that you want to accept.
       * `LIMIT_1` and `LIMIT_2`: the connection limits for the networks. The connection limit is the number of consumer endpoints that can connect to this service.
       * `REJECTED_PROJECT_ID_1` and `REJECTED_PROJECT_ID_2`: the IDs of the parent projects of the networks that you want to reject. `consumerRejectLists` is optional and can contain one or more networks.
       * `REJECTED_NETWORK_1` and `REJECTED_NETWORK_2`: the names of the networks that you want to reject.
     * To accept or reject consumers based on individual Private Service Connect endpoints, send the following request.

HTTP method and URL:
           
           PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/serviceAttachments/ATTACHMENT_NAME
           

Request JSON body:
           
           {
             "consumerAcceptLists": [
               {
                 "endpointUrl": "ACCEPTED_ENDPOINT_URI_1"
               },
               {
                 "endpointUrl": "ACCEPTED_ENDPOINT_URI_2"
               }
             ],
             "consumerRejectLists": [
               "REJECTED_ENDPOINT_URI_1",
               "REJECTED_ENDPOINT_URI_2"
             ],
             "fingerprint": "FINGERPRINT"
           }
           

Replace the following:

       * `ACCEPTED_ENDPOINT_URI_1` and `ACCEPTED_ENDPOINT_URI_2`: the ID-based URIs of one or more Private Service Connect endpoints to accept. To find a Private Service Connect endpoint's ID-based URI, describe a connected service attachment and check the `endpointWithId` field, or describe the endpoint and check the `selfLinkWithId` field. An example ID-based URI is `https://www.googleapis.com/compute/v1/projects/consumer-project/regions/us-central1/forwardingRules/1234567890`

This list is optional.

       * `REJECTED_ENDPOINT_URI_1` and `REJECTED_ENDPOINT_URI_2`: the ID-based URIs of one or more Private Service Connect endpoints to reject. This list is optional.




## Change the connection preference for a published service

You can switch between automatic and explicit consumer acceptance for a published service. The effect that this change has on existing connections depends on whether [connection reconciliation](https://docs.cloud.google.com/vpc/docs/about-controlling-access-published-services#connection-reconciliation) is enabled for the service attachment.

If connection reconciliation is disabled, changing the connection preference doesn't affect existing `ACCEPTED` or `REJECTED` connections:

  * When you switch from automatic acceptance to explicit acceptance, new connections must be on the consumer accept list to be be `ACCEPTED`.
  * When you switch from explicit acceptance to automatic acceptance, any existing `PENDING` connections are automatically `ACCEPTED`.



If connection reconciliation is enabled, all existing connections are re-evaluated based on the new connection preference:

  * When you switch from automatic to explicit acceptance, any existing connections from consumers that are not in the consumer accept list change to `PENDING`, and those connections are terminated.
  * When you switch from explicit to automatic acceptance, all existing `PENDING` and `REJECTED` connections change to `ACCEPTED`.



For more information about updating a service's consumer accept list, see Manage requests for access to a published service.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.serviceAttachments.update`



**Roles**

See Roles for role information.

###  Console 

  1. In the Google Cloud console, go to the **Private Service Connect** page.

[Go to Private Service Connect](https://console.cloud.google.com/net-services/psc)

  2. Click the **Published services** tab.

  3. Click the service that you want to update, and then click **Edit service details**.

  4. Select the new connection preference to use for this service.

  5. Optional: If you are switching to use explicit acceptance, you can add consumers to your accept list now, or you can add them later. To accept consumers, do one of the following. You can repeat this step for each consumer that you want to add.

     * For **Accept connections for selected projects** , click **Add accepted project** , and then enter the project and connection limit.
     * For **Accept connections for selected networks** , click **Add accepted network** , and then enter the project, VPC network, and connection limit.
     * For **Accept connections for selected endpoints** , click **Add accepted endpoint** , and then enter the project and the endpoint's ID.
  6. Click **Save**.




###  gcloud 

  * To change the connection preference for the service attachment from `ACCEPT_AUTOMATIC` to `ACCEPT_MANUAL`, use the [`gcloud compute service-attachments update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/service-attachments/update).

You control which projects can connect to your service by using `--consumer-accept-list` and `--consumer-reject-list`. You can configure the accept and reject lists when you change the connection preference, or update the lists later.
        
        gcloud compute service-attachments update ATTACHMENT_NAME \
            --region=REGION \
            --connection-preference=ACCEPT_MANUAL \
            [ --consumer-accept-list=ACCEPTED_PROJECT_OR_NETWORK_1=LIMIT_1,ACCEPTED_PROJECT_OR_NETWORK_2=LIMIT_2] \
            [ --consumer-reject-list=REJECTED_PROJECT_OR_NETWORK_1,REJECTED_PROJECT_OR_NETWORK_2 ]
        

Replace the following:

    * `ATTACHMENT_NAME`: the name of the service attachment.

    * `REGION`: the region where the service attachment is located.

    * `ACCEPTED_PROJECT_OR_NETWORK_1` and `ACCEPTED_PROJECT_OR_NETWORK_2`: the project IDs, project names, or network URLs to accept. `--consumer-accept-list` is optional and can contain one or more projects or networks, but not a mix of both types.

    * `LIMIT_1` and `LIMIT_2`: the connection limits for the projects. The connection limit is the number of consumer endpoints that can connect to this service.

    * `REJECTED_PROJECT_OR_NETWORK_1` and `REJECTED_PROJECT_OR_NETWORK_2`: the project IDs, project names, or network URLs to reject. `--consumer-reject-list` is optional and can contain one or more projects or networks, but not a mix of both types.

  * To change the connection preference for the service attachment from `ACCEPT_MANUAL` to `ACCEPT_AUTOMATIC`, use the following command.

If you have values in the accept list or reject list, set them to empty when you change the connection preference (`""`).
        
        gcloud compute service-attachments update ATTACHMENT_NAME \
            --region=REGION \
            --connection-preference=ACCEPT_AUTOMATIC \
            --consumer-accept-list="" \
            --consumer-reject-list=""
        

Replace the following:

    * `ATTACHMENT_NAME`: the name of the service attachment.

    * `REGION`: the region where the service attachment is located.




###  API 

  1. To get the service attachment's `fingerprint`, send a request to the [`serviceAttachments.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/serviceAttachments/get).

HTTP method and URL:
         
         GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/serviceAttachments/ATTACHMENT_NAME
         

Replace the following:

     * `PROJECT_ID`: the project for the service attachment.
     * `REGION`: the region for the service attachment.
     * `ATTACHMENT_NAME`: the name of the service attachment.

Note the `fingerprint` value, which you use in the next step.

  2. To change the connection preference for the service attachment, send a request to the [`serviceAttachments.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/serviceAttachments/patch).

     * To change the connection preference from `ACCEPT_AUTOMATIC` to `ACCEPT_MANUAL` and update consumer accept and reject lists based on project, make the following request.

HTTP method and URL:
           
           PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/serviceAttachments/ATTACHMENT_NAME
           

Request JSON body:
           
           {
             "connectionPreference": "ACCEPT_MANUAL",
             "consumerAcceptLists": [
               {
                 "projectIdOrNum": "ACCEPTED_PROJECT_1"
                 "connectionLimit": "LIMIT_1",
               },
               {
                 "projectIdOrNum": "ACCEPTED_PROJECT_2"
                 "connectionLimit": "LIMIT_2",
               }
             ],
             "consumerRejectLists": [
               "REJECTED_PROJECT_1",
               "REJECTED_PROJECT_2",
             ],
             "fingerprint" : "FINGERPRINT"
           }
           

Replace the following:

       * `PROJECT_ID`: the project for the service attachment.
       * `REGION`: the region for the service attachment.
       * `ATTACHMENT_NAME`: the name of the service attachment.
       * `ACCEPTED_PROJECT_1` and `ACCEPTED_PROJECT_2`: the project IDs or numbers of the projects to accept. `consumerAcceptList` is optional and can contain one or more projects.
       * `LIMIT_1` and `LIMIT_2`: the connection limits for the projects. The connection limit is the number of consumer endpoints that can connect to this service.
       * `REJECTED_PROJECT_1` and `REJECTED_PROJECT_2`: the project IDs or numbers of the projects to reject. `consumerRejectList` is optional and can contain one or more projects.
       * `FINGERPRINT`: the up-to-date fingerprint for the service attachment that you found in step 1.
     * To change the connection preference from `ACCEPT_AUTOMATIC` to `ACCEPT_MANUAL` and update consumer accept and reject lists based on VPC network, make the following request.

HTTP method and URL:
           
           PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/serviceAttachments/ATTACHMENT_NAME
           

Request JSON body:
           
           {
             "connectionPreference": "ACCEPT_MANUAL",
             "consumerAcceptLists": [
               {
                 "networkUrl": "projects/ACCEPTED_PROJECT_ID_1/global/networks/ACCEPTED_NETWORK_1",
                 "connectionLimit": "LIMIT_1"
               },
               {
                 "networkUrl": "projects/ACCEPTED_PROJECT_ID_2/global/networks/ACCEPTED_NETWORK_2",
                 "connectionLimit": "LIMIT_2"
               }
             ],
             "consumerRejectLists": [
               "projects/REJECTED_PROJECT_ID_1/global/networks/REJECTED_NETWORK_1",
               "projects/REJECTED_PROJECT_ID_2/global/network/REJECTED_NETWORK_2"
             ],
             "fingerprint" : "FINGERPRINT"
           }
           

Replace the following:

       * `ACCEPTED_PROJECT_ID_1` and `ACCEPTED_PROJECT_ID_2`: the IDs of the parent projects of the networks that you want to accept. `consumerAcceptLists` is optional and can contain one or more networks.
       * `ACCEPTED_NETWORK_1` and `ACCEPTED_NETWORK_2`: the names of the networks that you want to accept.
       * `LIMIT_1` and `LIMIT_2`: the connection limits for the networks. The connection limit is the number of consumer endpoints that can connect to this service.
       * `REJECTED_PROJECT_ID_1` and `REJECTED_PROJECT_ID_2`: the IDs of the parent projects of the networks that you want to reject. `consumerRejectLists` is optional and can contain one or more networks.
       * `REJECTED_NETWORK_1` and `REJECTED_NETWORK_2`: the names of the networks that you want to reject.
       * `FINGERPRINT`: the up-to-date fingerprint for the service attachment that you found step 1.


  * To change the connection preference for the service attachment from `ACCEPT_MANUAL` to `ACCEPT_AUTOMATIC`, make the following request.

If the `consumerAcceptLists` or `consumerRejectLists` fields specify any consumers, set them to empty when you change the connection preference to `ACCEPT_AUTOMATIC`.

HTTP method and URL:
        
        PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/serviceAttachments/ATTACHMENT_NAME
        

Request JSON body:
        
        {
          "connectionPreference": "ACCEPT_AUTOMATIC",
          "consumerAcceptLists": [ ],
          "consumerRejectLists": [ ],
          "fingerprint" : "FINGERPRINT"
        }
        

Replace the following:

    * `PROJECT_ID`: the project for the service attachment.

    * `REGION`: the region for the service attachment.

    * `ATTACHMENT_NAME`: the name of the service attachment.

    * `FINGERPRINT`: the up-to-date fingerprint for the service attachment that you found step 1.




## Remove obsolete endpoints from consumer lists

If your consumer accept and reject lists are configured to use individual endpoints, a value can remain in the lists after a consumer deletes the corresponding endpoint. To simplify the management of your consumer lists, you can use the [`gcloud compute service-attachments update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/service-attachments/update) to remove values for any endpoints that no longer exist. This feature is only supported for the Google Cloud CLI.

###  gcloud 
    
    
    gcloud compute service-attachments update ATTACHMENT_NAME \
        --region=REGION \
        --remove-obsolete-endpoint-accept-reject-entries
    

Replace the following:

  * `ATTACHMENT_NAME`: the name of the service attachment to update.
  * `REGION`: the region for the service attachment.



## Configure connection reconciliation

You can enable or disable [connection reconciliation](https://docs.cloud.google.com/vpc/docs/about-controlling-access-published-services#connection-reconciliation) for existing service attachments.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.serviceAttachments.update`



**Roles**

See Roles for role information.

###  Console 

  1. In the Google Cloud console, go to the **Private Service Connect** page.

[Go to Private Service Connect](https://console.cloud.google.com/net-services/psc)

  2. Click the **Published services** tab.

  3. Click the service that you want to update, and then click **Edit service details**.

  4. Select or clear the **Enable connection reconciliation** checkbox, and then click **Save**.




###  gcloud 

  * To enable connection reconciliation, use the [`service-attachments update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/service-attachments/update).
        
        gcloud compute service-attachments update ATTACHMENT_NAME \
            --region=REGION \
            --reconcile-connections
        

Replace the following:

    * `ATTACHMENT_NAME`: the name of the service attachment.
    * `REGION`: the region of the service attachment.
  * To disable connection reconciliation, use the following command:
        
        gcloud compute service-attachments update ATTACHMENT_NAME \
            --region=REGION \
            --no-reconcile-connections
        




###  API 

  1. To get the service attachment's `fingerprint`, send a request to the [`serviceAttachments.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/serviceAttachments/get).

HTTP method and URL:
         
         GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/serviceAttachments/ATTACHMENT_NAME
         

Replace the following:

     * `PROJECT_ID`: the project for the service attachment.
     * `REGION`: the region for the service attachment.
     * `ATTACHMENT_NAME`: the name of the service attachment.

Note the `fingerprint` value, which you use in the next step.

  2. Send a request to the [`serviceAttachments.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/serviceAttachments/patch).

HTTP method and URL:
         
         PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/serviceAttachments/ATTACHMENT_NAME
         

Request JSON body:
         
         {
           "reconcileConnections": RECONCILIATION,
           "fingerprint": "FINGERPRINT"
         }
         

Replace the following:

     * `PROJECT_ID`: the project for the service attachment.
     * `REGION`: the region for the service attachment.
     * `ATTACHMENT_NAME`: the name of the service attachment.
     * `RECONCILIATION`: whether to enable connection reconciliation. Options are `true` or `false`.
     * `FINGERPRINT`: the up-to-date fingerprint for the service attachment that you found in the previous step.



## Add or remove subnets from a published service

You can edit a published service to add Private Service Connect subnets.

For example, you might need to make more IP addresses available for an existing service. To add more addresses, do one of the following:

  * [Create another Private Service Connect subnet](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer#add-subnet-psc), and edit the service attachment to add the new subnet.

  * Edit the subnet to [expand the IPv4 range](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#expand-subnet).




Similarly, you can edit a published service to remove Private Service Connect subnets. However, if any of the subnet's IP addresses are being used to perform SNAT for Private Service Connect, removing the subnet fails.

If you change the subnet configuration, update your [firewall rules](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer#firewall-rules) to allow requests from the new subnets to reach the backend VMs.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.serviceAttachments.update`



**Roles**

See Roles for role information.

###  Console 

  1. In the Google Cloud console, go to the **Private Service Connect** page.

[Go to Private Service Connect](https://console.cloud.google.com/net-services/psc)

  2. Click the **Published services** tab.

  3. Click the service that you want to update, and then click **Edit service details**.

  4. Modify the subnets used for this service.

If you want to add a new subnet, you can create one:

     1. Click **Reserve new subnet**.
     2. Enter a **Name** and optional **Description** for the subnet.
     3. Select a **Region** for the subnet.
     4. Enter the **IP range** to use for the subnet and click **Add**.
  5. Click **Save**.




###  gcloud 

To update the Private Service Connect subnets that are used for this service attachment, use the [`gcloud compute service-attachments update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/service-attachments/update).
    
    
    gcloud compute service-attachments update ATTACHMENT_NAME \
        --region=REGION \
        --nat-subnets=PSC_SUBNET_LIST
    

Replace the following:

  * `ATTACHMENT_NAME`: the name of the service attachment.

  * `REGION`: the region where the service attachment is located.

  * `PSC_SUBNET_LIST`: a comma-separated list of one or more subnets to use with this service attachment.




###  API 

  1. To get the service attachment's `fingerprint`, send a request to the [`serviceAttachments.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/serviceAttachments/get).

HTTP method and URL:
         
         GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/serviceAttachments/ATTACHMENT_NAME
         

Replace the following:

     * `PROJECT_ID`: the project for the service attachment.
     * `REGION`: the region for the service attachment.
     * `ATTACHMENT_NAME`: the name of the service attachment.

Note the `fingerprint` value, which you use in the next step.

  2. To update the Private Service Connect subnets that are used for this service attachment, send a request to the [`serviceAttachments.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/serviceAttachments/patch).

HTTP method and URL:
         
         PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/serviceAttachments/ATTACHMENT_NAME
         

Request JSON body:
         
         {
           "natSubnets": [
           "PSC_SUBNET1_URI",
           "PSC_SUBNET2_URI"
           ],
           "fingerprint": "FINGERPRINT"
         }
         

Replace the following:

     * `PROJECT_ID`: the project for the service attachment.

     * `REGION`: the region for the service attachment.

     * `ATTACHMENT_NAME`: the name of the service attachment.

     * `PSC_SUBNET1_URI` and `PSC_SUBNET2_URI`: URIs of the subnets that you want to use with this service attachment. You can specify one or more subnets.

     * `FINGERPRINT`: the up-to-date fingerprint for the service attachment that you found in the previous step.




## Update the number of NAT IP addresses per endpoint

You can update a service attachment to increase the number of NAT IP addresses allocated per consumer endpoint or backend from `1` to `2`. When you do this, the NAT IP addresses that are already allocated aren't affected. You can't decrease the number of NAT IP addresses.

Increasing this value can increase the maximum number of simultaneous IPv4 connections per endpoint or backend, if the producer backend VMs have enough vCPUs. For more information, see [Maximum connections](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#max-connections).

The service attachment's NAT subnets must have enough capacity to allocate additional IP addresses for each accepted endpoint (including propagated endpoint connections) and backend.

If the NAT subnets don't have enough available IP addresses, the update fails with the following error:

`Insufficient IPv4 capacity on NAT subnetworks for the requested Service Attachment update.`

In this case, you must add or expand a NAT subnet before retrying the update.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.serviceAttachments.update`



**Roles**

See Roles for role information.

###  Console 

  1. In the Google Cloud console, go to the **Private Service Connect** page.

[Go to Private Service Connect](https://console.cloud.google.com/net-services/psc)

  2. Click the **Published services** tab.

  3. Click the service that you want to update, and then click **Edit service details**.

  4. Click **Allocated IPs per PSC endpoint** , and then select **2**.

  5. Click **Save**.




###  gcloud 

To increase the number of NAT IP addresses per endpoint for an existing service attachment, use the [`gcloud compute service-attachments update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/service-attachments/update).
    
    
    gcloud compute service-attachments update ATTACHMENT_NAME \
        --region=REGION \
        --nat-ips-per-endpoint=2
    

Replace the following:

  * `ATTACHMENT_NAME`: the name of the service attachment to update.
  * `REGION`: the region of the service attachment.



###  API 

  1. To get the service attachment's `fingerprint`, send a request to the [`serviceAttachments.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/serviceAttachments/get).
         
         GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/serviceAttachments/ATTACHMENT_NAME
         

Replace the following:

     * `PROJECT_ID`: the project ID for the service attachment.
     * `REGION`: the region for the service attachment.
     * `ATTACHMENT_NAME`: the name of the service attachment.
  2. Send a `PATCH` request to the [`serviceAttachments.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/serviceAttachments/patch).
         
         PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/serviceAttachments/ATTACHMENT_NAME
         {
           "natIpsPerEndpoint": 2,
           "fingerprint": "FINGERPRINT"
         }
         

Replace `FINGERPRINT` with the up-to-date fingerprint for the service attachment that you found in the previous step.




## Update target service

For supported configurations, you can update a service attachment to target a different service. For information about supported configurations and limitations, see [Service mutability](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#service-mutability).

When you update a target service, traffic is disrupted for a short time. However, consumers aren't automatically notified that the service is down, and updating a target service doesn't affect the [connection statuses](https://docs.cloud.google.com/vpc/docs/about-controlling-access-published-services#statuses) of connected consumers.

### Prepare for the update

The steps in the following sections are optional. In most cases, you can skip to the Update the service attachment section, unless you want to do the following:

  * If you want to explicitly signal downtime to consumers by updating connection statuses to `REJECTED`, complete the steps in the Signal downtime to consumers section.
  * If you want to create a test instance to verify when connectivity to the service is restored, complete the steps in the Prepare a test consumer section.



#### Signal downtime to consumers during an update

To explicitly inform consumers that the service is unavailable, complete the following optional steps:

  1. Make sure that connection reconciliation is enabled for the service attachment.
  2. Add all consumers from the accept list to the reject list. This changes the connection statuses to `REJECTED`.
  3. After the update is complete, remove the consumers from the reject list to transition connection statuses back to `ACCEPTED`.



#### Prepare a test consumer

To verify when connectivity to the service is restored, you can optionally send probe packets to the service from a test instance. To set up the test, do the following:

  1. [Create a test VPC network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#creating_networks) in your project.
  2. In the test VPC network, do the following: 
     * [Create a Private Service Connect endpoint](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#create-endpoint) that connects to your service attachment.
     * [Create a test instance](https://docs.cloud.google.com/compute/docs/create-linux-vm-instance).
  3. Prepare one of the following ways to test the connection: 
     * Set up Connectivity Tests to [test connectivity between your test VM and the endpoint](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests#testing-psc). You can retry this test after the update to determine when connectivity is restored.
     * If you want to send probe packets manually, [connect to the test instance](https://docs.cloud.google.com/compute/docs/connect/standard-ssh#connect_to_vms) and verify that you can reach the endpoint's IP address using a tool such as `curl`.



### Update the service attachment

To update the service attachment's target service, do the following.

To update to or from an internal protocol forwarding target service, you must use the gcloud CLI or send an API request.

###  Console 

  1. In the Google Cloud console, go to the **Private Service Connect** page.

[Go to Private Service Connect](https://console.cloud.google.com/net-services/psc)

  2. Click the **Published services** tab.

  3. Click the service that you want to update.

  4. Click **Edit service details**.

  5. Select the load balancer type of your new target service.

  6. Select the forwarding rule of your new target service.

  7. Click **Save**.




###  gcloud 

Use the [`gcloud compute service-attachments update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/service-attachments/update).
    
    
    gcloud compute service-attachments update ATTACHMENT_NAME \
        --region=REGION \
        --target-service=TARGET_SERVICE
    

Replace the following:

  * `ATTACHMENT_NAME`: the name of the service attachment to update.
  * `REGION`: the region of the service attachment.
  * `TARGET_SERVICE`: the URI of the new target service, in the following format: `projects/PROJECT_ID/regions/RULE_REGION/forwardingRules/RULE_NAME`



###  API 

  1. To get the service attachment's `fingerprint`, send a request to the [`serviceAttachments.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/serviceAttachments/get).

HTTP method and URL:
         
         GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/serviceAttachments/ATTACHMENT_NAME
         

Replace the following:

     * `PROJECT_ID`: the project for the service attachment.
     * `REGION`: the region for the service attachment.
     * `ATTACHMENT_NAME`: the name of the service attachment.

Note the `fingerprint` value, which you use in the next step.

  2. Send a request to the [`serviceAttachments.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/serviceAttachments/patch).

HTTP method and URL:
         
         PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/serviceAttachments/ATTACHMENT_NAME
         

Request JSON body:
         
         {
           "targetService": "TARGET_SERVICE",
           "fingerprint": "FINGERPRINT"
         }
         

Replace the following:

     * `TARGET_SERVICE`: the URI of the new target service, in the following format: `projects/PROJECT_ID/regions/RULE_REGION/forwardingRules/RULE_NAME`
     * `FINGERPRINT`: the up-to-date fingerprint for the service attachment that you found in the previous step.



### Verify the update and restore access

If you created a test VPC network and instance, verify that the update is complete and the service is available. This step is optional. Do one of the following:

  * If you created a test with Connectivity Tests, [rerun the test](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests#rerunning-tests). When the [live data plane analysis](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#live-data-plane) for a test shows that all packets were successfully delivered, the update is complete.
  * Manually send probe packets from the test instance to the target service. When the instance successfully receives responses, the update is complete.



When connectivity has resumed, do the following:

  1. If you added consumers to the reject list, remove them from the reject list to signal that the service is available.
  2. If you created resources to verify when the update is complete, follow these steps to delete the resources and avoid unnecessary charges: 
     1. [Delete the test instance](https://docs.cloud.google.com/compute/docs/instances/deleting-instance#delete-vms)
     2. [Delete the test Private Service Connect endpoint](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#delete-endpoint)
     3. [Delete the test VPC network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#deleting_a_network)



## Update the propagated connection limit of a published service

You can update the [propagated connection limit](https://docs.cloud.google.com/vpc/docs/about-controlling-access-published-services#propagated-connection-limit) of a service attachment. When you increase the limit, Google Cloud automatically checks if any pending propagated connections can be created. When you decrease the limit, existing propagated connections are unaffected. However, attempts to reestablish deleted or rejected propagated connections might be blocked if the new limit is reached.

###  Console 

  1. In the Google Cloud console, go to the **Private Service Connect** page.

[Go to Private Service Connect](https://console.cloud.google.com/net-services/psc)

  2. Click the **Published services** tab.

  3. Click the service that you want to update, and then click **Edit service details**.

  4. Click **Advanced configuration**.

  5. Enter the new **NCC propagated connections limit**.




###  gcloud 

Use the [`gcloud compute service-attachments update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/service-attachments/update).
    
    
    gcloud compute service-attachments update ATTACHMENT_NAME \
        --region=REGION \
        --propagated-connection-limit=LIMIT
    

Replace the following:

  * `ATTACHMENT_NAME`: the name of the service attachment.

  * `REGION`: the region where the service attachment is located.

  * `LIMIT`: the new value for the propagated connection limit.




###  API 

  1. To get the service attachment's `fingerprint`, send a request to the [`serviceAttachments.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/serviceAttachments/get).

HTTP method and URL:
         
         GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/serviceAttachments/ATTACHMENT_NAME
         

Replace the following:

     * `PROJECT_ID`: the project for the service attachment.
     * `REGION`: the region for the service attachment.
     * `ATTACHMENT_NAME`: the name of the service attachment.

Note the `fingerprint` value, which you use in the next step.

  2. Send a request to the [`serviceAttachments.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/serviceAttachments/patch).

HTTP method and URL:
         
         PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/serviceAttachments/ATTACHMENT_NAME
         

Request JSON body:
         
         {
           "propagatedConnectionLimit": LIMIT,
           "fingerprint": "FINGERPRINT"
         }
         

Replace the following:

     * `PROJECT_ID`: the project for the service attachment.

     * `REGION`: the region for the service attachment.

     * `ATTACHMENT_NAME`: the name of the service attachment.

     * `LIMIT`: the new value for the propagated connection limit.

     * `FINGERPRINT`: the up-to-date fingerprint for the service attachment that you found in the previous step.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
