---
url: https://docs.cloud.google.com/chrome-enterprise-premium/docs/manage-security-gateway/
title: Manage a secure gateway \u00a0|\u00a0 Chrome Enterprise Premium \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:01:27.818741+00:00
---

# Manage a secure gateway  |  Chrome Enterprise Premium  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chrome-enterprise-premium/docs/manage-security-gateway/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Chrome Enterprise Premium ](https://docs.cloud.google.com/chrome-enterprise-premium/docs)
  * [ Guides ](https://docs.cloud.google.com/chrome-enterprise-premium/docs/overview)



Send feedback 

#  Manage a secure gateway Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to complete common secure gateway management tasks.

## Set up your shell environment

To streamline the setup process and interact with the secure gateway APIs, define the following environment variables in your working shell.

  * General parameters
        
        PROJECT_ID=PROJECT_ID
        APPLICATION_ID=APPLICATION_ID
        APPLICATION_DISPLAY_NAME="APPLICATION_DISPLAY_NAME"
        HOST_NAME=HOST_NAME

Replace the following:

    * `PROJECT_ID`: The ID of the project where the secure gateway is created.
    * `APPLICATION_ID`: The ID of your application, such as `github`. The name can be up to 63 characters, and can contain lowercase letters, numbers, and hyphens. The first character must be a letter, and the last character can be a letter or number.
    * `APPLICATION_DISPLAY_NAME`: The human-readable name to display.
    * `HOST_NAME`: The hostname of your application. For example, `github.com`. The hostname can be up to 253 characters long, and must adhere to one of the following formats:

      * A valid IPv4 address
      * A valid IPv6 address
      * A [valid DNS](https://datatracker.ietf.org/doc/html/rfc1034) name
      * An asterisk (*)
      * An asterisk (*) followed by a valid DNS name
  * Secure gateway parameters
        
        SECURITY_GATEWAY_ID=SECURITY_GATEWAY_ID
        SECURITY_GATEWAY_DISPLAY_NAME="SECURITY_GATEWAY_DISPLAY_NAME"

Replace the following:

    * `SECURITY_GATEWAY_ID`: The ID of the secure gateway. The ID can be up to 63 characters, and can contain lowercase letters, numbers, and hyphens. The first character should be a letter, and the last character can be a letter or number.
    * `SECURITY_GATEWAY_DISPLAY_NAME`: The human-readable name of the secure gateway. The name can be up to 63 characters long and can only contain printable characters.



## Update a secure gateway

The following example shows how to update the hubs of an existing secure gateway.

### console

To update the egress hubs of a secure gateway, do the following:

  1. In the Google Cloud console, go to the **SaaS Egress Hubs** page.   
[Go to SaaS Egress Hubs](https://console.cloud.google.com/security/cep/secure-gateway/egress-hubs)
  2. Select the project you want to update the SaaS Egress Hubs for.
  3. To add SaaS egress hubs, click **Add SaaS egress hub**.
  4. From the drop-down list, select the regions where you'd like to add the egress hubs.
  5. To add hubs, click **Add SaaS egress hub**. To update the egress hubs, click **Save**.



### gcloud
    
    
    gcloud beyondcorp security-gateways update SECURITY_GATEWAY_ID \
        --project=PROJECT_ID \
        --location=global \
        --hubs=us-central1,us-east1
          

### REST
    
    
    curl \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        -X PATCH \
        -d "{ \"hubs\": {\"us-central1\": {}, \"us-east1\": {}} }" \
        "https://beyondcorp.googleapis.com/v1/projects/PROJECT_ID/locations/global/securityGateways/SECURITY_GATEWAY_ID?update_mask=hubs"
          

## Get a secure gateway's details

To get the details for a secure gateway, run the following command.

### gcloud
    
    
    gcloud beyondcorp security-gateways describe SECURITY_GATEWAY_ID \
        --project=PROJECT_ID \
        --location=global
          

### REST
    
    
    curl \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://beyondcorp.googleapis.com/v1/projects/PROJECT_ID/locations/global/securityGateways/SECURITY_GATEWAY_ID"
          

## List secure gateways

To list all of the secure gateways in a project, run the following command.

### gcloud
    
    
    gcloud beyondcorp security-gateways list \
        --project=PROJECT_ID \
        --location=global
          

### REST
    
    
    curl \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://beyondcorp.googleapis.com/v1/projects/PROJECT_ID/locations/global/securityGateways"
          

## Delete a secure gateway

To delete a secure gateway, run the following command.

### gcloud
    
    
    gcloud beyondcorp security-gateways delete SECURITY_GATEWAY_ID \
        --project=PROJECT_ID \
        --location=global
          

### REST
    
    
    curl \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        -X DELETE \
        "https://beyondcorp.googleapis.com/v1/projects/PROJECT_ID/locations/global/securityGateways/SECURITY_GATEWAY_ID"
          

## Enable secure gateway logging

To enable secure gateway logging, run the following command.

### console

To enable logging, do the following:

  1. Go to the **Secure Gateway Logging** page.   
[Go to Secure Gateway Logging](https://console.cloud.google.com/security/cep/secure-gateway/logging)
  2. Check **Enable logging**



### gcloud
    
    
            gcloud beyondcorp security-gateways update SECURITY_GATEWAY_ID \
            --project=PROJECT_ID \
            --location=global \
            --logging={}
          

### REST
    
    
    curl \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        -X PATCH \
        -d "{ \"logging\": {} }" \
        "https://beyondcorp.googleapis.com/v1/projects/PROJECT_ID/locations/global/securityGateways/SECURITY_GATEWAY_ID?update_mask=logging"
          

## Disable secure gateway logging

To disable secure gateway logging, run the following command.

### console

To disable logging, do the following:

  1. Go to the **Secure Gateway Logging** page.   
[Go to Secure Gateway Logging](https://console.cloud.google.com/security/cep/secure-gateway/logging)
  2. Clear **Enable logging**



### gcloud
    
    
            gcloud beyondcorp security-gateways update SECURITY_GATEWAY_ID \
            --project=PROJECT_ID \
            --location=global \
            --clear-logging
          

### REST
    
    
    curl \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        -X PATCH \
        -d "{ \"logging\": null }" \
        "https://beyondcorp.googleapis.com/v1/projects/PROJECT_ID/locations/global/securityGateways/SECURITY_GATEWAY_ID?update_mask=logging"
          

## Update an application resource

The following example shows how to update an existing application. Allowed editable fields include the following:

  * `display_name`
  * `endpoint_matchers`



### console

To update an application resource, do the following:

  1. To modify an application resource, go to the **Applications** page.   
[Go to Applications](https://console.cloud.google.com/security/cep/secure-gateway/applications)
  2. Find the application that you want to edit.
  3. To edit the application, click the **More actions** menu (more_vert) and select **View Details**.
  4. On the Application details page, click **Edit**.
  5. Modify the **Application name** or **Domain matchers** as needed.
  6. To update the application resource, click **Save**.



### gcloud
    
    
    gcloud beyondcorp security-gateways applications update APPLICATION_ID \
        --project=PROJECT_ID \
        --security-gateway=SECURITY_GATEWAY_ID \
        --location=global \
        --endpoint-matchers="hostname=HOST_NAME,ports=[443]"
          

### REST

You can use `update_mask` to control which fields are updated. The following example shows how to update the `endpoint_matchers` field: 
    
    
    curl \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        -X PATCH \
        -d "{ \"endpoint_matchers\": [{hostname: \"HOST_NAME\", ports: [443]}] }" \
        "https://beyondcorp.googleapis.com/v1/projects/PROJECT_ID/locations/global/securityGateways/SECURITY_GATEWAY_ID/applications/APPLICATION_ID?update_mask=endpoint_matchers"
          

## Get the details of an application resource

### console

To get the details of an application resource, do the following:

  1. Go to the **Applications** page.   
[Go to Applications](https://console.cloud.google.com/security/cep/secure-gateway/applications)
  2. Find the application you want to view the details for.
  3. To view the application details, click the application name or go to the **More actions** menu (more_vert) and select **View Details**.



### gcloud

To get the details of an application, run the following command:
    
    
    gcloud beyondcorp security-gateways applications describe APPLICATION_ID \
        --project=PROJECT_ID \
        --security-gateway=SECURITY_GATEWAY_ID \
        --location=global
          

### REST

To get the details of an application, run the following command:
    
    
    curl \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://beyondcorp.googleapis.com/v1/projects/PROJECT_ID/locations/global/securityGateways/SECURITY_GATEWAY_ID/applications/APPLICATION_ID"
          

## List application resources

### console

To list all the application resources, do the following:

  1. Go to the **Applications** page.   
[Go to Applications](https://console.cloud.google.com/security/cep/secure-gateway/applications)
  2. The page displays a table listing all the application resources for the secure gateway, showing details such as Type and Name.



### gcloud

To list all of the applications in a secure gateway, run the following command.
    
    
    gcloud beyondcorp security-gateways applications list \
        --project=PROJECT_ID \
        --security-gateway=SECURITY_GATEWAY_ID \
        --location=global
            

### REST

To list all the applications in a secure gateway, run the following command.
    
    
    curl \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://beyondcorp.googleapis.com/v1/projects/PROJECT_ID/locations/global/securityGateways/SECURITY_GATEWAY_ID/applications"
          

## Delete an application resource

### console

To delete an application resource, do the following:

  1. Go to the **Applications** page.   
[Go to Applications](https://console.cloud.google.com/security/cep/secure-gateway/applications)
  2. Find the application that you want to delete.
  3. To view the application details, click the application name or go to the **More actions** menu (more_vert) and select **View Details**.
  4. To remove the application resource, click **Remove**.



### gcloud

To delete an application, run the following command.
    
    
    gcloud beyondcorp security-gateways applications delete APPLICATION_ID \
        --project=PROJECT_ID \
        --security-gateway=SECURITY_GATEWAY_ID \
        --location=global
          

### REST

To delete an application, run the following command.
    
    
    curl \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        -X DELETE \
        "https://beyondcorp.googleapis.com/v1/projects/PROJECT_ID/locations/global/securityGateways/SECURITY_GATEWAY_ID/applications/APPLICATION_ID"
          

**Important:** Removing the application definition from secure gateway will disrupt user traffic for that application. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
