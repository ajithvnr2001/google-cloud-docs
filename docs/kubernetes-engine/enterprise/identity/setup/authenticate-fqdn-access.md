---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/authenticate-fqdn-access/
title: Log in using a fully qualified domain name (FQDN) \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:25:01.591447+00:00
---

# Log in using a fully qualified domain name (FQDN)  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/authenticate-fqdn-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)



Send feedback 

#  Log in using a fully qualified domain name (FQDN) Stay organized with collections  Save and categorize content based on your preferences. 

After you configure authentication for fleet member clusters, you can log in to configured clusters from the command line using a username and password from a third party identity provider. Follow the instructions in this page if your cluster administrator has chosen to let you authenticate directly to the cluster with a fully qualified domain name (FQDN). For SAML providers, login access is supported only through this authentication approach.

This authentication approach is supported only for on-prem clusters (Google Distributed Cloud) on VMware and bare metal, from version 1.29. Other cluster types are not supported.

The `gcloud` CLI version required to log in with your provided FQDN is atleast version 477.0.0.

## Login workflow

Here are the workflow steps when a user logs in using the FQDN access approach:

  1. **Initiate login** : The user runs the command `gcloud anthos auth login --server APISERVER-URL` to initiate the login process.
  2. **Identity provider selection** : The user is given a list of configured identity providers. The user selects the provider where their credentials are stored.
  3. **Authentication with identity provider:** The authentication process differs based on the identity provider protocol you choose:

     * **OIDC** : The user is redirected to the OIDC-provider login page. After a successful login, the provider sends a code back to the cluster, which exchanges it for an access token through a back-channel communication.
     * **SAML** : The user is redirected to the SAML-provider login page. After a successful login, the provider directly sends a token (assertion) back to the cluster thereby avoiding an additional callback.
     * **LDAP** : Instead of redirecting to an external provider, a login page appears where the user enters their LDAP credentials, which is verified directly with the LDAP server.
  4. **Token verification and kubeconfig file generation** : The cluster verifies the token received (or assertion), creates a new token for the user, and sends back a kubeconfig file containing this token.

  5. **Cluster access** : The user can access the cluster using `kubectl` commands. The `kubectl` client automatically sends the token from the kubeconfig file with each request.

  6. **Token validation and RBAC authorization** : The Kubernetes API server receives the token, the authentication service verifies this token, and retrieves the user's claims (username and groups). After successful validation, the API server runs Role-Based Access Control (RBAC) checks to determine the resources that the user is authorized to access.




## Log in using trusted SNI certificates

SNI certificates simplify cluster access by leveraging trusted certificates already present on corporate devices. Administrators can specify this certificate at the time of cluster creation. If your cluster uses a trusted SNI certificate at the cluster level, use the command in this section with the FQDN provided by your administrator to log in to the cluster and receive an access token. You can also use a secure `kubeconfig` file where the token is stored after successful authentication.

Run the following command to authenticate to the server:

`gcloud anthos auth login --server APISERVER-URL --kubeconfig OUTPUT_FILE`

Replace the following:

  * APISERVER-URL: FQDN of the cluster's Kubernetes API server.
  * OUTPUT_FILE: Use this flag if your `kubeconfig` file resides in a location other than the default. If this flag is omitted, authentication tokens are added to the `kubeconfig` file in the default location. For example: `--kubeconfig /path/to/custom.kubeconfig`.



## Log in using cluster CA-issued certificates

If you don't use a trusted SNI certificate at the cluster level, then the certificate used by the identity service is issued by the cluster's certificate authority (CA). Administrators distribute this CA certificate to users. Run the following command using the cluster's CA certificate to log in to your cluster:

`gcloud anthos auth login --server APISERVER-URL --kubeconfig OUTPUT_FILE --login-config-cert CLUSTER_CA_CERTIFICATE`

**Note:** As a recommendation, users can trust the CA certificate on their devices and browsers by following the device-specific instructions. This is a one-time activity. Once the CA certificate is trusted, you can log in to the cluster without specifying the `--login-config-cert` argument in the command.

