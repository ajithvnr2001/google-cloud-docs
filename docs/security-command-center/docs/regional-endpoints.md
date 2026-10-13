---
url: https://docs.cloud.google.com/security-command-center/docs/regional-endpoints/
title: Security Command Center regional endpoints \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:13:42.721738+00:00
---

# Security Command Center regional endpoints  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/regional-endpoints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Security Command Center regional endpoints Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation)) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This document explains how to work with Security Command Center resources when [data residency](https://docs.cloud.google.com/security-command-center/docs/data-residency-support) is enabled. You can only enable data residency for Security Command Center when you [activate Security Command Center for an organization](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation).

## Resources with data residency controls

The following Security Command Center resource types are [subject to data residency controls](https://docs.cloud.google.com/security-command-center/docs/data-residency-support#scc-resources-subject-to-drz):

  * All [Google Security Operations](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview) resources
  * [BigQuery export configurations](https://docs.cloud.google.com/security-command-center/docs/how-to-analyze-findings-in-big-query)
  * [Continuous export configurations](https://docs.cloud.google.com/security-command-center/docs/how-to-export-data#continuous_exports)
  * Findings
  * [Mute rule configurations](https://docs.cloud.google.com/security-command-center/docs/how-to-mute-findings)



To work with these resources programmatically or on the command line, you must use the regional endpoints for the Security Command Center API. To work with these resources in the Google Cloud console, you must use the jurisdictional Google Cloud console.

For all other resource types, use the default API endpoints and the [Google Cloud console](https://console.cloud.google.com/).

## About regional endpoints

Regional endpoints provide access to resources in a specific location. When you use a regional endpoint, your request is routed directly to the endpoint's location. You can't use a regional endpoint to access resources in other locations.

Using a regional endpoint helps you [enforce data residency controls](https://docs.cloud.google.com/security-command-center/docs/data-residency-support#enforcement) for your resources when they're at rest, in use, and in transit.

Security Command Center includes multiple services. For resource types that are subject to data residency controls, the following services require you to use regional endpoints:

[Security Command Center API](https://docs.cloud.google.com/security-command-center/docs/reference/rest)
    `securitycenter.LOCATION.rep.googleapis.com`
Google SecOps
    See the [Google SecOps reference documentation](https://docs.cloud.google.com/chronicle/docs/reference).

Replace `LOCATION` with a supported location for the service.

For all other resource types, you must use the default endpoint.

## About the jurisdictional Google Cloud console

The jurisdictional Google Cloud console lets you enable data residency when you [activate Security Command Center](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview). It also provides access to resources in a specific location.

Using the jurisdictional Google Cloud console helps you [enforce data residency controls](https://docs.cloud.google.com/security-command-center/docs/data-residency-support#enforcement) for your resources when they're at rest, in use, and in transit.

You can use the jurisdictional Google Cloud console to access only resource types that are subject to data residency controls. To open the console, use the appropriate URL for your location:

European Union
    [Federated identity users](https://docs.cloud.google.com/iam/docs/workforce-identity-federation): [`console.eu.cloud.google`](https://console.eu.cloud.google/)
    All other users: [`console.eu.cloud.google.com`](https://console.eu.cloud.google.com/)
Kingdom of Saudi Arabia (KSA)
    Federated identity users: [`console.sa.cloud.google`](https://console.sa.cloud.google/)
    All other users: [`console.sa.cloud.google.com`](https://console.sa.cloud.google.com/)
United States
    Federated identity users: [`console.us.cloud.google`](https://console.us.cloud.google/)
    All other users: [`console.us.cloud.google.com`](https://console.us.cloud.google.com/)

For all other resource types, you must use the standard Google Cloud console.

## Locations for regional endpoints

This section lists the locations where regional endpoints are available for the Security Command Center API and related services.

### Locations for the Security Command Center API

The Security Command Center API provides regional and multi-region endpoints in the following locations:

European Union
    `eu`
Kingdom of Saudi Arabia (KSA)
    `me-central2`
United States
    `us`

### Locations for AI Protection

Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

For the full benefit of AI Protection, the AI workloads need to be in these regions: 

European Union
    `europe-west4`: Netherlands ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
Kingdom of Saudi Arabia (KSA)
    `me-central2`: Dammam 
United States
    `us-central1`: Iowa ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
    `us-east4`: Northern Virginia 
    `us-west1`: Oregon ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)

AI Protection provides multi-region endpoints in the following locations: 

European Union
    `eu`
Kingdom of Saudi Arabia (KSA)
    `sa`
United States
    `us`

The available features vary by region. To find out which features are or aren't available in your region, refer to the following table.

Region | Notebook Security Scanner ([Preview](https://cloud.google.com/products/#product-launch-stages)) | [Model Armor](https://docs.cloud.google.com/model-armor/overview) | Features not available  
---|---|---|---  
`me-central2` (KSA) | No | No | 

  * The AI Discovery service is not available. AI Protection doesn't discover Gemini foundation models.
  * Model Armor is not supported in this region. The Gemini Enterprise Agent Platform model isn't protected by Model Armor and the corresponding widgets don't display data in the dashboard.
  * Package vulnerability findings aren't available.

  
`us-east7` | Yes | No | 

  * The Gemini Enterprise Agent Platform model isn't protected by Model Armor.
  * Findings aren't available.
  * Two Model Armor widgets don't have any data available.

  
`europe-west1`   
`europe-west2`   
`asia-southeast1` | No | Yes | Package vulnerability findings aren't available.  
Other regions | No | No | 

  * The Gemini Enterprise Agent Platform model isn't protected by Model Armor.
  * Findings aren't available.
  * Two Model Armor widgets don't have any data available.
  * Package vulnerability findings aren't available.

  
  
### Locations for Google SecOps

See the [Google SecOps locations page](https://cloud.google.com/terms/secops/data-residency).

## Tools for regional endpoints

To manage resource types that are subject to data residency controls, you must specify a regional endpoint when you create a client or run a command.

For all other resource types, you must use the default endpoint.

**Note:** For Google SecOps, see the [Google SecOps reference documentation](https://docs.cloud.google.com/chronicle/docs/reference).

### gcloud

The following gcloud CLI [command groups](https://docs.cloud.google.com/sdk/gcloud#command_groups) require you to use a regional endpoint:

  * [`gcloud scc bqexports`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/bqexports): manages [BigQuery export configurations](https://docs.cloud.google.com/security-command-center/docs/how-to-analyze-findings-in-big-query)
  * [`gcloud scc findings`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/findings): manages findings
  * [`gcloud scc muteconfigs`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/muteconfigs): manages [mute rule configurations](https://docs.cloud.google.com/security-command-center/docs/how-to-mute-findings)
  * [`gcloud scc notifications`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/notifications): manages [continuous export configurations](https://docs.cloud.google.com/security-command-center/docs/how-to-export-data#continuous_exports)



For all other `gcloud scc` command groups, you must use the default endpoint for the Security Command Center API.

### Change the service endpoint

To switch to a regional endpoint, run the following command:
    
    
    gcloud config set api_endpoint_overrides/SERVICE \
        https://SERVICE.LOCATION.rep.googleapis.com/

To switch to the default endpoint, run the following command:
    
    
    gcloud config unset api_endpoint_overrides/SERVICE

Replace the following:

  * `SERVICE`: the service to configure; use `securitycenter` for the Security Command Center API
  * `LOCATION`: a supported location for the service



Optionally, you can create a [named configuration](https://docs.cloud.google.com/sdk/gcloud/reference/topic/configurations) for the gcloud CLI that uses the regional endpoint. Before you run a gcloud CLI command, you can switch to the named configuration by running the [`gcloud config configurations activate`](https://docs.cloud.google.com/sdk/gcloud/reference/config/configurations/activate) command.

### Run a gcloud CLI command

When you run a gcloud CLI command for the Security Command Center API, you must always specify the location. There are a few ways to do this:

  * Use the `--location` flag.
  * If you provide the full path of the resource name, use a format that specifies a location, like `projects/123/sources/456/locations/LOCATION/findings/a1b2c3`.



The following example shows how to use the `--location` flag.

The [`gcloud scc findings list`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/findings/list) command lists an organization's findings in a specific location. 

Before using any of the command data below, make the following replacements: 

  * `ORGANIZATION_ID`: the numeric ID of the organization. 
  * `LOCATION`: a [supported location](https://docs.cloud.google.com/security-command-center/docs/regional-endpoints#locations-security-command-center) for the Security Command Center API 



Execute the [`gcloud scc findings list`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/findings/list) command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud scc findings list ORGANIZATION_ID --location=LOCATION

#### Windows (PowerShell)
    
    
    gcloud scc findings list ORGANIZATION_ID --location=LOCATION

#### Windows (cmd.exe)
    
    
    gcloud scc findings list ORGANIZATION_ID --location=LOCATION

The response contains a list of findings.

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    provider "google" {
      alias                              = "securitycenter_v2_endpoint_us"
      security_center_v2_custom_endpoint = "https://securitycenter.us.rep.googleapis.com/v2/"
    }

### Go

Use one of the following regional endpoints:

Security Command Center API
    `securitycenter.LOCATION.rep.googleapis.com:443`

Replace `LOCATION` with a supported location for the service.

The following code sample shows how to create a Security Command Center API client that uses a regional endpoint.
    
    
    import (
    	"context"
    	"fmt"
    
    	securitycenter "cloud.google.com/go/securitycenter/apiv2"
    	"google.golang.org/api/option"
    )
    
    // createClientWithEndpoint creates a Security Command Center client for a
    // regional endpoint.
    func createClientWithEndpoint(repLocation string) error {
    	// Assemble the regional endpoint URL using provided location.
    	repEndpoint := fmt.Sprintf("securitycenter.%s.rep.googleapis.com:443", repLocation)
    	// Instantiate client for regional endpoint. Use this client to access resources that
    	// are subject to data residency controls, and that are located in the region
    	// specified in repLocation.
    	repCtx := context.Background()
    	repClient, err := securitycenter.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_Client_NewClient)(repCtx, option.WithEndpoint(repEndpoint))
    	if err != nil {
    		return err
    	}
    	defer repClient.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_Client_Close)()
    
    	return nil
    }
    

### Java

Use one of the following regional endpoints:

Security Command Center API
    `securitycenter.LOCATION.rep.googleapis.com:443`

Replace `LOCATION` with a supported location for the service.

The following code sample shows how to create a Security Command Center API client that uses a regional endpoint.
    
    
    import com.google.cloud.securitycenter.v2.[SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html);
    import com.google.cloud.securitycenter.v2.[SecurityCenterSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterSettings.html);
    import java.io.IOException;
    
    public class CreateClientWithEndpoint {
    
      public static void main(String[] args) throws IOException {
        // TODO: Replace the value with the endpoint for the region in which your
        // Security Command Center data resides.
        String regionalEndpoint = "securitycenter.me-central2.rep.googleapis.com:443";
        [SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html) client = createClientWithEndpoint(regionalEndpoint);
        System.out.println("Client initiated with endpoint: " + client.[getSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html#com_google_cloud_securitycenter_v2_SecurityCenterClient_getSettings__)().getEndpoint());
      }
    
      // Creates Security Command Center client for a regional endpoint.
      public static [SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html) createClientWithEndpoint(String regionalEndpoint)
          throws java.io.IOException {
        [SecurityCenterSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterSettings.html) regionalSettings =
            [SecurityCenterSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterSettings.html).newBuilder().setEndpoint(regionalEndpoint).build();
        return [SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html).create(regionalSettings);
      }
    }
    

### Python

Use one of the following regional endpoints:

Security Command Center API
    `securitycenter.LOCATION.rep.googleapis.com`

Replace `LOCATION` with a supported location for the service.

The following code sample shows how to create a Security Command Center API client that uses a regional endpoint.
    
    
    from google.cloud import securitycenter_v2
    
    
    def create_client_with_endpoint(api_endpoint) -> securitycenter_v2.SecurityCenterClient:
        """
        Creates a Security Command Center client for a regional endpoint.
        Args:
            api_endpoint: the regional endpoint's hostname, like 'securitycenter.REGION.rep.googleapis.com'
        Returns:
            securitycenter_v2.SecurityCenterClient: returns a client for the regional endpoint
        """
        regional_client = securitycenter_v2.SecurityCenterClient(
            client_options={"api_endpoint": api_endpoint}
        )
        print(
            "Regional client initiated with endpoint: {}".format(
                regional_client.api_endpoint
            )
        )
        return regional_client
    
    

### REST

To access the following REST API resource types, you must use a regional service endpoint:

Security Command Center API
    

Endpoint: `https://securitycenter.LOCATION.rep.googleapis.com`

Replace `LOCATION` with a supported location for the service.

    

Resource types:

  * [`folders.locations.bigQueryExports`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/folders.locations.bigQueryExports)
  * [`folders.locations.findings`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/folders.locations.findings)
  * [`folders.locations.muteConfigs`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/folders.locations.muteConfigs)
  * [`folders.locations.notificationConfigs`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/folders.locations.notificationConfigs)
  * [`organizations.locations.bigQueryExports`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.locations.bigQueryExports)
  * [`organizations.locations.findings`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.locations.findings)
  * [`organizations.locations.muteConfigs`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.locations.muteConfigs)
  * [`organizations.locations.notificationConfigs`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.locations.notificationConfigs)
  * [`projects.locations.bigQueryExports`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/projects.locations.bigQueryExports)
  * [`projects.locations.findings`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/projects.locations.findings)
  * [`projects.locations.muteConfigs`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/projects.locations.muteConfigs)
  * [`projects.locations.notificationConfigs`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/projects.locations.notificationConfigs)



Replace `LOCATION` with a supported location for the service.

For all other resource types, you must use the default endpoint.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
