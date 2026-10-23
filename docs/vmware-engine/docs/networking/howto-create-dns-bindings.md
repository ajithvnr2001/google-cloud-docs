---
url: https://docs.cloud.google.com/vmware-engine/docs/networking/howto-create-dns-bindings/
title: Configure DNS bindings \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:55.249152+00:00
---

# Configure DNS bindings  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/networking/howto-create-dns-bindings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure DNS bindings

This page describes how to configure DNS bindings for _Standard VMware Engine Networks_.

**Note:** Cloud DNS and DNS bindings are only available for Standard VMware Engine networks. For Legacy VMware Engine Networks see, [Create DNS forwarding rules](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-legacy-conditional-dns-forwarding).

Each private cloud deploys a Cloud DNS Server that is used for all management appliances resolution. You can configure this server as the DNS server for all VMware workloads by setting up DNS bindings. To do so, you need to:

  1. Get the IP address of the Private Cloud's DNS server
  2. Set up DNS bind permissions to allow a user principal to bind to the intranet VPC
  3. Configure DNS for your VMware workloads or NSX segment DHCP DNS setting



## Before you begin

You can only configure DNS bindings using the `gcloud` tool or the API.

### gcloud and API requirements

To use the `gcloud` command line tool or the API to manage your VMware Engine resources, we recommend configuring the tools as described below.

###  gcloud 

  1. Set your default project ID:
         
         gcloud config set project PROJECT_ID
         

  2. Set a default region and zone:
         
         gcloud config set compute/region REGION
         
         
         gcloud config set compute/zone ZONE
         




