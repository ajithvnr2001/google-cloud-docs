---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/products/update/
title: gcloud beta apigee products update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:31:25.732177+00:00
---

# gcloud beta apigee products update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/products/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta apigee products update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta apigee products update - update an existing Apigee API product 
SYNOPSIS
    

`gcloud beta apigee products update` (`PRODUCT` : `--organization`=`ORGANIZATION`) [`--display-name`=`SET_DISPLAYNAME`] [`--all-apis` | `--add-api`=[`API`,…] `--remove-api`=[`API`,…]] [`--all-environments` | `--add-environment`=[`ENVIRONMENT`,…] `--remove-environment`=[`ENVIRONMENT`,…]] [`--all-resources` | `--add-resource`=[`RESOURCE`#…] `--remove-resource`=[`RESOURCE`#…]] [`--automatic-approval` | `--manual-approval`] [`--clear-attributes` | `--add-attribute`=[`NAME`=`VALUE`,…] `--remove-attribute`=[`NAME`,…]] [`--clear-description` | `--description`=`SET_DESCRIPTION`] [`--clear-oauth-scopes` | `--add-oauth-scope`=[`OAUTH-SCOPE`,…] `--remove-oauth-scope`=[`OAUTH-SCOPE`,…]] [`--clear-quota` | `--quota`=`QUOTA` `--quota-interval`=`QUOTA_INTERVAL` `--quota-unit`=`QUOTA_UNIT`] [`--internal-access` | `--private-access` | `--public-access`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Update an existing Apigee API product. 

`gcloud beta apigee products update` applies a set of modifications to an existing API product. 

To create a new API product, run: 
    
    
    [gcloud beta apigee products create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/products/create)

EXAMPLES
     To update the display name of the API product with the internal name ``my-prod``, run: 
    
    
    gcloud beta apigee products update my-prod --display-name="Example Project"

To update the description of the API product, run: 
    
    
    gcloud beta apigee products update my-prod --description="This API is famous for appearing in a YouTube video."

To remove the API product's description, run: 
    
    
    gcloud beta apigee products update my-prod --clear-description

To remove manual approval requirements from the API and change its access level to public, run: 
    
    
    gcloud beta apigee products update my-prod --public-access --automatic-approval

To impose a quota of 45 calls per minute per application on the API product, run: 
    
    
    gcloud beta apigee products update my-prod --quota=45 --quota-interval=1 --quota-unit=minute

To remove a quota on the API product and switch it to unlisted access with manual approval, run: 
    
    
    gcloud beta apigee products update my-prod --manual-approval --private-access --clear-quota

To set the API product's custom attribute ``foo`` to the value ``bar``, updating that attribute if it exists and creating it if it doesn't, and remove the attribute ``baz`` if it exists, run: 
    
    
    gcloud beta apigee products update my-prod --add-attribute="foo=bar" --remove-attribute=baz

To update the list of API proxies included in the API product, run: 
    
    
    gcloud beta apigee products update my-prod --add-api=NEW_ONE,NEW_TWO --remove-api=OLD_ONE,OLD_TWO

To switch the API product to including all ``test`` environment APIs no matter what API proxy or resource they expose, run: 
    
    
    gcloud beta apigee products update my-prod --add-environment=test --all-apis --all-resources

To update the list of API resources included in the API product, and output the updated API product as a JSON object, run: 
    
    
    gcloud beta apigee products update my-prod --add-resource="NEW_ONE#NEW_TWO" --remove-resource="OLD_ONE#OLD_TWO" --format=json

POSITIONAL ARGUMENTS
    

API product resource - API product to be updated. To get a list of available API products, run: 
    
    
    [gcloud beta apigee products list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/products/list)
    
    
    The arguments in this group can be used to specify the attributes of this resource.

This must be specified. 

`PRODUCT`
     ID of the API product or fully qualified identifier for the API product. 

To set the `product` attribute: 

  * provide the argument `PRODUCT` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--organization`=`ORGANIZATION`
     Apigee organization containing the API product. If unspecified, the Cloud Platform project's associated organization will be used. 

To set the `organization` attribute: 

  * provide the argument `PRODUCT` on the command line with a fully specified name; 
  * provide the argument `--organization` on the command line; 
  * set the property [project] or provide the argument [--project] on the command line, using a Cloud Platform project with an associated Apigee organization. 


FLAGS
    

`--display-name`=`SET_DISPLAYNAME`
     Name to be displayed in the UI or developer portal to developers registering for API access. 
At most one of these can be specified: 

`--all-apis`
     Include all deployed API proxies in the product, so long as they match the other parameters. 
Or at least one of these can be specified: 

API proxies to which this API product is bound. Only those API proxies will be accessible through the API product. 

The API proxy names must already be deployed to the bound environments, or creation of the API product will fail. To get a list of deployed API proxies, run: 
    
    
    [gcloud beta apigee deployments list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/deployments/list)

To deploy an API proxy, run: 
    
    
    [gcloud beta apigee apis deploy](https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/apis/deploy).

`--add-api`=[`API`,…]
     Adds a new API to the set of APIs. 
`--remove-api`=[`API`,…]
     Removes an existing API from the set of APIs. 
At most one of these can be specified: 

`--all-environments`
     Make all environments accessible through this API product. 
Or at least one of these can be specified: 

Environments to which the API product is bound. Requests to environments that are not listed are rejected, preventing developers from accessing those resources even if they can access the same API proxies in another environment. 

For example, this can be used to prevent applications with access to production APIs from accessing the alpha or beta versions of those APIs. 

To get a list of available environments, run: 
    
    
    [gcloud beta apigee environments list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/environments/list)

`--add-environment`=[`ENVIRONMENT`,…]
     Adds a new environment to the set of environments. 
`--remove-environment`=[`ENVIRONMENT`,…]
     Removes an existing environment from the set of environments. 
At most one of these can be specified: 

`--all-resources`
     Include all deployed API resources in the product, so long as they match the other parameters. 
Or at least one of these can be specified: 

API resources to be bundled in the API product. 

By default, the resource paths are mapped from the `proxy.pathsuffix` variable. 

The proxy path suffix is defined as the URI fragment following the ProxyEndpoint base path. For example, if ``/forecastrss`` is given as an element of this list, and the base path defined for the API proxy is `/weather`, then only requests to `/weather/forecastrss` are permitted by the API product. 

Proxy paths can use asterisks as wildcards; `/**` indicates that all sub-URIs are included, whereas a single asterisk indicates that only URIs one level down are included. 

By default, `/` supports the same resources as `/**` as well as the base path defined by the API proxy. 

For example, if the base path of the API proxy is `/v1/weatherapikey`, then the API product supports requests to `/v1/weatherapikey` and to any sub-URIs, such as `/v1/weatherapikey/forecastrss`, `/v1/weatherapikey/region/CA`, and so on. 

The API proxy resources must already be deployed to the bound environments, or creation of the API product will fail. 

`--add-resource`=[`RESOURCE`#…]
     Adds a new resource to the set of resources. 
`--remove-resource`=[`RESOURCE`#…]
     Removes an existing resource from the set of resources. 
At most one of these can be specified: 

`--automatic-approval`
     Allow developers to generate approved consumer keys without waiting for approval. 
`--manual-approval`
     Require manual approval of developer requests to access this API product before their consumer keys can be used. 
At most one of these can be specified: 

`--clear-attributes`
     Removes all attributes. 
Or at least one of these can be specified: 

Key-value attribute pairs that may be used to extend the default API product profile with customer-specific metadata. Up to 17 attributes can be specified. 
`--add-attribute`=[`NAME`=`VALUE`,…]
     Adds a new attribute to the set of attributes. 
`--remove-attribute`=[`NAME`,…]
     Removes an existing attribute from the set of attributes. 
At most one of these can be specified: 

`--clear-description`
     Remove the API product's description. 
`--description`=`SET_DESCRIPTION`
     Overview of the API product. Include key information about the API product that is not captured by other fields. 
At most one of these can be specified: 

`--clear-oauth-scopes`
     Removes all OAuth scopes. 
Or at least one of these can be specified: 

Comma-separated list of OAuth scopes that are validated at runtime. Apigee validates that the scopes in any access token presented match the scopes defined in the OAuth policy assoicated with the API product. 
`--add-oauth-scope`=[`OAUTH-SCOPE`,…]
     Adds a new OAuth scope to the set of OAuth scopes. 
`--remove-oauth-scope`=[`OAUTH-SCOPE`,…]
     Removes an existing OAuth scope from the set of OAuth scopes. 
At most one of these can be specified: 

`--clear-quota`
     Remove any quota currently imposed on the API product. 
Or at least one of these can be specified: 

To impose a quota limit on calls to the API product, specify all of the following: 
`--quota`=`QUOTA`
     Number of request messages permitted per app by this API product for the specified `--quota-interval` and `--quota-unit`. 

For example, `--quota=50`, `--quota-interval=12`, and `--quota-unit=hour` means 50 requests are allowed every 12 hours. 

`--quota-interval`=`QUOTA_INTERVAL`
     Time interval over which the number of request messages is calculated. 
`--quota-unit`=`QUOTA_UNIT`
     Time unit for `--quota-interval`. `QUOTA_UNIT` must be one of: `minute`, `hour`, `day`, `month`. 
At most one of these can be specified: 

`--internal-access`
     Prevent external access to this API product. 
`--private-access`
     Hide this API product in the developer portal but make it accessible by external developers. 
`--public-access`
     Make this API product visible to developers in the Apigee developer portal. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud apigee products update](https://docs.cloud.google.com/sdk/gcloud/reference/apigee/products/update)
    
    
    [gcloud alpha apigee products update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
