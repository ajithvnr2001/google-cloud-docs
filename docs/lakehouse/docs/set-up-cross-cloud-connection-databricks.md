---
url: https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-databricks/
title: Set up cross-cloud connection for Databricks Unity Catalog \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:31:16.312063+00:00
---

# Set up cross-cloud connection for Databricks Unity Catalog  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-databricks/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Set up cross-cloud connection for Databricks Unity Catalog Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** For support during the preview, send an email to [biglake-help@google.com](mailto:biglake-help@google.com).

A cross-cloud connection to a Databricks Unity Catalog lets you query data from that catalog directly within Google Cloud. This capability unifies your data analytics by integrating your external data sources with your existing Google Cloud environment.

After you set up the connection, you can manage access to your federated data in _borderless Lakehouse_.

## Before you begin

  1. Review the [Lakehouse overview](https://docs.cloud.google.com/lakehouse/docs/introduction) to understand how Lakehouse manages access to data.
  2. Read [about accessing cross-cloud data](https://docs.cloud.google.com/lakehouse/docs/about-cross-cloud-data-access) to understand how it works.
  3. Review the [supported catalogs](https://docs.cloud.google.com/lakehouse/docs/about-cross-cloud-data-access#supported-catalogs) to verify supported configurations.
  4. Understand how to use [regional Secret Manager secrets](https://docs.cloud.google.com/secret-manager/regional-secrets/overview-rs). This is required to set up a Lakehouse with Databricks Unity Catalog using secret-based authentication.
  5. Optional: If you plan to route queries over a private interconnect between your Google Cloud VPC and your remote cloud provider's VPC (for example, AWS), ensure that you have an active account with your remote provider, provision a [Dedicated Cross-Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview#setup-process) or [Partner Cross-Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-cci-for-aws-overview), establish BGP sessions with your Cloud Router, and verify that you have the required IAM permissions in both cloud environments.

  6. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  7. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  8. Enable the BigLake, Secret Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=biglake.googleapis.com,secretmanager.googleapis.com)

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. Enable the BigLake, Secret Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=biglake.googleapis.com,secretmanager.googleapis.com)




### Required roles

To get the permissions that you need to set up cross-cloud access, ask your administrator to grant you the following IAM roles on your project: 

  * Manage Lakehouse catalogs: [BigLake Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`) 
  * Manage secrets (if using secret-based authentication): [Secret Manager Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.admin) (`roles/secretmanager.admin`) 
  * Route traffic over private interconnect (User): [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) 
  * Route traffic over private interconnect (Catalog service account): 
    * [Service Directory Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.viewer) (`roles/servicedirectory.viewer`)
    * [Service Directory PSC Authorized Service ](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.pscAuthorizedService) (`roles/servicedirectory.pscAuthorizedService`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Caution:** If using secret-based authentication, to follow the principle of least privilege and avoid granting access to all secrets in the project, have a Secret Manager administrator create the secret for you and grant you permissions to modify only that specific secret for Lakehouse.

### Limitations and considerations

This section lists the limitations and considerations for accessing cross-cloud data.

  * **Supported Cloud Providers for Cross-Cloud Interconnect:** Using a private interconnect with your borderless Lakehouse is supported with the following remote cloud providers: Amazon Web Services (AWS). You can use either a [Dedicated Cross-Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview#setup-process) or a [Partner Cross-Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-cci-for-aws-overview).
  * **Network routing:** If a private interconnect (such as Dedicated CCI or Partner CCI) is not configured, queries route over the public internet. This can result in higher egress fees from your remote cloud provider and less predictable performance.
  * **Databricks Unity Catalog configuration:**
    * Only Databricks Unity Catalogs that use an [external location on AWS](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-external-locations) or an [external location on Google Cloud](https://docs.databricks.com/gcp/en/sql/language-manual/sql-ref-external-locations) are supported. Unity Catalogs that use [default storage on AWS](https://docs.databricks.com/aws/en/storage/default-storage) or [default storage on Google Cloud](https://docs.databricks.com/gcp/en/storage/default-storage) are _not supported_.
    * You must enable [external data access](https://docs.databricks.com/aws/en/external-access/admin) on the metastore used by Unity Catalog, which is disabled by default.
    * You must grant the `EXTERNAL USE SCHEMA` privilege to the Databricks Service Principal on the target schemas or catalog to enable credential vending for external data access. Without this privilege, background metadata refresh and credential vending for queries fails.
  * **Read-only:** Federated catalogs in Lakehouse are read-only views of the remote catalog. Resource manipulation (such as creating, updating, or deleting resources) are not supported and must be performed directly in the remote catalog.
  * **Data freshness:** The `--refresh-interval` flag for a federated catalog determines how often metadata is synchronized. The value must be `0s` (disabled) or at least `300s` (5 minutes). A catalog's background metadata refresh may take longer the more namespace and table resources there are. If the previous refresh overruns, the current refresh will be skipped, but the next refresh will be scheduled at the following interval. Queries use the most recently synchronized catalog metadata, so changes made in the remote catalog, such as new tables, schema updates, or newly committed data, aren't visible in Lakehouse until the next background metadata refresh completes. 
  * **Lakehouse caching:** Lakehouse caching is enabled automatically for all cross-cloud queries to save egress costs by storing data blocks locally in Google Cloud. Customer-managed encryption keys (CMEK) are not supported for caching; cached data is encrypted using Google-owned and Google-managed encryption keys. If the `constraints/gcp.restrictNonCmekServices` organization policy constraint is enforced on any table in the query, caching is automatically disabled for that query. For more information, see [Intelligent caching](https://docs.cloud.google.com/lakehouse/docs/about-cross-cloud-data-access#intelligent-caching). 
  * **Data residency and compliance:** Creating a federated catalog or connection in a Google Cloud region stores cached data at rest in that target region. If your remote cloud data resides in a different jurisdiction, ensure that cross-region caching complies with your organization's data residency and regulatory compliance requirements. 



## General workflow

To access cross-cloud data, follow these general steps:

  * **Set up Cross-Cloud Interconnect (Optional):** Configure a private connection between your Google Cloud VPC and your remote cloud provider.
  * **Set up federation:** Configure authentication and create a federated catalog in Lakehouse. 
    * **OpenID Connect (OIDC) (Recommended):** Create the federated catalog in Lakehouse specifying the remote [Service Principal](https://docs.databricks.com/aws/en/admin/users-groups/manage-service-principals) Application ID, then [configure a federation policy](https://docs.databricks.com/aws/en/dev-tools/auth/oauth-federation-policy#workload-identity-federation) in Databricks using the Lakehouse catalog service account's unique ID.
    * **Secret-based authentication:** Create a secret in Secret Manager with your remote catalog credentials. Then, create a federated catalog in Lakehouse and grant the catalog service account access to the secret.
  * **Verify the connection:** Verify that Lakehouse can successfully connect to your remote catalog.
  * **Query data:** Run queries against your federated data using BigQuery or Managed Service for Apache Spark. Lakehouse caching is enabled automatically for queries to save egress costs. For more information, see [Query remote data](https://docs.cloud.google.com/lakehouse/docs/query-remote-data).
  * **Configure permissions:** Use Identity and Access Management (IAM) to manage who can view and query the federated data.



## Set up Cross-Cloud Interconnect (Optional)

Queries to your remote catalog travel over the public internet by default. To help enhance security and compliance, provide predictable performance, and reduce data transfer costs, use a private interconnect. This establishes a dedicated, private network connection between your Google Cloud Virtual Private Cloud (VPC) and your remote cloud provider's network (for example, AWS).

You can provision and configure either of the following private interconnect options between your Google Cloud VPC and your remote cloud provider's VPC (for example, AWS):

  * [**Dedicated Cross-Cloud Interconnect**](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview#setup-process): A dedicated physical connection.
  * [**Partner Cross-Cloud Interconnect**](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-cci-for-aws-overview): A connection through a supported service provider.



Establish BGP sessions between your Cloud Router in Google Cloud and your remote cloud provider's VPC to ensure route exchange.

To enable private querying, you must configure a path from Lakehouse to your remote storage bucket (for example, an AWS Amazon S3 bucket) through your private interconnect. There are two architectural flows you can follow to configure this routing:

  * **Internal regional proxy Network Load Balancer routing:** This flow uses a Google Cloud internal regional proxy Network Load Balancer to distribute requests across Hybrid Connectivity Network Endpoint Groups (NEGs) pointing to multiple AWS Elastic Network Interfaces (ENIs). This flow is essential for load balancing, scalability, and high availability. It is required for Partner CCI and recommended for Dedicated CCI for load balancing, scalability, and high availability.
  * **Direct endpoint routing:** This flow connects Service Directory directly to a single AWS Interface VPC Endpoint IP address. This flow only works for Dedicated CCI and is not supported for Partner CCI.



Select the configuration flow that matches your architecture requirements:

###  Internal regional proxy Network Load Balancer 

To configure an internal regional proxy Network Load Balancer to distribute requests across multiple AWS ENIs for high availability and load balancing, follow these steps:

**Configure AWS networking**

First, create an Amazon S3 VPC Interface Endpoint (AWS PrivateLink):

  1. In the AWS VPC console, create an Interface Endpoint for Amazon S3.
  2. For the service name, specify `com.amazonaws.AWS_REGION.s3`.
  3. Select the VPC and subnets that are connected through Direct Connect to your Google Cloud VPC.
  4. Attach Security Groups to the endpoint to control inbound access.
  5. This provisions Elastic Network Interfaces (ENIs) in each selected subnet. Note the private IP addresses of these ENIs.



Next, configure Security Groups:

  * Ensure that the Security Group or groups attached to the Amazon S3 Endpoint ENIs allow inbound TCP traffic on port `443` from your Google Cloud VPC. This must include the CIDR range of your Google Cloud proxy-only subnet to allow health checks and forwarded traffic.



**Configure Google Cloud networking**

**Important:** You must deploy all Google Cloud resources in this section (health check, hybrid NEGs, backend service, and load balancer) in the exact same region where your Cross-Cloud Interconnect VLAN attachment is located. If they are in different regions, traffic will fail to route to your remote storage.

To simplify setup, run the following commands to configure the internal load balancer. For advanced configurations or more details, see [Set up an Internal regional proxy Network Load Balancer for hybrid endpoints](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-hybrid).

**Note:** Before you begin, ensure you have a proxy-only subnet configured in your VPC network in the region. If you don't have one, run the following command to create it:
    
    
    gcloud compute networks subnets create PROXY_SUBNET_NAME \
        --purpose=REGIONAL_MANAGED_PROXY \
        --role=ACTIVE \
        --region=REGION \
        --network=VPC_NETWORK \
        --range=PROXY_SUBNET_RANGE

Replace the following:

  * `PROXY_SUBNET_NAME`: a name for the proxy-only subnet.
  * `PROXY_SUBNET_RANGE`: an unused CIDR range within your VPC network (for example, `10.129.0.0/23`).

**Important:** Cloud Router does not automatically advertise proxy-only subnets using BGP. You must manually configure your Cloud Router to advertise the CIDR range of your proxy-only subnet to your remote network (for example, AWS) using custom route advertisements. This ensures that response traffic from your remote storage can route back to the load balancer.

  1. Create a regional health check:
         
         gcloud compute health-checks create tcp HEALTH_CHECK_NAME \
             --region=REGION \
             --port=443

Replace the following:

     * `HEALTH_CHECK_NAME`: a name for the health check.
     * `REGION`: the Google Cloud region (for example, `us-east4`).
  2. Create hybrid Connectivity Network Endpoint Groups (NEGs) and add endpoints:

Create a hybrid NEG (`NON_GCP_PRIVATE_IP_PORT`) for each zone:
         
         gcloud compute network-endpoint-groups create NEG_NAME \
             --network-endpoint-type=NON_GCP_PRIVATE_IP_PORT \
             --zone=ZONE \
             --network=VPC_NETWORK

Add the private IP address of your AWS ENI to the corresponding hybrid NEG:
         
         gcloud compute network-endpoint-groups update NEG_NAME \
             --zone=ZONE \
             --add-endpoint="ip=AWS_S3_IP,port=443"

Replace the following:

     * `NEG_NAME`: a name for the hybrid NEG.
     * `ZONE`: the Google Cloud zone (for example, `us-east4-a`). This zone must reside within the region of your Cross-Cloud Interconnect VLAN attachment.
     * `VPC_NETWORK`: the name of your VPC network.
     * `AWS_S3_IP`: the private IP address of the AWS Amazon S3 VPC Endpoint (ENI) in that zone.

Repeat these commands to create NEGs and add endpoints for other zones if your AWS ENIs are distributed across multiple zones.

  3. Create and configure the backend service:

Create a regional backend service with internal managed load balancing:
         
         gcloud compute backend-services create BACKEND_SERVICE_NAME \
             --load-balancing-scheme=INTERNAL_MANAGED \
             --protocol=TCP \
             --region=REGION \
             --health-checks=HEALTH_CHECK_NAME \
             --health-checks-region=REGION

Add your hybrid NEGs to the backend service:
         
         gcloud compute backend-services add-backend BACKEND_SERVICE_NAME \
             --region=REGION \
             --network-endpoint-group=NEG_NAME \
             --network-endpoint-group-zone=ZONE \
             --balancing-mode=CONNECTION \
             --max-connections=MAX_CONNECTIONS

Replace the following:

     * `BACKEND_SERVICE_NAME`: a name for the backend service.
     * `NEG_NAME`: the name of the hybrid NEG you created in the previous step.
     * `ZONE`: the Google Cloud zone (for example, `us-east4-a`).
     * `MAX_CONNECTIONS`: the maximum concurrent connections the backend should handle (for example, `100`).

Repeat the `add-backend` command for each hybrid NEG you created.

  4. Configure the load balancer frontend:

Create a target TCP proxy:
         
         gcloud compute target-tcp-proxies create TARGET_PROXY_NAME \
             --backend-service=BACKEND_SERVICE_NAME \
             --region=REGION

Create a forwarding rule to route traffic to the target proxy:
         
         gcloud compute forwarding-rules create FORWARDING_RULE_NAME \
             --load-balancing-scheme=INTERNAL_MANAGED \
             --network=VPC_NETWORK \
             --subnet=VPC_SUBNET \
             --ports=443 \
             --region=REGION \
             --target-tcp-proxy=TARGET_PROXY_NAME \
             --target-tcp-proxy-region=REGION \
             --allow-global-access

Replace the following:

     * `TARGET_PROXY_NAME`: a name for the target proxy.
     * `FORWARDING_RULE_NAME`: a name for the forwarding rule.
     * `VPC_SUBNET`: the name of your VPC subnetwork.



After creating the forwarding rule for the load balancer, note the internal IP address assigned to it. This is your `ILB_IP_ADDRESS`.

**Configure Service Directory**

Register the ILB's IP address in Service Directory, so Lakehouse can discover it.

  1. Create a namespace for your remote cloud:
         
         gcloud service-directory namespaces create NAMESPACE \
             --project=PROJECT_ID \
             --location=REGION

Replace the following:

     * `NAMESPACE`: a unique identifier for your namespace.
     * `PROJECT_ID`: your Google Cloud project ID.
     * `REGION`: the Google Cloud region. For example, `us-east4`. This must be the same region as the federated catalog.
  2. Create a service in the Service Directory namespace:
         
         gcloud service-directory services create SERVICE_NAME \
             --namespace=NAMESPACE \
             --project=PROJECT_ID \
             --location=REGION

Replace the following:

     * `SERVICE_NAME`: a unique identifier for your service.
  3. Create an endpoint for the ILB in the service:
         
         gcloud service-directory endpoints create ENDPOINT_NAME \
             --project=PROJECT_ID \
             --namespace=NAMESPACE \
             --service=SERVICE_NAME \
             --location=REGION \
             --network=projects/PROJECT_NUMBER/global/networks/VPC_NETWORK \
             --address=ILB_IP_ADDRESS \
             --port=443

Replace the following:

     * `ENDPOINT_NAME`: a unique identifier for your endpoint.
     * `PROJECT_NUMBER`: your Google Cloud project number. Use your project number in the `--network` flag.
     * `ILB_IP_ADDRESS`: the internal IP address of your ILB forwarding rule.



###  Direct endpoint 

To configure Service Directory to route traffic directly to a single AWS Interface VPC Endpoint IP address, follow these steps:

  1. Create an [Interface VPC Endpoint](https://docs.aws.amazon.com/AmazonS3/latest/userguide/privatelink-interface-endpoints.html) for Amazon S3 inside your AWS VPC. Note the IP address and port of this endpoint.
  2. Create a namespace for your remote cloud:
         
         gcloud service-directory namespaces create NAMESPACE \
             --project=PROJECT_ID \
             --location=REGION

Replace the following:

     * `NAMESPACE`: a unique identifier for your namespace.
     * `PROJECT_ID`: your Google Cloud project ID.
     * `REGION`: the Google Cloud region. For example, `us-east4`. This must be the same region as the federated catalog.
  3. Create a service in the Service Directory namespace:
         
         gcloud service-directory services create SERVICE_NAME \
             --namespace=NAMESPACE \
             --project=PROJECT_ID \
             --location=REGION

Replace the following:

     * `SERVICE_NAME`: a unique identifier for your service.
  4. Create an endpoint in the service containing the routing information for your Amazon S3 Interface VPC Endpoint:
         
         gcloud service-directory endpoints create ENDPOINT_NAME \
             --service=SERVICE_NAME \
             --namespace=NAMESPACE \
             --project=PROJECT_ID \
             --location=REGION \
             --address=S3_VPCE_IP_ADDRESS \
             --port=S3_VPCE_PORT \
             --network=projects/PROJECT_NUMBER/global/networks/VPC_NETWORK

Replace the following:

     * `ENDPOINT_NAME`: a unique identifier for your endpoint.
     * `S3_VPCE_IP_ADDRESS`: the IP address of your Amazon S3 Interface VPC Endpoint. For example, `10.0.1.45`.
     * `S3_VPCE_PORT`: the port number of your Amazon S3 Interface VPC Endpoint. For example, `443`.
     * `PROJECT_NUMBER`: your Google Cloud project number. Use your project number in the `--network` flag.
     * `VPC_NETWORK`: the Google Cloud VPC network name associated with your private interconnect.



## Set up federation

To query your data, you must set up a Lakehouse federated catalog that connects to your remote Databricks Unity Catalog.

### Configure authentication

Federation requires authenticating to the remote catalog as a Databricks service principal. Choose one of the following authentication options:

###  OIDC 

OpenID Connect (OIDC) allows secretless authentication through [Databricks OAuth token federation](https://docs.databricks.com/aws/en/dev-tools/auth/oauth-federation).

  1. Create a [Service Principal](https://docs.databricks.com/aws/en/admin/users-groups/manage-service-principals) in your Databricks account that has read access to the target Unity Catalog and the `EXTERNAL USE SCHEMA` privilege on the target schemas or catalog.
  2. Save the **Application ID** (UUID) for the Service Principal. You will need this for a later step.



###  Secret-based 

This option uses an OAuth client ID and client secret stored securely with regional [Secret Manager](https://docs.cloud.google.com/secret-manager/regional-secrets/overview-rs) secrets.

  1. Create a [Service Principal](https://docs.databricks.com/aws/en/admin/users-groups/manage-service-principals) in your Databricks account that has read access to the target Unity Catalog.

  2. Generate an [OAuth secret](https://docs.databricks.com/aws/en/dev-tools/auth/oauth-m2m) for the service principal.

  3. Create a JSON file named `credentials.json` with your payload:
         
         {
             "client_id": "CLIENT_ID",
             "client_secret": "CLIENT_SECRET"
         }

Replace the following:

     * `CLIENT_ID`: The OAuth client ID for your Databricks Service Principal.
     * `CLIENT_SECRET`: The OAuth client secret for your Databricks Service Principal.
  4. Configure the regional endpoint for Secret Manager:

By default, Secret Manager uses a global endpoint. However, Lakehouse requires that your secrets be stored in the same region as your Lakehouse catalog. To interact with regional secrets using the `gcloud` CLI, you must override the default API endpoint for your current session or profile. For example, `secretmanager.us-east4.rep.googleapis.com`.
         
         gcloud config set api_endpoint_overrides/secretmanager https://secretmanager.REGION.rep.googleapis.com/

Replace the following:

     * `REGION`: The Google Cloud region where your Secret Manager secret is stored. For example, `us-east4`. To avoid connectivity issues, your secret and your catalog must be created in the same region.
  5. Upload the payload to Secret Manager:
         
         gcloud secrets create DATABRICKS_SECRET_NAME \
           --location="REGION" \
           --project="PROJECT_ID" \
           --data-file=credentials.json

Replace the following:

     * `DATABRICKS_SECRET_NAME`: A name for your Databricks secret.
     * `PROJECT_ID`: your Google Cloud project ID.



### Create a federated catalog

Create the federated catalog using the Google Cloud console or the `gcloud` CLI.

**Considerations:**

  * Only Databricks Unity Catalogs that use an [external location on AWS](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-external-locations) or an [external location on Google Cloud](https://docs.databricks.com/gcp/en/sql/language-manual/sql-ref-external-locations) are supported. Databricks Unity Catalogs that use [default storage on AWS](https://docs.databricks.com/aws/en/storage/default-storage) or [default storage on Google Cloud](https://docs.databricks.com/gcp/en/storage/default-storage) are _not supported_.

  * You must enable [external data access](https://docs.databricks.com/aws/en/external-access/admin) on the metastore used by Unity Catalog, which is disabled by default.

  * You must grant the `EXTERNAL USE SCHEMA` privilege to the Databricks Service Principal on the target schemas or catalog to enable credential vending for external data access. Without this privilege, background metadata refresh and credential vending for queries will fail.




###  Console 

To create a federated catalog:

  1. In the Google Cloud console, go to **Lakehouse**.

[Go to Lakehouse](https://console.cloud.google.com/biglake)

  2. Click add_box **Create catalog**.

  3. Click **Federated catalog**.

The **Catalog configuration** section appears.

  4. For **Federated catalog source** , select **Databricks (Unity)**.

  5. For **Data location** , select the Lakehouse region where you want to create the federated catalog. For example, `us-east4`. To minimize latency (even over public internet) do the following when selecting a region:

     * If your Unity Catalog is on AWS, select the Google Cloud region closest to your AWS region.
     * If your Unity Catalog is on Google Cloud, select the exact same region.
  6. Click **Continue**.

The **Connection details** section appears.

  7. In the **Remote catalog details** section, in the **Unity instance name** field, enter your target Databricks instance name. For example: `abcd.cloud.databricks.com`.

  8. In the **Unity catalog name** field, enter the name of the target Databricks Unity Catalog to federate to.

  9. Select an option for **Authentication Method** :

     * For **OIDC** , enter the Application ID for the Service Principal.
     * For **Secret** , enter the name of your secret. Use the following format: `projects/PROJECT_ID/locations/REGION/secrets/DATABRICKS_SECRET_NAME`.
  10. Optional: In the **Service directory name** field, enter the path to your Service Directory service. For example: `projects/PROJECT_ID/locations/REGION/namespaces/SERVICE_DIRECTORY_NAMESPACE/services/SERVICE_NAME`. This is only required if you are configuring a private interconnect (Cross-Cloud Interconnect).

  11. Click **Create**.




###  gcloud 

###  OIDC 

If you use OIDC, you must specify `--unity-service-principal-application-id`.

#### Public internet (no CCI)

If you don't configure CCI, the connection travels securely over the public internet.
    
    
    gcloud alpha biglake iceberg catalogs create FEDERATED_CATALOG_NAME \
        --project="PROJECT_ID" \
        --primary-location="REGION" \
        --catalog-type="federated" \
        --federated-catalog-type="unity" \
        --unity-service-principal-application-id="UNITY_SERVICE_PRINCIPAL_APPLICATION_ID" \
        --unity-instance-name="UNITY_INSTANCE_NAME" \
        --unity-catalog-name="UNITY_CATALOG_NAME" \
        --refresh-interval="REFRESH_INTERVAL" \
        --namespace-filters="NAMESPACE_FILTERS"

#### Customer-owned (CCI)

If you configured a private interconnect (such as Dedicated CCI or Partner CCI), provide the Service Directory service reference so that Lakehouse routes traffic privately.
    
    
    gcloud alpha biglake iceberg catalogs create FEDERATED_CATALOG_NAME \
        --project="PROJECT_ID" \
        --primary-location="REGION" \
        --catalog-type="federated" \
        --federated-catalog-type="unity" \
        --unity-service-principal-application-id="UNITY_SERVICE_PRINCIPAL_APPLICATION_ID" \
        --unity-instance-name="UNITY_INSTANCE_NAME" \
        --unity-catalog-name="UNITY_CATALOG_NAME" \
        --refresh-interval="REFRESH_INTERVAL" \
        --namespace-filters="NAMESPACE_FILTERS" \
        --service-directory-name="projects/PROJECT_ID/locations/REGION/namespaces/SERVICE_DIRECTORY_NAMESPACE/services/SERVICE_NAME"

Replace the following:

  * `FEDERATED_CATALOG_NAME`: a name for your federated catalog.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `REGION`: the Lakehouse region where the federated catalog is created. This must be the same region as the Service Directory namespace and regional secret. To minimize latency: 
    * If your Unity Catalog is on AWS, select the Google Cloud region closest to your AWS region.
    * If your Unity Catalog is on Google Cloud, select the exact same region.
  * `UNITY_SERVICE_PRINCIPAL_APPLICATION_ID`: The Application ID (UUID) of your Databricks Service Principal.
  * `UNITY_INSTANCE_NAME`: your target Databricks instance name. For example: `abcd.cloud.databricks.com`.
  * `UNITY_CATALOG_NAME`: the name of the target Databricks Unity Catalog to federate to.
  * `REFRESH_INTERVAL`: Specifies how often background metadata refresh runs. Set this value as a duration, for example, `330s` or `5m30s`.
  * `NAMESPACE_FILTERS`: Optional: A comma-separated list of namespaces to federate. For example, `ns1,ns2`. _If omitted, all namespaces will be included_.
  * If you are using a private interconnect (CCI): 
    * `SERVICE_DIRECTORY_NAMESPACE`: the Service Directory namespace you created during private interconnect setup.
    * `SERVICE_NAME`: the Service Directory service name you created during private interconnect setup.



###  Secret-based 

If you use secret-based authentication, you must specify `--secret-name`.

#### Public internet (no CCI)

If you don't configure CCI, the connection travels securely over the public internet.
    
    
    gcloud alpha biglake iceberg catalogs create FEDERATED_CATALOG_NAME \
        --project="PROJECT_ID" \
        --primary-location="REGION" \
        --catalog-type="federated" \
        --federated-catalog-type="unity" \
        --secret-name="projects/PROJECT_ID/locations/REGION/secrets/DATABRICKS_SECRET_NAME" \
        --unity-instance-name="UNITY_INSTANCE_NAME" \
        --unity-catalog-name="UNITY_CATALOG_NAME" \
        --refresh-interval="REFRESH_INTERVAL" \
        --namespace-filters="NAMESPACE_FILTERS"

#### Customer-owned (CCI)

If you configured a private interconnect (such as Dedicated CCI or Partner CCI), provide the Service Directory service reference so that Lakehouse routes traffic privately.
    
    
    gcloud alpha biglake iceberg catalogs create FEDERATED_CATALOG_NAME \
        --project="PROJECT_ID" \
        --primary-location="REGION" \
        --catalog-type="federated" \
        --federated-catalog-type="unity" \
        --secret-name="projects/PROJECT_ID/locations/REGION/secrets/DATABRICKS_SECRET_NAME" \
        --unity-instance-name="UNITY_INSTANCE_NAME" \
        --unity-catalog-name="UNITY_CATALOG_NAME" \
        --refresh-interval="REFRESH_INTERVAL" \
        --namespace-filters="NAMESPACE_FILTERS" \
        --service-directory-name="projects/PROJECT_ID/locations/REGION/namespaces/SERVICE_DIRECTORY_NAMESPACE/services/SERVICE_NAME"

Replace the following:

  * `FEDERATED_CATALOG_NAME`: a name for your federated catalog.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `REGION`: the Lakehouse region where the federated catalog is created. This must be the same region as the Service Directory namespace and regional secret. To minimize latency: 
    * If your Unity Catalog is on AWS, select the Google Cloud region closest to your AWS region.
    * If your Unity Catalog is on Google Cloud, select the exact same region.
  * `DATABRICKS_SECRET_NAME`: the name of your Databricks secret.
  * `UNITY_INSTANCE_NAME`: your target Databricks instance name. For example: `abcd.cloud.databricks.com`.
  * `UNITY_CATALOG_NAME`: the name of the target Databricks Unity Catalog to federate to.
  * `REFRESH_INTERVAL`: Specifies how often background metadata refresh runs. Set this value as a duration, for example, `330s` or `5m30s`.
  * `NAMESPACE_FILTERS`: Optional: A comma-separated list of namespaces to federate. For example, `ns1,ns2`. _If omitted, all namespaces will be included_.
  * If you are using a private interconnect (CCI): 
    * `SERVICE_DIRECTORY_NAMESPACE`: the Service Directory namespace you created during private interconnect setup.
    * `SERVICE_NAME`: the Service Directory service name you created during private interconnect setup.



### Complete authentication setup

Complete the authentication process using your chosen authentication type.

###  OIDC 

When the catalog is created, Lakehouse provisions a unique service account for it. You must retrieve the service account's numeric unique ID and use it to [configure a federation policy](https://docs.databricks.com/aws/en/dev-tools/auth/oauth-federation-policy#workload-identity-federation) for the Databricks Service Principal.

  1. Retrieve the Lakehouse catalog service account's numeric unique ID:
         
         gcloud alpha biglake iceberg catalogs describe FEDERATED_CATALOG_NAME \
             --project="PROJECT_ID" \
             --format='value(biglake-service-account-id)'

  2. In your Databricks account, configure a federation policy for the Service Principal you created earlier. Use the following values:

     * **Issuer URL** : `https://accounts.google.com`
     * **Subject** : the numeric unique ID of the Lakehouse catalog service account retrieved in the previous step.
     * **Audience** : `https://accounts.cloud.databricks.com`

Ensure that the Databricks Service Principal has read access to the target catalog and workspace, as well as the `EXTERNAL USE SCHEMA` privilege on the target schemas or catalog.




###  Secret-based 

When the catalog is created, Lakehouse provisions a unique service account for it (returned as `biglake-service-account` in the resource description).

You must grant this service account permission to access the secret you created earlier. Note that propagating IAM policies can take a few minutes.

Grant the catalog's service account permission to access the secret:
    
    
    gcloud config set api_endpoint_overrides/secretmanager https://secretmanager.REGION.rep.googleapis.com/
    gcloud secrets add-iam-policy-binding DATABRICKS_SECRET_NAME \
      --project="PROJECT_ID" \
      --location="REGION" \
      --member="serviceAccount:$(gcloud alpha biglake iceberg catalogs describe FEDERATED_CATALOG_NAME \
          --project="PROJECT_ID" \
          --format='value(biglake-service-account)')" \
      --role="roles/secretmanager.secretAccessor"

To verify that the federated catalog service account has access to the secret, run the following command:
    
    
    gcloud config set api_endpoint_overrides/secretmanager https://secretmanager.REGION.rep.googleapis.com/
    gcloud secrets get-iam-policy DATABRICKS_SECRET_NAME \
         --project="PROJECT_ID" \
         --location="REGION"

In the output, verify that the `biglake-service-account` service account has the `roles/secretmanager.secretAccessor` role assigned to it.

Ensure that the Databricks Service Principal has read access to the target catalog and workspace, as well as the `EXTERNAL USE SCHEMA` privilege on the target schemas or catalog.

### Complete private interconnect setup (Cross-Cloud Interconnect only)

If you are routing traffic over a private interconnect (Dedicated or Partner CCI), you must grant the Lakehouse catalog service account permissions to discover and authorize connections through Service Directory.

**Note:** The catalog service account is an internal Google Cloud service account (Service Agent). It might not be visible in your project's service account list in the Google Cloud console, but you can assign roles to it manually.

###  Console 

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Click **Grant Access** (or **Add**).

  3. In the **New principals** field, enter the Lakehouse catalog service account email address. You can retrieve this email address by describing the catalog (see the `gcloud` tab).

  4. In the **Role** menu, select **Service Directory Viewer** (`roles/servicedirectory.viewer`).

  5. Click **Add another role** and select **Service Directory PSC Authorized Service** (`roles/servicedirectory.pscAuthorizedService`).

  6. Click **Save**.




###  gcloud 

Grant the required roles to the catalog's service account:
    
    
    # Grant Service Directory Viewer
    gcloud projects add-iam-policy-binding PROJECT_ID \
    --member="serviceAccount:$(gcloud alpha biglake iceberg catalogs describe FEDERATED_CATALOG_NAME \
        --project="PROJECT_ID" \
        --format='value(biglake-service-account)')" \
    --role="roles/servicedirectory.viewer"
    
    # Grant Service Directory PSC Authorized Service
    gcloud projects add-iam-policy-binding PROJECT_ID \
    --member="serviceAccount:$(gcloud alpha biglake iceberg catalogs describe FEDERATED_CATALOG_NAME \
        --project="PROJECT_ID" \
        --format='value(biglake-service-account)')" \
    --role="roles/servicedirectory.pscAuthorizedService"

## Verify the connection

Verify that the catalog background metadata refresh cycle completed successfully and namespaces are synchronized.

  1. Verify that the refresh status indicates success:
         
         gcloud alpha biglake iceberg catalogs describe FEDERATED_CATALOG_NAME \
           --project="PROJECT_ID"

  2. Confirm that the namespaces are synchronized:
         
         gcloud alpha biglake iceberg namespaces list \
           --project="PROJECT_ID" \
           --catalog="FEDERATED_CATALOG_NAME"




## What's next

  * [Query remote data](https://docs.cloud.google.com/lakehouse/docs/query-remote-data).
  * [Troubleshoot cross-cloud data access for Databricks Unity Catalog](https://docs.cloud.google.com/lakehouse/docs/troubleshoot-cross-cloud-data-access-databricks).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
