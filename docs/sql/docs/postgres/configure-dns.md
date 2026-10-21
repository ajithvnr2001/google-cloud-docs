---
url: https://docs.cloud.google.com/sql/docs/postgres/configure-dns/
title: Configure DNS in Private Service Connect \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:10.148752+00:00
---

# Configure DNS in Private Service Connect  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/configure-dns/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Configure DNS in Private Service Connect Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/configure-dns "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/configure-dns "View this page for the SQL Server database engine")

This page describes how to configure DNS in Private Service Connect.

## Overview

DNS is the recommended way to connect to instances that have Private Service Connect enabled. A DNS name lets different networks connect to the same instance, where Private Service Connect endpoints in each network might have different IP addresses. Additionally, the Cloud SQL Auth Proxy and language connectors require DNS names to connect to these instances.

Cloud SQL instances with Private Service Connect enabled can have two types of DNS names:

  * **A per-instance DNS name**. This is available for instances in all editions of Cloud SQL. The primary instance and each replica instance have different per-instance DNS names.

  * **A global write endpoint DNS name**. This is available for instances in Cloud SQL Enterprise Plus edition, to help with [advanced disaster recovery (ADR)](https://docs.cloud.google.com/sql/docs/postgres/use-advanced-disaster-recovery). A write endpoint is a global DNS name that automatically resolves to the IP address of the current primary instance. In the case of a replica failover or switchover operation, this write endpoint redirects incoming connections to the new primary instance automatically. By using a write endpoint, you can avoid having to make application connection changes when you perform a replica failover or switchover operation for region outage recovery or a disaster recovery drill.




## DNS automation in Private Service Connect

To create a per-instance DNS name, you can use the Cloud SQL DNS automation feature to set up the DNS records and name for you. When you enable DNS automation, Cloud SQL automatically provisions and manages DNS records for the per-instance DNS name in your authorized consumer VPC networks.

With DNS automation enabled on a Cloud SQL Enterprise Plus edition instance, you can also enable a global write endpoint DNS name that always automatically resolves to the IP address of the current primary instance.

Optionally, you can manually configure a per-instance DNS record for the instance (see Configure DNS manually), but we recommend using DNS automation. Manual DNS configuration is a legacy option.

### Prerequisites for enabling DNS automation

  * To use DNS automation or a global write endpoint DNS name, you need to enable the [Cloud DNS API](https://docs.cloud.google.com/dns/docs/reference/rest).
  * DNS automation can only be enabled when Private Service Connect is enabled (use the `--enable-private-service-connect` parameter).
  * DNS automation can only be enabled when there's at least one Private Service Connect auto connection specified (use `--psc-auto-connections=network`).
  * A global write endpoint DNS name can only be enabled for an Cloud SQL Enterprise Plus edition instance that has DNS automation enabled.



### DNS automation configuration

**Note:** Enabling DNS automation requires that Private Service Connect be enabled, and enabling write endpoint DNS automation requires that DNS automation be enabled in an Enterprise Plus instance.

You can enable DNS automation and global write endpoint DNS name when you create a new instance, with Private Service Connect enabled, as shown in [Create a Cloud SQL instance](https://docs.cloud.google.com/sql/docs/postgresconfigure-private-service-connect#create-cloud-sql-instance-psc-enabled-2).

You can also enable or disable DNS automation for existing instances. When you do, Cloud SQL automatically provisions or cleans up the associated DNS records in the respective networks.

### gcloud

#### Enable DNS automation and a global write endpoint DNS name

To enable DNS automation and a global write endpoint DNS name, use the following command:
    
    
    gcloud sql instances patch INSTANCE_NAME \
      --enable-psc-auto-dns \
      --enable-psc-write-endpoint-dns

  * INSTANCE_NAME: the name of the Cloud SQL instance.



To specify `--enable-psc-write-endpoint-dns`, you must have already enabled DNS automation, or you must enable it in the same command.

#### Disable DNS automation or the global write endpoint DNS name

To disable DNS automation or the global write endpoint DNS name, use the following command:
    
    
    gcloud sql instances patch INSTANCE_NAME \
      --no-enable-psc-auto-dns \
      [--no-enable-psc-write-endpoint-dns]

Replace the following:

  * INSTANCE_NAME: the name of the Cloud SQL instance.



### REST

The HTTP method and URL: would look like this:
    
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances

The JSON request body would take a form like this:
    
    
    {
      "name": "INSTANCE_NAME",
      "project": "PROJECT_ID",
      "region": "REGION_NAME",
      "databaseVersion": "DATABASE_VERSION",
      "kind": "sql#instance",
      "settings": {
        "availabilityType": "AVAILABILITY_TYPE",
        "ipConfiguration": {
          "ipv4Enabled": false,
          "pscConfig": {
            "allowedConsumerProjects": [
              "ALLOWED_PROJECTS"
            ],
            "pscAutoConnections": [
              {
                "consumerProject":"CONSUMER_PROJECT",
                "consumerNetwork":"projects/PARENT_PROJECT/global/networks/CONSUMER_NETWORK"
              }
            ],
            "pscEnabled": true,
            "pscAutoDnsEnabled": DNS_ENABLEMENT,
            "pscWriteEndpointDnsEnabled": GLOBAL_DNS_ENABLEMENT,
          }
        },
        "kind": "sql#settings",
        "pricingPlan": "PER_USE",
        "replicationType": "SYNCHRONOUS",
        "tier": "MACHINE_TYPE"
      }
    }

Make the following replacements:

  * DNS_ENABLEMENT: `true` or `false` depending on whether you want to enable or disable DNS automation.
  * GLOBAL_DNS_ENABLEMENT: `true` or `false` depending on whether you want to enable or disable a global write endpoint DNS name. If `true`, then `enable-psc-auto-dns` must also be `true`.



## View DNS names

You can find both the per-instance DNS name for an instance and the global write endpoint DNS name for the project using the `describe` command.

### gcloud

#### Per-instance DNS name

To find the per-instance DNS name created using DNS automation, use the [`gcloud sql instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/describe) command like this:
    
    
        gcloud sql instances describe INSTANCE_NAME \
          --project=PROJECT_ID  \
          --flatten="dnsNames[]" \
          --format="csv[no-heading](dnsNames.dnsScope, dnsNames.recordManager, dnsNames.name)" \
            | grep "INSTANCE,CLOUD_SQL_AUTOMATION"
      

The output will look like this (where DNS_NAME will be the per-instance DNS name for the instance):
    
    
    INSTANCE,CLOUD_SQL_AUTOMATION,DNS_NAME

The DNS name will end with the instance's region name followed by `.sql-psc-goog`, like this:  
`INSTANCE,CLOUD_SQL_AUTOMATION,d73a167a8c3a.2naantchj3tsc.us-central1.sql-psc.goog`.  
To return the undecorated DNS name only, add `| cut -d, -f3` to the end of the command.

#### The global write endpoint DNS name

Similarly, you can use the `describe` command to find the global write endpoint DNS name for your replication cluster:
    
    
        gcloud sql instances describe INSTANCE_NAME \
          --project=INSTANCE_NAME  \
          --flatten="dnsNames[]" \
          --format="csv[no-heading](dnsNames.dnsScope, dnsNames.recordManager, dnsNames.name)" \
            | grep "CLUSTER,CLOUD_SQL_AUTOMATION"
      

The output will look like this (where GLOBAL_DNS_NAME will be the global write-endpoint DNS name for your replication cluster):
    
    
    CLUSTER,CLOUD_SQL_AUTOMATION,GLOBAL_DNS_NAME

The global write endpoint DNS name ends with `.global.sql-psc-goog`, like this:  
`CLUSTER,CLOUD_SQL_AUTOMATION,d73a167a8c3a.2naantchj3tsc.global.sql-psc.goog`. To return the undecorated DNS name only, add `| cut -d, -f3` to the end of the command.

### REST

The HTTP method and URL: would look like this:
    
    
    GET https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances

The per-instance DNS name and the global write endpoint DNS name would be returned in the `dnsNames` field of the response, like this:
    
    
    {
      "dnsNames": [
        {
          "connectionType": "PRIVATE_SERVICE_CONNECT",
          "dnsScope": "INSTANCE",
          "name": "31f5395197d0.3e0v7ztul56ph.us-central1.sql.goog.",
          "recordManager": "CUSTOMER"
        },
        {
          "connectionType": "PRIVATE_SERVICE_CONNECT",
          "dnsScope": "INSTANCE",
          "name": "31f5395197d0.3e0v7ztul56ph.us-central1.sql-psc.goog",
          "recordManager": "CLOUD_SQL_AUTOMATION"
        },
        {
          "connectionType": "PRIVATE_SERVICE_CONNECT",
          "dnsScope": "CLUSTER",
          "name": "3lbvojtu2fo6q.3e0v7ztul56ph.global.sql-psc.goog",
          "recordManager": "CLOUD_SQL_AUTOMATION"
        }
      ],
    }

You can use the global write endpoint DNS name or the per-instance DNS name to connect to the instance. See [Connect using a DNS record](https://docs.cloud.google.com/sql/docs/postgres/configure-private-service-connect#connect-using-dns).

## DNS automation status fields

You can determine the status of DNS for your instance and replication cluster in these two output fields:

  * `instanceAutoDnsStatus`: Shows the status of per-instance DNS.
  * `writeEndpointAutoDnsStatus`: Shows the status of the global write endpoint DNS.



Both fields can have the following values:

  * `AUTO_DNS_STATUS_UNSPECIFIED`
  * `AUTO_DNS_OK`
  * `AUTO_DNS_FAILED`
  * `AUTO_DNS_UNKNOWN`



These fields appear within the `pscAutoConnections` output field:
    
    
        "pscAutoConnections": [
          {
            "consumerNetwork": "projects/my-psc-project/global/networks/psc-dns-net2",
            "consumerNetworkStatus": "VALID",
            "consumerProject": "my-psc-project",
            "instanceAutoDnsStatus": "AUTO_DNS_OK",
            "ipAddress": "10.0.2.4",
            "status": "ACTIVE",
            "writeEndpointAutoDnsStatus": "AUTO_DNS_OK"
          }
        ]

## Troubleshooting DNS automation

If the Cloud DNS API isn't enabled, or the Private Service Connect service connection policy is missing, or if there are backend errors during DNS record creation, then DNS automation can fail to create a per-instance DNS record or a global write endpoint DNS name.

To troubleshoot and attempt to resolve these issues, reconcile the networking for DNS automation. Use the `curl` command to `PATCH` the Cloud SQL instance and specify one of the following query parameters:

  * **`reconcilePscNetworking`** : when you set the query parameter to `true`, Cloud SQL tries to restore any parts of DNS automation that aren't working. To attempt reconciliation, run the following command:
        
        curl -X PATCH \
            -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
            -H "Content-Type: application/json" \
            "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME?reconcilePscNetworking=true" \
            -d '{
              "kind": "sql#instance",
              "project": "PROJECT_ID",
              "name": "INSTANCE_NAME",
              "settings": {
                "kind": "sql#settings"
              }
            }'

Replace the following: 

    * PROJECT_ID: the ID of the Google Cloud project
    * INSTANCE_NAME: the name of the Cloud SQL instance

This operation doesn't cause downtime.

  * **`reconcilePscNetworkingForce`** : similar to `reconcilePscNetworking`, but when you set to true, Cloud SQL tries to restore all DNS automation settings at the cost of brief downtime of the existing DNS automation parts that are working. This can help in some cases where `reconcile-psc-networking` doesn't work.
        
        curl -X PATCH \
            -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
            -H "Content-Type: application/json" \
            "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME?reconcilePscNetworkingForce=true" \
            -d '{
              "kind": "sql#instance",
              "project": "PROJECT_ID",
              "name": "INSTANCE_NAME",
              "settings": {
                "kind": "sql#settings"
              }
            }'

Replace the following: 

    * PROJECT_ID: the ID of the Google Cloud project
    * INSTANCE_NAME: the name of the Cloud SQL instance



## Assign custom DNS names

You can configure custom DNS names for your Private Service Connect Cloud SQL instances. Simply create a `CNAME` record with the Private Service Connect instance DNS name as its value. For example, if you wanted to configure your applications using the database DNS name `sample-db.mycompany.example.com` to refer to the database instance with the Private Service Connect DNS name `abcdef123456.987654321fedcb.us-central1.sql-psc.goog`, you would first have to configure the instance with a [custom DNS name](https://docs.cloud.google.com/sql/docs/postgres/custom-dns-name), and then create a DNS `CNAME` record using the DNS provider:

NAME | TYPE | TTL | VALUE  
---|---|---|---  
`sample-db.mycompany.example.com` | CNAME | 600 | `abcdef123456.987654321fedcb.us-central1.sql-psc.goog`  
**Note:** in order to use custom DNS names and custom Private Service Connect write endpoint names, the Cloud SQL auth proxy or Cloud SQL connector must be able to resolve the DNS records for the instance. If the auth proxy or connector is unable to connect, and you see `DNS record not found` errors in the logs, then check that the DNS records are configured correctly and can be resolved.

## Configure DNS manually

We recommend using the DNS automation, because the manual DNS configuration is a legacy option. Optionally, you can manually configure a per-instance DNS record for the instance. A DNS name provides a consistent way of using the auth proxy or language connectors to connect from different networks. The instance lookup API response provides a suggested DNS name that you can use to create the DNS record in a [private DNS zone](https://docs.cloud.google.com/dns/docs/dns-overview#private_zone) in the corresponding VPC network.

**Important:** If you're using the [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/postgres/configure-private-service-connect#connect-cloud-sql-auth-proxy) or the [Cloud SQL Language Connectors](https://docs.cloud.google.com/sql/docs/postgres/configure-private-service-connect#connect-using-language-connectors), then set up a [DNS record](https://docs.cloud.google.com/dns/docs/records-overview) which matches the recommended DNS name provided for the instance. For more information, see [Connect using the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/postgres/connect-auth-proxy).

For more information about best practices for private DNS zones, including how to allow on-premises hosts to query DNS records that are hosted in these zones, see [Best practices for Cloud DNS private zones](https://docs.cloud.google.com/dns/docs/best-practices#best_practices_for_private_zones).

### gcloud

  1. To view summary information about a Cloud SQL instance, including the DNS name of the instance, use the [`gcloud sql instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/describe) command:
         
         gcloud sql instances describe INSTANCE_NAME \
                   --project=PROJECT_ID
               

Make these replacements:

     * INSTANCE_NAME: the name of the Cloud SQL instance
     * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance

In the response, verify that the DNS name appears. This name has the following pattern: `INSTANCE_UID.PROJECT_DNS_LABEL.REGION_NAME.sql.goog.`. For example: `1a23b4cd5e67.1a2b345c6d27.us-central1.sql.goog.`.

**Note:** DNS names always end with a period (`.`).

If you want to use a custom DNS name to connect to a Cloud SQL instance instead of using the predefined DNS name in this section, then configure the custom subject alternative name (SAN) setting while creating the instance. The custom DNS name that you insert into the custom SAN setting is added to the SAN field of the server certificate of the instance. This lets you use the custom DNS name with hostname validation securely.

For more information about configuring the custom SAN setting, see [Create instances](https://docs.cloud.google.com/sql/docs/postgres/create-instance).

  2. To create a private DNS zone, use the [`gcloud dns managed-zones create`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/managed-zones/create) command. This zone is associated with the VPC network that's used to connect to the Cloud SQL instance through the Private Service Connect endpoint.

**Note:** For each VPC network, create a DNS zone.
         
         gcloud dns managed-zones create ZONE_NAME \
             --project=PROJECT_ID \
             --description="DESCRIPTION" \
             --dns-name=DNS_NAME \
             --networks=NETWORK_NAME \
             --visibility=private
               

Make the following replacements:

     * ZONE_NAME: the name of the DNS zone
     * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the zone
     * DESCRIPTION: a description of the zone (for example, a DNS zone for the Cloud SQL instance)
     * DNS_NAME: the name of the DNS suffix for the zone, such as `REGION_NAME.sql.goog.` (where REGION_NAME is the region name for the zone)
     * NETWORK_NAME: the name of the VPC network
  3. After you [create the Private Service Connect endpoint](https://docs.cloud.google.com/sql/docs/postgres/configure-private-service-connect#create-psc-endpoint-new), to create a DNS record in the zone, use the [`gcloud dns record-sets create`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/record-sets/create) command:
         
         gcloud dns record-sets create DNS_RECORD \
              --project=PROJECT_ID \
              --type=RRSET_TYPE \
              --rrdatas=RR_DATA \
              --zone=ZONE_NAME
               

Make the following replacements:

     * DNS_RECORD: the name of the DNS record. This record is set to the DNS name that you retrieved from the Cloud SQL instance earlier in this procedure (for example,  
`1a23b4cd5e67.1a2b345c6d27.us-central1.sql.goog.`).
     * RRSET_TYPE: the resource record type of the DNS record set. If the internal IP address that you reserved for the Private Service Connect endpoint is an IPv4 address, then specify `A` for this parameter. Otherwise, if the IP address for the endpoint is an IPv6 address, then specify `AAAA`.
     * RR_DATA: the IP address allocated for the Private Service Connect endpoint (for example, `198.51.100.5`). You can also enter multiple values such as `rrdata1 rrdata2 rrdata3` (for example,  
`10.1.2.3 10.2.3.4 10.3. 4.5`).



### REST

  1. Get the DNS name of a Cloud SQL instance.

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance
     * INSTANCE_NAME: the name of the instance

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_NAME

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    {
      ...
      "dnsName": "INSTANCE_ID.PROJECT_DNS_LABEL.REGION_NAME.sql.goog."
    }
    

The `dnsName` field displays the DNS name of the Cloud SQL instance. DNS names always end with a period (`.`).

  2. Create a private DNS zone. This zone is associated with the VPC network that's used to connect to the Cloud SQL instance through the Private Service Connect endpoint.

**Note:** For each VPC network, create a DNS zone.

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the DNS zone
     * ZONE_NAME: the name of the zone
     * DESCRIPTION: a description of the zone (for example, a DNS zone for the Cloud SQL instance)
     * DNS_NAME: the name of the DNS suffix for the zone, such as `REGION_NAME.sql.goog.` (where REGION_NAME is the region name for the zone)
     * NETWORK_NAME: the name of the VPC network 

HTTP method and URL: 
    
    POST https://dns.googleapis.com/dns/v1/projects/PROJECT_ID/managedZones

Request JSON body: 
    
    {
      "name": "ZONE_NAME",
      "description": "DESCRIPTION",
      "dnsName": "DNS_NAME",
      "visibility": "private",
      "privateVisibilityConfig": {
        "kind": "dns#managedZonePrivateVisibilityConfig",
        "networks": [
          {
            "kind": "dns#managedZonePrivateVisibilityConfigNetwork",
            "networkUrl": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/NETWORK_NAME"
          }
        ]
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://dns.googleapis.com/dns/v1/projects/PROJECT_ID/managedZones"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://dns.googleapis.com/dns/v1/projects/PROJECT_ID/managedZones" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    {
      "name": "ZONE_NAME",
      "dnsName": "DNS_NAME",
      "description": "DESCRIPTION",
      "id": "ID",
      "nameServers": [
        "ns-gcp-private.googledomains.com."
      ],
      "creationTime": "2024-05-10T17:05:34.607Z",
      "visibility": "private",
      "privateVisibilityConfig": {
        "networks": [
          {
            "networkUrl": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/NETWORK_NAME",
            "kind": "dns#managedZonePrivateVisibilityConfigNetwork"
          }
        ],
        "gkeClusters": [],
        "kind": "dns#managedZonePrivateVisibilityConfig"
      },
      "cloudLoggingConfig": {
        "kind": "dns#managedZoneCloudLoggingConfig"
      },
      "kind": "dns#managedZone"
    }
    

  3. After you [create the Private Service Connect endpoint](https://docs.cloud.google.com/sql/docs/postgres/configure-private-service-connect#create-psc-endpoint-new), create a DNS record in the zone.

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the DNS zone.
     * ZONE_NAME: the name of the zone.
     * DNS_RECORD: the name of the DNS record. This record is set to the DNS name that you retrieved from the Cloud SQL instance earlier in this procedure (for example, `1a23b4cd5e67.1a2b345c6d27.us-central1.sql.goog.`).
     * RRSET_TYPE: the resource record type of the DNS record set. If the internal IP address that you reserved for the Private Service Connect endpoint is IPv4, then specify `A` for this parameter. Otherwise, if the IP address for the endpoint is IPv6, then specify `AAAA`.
     * TTL: the time to live (TTL) for the record set in the number of seconds (for example, `300`).
     * RR_DATA: the IP address allocated for the Private Service Connect endpoint (for example, `198.51.100.5`). You can also enter multiple values such as `rrdata1 rrdata2 rrdata3` (for example, `10.1.2.3 10.2.3.4 10.3.4.5`).

HTTP method and URL: 
    
    POST https://dns.googleapis.com/dns/v1/projects/PROJECT_ID/managedZones/ZONE_NAME

Request JSON body: 
    
    {
      "deletions": []
      "additions": [
        {
          "name": "DNS_RECORD",
          "type": "RRSET_TYPE",
          "ttl": TTL,
          "rrdatas": [
            "RR_DATA"
          ]
        }
      ]
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://dns.googleapis.com/dns/v1/projects/PROJECT_ID/managedZones/ZONE_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://dns.googleapis.com/dns/v1/projects/PROJECT_ID/managedZones/ZONE_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    {
      "additions": [
        {
          "name": "DNS_RECORD",
          "type": "RRSET_TYPE",
          "ttl": TTL,
          "rrdatas": [
            "RR_DATA"
          ],
          "signatureRrdatas": [],
          "kind": "dns#resourceRecordSet"
        }
      ],
      "deletions": [],
      "startTime": "2024-05-10T17:29:44.375Z",
      "id": "CHANGE_ID",
      "status": "pending",
      "kind": "dns#change"
    }
    

**Note:** If you're using this DNS record to [connect to the Cloud SQL instance](https://docs.cloud.google.com/sql/docs/postgres/configure-private-service-connect#connect-to-instance-psc-enabled), then make a note of the CHANGE_ID value.


Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
