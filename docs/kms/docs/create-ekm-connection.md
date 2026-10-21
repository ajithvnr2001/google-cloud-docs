---
url: https://docs.cloud.google.com/kms/docs/create-ekm-connection/
title: Create an EKM connection \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:24:31.853759+00:00
---

# Create an EKM connection  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/create-ekm-connection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Create an EKM connection Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to set up Cloud External Key Manager (Cloud EKM) to connect to your external key management (EKM) provider over a [Virtual Private Cloud (VPC) network](https://docs.cloud.google.com/vpc/docs/vpc).

You can use external keys over VPC in Cloud KMS locations that support EKM over VPC. For more information, see the [Cloud KMS Locations page](https://docs.cloud.google.com/kms/docs/locations).

If you're migrating existing `EXTERNAL` keys to the `EXTERNAL_VPC` protection level ([Preview](https://cloud.google.com/products#product-launch-stages)), then you must complete these setup steps first.

## Terminology

  * **EKM connection**

The Cloud KMS resource used to configure a connection to your external key manager. In the Google Cloud console, this is referred to as an **EKM via VPC connection**.

  * **VPC project**

The project that holds the VPC resource that is used to connect to your external key manager.

  * **Key projects**

The projects that hold EKM connection resources and Cloud EKM keys in Cloud KMS. A key project can be the same as a VPC project, but it is not required.

  * **Crypto space**

A container for your resources within your external key management partner. Your crypto space is identified by a unique crypto space path. The format of the crypto space path varies by external key management partner—for example, `v0/cryptospaces/YOUR_UNIQUE_PATH`.




## Before you begin

After you complete the steps below, you can begin using Cloud EKM keys to protect your data.

### Create a new project

  1. In the Google Cloud console, go to the **Manage resources** page.

[Go to Manage resources](https://console.cloud.google.com/project)

  2. Create a new Google Cloud project or select an existing project.

**Important:** The name you use must be between 4 and 30 characters. When you type the name, the form will suggest a project ID, which you can edit. The project ID you use must be between 6 and 30 characters, with a lowercase letter as the first character. You can use a dash, lowercase letter, or digit for the remaining characters, but the last character cannot be a dash. You should be aware that some resource identifiers (such as project IDs) might be retained beyond the life of your project. For this reason, avoid storing sensitive information in resource identifiers. ...see naming guidelines
  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

You can learn more about [Cloud EKM pricing](https://cloud.google.com/kms/pricing).




### Enable Cloud KMS

  1. Enable the Cloud Key Management Service API for the project.

[Enable the Cloud Key Management Service API](https://console.cloud.google.com/apis/enableflow?apiid=cloudkms.googleapis.com)

  2. Make a note of your project's Cloud EKM service account. In the following example, replace `PROJECT_NUMBER` with your Google Cloud project's [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). This information is also visible each time you use the Google Cloud console to create a Cloud EKM key.
         
         service-PROJECT_NUMBER@gcp-sa-ekms.iam.gserviceaccount.com
         




### Ensure gcloud CLI is up to date {: class="hide-from-toc"}

If you're going to use the Google Cloud CLI, ensure that it's up-to-date with the following command:

###  gcloud 
    
    
    gcloud components update
    

### Prepare a VPC network

There are two options when setting up a VPC network:

  * [Auto mode VPC network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#create-auto-network)
  * [Custom mode VPC network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#create-custom-network)



By default, new projects contain an auto mode VPC network that is [pre-populated with firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls#more_rules_default_vpc). If the VPC network won't be used for production purposes, the default auto mode VPC network is the quickest way to get started.

If your external key manager is running on-premises and you will connect to it by using hybrid connectivity, you should use a custom mode VPC network because it provides control over the subnet IP address ranges.

Follow these steps for setting up your VPC:

  1. **Enable private Google access**

The external key manager must verify the OIDC token contained in each request. To verify the token, the external key manager must retrieve the OAuth2 public key from the `www.googleapis.com` domain name. If the external key manager runs in Google Cloud and does not have access over the internet (e.g. a VM without an external IP or blocked by a firewall), follow the instructions for [configuring private Google access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access).

  2. **Firewall configuration for IP range`35.199.192.0/19`**

Requests from Cloud EKM will come from this range. Create both ingress and egress allow [firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) for TCP for the port on which the external key manager is listening.




#### Set up hybrid connectivity

If the external key manager is running on-premise, use a [hybrid connectivity solution](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product) to connect the VPC with your on-premises network. Once you have set up connectivity, follow these additional steps:

  1. **Enable Private Google Access**

The external key manager must verify the OIDC token contained in each request. To verify the token, the external key manager must retrieve the OAuth2 public key from the `www.googleapis.com` domain name. If the external key manager runs on-premise and doesn't have access over the internet, follow the instructions for [configuring private Google access for on-premises hosts](https://docs.cloud.google.com/vpc/docs/configure-private-google-access-hybrid).

  2. **Firewall configuration for IP range`35.199.192.0/19`**

Requests from Cloud EKM come from this range. Configure your on-premise network firewall or similar equipment to permit TCP traffic on the port on which the external key manager is listening.

  3. **Ensure that your VPC has a return route to IP range`35.199.192.0/19`**

Your on-premises network must have a route for the `35.199.192.0/19` destination. For information about how to meet this requirement, see return route strategies for on-premise targets.




#### Return route strategies for on-premise targets

  * For Cloud VPN tunnels that use static routing, manually create a route in your on-premises network whose destination is `35.199.192.0/19` and whose next hop is the Cloud VPN tunnel. For Cloud VPN tunnels that use policy-based routing, [configure the Cloud VPN's local traffic selector](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/choosing-networks-routing#traffic-selectors) and the on-premises VPN gateway's remote traffic selector to include `35.199.192.0/19`.

  * For Cloud VPN tunnels that use dynamic routing or for Cloud Interconnect, [configure custom advertisement mode](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/advertising-custom-ip) for `35.199.192.0/19` on the BGP session of the Cloud Router that manages the tunnel or VLAN attachment.




### Set up your external key manager

Follow the instructions from your EKM provider to set up your EKM.

#### Set up your crypto space

If you use Cloud EKM as part of a partner-managed EKM arrangement, these steps have been completed for you as part of your partner's provisioning process.

If your EKM provider is compatible with EKM key management from Cloud KMS, the following setup and configuration steps need to be made in your EKM:

  * Create a crypto space for your Cloud KMS-managed resources in your EKM.

  * Grant your Cloud KMS service account access to your crypto space and the keys created in it.

  * Set up Key Access Justifications policy to define which access justifications should be allowed or denied.




The exact process for each of these steps depends on your EKM. For more information, see your EKM provider's documentation.

### Create a Service Directory service endpoint

[Create and configure a Service Directory](https://docs.cloud.google.com/service-directory/docs/configuring-private-network-access) service endpoint in your VPC project that points to the private IP address and port of your your external key manager. If you are using a load balancer in front of multiple EKM replicas, use the load balancer's IP address and port. Ensure the **network** field of your Service Directory service endpoint is populated.

### Authorize Cloud EKM to access your VPC

For each key project, you must authorize Cloud EKM to access your VPC on that project's behalf, even if the key project and the VPC project are the same. By authorizing access, keys in your key project can use the VPC in your VPC project.

  1. Use the gcloud CLI to ensure a Cloud EKM service account exists for the project.
         
         gcloud beta services identity create \
             --service=cloudkms.googleapis.com \
             --project=KEY_PROJECT_ID
         

  2. Use the gcloud CLI to grant the [`servicedirectory.viewer`](https://docs.cloud.google.com/service-directory/docs/access-control#roles) and [`servicedirectory.pscAuthorizedService`](https://docs.cloud.google.com/service-directory/docs/access-control#roles) in your VPC project to `service-KEY_PROJECT_NUMBER@gcp-sa-ekms.iam.gserviceaccount.com` For help with getting your project ID and number, see [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).
         
         gcloud projects add-iam-policy-binding VPC_PROJECT_ID \
             --member=serviceAccount:service-KEY_PROJECT_NUMBER@gcp-sa-ekms.iam.gserviceaccount.com \
             --role=roles/servicedirectory.viewer
         
         gcloud projects add-iam-policy-binding VPC_PROJECT_ID \
             --member=serviceAccount:service-KEY_PROJECT_NUMBER@gcp-sa-ekms.iam.gserviceaccount.com \
             --role=roles/servicedirectory.pscAuthorizedService
         




## Create an EKM connection

To connect your external key manager to Cloud EKM, create an **EKM connection** in your _key project_.

**Note:** All Cloud KMS keys associated with an EKM connection need to reside in the same Google Cloud location as the EKM connection.**Note:** EKM connections with the same name can exist in different [locations](https://docs.cloud.google.com/kms/docs/locations), so you must always specify the location.

### Console

  1. In the Google Cloud console, go to the **KMS infrastructure** page.

[Go to KMS infrastructure](https://console.cloud.google.com/security/kms/infrastructure)

  2. Click add **Create connection**.

  3. For **Connection name** , enter a name for your connection.

  4. For **Region** , select a location for the EKM connection. Any Cloud KMS keys associated with this connection must be in the same location as the connection.

  5. For the **Service resource ID (self_link)** field, enter the value of the Service Directory service created in the Create a Service Directory service endpoint section. The service directory service must be in the same location as the connection.

  6. In the **Hostname** field, add the host name for your external key manager.

  7. In **Certificates** , click **Add certificate** to upload one or more X.509 server certificates for your external key manager. Certificates must be in DER format.

  8. For **EKM management mode** , select **Manual** to use the EKM connection for manually managed external keys, or select **Cloud KMS** to use the EKM connection for coordinated external keys.

  9. If you selected **Cloud KMS** for **EKM management mode** , then in the **Crypto space path** field, enter the crypto space path provided by your EKM.

  10. Optional. To set the EKM connection as the default connection for this project and location, select the **Set connection as the default** checkbox. If another EKM connection is currently set as the default connection for this project and location, this EKM connection replaces the existing default.

  11. Click **Create**.




### gcloud

To use Cloud KMS on the command line, first [Install or upgrade to the latest version of Google Cloud CLI](https://docs.cloud.google.com/sdk/install).

To create an EKM connection for manually managed external keys, run the following command:
    
    
    gcloud beta kms ekm-connections create EKM_CONNECTION \
        --location LOCATION \
        --service-directory-service SERVICE_DIRECTORY_SERVICE \
        --hostname HOSTNAME \
        --server-certificates-files SERVER_CERTIFICATE_FILES \
        --key-management-mode manual
    

Replace the following:

  * `EKM_CONNECTION`: a name for the EKM connection.
  * `LOCATION`: the Cloud KMS location where you want to create the EKM connection. Any Cloud KMS keys associated with this connection must be in the same location as the connection.
  * `SERVICE_DIRECTORY_SERVICE`: the resource ID of the Service Directory service for your connection.
  * `HOSTNAME`: the hostname of your external key manager.
  * `SERVER_CERTIFICATE_FILES`: a comma-separated list of files containing X.509 server certificates for your external key manager. Certificates must be in DER format.



To create an EKM connection for coordinated external keys, run the following command:
    
    
    gcloud beta kms ekm-connections create EKM_CONNECTION \
        --location LOCATION \
        --service-directory-service SERVICE_DIRECTORY_SERVICE \
        --hostname HOSTNAME \
        --server-certificates-files SERVER_CERTIFICATE_FILES \
        --key-management-mode cloud-kms \
        --crypto-space-path CRYPTO_SPACE_PATH
    

Replace the following:

  * `EKM_CONNECTION`: a name for the EKM connection.
  * `LOCATION`: the Cloud KMS location where you want to create the EKM connection. Any Cloud KMS keys associated with this connection must be in the same location as the connection.
  * `SERVICE_DIRECTORY_SERVICE`: the resource ID of the Service Directory service for your connection.
  * `HOSTNAME`: the hostname of your external key manager.
  * `SERVER_CERTIFICATE_FILES`: a comma-separated list of files containing X.509 server certificates for your external key manager. Certificates must be in DER format.
  * `CRYPTO_SPACE_PATH`: the crypto space path provided by your EKM provider.



For information on all flags and possible values, run the command with the `--help` flag.

### API

These examples use [curl](https://curl.haxx.se/) as an HTTP client to demonstrate using the API. For more information about access control, see [Accessing the Cloud KMS API](https://docs.cloud.google.com/kms/docs/accessing-the-api). 

To create an EKM connection for coordinated external keys, run the following command:
    
    
    curl "https://cloudkms.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/ekmConnections" \
        --request "POST" \
        --header "authorization: Bearer TOKEN" \
        --header "content-type: application/json" \
        --header "x-goog-user-project: PROJECT_ID" \
        --data '{
          "name": "EKM_CONNECTION",
          "serviceResolvers": [
            {
              "serviceDirectoryService": "SERVICE_DIRECTORY_SERVICE",
              "hostname": "HOSTNAME",
              "serverCertificates": [
                {
                  SERVER_CERTIFICATES
                }
              ]
            }
          ]
          "keyManagementMode": "CLOUD_KMS",
          "cryptoSpacePath": "CRYPTO_SPACE_PATH"
        }'
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where you want to create the EKM connection.
  * `LOCATION`: the Cloud KMS where you want to create the EKM connection.
  * `EKM_CONNECTION`: the name to use for the EKM connection.
  * `SERVER_CERTIFICATES`: a list of up to 10 `Certificate` objects that represent leaf server certificates.
  * `HOSTNAME`: the hostname of your external key manager.
  * `CRYPTO_SPACE_PATH`: the crypto space path provided by your EKM provider.



To create an EKM connection for manually managed external keys, run the following command:
    
    
    curl "https://cloudkms.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/ekmConnections" \
        --request "POST" \
        --header "authorization: Bearer TOKEN" \
        --header "content-type: application/json" \
        --header "x-goog-user-project: PROJECT_ID" \
        --data '{
          "name": "EKM_CONNECTION",
          "serviceResolvers": [
            {
              "serviceDirectoryService": "SERVICE_DIRECTORY_SERVICE",
              "hostname": "HOSTNAME",
              "serverCertificates": [
                {
                  SERVER_CERTIFICATES
                }
              ]
            }
          ]
        }'
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where you want to create the EKM connection.
  * `LOCATION`: the Cloud KMS where you want to create the EKM connection.
  * `EKM_CONNECTION`: the name to use for the EKM connection.
  * `SERVER_CERTIFICATES`: a list of up to 10 [`Certificate` objects](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.ekmConnections#Certificate) that represent leaf server certificates.
  * `HOSTNAME`: the hostname of your external key manager.



See the [`EkmConnection.create` API documentation](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.ekmConnections/create) for more information.

### Certificate status

Once you've uploaded a certificate for your EKM connection, you can check the overall certificate status of the EKM connection as well as the status of each certificate from the [KMS infrastructure page](https://console.cloud.google.com/security/kms/infrastructure).

EKM connections have an overall status in the **Certificate status** column of each connection. If an EKM connection has a status other than **Active** , we recommend updating the certificate(s) on your EKM connection.

Both EKM connections and individual certificates can have the following status:

  * **Active** : The certificate is valid and is not nearing its expiration date.
  * **Expiring within 30 days** : The certificate is valid, but has an expiration date in the next 30 days.
  * **Expired** : The certificate is expired and is no longer valid. We recommend updating any expired certificates.
  * **Not valid yet** : The certificate is not active. This can happen if the certificate's start date is in the future.



If your certificate is no longer valid, update your EKM connection in the Google Cloud console.

###  Console 

  1. In the Google Cloud console, go to the **KMS infrastructure** page.

[Go to KMS infrastructure](https://console.cloud.google.com/security/kms/infrastructure)

  2. Click the name of the EKM over VPC connection with the certificate that needs to be updated.

  3. Click **Edit connection**.

  4. Click **Add certificate** to upload one or more X.509 server certificates for your external key manager. Certificates must be in DER format.

  5. Remove the expired certificates. Hover over the expired certificate and select the **Delete** icon on the right.

  6. Click **Update connection** to update the EKM over VPC connection.




## Set an EKM connection as default

You can set an EKM connection as the default connection for a given project and location. When a default EKM connection is set for a project and location, new Cloud EKM by VPC keys created in key rings in that location use the indicated EKM connection unless another EKM connection is selected.

To set an EKM connection as the default for its project and location, complete the following steps:

###  Console 

  1. In the Google Cloud console, go to the **KMS infrastructure** page.

[Go to KMS infrastructure](https://console.cloud.google.com/security/kms/infrastructure)

  2. Click the EKM connection that you want to set as the default.

  3. Click **Edit connection**.

  4. Under **Default connection** , select the **Set connection as the default for LOCATION** checkbox.

  5. Click **Update connection**.




###  gcloud 
    
    
    gcloud kms ekm-config update
      --location=LOCATION
      --default-ekm-connection=projects/PROJECT_ID/locations/LOCATION/ekmConnections/DEFAULT_EKM_CONNECTION
    

Replace the following:

  * `LOCATION`: the Cloud KMS for which you want to set the default EKM connection.
  * `PROJECT_ID`: the name of the project for which you want to set the default EKM connection.
  * `DEFAULT_EKM_CONNECTION`: the name of the EKM connection that you want to set as the default for this location. The location of the EKM connection must match the location given in `LOCATION`.



###  REST 

To set the default EKM connection for a location, use the `EkmConfig.patch` method:
    
    
    curl "https://cloudkms.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/ekmConfig" \
        --request "PATCH" \
        --header "authorization: Bearer TOKEN" \
        --header "content-type: application/json" \
        --data '{"defaultEkmConnection": "projects/PROJECT_ID/locations/LOCATION/ekmConnections/DEFAULT_EKM_CONNECTION"}'
    

Replace the following:

  * `PROJECT_ID`: the ID of the project for which you want to set a default EKM connection.
  * `LOCATION`: the Cloud KMS for which you want to set the default EKM connection.
  * `DEFAULT_EKM_CONNECTION`: the name of the EKM connection that you want to set as the default for this location. The location of the EKM connection must match the location given in `LOCATION`.



If another EKM connection had been set as the default for this location, the selected EKM connection replaces it as the default. Only one EKM connection can be default for a given project and location.

## What's next

  * [Create an external key](https://docs.cloud.google.com/kms/docs/create-external-key).
  * Optionally, you can [migrate external keys][migrate] ([Preview](https://cloud.google.com/products#product-launch-stages)).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
