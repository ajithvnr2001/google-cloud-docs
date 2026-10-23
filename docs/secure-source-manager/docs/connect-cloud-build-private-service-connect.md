---
url: https://docs.cloud.google.com/secure-source-manager/docs/connect-cloud-build-private-service-connect/
title: Connect Cloud Build to a Private Service Connect instance \u00a0|\u00a0 Secure Source Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:11.669999+00:00
---

# Connect Cloud Build to a Private Service Connect instance  |  Secure Source Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-source-manager/docs/connect-cloud-build-private-service-connect/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Secure Source Manager ](https://docs.cloud.google.com/secure-source-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-source-manager/docs/overview)



Send feedback 

#  Connect Cloud Build to a Private Service Connect instance Stay organized with collections  Save and categorize content based on your preferences. 

You can connect Cloud Build to a Secure Source Manager Private Service Connect instance using [Cloud Build private pools](https://docs.cloud.google.com/build/docs/private-pools/private-pools-overview). This connection is a more complex alternative to using [Developer Connect](https://docs.cloud.google.com/developer-connect/docs/connect-secure-source-manager). Use the approach outlined in this guide if you aren't comfortable exposing a git proxy endpoint.

## Before you begin

  1. [Create a Private Service Connect Secure Source Manager instance](https://docs.cloud.google.com/secure-source-manager/docs/create-private-service-connect-instance).
  2. If you previously configured the endpoints for your Private Service Connect instance, then you must disconnect them. To release your endpoints, follow the instructions in [Release a static internal IPv4 or IPv6 address](https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address#delete_a_static_internal_ip_address).
  3. Enable the Cloud Build, Service Networking, and Compute Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,servicenetworking.googleapis.com,compute.googleapis.com)




## Required roles

To get the permissions that you need to connect Cloud Build to a Private Service Connect Secure Source Manager instance, ask your administrator to grant you the [Access Context Manager Admin role ](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyAdmin) (`roles/accesscontextmanager.policyAdmin`) IAM role on the organization. 

## Configure your service account

To follow the [principle of least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely) in Cloud Build, you can configure Cloud Build to use a service account with just enough privileges to execute a build.

If you don't specify a service account, Cloud Build might automatically select a service account to execute builds on your behalf. This service account might have permissions that are unnecessarily broad for your use-case, like access to your Secure Source Manager instance and any repositories in your project.

  1. [Create a service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) if you don't already have one you want to use.

  2. In the Google Cloud console, go to the _settings_ Secure Source Manager **Permissions** page: 

[Go to **Permissions**](https://console.cloud.google.com/cloud-build/settings)

  3. In the **Service account permissions** tab, select the service account you want to use as the Cloud Build service account.

  4. Optionally, select **Set as preferred service account** to pre-populate your service account when you create new triggers.




### Grant the service account required permissions

  1. Grant the service account the required Cloud Build roles for your use-case. For information on what Cloud Build roles are required for different Cloud Build actions, see [Configuring access to Cloud Build](https://docs.cloud.google.com/build/docs/securing-builds/configure-access-to-resources).

  2. To grant the service account permissions to retrieve the CA certificate, run the following command.
         
         gcloud projects add-iam-policy-binding CA_PROJECT_ID \
           --member=serviceAccount:SA_EMAIL \
           --role=roles/privateca.auditor \
           --condition=None
         

Replace the following:

     * `CA_PROJECT_ID`: with the project ID of the CA pool project.
     * `SA_EMAIL`: with the email of the service account you set as your Cloud Build service account.
  3. To grant the service account permissions to access the Secure Source Manager instance, run the following command.
         
         gcloud projects add-iam-policy-binding INSTANCE_PROJECT_ID \
           --member=serviceAccount:SA_EMAIL \
           --role=roles/securesourcemanager.instanceAccessor \
           --condition=None
         

  4. To grant the service account permissions to read from Secure Source Manager repositories, run the following command.
         
         gcloud projects add-iam-policy-binding INSTANCE_PROJECT_ID \
           --member=serviceAccount:SA_EMAIL \
           --role=roles/securesourcemanager.repoReader \
           --condition=None
         




### Set up build logs

When you specify your own service account for builds, you must store your build logs either in Cloud Logging or in a user-created Cloud Storage bucket. You can't store your logs in the default logs bucket.

To store build logs in Cloud Logging, grant the [Logs Writer (`roles/logging.logWriter`) role](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.logWriter) to your Cloud Build service account.

For more information on how to set up your build logs, see [Configure user-specified service accounts](https://docs.cloud.google.com/build/docs/securing-builds/configure-user-specified-service-accounts#set_up_build_logs).

## Create a private Cloud DNS zone

To create a managed private Cloud DNS zone, run the following command.
    
    
    gcloud dns managed-zones create ZONE_NAME \
        --project=PROJECT_ID \
        --description=DESCRIPTION \
        --dns-name="INSTANCE_LOCATION.p.sourcemanager.dev." \
        --visibility="private" \
        --networks="https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/NETWORK"
    

Replace the following:

  * `ZONE_NAME`: with the name you want to give the managed-zone.
  * `PROJECT_ID`: with the project ID of the Google Cloud project you want to use for the Cloud DNS zone.
  * `DESCRIPTION`: with a description for the zone.
  * `INSTANCE_LOCATION`: with the location where you want to create your Secure Source Manager instance.



For more information on managed private Cloud DNS zones, see [Cloud DNS overview](https://docs.cloud.google.com/dns/docs/overview).

## Configure your Virtual Private Cloud (VPC) network

  1. Reserve an IP range that you want to use to peer the Secure Source Manager VPC with the Cloud Build private pool.
         
         gcloud compute addresses create CB_PEER_RANGE \
           --global \
           --purpose=VPC_PEERING \
           --prefix-length=24 \
           --description="IP range for peering with Cloud Build private pool" \
           --network=NETWORK \
           --project=INSTANCE_PROJECT_ID
         

Replace the following:

     * `CB_PEER_RANGE`: with the name of the address to create.
     * `NETWORK`: with the network resource in which the addresses should be reserved. If you're using the [default network](https://docs.cloud.google.com/vpc/docs/vpc#default-network), the value is `default`.
     * `INSTANCE_PROJECT_ID`: with the Private Service Connect instance project ID.
  2. To create a VPC peering with `servicenetworking.googleapis.com`, run the following command.
         
         gcloud services vpc-peerings connect \
           --service=servicenetworking.googleapis.com \
           --ranges=CB_PEER_RANGE \
           --network=NETWORK \
           --project=INSTANCE_PROJECT_ID
         

  3. To create a peered DNS domain to connect with Cloud Build, run the following command.
         
         gcloud services peered-dns-domains create DNS_PEERING_DOMAIN \
           --network=NETWORK \
           --project=INSTANCE_PROJECT_ID \
           --dns-suffix=INSTANCE_LOCATION.p.sourcemanager.dev.
         

Replace the following:

     * `DNS_PEERING_DOMAIN`: with the name of the peered DNS domain you are creating.

Private DNS zones must be explicitly shared. For more information on sharing private DNS zones, see [Share private DNS zones with service producers](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#dns-peering).

  4. To export network routes to Cloud Build, run the following command.
         
         gcloud compute networks peerings update servicenetworking-googleapis-com \
           --network=NETWORK \
           --export-custom-routes \
           --no-export-subnet-routes-with-public-ip \
           --project=INSTANCE_PROJECT_ID
         

  5. To create the Cloud Build private pool in the same Google Cloud project as the Private Service Connect instance, run the following command.
         
         gcloud builds worker-pools create PRIVATE_POOL_ID \
           --project=INSTANCE_PROJECT_ID \
           --region=INSTANCE_LOCATION \
           --peered-network=projects/INSTANCE_PROJECT_ID/global/networks/NETWORK \
           --worker-disk-size=100 \
           --no-public-egress
         

Where `PRIVATE_POOL_ID` is the name for the private pool you are creating. The name must be between 1-63 characters, and valid characters are `[a-zA-Z0-9_-]+`.

  6. To Create a Private Service Connect Network Endpoint Group (NEG) for the HTTP endpoint, run the following command:
         
         gcloud compute network-endpoint-groups create HTTP_NEG_NAME \
             --project=INSTANCE_PROJECT_ID \
             --region=INSTANCE_LOCATION \
             --network-endpoint-type=PRIVATE_SERVICE_CONNECT \
             --psc-target-service=HTTP_PSC \
             --network=NETWORK --subnet=SUBNET
         

Where:

     * `HTTP_NEG_NAME` is the name of the NEG you want to create for the HTTP endpoint.
     * `HTTP_PSC` is the HTTP Private Service Connect endpoint value.
  7. To create a Private Service Connect NEG for the SSH endpoint, run the following command:
         
         gcloud compute network-endpoint-groups create SSH_NEG_NAME \
           --project=INSTANCE_PROJECT_ID \
           --region=INSTANCE_LOCATION \
           --network-endpoint-type=PRIVATE_SERVICE_CONNECT \
           --psc-target-service=SSH_PSC \
           --network=NETWORK --subnet=SUBNET
         

Where:

     * `SSH_NEG_NAME` is the name of the NEG you want to create for the SSH endpoint.
     * `SSH_PSC` is the SSH Private Service Connect endpoint value.



## Set up a proxy internal load balancer (ILB)

Endpoints are not accessible from peered VPC networks. To access the Secure Source Manager endpoints, you must set up an [L4 internal load balancer (ILB)](https://docs.cloud.google.com/load-balancing/docs/internal) for each endpoint. For more information on accessing published services through endpoints, see [About accessing published services through endpoints](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints).

  1. To create a [proxy-only subnet for ILBs](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets), run the following command.
         
         gcloud compute networks subnets create ILB_PROXY_SUBNET_NAME \
         --purpose=REGIONAL_MANAGED_PROXY \
         --role=ACTIVE \
         --region=INSTANCE_LOCATION \
         --network=NETWORK \
         --range=CIDR_RANGE \
         --project=INSTANCE_PROJECT_ID
         

Where:

     * `ILB_PROXY_SUBNET_NAME` is the name of the subnet to create.
     * `CIDR_RANGE` is the primary IP address range of the subnet. You must use a subnet mask no longer than `26` so that at least 64 IP addresses are available for proxies in the region. The recommended subnet mask length is `/23`. For more information on proxy-only subnets, see [Proxy-only subnets for Envoy-based load balancers](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets).
  2. To create L4 ILB for the HTTP connection NEG, run the following command.
         
         gcloud compute backend-services create HTTP_PROXY_ILB \
           --project=INSTANCE_PROJECT_ID \
           --region=INSTANCE_LOCATION \
           --load-balancing-scheme=INTERNAL_MANAGED
         

Where `HTTP_PROXY_ILB` is the name of the ILB to create for the HTTP endpoint.

  3. To create an L4 ILB for the SSH connection NEG, run the following command.
         
         gcloud compute backend-services create SSH_PROXY_ILB \
             --project=INSTANCE_PROJECT_ID \
             --region=INSTANCE_LOCATION \
             --load-balancing-scheme=INTERNAL_MANAGED
         

Where `SSH_PROXY_ILB` is the name of the ILB to create for the SSH endpoint.




### Register the Private Service Connect NEG as the ILBs' backend

  1. To register the HTTP NEG, run the following command.
         
         gcloud compute backend-services add-backend HTTP_PROXY_ILB \
           --network-endpoint-group=HTTP_NEG_NAME \
           --network-endpoint-group-region=INSTANCE_LOCATION \
           --project=INSTANCE_PROJECT_ID
         

  2. To register the SSH NEG, run the following command.
         
         gcloud compute backend-services add-backend SSH_PROXY_ILB \
           --network-endpoint-group=SSH_NEG_NAME \
           --network-endpoint-group-region=INSTANCE_LOCATION \
           --project=INSTANCE_PROJECT_ID
         




### Create target TCP proxies for the ILBs

  1. To create a target TCP proxy for the HTTP ILB, run the following command.
         
         gcloud compute target-tcp-proxies create ILB_HTTP_TCP_TARGET_PROXY \
           --backend-service=HTTP_PROXY_ILB \
           --region=INSTANCE_LOCATION \
           --project=INSTANCE_PROJECT_ID
         

Where `ILB_HTTP_TCP_TARGET_PROXY` is the name of the target TCP proxy you want to create for the HTTP ILB.

  2. To create a target TCP proxy for the SSH ILB, run the following command.
         
         gcloud compute target-tcp-proxies create ILB_SSH_TCP_TARGET_PROXY \
           --backend-service=SSH_PROXY_ILB \
           --region=INSTANCE_LOCATION \
           --project=INSTANCE_PROJECT_ID
         

Where `ILB_SSH_TP_TARGET_PROXY` is the name of the target TCP proxy you are creating for the SSH ILB.




### Create forwarding rules to route traffic to the ILBs

  1. To create a forwarding rule for routing traffic to the HTTP ILB, run the following command.
         
         gcloud compute forwarding-rules create HTTP_PROXY_FORWARD \
             --project=INSTANCE_PROJECT_ID \
             --ports 443 \
             --target-tcp-proxy=ILB_HTTP_TCP_TARGET_PROXY \
             --target-tcp-proxy-region=INSTANCE_LOCATION \
             --network-tier PREMIUM \
             --load-balancing-scheme=INTERNAL_MANAGED \
             --network=NETWORK \
             --subnet=SUBNET \
             --subnet-region=INSTANCE_LOCATION
         

Where `HTTP_PROXY_FORWARD` is the name of the forwarding rule you are creating.

  2. To create a forwarding rule for routing traffic to the SSH ILB, run the following command.
         
         gcloud compute forwarding-rules create SSH_PROXY_FORWARD \
             --project=INSTANCE_PROJECT_ID \
             --ports 22 \
             --target-tcp-proxy=ILB_SSH_TCP_TARGET_PROXY \
             --target-tcp-proxy-region=INSTANCE_LOCATION \
             --network-tier PREMIUM \
             --load-balancing-scheme=INTERNAL_MANAGED \
             --network=NETWORK \
             --subnet=SUBNET \
             --subnet-region=INSTANCE_LOCATION
         

Where `SSH_PROXY_FORWARD` is the name of the forwarding rule you are creating.




## Create your private DNS records

Once the forwarding rules are set up, you need to register DNS records in your private Cloud DNS zone for each of the instance's hostnames.

  1. To get the IP address for your HTTP forwarding rule, run the following command.
         
         gcloud compute forwarding-rules describe HTTP_PROXY_FORWARD \
             --project=INSTANCE_PROJECT_ID \
             --region=INSTANCE_LOCATION
         

Where `HTTP_PROXY_FORWARD` is the name you gave the forwarding rule for HTTP.

  2. To register the API hostname, run the following command.
         
         gcloud dns record-sets create INSTANCE_ID-INSTANCE_PROJECT_NUMBER-api.INSTANCE_LOCATION.p.sourcemanager.dev. \
             --project=INSTANCE_PROJECT_ID \
             --zone=ZONE_NAME \
             --type=A \
             --ttl=300 \
             --rrdatas=HTTP_LB_IP
         

Replace the following:

     * `INSTANCE_ID`: with your instance ID.
     * `INSTANCE_PROJECT_NUMBER`: with you instance's Google Cloud project number.
     * `INSTANCE_LOCATION`: with the region of your instance.
     * `INSTANCE_PROJECT_ID`: with your instance's Google Cloud project ID.
     * `ZONE_NAME`: with the name you gave the managed-zone.
     * `HTTP_LB_IP`: is the output of `gcloud compute forwarding-rules describe HTTP_PROXY_FORWARD`.
  3. To register the Git HTTP hostname, run the following command.
         
         gcloud dns record-sets create INSTANCE_ID-INSTANCE_PROJECT_NUMBER-git.INSTANCE_LOCATION.p.sourcemanager.dev. \
             --project=INSTANCE_PROJECT_ID \
             --zone=ZONE_NAME \
             --type=A \
             --ttl=300 \
             --rrdatas=HTTP_LB_IP
         

  4. To register the HTML hostname for the web interface, run the following command.
         
         gcloud dns record-sets create INSTANCE_ID-INSTANCE_PROJECT_NUMBER.INSTANCE_LOCATION.p.sourcemanager.dev.\
             --project=INSTANCE_PROJECT_ID \
             --zone=ZONE_NAME \
             --type=A \
             --ttl=300 \
           --rrdatas=HTTP_LB_IP
         

  5. To get the IP address for your SSH forwarding rule, run the following command.
         
         gcloud compute forwarding-rules describe SSH_PROXY_FORWARD \
             --project=INSTANCE_PROJECT_ID \
             --region=INSTANCE_LOCATION
         

Where `SSH_PROXY_FORWARD` is the name you gave the forwarding rule for SSH.

  6. To register the Git SSH hostname, run the following command.
         
         gcloud dns record-sets create INSTANCE_ID-INSTANCE_PROJECT_NUMBER-ssh.INSTANCE_LOCATION.p.sourcemanager.dev. \
             --project=INSTANCE_PROJECT_ID \
             --zone=ZONE_NAME \
             --type=A \
             --ttl=300 \
             --rrdatas=SSH_LB_IP
         

Where `SSH_LB_IP` is the output of `gcloud compute forwarding-rules describe SSH_PROXY_FORWARD`.




## Create a repository in your instance

You can use a bastion host to access and create a repository in your Private Service Connect instance.

  1. Create a bastion host VM with the `cloud-platform` [scope](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create#--scopes) by following the instructions in [Create a bastion host VM](https://docs.cloud.google.com/compute/docs/connect/ssh-using-bastion-host#create-bastion).

  2. Create a repository by running the following command.
         
         curl \
         -H "Content-Type: application/json" \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         https://INSTANCE_ID-PROJECT_NUMBER-api.INSTANCE_LOCATION.p.sourcemanager.dev/v1/projects/PROJECT_NUMBER/locations/INSTANCE_LOCATION/repositories?repository_id=REPOSITORY_ID \
         -d '{}'
         

Replace the following:

     * `INSTANCE_ID`: with the name of your Secure Source Manager instance.
     * `PROJECT_NUMBER`: with your instance's Google Cloud project number.
     * `INSTANCE_LOCATION`: with the location of your instance.
     * `REPOSITORY_ID`: with the name you want to give your repository.

A repository is created in your Private Service Connect instance.




## Test access to Secure Source Manager from Cloud Build

To confirm everything is working correctly, you can use the following build config file to test connectivity and pull source code from Secure Source Manager. The build config file assumes you are using Cloud Logging to store your build logs. If you are using a user-created Cloud Storage bucket, see [Execute a build using a config file](https://docs.cloud.google.com/build/docs/securing-builds/configure-user-specified-service-accounts#execute_a_build_using_a_config_file) for instructions on how to edit the build config file.

Before you use the following YAML file, replace the following:

  * `CA_POOL_NAME`: with the CA pool name you used when you created your Private Service Connect instance.
  * `CA_PROJECT_ID`: with the Google Cloud project you used to create the CA pool.
  * `INSTANCE_LOCATION`: with the location of your instance.
  * `INSTANCE_ID`: with the name of your instance.
  * `INSTANCE_PROJECT_NUMBER`: with your instance's Google Cloud project number.
  * `REPOSITORY_ID`: with the name you gave your repository.
  * `SA_PROJECT_ID`: with the project ID of the service account you are using with Cloud Build.
  * `SERVICE_ACCOUNT`: with the email address of the service account you are using with Cloud Build.


    
    
    steps:
      - name: gcr.io/cloud-builders/gcloud
        args:
          - privateca
          - pools
          - get-ca-certs
          - CA_POOL_NAME
          - '--project'
          - CA_PROJECT_ID
          - '--location'
          - INSTANCE_LOCATION
          - '--output-file=cacert.pem'
      - name: gcr.io/cloud-builders/git
        args:
          - config
          - '--global'
          - 'credential.https://INSTANCE_ID-INSTANCE_PROJECT_NUMBER-git.INSTANCE_LOCATION.p.sourcemanager.dev.helper'
          - gcloud.sh
      - name: gcr.io/cloud-builders/git
        args:
          - config
          - '--global'
          - http.sslCAInfo
          - cacert.pem
      - name: gcr.io/cloud-builders/git
        env:
          - GIT_TRACE=1
          - GIT_CURL_VERBOSE=1
        args:
          - clone
          - >-
            https://INSTANCE_ID-INSTANCE_PROJECT_NUMBER-git.INSTANCE_LOCATION.p.sourcemanager.dev/INSTANCE_PROJECT_ID/REPOSITORY_ID
          - https-clone
    serviceAccount: 'projects/SA_PROJECT_ID/serviceAccounts/SERVICE_ACCOUNT'
    options:
      logging: CLOUD_LOGGING_ONLY
    

## What's next

  * To automate builds from Secure Source Manager, follow the instructions in [Create a triggers file](https://docs.cloud.google.com/secure-source-manager/docs/create-triggers-file).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
