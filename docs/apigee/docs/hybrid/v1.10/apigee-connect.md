---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/apigee-connect/
title: Apigee Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:43:56.837271+00:00
---

# Apigee Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/apigee-connect/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Apigee Connect Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.10 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.10 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/apigee-connect.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/apigee-connect.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/apigee-connect.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/apigee-connect.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/apigee-connect.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/apigee-connect.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/apigee-connect.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/apigee-connect.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/apigee-connect.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/apigee-connect.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/apigee-connect.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/apigee-connect.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/apigee-connect.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/apigee-connect.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/apigee-connect.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/apigee-connect.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/apigee-connect.html)



This section describes using Apigee Connect for communication between the hybrid management plane and the MART service in the runtime plane.

## Introduction

Apigee Connect allows the Apigee hybrid management plane to connect securely to the MART service in the runtime plane without requiring you to expose the MART endpoint on the internet. If you use Apigee Connect, you do not need to configure the MART ingress gateway with a host alias and an authorized DNS certificate.

![Primary services that execute on the hybrid runtime plane showing Apigee Connect](https://docs.cloud.google.com/static/apigee/docs/hybrid/v1.10/images/arch-runtime-apigee-connect.png)

## Prerequisites

Apigee hybrid 1.2.0. or newer.

## Add Apigee Connect to the hybrid runtime

Apigee Connect is enabled by default for new installations of Apigee hybrid version 1.3.0 and newer. Therefore, you are most likely to need these steps if you are upgrading from an older version. 

When Apigee Connect is configured and enabled, the MART ingress is ignored: the management plane only connects to MART using Apigee Connect. All MART traffic between the hybrid runtime plane passes through the secure Apigee Connect connection.

Follow these steps to enable and use Apigee Connect with Apigee hybrid:

  1. Enable the **Apigee Connect API** in the [ Google Cloud API Library](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/cloud.google.com/endpoints/docs/openapi/enable-api). You can enable the API in the [ Google Cloud console](https://pantheon.corp.google.com/home/dashboard) or with `gcloud`. For instructions on enabling APIs in the Google Cloud console, see [ Step 3: Enable APIs](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/precog-enableapi). To use `gcloud` to enable the API: 
     1. Set the current project in gcloud to the same Google Cloud project for which Apigee was enabled and your Apigee org was provisioned. 
            
            $ gcloud config set project YOUR_GCP_PROJECT_ID

Where **`_YOUR_GCP_PROJECT_ID_`** is the project ID. 

     2. Check to see if the Apigee Connect API is already enabled: 
            
            gcloud services list
            
            NAME                                 TITLE
            apigee.googleapis.com                Apigee API
            **apigeeconnect.googleapis.com         Apigee Connect API**
            bigquery.googleapis.com              BigQuery API
            
            ...

     3. If the results do not include `apigeeconnect.googleapis.com`, enable the API: 
            
            $ gcloud services enable apigeeconnect.googleapis.com

  2. Add the **Apigee Connect Agent** role to the MART service account that you created in the [ Create service accounts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-service-accounts) step in the Apigee hybrid installation instructions: 
     1. If you need, get the email address of your MART service account: 
            
            gcloud iam service-accounts list
            
            NAME                          EMAIL                                                 DISABLED
            apigee-mart                   apigee-mart@hybrid-example.iam.gserviceaccount.com       False
            
            ...

     2. Check to see if the MART service account already has the role assigned to it: 
            
            gcloud projects get-iam-policy YOUR_GCP_PROJECT_ID
            
            ...
            
            - members:
              - serviceAccount:apigee-mart@hybrid-example.iam.gserviceaccount.com
              role: roles/apigeeconnect.Agent
            
            ...

     3. If the results to not include `role: roles/apigeeconnect.Agent`, assign the role: 
            
            gcloud projects add-iam-policy-binding YOUR_GCP_PROJECT_ID \
            --member serviceAccount:YOUR_MART_SERVICE_ACCOUNT_EMAIL --role roles/apigeeconnect.Agent

Where **`_YOUR_GCP_PROJECT_ID_`** is the ID of your Google Cloud project, and **`_YOUR_MART_SERVICE_ACCOUNT_EMAIL_`** is the MART service account email address.

The **Apigee Connect Agent** role is predefined and has the following permission assigned to it: 

Permission | Description  
---|---  
`apigeeconnect.endpoints.connect` | This is the permission to set up the Apigee Connect Agent.  
  
For details on assigning granting access permissions through either the Google Cloud console or APIs, see:

     * [Granting, changing, and revoking access to resources](https://cloud.google.com/iam/docs/granting-changing-revoking-access)
     * [Method: roles.queryGrantableRoles](https://cloud.google.com/iam/reference/rest/v1/roles/queryGrantableRoles)
  3. Be sure the MART service account's key file is in the `hybrid_files/service_accounts` directory, as explained in [Create service accounts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-service-accounts).
  4. Open your overrides file. If the `connectAgent:enabled` property is not set to true, or is missing, add or update the following stanza. 

The Apigee Connect stanza must immediately follow under the **k8sCluster** stanza. 

The configuration requires you to provide the path to the downloaded service account key. The key must be for the service account with the **Apigee Connect Agent** role. 
         
         # Apigee Connect Agent
         connectAgent:
           enabled: true
           serviceAccountPath: ./service-accounts/MART_SA_KEYFILE.json

**Note:** By default, a `replicaCountMin` of 1 is used for the `connectAgent`. For other use cases, such as a production deployment, change the `replicaCountMin` to 3. For example:
         
         # Apigee Connect Agent
         connectAgent:
           enabled: true
           replicaCountMin: 3
           serviceAccountPath: ./service-accounts/connect_agent_sa_key.json

  5. Enable the Apigee Connect feature for your organization. The feature name is `features.mart.connect.enabled`. 
     1. Locate the service account key with the **Apigee Organization Admin** role that you used when you originally installed Apigee hybrid as described in the section [Enable synchronizer access](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-apply-hybrid#enable-synchronizer-access). This is the apigee-org-admin service account. You will need this key to generate a token needed to make an API call as explained below.
     2. Execute these two commands to get a token: 
            
            export GOOGLE_APPLICATION_CREDENTIALS=org-admin-service-account-file
            $ export TOKEN=$(gcloud auth application-default print-access-token)

Where **_org-admin-service-account-file_** is the path on your system to the service account key with the **Apigee Organization Admin** role. 

     3. Check to see if Apigee Connect is already enabled: 
            
            curl  https://apigee.googleapis.com/v1/organizations/your_org_name \
              -H "Authorization: Bearer $TOKEN"

Look in the results for: 
            
            "properties": {
                "property": [
                  {
                    **"name": "features.mart.connect.enabled",
                    "value": "true"**
                  },
                  {
                    "name": "features.hybrid.enabled",
                    "value": "true"
                  }
                ]
              },

     4. If the results do not include `features..mart.connect.enabled` set to `true`, call the following Apigee API to enable Apigee Connect for your organization: 
            
            curl -v -X PUT \
               https://apigee.googleapis.com/v1/organizations/your_org_name \
              -H "Content-Type: application/json" \
              -H "Authorization: Bearer $TOKEN" \
              -d '{
              "name" : "your_org_name",
              "properties" : {
                "property" : [ {
                  "name" : "features.hybrid.enabled",
                  "value" : "true"
                }, {
                  "name" : "features.mart.connect.enabled",
                  "value" : "true"
                } ]
              }
            }'

  
**Note:** The best practice is to leave your original MART endpoint property in the request body. Otherwise, your original MART configuration properties will be lost. Note that when Apigee Connect is enabled, the MART server endpoint configuration will be ignored: the management plane will connect with the MART server through Apigee Connect rather than the MART service endpoint. **Tip:** If you are upgrading an existing Apigee hybrid installation, you can preserve the ability to stop using Apigee Connect and revert to using the MART Istio Ingress endpoint directly. To do so, include a name value pair for the MART services endpoint as follows: 
            
            curl -v -X PUT \
               https://apigee.googleapis.com/v1/organizations/your_org_name \
              -H "Content-Type: application/json" \
              -H "Authorization: Bearer $TOKEN" \
              -d '{
              "name" : "your_org_name",
              "properties" : {
                "property" : [ {
                  "name" : "features.hybrid.enabled",
                  "value" : "true"
                }, **{
                  "name" : "features.mart.server.endpoint",
                  "value" : "https://HOST_ALIAS_DNS"
                },** {
                  "name" : "features.mart.connect.enabled",
                  "value" : "true"
                } ]
              }
            }'

  6. Start the Apigee Connect Agent in the cluster. 

If you have made changes in any of the steps above, use the following command to start the Apigee Connect Agent: 
         
         $APIGEECTL_HOME/apigeectl apply -f your_overrides_file.yaml --org

**NOTE:** With Apigee Connect enabled, the `mart` configuration stanza only needs to contain the value for `serviceAccountPath`. Other values will be ignored and can be omitted.   

    
    **mart:**
      hostAlias: "mart.apigee-hybrid-docs.net"  _# ignored when Apigee Connect is enabled._
      **serviceAccountPath: ./service-accounts/example-project-apigee-mart.json**
      sslCertPath: ./certs/fullchain.pem  _# ignored when Apigee Connect is enabled._
      sslKeyPath: ./certs/privkey.key  _# ignored when Apigee Connect is enabled._

  7. Check the Apigee Connect Agent log. If there are no errors reported, the upgrade succeeded:  

         
         kubectl logs -n namespace apigee-connect-agent-pod-name

  
The Apigee Connect Agent reports the following log categories:  
Audit logs category | Operations  
---|---  
DATA_READ | `ConnectionService.ListConnections`  
DATA_WRITE | `Tether.Egress`  
For help on viewing audit logs in Apigee hybrid see [ Audit logging information](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/audit-logging-info).

With this upgrade, the hybrid runtime plane communicates with the management plane through Apigee Connect.

  8. Test the installation.



See also: Removing Apigee Connect. 

## Test the installation

  1. Open the [Apigee hybrid UI](https://apigee.google.com/edge).
  2. Verify that any Developers and Developer apps that you previously created are present in the UI. Because these entities are queried from the MART server, they will be present only if the communication between the management and runtime planes is correctly configured.
  3. To be sure requests are going through Apigee Connect and not through the MART ingress, check the MART server's log. You should see entries for the Apigee Connect agent named `apigee-connect-agent-1.0`: 
         
         kubectl logs -n apigee apigee-mart-orgname-rc101-q72tl --org | grep connect

For example: 
         
         "2020-07-31 04:59:52,321 org: env: target: action: context-id: mode: pool-1-thread-1 INFO.
         gserviceaccount.com 1576040392317 /v1/organizations/apigee-connect-hybrid-prod/developers/
         count=100&expand=true&startKey=4ee9e8f7-12b2-4cde-bf10-32d991469876 200 GET apigee-connect
         -hybrid-prod 10.40.11.3 10.40.0.5 apigee-connect-agent-1.0 null"

  4. Refresh your authorization token: 
         
         export TOKEN=$(gcloud auth application-default print-access-token)

  5. Call the Apigee API to view the available streams connecting with the `apigee-mart` endpoint: 
         
         curl -s https://apigeeconnect.googleapis.com/v1/projects/YOUR_GCP_PROJECT_ID/endpoints/apigee_mart/connections \
           -H "Authorization: Bearer $TOKEN"
         
         {
           "connections": [
             {
               "endpoint": "projects/865098068308/endpoints/apigee_mart",
               "cluster": {
                 "name": "apigee-connect-test-cluster2",
                 "region": "australia-southeast1"
               },
               "streamCount": 4
             },
             {
               "endpoint": "projects/865098068308/endpoints/apigee_mart",
               "cluster": {
                 "name": "apigee-connect-test-cluster",
                 "region": "us-central1"
               },
               "streamCount": 2
             }
           ]
         }

  6. Check the Apigee Connect Agent logs: 
         
         kubectl logs -n namespace apigee-connect-agent-YOUR_GCP_PROJECT_ID-<....>

The following logs indicate the Apigee Connect Agent has started up and is communicating properly: 
         
         I0719 11.66:10.765526 2314949 main.go:47] Agent's flag values below
         I0719 11.66:10.765928 2314949 main.go:50] "alsologtostderr" : false
         I0719 11.66:10.765940 2314949 main.go:50] "cluster_name" : testABC
         I0719 11.66:10.765947 2314949 main.go:50] "cluster_region" : us-west2
         I0719 11.66:10.765953 2314949 main.go:50] "cpu_profile_enabled" : false
         I0719 11.66:10.765959 2314949 main.go:50] "http_client_timeout" : 2m0s
         I0719 11.66:10.765966 2314949 main.go:50] "http_port" : 7070
         I0719 11.66:10.765972 2314949 main.go:50] "http_server" : false
         I0719 11.66:10.765978 2314949 main.go:50] "insecure_ssl" : false
         I0719 11.66:10.765984 2314949 main.go:50] "local_cert" :
         I0719 11.66:10.765990 2314949 main.go:50] "log_backtrace_at" : :0
         I0719 11.66:10.766001 2314949 main.go:50] "log_dir" :
         I0719 11.66:10.766007 2314949 main.go:50] "logtostderr" : true
         I0719 11.66:10.766012 2314949 main.go:50] "mem_profile_enabled" : false
         I0719 11.66:10.766018 2314949 main.go:50] "project" : projects/apigee-connect-hybrid-prod
         I0719 11.66:10.766025 2314949 main.go:50] "resource_id" :
         I0719 11.66:10.766031 2314949 main.go:50] "server_addr" : apigeeconnect.googleapis.com:443
         I0719 11.66:10.766036 2314949 main.go:50] "server_cert" : ./server.crt
         I0719 11.66:10.766042 2314949 main.go:50] "server_key" : ./server.key
         I0719 11.66:10.766047 2314949 main.go:50] "stderrthreshold" : 2
         I0719 11.66:10.766054 2314949 main.go:50] "target_server" : http://127.0.0.1/
         I0719 11.66:10.766059 2314949 main.go:50] "tether_endpoint" : APIGEE_MART
         I0719 11.66:10.766065 2314949 main.go:50] "v" : 0
         I0719 11.66:10.766072 2314949 main.go:50] "vmodule" :
         I0719 11.66:10.845441 2314949 agent.go:400] successfully initiated http client
         I0719 11.66:10.845772 2314949 agent.go:728] starting metrics http server at ":7070"
         I0719 11.66:11.231.69 2314949 agent.go:245] listening on tether 6407043920806543360
         I0719 11.68:11.346544 2314949 agent.go:245] listening on tether 2101602677040349184
         I0719 12:00:11.461084 2314949 agent.go:245] listening on tether 9109203697228840960
         I0719 12:02:11.683743 2314949 agent.go:245] listening on tether 8978599308035096576
         I0719 12:02:40.325633 2314949 agent.go:255] tether id 6407043920806543360 is closed
         
         ...

  7. In the hybrid UI, create an API product, a developer, and a developer app. Then make several API calls to a proxy. 

