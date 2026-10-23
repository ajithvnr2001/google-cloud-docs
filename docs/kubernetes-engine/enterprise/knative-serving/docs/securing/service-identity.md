---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/securing/service-identity/
title: Using OAuth2 access tokens \u00a0|\u00a0 Knative serving \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:42.073801+00:00
---

# Using OAuth2 access tokens  |  Knative serving  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/securing/service-identity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Knative serving ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview)



Send feedback 

#  Using OAuth2 access tokens Stay organized with collections  Save and categorize content based on your preferences. 

You can use access tokens to authenticate for a short period of time with Google Cloud APIs. If access tokens are not required, you should use a [service account](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving//docs/securing/service-accounts) to authenticate your Knative serving services.

## Fetching access tokens

When your code runs on Knative serving it can use the [Compute Metadata Server](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata) to fetch access tokens. You cannot query the metadata server directly from your local computer.

### Access tokens

By default, access tokens have the `cloud-platform` scope, which allows access to all Google Cloud APIs, assuming Identity and Access Management also allows access. In order to access other Google or Google Cloud APIs, you will need to fetch an access token with the appropriate scope.

You can use the Compute Metadata Server to [fetch access tokens](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#applications).

If you need an access token with a specific scope, you can generate one as follows:
    
    
    curl "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token?scopes=[SCOPES]" \
      -H "Metadata-Flavor: Google"

Where `SCOPES` is a comma separated list of OAuth scopes requested, for example: `https://www.googleapis.com/auth/drive,https://www.googleapis.com/auth/spreadsheets`.

Consult the full list of [Google OAuth scopes](https://developers.google.com/identity/protocols/googlescopes) to find which scopes you need.

**Note:** the `?scopes=` query parameter is only available on App Engine, Cloud Run functions, Cloud Run, and Knative serving.

## Next steps

Learn how to [manage access](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/securing/managing-access) to your services.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