## Cross-device authentication

Cross-device authentication lets you sign in to Google Distributed Cloud (GDC) clusters from devices that don't have a browser installed. You can initiate the authentication process on your primary device (which doesn't have a browser installed) and complete it on a secondary device installed with a browser.

Use the following steps for a cross-device authentication setup.

  1. **Log in to your primary device**

Run the following command to authenticate to the server on your primary device. Specify the argument `--no-browser` to indicate that the device you need to access your cluster from does not have a browser installed.

`gcloud anthos auth login --server APISERVER-URL --kubeconfig OUTPUT_FILE --no-browser`

The output is a command that you need to use when you log in from the second device. Here's an example of what the command looks like:
         
         You are authorizing gcloud CLI without access to a web browser. Please run the following command on a machine with a web browser and copy its output back here.
         
         gcloud auth login --server APISERVER-URL --kubeconfig OUTPUT_FILE --remote-bootstrap="URL_TO_COPY_ON_THE_SECOND_DEVICE"
         
         Enter the output of the above command:
         

Copy the `gcloud` command.

  2. **Log in to clusters on the second device**

Before logging in from the second device, verify that you have the browser installed and have network connectivity to the Kubernetes API server. Run the command you copied from the previous step on the second device.
         
         gcloud auth login --server APISERVER-URL --kubeconfig OUTPUT_FILE --remote-bootstrap="URL_TO_COPY_ON_THE_SECOND_DEVICE"
         

When attempting to log in from this device, a warning message is displayed. Follow the standard authentication process as displayed on the browser. After a successful authentication, you will be provided with a one-time code. Copy this code.
         
         WARNING: The following line enables access to your Cluster resources. ONLY COPY IT TO A MACHINE YOU TRUST AND RUN 'gcloud auth login --server APISERVER-URL --kubeconfig OUTPUT_FILE --no-browser' EARLY ON.
         
         Or_mHYQFm90efgJdwhajx0KeC_WXkuvBPuWv_83nFX9J_Eawm3tQcBpxBBWszj6Ix8dAWCgc1QjJBrlt67bzIYIBTexU7dc_ggtkMTNkG7wCIGYZ75zfg9P1gBshP33STe0ks-AoVonzk01YekMbyNugeYSO18CBwFhaDDSMABq4PI-clgbaSh8CPqrvDKRLenbvfD9BSK6SW945I0bOgPURxNzUX4sICWcvFozhQdLYICuwRM0AgarNFwoeh-0wbJGyRqUjq2NJbaYdf-VCaByiZaGPR2B1QVGXO7deKGtUnk1_tTFOnB6sJQvT6UJ8Ge5nkR38rqBeeGkYdlVIBTXShENG80An1Ve524xZupSzCHNSVTJqYg
         

  3. **Complete log in on your primary device**

Paste the copied code from the previous step into the prompt of your primary device.
         
         Enter the code you received on the other device: Or_mHYQFm90efgJdwhajx0KeC_WXkuvBPuWv_83nFX9J_Eawm3tQcBpxBBWszj6Ix8dAWCgc1QjJBrlt67bzIYIBTexU7dc_ggtkMTNkG7wCIGYZ75zfg9P1gBshP33STe0ks-AoVonzk01YekMbyNugeYSO18CBwFhaDDSMABq4PI-clgbaSh8CPqrvDKRLenbvfD9BSK6SW945I0bOgPURxNzUX4sICWcvFozhQdLYICuwRM0AgarNFwoeh-0wbJGyRqUjq2NJbaYdf-VCaByiZaGPR2B1QVGXO7deKGtUnk1_tTFOnB6sJQvT6UJ8Ge5nkR38rqBeeGkYdlVIBTXShENG80An1Ve524xZupSzCHNSVTJqYg
         

Your device uses this code to generate a credential that is saved in a `kubeconfig` file. This file enables access to the cluster on your primary device. When you have logged in, the following message is displayed:
         
         You are logged in!
          Context is stored under the name '{cluster-name}'
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
