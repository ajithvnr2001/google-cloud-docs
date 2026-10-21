---
url: https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v2.0.x/example-apigee/
title: Native Envoy example for Apigee and hybrid \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:03:43.850236+00:00
---

# Native Envoy example for Apigee and hybrid  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v2.0.x/example-apigee/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Native Envoy example for Apigee and hybrid Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This example demonstrates how to use Apigee Adapter for Envoy by installing and running Envoy locally, not inside a [Kubernetes cluster](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v2.0.x/example-hybrid). You can follow the example in this document for both Apigee and Apigee hybrid installations.

API proxy calls go through Envoy running as a native application. Apigee provides API management services, such as API product and developer app creation. Envoy communicates with the Apigee management plane through the adapter's remote service. The adapter also pushes analytics data to Apigee where you can see it in [Apigee Analytics](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-services-overview). 

## Prerequisites

Before you begin:  
---  
Download and install the Apigee Adapter for Envoy Remote Service and command-line interface (CLI) as explained in [Getting started](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v2.0.x/getting-started).  
Be sure you have the [Google Cloud SDK](https://cloud.google.com/sdk/install) installed. The SDK includes the `gcloud` command-line tool.  
Be sure you have [`kubectl`](https://kubernetes.io/docs/tasks/tools/install-kubectl/) installed.  
  
##  Check your gcloud configuration 

  1. Check that your `gcloud` configuration is set to the Google Cloud project associated with your Apigee organization. 

To list the current settings. See also [gcloud config](https://cloud.google.com/sdk/gcloud/reference/config). 
         
         gcloud config list

If necessary, set the correct Google Cloud project ID with this command: 
         
         gcloud config set project project-id

  2. You must be authenticated with Google Cloud SDK (gcloud) for your Google Cloud project. See also [gcloud auth login](https://cloud.google.com/sdk/gcloud/reference/auth/login). 
         
         gcloud auth login




##  Provision Apigee 

In this step, you will use the Remote Service CLI to provision Apigee Adapter for Envoy assets to Apigee. The provisioning command deploys API proxies used for Apigee adapter operations, sets up a certificate on Apigee, and generates credentials the remote service will use to securely connect from your system to Apigee. 

  1. Go to the `$CLI_HOME` directory: 
         
         cd $CLI_HOME

  2. (Optional) By default, the adapter looks for default service account credentials in your Google Cloud project for permission to send analytics data to Apigee. If you don't want to use the [default service account credentials](https://cloud.google.com/docs/authentication/production#automatically), you can create a service account and reference its key in the provisioning command. The service account must have the `apigee.analyticsAgent` role. For instructions, see [Creating and managing service accounts](https://cloud.google.com/iam/docs/creating-managing-service-accounts). 
  3. Create the following environment variables. These variables will be used as parameters to the provisioning script: 
         
         export ORG=organization_name
         export ENV=environment_name
         export RUNTIME=host_alias_url
         export NAMESPACE=hybrid_runtime_namespace  ## Apigee hybrid only
         export AX_SERVICE_ACCOUNT=analytics_service_account  ## Optional

Where: 

Variable | Description  
---|---  
organization_name | The name of your Apigee organization.  
environment_name | The name of an environment in your organization.  
host_alias_url | 
     * For Apigee hybrid, a URL that includes the `hostAlias` for a virtual host defined in your hybrid configuration.
     * For Apigee, a hostname from the environment group that includes the environment. You can find environment groups in the Apigee UI under **Admin > Environments > Groups**.
Note: The URL must start with `https://`. For example: `https://apitest.mydomain.net`  
hybrid_runtime_namepace | (Apigee hybrid only) The namespace in which the Hybrid runtime components are deployed. Note: The default namespace for a hybrid deployment is `apigee`.  
analytics_service_account | (Optional) The path to a Google Cloud service account key JSON file that has the `Apigee Analytics Agent` role. For a detailed description of this parameter, see [Provision command](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v2.0.x/reference#provision-command).  
  4. If you are not an owner of the Google Cloud project associated with the Apigee organization, be sure that your Google Cloud user account includes either the **Apigee Organization Admin** role, or both the **API Creator** and the **Deployer** roles. See [Granting, changing, and revoking access to resources](https://cloud.google.com/iam/docs/granting-changing-revoking-access).
  5. Get an access token: 
         
         TOKEN=$(gcloud auth print-access-token);echo $TOKEN

  6. Provision the remote service proxy to Apigee. The command output is redirected to a config file that you will use in a later step. **IF YOU ARE UPGRADING:** If you are upgrading an existing Apigee Adapter for Envoy, you must add the  
`--force-proxy-install` flag to the `provision` command. This flag forces the Apigee proxy to be replaced with the latest proxy.

If you are **not** upgrading, use this command to provision Apigee. If you are provisioning to Apigee hybrid, be sure to add the `--namespace $NAMESPACE` parameter: 
         
         ./apigee-remote-service-cli provision --organization $ORG --environment $ENV \
              --runtime $RUNTIME --analytics-sa $AX_SERVICE_ACCOUNT --token $TOKEN > config.yaml

If you are upgrading, use this command with the `--force-proxy-install` flag to provision Apigee. If you are provisioning to Apigee hybrid, be sure to add the `--namespace $NAMESPACE` parameter: 
         
         ./apigee-remote-service-cli provision --force-proxy-install --organization $ORG --environment $ENV \
              --runtime $RUNTIME --analytics-sa $AX_SERVICE_ACCOUNT --token $TOKEN > config.yaml

  7. Check the contents of the `config.yaml` file. It should look something like this: 
         
         # Configuration for apigee-remote-service-envoy (platform: Google Cloud)
         # generated by apigee-remote-service-cli provision on 2020-11-20 02:49:28
         apiVersion: v1
         kind: ConfigMap
         metadata:
           name: apigee-remote-service-envoy
           namespace: apigee
         data:
           config.yaml: |
             tenant:
               remote_service_api: https://apitest.mydomain.com/remote-service
               org_name: my-org
               env_name: test
             analytics:
               collection_interval: 10s
             auth:
               jwt_provider_key: https://apitest.mydomain.com/remote-service/token
         ---
         apiVersion: v1
         kind: Secret
         metadata:
           name: my-org-new-test-policy-secret
           namespace: apigee
         type: Opaque
         data:
           remote-service.crt: eyJrZXlzIjpbeyJrdHkiOiJSU0EiLCJhbGci...
           remote-service.key: LS0tLS1CRUdJTiBSU0EgUFJJVkFURS...
           remote-service.properties: a2lkPTIwMjAtMDctMDZ...
         ---
         apiVersion: v1
         kind: Secret
         metadata:
           name: my-org-new-test-analytics-secret
           namespace: apigee
         type: Opaque
         data:
           client_secret.json: ewogICJ0eXBlIjogInNlcnZ...
         ---
         apiVersion: v1
         kind: ServiceAccount
         metadata:
           name: apigee-remote-service-envoy
           namespace: apigee

  8. If you are using Apigee hybrid, apply the service configuration (the file output by the provisioning command) to the cluster where Apigee hybrid was installed in [Step 1: Create a cluster](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/install-create-cluster). 



##  Run `apigee-remote-service-envoy`

You can run the Remote Service either as a native binary or on Docker. 

###  Run the service natively 

Execute the service binary with the config file that was output by the provisioning command: 
    
    
    $REMOTE_SERVICE_HOME/apigee-remote-service-envoy -c config_file_path/config.yaml

###  Run the service on Docker 

Docker images are published with release tags. For this install, use the latest version. There are three image variations to choose from: 

Variation | Image  
---|---  
Google distroless | `google/apigee-envoy-adapter:v2.0.3`  
Ubuntu | `google/apigee-envoy-adapter:v2.0.3-ubuntu`  
Ubuntu with Boring Crypto | `google/apigee-envoy-adapter:v2.0.3-boring`  
  
For example, to run the scratch image with your local `config.yaml` available as `/config.yaml` via a volume mount, use this command:
    
    
    docker run -v ./config.yaml:/config.yaml google/apigee-envoy-adapter:v2.0.3
    

**Note:** The Docker image runs as a non-root user. Make sure it is granted read permission to the `config.yaml` file.

##  Create a sample Envoy configuration file 

Generate a sample Envoy configuration file using the CLI: 

  1. Make sure you are in the `$ENVOY_HOME` directory.
  2. List the available configuration templates: 
         
         $CLI_HOME/apigee-remote-service-cli samples templates

  3. Execute the samples command. For TEMPLATE, substitute one of the supported Envoy templates: 
         
         $CLI_HOME/apigee-remote-service-cli samples create --template TEMPLATE -c ./config.yaml

The command creates the file `./samples/envoy-config.yaml`. 




For more information, see [Samples command](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v2.0.x/reference#samples-command). 

##  Install and run the Envoy proxy 

Follow these steps to install and run the Envoy proxy: 

  1. Download an Envoy [binary](https://www.getenvoy.io/) or [build](https://www.envoyproxy.io/docs/envoy/latest/start/building) it.
  2. Run Envoy using a sample configuration file that you generated previously for the `httpbin.org` service: 
         
         envoy -c ./samples/envoy-config.yaml




##  Test the installation 

  1. Configure an API product and get an API key as explained in [How to obtain an API key](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v2.0.x/operation#how-to-obtain-an-api-key).
  2. Call the `httpbin` service without an API key: 
         
         curl -i http://localhost:8080/headers -H "HOST:httpbin.org"
         

**Note:** You must include the `HOST` header and set it to the remote service host that was set in the API product. 

The service is now being managed by Apigee, and because you did not supply an API key, the call returns the following error.
         
         curl -i http://localhost:8080/headers -H "HOST:httpbin.org"
         HTTP/1.1 403 Forbidden
         date: Tue, 12 May 2020 17:51:36 GMT
         server: envoy
         content-length: 0
         x-envoy-upstream-service-time: 11

  3. Make an API call using the key: 
         
         export APIKEY=YOUR_API_KEY
         curl -i http://localhost:8080/headers -H "HOST:httpbin.org" -H "x-api-key: $APIKEY"

The call should succeed with a 200 status and return a list of headers in the response. For example: 
         
         curl -i httpbin.default.svc.cluster.local/headers -H "x-api-key: kyOTalNNLMPfOSy6rnVeclmVSL6pA2zS"
         HTTP/1.1 200 OK
         server: envoy
         date: Tue, 12 May 2020 17:55:34 GMT
         content-type: application/json
         content-length: 828
         access-control-allow-origin: *
         access-control-allow-credentials: true
         x-envoy-upstream-service-time: 301
         
         {
           "headers": {
             "Accept": "*/*",
             "Content-Length": "0",
             "Host": "httpbin.default.svc.cluster.local",
             "User-Agent": "curl/7.70.0-DEV",
             "X-Api-Key": "kyOTalNNLMPfOSy6rneclmVSL6pA2zS",
             "X-Apigee-Accesstoken": "",
             "X-Apigee-Api": "httpbin.default.svc.cluster.local",
             "X-Apigee-Apiproducts": "httpbin",
             "X-Apigee-Application": "httpbin",
             "X-Apigee-Authorized": "true",
             "X-Apigee-Clientid": "kyOTalNNLMPfOSy6rVeclmVSL6pA2zS",
             "X-Apigee-Developeremail": "user@mydomain.com",
             "X-Apigee-Environment": "test",
             "X-Apigee-Organization": "my-org",
             "X-Apigee-Scope": "",
             "X-B3-Parentspanid": "1476f9a2329bbdfa",
             "X-B3-Sampled": "0",
             "X-B3-Spanid": "1ad5c19bfb4bc96f",
             "X-B3-Traceid": "6f329a34e8ca07811476f9a2329bbdfa"
           }
         }




##  Uninstall Apigee Envoy adapter 

To remove an Apigee Envoy adapter installation:

  1. Wherever you chose to have envoy adapter run (natively or on Docker), remove it.
  2. Delete the **remote-service** and **remote-token** proxies from your Apigee environment(s). See [Deleting an API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/develop/ui-delete-proxy).
  3. Remove any unused API products or [operations](https://docs.cloud.google.com/apigee/docs/api-platform/publish/create-api-products#operations) used by the Envoy adapter use cases. See [Deleting an API product](https://docs.cloud.google.com/apigee/docs/api-platform/publish/create-api-products#delete). 



##  Next steps 

API traffic to the `httpbin` service is now managed by Apigee. Here are some features you can explore and try: 

  * Access Apigee Analytics in the Edge UI. Go to **Analyze > API Metrics > API Proxy Performance**.
  * Explore the CLI options in the [Reference](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v2.0.x/reference).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