The Connect Agent logs generated while processing requests will be helpful to see health or errors: 
         
         kubectl logs -n namespace apigee-connect-agent-YOUR_GCP_PROJECT_ID-<....>
         
         INFO: 2020/04/13 03:29:08 "961ff385-600a-427a-8864-ba066ff42330": received response from target
         "apigee-mart-apigee-connect-hybrid-prod.apigee.svc.cluster.local:8843", status code: 200
         INFO: 2020/04/13 03:29:08 Attempting to send response 961ff385-600a-427a-8864-ba066ff42330 on
         tether 16734438331890270208
         INFO: 2020/04/13 03:29:09 "e2fc0492-6e78-4c58-972b-7de8258b9e86": received response from target
         "apigee-mart-apigee-connect-hybrid-prod.apigee.svc.cluster.local:8843", status code: 200
         INFO: 2020/04/13 03:29:09 Attempting to send response e2fc0492-6e78-4c58-972b-7de8258b9e86 on
         tether 12483040283652521984
         INFO: 2020/04/13 03:29:10 "1ab3023b-b763-4b91-bf4f-ca8c02f62e50": received response from target
         "apigee-mart-apigee-connect-hybrid-prod.apigee.svc.cluster.local:8843", status code: 200
         INFO: 2020/04/13 03:29:10 Attempting to send response 1ab3023b-b763-4b91-bf4f-ca8c02f62e50 on
         tether 12483040283652521984
         INFO: 2020/04/13 03:29:12 "1fa3e3c3-a36e-4ff1-b2d3-5cf14f2f8fdd": received response from target
         "apigee-mart-apigee-connect-hybrid-prod.apigee.svc.cluster.local:8843", status code: 200
         INFO: 2020/04/13 03:29:12 Attempting to send response 1fa3e3c3-a36e-4ff1-b2d3-5cf14f2f8fdd on
         tether 16734438331890270208
         INFO: 2020/04/13 03:29:13 "09b7ef9d-f53d-466a-a174-e88fc7e5286d": received response from target
         "apigee-mart-apigee-connect-hybrid-prod.apigee.svc.cluster.local:8843", status code: 200
         INFO: 2020/04/13 03:29:13 Attempting to send response 09b7ef9d-f53d-466a-a174-e88fc7e5286d on
         tether 16734438331890270208
         INFO: 2020/04/13 03:29:14 "c2ce8b73-8faf-4a05-88d9-24fb2bf45552": received response from target
         "apigee-mart-apigee-connect-hybrid-prod.apigee.svc.cluster.local:8843", status code: 200
         INFO: 2020/04/13 03:29:14 Attempting to send response c2ce8b73-8faf-4a05-88d9-24fb2bf45552 on
         tether 12483040283652521984
         INFO: 2020/04/13 03:29:15 "fdc3bac5-2b83-4b57-a28d-d8b455dae71e": received response from target
         "apigee-mart-apigee-connect-hybrid-prod.apigee.svc.cluster.local:8843", status code: 200
         INFO: 2020/04/13 03:29:15 Attempting to send response fdc3bac5-2b83-4b57-a28d-d8b455dae71e on
         tether 12483040283652521984
         INFO: 2020/04/13 03:29:16 "260026a9-f578-4447-a1d2-d8e49cf181d8": received response from target
         "apigee-mart-apigee-connect-hybrid-prod.apigee.svc.cluster.local:8843", status code: 200
         INFO: 2020/04/13 03:29:16 Attempting to send response 260026a9-f578-4447-a1d2-d8e49cf181d8 on
         tether 12483040283652521984
         INFO: 2020/04/13 03:29:17 "bf3d74a1-94ae-4041-892f-56f1ed9c9cff": received response from target
         "apigee-mart-apigee-connect-hybrid-prod.apigee.svc.cluster.local:8843", status code: 200
         INFO: 2020/04/13 03:29:17 Attempting to send response bf3d74a1-94ae-4041-892f-56f1ed9c9cff on
         tether 16734438331890270208
         INFO: 2020/04/13 03:29:18 "6d017278-3b7a-40fb-9c63-7c34320e7df1": received response from target
         "apigee-mart-apigee-connect-hybrid-prod.apigee.svc.cluster.local:8843", status code: 200

Logs caused by Connect Agent failure due to IAM permission denied error, causing the agent to crash: 
         
         F0719 12:34:33.128565 2326128 tether.go:29] failed to register stream with Apigee Connect, got
         'PermissionDenied': rpc error: code = PermissionDenied desc = Permission denied on resource '//
         apigeeconnect.googleapis.com/projects/apigee-connect-hybrid-prod/endpoints/APIGEE_MART' (or it
         may not exist).
         
         F0719 12:34:33.128565 2326128 tether.go:29] failed to register stream with Apigee Connect, got
         'PermissionDenied': rpc error: code = PermissionDenied desc = Permission denied on resource pro
         ject apigee-connect-hybrid-prod.




## Removing Apigee Connect

If you delete the Apigee Connect deployment, the pod status can remain in the "Terminating" state for up to seven minutes. This amount of time is expected. Apigee Connect agents wait for the existing connections to expire instead of stopping them suddenly. The delay ensures that inflight requests are not lost. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