For more information on the `gcloud vmware` tool, [see the Cloud SDK reference docs](https://docs.cloud.google.com/sdk/gcloud/reference/vmware).

###  API 

API examples in this documentation set use the `cURL` command-line tool to query the API. A valid access token is required as part of the `cURL` request. There are many ways to get a valid access token; the following steps use the `gcloud` tool to generate a access token:

  1. Login to Google Cloud:
         
         gcloud auth login
         

  2. Generate access token and export to TOKEN:
         
         export TOKEN=`gcloud auth print-access-token`
         

  3. Verify that TOKEN is set properly:
         
         echo $TOKEN
         




Now, use the authorization token in your requests to the API. For example:
    
    
    curl -X GET -H "Authorization: Bearer \"$TOKEN\"" -H "Content-Type: application/json; charset=utf-8" https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations
    

### Python

Python code samples in this documentation use the [VMware Engine library](https://cloud.google.com/python/docs/reference/vmwareengine/latest) to communicate with the API. To be able to use this approach, the library needs to be installed and the [Application Default Credentials](https://cloud.google.com/docs/authentication/application-default-credentials) should be configured.

  1. Download and install the Python library:
         
         pip install google-cloud-vmwareengine
         

  2. Configure the ADC information by executing those command in your shell:
         
         gcloud auth application-default login
         

Or, use a Service Account key file:
         
         export GOOGLE_APPLICATION_CREDENTIALS="FILE_PATH"
         




For more information about the library, visit the [reference page](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest) or view [code samples on GitHub](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/vmwareengine/cloud-client).

## Get a private cloud workload DNS server IP

###  Console 

To get the IP address of your private cloud's DNS server, follow these steps.

  1. In the Google Cloud console, go to the **Private clouds** page.

[Go to Private clouds](https://console.cloud.google.com/vmwareengine/privateclouds)

  2. Click **Select a project** and then select the organization, folder, or project that contains the private cloud you want to connect to.

  3. Click the name of the private cloud.

  4. On the **Summary** page for the private cloud, under **Private Cloud DNS servers** , click **Copy** to copy the private Cloud DNS server IP address.




###  gcloud 

To get the IP address of your private cloud's DNS server using Google Cloud CLI, use the [`gcloud vmware private-clouds describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/describe):
    
    
     gcloud vmware private-clouds describe PRIVATE_CLOUD_ID \
      --project=PROJECT_ID \
      --location=REGION

Replace the following:

  * `PRIVATE_CLOUD_ID`: the private cloud name for this request
  * `PROJECT_ID`: the project ID for this request
  * `REGION`: the region of the private cloud; if this is stretched private cloud, specify the zone for this private cloud



###  API 

To get the IP address of your private cloud's DNS server using the VMware Engine API, make a `GET` request:
    
    
    curl -X GET -H "Authorization: Bearer TOKEN"  -H "Content-Type: application/json; charset=utf-8" "https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/privateCloud/PRIVATE_CLOUD_ID"

Replace the following:

  * `PROJECT_ID`: the project ID for this request
  * `REGION`: the region of the private cloud; if this is stretched private cloud, specify the zone for this private cloud
  * `PRIVATE_CLOUD_ID`: the private cloud name for this request.



## Set up DNS bind permissions

You can only set up and manage DNS bind permissions using the `gcloud` tool or directly using the REST API. It is not possible to set up bindings through the console.

### Grant DNS bind permission

In order for a user to configure DNS bindings, you must grant a user principal the permission to bind to the intranet VPC. In this case, a user principal is the email address of the user who will bind the private DNS zone with the intranet VPC.

###  gcloud 
    
    
    gcloud vmware dns-bind-permission grant \
      --user=USER \
      --project=PROJECT_ID

Replace the following:

  * `USER`: the email of the user who is going to bind the private DNS zone with the intranet VPC; for example, `example1@gmail.com`
  * `PROJECT_ID`: the project ID for this request

**Note:** The `gcloud vmware dns-bind-permission grant` command must be run in a project with an existing VMware Engine network.

###  API 

Make a `POST` request to `dnsBindPermissions:grant` method and provide the user email address in the request body.
    
    
    curl -X POST -H "Authorization: Bearer TOKEN"  -H "Content-Type: application/json; charset=utf-8" https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/dnsBindPermission:grant -d '
    {
    "principal": {
      "user": "USER"
    }
    }'

Replace the following:

  * `PROJECT_ID`: the project for this request.
  * `USER`: the email of the user for whom you want to revoke permissions. For example, `example1@gmail.com`.



### Revoke DNS Bind Permission

Revokes the DNS Bind Permission that was previously granted to the user.

###  gcloud 
    
    
    gcloud vmware dns-bind-permission revoke \
      --user=USER \
      --project=PROJECT_ID

Replace the following:

  * `USER`: the email of the user for whom you want to revoke permissions; for example, `example1@gmail.com`
  * `PROJECT_ID`: the project ID for this request



###  API 

Make a `POST` request to `dnsBindPermissions:revoke` and provide the user email address in the request body.
    
    
    curl -X POST -H "Authorization: Bearer TOKEN"  -H "Content-Type: application/json; charset=utf-8" https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/dnsBindPermission:revoke -d '
    {
    "principal": {
      "user": "USER"
    }
    }'

Replace the following:

  * `PROJECT_ID`: the project for this request.
  * `USER`: the email of the user for whom you want to revoke permissions. For example, `example1@gmail.com`.



## Describe DNS bind Permission

Describes DNS bind permissions for a project and which user principal has access to configure DNS bindings.

###  gcloud 
    
    
    gcloud vmware dns-bind-permission describe \
    --project=PROJECT_ID

Replace `PROJECT_ID` with the project ID for this request.

###  API 

Make a `GET` request to `dnsBindPermissions` resource.
    
    
    curl -X GET -H "Authorization: Bearer TOKEN"  -H "Content-Type: application/json; charset=utf-8" https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/dnsBindPermission

Replace `PROJECT_ID` with the project for this request.

## Binding Private Cloud DNS Zone with the VMware Engine network intranet VPC

Once you grant a user principal the permissions to configure DNS bindings, the user can create a binding between the private DNS zone in Cloud DNS and the intranet VPC of the VMware Engine Network. VMware Engine uses [DNS peering](https://docs.cloud.google.com/dns/docs/zones/peering-zones) to facilitate Cloud DNS resolution.

### Locating the Intranet VPC URL

You need the network intranet VPC URL to create the new binding. The VMware Engine network intranet VPC can be found by listing the details of the VMware Engine network.

###  Console 

To locate the Intranet VPC URL using the Google Cloud console, follow these steps:

  1. In the Google Cloud console, go to the **VMware Engine networks** page.

[Go to VMware Engine networks](https://console.cloud.google.com/vmwareengine/networks)

  2. Click **Select a project** and then select the organization, folder, or project that contains the VMware Engine network.

  3. Locate the VMware Engine Network, click the **Action** option and select **Copy Intranet VPC network URL**.




###  gcloud 
    
    
    gcloud vmware networks describe VMWARE_ENGINE_NETWORK \
    --project=PROJECT_ID

Replace the following:

  * `VMWARE_ENGINE_NETWORK`: the network to describe
  * `PROJECT_ID`: the project ID for this request



###  API 

Make a `GET` request to the `vmwareEngineNetworks` resource and provide the name of the network:
    
    
    curl -X GET -H "Authorization: Bearer TOKEN"  -H "Content-Type: application/json; charset=utf-8" https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/vmwarenEngineNetworks/NETWORK_ID

Replace the following:

  * `PROJECT_ID`: the project for this request
  * `NETWORK_ID`: the network to describe



### Binding

The intended workflow, once bind permissions are configured, is to add a DNS peering to the VMware Engine network intranet VPC into your standard Cloud DNS zone management process for each zone.

###  gcloud 
    
    
    gcloud dns managed-zones create peering-DOMAIN  \
    --dns-name="DOMAIN" \
    --visibility="private" \
    --networks="INTRANET_VPC_URL" \
    --target-project="PROJECT_ID" \
    --target-network="EXISTING_VPC" \
    --description="DESCRIPTION"

Replace the following:

  * `DOMAIN`: the domain to extended, example `zone1.example.com`
  * `INTRANET_VPC_URL`: the intranet VPC URL for the VMware Engine network
  * `EXISTING_VPC`: the URL of the existing VPC network that the `DOMAIN` is already bound to
  * `PROJECT_ID`: the project ID for this request



###  API 

Make a `PATCH` request to the `managedZones` resource and provide the name of the zone:
    
    
    curl -X POST -H "Authorization: Bearer TOKEN"  -H "Content-Type: application/json; charset=utf-8" https://dns.googleapis.com/v1/projects/PROJECT_ID/managedZones -d "{
    "name": "peering-DOMAIN",          
    "description": "",
    "dnsName": DOMAIN,
    "peeringConfig": {
        "targetNetwork": {
            "networkUrl": EXISTING_VPC
        }
      },
      "privateVisibilityConfig": {
        "networks": [
          {
            "networkUrl": INTRANET_VPC_URL
          }
        ]
      }  
    }"

Replace the following:

  * `PROJECT_ID`: the project ID for this request
  * `DOMAIN`: the domain to extended, example `zone1.example.com`
  * `INTRANET_VPC_URL`: the intranet VPC URL for the VMware Engine network.
  * `EXISTING_VPC`: the URL of the existing VPC network that the DOMAIN is already bound to



## Example DNS Bindings

The following are some example DNS bindings you might use.

### Authoritative
    
    
    gcloud dns managed-zones create zone1 \
      --dns-name="zone1.example.com." \
      --visibility="private" \
      --description="DESCRIPTION" \
      --networks="EXISTING_VPC"
    
    
    gcloud dns managed-zones create peering-zone1 \
      --dns-name="zone1.example.com." \
      --visibility="private" \
      --networks="INTRANET_VPC_URL" \
      --target-project="PROJECT_ID" \
      --target-network="EXISTING_VPC" \
      --description="DESCRIPTION"

### Conditional Forwarding
    
    
    gcloud dns managed-zones create zone1 \
      --description="DESCRIPTION" \
      --dns-name="zone1.example.com." \
      --visibility="private" \
      --networks=EXISTING_VPC \
      --forwarding-targets="DNS_SERVER_IP1","DNS_SERVER_IP2"
    
    
    gcloud dns managed-zones create peering-zone1 \
      --dns-name="zone1.example.com." \
      --visibility="private" \
      --networks="INTRANET_VPC_URL" \
      --target-project="PROJECT_ID" \
      --target-network="EXISTING_VPC" \
      --description="DESCRIPTION"

### Forwarding All
    
    
    gcloud dns managed-zones create forward-all \
      --description="" --dns-name="." \
      --visibility="private" \
      --networks="EXISTING_VPC" \
      --forwarding-targets="DNS_SERVER_IP1","DNS_SERVER_IP2"
    
    
    gcloud dns managed-zones create peering-forward-all \
      --dns-name="." \
      --visibility="private" \
      --networks="INTRANET_VPC_URL" \
      --target-project="PROJECT_ID" \
      --target-network="EXISTING_VPC" \
      --description="DESCRIPTION"

### Google API Private
    
    
    gcloud dns managed-zones create googleapis \
      --dns-name="googleapis.com." \
      --visibility="private" \
      --description="Direct GCVE traffic to Private IPs for Google API Access" \
      --networks="EXISTING_VPC"
    
    
    gcloud dns managed-zones create peering-googleapis  \
      --dns-name="googleapis.com." \
      --visibility="private" \
      --networks="INTRANET_VPC_URL" \
      --target-project="PROJECT_ID" \
      --target-network="EXISTING_VPC" \
      --description="DESCRIPTION"
    
    
    gcloud dns record-sets create private.googleapis.com. \
      --zone="googleapis" \
      --type="A" \
      --ttl="300" \
      --rrdatas="199.36.153.8,199.36.153.9,199.36.153.10,199.36.153.11"
    
    
    gcloud dns record-sets create *.googleapis.com. \
      --zone="googleapis" \
      --type="CNAME" \
      --ttl="300" \
      --rrdatas="private.googleapis.com."

### Google API Restricted
    
    
    gcloud dns managed-zones create googleapis \
      --dns-name="googleapis.com." \
      --visibility="private" \
      --description="Direct GCVE traffic to Private IPs for Google API Access" \
      --networks="EXISTING_VPC"
    
    
    gcloud dns managed-zones create peering-googleapis \
      --dns-name="googleapis.com." \
      --visibility="private" \
      --networks="INTRANET_VPC_URL" \
      --target-project="PROJECT_ID" \
      --target-network="EXISTING_VPC" \
      --description="DESCRIPTION"
    
    
    gcloud dns record-sets create restricted.googleapis.com. \
      --zone="googleapis" \
      --type="A" \
      --ttl="300" \
      --rrdatas="199.36.153.4, 199.36.153.5, 199.36.153.6, 199.36.153.7"
    
    
    gcloud dns record-sets create *.googleapis.com. \
      --zone="googleapis" \
      --type="CNAME" \
      --ttl="300" \
      --rrdatas="restricted.googleapis.com."

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
