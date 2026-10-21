---
url: https://docs.cloud.google.com/oracle/database/docs/configure-vpc-service-controls/
title: Configure VPC Service Controls \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:26:11.005761+00:00
---

# Configure VPC Service Controls  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/configure-vpc-service-controls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  Configure VPC Service Controls Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how you can use VPC Service Controls to secure Oracle Database@Google Cloud resources. VPC Service Controls let you create a service perimeter that protects the resources and data of the services that you specify.

Using VPC Service Controls provides the following advantages:

  * Protecting against the risk of data exfiltration
  * Preventing data leakage by restricting access to resources, except those specifically allowed in the ingress and egress rules
  * Providing an extra layer of security against misconfigured Identity and Access Management (IAM) policies



For more information about VPC Service Controls, its security benefits, and its capabilities, see [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

This guide also explains how you can use VPC Service Controls with [Google Cloud CMEK](https://docs.cloud.google.com/oracle/database/docs/cmek).

## Limitations

**Note:** The following limitation is applicable only to Exadata VM Clusters and Exascale VM Clusters.

Enabling VPC Service Controls perimeter before creating an Exadata VM Cluster or an Exascale VM Cluster might cause service account attachment to fail, and log a VPC Service Controls violation. Additionally, if VPC Service Controls perimeter is enabled after creating an Exadata VM Cluster or Exascale VM Cluster, VPC Service Controls violation error might be logged continuously. These VPC Service Controls violation errors (with Google-managed Workload Identity pool in the `principalSubject` of the audit log) don't affect the functionality of Oracle Database@Google Cloud, and can be safely ignored. This is applicable only if you use Oracle-managed encryption keys.

## Before you begin

  * Set up your [Oracle Database@Google Cloud environment](https://docs.cloud.google.com/oracle/database/docs/setup-oracle-database-environment).
  * Grant the [IAM roles and permissions](https://docs.cloud.google.com/vpc-service-controls/docs/access-control) required to create service perimeters.
  * [Create an access policy](https://docs.cloud.google.com/access-context-manager/docs/create-access-policy), if you don't already have one.
  * Enable the Compute Engine API.

[Enable the Compute Engine API](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com)

  * Enable the Service Networking API.

[Enable the Service Networking API](https://console.cloud.google.com/apis/enableflow?apiid=servicenetworking.googleapis.com)

  * Review [limitations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_oracle_database) when you use VPC Service Controls with Oracle Database@Google Cloud.

  * Additionally, to use [Google Cloud CMEK](https://docs.cloud.google.com/oracle/database/docs/cmek) along with VPC Service Controls for your resources, enable [Private Google Access](https://docs.cloud.google.com/vpc-service-controls/docs/private-connectivity) on all database subnets. This is required to access `iamcredentials.googleapis.com` and `cloudkms.googleapis.com`.

For more information, see [Configure Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access).




## Create a service perimeter

To create a service perimeter, follow the instructions in [Create a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters).

If you plan to use [Google Cloud CMEK](https://docs.cloud.google.com/oracle/database/docs/cmek) for your Exadata VM Clusters, Exascale VM Clusters, and Autonomous AI Databases, you must also complete the following additional step:

  1. Configure [VPC accessible services](https://docs.cloud.google.com/vpc-service-controls/docs/vpc-accessible-services) to ensure that the required services are accessible from network endpoints inside the perimeter. While creating the perimeter, do the following:

     1. If under **VPC accessible services** pane, the **Services accessible using Private Google Access** is set to **Select Services** , then add the following services to the list:

        * `sts.googleapis.com`
        * `iamcredentials.googleapis.com`
        * `cloudkms.googleapis.com`
  2. Configure ingress and egress rules for Exadata VM Cluster.

  3. Configure ingress and egress rules for Exascale VM Cluster.

  4. Configure ingress and egress rules for Autonomous AI Database.




### Configure ingress and egress rules for Exadata VM Cluster

To configure the service perimeter for Exadata VM Clusters, add the following **egress** rule as per the [Egress rules reference](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#egress-rules-reference):

Egress rule attribute | Value  
---|---  
From: Identities |  Add a principal identifier in the following format:
    
    
        principalSet://iam.googleapis.com/WORKLOAD_IDENTITY_POOL/*
        

You can obtain the WORKLOAD_IDENTITY_POOL as follows:

  1. In the OCI console, go to the **VM Cluster information** page.
  2. Click the value of the **Identity connector** field.
  3. From the **Identity Connector** page, copy the value of the **Workload Identity Pool** field.

**Note:** If you want to restrict just one project, then make sure that it's the host project that contains the ODB Network and the ODB Subnets.   
To Service | `iamcredentials.googleapis.com`  
To Methods |  `*` **Note:** This service doesn't support method-level VPC Service Controls restrictions.   
To Resources: Projects | Project ID: `gcp-sa-oci`  
Project name: `gcp-sa-oci`  
  
For instructions about how to add an egress rule, see [Configuring ingress and egress policies](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies).

### Configure ingress and egress rules for Exascale VM Cluster

To configure the service perimeter for Exascale VM Clusters, add the following **egress** rule as per the [Egress rules reference](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#egress-rules-reference):

Egress rule attribute | Value  
---|---  
From: Identities |  Add a principal identifier in the following format:
    
    
        principalSet://iam.googleapis.com/WORKLOAD_IDENTITY_POOL/*
        

You can obtain the WORKLOAD_IDENTITY_POOL as follows:

  1. In the OCI console, go to the **VM Cluster information** page.
  2. Click the value of the **Identity connector** field.
  3. From the **Identity Connector** page, copy the value of the **Workload Identity Pool** field.

**Note:** If you want to restrict just one project, then make sure that it's the host project that contains the ODB Network and the ODB Subnets.   
To Service | `iamcredentials.googleapis.com`  
To Methods |  `*` **Note:** This service doesn't support method-level VPC Service Controls restrictions.   
To Resources: Projects | Project ID: `gcp-sa-oci`  
Project name: `gcp-sa-oci`  
  
For instructions about how to add an egress rule, see [Configuring ingress and egress policies](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies).

### Configure ingress and egress rules for Autonomous AI Database

Autonomous AI Databases use Oracle-managed service accounts. The configuration of the service perimeter for an Autonomous AI Database differs based on the value of the `ROUTE_OUTBOUND_CONNECTIONS` database property.

Before creating the ingress and egress rules, obtain the value of the `ROUTE_OUTBOUND_CONNECTIONS` property by running the following SQL query in the database:
    
    
    SELECT * FROM DATABASE_PROPERTIES WHERE PROPERTY_NAME = 'ROUTE_OUTBOUND_CONNECTIONS';
    

Based on the value of the `ROUTE_OUTBOUND_CONNECTIONS` database property, configure your service perimeter as follows:

  * **Case 1** : `ROUTE_OUTBOUND_CONNECTIONS` is not set, that is, it has default value (public routing). In this case, the traffic enters Google Cloud from the public internet and is treated as an ingress violation.

Add the following **ingress** rule as per the [Ingress rules reference](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#ingress-rules-reference):

Ingress rule attribute | Value  
---|---  
From: Identities |  **Identity** : Oracle-managed service account You can obtain the service account from the **Autonomous AI Database details** page in Google Cloud console, in the **Oracle-managed service account** section. **Source** : access level containing the Outbound IP address of the database. To obtain the Outbound IP address, run the following SQL query in the database:
        
        SELECT cloud_identity FROM v$pdbs;
          

In the resulting JSON response, look for the `OUTBOUND_IP_ADDRESS` property.  
To Service | `cloudkms.googleapis.com`  
Operations |  `*` **Note:** This service doesn't support method-level VPC Service Controls restrictions.   
  * **Case 2** : `ROUTE_OUTBOUND_CONNECTIONS` is set to `ENFORCE_PRIVATE_ENDPOINT` (private path enforcement). In this case, the traffic is forced through the private endpoint in the service perimeter and is treated as an egress violation.

Add the following **egress** rule as per the [Egress rules reference](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#egress-rules-reference):

Egress rule attribute | Value  
---|---  
From: Identities |  **Identity** : Oracle-managed service account You can obtain the service account from the **Autonomous AI Database details** page in Google Cloud console, in the **Oracle-managed service account** section. **Source** : your Google Cloud project.  
To Service | `iamcredentials.googleapis.com`  
To Methods |  `*` **Note:** This service doesn't support method-level VPC Service Controls restrictions.   



For instructions about how to adds ingress and egress rules, see [Configuring ingress and egress policies](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies).

## Add Oracle Database@Google Cloud API to the perimeter

To mitigate the risk of your data being exfiltrated from Oracle Database@Google Cloud, you must restrict the Oracle Database@Google Cloud API.

To add Oracle Database@Google Cloud as a restricted service through Google Cloud console, see [update a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#update).

Alternatively, you can use the `gcloud access-context-manager perimeters update` command to restrict Oracle Database@Google Cloud. For reference information, see [access-context-manager perimeters update](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/update).
    
    
    gcloud access-context-manager perimeters update PERIMETER_ID \
    --policy=POLICY_ID \
    --add-restricted-services=oracledatabase.googleapis.com
    

Replace the following:

  * PERIMETER_ID: the ID of the perimeter
  * POLICY_ID: the ID of the access policy



## Test the perimeter

Test your VPC Service Controls perimeter before enforcing it. For more information, see [Dry run mode for service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/dry-run-mode) and [Using dry-run mode to test ingress or egress policies](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#using-dryrun-ingress-egress-rules).

## Update the perimeter

To add or remove resources, you can [update a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#update).

## Create access levels

Optionally, to permit external access to protected resources inside a perimeter, you can use access levels. Access levels apply only to requests for protected resources coming from outside the service perimeter. You can't use access levels to give protected resources or VMs permission to access data and services outside the perimeter.

See [Allowing access to protected resources from outside a perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/use-access-levels).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
