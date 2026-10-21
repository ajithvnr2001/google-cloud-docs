---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/lets-encrypt/
title: Obtain TLS certificates: An example \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:27:18.003936+00:00
---

# Obtain TLS certificates: An example  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/lets-encrypt/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Obtain TLS certificates: An example Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.13 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.13 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/lets-encrypt.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/lets-encrypt.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/lets-encrypt.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/lets-encrypt.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/lets-encrypt.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/lets-encrypt.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/lets-encrypt.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/lets-encrypt.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/lets-encrypt.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/lets-encrypt.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/lets-encrypt.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/lets-encrypt.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/lets-encrypt.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/lets-encrypt.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/lets-encrypt.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/lets-encrypt.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/lets-encrypt.html)



This topic is intended as an example only. It explains how to obtain a TLS certificate from the certificate authority (CA) [Let's Encrypt](https://letsencrypt.org). These steps are provided primarily as an example to follow if you do not have another ready way to obtain a certificate/key pair that is authorized by a CA. The example shows how to generate certificates using the [Let's Encrypt](https://letsencrypt.org) CA, the [Certbot client](https://certbot.eff.org/pages/about), and Google Cloud Platform [Cloud DNS](https://cloud.google.com/dns/docs/). 

**Note:** See also this [ Apigee Community article](https://discuss.google.dev/t/free-trusted-ssl-certificates-for-apigee-hybrid-ingress-on-gke/18240) on using Let's Encrypt with Apigee hybrid.

##  Where you can use these certificates 

You must provide TLS certificates for Runtime ingress gateways exposed outside the cluster. 

**Note:** In a test or eval environment, you can use a self-signed certificate/key pair or authorized TLS certificates. However, in a production environment, you will need to use signed certificates. You can use either a certificate/key pair or a Kubernetes secret. See also [External connections](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/ports#external). 

##  Requirements 

You will need a domain name obtained through a domain name registrar. You can register a domain name through Google Domains or another domain registrar of your choice.

##  Configure Cloud DNS 

To obtain authorized TLS certificates, you must have a qualified domain name. The following steps explain how to use [Google Cloud DNS](https://cloud.google.com/dns/) to obtain a domain name and manage your domain servers. 

  1. Open the [Google Cloud console](https://console.cloud.google.com) and log into your account.
  2. Select the project where Apigee hybrid is installed.
  3. If you have not already done so, enable the **Cloud DNS API**. See [Enabling APIs](https://cloud.google.com/apis/docs/getting-started#enabling_apis).
  4. Create a static IP address: 
     * If you are on GKE, follow the instructions in [ Configure static external IP addresses](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address) to create a static IP addresses that external processes can use to communicate with the hybrid runtime ingress. You can give the address any name you wish, for example: `apigee-hybrid-runtime`. When you finish, you will use the IP number in the cluster configuration in the next step. For example: `34.66.75.196`
     * If you are on Google Distributed Cloud, follow instructions in the [ Plan IP addresses](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/plan-ip-addresses) and [Create a user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster) to create a static IP address.
  5. Get the External IP you just reserved. 
  6. Create a record set for the runtime Istio ingress endpoint. This is the address for making API calls to the hybrid gateway. Enter the External IP you obtained in the previous step and add a prefix to the domain name, such as `example-endpoint`. For instructions, see [Create a new record](https://cloud.google.com/dns/docs/set-up-dns-records-domain-name#create_a_new_record). 
     1. Create a managed public zone. For instructions, see [ Create a managed public zone](https://cloud.google.com/dns/docs/set-up-dns-records-domain-name#create_a_managed_public_zone).
     2. Create a new record set with: 
        * **DNS Name** : The name of the endpoint external API calls will communicate with, like ` api-services` or `example-endpoint`
        * **Resource Record Type** : **A**
        * **TTL** and **TTL Unit** : Accept defaults
        * **IP Address** : The static IP you created.
  7. The **Zone details** view will list four DNS servers as the NS data for your new zone. Copy the DNS record data, as shown in the following example: 

![](https://docs.cloud.google.com/static/apigee/docs/hybrid/v1.13/images/copy-dns-records.png)

  8. Return to your domain page at your registrar (for example, [Google Domains](https://domains.google.com)).
  9. Select your domain.
  10. Select **DNS**.
  11. In the Name Servers section, click **Edit**. 
  12. Enter the domain name servers that you copied from the Network Services Cloud DNS page. For example:

![](https://docs.cloud.google.com/static/apigee/docs/hybrid/v1.13/images/hybrid-dns-fields.png)




Now, your Google Cloud DNS will manage the DNS records for your domain. 

##  Install Certbot on a VM 

Now that you have Cloud DNS set up to manage your domain servers, you will install the Certbot client with the [dns_google](https://certbot-dns-google.readthedocs.io/en/stable/) plugin on a Cloud VM. The client enables you to get authorized certificates for your domain from a Let's Encrypt endpoint. 

  1. Open the [Google Cloud console](https://console.cloud.google.com) and log in with the account you created in [Step 1: Create a Google Cloud account](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/precog-gcpaccount).
  2. Select the project that you created in [Step 2: Create a Google Cloud project](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/precog-gcpproject).
  3. Select **IAM & admin > Service accounts**. 

The **Service accounts view** displays a list of the project's service accounts. 

  4. To create a new service account, click **+Create Service Account** at the top of the view. 

The **Service account details** view displays.

  5. In the **Service account name** field, enter the name of the service account. 

![](https://docs.cloud.google.com/static/apigee/docs/hybrid/v1.13/images/my-certmanager-name.png)

You can optionally add a description in the **Service account description** field. Descriptions are helpful at reminding you what a particular service account is used for.

  6. Click **Create**. 

Google Cloud creates a new service account and displays the **Service account permissions** view. Use this view to assign a role to your new service account.

  7. Click the **Select a role** drop-down list.
  8. Select the **Project Owner** role. 
  9. Click **Continue**. 
  10. Click **Done**.
  11. In the Google Cloud console, select **Compute Engine > VM Instances**.
  12. Create a VM instance named **certmanager**.
  13. Under the Boot Disk section, choose CentOS7 and 20 GB for the SSD persistent drive.
  14. Set the Service Account to the one you created above.
  15. Install Certbot and the [dns_google](https://certbot-dns-google.readthedocs.io/en/stable/) plugin on the machine and run the Certbot client: 
         
         sudo su -
           yum -y install yum-utils
           yum install certbot -y
           yum install certbot-dns-google -y
           certbot certonly --dns-google -d *.your_domain_name,*.your_domain_name --server https://acme-v02.api.letsencrypt.org/directory
           

For example: 
         
         sudo su -
         yum -y install yum-utils
         yum install certbot -y
         yum install certbot-dns-google -y
         certbot certonly --dns-google -d *.apigee-hybrid-docs.net,*.apigee-hybrid-docs.net --server https://acme-v02.api.letsencrypt.org/directory

  16. You can now find your authorized certificate and private key files in this directory: `cd /etc/letsencrypt/live/your_domain_name/`

For example: 
         
         cd /etc/letsencrypt/live/apigee-hybrid-docs.net
         ls
           cert.pem  chain.pem  fullchain.pem  privkey.key  README

  17. Copy the files `fullchain.pem` and `privkey.key` to your local machine.
  18. _Optional_ : Create a Kubernetes secret with the certificate/key pair. See the instructions in [Option 2: Kubernetes Secret](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/ingress-tls#option-2:-kubernetes-secret) in [Configuring TLS and mTLS on the Istio ingress](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/ingress-tls).
  19. Update your overrides file to point to the certificate and private key. 

For example:
         
         ...
         envs:
           - name: test
             serviceAccountPaths:
               synchronizer: "your_keypath/synchronizer-manager-service-account.json
               udca: "your_keypath/analytic-agent-service-account.json
         
         virtualhosts:
           - name: my-env-group
             sslCertPath: "$HOME/hybrid/apigee-hybrid-setup/tls/fullchain.pem"
             sslKeyPath: "$HOME/hybrid/apigee-hybrid-setup/tls/privkey.key"

Or if using Kubernetes secrets:
         
         ...
         envs:
           - name: test
             serviceAccountPaths:
               synchronizer: "your_keypath/synchronizer-manager-service-account.json
               udca: "your_keypath/analytic-agent-service-account.json
         
         virtualhosts:
           - name: my-env-group
             tlsMode: SIMPLE  # Note: SIMPLE is the default, MUTUAL is also an available value.
             sslSecret: myorg-test-policy-secret"
         
         ...  

  20. Apply changes to the `envs` configuration: 

Run helm upgrade for each environment you want to update.
         
         helm upgrade ENV_NAME apigee-env/ \
           --namespace apigee \
           --set env=ENV_NAME \
           --atomic \
         -f OVERRIDES_FILE.yaml
         

**Note:** If you see an error saying `Error: UPGRADE FAILED: "_ENV_NAME_ " has no deployed releases`, replace `upgrade` with `install` and try the command again.

##  Test the configuration 

Deploy and test a proxy. See [Build your first API proxy overview](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/get-started). 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
