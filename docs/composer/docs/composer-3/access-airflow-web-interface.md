---
url: https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-web-interface/
title: Access the Airflow web interface \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:27:40.449010+00:00
---

# Access the Airflow web interface  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-web-interface/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 3 Guides ](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview)



Send feedback 

#  Access the Airflow web interface Stay organized with collections  Save and categorize content based on your preferences. 

**Managed Airflow (Gen 3)** | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/access-airflow-web-interface "View this page for Managed Airflow \(Gen 2\)") | [Managed Airflow (Legacy Gen 1)](https://docs.cloud.google.com/composer/docs/composer-1/access-airflow-web-interface "View this page for Managed Airflow \(Legacy Gen 1\)")

Apache Airflow includes a web user interface called [Airflow UI](https://airflow.apache.org/docs/apache-airflow/stable/ui.html), which you can use to manage Airflow DAGs, view DAG run logs, monitor Airflow, and perform administrative actions.

## About the Airflow web server

Each Managed Airflow environment has a web server that runs the Airflow UI. The web server is a part of [Managed Airflow environment architecture](https://docs.cloud.google.com/composer/docs/composer-3/environment-architecture).

## Before you begin

  * You must have a role that can view Managed Airflow environments. For more information, see [Access control](https://docs.cloud.google.com/composer/docs/composer-3/access-control).

  * During the environment creation, Managed Airflow configures the URL for the web server that runs the Airflow UI. The URL is non-customizable.



  * Managed Airflow (Gen 3) supports the [Airflow UI Access Control](https://docs.cloud.google.com/composer/docs/composer-3/airflow-rbac) (Airflow Role-Based Access Control) feature for the Airflow UI.

  * If the **API Controls** > **Unconfigured third-party apps** > **Don't allow users to access any third-party apps** option is enabled in Google Workspace and the Apache Airflow in Managed Airflow app is not explicitly allowed, then users are not able to access the Airflow UI unless they explicitly allow the application. To allow access, perform steps provided in [Allow access to Airflow UI in Google Workspace](https://docs.cloud.google.com/composer/docs/composer-3/access-control#airflow-ui-access-google-workspace).

  * If Chrome Enterprise Premium [Context-Aware Access bindings](https://docs.cloud.google.com/chrome-enterprise-premium/docs/securing-console-and-apis) are used with access levels that rely on device attributes, and the Apache Airflow in Managed Airflow app is not exempted, then it's not possible to access the Airflow UI because of a login loop. To allow access, perform steps provided in [Allow access to Airflow UI in Context-Aware Access bindings](https://docs.cloud.google.com/composer/docs/composer-3/access-control#airflow-ui-access-caa-bindings).

  * If [ingress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) are configured in a VPC Service Controls perimeter that protects the project, and the ingress rule that allows access to the Managed Airflow service uses `ANY_SERVICE_ACCOUNT` or `ANY_USER_ACCOUNT` identity type, then users can't access the Airflow UI, ending up in a login loop. For more information about addressing this scenario, see [Allow access to Airflow UI in VPC Service Controls ingress rules](https://docs.cloud.google.com/composer/docs/composer-3/access-control#airflow-ui-access-vpcsc-ingress-rules).

  * Managed Airflow doesn't support using [third-party identities](https://docs.cloud.google.com/composer/docs/composer-3/access-environments-with-workforce-identity-federation) in ingress and egress rules to allow Apache Airflow UI operations. However, you can use the `ANY_IDENTITY` identity type in ingress and egress rules to allow access to all identities, including third-party identities. For more information about the `ANY_IDENTITY` identity type, see [Ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules).




## Access the Airflow UI

In Managed Airflow (Gen 3), the Airflow web server runs [in the tenant project of your environment](https://docs.cloud.google.com/composer/docs/composer-3/environment-architecture). The web server is deployed to the `composer.googleusercontent.com` domain and provides access to the Airflow UI.

Managed Airflow (Gen 3) provides access to the interface based on user identities and IAM policy bindings defined for users.

### Access the Airflow UI from the Google Cloud console

To access the Airflow UI from the Google Cloud console:

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the **Airflow webserver** column, follow the **Airflow** link for your environment.

  3. Sign in with a Google Account that has the appropriate permissions.




### Obtain the Airflow UI URL with Google Cloud CLI

You can access the Airflow UI from any web browser. To get the URL for the Airflow UI, run the following command in Google Cloud CLI:
    
    
    gcloud composer environments describe ENVIRONMENT_NAME \
      --location LOCATION
    

Replace the following:

  * `ENVIRONMENT_NAME`: the name of your environment.
  * `LOCATION`: the region where the environment is located.



The Google Cloud CLI command shows the properties of a Managed Airflow environment, including the URLs for the Airflow UI. The URLs are listed as `airflowUri` and `airflowByoidUri`:

  * The `airflowUri` URL address is used by Google Accounts.
  * The `airflowByoidUri` URL address is used by external identities if you [configure Workforce identity federation](https://docs.cloud.google.com/composer/docs/composer-3/access-environments-with-workforce-identity-federation) in your project.


    
    
    config:
      airflowUri: https://example-dot-us-central1.composer.googleusercontent.com
      airflowByoidUri: https://example-dot-us-central1.composer.byoid.googleusercontent.com
    

## Restart the web server

When debugging or troubleshooting Managed Airflow environments, some issues may be resolved by restarting the Airflow web server. You can restart the web server using the [restartWebServer API](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments/restartWebServer) or the `restart-web-server` command in Google Cloud CLI:
    
    
    gcloud composer environments restart-web-server ENVIRONMENT_NAME \
      --location=LOCATION
    

Replace the following:

  * `ENVIRONMENT_NAME`: the name of your environment.
  * `LOCATION`: the region where the environment is located.



## Configure web server network access

The Airflow web server access parameters don't depend on your environment's networking configuration. Instead, you configure web server access separately. For example, a Private IP environment can still have the Airflow UI accessible from the internet.

**Note:** The Airflow web server of your environment is always protected by IAM, regardless of the IP ranges that are allowed to access it.

It's not possible to configure the allowed IP ranges to be private IP addresses.

**Important:** In some cases, changes to the web server access parameters can take up to 10 minutes to propagate.

###  Console 

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Go to the **Environment configuration** tab.

  4. In the **Network configuration** section, find the **Web server access control** item and click **Edit**.

  5. In the **Web server network access control** dialog:

     * To provide access to the Airflow web server from all IP addresses, select **Allow access from all IP addresses**.

     * To restrict access only to specific IP ranges, select **Allow access only from specific IP addresses**. In the **IP range** field, specify an IP range in the CIDR notation. In the **Description** field, specify an optional description for this range. If you want to specify more than one range, click **Add IP range**.

     * To forbid access for all IP addresses, select **Allow access only from specific IP addresses** and click **Delete item** next to the empty range entry.




###  gcloud 

When you update an environment, the following arguments control web server access parameters:

  * `--web-server-allow-all` provides access to Airflow from all IP addresses. This is the default option.

  * `--update-web-server-allow-ip` restricts access only to specific source IP ranges. To specify several IP ranges, use this argument multiple times.

  * `--web-server-deny-all` forbids access for all IP addresses.



    
    
    gcloud composer environments update ENVIRONMENT_NAME \
        --location LOCATION \
        --update-web-server-allow-ip ip_range=WS_IP_RANGE,description=WS_RANGE_DESCRIPTION
    

Replace the following:

  * `ENVIRONMENT_NAME`: the name of your environment.
  * `LOCATION`: the region where the environment is located.
  * `WS_IP_RANGE`: the IP range, in the CIDR notation, that can access the Airflow UI.
  * `WS_RANGE_DESCRIPTION`: the description of the IP range.



Example:
    
    
    gcloud composer environments update example-environment \
        --location us-central1 \
        --update-web-server-allow-ip ip_range=192.0.2.0/24,description="example range" \
        --update-web-server-allow-ip ip_range=192.0.4.0/24,description="example range 2"
    

###  API 

  1. Construct an [`environments.patch`][api-patch] API request.

  2. In this request:

     1. In the `updateMask` parameter, specify the `config.webServerNetworkAccessControl` mask.

     2. In the request body, specify how Airflow task logs must be saved:

        * To provide access to Airflow from all IP addresses, specify an empty `config` element (the `webServerNetworkAccessControl` element must not be present).

        * To restrict access only to specific IP ranges, specify one or more ranges in `allowedIpRanges`.

        * To forbid access for all IP addresses, specify an empty `webServerNetworkAccessControl` element. The `webServerNetworkAccessControl` element must be present, but must not contain an `allowedIpRanges` element.



    
    
    {
      "config": {
        "webServerNetworkAccessControl": {
          "allowedIpRanges": [
            {
              "value": "WS_IP_RANGE",
              "description": "WS_RANGE_DESCRIPTION"
            }
          ]
        }
      }
    }
    

Replace the following:

  * `WS_IP_RANGE`: the IP range, in the CIDR notation, that can access the Airflow UI.
  * `WS_RANGE_DESCRIPTION`: the description of the IP range.



Example:
    
    
    // PATCH https://composer.googleapis.com/v1/projects/example-project/
    // locations/us-central1/environments/example-environment?updateMask=
    // config.webServerNetworkAccessControl
    
    {
      "config": {
        "webServerNetworkAccessControl": {
          "allowedIpRanges": [
            {
              "value": "192.0.2.0/24",
              "description": "example range"
            },
            {
              "value": "192.0.4.0/24",
              "description": "example range 2"
            }
          ]
        }
      }
    }
    

###  Terraform 

In the `allowed_ip_range` block, in the `web_server_network_access_control` specify IP ranges that can access web server.
    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "ENVIRONMENT_NAME"
      region = "LOCATION"
    
      config {
    
        web_server_network_access_control {
    
          allowed_ip_range {
            value = "WS_IP_RANGE"
            description = "WS_RANGE_DESCRIPTION"
          }
    
        }
    
      }
    }
    

Replace the following:

  * `WS_IP_RANGE`: the IP range, in the CIDR notation, that can access the Airflow UI.
  * `WS_RANGE_DESCRIPTION`: the description of the IP range.



Example:
    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "example-environment"
      region = "us-central1"
    
      config {
    
        web_server_network_access_control {
          allowed_ip_range {
            value = "192.0.2.0/24"
            description = "example range"
          },
          allowed_ip_range {
            value = "192.0.4.0/24"
            description = "example range 2"
          }
    
        }
    }
    

## What's next

  * [Airflow UI Access Control](https://docs.cloud.google.com/composer/docs/composer-3/airflow-rbac)
  * [Troubleshooting Airflow web server issues](https://docs.cloud.google.com/composer/docs/composer-3/troubleshooting-web-server)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
