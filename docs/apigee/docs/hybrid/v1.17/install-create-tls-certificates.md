---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-create-tls-certificates/
title: Step 6: Create TLS certificates \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:54:30.312390+00:00
---

# Step 6: Create TLS certificates  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-create-tls-certificates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Step 6: Create TLS certificates Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.17 (latest)keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-create-tls-certificates)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-tls-certificates)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/install-create-tls-certificates)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/install-create-tls-certificates)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-create-tls-certificates)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/install-create-tls-certificates)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-create-tls-certificates)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-create-tls-certificates)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-create-tls-certificates)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/install-create-tls-certificates)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/install-create-tls-certificates)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/install-create-tls-certificates)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/install-create-tls-certificates)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/install-create-tls-certificates)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/install-create-tls-certificates)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/install-create-tls-certificates)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/install-create-tls-certificates)



This step explains how to create the TLS credentials that are required for Apigee hybrid to operate. 

##  Create TLS certificates 

You are required to provide TLS certificates for the runtime ingress gateway in your Apigee hybrid configuration. For the purpose of this quickstart (a non-production trial installation), the runtime gateway can accept self-signed credentials. In the following steps, [openssl](https://www.openssl.org/) is used to generate the self-signed credentials. 

**Note:** In a production environment, you will need to use signed certificates. You can use either a certificate and key pair or a Kubernetes secret. For an example on how to obtain a TLS certificate from the _Lets Encrypt_ certificate authority (CA), see [Obtain TLS credentials: An example](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/lets-encrypt). 

In this step, you will create the TLS credential files and add them to the `$APIGEE_HELM_CHARTS_HOME/certs` directory. In [ Step 7: Create the overrides](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-create-overrides), you will add the file paths to the cluster configuration file. 

  1. Create a directory for the credential files. Helm charts cannot read files outside the chart directory, and the TLS credentials are managed with the `apigee-virtualhost` chart. therefore create your directory for the credential files within the `$APIGEE_HELM_CHARTS_HOME/apigee-virtualhost/` directory. 

For example:
         
         mkdir $APIGEE_HELM_CHARTS_HOME/apigee-virtualhost/certs/

  2. Execute the following command to create the credential files and store them in your `$APIGEE_HELM_CHARTS_HOME/apigee-virtualhost/certs` directory: 
         
         openssl req  -nodes -new -x509 -keyout $APIGEE_HELM_CHARTS_HOME/apigee-virtualhost/certs/keystore_$ENV_GROUP.key -out \
             $APIGEE_HELM_CHARTS_HOME/apigee-virtualhost/certs/keystore_$ENV_GROUP.pem -subj '/CN=**' $DOMAIN'**' -days 3650

Where: 

     * DOMAIN is the domain you provided as the hostname for the environment group you created in [Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/precog-add-environment#create-an-environment-group).
     * ENV_GROUP is the name of the environment group where the domain is specified as a hostname. It's a good practice to include the environment group name in the key and keystore name to avoid accidentally reusing the same domain value if you create keys for multiple environment groups.

This command creates a self-signed certificate/key pair that you can use for the quickstart installation. 

If you have additional environment groups with unique domain names, repeat this step for each environment group. You will reference these groups and certificates in the cluster configuration step. 

  3. Check to make sure the files are in the `$APIGEE_HELM_CHARTS_HOME/apigee-virtualhost/certs` directory using the following command: 
         
         ls $APIGEE_HELM_CHARTS_HOME/apigee-virtualhost/certs

This you should see two files:

     * `keystore_ENV_GROUP.pem` or `keystore_ENV_GROUP.crt` is the self-signed TLS certificate file.
     * `keystore_ENV_GROUP.key` is the key file.



You now have the credentials needed to manage Apigee hybrid in your Kubernetes cluster. Next, you will create an overrides file that is used by Kubernetes to deploy the hybrid runtime components to the cluster. 

## Next step

[1](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-create-cluster) [2](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-download-charts) [3](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-create-namespace) [4](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-service-accounts) [5](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-sa-authentication) [6](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-create-tls-certificates) [(NEXT) Step 7: Create the overrides](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-create-overrides) [8](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-enable-control-plane-access) [9](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-cert-manager) [10](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-crds) [11](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-helm-charts)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
