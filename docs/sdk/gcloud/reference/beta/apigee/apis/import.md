---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/apis/import/
title: gcloud beta apigee apis import \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:58:53.669748+00:00
---

# gcloud beta apigee apis import  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/apis/import/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta apigee apis import Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta apigee apis import - import an Apigee API proxy from local files 
SYNOPSIS
    

`gcloud beta apigee apis import` (`API` : `--organization`=`ORGANIZATION`) (`--from-bundle`=`BUNDLE_PATH` | `--from-template`=`TEMPLATE_PATH`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Import an Apigee API proxy from local files. 

`gcloud beta apigee apis import` uploads local files describing an API proxy to Apigee. If an API proxy with the given name already exists, a new revision is created; otherwise, a new API proxy is created. 

The API proxy source is provided in exactly one of two formats. 

Use `--from-bundle` to upload a standard Apigee API proxy bundle ZIP, which stores the proxy configuration under an `apiproxy/` directory. 

Use `--from-template` to build the API proxy from an Apigee Feature Template: a YAML file that composes one or more reusable feature files into an API proxy. The template is compiled into a bundle locally before being uploaded. 

When using `--from-template`, any feature files referenced by the template must reside in the same directory as the template file. 

For an overview of defining an API proxy in YAML, see [Configuring a proxy with YAML](https://cloud.google.com/apigee/docs/api-platform/fundamentals/configure-proxy-with-yaml). For the complete set of fields supported in templates, features, and proxies, see the [API proxy YAML configuration reference](https://cloud.google.com/apigee/docs/api-platform/reference/api-proxy-yaml-configuration-reference). 

To use this command, the active Google Cloud project must have an associated Apigee organization, or an organization must be specified with `--organization` or by providing the fully qualified name (FQN) of the API proxy as the API proxy name (for example, ``organizations/my-org/apis/helloworld``). 

EXAMPLES
     To import an API proxy named ``helloworld`` from a local bundle ZIP, given that the matching Google Cloud project has been set in gcloud settings, run: 
    
    
    gcloud beta apigee apis import helloworld --from-bundle=./helloworld.zip

To import an API proxy named ``helloworld`` from an Apigee Feature Template, run: 
    
    
    gcloud beta apigee apis import helloworld --from-template=./helloworld.yaml

To import that API proxy into an organization named ``my-org``, run: 
    
    
    gcloud beta apigee apis import helloworld --organization=my-org --from-template=./helloworld.yaml

Alternatively, the organization can be specified by providing the fully qualified name of the API proxy: 
    
    
    gcloud beta apigee apis import organizations/my-org/apis/helloworld --from-bundle=./helloworld.zip

To import that API proxy and print the resulting revision as a JSON object, run: 
    
    
    gcloud beta apigee apis import helloworld --from-template=./helloworld.yaml --format=json

POSITIONAL ARGUMENTS
    

API proxy resource - API proxy to import or update. If an API proxy with this name already exists in the organization, a new revision is created. The arguments in this group can be used to specify the attributes of this resource. 

This must be specified. 

`API`
     ID of the API proxy or fully qualified identifier for the API proxy. 

To set the `api` attribute: 

  * provide the argument `API` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--organization`=`ORGANIZATION`
     Apigee organization containing the API proxy. If unspecified, the Cloud Platform project's associated organization will be used. 

To set the `organization` attribute: 

  * provide the argument `API` on the command line with a fully specified name; 
  * provide the argument `--organization` on the command line; 
  * set the property [project] or provide the argument [--project] on the command line, using a Cloud Platform project with an associated Apigee organization. 


REQUIRED FLAGS
    

Source from which to import the API proxy. 

Exactly one of these must be specified: 

`--from-bundle`=`BUNDLE_PATH`
     Path to an Apigee API proxy bundle ZIP file to import the API proxy from. 

The ZIP file must contain the API proxy configuration under an `apiproxy/` directory. 

`--from-template`=`TEMPLATE_PATH`
     Path to an Apigee Feature Template YAML file to import the API proxy from. 

The template composes one or more reusable feature files into an API proxy. Any feature files referenced by the template must reside in the same directory as the template file. 

The template is compiled into an API proxy bundle locally before being uploaded to Apigee. 

For an overview of defining an API proxy in YAML, see [Configuring a proxy with YAML](https://cloud.google.com/apigee/docs/api-platform/fundamentals/configure-proxy-with-yaml). For the complete set of fields supported in templates, features, and proxies, see the [API proxy YAML configuration reference](https://cloud.google.com/apigee/docs/api-platform/reference/api-proxy-yaml-configuration-reference). 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

GUIDANCE
    
Prerequisites
     Requires permission to create API proxies in the target Apigee organization (for example, `roles/apigee.apiAdmin`), and an active Google Cloud project associated with that organization. 
Working with templates
     When using `--from-template`, keep the template file and every feature file it references in the same directory. Feature paths are resolved relative to the template file, so a template in one directory cannot reference feature files in another. 
After importing
     Each import creates a new API proxy revision rather than overwriting an existing one. Deploy the new revision to an environment with `[gcloud apigee apis deploy](https://docs.cloud.google.com/sdk/gcloud/reference/apigee/apis/deploy)`. 
Troubleshooting
     If the command cannot find an Apigee organization for the active project, that project has no associated Apigee organization. Pass `--organization`, set the active project to one that has an Apigee organization, or give the full API proxy name (for example, ``organizations/my-org/apis/helloworld``). 

If the command fails with a permissions error, the account cannot create API proxies. Grant a role such as `roles/apigee.apiAdmin` on the organization. 

If `--from-template` cannot read a feature file, the feature file is not in the template directory. Keep the template and its feature files in the same directory. Feature paths are resolved relative to the template file. 

If `--from-template` fails with "Failed to parse YAML" or a schema error (for example, "missing required top-level 'gateway' field"), the template or a feature file is not valid. Set the required `gateway` and `schemaVersion` fields to supported values (for example, `gateway: apigee` and `schemaVersion: 1.0.0`), and remove fields that are not in the schema. 

If `--from-bundle` reports an invalid bundle, the ZIP does not contain the proxy configuration under an `apiproxy/` directory. Repackage the ZIP so that the `apiproxy/` directory is at the root. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud apigee apis import](https://docs.cloud.google.com/sdk/gcloud/reference/apigee/apis/import)
    
    
    [gcloud alpha apigee apis import](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/apis/import)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
