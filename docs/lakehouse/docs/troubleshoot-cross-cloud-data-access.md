---
url: https://docs.cloud.google.com/lakehouse/docs/troubleshoot-cross-cloud-data-access/
title: Troubleshoot cross-cloud data access \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:25:56.047714+00:00
---

# Troubleshoot cross-cloud data access  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/troubleshoot-cross-cloud-data-access/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Troubleshoot cross-cloud data access Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** For support during the preview, send an email to [biglake-help@google.com](mailto:biglake-help@google.com).

This document shows you how to resolve common issues when using cross-cloud data access capability of borderless Lakehouse.

## Data and resources are stale or not updating

Lakehouse federated catalogs synchronize metadata from a remote cloud based on a refresh interval. A catalog's background metadata refresh may take longer the more resources there are (shares, schemas, namespaces, tables). If the previous refresh overruns, the current refresh will be skipped, but the next refresh will be rescheduled at the following interval.

If queried data appears stale, the catalog's background metadata refresh may be overrunning or failing. Remote cloud resources are also subject to the same behavior. If you delete a resource in the remote cloud, then it will only be deleted from Lakehouse on the next successful background metadata refresh.

Check the background metadata refresh status on a federated catalog in the **Lakehouse** Google Cloud console page, or by running the gcloud CLI:

[Go to Lakehouse](https://console.cloud.google.com/biglake)
    
    
    gcloud alpha biglake iceberg catalogs describe FEDERATED_CATALOG_NAME \
        --project="PROJECT_ID"
    
    gcloud alpha biglake delta-sharing catalogs describe FEDERATED_CATALOG_NAME \
        --project="PROJECT_ID"

## Connectivity or routing issues

If you encounter connectivity or routing issues when you use a private interconnect, verify the following:

  * **Verify route propagation:** Check the Cloud Router in Google Cloud to verify that it has learned the AWS VPC prefixes. Check your AWS route tables to verify that they have routes back to your Google Cloud VPC.
  * **Check ILB health:** In the Google Cloud console, go to **Network Services > Load balancing**. Check whether the backends (NEGs) for your ILB backend service are healthy. If they aren't, verify network connectivity and AWS Security Group rules.
  * **Test connectivity from Google Cloud:** Launch a test VM instance in the same Google Cloud VPC and subnet as the ILB or Service Directory endpoint and try to connect to the AWS ENI IP addresses on port `443` (for example, by using `curl` or `telnet`).
  * **Service Directory resolution:** Verify that the catalog's service account has permissions to resolve Service Directory endpoints (`roles/servicedirectory.viewer`, `roles/servicedirectory.pscAuthorizedService`).
  * **Security Groups and firewall rules:** Verify that Google Cloud firewall rules and AWS Security Groups allow traffic on TCP port `443` between the relevant IP ranges.



## Snowflake catalog refresh fails with Code 16 (Unauthenticated)

If the background metadata refresh for a Snowflake Horizon Catalog fails with status `Code 16` (`UNAUTHENTICATED`), verify the following:

  * **Secret payload formatting:** Ensure that the secret token in Secret Manager contains the required JSON structure (`{"client_secret": "<var>SNOWFLAKE_PAT_TOKEN</var>", "scope": "session:role:<var>SNOWFLAKE_ROLE</var>"}`) rather than the raw Personal Access Token (PAT) string.
  * **Token expiration and permissions:** Ensure the Snowflake PAT is valid and the associated user and role have sufficient privileges to access the target catalog and databases.
  * **Network policy:** If a Snowflake network policy is configured, ensure that Google's egress IP address ranges from [`goog.json`](https://www.gstatic.com/ipranges/goog.json) are allowlisted.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
