---
url: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/accessing-internal-proxies/
title: Calling an API proxy with internal-only access \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:15:19.429133+00:00
---

# Calling an API proxy with internal-only access  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/accessing-internal-proxies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Calling an API proxy with internal-only access Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** , but not to **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

![](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/ng-saas/chevrons-1-setup.png)

This document explains how to call API proxies from clients running on your internal network. These steps are useful for testing your setup if Apigee is provisioned to use internal network routing. You can follow the steps in this document if Apigee was provisioned with any of these network routing configurations:

Provisioning option | Networking option | Provisioning steps  
---|---|---  
Paid subscription | With VPC peering | [Internal routing (VPC)](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli#internal-routing-vpc)  
[Internal routing (Private Service Connect)](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli#internal-routing-psc)  
Pay-as-you-go | With VPC peering | [Internal routing (VPC)](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli-paygo#internal-routing-vpc)  
[Internal routing (Private Service Connect)](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli-paygo#internal-routing-psc)  
Evaluation | With VPC peering | [Configure routing (internal)](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli-eval#configure-routing)  
Evaluation | Without VPC peering | [Internal routing (Private Service Connect)](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli-non-peered-eval#internalpsc)  
  
See also [Networking options](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/networking-options).

##  Before you begin 

Do the following preliminary setup steps:

  1. If you haven't already, initialize the Cloud SDK, as described in [Initialize the gcloud CLI](https://docs.cloud.google.com/sdk/docs/initialize), or otherwise ensure that the Google Cloud project you created in [Prerequisites](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/prerequisites) is the default project for `gcloud`. 
  2. Define the following local environment variables:
         
         export PROJECT_ID=YOUR_PROJECT_ID
         export AUTH="Authorization: Bearer $(gcloud auth print-access-token)"
         export SUBNET=NETWORK_NAME
         export INSTANCE_NAME=INSTANCE_NAME
         export PROJECT_NUMBER=$(gcloud projects describe $PROJECT_ID --format="value(projectNumber)")

Where:

     * **`PROJECT_ID`** is the Cloud project ID that you created as part of the [Prerequisites](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/prerequisites).
     * **`AUTH`** defines the `Authentication` header with a bearer token. You will use this header when calling Apigee APIs. Note that the token expires after a period of time and when it does, you can simply regenerate it using the same command. For more information, see the reference page for the [print-access-token command](https://cloud.google.com/sdk/gcloud/reference/auth/application-default/print-access-token).
     * **`SUBNET`** is the subnet specified during provisioning. For example: `default`.
     * `**INSTANCE_NAME**`: Your new instance's name. For example, `my-runtime-instance`. The name must start with a lowercase letter, can be up to 32 characters long, and can include only lowercase letters, numbers and hyphens. It cannot start or end with a hyphen and must be at least two characters long. **Tip:** Your instance name must match the following regular expression: 
           
           ^[a-z][a-z\-\d]{0,30}[a-z\d]$

     * **`PROJECT_NUMBER`** is the Cloud project number that you created as part of the [Prerequisites](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/prerequisites). This example issues a `gcloud` command to get the project number for you.
  3. Get the value of the `location` property from your Apigee instance. This value is the region where the instance is located, such as `us-west1`: 
         
         curl -H "**$AUTH** " https://apigee.googleapis.com/v1/organizations/**$PROJECT_ID** /instances

  4. Pick [a zone](https://cloud.google.com/sdk/gcloud/reference/beta/compute/instances/create#--zone) within the instance region, and put the zone name in a variable. The zone must be within the instance. For example: 
         
         export **VM_ZONE** ="us-west1-b"

If you need help identifying a zone within the instance region, you can use this `gcloud` command to return a zone name for the configured runtime region. For example: 
         
         VM_ZONE=$(gcloud compute zones list | grep "us-west1" | head -n 1 | awk '{print $1}')




##  Create a VM and call the API proxy 

Next, create a new VM inside your VPC network using the [gcloud beta compute](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instances/create) command. The VM acts as a bridge that allows you to send requests to the internal load balancer IP. After the VM is set up, you can call a deployed API proxy: 

  1. The following example creates a new VM with some common options and uses environment variables that you defined previously as inputs. 
         
         gcloud beta compute --project=**$PROJECT_ID** \
           instances create **$INSTANCE_NAME** \
           --zone=**$VM_ZONE** \
           --machine-type=e2-micro \
           --subnet=**$SUBNET** \
           --network-tier=PREMIUM \
           --no-restart-on-failure \
           --maintenance-policy=TERMINATE \
           --preemptible \
           --service-account=**$PROJECT_NUMBER** -compute@developer.gserviceaccount.com \
           --scopes=https://www.googleapis.com/auth/cloud-platform \
           --tags=http-server,https-server \
           --image=debian-12-bookworm-v20240701 \
           --image-project=debian-cloud \
           --boot-disk-size=10GB \
           --boot-disk-type=pd-standard \
           --boot-disk-device-name=**$INSTANCE_NAME** \
           --no-shielded-secure-boot \
           --shielded-vtpm \
           --shielded-integrity-monitoring \
           --reservation-affinity=any

  2. Open a secure connection to the new VM that you just created.
         
         gcloud compute ssh **$INSTANCE_NAME** --zone=**$VM_ZONE** --project=**$PROJECT_ID**

**Note:** If the `ssh` fails or hangs, try the following command to create a firewall rule to allow access, then repeat the `gcloud compute ssh` command: 
         
         gcloud compute --project=**$PROJECT_ID** firewall-rules create allow-ssh \
                 --direction=INGRESS --priority=1000 --network=default --action=ALLOW --rules=tcp:22 \
                 --source-ranges=0.0.0.0/0

  3. In the VM shell, install the `jq` utility. It is used in subsequent steps: 
         
         sudo apt-get update -y
         sudo apt-get install -y jq
         

  4. In the VM shell, create the following environment variables to make it easy to copy/paste the API proxy request: 
         
         export **AUTH** ="Authorization: Bearer $(gcloud auth print-access-token)"
         export **PROJECT_ID** =YOUR_PROJECT_ID
         export **ENV_GROUP_HOSTNAME** =$(curl -H "**$AUTH** " https://apigee.googleapis.com/v1/organizations/**$PROJECT_ID** /envgroups -s | jq -r '.environmentGroups[0].hostnames[0]')
         

  5. Make sure the variables are set correctly: 
         
         echo $AUTH
         echo $PROJECT_ID
         echo $ENV_GROUP_HOSTNAME

  6. Call an API proxy. Select an option below that corresponds to how you configured routing during Apigee provisioning. 

#### Options for installations that use VPC peering

     * (TLS option #1) If you configured an internal load balancer (ILB) in your project, as explained in [Internal routing (VPC)](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli#internalvpc), call the proxy using the IP of that ILB. This option uses CA certs that are under your control and that were created when the internal load balancer was created: **Caution:** Because of a [limitation](https://docs.cloud.google.com/load-balancing/docs/l7-internal#limitations) on Google Cloud internal Application Load Balancer, the Apigee internal routing option does not support HTTP 1.0 requests. Incoming client requests that specify the HTTP 1.0 protocol will fail. Later HTTP versions are supported.
       1. Get the IP of the ILB in your project, as explained in [ Set up Internal HTTP(S) Load Balancing with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal#configure-internal-https-load-balancing-with-vm-based-service). 
       2. Call an API proxy: 
              
              curl -H "Host: **$ENV_GROUP_HOSTNAME** " \
                https://INTERNAL_LOAD_BALANCER_IP/PROXY_BASEPATH

     * (TLS option #2) Use the default, fully qualified domain name that resolves to the internal load balancer in the Apigee project. With this option, TLS is employed using internally created Apigee self-signed certs. You do not have control over these certificates. **Caution:** Because of a [limitation](https://docs.cloud.google.com/load-balancing/docs/l7-internal#limitations) on Google Cloud internal Application Load Balancer, the Apigee internal routing option does not support HTTP 1.0 requests. Incoming client requests that specify the HTTP 1.0 protocol will fail. Later HTTP versions are supported.
       1. Get the IP of the internal load balancer in the Apigee project: 
              
              export **INTERNAL_LOAD_BALANCER_IP** =$(curl -H "**$AUTH** " https://apigee.googleapis.com/v1/organizations/**$PROJECT_ID** /instances -s | jq -r '.instances[0].host')

       2. Pull the CA Certificate that was created during org creation with the following command: 
              
              curl -H "**$AUTH** " https://apigee.googleapis.com/v1/organizations/**$PROJECT_ID** | jq -r .caCertificate | base64 -d > cacert.crt

       3. Send the request to a deployed API proxy, where `example.$PROJECT_ID.apigee.internal` is the internal, default, fully qualified domain name that resolves to the internal load balancer. 
              
              curl -is -H "Host: **$ENV_GROUP_HOSTNAME** " \
                https://example.**$PROJECT_ID**.apigee.internal/PROXY_BASEPATH \
                --cacert cacert.crt \
                --resolve example.**$PROJECT_ID**.apigee.internal:443:$INTERNAL_LOAD_BALANCER_IP

     * (Non-TLS option) If you experience SSL/TLS certificate validation issues, you can use the `-k` (or `--insecure`) flag with the `curl` command. This bypasses certificate validation, allowing the connection to proceed. Note that while the communication remains encrypted, this option carries security implications as server authenticity isn't verified. 
       1. Get the IP of the internal load balancer in the Apigee project: 
              
              export **INTERNAL_LOAD_BALANCER_IP** =$(curl -H "**$AUTH** " https://apigee.googleapis.com/v1/organizations/**$PROJECT_ID** /instances -s | jq -r '.instances[0].host')

       2. Call an API proxy: 
              
              curl -i -k \
                -H "Host: **$ENV_GROUP_HOSTNAME** " \
                https://**$INTERNAL_LOAD_BALANCER_IP** /PROXY_BASEPATH

     * (Service endpoint option) If you provisioned a paid or evaluation organization with Private Service Connect and chose the service endpoint routing option:
       1. Get the IP of the service endpoint. If you need to look up the endpoint IP, see [List endpoints](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#list-endpoints). 
       2. Call an API proxy: 
              
              curl -i -k \
                 -H "Host: **$ENV_GROUP_HOSTNAME** " \
                 https://SERVICE_ENDPOINT_IP/PROXY_BASEPATH

For example:
              
              curl -H "Host: $ENV_GROUP_HOSTNAME" https://10.138.0.2/helloworld -k

#### Options for installations that do not use non-VPC peering

     * (Service endpoint option) If you provisioned a paid or evaluation organization with Private Service Connect and chose the service endpoint routing option:
       1. Get the IP of the service endpoint. If you need to look up the endpoint IP, see [List endpoints](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#list-endpoints). 
       2. Call an API proxy: 
              
              curl -i -k \
                  -H "Host: **$ENV_GROUP_HOSTNAME** " \
                  https://SERVICE_ENDPOINT_IP/PROXY_BASEPATH

For example:
              
              curl -H "Host: $ENV_GROUP_HOSTNAME" https://10.138.0.2/helloworld -k

If you encounter errors during this part of the process, be sure that all of the environment variables you created and used in commands have valid values. See also [Troubleshooting](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/troubleshooting-install).

##  Next step 

Try [creating a proxy](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/get-started) which you can then deploy, or [take a tour](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/tutorials) of the Apigee tutorials that will introduce you to the features of Apigee, such as [guarding against sudden traffic spikes](https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/add-spike-arrest) or [getting a detailed view of the request/response flow](https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/view-with-trace).

**(Advanced)** If you plan on turning this into a production setup, you can configure a security perimeter around your new cluster and related Cloud services. This is possible with [VPC Service Controls](https://docs.cloud.google.com/apigee/docs/api-platform/security/vpc-sc).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
  *[VPC]: Virtual Private Cloud
