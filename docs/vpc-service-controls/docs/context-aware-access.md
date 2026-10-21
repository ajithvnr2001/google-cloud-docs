---
url: https://docs.cloud.google.com/vpc-service-controls/docs/context-aware-access/
title: Context-aware access with ingress rules \u00a0|\u00a0 VPC Service Controls \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:35.585955+00:00
---

# Context-aware access with ingress rules  |  VPC Service Controls  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc-service-controls/docs/context-aware-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ VPC Service Controls ](https://docs.cloud.google.com/vpc-service-controls/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc-service-controls/docs/overview)



Send feedback 

#  Context-aware access with ingress rules Stay organized with collections  Save and categorize content based on your preferences. 

Context-aware access ingress rule setups allow access to resources based on client attributes such as network origin (IP address or VPC network), identity type (service account or user), identity, and device data. Access is defined by ingress rules.

For an overview of ingress and egress rules, see [Ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules).

For instructions on how to apply ingress and egress rule policies, see [Configuring ingress and egress policies](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies).

## Configuration examples of context-aware access use cases

This section contains the following examples of context-aware access:

  1. [Allow human users to access BigQuery from the internet and only specific service accounts access from a specified IP range](https://docs.cloud.google.com/vpc-service-controls/docs/context-aware-access#allow_human_users_to_access_bigquery_from_the_internet_and_only_specific_service_accounts_access_from_a_specified_ip_range)
  2. [Allow employees to query BigQuery from trusted devices over the internet and a specific service account to privately load data to a Cloud Storage bucket (source data)](https://docs.cloud.google.com/vpc-service-controls/docs/context-aware-access#allow_employees_to_query_bigquery_from_trusted_devices_over_the_internet_and_a_specific_service_account_to_privately_load_data_to_a_cloud_storage_bucket_source_data)



### Allow human users to access BigQuery from the internet and only specific service accounts access from a specified IP range

![Ingress from recognized users and networks](https://docs.cloud.google.com/static/vpc-service-controls/images/directional_policy_bigquery_service_account_ingress.png)

Assume that you have defined the following perimeter, found by [listing the perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#list-and-describe) with gcloud:
    
    
    name: accessPolicies/222/servicePerimeters/Example
    status:
      resources:
      - projects/111
      restrictedServices:
      - bigquery.googleapis.com
      - storage.googleapis.com
      vpcAccessibleServices:
        enableRestriction: true
        allowedServices:
        - RESTRICTED_SERVICES
    title: Example
    

We also assume that an access level called CorpDatacenters has been defined. CorpDatacenters, in this example, is a whitelisted range of IPs of corporate data centers that access from which service accounts are allowed.

Here is the directional policy to allow all humans and a specific set of service accounts, limited to a particular set of IPs (defined by an access level):
    
    
    echo """
    - ingressFrom:
        identities:
        - serviceAccount:my-sa@my-project.iam.gserviceaccount.com
        sources:
        - accessLevel: accessPolicies/222/accessLevels/CorpDatacenters
      ingressTo:
        operations:
        - serviceName: bigquery.googleapis.com
          methodSelectors:
          - method: \"*\"
        resources:
        - \"*\"
    - ingressFrom:
        identityType: ANY_USER_ACCOUNT
        sources:
        - accessLevel: \"*\"
      ingressTo:
        operations:
        - serviceName: bigquery.googleapis.com
          methodSelectors:
          - method: \"*\"
        resources:
        - \"*\"
    """ > ingress.yaml
    

Apply the ingress rules by running the following command:
    
    
    gcloud access-context-manager perimeters update Example --set-ingress-policies=ingress.yaml
    

### Allow employees to query BigQuery and privately load data to a Cloud Storage bucket

![Ingress from recognized devices and networks](https://docs.cloud.google.com/static/vpc-service-controls/images/bigquery-cloud-storage-service-account-ingress.png)

Assume that you have defined the following perimeter, found by [listing the perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#list-and-describe) with gcloud:
    
    
    name: accessPolicies/222/servicePerimeters/Example
    status:
      resources:
      - projects/111
      restrictedServices:
      - bigquery.googleapis.com
      - storage.googleapis.com
      vpcAccessibleServices:
        enableRestriction: true
        allowedServices:
        - RESTRICTED_SERVICES
    title: Example
    

Here is the directional policy to allow humans to access BigQuery views from trusted devices (using a Access Level) and a specific service account private to access Cloud Storage from an authorized VPC network:
    
    
    echo """
    - ingressFrom:
        identities:
        - serviceAccount:my-sa@my-project.iam.gserviceaccount.com
        sources:
        - resource: projects/111
      ingressTo:
        operations:
        - serviceName: storage.googleapis.com
          methodSelectors:
          - method: google.storage.Write
          - method: google.storage.objects.create
        resources:
        - \"*\"
    
    - ingressFrom:
        identityType: ANY_SERVICE_ACCOUNT
        sources:
          - resource: //compute.googleapis.com/projects/my-network-project/global/networks/top-tier-vpc-network
      ingressTo:
        operations:
        - serviceName: storage.googleapis.com
          methodSelectors:
          - method: google.storage.Write
          - method: google.storage.objects.create
        resources:
        - \"*\"
    
    - ingressFrom:
        identityType: ANY_USER_ACCOUNT
        sources:
        - accessLevel: accessPolicies/222/accessLevels/TrustedDevices
      ingressTo:
        operations:
        - serviceName: bigquery.googleapis.com
          methodSelectors:
          - permission: bigquery.tables.getData
        resources:
        - \"*\"
    """ > ingress.yaml
    

Apply the ingress rules by running the following command:
    
    
    gcloud access-context-manager perimeters update Example --set-ingress-policies=ingress.yaml
    

For information about VPC networks limitations when you use VPC networks in service perimeters, see [VPC network limitations](https://docs.cloud.google.com/vpc-service-controls/docs/vpc-perimeters-management#limitations).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
