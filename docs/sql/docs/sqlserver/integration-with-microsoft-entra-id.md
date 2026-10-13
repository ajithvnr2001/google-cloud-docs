---
url: https://docs.cloud.google.com/sql/docs/sqlserver/integration-with-microsoft-entra-id/
title: Integration with Microsoft Entra ID \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:15:47.237937+00:00
---

# Integration with Microsoft Entra ID  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/integration-with-microsoft-entra-id/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Integration with Microsoft Entra ID Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

Cloud SQL for SQL Server integration with Microsoft Entra ID provides centralized identity and access management (IAM) for your databases using your existing [Microsoft Entra ID](https://www.microsoft.com/en-us/security/business/identity-access/microsoft-entra-id) tenant.

This integration offers the following benefits:

  * **Centralized authentication.** Lets users and applications sign in to their Cloud SQL for SQL Server instances using their existing Microsoft Entra ID identities without re-entering a password. This capability eliminates the need to manage separate SQL Server-specific logins and passwords.

  * **Enhanced security.** Helps you enforce your organization's existing security policies, such as multi-factor authentication (MFA) and conditional access (CA) rules, at the database level.

  * **Simplified user management.** When a user's Microsoft Entra ID account is disabled or removed, the user's database access is automatically revoked. This capability helps simplify offboarding and access reviews.




## Prerequisites for integration

**Note:** Make sure you're using the latest version of [`gcloud`](https://docs.cloud.google.com/sdk/docs/cheatsheet#getting_started).

To use Cloud SQL for SQL Server integration with Microsoft Entra ID, your instance must meet the following requirements:

  1. You must have an existing instance or create a new one.

Microsoft Entra ID authentication is only supported on SQL Server 2022 or later versions; it is not available on SQL Server 2017 or SQL Server 2019.

  2. Enable Microsoft Entra ID authentication.

Before you enable Microsoft Entra ID authentication, complete the following steps in your Azure portal:

     1. [Find your Microsoft Entra tenant ID.](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-find-tenant)
     2. [Create a new application registration in Microsoft Entra ID.](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app)

Cloud SQL for SQL Server uses this application to communicate with your Microsoft Entra tenant ID. When you create the application, note the application or client ID.

     3. [Grant permissions for the application to read directory data:](https://learn.microsoft.com/en-us/sql/relational-databases/security/authentication-access/azure-ad-authentication-sql-server-setup-tutorial)

        1. Select the application registration you just created, then click **API permissions**.
        2. Select **Add a permission** > **Microsoft Graph** > **Application permissions**.
        3. Grant one of the following permission sets: 
           * Option 1. 
             * **Directory.Read.All**
           * Option 2. Provides more specific permissions. 
             * **Application.Read.All**
             * **Group.Read.All**
             * **User.Read.All**
        4. [Grant tenant-wide administrator consent](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/grant-admin-consent?pivots=portal) to allow the application to use these permissions.



## Network connectivity

Microsoft Entra ID is a public service that uses public endpoints for authentication. In order for Microsoft Entra ID authentication to work properly, your Cloud SQL instance must be able to make outbound connections to these public endpoints. The following sections discuss next steps, based on your instance's network connectivity configuration:

  * Instances with a public IP
  * Instances with a private IP



### Instances with a public IP

If your Cloud SQL instance is configured with a public IP address, it has built-in, outbound access to the internet.

While no additional network configuration is required for Microsoft Entra ID authentication to work, review Limitations before you continue.

### Instances with a private IP

If your Cloud SQL instance is configured with only a private IP address, it doesn't have direct access to the internet. You must configure an egress path to allow the instance to reach Microsoft's public identity endpoints. Microsoft Entra ID integration configuration depends on how your private instance is configured:

  * Private Service Connect
  * Private services access (PSA)



### Private Service Connect

If your Cloud SQL instance is configured to use a private IP address, we recommend using [Private Service Connect](https://docs.cloud.google.com/sql/docs/mysql/configure-private-service-connect) to enable Microsoft Entra ID, as it eliminates certain overhead maintenance tasks such as the following:

  * Managing [bastion host](https://docs.cloud.google.com/compute/docs/connect/ssh-using-bastion-host) VMs.
  * Maintaining routes.
  * Creating overly broad routes like those required for PSA connectivity.



Before you continue, review the limitations for using Microsoft Entra ID.

To enable connectivity, you need to configure [Cloud network address translation (Cloud NAT)](https://docs.cloud.google.com/nat/docs/overview) in the consumer VPC. This allows the PSC-enabled instance to use the Cloud NAT gateway for outbound traffic to public Microsoft endpoints. Once enabled, internal routing restricts traffic so that only Microsoft Entra ID-related traffic reaches your Cloud NAT instance.

To enable connectivity, complete the following required steps:

  1. [Create a PSC-enabled instance.](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-service-connect)
  2. [Configure outbound connectivity for your Cloud SQL instance.](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-service-connect#configure-psc-outbound)
  3. [Create a Cloud NAT gateway.](https://docs.cloud.google.com/nat/docs/overview)



### Private services access

If your Cloud SQL instance is configured to use a private IP address and you use PSA, the following steps are required to enable connectivity to Microsoft Entra ID:

  1. Deploy a [bastion host VM](https://docs.cloud.google.com/solutions/connecting-securely#bastion) within your VPC.

When you create a bastion host VM in your project, IP forwarding must be enabled. If you created a Linux-based bastion host VM, configure the bastion host VM you just created to perform IP forwarding:
         
         sudo sysctl net.ipv4.conf.all.forwarding=1
         sudo iptables --table nat --append POSTROUTING --out-interface  ens4 -j MASQUERADE
         

**Caution:** If service disruptions occur, this configuration doesn't persist. If the VM is restarted, then you need to re-apply the configuration. To automatically apply the configuration after a restart, we recommend scheduling a cron job.**Note:** To help reduce the risk of an outage, we recommend you deploy two bastion host VMs in separate zones. We also recommend you manage incoming traffic to the bastion host VMs with a [load balancer](https://docs.cloud.google.com/compute/docs/load-balancing-and-autoscaling).
  2. Configure the necessary network routes to direct Microsoft Entra ID authentication traffic from your Cloud SQL instance through the bastion host VM host to reach the internet.

Add the corresponding routes for each Microsoft Entra ID endpoint. You can find the current IP ranges in the `AzureActiveDirectory.ServiceEndpoint` section in the [Azure IP Ranges and Service Tags](https://www.microsoft.com/en-us/download/details.aspx?id=56519) resource file.

**Caution:** Microsoft Entra ID endpoint IPs vary by region and may be changed by Microsoft at any time. You must review and update these routes regularly, or create broader routes, such as `/16` CIDR blocks, to accommodate potential changes.

###  gcloud 

For each Microsoft Entra ID IP range, create two routes, replacing `VM_NAME` and `VM_ZONE` with the actual name and zone of your bastion host VM:
         
         gcloud --project=PROJECT_ID compute routes create NAME \
           --network=NETWORK --destination-range=RANGE \
           --priority=998 --next-hop-gateway=default-internet-gateway
         
         gcloud  --project=PROJECT_ID compute routes create NAME \
           --network=NETWORK --destination-range=RANGE --priority=999 \
           --next-hop-instance=VM_NAME --next-hop-instance-zone=VM_ZONE \
           --next-hop-ilb=ILB_VALUE
         

Replace the following:

     * PROJECT_ID: the ID of the project where your Cloud SQL instance resides.
     * NAME: the name of the route you want to create.
     * NETWORK: the name of the network where your Cloud SQL instance resides.
     * RANGE: the IP range you want to use.
     * VM_NAME: the name of the bastion host VM you want to include.
     * VM_ZONE: the zone of the bastion host VM you want to include, such as `us-central1`.
     * ILB_VALUE: Optional. The name or IP address of a forwarding rule for an internal TCP/UDP load balancer. If you configured a load balancer in front of your bastion host VMs, then you need to include the [`--next-hop-ilb`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routes/create#--next-hop-ilb) flag in this command.

For more information, see [Internal passthrough Network Load Balancers as next hops](https://docs.cloud.google.com/load-balancing/docs/internal/ilb-next-hop-overview#additional_considerations).

An example might look like the following:
    
    gcloud  --project=my-customer-project compute routes create my-route-1 --network=default --destination-range=20.20.32.0/27 --priority=998 --next-hop-gateway=default-internet-gateway
    
    gcloud  --project=my-customer-project compute routes create my-route-2 --network=default --destination-range=20.20.32.0/27 --priority=999 --next-hop-instance=my-bastion-vm --next-hop-instance-zone=us-central1-c --next-hop-ilb=fr-ilb1
    

  3. Use the same command in the previous step to apply the same configuration to allow traffic for Microsoft Entra ID certificate revocation checks. Use the IP ranges listed at [DigiCert Certificate Status IP address](https://knowledge.digicert.com/alerts/digicert-certificate-status-ip-address).

If you don't complete this step, Microsoft Entra ID authentication might still work, but you might also experience delays when opening new connections.




## Manage Microsoft Entra ID authentication

You can enable Entra ID authentication for a new or existing instance.

### Create an instance with Microsoft Entra ID authentication enabled

You can enable Microsoft Entra ID authentication when you create a new Cloud SQL for SQL Server instance. You need to provide the specific Microsoft Entra tenant ID and application ID (client ID) of the App Registration you configured in your Azure portal.

For more information, see Prerequisites.

###  gcloud 
    
    
    gcloud sql instances create INSTANCE_NAME \
        --database-version=EDITION \
        --tier=TIER \
        --network=NETWORK
        --root-password=PASSWORD
        --entra-id-tenant-id=TENANT_ID \
        --entra-id-application-id=APPLICATION_ID
    

Replace the following:

  * INSTANCE_NAME: the name of the instance you want to create.
  * EDITION: the instance edition you want to use, such as `SQLSERVER_2025_STANDARD`.
  * TIER: the instance tier or machine type you want to use, such as `db-custom-2-3840`.
  * NETWORK: the network name you want to use.
  * PASSWORD: the instance password.
  * TENANT_ID: the Microsoft Entra tenant ID.
  * APPLICATION_ID: the application or client ID.



An example might look like the following:
    
    
    gcloud sql instances create my-entraid-instance \
        --database-version=SQLSERVER_2025_STANDARD \
        --tier=db-custom-2-3840 \
        --assign-ip \
        --root-password=D61Xv36f!0lE \
        --entra-id-tenant-id=7e281aab-e994-4c83-88ed-d1674477a39c \
        --entra-id-application-id=4c5ed2da-0478-4aaa-ab65-6dfd33ba8bfd
    

###  REST v1 

Not all possible fields are shown in the following basic API call. For a prototype of a JSON request, see [Settings](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/instances#settings).

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the name of the project where the instance you want to create will be located.
  * INSTANCE_ID: the ID of the instance you want to create.
  * EDITION: the instance edition you want to use, such as `SQLSERVER_2022_STANDARD`.
  * REGION: the region where you want the instance to reside, such as `us-central1`.
  * PASSWORD: the instance password.
  * TIER: the instance tier or machine type you want to use, such as `db-custom-2-3840`.
  * NETWORK: the network name you want to use.
  * TENANT_ID: the Microsoft Entra tenant ID.
  * APPLICATION_ID: the application or client ID.



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances

Request JSON body: 
    
    
    {
      "databaseVersion":"EDITION",
      "name":"INSTANCE_ID",
      "region":"REGION",
      "rootPassword":"PASSWORD",
      "settings":
      {
        "tier":"TIER",
        "ipConfiguration":
          {
            "privateNetwork":"NETWORK"
          },
        "entraidConfig":
        {
          "tenantId": "TENANT_ID",
          "applicationId": "APPLICATION_ID"
        }
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
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-01T19:13:21.834Z",
      "operationType": "CREATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

###  REST v1beta4 

Not all possible fields are shown in the following basic API call. For a prototype of a JSON request, see [Settings](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances#settings).

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the name of the project where the instance you want to create will be located.
  * INSTANCE_ID: the ID of the instance you want to create.
  * EDITION: the instance edition you want to use, such as `SQLSERVER_2022_STANDARD`.
  * REGION: the region where you want the instance to reside, such as `us-central1`.
  * PASSWORD: the instance password.
  * TIER: the instance tier or machine type you want to use, such as `db-custom-2-3840`.
  * NETWORK: the network name you want to use.
  * TENANT_ID: the Microsoft Entra tenant ID.
  * APPLICATION_ID: the application or client ID.



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances

Request JSON body: 
    
    
    {
      "databaseVersion":"EDITION",
      "name":"INSTANCE_ID",
      "region":"REGION",
      "rootPassword":"PASSWORD",
      "settings":
      {
        "tier":"TIER",
        "ipConfiguration":
          {
            "privateNetwork":"NETWORK"
          },
        "entraidConfig":
        {
          "tenantId": "TENANT_ID",
          "applicationId": "APPLICATION_ID"
        }
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
         "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances"

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
        -Uri "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-01T19:13:21.834Z",
      "operationType": "CREATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

### Manage Microsoft Entra ID authentication on an existing instance

You can enable, modify, or disable the Microsoft Entra ID configuration on an existing instance at any time.

**Caution:** Updating an instance's Microsoft Entra ID configuration, whether enabling, modifying, or disabling integration, causes the instance to restart.

To modify your instance's configuration, you must patch the instance with the new or deleted tenant ID and application (client) ID values.

This process doesn't involve joining or unjoining a domain.

You can update the tenant ID and application ID values without enabling or disabling integration with Microsoft Entra ID.

###  gcloud 
    
    
    gcloud sql instances patch INSTANCE_NAME \
        --entra-id-tenant-id="NEW_TENANT_ID" \
        --entra-id-application-id="NEW_APPLICATION_ID"
    

Replace the following:

  * INSTANCE_NAME: the name of the instance you want to modify.
  * NEW_TENANT_ID: the new Microsoft Entra tenant ID. To disable Microsoft Entra ID, leave this string empty.
  * NEW_APPLICATION_ID: the new application or client ID. To disable Microsoft Entra ID, leave this string empty.



An example might look like the following:
    
    
    gcloud sql instances patch my-existing-instance \
        --entra-id-tenant-id=7e281aab-e994-4c83-88ed-d1674477a39c \
        --entra-id-application-id=4c5ed2da-0478-4aaa-ab65-6dfd33ba8bfd
    

###  REST v1 

Not all possible fields are shown in the following basic API call. For a prototype of a JSON request, see [Settings](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/instances#settings).

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID of the project where the instance you want to modify is located.
  * INSTANCE_ID: the ID of the instance you want to modify.
  * TENANT_ID: the Microsoft Entra tenant ID. To disable Microsoft Entra ID, leave this string empty.
  * APPLICATION_ID: the application or client ID. To disable Microsoft Entra ID, leave this string empty.



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances

Request JSON body: 
    
    
    {
      "settings":
      {
        "entraidConfig":
        {
          "tenantId": "NEW_TENANT_ID",
          "applicationId": "NEW_APPLICATION_ID"
        }
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-01T19:13:21.834Z",
      "operationType": "CREATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

###  REST v1beta4 

Not all possible fields are shown in the following basic API call. For a prototype of a JSON request, see [Settings](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/instances#settings).

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID of the project where the instance you want to modify is located.
  * INSTANCE_ID: the ID of the instance you want to modify.
  * TENANT_ID: the Microsoft Entra tenant ID. To disable Microsoft Entra ID, leave this string empty.
  * APPLICATION_ID: the application or client ID. To disable Microsoft Entra ID, leave this string empty.



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances

Request JSON body: 
    
    
    {
      "settings":
      {
        "entraidConfig":
        {
          "tenantId": "NEW_TENANT_ID",
          "applicationId": "NEW_APPLICATION_ID"
        }
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-01T19:13:21.834Z",
      "operationType": "CREATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

## Add the certificate to the application

In order for your Microsoft Entra ID to authenticate your Cloud SQL for SQL Server instance, you must upload the Cloud SQL for SQL Server instance's public certificate to your Microsoft Entra ID App Registration.

  1. After you enable Microsoft Entra ID authentication on your instance, [create an instance-specific certificate for Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity-platform/how-to-add-credentials?tabs=certificate).

**Caution:** If the instance doesn't already have a Microsoft Entra ID certificate, then creating a certificate and assigning it to the instance automatically activates it. Doing so causes the instance and its replicas to restart.**Caution:** This certificate is valid for 3 years from its creation date. You are responsible for manually rotating this certificate before it expires to prevent an authentication outage.

###  gcloud 
         
         gcloud sql ssl entraid-certs create --instance=INSTANCE_NAME
         

Replace the following:

     * INSTANCE_NAME: the name of the instance for which you want to create a certificate.

###  REST v1 

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the ID of the project where your instance is located.
     * INSTANCE_ID: the ID of the instance.

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/addEntraIdCertificate

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/addEntraIdCertificate"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/addEntraIdCertificate" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-01T19:13:21.834Z",
      "operationType": "CREATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

###  REST v1beta4 

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the ID of the project where your instance is located.
     * INSTANCE_ID: the ID of the instance.

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/addEntraIdCertificate

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/addEntraIdCertificate"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/addEntraIdCertificate" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-01T19:13:21.834Z",
      "operationType": "CREATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

  2. Get the details for the certificate you just created by retrieving the instance's details:

###  gcloud 
         
         gcloud sql ssl entraid-certs list --instance=INSTANCE_NAME --format="value(ssl_cert.cert)"
         

Replace the following:

     * INSTANCE_NAME: the name of the instance associated with the certificate you just created.

###  REST v1 

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the ID of the project where your instance is located.
     * INSTANCE_ID: the ID of the instance.

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/listEntraIdCertificates

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/listEntraIdCertificates"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/listEntraIdCertificates" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

This command prints a certificate you can save to a file and then later upload to the Azure portal.

You must remove all embedded newline characters from the file and manually separate each new line. Failure to do so causes the file upload to fail.

For example, you might receive a text string similar to the following:
    
    Line1\Line2\Line3
    

You must manually separate each line, similar to the following:
    
    Line1
    Line2
    Line3
    

Alternatively, if you don't want to perform this task manually, use the following command:
    
    curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json; charset=utf-8" \
    -H "x-goog-user-project: PROJECT_ID" "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME/listEntraIdCertificates" -s | jq -r '.certs[0].cert'
    

Replace the following:

     * PROJECT_ID: the project ID where your instance is located.
     * INSTANCE_NAME: the name of the instance associated with the certificate you just created.

###  REST v1beta4 

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the ID of the project where your instance is located.
     * INSTANCE_ID: the ID of the instance.

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/listEntraIdCertificates

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/listEntraIdCertificates"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/listEntraIdCertificates" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

This command prints a certificate you can save to a file and then later upload to the Azure portal.

You must remove all embedded newline characters from the file and manually separate each new line. Failure to do so causes the file upload to fail.

For example, you might receive a text string similar to the following:
    
    Line1\Line2\Line3
    

You must manually separate each line, similar to the following:
    
    Line1
    Line2
    Line3
    

Alternatively, if you don't want to perform this task manually, use the following command:
    
    curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json; charset=utf-8" \
    -H "x-goog-user-project: PROJECT_ID" "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME/listEntraIdCertificates" -s | jq -r '.certs[0].cert'
    

Replace the following:

     * PROJECT_ID: the project ID where your instance is located.
     * INSTANCE_NAME: the name of the instance associated with the certificate you just created.

  3. Add your certificate to the Azure portal.

     1. Navigate to your **App Registration** in the Azure portal.
     2. Open **Certificates & secrets**.
     3. Select **Upload certificate**. Browse to the certificate file you retrieved from your instance, and add it.
     4. Click **OK**.



## Rotate the Microsoft Entra ID certificate

You must rotate the Microsoft Entra ID certificate before it expires. We recommend starting this process at least one week before the scheduled expiration date:

  1. Follow the steps in Add the certificate to the application to create a new, inactive certificate on your Cloud SQL for SQL Server instance and then upload it to Microsoft Entra ID using the Azure portal. This doesn't impact the current active certificate.

  2. Activate the new certificate on the Cloud SQL for SQL Server instance, which triggers Cloud SQL for SQL Server to start using the new certificate for all new authentications.

**Caution:** Certificate activation causes the instance and its replicas to restart.

###  gcloud 
         
         gcloud sql ssl entraid-certs rotate --instance=INSTANCE_NAME
         

Replace the following:

     * INSTANCE_NAME: the name of the instance associated with the certificate you want to rotate.

###  REST v1 

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the ID of the project where your instance is located.
     * INSTANCE_ID: the ID of the instance.

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/rotateEntraIdCertificate

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/rotateEntraIdCertificate"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/rotateEntraIdCertificate" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

###  REST v1beta4 

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the ID of the project where your instance is located.
     * INSTANCE_ID: the ID of the instance.

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/rotateEntraIdCertificate

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/rotateEntraIdCertificate"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/rotateEntraIdCertificate" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

  3. Your instance now uses the new certificate.

You can safely remove the old certificate from your Microsoft Entra ID App Registration and from the Cloud SQL for SQL Server instance. For more information, see [Add and manage application credentials in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity-platform/how-to-add-credentials?tabs=certificate).




## Roll back the Microsoft Entra ID certificate

If you experience issues after rotating to a new certificate, you can roll back to the previous certificate.

To perform a rollback, the previous certificate must still be valid and must still be trusted by your Microsoft Entra ID App Registration.

The following commands immediately reactivate the specified previous certificate on your Cloud SQL for SQL Server instance.

**Caution:** Certificate rollback causes the instance and its replicas to restart.

###  gcloud 
    
    
    gcloud sql ssl entraid-certs rollback --instance=INSTANCE_NAME
    

Replace the following:

  * INSTANCE_NAME: the name of the instance associated with the certificate you want to roll back.



###  REST v1 

Not all possible fields are shown in the following basic API call. For a prototype of a JSON request, see [Settings](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/instances#settings).

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID of the project where the instance is located.
  * INSTANCE_ID: the ID of the instance for which you want to rollback the certificate.
  * CERTIFICATE_NAME: the name of the new certificate you want to use to replace the old certificate, such as `sha1Fingerprint`.



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/rollbackEntraIdCertificate

Request JSON body: 
    
    
    {
      {
      "RotateEntraIdCertificateContext": {"nextVersion": "CERTIFICATE_NAME"}
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
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/rollbackEntraIdCertificate"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/rollbackEntraIdCertificate" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-01T19:13:21.834Z",
      "operationType": "CREATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

###  REST v1beta4 

Not all possible fields are shown in the following basic API call. For a prototype of a JSON request, see [Settings](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/instances#settings).

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID of the project where the instance is located.
  * INSTANCE_ID: the ID of the instance for which you want to rollback the certificate.
  * CERTIFICATE_NAME: the name of the new certificate you want to use to replace the old certificate, such as `sha1Fingerprint`.



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/rollbackEntraIdCertificate

Request JSON body: 
    
    
    {
      {
      "RotateEntraIdCertificateContext": {"nextVersion": "CERTIFICATE_NAME"}
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
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/rollbackEntraIdCertificate"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/rollbackEntraIdCertificate" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-01T19:13:21.834Z",
      "operationType": "CREATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

## Create the initial Microsoft Entra ID login

After enabling Microsoft Entra ID authentication on the instance, you need to create your Microsoft Entra ID logins.

  1. Create the first Microsoft Entra ID login.

This initial login, which represents a Microsoft Entra ID user or group, can't be created using T-SQL. You must create it using either the gcloud CLI or the Cloud SQL Admin API:

###  gcloud 
         
         gcloud sql users create USER_NAME --instance=INSTANCE_NAME --type=ENTRAID_USER
         

Replace the following:

     * USER_NAME: the name of the Cloud SQL for SQL Server user you want to create.
     * INSTANCE_NAME: the name of the instance for which you want to create Microsoft Entra ID logins.
     * ENTRAID_USER: the Microsoft Entra ID username.

An example might look like the following:
    
    gcloud sql users create myentraiduser@mytenant.com --instance=my-entraid-instance --type=ENTRAID_USER
    

###  REST v1 

Not all possible fields are shown in the following basic API call. For a prototype of a JSON request, see [Settings](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/instances#settings).

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the ID of the project where the instance is located.
     * INSTANCE_ID: the ID of the instance for which you want to update.
     * USER_NAME: the name of the Cloud SQL for SQL Server user you want to create.
     * ENTRAID_USER: the Microsoft Entra ID username.

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/users

Request JSON body: 
    
    {
      "name": "USER_NAME"
      "type": "ENTRAID_USER"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/users"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/users" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-01T19:13:21.834Z",
      "operationType": "CREATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

###  REST v1beta4 

Not all possible fields are shown in the following basic API call. For a prototype of a JSON request, see [Settings](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/instances#settings).

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the ID of the project where the instance is located.
     * INSTANCE_ID: the ID of the instance for which you want to update.
     * USER_NAME: the name of the Cloud SQL for SQL Server user you want to create.
     * ENTRAID_USER: the Microsoft Entra ID username.

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/users

Request JSON body: 
    
    {
      "name": "USER_NAME"
      "type": "ENTRAID_USER"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/users"

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
        -Uri "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/users" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-01T19:13:21.834Z",
      "operationType": "CREATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

Once the initial Microsoft Entra ID login is created, you can connect to the database as that user.

  2. Create subsequent Microsoft Entra ID logins.

You can create and manage additional Microsoft Entra ID logins as noted in the previous step.

Alternatively, if you prefer to use another tool such as [SQL Server Management Studio (SSMS)](https://learn.microsoft.com/en-us/ssms/install/install), you must first grant the initial login the permission to manage other logins:
         
         GRANT ALTER ANY LOGIN TO [ENTRA_ID_USER] AS CustomerDbRootRole
         

Replace ENTRAID_USER with the Microsoft Entra ID username.

Once permissions are granted, this login can create and manage other Microsoft Entra ID logins using standard T-SQL commands. An example command might be similar to the following:
         
         CREATE LOGIN [<<ENTRA_ID_USER>>] FROM EXTERNAL PROVIDER
         

Replace ENTRAID_USER with the Microsoft Entra ID username.

To create users based on Microsoft Entra ID logins, or to grant permissions, use standard T-SQL commands.

For more information, including how to create a login using the proper syntax, see [Set up Microsoft Entra authentication for SQL Server with app registration](https://learn.microsoft.com/en-us/sql/relational-databases/security/authentication-access/azure-ad-authentication-sql-server-setup-tutorial?view=sql-server-ver17#create-user-syntax).




## Best practices

To help isolate permissions and to better define security boundaries, we strongly encourage you to create a unique Microsoft Entra ID application registration for each Cloud SQL for SQL Server instance. Revoking the application's credentials won't impact other, unrelated instances.

For more information, see [How to register an application in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app).

## Troubleshooting

The following sections help address issues you might encounter while managing Microsoft Entra ID integration.

### Network connectivity issues with private IP instances

You might experience some of the following issues during integration setup:

  * Slow operations to create Microsoft Entra ID logins
  * Unable to create Microsoft Entra ID logins
  * Unable to connect to the instance using Microsoft Entra ID authentication



To help address these issues, perform the following connectivity test:

  1. Within the same Google Cloud project and VPC, and in the same region as your Cloud SQL for SQL Server instance, create a test VM configured with only a private IP.

  2. Connect to the VM you just created using either the remote desktop protocol (RDP) or secure shell protocol (SSH). Then, run the following commands to test reachability. These steps can be applied to both Linux-based and Windows-based VMs:
         
         curl -4iv login.microsoftonline.com
         curl -4iv graph.microsoft.com
         curl -4iv ocsp.digicert.com
         




If you can't reach any of these endpoints, whether due to timeouts or refused connection errors, check your network configuration for the following:

  * For Private Service Connect, make sure Cloud NAT is correctly configured to allow outbound internet access.
  * For private services access, verify your custom routes and bastion hosts configuration.
  * Check your VPC Firewall rules to ensure egress traffic to these domains isn't blocked.



### Common error messages

You might encounter the following login error during Microsoft Entra ID authentication:
    
    
    Login failed for user ""
    

To resolve this issue, make sure that a SQL Server login exists for this Microsoft Entra ID user.

## Migration from Microsoft Active Directory

In the following scenarios, you can enable Microsoft Entra ID authentication without disabling the existing Microsoft Active Directory authentication:

  * Performing a phased migration. Moving authentication authority from Microsoft Active Directory to Microsoft Entra ID using either [customer-managed Active Directory (CMAD)](https://docs.cloud.google.com/sql/docs/sqlserver/cmad) or [Managed Service for Microsoft Active Directory](https://docs.cloud.google.com/sql/docs/sqlserver/ad).
  * Using a hybrid environment. Keeping both Microsoft Active Directory and Microsoft Entra ID enabled simultaneously.



## Logging

For reports on basic errors and warnings, such as whether Microsoft Entra ID is enabled, use the standard `sqlserver.err` log. For more detailed monitoring and troubleshooting information, use the `entraid.log` log, which offers information such as the following:

  * Provides the connectivity state for each required endpoint.
  * Reports details about any missing API permissions.
  * Indicates the number of days that remain until the client certificate expires.
  * Provides specific internal errors, such as token acquisition failures, which might help you locate the cause of an issue.



Log entries update on a daily basis or whenever a state changes.

## Read replicas

  * If you add a read replica to a primary instance that has Microsoft Entra ID enabled, the read replica is automatically configured to use Microsoft Entra ID.
  * If the primary instance has Microsoft Entra ID enabled, and you restore a backup to that instance, its associated read replica is automatically configured to use Microsoft Entra, as the identity doesn't change.
  * Changes to the tenant ID, application ID, or certificates of the primary instance automatically propagate to the instance's associated read replicas.



## Managed read pools

  * Changes to the tenant ID, application ID, or certificates of the primary instance automatically propagate to the instance's associated managed read pools.



## Cloned instances and restoring to a different instance

Microsoft Entra ID integration isn't automatically configured to the new instance in the following scenarios:

  * A clone of the primary instance.
  * A backup restored to an instance that isn't the primary.



In such cases, you must manually enable Microsoft Entra ID on the new instance and then re-upload its certificate to the Microsoft Entra ID application. This requirement is a security measure to help prevent multiple, unrelated instances from using the same application identity.

## Limitations

  * Microsoft Entra ID authentication is only supported on SQL Server 2022 or later versions; it is not available on SQL Server 2017 or SQL Server 2019.
  * If you clone an instance or restore a backup to a different instance, Microsoft Entra ID integration isn't automatically configured on the new instance.
  * To enable Microsoft Entra ID authentication on a regional instance with a public IP and private services access, your instance needs to be configured for use with a private services access route from a bastion VM.
  * To enable Microsoft Entra ID authentication on a regional instance that uses Private Service Connect and private services access, your instance needs to be configured for use with a private services access route from a bastion VM.



## What's next

  * Learn more about [Microsoft Entra ID](https://www.microsoft.com/en-us/security/business/identity-access/microsoft-entra-id)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
