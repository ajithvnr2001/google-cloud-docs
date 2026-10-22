---
url: https://docs.cloud.google.com/distributed-cloud/gemini-on-gdcc/latest/docs/endpoints/
title: Create and manage endpoints \u00a0|\u00a0 Gemini on GDC API on GDC connected \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:39:24.216774+00:00
---

# Create and manage endpoints  |  Gemini on GDC API on GDC connected  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/gemini-on-gdcc/latest/docs/endpoints/

**Gemini on GDC API on GDC connected Public Preview (current)**

For version information, see the [Gemini on GDC API on GDC connected release notes](https://docs.cloud.google.com/distributed-cloud/gemini-on-gdcc/latest/docs/release-notes). 

Available versions: **Public Preview**

  * [ Home ](https://docs.cloud.google.com/)
  * [ Gemini on GDC API on GDC connected ](https://docs.cloud.google.com/distributed-cloud/gemini-on-gdcc/latest)
  * [ Documentation ](https://docs.cloud.google.com/distributed-cloud/gemini-on-gdcc/latest/docs)
  * [ Guides ](https://docs.cloud.google.com/distributed-cloud/gemini-on-gdcc/latest/docs/overview)



Send feedback 

#  Create and manage endpoints Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Warning:** During the Preview period, you may only use Gemini on GDC connected API for evaluation and testing purposes. You may not use the Preview release of Gemini on GDC connected API for commercial or production purposes, or disclose generated output to a third party.

This page describes how to create and manage Gemini on Google Distributed Cloud connected API endpoints.

## Prerequisites

This section describes the one-time steps you must complete before you can deploy Gemini on GDC connected API endpoints. Complete the steps on the [turn-up machine](https://docs.cloud.google.com/distributed-cloud/gemini-on-gdcc/latest/docs/requirements#turn-up).

You must complete the steps in this section using an IT Administrator account with the [Edge Container Zone Viewer role](https://docs.cloud.google.com/distributed-cloud/gemini-on-gdcc/latest/docs/permissions#edgecontainer). When you've completed the steps in this section, provide the gathered information, including the CA certificate and the DNS server IP address to the Google Cloud project Administrator who deploys the endpoint as described in Deploy a Gemini on GDC connected API endpoint.

### Complete the hardware turn-up

Before you complete the steps on this page, you must:

  * Successfully deploy the Google-certified hardware as described in [Installation requirements](https://docs.cloud.google.com/distributed-cloud/gemini-on-gdcc/latest/docs/requirements).

  * Work with your Google representative to create the required Distributed Cloud connected clusters.




### Grant the required roles

You must configure the following required roles:

  * For accounts used to manage your Gemini on GDC connected API deployment, grant the roles listed in [Distributed Cloud Edge Container API roles and permissions](https://docs.cloud.google.com/distributed-cloud/gemini-on-gdcc/latest/docs/permissions#edgecontainer).

  * For accounts used to interact with Gemini on GDC connected API endpoints, grant the roles listed in [Vertex AI API roles and permissions](https://docs.cloud.google.com/distributed-cloud/gemini-on-gdcc/latest/docs/permissions#vertex_ai).




### Get information about the target Distributed Cloud connected zone

To get the name of your target Distributed Cloud connected zone, do the following:

  1. Get the name of the target Google Cloud organization ID:
         
         gcloud organizations list
         

  2. List the Distributed Cloud connected zones in your Google Cloud organization:
         
         gcloud alpha edge-cloud zones list \
            --organization ORGANIZATION_ID \
            --location REGION
         

Replace the following:

     * `ORGANIZATION_ID`: the ID of the target Google Cloud organization.
     * `REGION`: the Google Cloud region in which the target Distributed Cloud connected zone has been created. During Public Preview, the only supported region is `us-west2`.
  3. Get detailed information about the target zone:
         
         gcloud alpha edge-cloud zones describe ZONE \
            --organization ORGANIZATION_ID \
            --location REGION
         

Replace the following:

     * `ZONE`: the target Distributed Cloud connected zone.
     * `ORGANIZATION_ID`: the ID of the target Google Cloud organization.
     * `REGION`: the Google Cloud region in which the target Distributed Cloud connected zone has been created. During Public Preview, the only supported region is `us-west2`.



### Get information about the certified machines in your Distributed Cloud connected zone

To get the names of the target certified machines in your Distributed Cloud connected zone, do the following:

  1. List the Distributed Cloud connected machines in the target Distributed Cloud connected zone as described in [List machines in a zone](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/machines#list_machines_in_a_zone).

  2. Get detailed information about the target machine as described in [Get information about a machine](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/machines#machine-info).




### Enable the local AI Platform API and Vertex AI API services

Use an IT Administrator account with the [Edge Container Zonal Project Admin role](https://docs.cloud.google.com/distributed-cloud/gemini-on-gdcc/latest/docs/permissions#edgecontainer) to complete the steps in this section.

  1. Enable the target Google Cloud project in your target Distributed Cloud connected zone:
         
         gcloud alpha edge-cloud projects enable PROJECT_ID \
            --organization ORGANIZATION_ID \
            --location REGION \
            --zone ZONE
         

Replace the following:

     * `PROJECT_ID`: the ID of the target Google Cloud project.
     * `ORGANIZATION_ID`: the ID of the target Google Cloud organization.
     * `REGION`: the Google Cloud region in which the target Distributed Cloud connected zone has been created.
     * `ZONE`: the target Distributed Cloud connected zone.
  2. Enable the AI Platform service on the target Google Cloud project:
         
         gcloud services enable aiplatform.googleapis.com --project PROJECT_ID
         

Replace `PROJECT_ID` with the ID of the target Google Cloud project.

  3. Enable the Vertex AI API service on the Distributed Cloud connected zone:
         
         gcloud alpha edge-cloud services enable aiplatform.googleapis.com --project PROJECT_ID \
            --location REGION \
            --zone ZONE
         

Replace the following:

     * `PROJECT_ID`: the ID of the target Google Cloud project.
     * `REGION`: the Google Cloud region in which the target Distributed Cloud connected zone has been created.
     * `ZONE`: the target Distributed Cloud connected zone.



### Configure the endpoint for DNS resolution

  1. Get the managed DNS address, the top-level domain (TLD), and the Certificate Authority (CA) certificate for target Distributed Cloud connected zone.
         
         gcloud alpha edge-cloud zones describe ZONE \
           --organization ORGANIZATION_ID \
           --location REGION \
           --format="value(certificateAuthorities)" \
           > CA_CERTIFICATE_FILE
         

Replace the following:

     * `ORGANIZATION_ID`: the ID of the target Google Cloud organization.
     * `REGION`: the Google Cloud region in which the target Distributed Cloud connected zone has been created.
     * `ZONE`: the target Distributed Cloud connected zone.
     * `CA_CERTIFICATE_FILE`: the file to which the certificate payload output by the command is saved. You will use this file later to generate the service account key.

Output similar to the following is stored in the file:
    
    -----BEGIN CERTIFICATE-----
    MIIDATCCAemgAwIBAgIRAOsIG15loHwPBpjQe9FZYUAwDQYJKoZIhvcNAQELBQAw
    GjEYMBYGA1UEAxMPZ2RjZS1jbHVzdGVyLWNhMB4XDTI1MDcyOTEyMTAwNloXDTQ5
    MDcyMzEyMTAwNlowGjEYMBYGA1UEAxMPZ2RjZS1jbHVzdGVyLWNhMIIBIjANBgkq
    hkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA3YdoASubyzHdgZ0vIU5g1dxdFRT1T4wc
    o9FaRXftSTDfiNVNKj/vC+De9EZokpyLZkdZNep6p0TLJAsPZYq+yiTCiaJ6Ihwy
    3LBn8j2PessSIte2LUhkft1yCQqfkgpYfKcjM3IauIXETS961m0uJb4sntgLJ4nM
    Scb5vpW1f70D1V27bqnEsE7+rbxzeFTosHC+DGBcLqIE0ptdionm/4xoltH7yv2O
    qKfcc/46TyPwGRzxifEdNzjKZ1kRdTThESfW+L7TQNv6VF5TC4FPksYX/ID/X7Fz
    G9BRey0mikvc4J7qQIeyMRlpIKqRh/1FCdRDC9vVEQipT2Ls0MwwTwIDAQABo0Iw
    QDAOBgNVHQ8BAf8EBAMCAYYwDwYDVR0TAQH/BAUwAwEB/zAdBgNVHQ4EFgQUmES2
    pyMLOnnsKug8amFmenOaTr8wDQYJKoZIhvcNAQELBQADggEBADn71zo7cNFZ0kQE
    C2lS6b0DLz4Nd1yCz5fGDvxzcTRdOT60wyq/TAx1YlYse33cGk/cQ7RkVsM56UX1
    T8RMvi09UcEQG3wFrYuU62ZjXF1a3RrOnHxyvVdyvbUYAO5gvzBQrj4tMZYX9kL3
    6H/9FwXuHVyqWAm0xpWvZfszwJjY4C1VxoDwmRiZPYzTrWI6/rY0QmORgcZXLnPL
    OVufbAX30aRGdTRnVXxE0fKmXwzbtbSHilU5hJT7EQWMvV5hJfyNqdXG0gbrhrsk
    sB0yRjk5PHQd9pOMcXcYIgfNnUEcQl4qeSll3g5cZ+cRrcTO1USFLRo8dcbQpJ6Y
    6ykzvKs=
    -----END CERTIFICATE-----
    createTime: '2025-08-25T20:46:50.269384028Z'
    dnsServers:
    - ipAddress: DNS_SERVER_ADDRESS
    tld: TOP_LEVEL_DOMAIN
    name: organizations/ORGANIZATION_ID/locations/REGION/zones/ZONE
    state: STATE_RUNNING
    

  2. Create the DNS configuration for the endpoint as follows using the DNS server IP address and Top-Level Domain (TLD) name obtained in the previous step. You must run this command from a machine that's on the same local network as the Gemini on GDC connected API certified machine.
         
         mkdir /etc/systemd/resolved.conf.d
         echo '[Resolve]
         DNS=DNS_SERVER_ADDRESS
         Domains=~TOP_LEVEL_DOMAIN' > /etc/systemd/resolved.conf.d/dns.conf
         sudo systemctl restart systemd-resolved
         

Replace the following:

     * `DNS_SERVER_ADDRESS`: the IP address of your DNS server.
     * `TOP_LEVEL_DOMAIN`: the top-level domain for the endpoint.



## Deploy a Gemini on GDC connected API endpoint

To deploy a Gemini on GDC connected API endpoint, do the following using a Google Cloud project Administrator account:

  1. Create the endpoint:
         
         gcloud beta ai endpoints create \
            --project=PROJECT_ID \
            --region=REGION \
            --gdc-zone=ZONE \
            --display-name=ENDPOINT_NAME \
            --endpoint-id=ENDPOINT_ID
         

Replace the following:

     * `PROJECT_ID`: the ID of the target Google Cloud project.
     * `REGION`: the Google Cloud region in which the target Distributed Cloud connected zone has been created.
     * `ZONE`: the target Distributed Cloud connected zone.
     * `ENDPOINT_NAME`: a meaningful name for this endpoint.
     * `ENDPOINT_ID`: (optional) a unique identifier for this endpoint. If omitted, a random identifier is generated.
  2. Deploy the model:
         
         gcloud beta ai endpoints deploy-model ENDPOINT_ID \
           --display-name=ENDPOINT_NAME \
           --model=MODEL_PUBLIC_ID \
           --region=REGION
         

Replace the following:

     * `ENDPOINT_ID`: the ID of the target endpoint.
     * `ENDPOINT_NAME`: the name of the target endpoint.
     * `REGION`: the Google Cloud region in which the target Distributed Cloud connected zone has been created.
     * `MODEL_PUBLIC_ID`: the model's public-facing ID. For a list of supported models, see [Supported models](https://docs.cloud.google.com/distributed-cloud/gemini-on-gdcc/latest/docs/how-it-works#supported_models).
  3. List the deployed endpoints:
         
         gcloud beta ai endpoints list \
           --project=PROJECT_ID \
           --region=REGION
         

Replace the following:

     * `PROJECT_ID`: the ID of the target Google Cloud project.
     * `REGION`: the Google Cloud region in which the target Distributed Cloud connected zone has been created.

Note the ID of the target endpoint.

  4. Get the endpoint address:
         
         gcloud beta ai endpoints describe ENDPOINT_ID \
           --project=PROJECT_ID \
           --region=REGION
         

Replace the following:

     * `ENDPOINT_ID`: the ID of the target endpoint.
     * `PROJECT_ID`: the ID of the target Google Cloud project.
     * `REGION`: the Google Cloud region in which the target Distributed Cloud connected zone has been created.
  5. Create the service account for the endpoint in the target Distributed Cloud connected zone:
         
         gcloud alpha edge-cloud service-accounts create SERVICE_ACCOUNT \
           --project PROJECT_ID \
           --location REGION \
           --zone ZONE
         

Replace the following:

     * `SERVICE_ACCOUNT`: a meaningful name that uniquely identifies this service account. This name must only consist of lowercase letters, numbers, '-' or '.', and must begin and end with an alphanumeric character. Uppercase letters are not allowed.
     * `PROJECT_ID`: the ID of the target Google Cloud project.
     * `REGION`: the Google Cloud region in which the target Distributed Cloud connected zone has been created.
     * `ZONE`: the target Distributed Cloud connected zone.
  6. Get the Identity and Access Management policy for the target Distributed Cloud connected zone:
         
         gcloud alpha edge-cloud zones get-iam-policy ZONE \
           --project PROJECT_ID \
           --location REGION
         

Replace the following:

     * `ZONE`: the target Distributed Cloud connected zone.
     * `PROJECT_ID`: the ID of the target Google Cloud project.
     * `REGION`: the Google Cloud region in which the target Distributed Cloud connected zone has been created.

Copy the policy payload output from this command and save it to a file (for example, `policy.json` or `policy.yaml`) for editing in the next step.

  7. Assign the [AI Platform Gemini Developer](https://docs.cloud.google.com/distributed-cloud/gemini-on-gdcc/latest/docs/permissions#gemini_on_gdc) (`roles/aiplatform.geminiDeveloper`) role to the service account:
         
         gcloud alpha edge-cloud zones set-iam-policy POLICY_FILE \
           --project PROJECT_ID \
           --location REGION \
           --zone ZONE
         

Replace the following:

     * `POLICY_FILE`: JSON or YAML file containing the role assignment policy.
     * `PROJECT_ID`: the ID of the target Google Cloud project.
     * `REGION`: the Google Cloud region in which the target Distributed Cloud connected zone has been created.
     * `ZONE`: the target Distributed Cloud connected zone.
**Caution:** The `set-iam-policy` command performs an authoritative overwrite and replaces the entire existing policy. Don't create a new policy file from scratch or leave the `etag` empty. In your saved policy file, append your new service account to the `members` list under the `roles/aiplatform.geminiDeveloper` role while preserving all existing bindings and the original `etag`. Overwriting the policy with missing members will revoke access for all other service accounts configured in the zone.

The following is an example policy in JSON format:
    
    {
      "bindings": [
         {
            "role": "roles/aiplatform.geminiDeveloper",
            "members": [
               {
                  "serviceAccount": "projects/PROJECT_ID/locations/REGION/serviceAccounts/SERVICE_ACCOUNT"
               }
            ]
         }
      ],
      "etag": ""
    }
    

The following is an example policy in YAML format:
    
    bindings:
    - role: roles/aiplatform.geminiDeveloper
      members:
      - serviceAccount: projects/PROJECT_ID/locations/REGION/serviceAccounts/SERVICE_ACCOUNT
    etag: ""
    

Replace the following:

     * `PROJECT_ID`: the ID of the target Google Cloud project.
     * `REGION`: the Google Cloud region in which the target Distributed Cloud connected zone has been created.
     * `SERVICE_ACCOUNT`: a meaningful name that uniquely identifies this service account.
  8. Generate a key for the service account:
         
         gcloud alpha edge-cloud service-accounts keys create SA_KEY_FILE \
           --service-account SERVICE_ACCOUNT \
           --project PROJECT_ID \
           --location REGION \
           --ca-cert-path CA_CERTIFICATE_FILE
         

Replace the following:

     * `SA_KEY_FILE`: file in which to store the generated service account key.
     * `SERVICE_ACCOUNT`: the service account you created earlier in this guide.
     * `PROJECT_ID`: the ID of the target Google Cloud project.
     * `REGION`: the Google Cloud region in which the target Distributed Cloud connected zone has been created.
     * `CA_CERTIFICATE_FILE`: the CA certificate file you created earlier.
  9. Get the endpoint's fully qualified URL:
         
         gcloud beta ai endpoints describe ENDPOINT_ID \
           --project=PROJECT_ID \
           --region=REGION
         

Replace the following:

     * `ENDPOINT_ID`: the target endpoint identifier.
     * `PROJECT_ID`: the ID of the target Google Cloud project.
     * `REGION`: the Google Cloud region in which the target Distributed Cloud connected zone has been created.
  10. Print the identity token for the service account. You must run this command from a machine that's on the same local network as the Gemini on GDC connected API certified machine.
         
         gcloud alpha edge-cloud auth print-identity-token \
           --cred-file=SA_KEY_FILE \
           --audience=ENDPOINT_URL
         

Replace the following:

     * `SA_KEY_FILE`: the service account key file you created earlier.
     * `ENDPOINT_URL`: the endpoint's fully qualified URL, including the TLD suffix.



## List deployed Gemini on GDC connected API endpoints

To list your deployed Gemini on GDC connected API endpoints, do the following:
    
    
    gcloud beta ai endpoints list \
        --project=PROJECT_ID \
        --region=REGION \
        --gdc-zone=ZONE
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the target Distributed Cloud connected zone has been created.
  * `ZONE`: the target Distributed Cloud connected zone.



## Get information about a Gemini on GDC connected API endpoint

To get information about a deployed Gemini on GDC connected API endpoint, do the following:
    
    
    gcloud beta ai endpoints describe ENDPOINT_ID \
        --project=PROJECT_ID \
        --region=REGION
       

Replace the following:

  * `ENDPOINT_ID`: the ID of the target endpoint.
  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the target Distributed Cloud connected zone has been created.



## Interact with a Gemini on Google Distributed Cloud connected API endpoint

Your Gemini on GDC connected API endpoint supports interaction through the `ChatCompletions` API and the `ListAvailableModels` API. Use these APIs to programmatically interact with your endpoint.

Here's an example of a request through the `ChatCompletions` API. The bearer token generated in this request is valid for 12 hours.

  1. Set the following variables in your shell environment:
         
         MODEL_PROMPT_ID="MODEL_PROMPT_ID"
         USER_CONTENT="Who invented the light bulb?"
         PROJECT="PROJECT_ID"
         LOCATION="REGION"
         IG_FQDN="inference-gateway.vai.ZONE.google.private.goog"
         CRED_FILE="SA_KEY_FILE"
         API_ENDPOINT="https://${IG_FQDN}/v1/projects/${PROJECT}/locations/${LOCATION}/chat/completions"
         

Replace the following:

     * `MODEL_NAME`: the name of the target model.
     * `PROJECT_ID`: the ID of the target Google Cloud project.
     * `REGION`: the Google Cloud region in which the target Distributed Cloud connected zone has been created.
     * `SA_KEY_FILE`: the service account key file you created earlier.
  2. Build the payload:
         
         REQUEST_BODY=$(cat <<EOF
         {
         "model": "${MODEL_PROMPT_ID}",
         "messages": [
            {
               "role": "system",
               "content": "Pizza for everyone!"
            },
            {
               "role": "user",
               "content": "${USER_CONTENT}"
            }
         ],
         "stream": false
         }
         EOF
         )
         

  3. Print the bearer token. You must run this command from a machine that's on the same local network as the Gemini on GDC connected API certified machine.
         
         BEARER_TOKEN=$(gcloud alpha edge-cloud auth print-identity-token --cred-file="${CRED_FILE}" --audience="https://${IG_FQDN}")
          echo $BEARER_TOKEN
         

  4. Send the request to the endpoint. You must run this command from a machine that's on the same local network as the Gemini on GDC connected API certified machine:
         
         curl -k -X POST \
         "${API_ENDPOINT}" \
         -d "${REQUEST_BODY}" \
         -H "Content-Type: application/json" \
         -H "Authorization: Bearer ${BEARER_TOKEN}" \
         -H "x-goog-user-project: projects/${PROJECT}"
         




### Example multimodal `ChatCompletions` API request with a JPEG image payload

The following is an example of a multimodal `ChatCompletions` API request payload with a JPEG image as input:

  1. Build the payload:
         
         BASE64_IMAGE=$(base64 -w 0 JPEG_FILE)
         REQUEST_BODY=$(cat <<EOF
         {
         "model": "${MODEL_PROMPT_ID}",
         "messages": [
            {
               "role": "user",
               "content": [
                     {
                        "type": "text",
                        "text": "What is this image?"
                     },
                     {
                        "type": "image_url",
                        "image_url": {
                           "url": "data:image/jpeg;base64,${BASE64_IMAGE}"
                        }
                     }
               ]
            }
         ]
         }
         EOF
         
         )
         

  2. Send the request to the endpoint. You must run this command from a machine that's on the same local network as the Gemini on GDC connected API certified machine.
         
         curl -k -X POST \
         "${API_ENDPOINT}" \
         -d "${REQUEST_BODY}" \
         -H "Content-Type: application/json" \
         -H "Authorization: Bearer ${BEARER_TOKEN}" \
         -H "x-goog-user-project: projects/${PROJECT}"
         




### Example multimodal `ChatCompletions` API request with a PDF document payload

The following is an example of a multimodal `ChatCompletions` API request payload with a PDF document as input:

  1. Build the payload:
         
         BASE64_PDF=$(base64 -w 0 PDF_FILE)
         REQUEST_BODY=$(cat <<EOF
         {
         "model": "${MODEL_PROMPT_ID}",
         "messages": [
            {
               "role": "user",
               "content": [
                     {
                        "type": "text",
                        "text": "Please summarize this document."
                     },
                     {
                        "type": "input_document",
                        "input_document": {
                           "data": "data:application/pdf;base64,${BASE64_PDF}",
                           "format": "pdf"
                        }
                     }
               ]
            }
         ]
         }
         EOF
         
         )
         

  2. Send the request to the endpoint. You must run this command from a machine that's on the same local network as the Gemini on GDC connected API certified machine.
         
         curl -k -X POST \
         "${API_ENDPOINT}" \
         -d "${REQUEST_BODY}" \
         -H "Content-Type: application/json" \
         -H "Authorization: Bearer ${BEARER_TOKEN}" \
         -H "x-goog-user-project: projects/${PROJECT}"
         




### Example multimodal `ChatCompletions` API request with an audio payload

The following is an example of a multimodal `ChatCompletions` API request payload with an audio file as input:

  1. Build the payload:
         
         BASE64_AUDIO=$(base64 -w 0 AUDIO_FILE)
         REQUEST_BODY=$(cat <<EOF
         {
         "model": "${MODEL_PROMPT_ID}",
         "messages": [
            {
               "role": "user",
               "content": [
                     {
                        "type": "text",
                        "text": "Transcribe this speech for me."
                     },
                     {
                        "type": "input_audio",
                        "input_audio": {
                           "data": "data:audio/mp3;base64,${BASE64_AUDIO}",
                           "format": "mp3"
                        }
                     }
               ]
            }
         ]
         }
         EOF
         
         )
         

  2. Send the request to the endpoint. You must run this command from a machine that's on the same local network as the Gemini on GDC connected API certified machine.
         
         curl -k -X POST \
         "${API_ENDPOINT}" \
         -d "${REQUEST_BODY}" \
         -H "Content-Type: application/json" \
         -H "Authorization: Bearer ${BEARER_TOKEN}" \
         -H "x-goog-user-project: projects/${PROJECT}"
         




### Example multimodal `ChatCompletions` API request with a video payload

The following is an example of a multimodal `ChatCompletions` API request payload with a video file as input:

  1. Build the payload:
         
         BASE64_VIDEO=$(base64 -w 0 VIDEO_FILE)
         REQUEST_BODY=$(cat <<EOF
         {
         "model": "${MODEL_PROMPT_ID}",
         "messages": [
            {
               "role": "user",
               "content": [
                     {
                        "type": "text",
                        "text": "Could you summarize this video for me?"
                     },
                     {
                        "type": "input_video",
                        "input_video": {
                           "data": "data:video/wmv;base64,${BASE64_VIDEO}",
                           "format": "wmv"
                        }
                     }
               ]
            }
         ]
         }
         EOF
         
         )
         

  2. Send the request to the endpoint. You must run this command from a machine that's on the same local network as the Gemini on GDC connected API certified machine.
         
         curl -k -X POST \
         "${API_ENDPOINT}" \
         -d "${REQUEST_BODY}" \
         -H "Content-Type: application/json" \
         -H "Authorization: Bearer ${BEARER_TOKEN}" \
         -H "x-goog-user-project: projects/${PROJECT}"
         




### Example `ListAvailableModels` API request

The following is an example of a `ListAvailableModels` API request:
    
    
    BEARER_TOKEN=$(gcloud alpha edge-cloud auth print-identity-token --cred-file="${CRED_FILE}" --audience="https://${IG_FQDN}")
    # The request body -d parameter is intentionally omitted.
    grpcurl -insecure \
      -H "Authorization: Bearer ${BEARER_TOKEN}" \
      -H "x-goog-user-project: projects/${PROJECT}" \
      "${IG_FQDN}" \
      cloud.gdc.ai.inference.inferencegateway.GeminiMetadataService.ListAvailableModels
    

## Delete a Gemini on Google Distributed Cloud connected API endpoint

To delete a Gemini on GDC connected API endpoint, do the following:

  1. Undeploy the model:
         
         gcloud beta ai endpoints undeploy-model ENDPOINT_ID \
           --region=REGION \
           --deployed-model-id=DEPLOYED_MODEL_ID
         

Replace the following:

     * `ENDPOINT_ID`: the ID of the target endpoint.
     * `REGION`: the Google Cloud region in which the target Distributed Cloud connected zone has been created.
     * `DEPLOYED_MODEL_ID`: the ID of the deployed model.
  2. Delete the endpoint:
         
         gcloud beta ai endpoints delete ENDPOINT_ID \
            --project=PROJECT_ID \
            --region=REGION
         

Replace the following:

     * `ENDPOINT_ID`: the ID of the target endpoint.
     * `PROJECT_ID`: the ID of the target Google Cloud project.
     * `REGION`: the Google Cloud region in which the target Distributed Cloud connected zone has been created.



## Clean up endpoint resources

To clean up the resources associated with an endpoint, complete the steps in this section.

  1. Delete the endpoint and undeploy the associated model as described in Delete a Gemini on Google Distributed Cloud connected API endpoint.

  2. Delete the service account associated with the endpoint:
         
         gcloud alpha edge-cloud service-accounts delete SERVICE_ACCOUNT \
             --project PROJECT_ID \
             --location REGION
         

Replace the following:

     * `SERVICE_ACCOUNT`: the name of the target service account.
     * `PROJECT_ID`: the ID of the target Google Cloud project.
     * `REGION`: the Google Cloud region of the target Google Cloud project.
  3. Disable the Agent Platform service instance associated with the endpoint:

     1. List the services deployed within the project and note the UUID value of the target Agent Platform (`VERTEX`) service instance returned in its `name` field:
            
            gcloud alpha edge-cloud services list \
               --project PROJECT_ID \
               --location REGION
            

Replace the following:

        * `PROJECT_ID`: the ID of the target Google Cloud project.
        * `REGION`: the Google Cloud region of the target Google Cloud project.

The `name` field value has the format `projects/PROJECT_ID/locations/REGION/zonalServices/SERVICE_UUID`.

     2. Disable the target Agent Platform (`VERTEX`) service instance:
            
            gcloud alpha edge-cloud services disable SERVICE_UUID \
              --project PROJECT_ID \
              --location REGION
            

Replace the following:

        * `SERVICE_UUID`: the UUID of the target Agent Platform service instance.
        * `PROJECT_ID`: the ID of the target Google Cloud project.
        * `REGION`: the Google Cloud region of the target Google Cloud project.
  4. Disable the Google Cloud project hosting the endpoint:
         
         gcloud alpha edge-cloud projects disable PROJECT_ID \
             --organization ORGANIZATION_ID \
             --location REGION \
             --zone ZONE
         

Replace the following:

     * `PROJECT_ID`: the ID of the target Google Cloud project.
     * `ORGANIZATION_ID`: the ID of the target Google Cloud organization.
     * `REGION`: the Google Cloud region of the target Google Cloud project.
     * `ZONE`: the target Distributed Cloud connected zone.



### Troubleshoot endpoints

If your Gemini on GDC connected API endpoint goes down, contact your Google representative to troubleshoot it.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
