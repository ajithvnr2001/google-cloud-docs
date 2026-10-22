---
url: https://docs.cloud.google.com/intrusion-detection-system/docs/configuring-ids/
title: Configure Cloud IDS \u00a0|\u00a0 Cloud Intrusion Detection System \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:31.333947+00:00
---

# Configure Cloud IDS  |  Cloud Intrusion Detection System  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/intrusion-detection-system/docs/configuring-ids/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud IDS ](https://docs.cloud.google.com/intrusion-detection-system/docs)
  * [ Guides ](https://docs.cloud.google.com/intrusion-detection-system/docs/overview)



Send feedback 

#  Configure Cloud IDS Stay organized with collections  Save and categorize content based on your preferences. 

This document helps you configure Cloud Intrusion Detection System (Cloud IDS) to secure your network traffic and detect threats. This set up lets you monitor Virtual Private Cloud (VPC) communication for malicious activity without impacting network performance. To configure Cloud IDS, you must set up Identity and Access Management (IAM) permission, enable private services access, create endpoints, and configure packet mirroring. For more information, see [Cloud IDS overview](https://docs.cloud.google.com/intrusion-detection-system/docs/overview).

## Before you begin

Before you configure Cloud IDS, you must complete the following requirements.

### Set up IAM permissions for Cloud IDS

Cloud IDS has several IAM roles. You can use the example commands to grant a principal the necessary IAM permissions.

  * **Cloud IDS Admin role (`roles/ids.admin`).** Project principals with this role can create IDS endpoints. If you are a project owner, you already have this permission and don't need an explicit `ids.admin` role to create IDS endpoints.
        
        gcloud projects add-iam-policy-binding PROJECT_ID \
            --role=roles/ids.admin \
            --member=user:USER_NAME ;
        

This role enables the following operations:

    * Create endpoint
    * Delete endpoint
    * Get endpoint
    * List endpoint
  * **Cloud IDS Viewer role (`roles/ids.viewer`).** Project viewers and principals with this role have read-only access to IDS endpoints. If you are a project owner, editor, or viewer, you already have this permission.
        
        gcloud projects add-iam-policy-binding PROJECT_ID \
            --role=roles/ids.viewer \
            --member=user:USER_NAME ;
        

  * **Compute packet mirroring user role (`roles/compute.packetMirroringUser`).** A role needed to attach a packet mirroring policy to the IDS endpoint. If you have the `compute.securityAdmin` or `container.serviceAgent` role, you already have this permission. For more information about this role, see the [IAM basic and predefined roles reference](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.packetMirroringUser).
        
        gcloud projects add-iam-policy-binding PROJECT_ID \
            --role=roles/compute.packetMirroringUser \
            --member=user:USER_NAME ;
        

  * **Logs Viewer role (`roles/logging.viewer`).** An additional role needed to view recent threats, which is a critical core feature of Cloud IDS. For more information about this role, see the [Access control guide](https://docs.cloud.google.com/logging/docs/access-control#permissions_and_roles).
        
        gcloud projects add-iam-policy-binding PROJECT_ID \
            --role=roles/logging.viewer \
            --member=user:USER_NAME ;
        




In addition, you need the following miscellaneous permissions:

  * `compute.regions.list`
  * `compute.zones.list`



### Set up private services access

To create IDS endpoints, you must enable the Service Networking API, and set up network peering for the Virtual Private Cloud (VPC) network. This only needs to be done once per customer project and can be done by using the Google Cloud console or the Google Cloud CLI. When you allocate an IP address range, it must be an RFC 1918-compliant private IP address range (`10.0.0.0/8`, `172.16.0.0/12`, or `192.168.0.0/16`), or endpoint creation fails.

Use the following steps to set up private services access:

  1. Enable the Service Networking API by using the following command. Replace `PROJECT_ID` with your project ID.
         
         gcloud services enable servicenetworking.googleapis.com \
              --project=PROJECT_ID
         

  2. Allocate an IP range for Google services in your VPC network. If you have already configured private services access for another service, you must allocate a separate, unique IP address range for Cloud IDS.

In the following command, you can omit the `addresses` field and Google Cloud selects an unused address range in your VPC network:
         
         gcloud compute addresses create RESERVED_RANGE_NAME \
              --global \
              --purpose=VPC_PEERING \
              --addresses=192.168.0.0 \
              --prefix-length=16 \
              --description="DESCRIPTION" \
              --network=VPC_NETWORK
         

Replace the following:

     * `RESERVED_RANGE_NAME`: a name for the allocated range, such as `my-allocated-range`

     * `DESCRIPTION`: a description for the range, such as `allocated for my-service`

     * `VPC_NETWORK`: the name of your VPC network, such as `my-vpc-network`

  3. Create a private connection to a service producer. The private connection establishes a [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering) connection between your VPC network and the service producer's network.

If you already have an existing private connection, use the [`gcloud services vpc-peerings update` command](https://docs.cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/update) to update it with the additional range that you allocated for Cloud IDS:
         
         gcloud services vpc-peerings update \
               --service=servicenetworking.googleapis.com \
               --ranges=RESERVED_RANGE_NAME \
               --network=VPC_NETWORK \
               --project=PROJECT_ID
         

If you don't already have a private connection, use the [`gcloud services vpc-peerings connect` command](https://docs.cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/connect). This command initiates a long-running operation that returns an operation name.
         
         gcloud services vpc-peerings connect \
               --service=servicenetworking.googleapis.com \
               --ranges=RESERVED_RANGE_NAME \
               --network=VPC_NETWORK \
               --project=PROJECT_ID
         

Replace the following:

     * `RESERVED_RANGE_NAME`: the name of one or more allocated ranges

     * `VPC_NETWORK`: the name of your VPC network

     * `PROJECT_ID`: the ID of the project that contains your VPC network

To check whether the operation was successful, use the [`gcloud services vpc-peerings operations describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/operations/describe):
    
    gcloud services vpc-peerings operations describe \
          --name=OPERATION_NAME
    

Replace `OPERATION_NAME` with the operation name that was returned from the previous step.




Repeat steps 2 and 3 for each VPC network that you want to monitor.

### Optional: Enable VPC Service Controls

After private services access is enabled, you can optionally enable [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) on Cloud IDS. If enabled, run the [`services vpc-peerings enable-vpc-service-controls` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/services/vpc-peerings/enable-vpc-service-controls) to enable VPC Service Controls for all your peering connections:
    
    
    gcloud services vpc-peerings enable-vpc-service-controls \
        --service=servicenetworking.googleapis.com \
        --network=VPC_NETWORK \
        --project=PROJECT_ID
    

Replace the following:

  * `VPC_NETWORK`: the name of your VPC network

  * `PROJECT_ID`: the ID of the project that contains your VPC network




### Understand best practices

We recommend that you understand the best practices before you configure Cloud IDS. For more information, see [Best practices for Cloud IDS](https://docs.cloud.google.com/intrusion-detection-system/docs/best-practice).

## Configure Cloud IDS endpoints

The following sections explain how to create Cloud IDS endpoints, attach them to a Packet Mirroring policy, view the Cloud IDS endpoints, delete the Cloud IDS endpoints, and how to configure threat exceptions.

### Create a Cloud IDS endpoint

We recommend that you create an IDS endpoint for every region in which you have deployed workloads. You can also create multiple IDS endpoints per region. Use the following steps to create an IDS endpoint and assign it an IDS service profile.

###  Console

In the Google Cloud console, go to **IDS Endpoints**.

[Go to IDS Endpoints](https://console.cloud.google.com/net-security/ids/list)

#### Configure the endpoint:

  1. Click **Create endpoint**.
  2. Enter a name in the **Endpoint name** field.
  3. Optional: Enter a description in the **Description** field.
  4. Click the **Network** list, and select the network that you want Cloud IDS to inspect. 
     1. Choose the region and zone of your network or subnet from the **Region** and **Zone** lists.
     2. Click **Continue**.



#### Select the Cloud IDS service profile:

  1. Click **Select IDS service profile**.
  2. Under **Minimum threat severity level** , select the correct alert level.
  3. Click **Create**. The creation process can take 10-15 minutes.



###  gcloud 

#### Optional flags

The commands in this section might have some or all of the following optional flags:

`--no-async`
     Wait for the operation in progress to complete, rather than returning immediately. 
`--filter=EXPRESSION`
    Apply a Boolean filter EXPRESSION to each resource item to be listed. If the expression evaluates True, then that item is listed. For more details and examples of filter expressions, run the [`gcloud topic filters` command](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters). This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`.
`--limit=LIMIT`
    The maximum number of resources to list. The default is unlimited. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`.
`--page-size=PAGE_SIZE`
    Cloud IDS groups resource-list output into pages. This flag specifies the maximum number of resources per page. The default is determined by the service if it supports paging; otherwise, it is unlimited (no paging). Paging can be applied before or after the `--filter` and `--limit` flags, depending on the service.
`--sort-by=[FIELD,…]`
    A comma-separated list of resource field key names to sort by. The default order is ascending. Prefix a field with a tilde (`~`) for descending order on that field. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`.
`--uri`
    Print a list of resource URIs instead of the default output.
`--threat-exceptions`
    A comma-separated list of threat IDs to exempt from alerting on this endpoint. Limited to 99 exceptions per endpoint.

#### Instructions

To create a new IDS endpoint, use the [`gcloud ids endpoints create` command](https://docs.cloud.google.com/sdk/gcloud/reference/ids/endpoints/create).
    
    
     gcloud ids endpoints create ENDPOINT_NAME \
         --network=VPC_NETWORK \
         --zone=ZONE \
         --severity=SEVERITY \
         [--no-async] \
         [GCLOUD_WIDE_FLAG...]
    

Replace the following:

  * `ENDPOINT_NAME`: the name or ID of the endpoint.
  * `VPC_NETWORK`: the name of your VPC network.
  * `ZONE`: the zone of the endpoint.
  * `SEVERITY`: the minimum severity of threats to report on.

The severity flag is required, and takes one of the following values:

    * `INFORMATIONAL`
    * `LOW`
    * `MEDIUM`
    * `HIGH`
    * `CRITICAL`



###  API 

Cloud IDS endpoint resources have the following fields: 

Field | Type | Field description  
---|---|---  
createTime | string | [Output only] Creation timestamp in RFC 3339 text format.  
updateTime | string | [Output only] Last update timestamp in RFC 3339 text format.  
name | string | [Output only] Name of the endpoint in the format `projects/{project_id}/locations/{locationId}/endpoints/{endpointId}`.  
network | string | Name of the VPC network that is connected to the IDS endpoint. This can either contain the VPC network name itself (like `"src-net"`) or the full URL to the network (like `"projects/{project_id}/global/networks/src-net"`). This field is required when creating the endpoint.  
severity | string | The minimum alert severity level that is reported by the endpoint. Possible values are as follows:

  * `INFORMATIONAL`
  * `LOW`
  * `MEDIUM`
  * `HIGH`
  * `CRITICAL`

This field is required when creating the endpoint.  
description | string | An optional description of the endpoint.  
endpoint_forwarding_rule | string | [Output only] URL of the endpoint's network address to which traffic is to be sent by Packet Mirroring.  
endpoint | string | [Output only] Internal IP address of the endpoint's network entry point.  
  
To create a Cloud IDS endpoint, use an HTTP POST request like the following, replacing variables as appropriate. The `ENDPOINT_NAME` must be between 1-63 characters; must only contain lowercase letters, digits, and hyphens; must start with a lowercase letter; and cannot end with a hyphen.
    
    
    POST https://ids.googleapis.com/v1/projects/PROJECT_NAME/locations/ZONE/endpoints?endpointId=ENDPOINT_NAME
    {
      "network": "NETWORK_NAME",
      "severity": "SEVERITY_LEVEL",
    }
    

**Important:** After your endpoint is created, you must attach a packet mirroring policy to it to begin inspecting traffic.

### Attach a Packet Mirroring policy to a Cloud IDS endpoint

Use the following steps to attach a Packet Mirroring policy to the IDS endpoint.

###  Console

After the IDS endpoint is created, attach a Packet Mirroring policy to the IDS endpoint:

  1. In the Google Cloud console, go to **IDS Endpoints**.

[Go to IDS Endpoints](https://console.cloud.google.com/net-security/ids/list)

  2. Next to the IDS endpoint, click **Attach**.

  3. In the **Policy name** field, enter a name for the Packet Mirroring policy.

  4. Click **Next**.

  5. Choose the subnet or instances to mirror. You can select multiple subnets and instances.

  6. Click **Next**.

  7. Determine whether you want to mirror all traffic or filter traffic:

     1. If you want to mirror all traffic, ensure that **Mirror All Traffic** is selected.
     2. If you want to filter traffic based on protocol, IP address range, or ingress or egress traffic, select **Mirror filtered traffic** : 
        1. Select either **Allow all protocols** or **Allow specific protocols**.
        2. Select either **Allow all IP ranges** or **Allow specific IP ranges**.
  8. Click **Submit**. The endpoint is created.




###  gcloud 

  1. After the endpoint has been created, attach a Packet Mirroring policy to it. First, obtain the URL from the `endpoint_forwarding_rule` field by using the following command:
         
         gcloud ids endpoints describe ENDPOINT_NAME
         

  2. Create the Packet Mirroring policy by using the following command:
         
         gcloud compute packet-mirrorings create POLICY_NAME \
              --region=REGION \
              --collector-ilb=ENDPOINT_FORWARDING_RULE \
              --network=VPC_NETWORK \
              --mirrored-subnets=SUBNET
         

  3. Packet Mirroring has several optional flags, including those that you can use to filter traffic based on protocol, IP address range, or ingress or egress traffic. For more information about these optional flags, see the [Packet Mirroring reference](https://docs.cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/create).




### Describe a Cloud IDS endpoint

Use the following steps to describe an IDS endpoint.

###  Console

  1. In the Google Cloud console, go to **IDS Endpoints**.

[Go to IDS Endpoints](https://console.cloud.google.com/net-security/ids/list)

  2. On the **IDS Endpoints** page, click the name of the IDS endpoint. The **Endpoint details** page is displayed.




###  gcloud 

To describe an IDS endpoint, use the [`gcloud ids endpoints describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/ids/endpoints/describe).
    
    
    gcloud ids endpoints describe ENDPOINT_NAME \
        [--project=PROJECT_ID] \
        [--zone=ZONE] \
        [GCLOUD_WIDE_FLAG...]
    

Replace the following:

  * `ENDPOINT_NAME`: the name or ID of the endpoint.
  * `PROJECT_ID`: the ID of the project.
  * `ZONE`: the zone of the endpoint.



###  API 

To get a Cloud IDS endpoint, use an `HTTP GET` request like the following, replacing variables as appropriate:
    
    
    GET https://ids.googleapis.com/v1/projects/PROJECT_NAME/locations/ZONE/endpoints?endpointId=ENDPOINT_NAME
    

### List Cloud IDS endpoints

Use the following steps to list all IDS endpoints.

###  Console

  1. In the Google Cloud console, go to **IDS Endpoints**.

[Go to IDS Endpoints](https://console.cloud.google.com/net-security/ids/list)




###  gcloud 

To list IDS endpoints, use the [`gcloud ids endpoints list` command](https://docs.cloud.google.com/sdk/gcloud/reference/ids/endpoints/list):
    
    
    gcloud ids endpoints list \
        [--filter=EXPRESSION] \
        [--limit=LIMIT] \
        [--page-size=PAGE_SIZE] \
        [--sort-by=[FIELD,...]] \
        [--uri] \
        [GCLOUD_WIDE_FLAG...]
    

Replace the following:

  * `EXPRESSION`: apply a Boolean filter to each resource item to be listed. If the expression evaluates True, then that item is listed.
  * `LIMIT`: the maximum number of resources to list.
  * `PAGE_SIZE`: the maximum number of resources per page.
  * `FIELD`: a comma-separated list of resource field key names to sort by.



###  API 

To list all Cloud IDS endpoints in a zone, use an `HTTP GET` request like the following, replacing variables as appropriate:
    
    
    GET https://ids.googleapis.com/v1/projects/PROJECT_NAME/locations/ZONE/endpoints
    

Alternatively, to list all Cloud IDS endpoints in all zones, you can replace the `ZONE` with a hyphen like the following:
    
    
    GET https://ids.googleapis.com/v1/projects/PROJECT_NAME/locations/-/endpoints
    

### Delete a Cloud IDS endpoint

Use the following steps to delete an IDS endpoint.

**Note:** An endpoint needs to be deleted in order to stop charges associated with Cloud IDS.

###  Console

  1. In the Google Cloud console, go to **IDS Endpoints**.

[Go to IDS Endpoints](https://console.cloud.google.com/net-security/ids/list)

  2. On the **IDS Endpoints** page, click the name of the IDS endpoint. The **Endpoint details** page is displayed.

  3. Click delete**Delete Endpoint**.




###  gcloud 

To delete an IDS endpoint, use the [`gcloud ids endpoints delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/ids/endpoints/delete).
    
    
    gcloud ids endpoints delete ENDPOINT_NAME \
        [--project=PROJECT_ID] \
        [--zone=ZONE] \
        [--no-async] \
        [GCLOUD_WIDE_FLAG...]
    

Replace the following:

  * `ENDPOINT_NAME`: the name or ID of the endpoint.
  * `PROJECT_ID`: the ID of the project.
  * `ZONE`: the zone of the endpoint.



###  API 

To delete a Cloud IDS endpoint, use an `HTTP DELETE` request like the following, replacing variables as appropriate:
    
    
    DELETE https://ids.googleapis.com/v1/projects/PROJECT_NAME/locations/ZONE/endpoints?endpointId=ENDPOINT_NAME
    

### Optional: Configure threat exceptions

You can disable noisy or otherwise unnecessary threat IDs by using the `--threat-exceptions` flag when you create or update your Cloud IDS endpoint. The following example updates an existing Cloud IDS endpoint `ENDPOINT_NAME` to exempt the threat IDs `THREAT_ID1` and `THREAT_ID2`:
    
    
    gcloud ids endpoints update ENDPOINT_NAME \
        --threat-exceptions=THREAT_ID1,THREAT_ID2
    

## View threat logs

Use the following steps to check to see if any threat logs have been generated.

  1. In the Google Cloud console, go to **IDS Threats**.

[Go to IDS Threats](https://console.cloud.google.com/net-security/ids/threats)

  2. Click a threat name to view the **Threat details** page for that threat.

  3. Return to the **Threats** tab.

  4. Click the more_vert**Menu** to the right of your IDS endpoint, and select **View threat logs**.




## What's next

  * [Examine logs](https://docs.cloud.google.com/intrusion-detection-system/docs/logging)
  * [Troubleshoot issues](https://docs.cloud.google.com/intrusion-detection-system/docs/troubleshooting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
