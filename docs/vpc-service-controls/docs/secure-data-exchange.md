---
url: https://docs.cloud.google.com/vpc-service-controls/docs/secure-data-exchange/
title: Secure data exchange with ingress and egress rules \u00a0|\u00a0 VPC Service Controls \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:14.433585+00:00
---

# Secure data exchange with ingress and egress rules  |  VPC Service Controls  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc-service-controls/docs/secure-data-exchange/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ VPC Service Controls ](https://docs.cloud.google.com/vpc-service-controls/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc-service-controls/docs/overview)



Send feedback 

#  Secure data exchange with ingress and egress rules Stay organized with collections  Save and categorize content based on your preferences. 

This document describes common use cases for secure data exchange and example configurations to allow access between clients and resources separated by service perimeters.

For an overview of ingress and egress rules, see [Ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules).

For instructions about how to configure ingress and egress rule policies, see [Configuring ingress and egress policies](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies).

## Configuration examples of secure data exchange use cases

This section contains example use cases on exchanging data securely across service perimeters.

  * [Access a Google Cloud resource outside the perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/secure-data-exchange#access-google-cloud-resource-outside-the-perimeter)
  * [Share data by using Pub/Sub between two organizations that use VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/secure-data-exchange#share-data-using-pubsub-between-two-organizations)
  * [Share anonymized PHI data with partner organization](https://docs.cloud.google.com/vpc-service-controls/docs/secure-data-exchange#share-anonymized-data-with-partner-org)
  * [Grant access to a third-party Compute Engine disk image](https://docs.cloud.google.com/vpc-service-controls/docs/secure-data-exchange#grant-access-third-party-compute-engine-disk-image)
  * [Read a BigQuery dataset by allowing private access from a VPC network outside the perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/secure-data-exchange#read-bigquery-dataset-by-allowing-private-access-outside-perimeter)
  * [Load into a Cloud Storage bucket (write) by allowing private access from a VPC network outside the perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/secure-data-exchange#load-cloud-storage-bucket-by-allowing-private-access-from-outside-perimeter)
  * [Share logs in a separate perimeter by allowing projects from multiple perimeters to share logs](https://docs.cloud.google.com/vpc-service-controls/docs/secure-data-exchange#share-logs-in-separate-perimeter-allow-projects-from-multiple-perimeters)



### Access a Google Cloud resource outside the perimeter

The following diagram shows a Compute Engine resource inside a service perimeter that requires access to a Cloud Storage resource, which is outside the perimeter:

![Egress from one perimeter](https://docs.cloud.google.com/static/vpc-service-controls/images/directional_policy_egress_to_resource_outside_perimeter.png)

Assume that you have defined the following perimeter:
    
    
    name: accessPolicies/222/servicePerimeters/Example
    status:
      resources:
      - projects/111
      restrictedServices:
      - bigquery.googleapis.com
      - containerregistry.googleapis.com
      - storage.googleapis.com
    title: Example
    

You need to grant read access to a Cloud Storage bucket in `project 999`, which is in a different organization. You then define the following egress rule in a file and save the file as `gcs.yaml`:
    
    
    echo """
    - egressTo:
        operations:
          - serviceName: storage.googleapis.com
            methodSelectors:
            - method: google.storage.objects.get
        resources:
        - projects/999
      egressFrom:
        identityType: ANY_IDENTITY
    """ > gcs.yaml
    

Apply the egress rule by running the following command:
    
    
    gcloud beta access-context-manager perimeters update Example --set-egress-policies=gcs.yaml
    

For more information about the `gcloud access-context-manager perimeters update` command, see [gcloud access-context-manager perimeters update](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/update).

### Share data by using Pub/Sub between two organizations that use VPC Service Controls

The following diagram shows two organizations, `Org1` and `Org2`, which use VPC Service Controls and share data by using a Pub/Sub topic:

![Egress from one perimeter and ingress to another perimeter](https://docs.cloud.google.com/static/vpc-service-controls/images/directional_policy_pubsub_egress_and_ingress.png)

Assume that you have defined the following perimeters:
    
    
    # Org 1 Perimeter Definition
    name: accessPolicies/222/servicePerimeters/Example1
    status:
      resources:
      - projects/111
      restrictedServices:
      - pubsub.googleapis.com
    title: Example1
    
    
    
    
    # Org 2 Perimeter Definition
    name: accessPolicies/333/servicePerimeters/Example2
    status:
      resources:
      - projects/222
      restrictedServices:
      - pubsub.googleapis.com
    title: Example2
    

To enable data exchange, `Org1` must define the following egress rule that allows the subscription and save the file as `org1egress.yaml`:
    
    
    # Org1: Org1's perimeter must allow a Pub/Sub subscription to project 222.
    
    echo """
    - egressTo:
        operations:
        - serviceName: pubsub.googleapis.com
          methodSelectors:
          - method: Subscriber.CreateSubscription
        resources:
        - projects/222
      egressFrom:
        identityType: ANY_IDENTITY
    """ > org1egress.yaml
    
    

`Org2` must define a corresponding _ingress rule_ allowing the subscription and save the file as `org2ingress.yaml`.
    
    
    # Org 2: Org2's perimeter must allow a Pub/Sub subscription from network
    project 111 in Org1.
    
    echo """
    - ingressFrom:
        identityType: ANY_IDENTITY
        sources:
        - resource: projects/111
      ingressTo:
        operations:
        - serviceName: pubsub.googleapis.com
          methodSelectors:
          - method: Subscriber.CreateSubscription
        resources:
        - \"*\"
    """ > org2ingress.yaml
    

Apply the ingress and egress rules by running the following commands:
    
    
    gcloud beta access-context-manager perimeters update Example2 1--set-egress-policies=org1egress.yaml
    
    
    
    gcloud beta access-context-manager perimeters update Example1 1--set-ingress-policies=org2ingress.yaml
    

### Share anonymized PHI data with a partner organization

The following diagram shows a perimeter around a Protected Health Information (PHI) data segment, a second perimeter around an anonymized data segment, and a separate partner organization. The PHI segment is able to manipulate the data in the anonymized data segment and the data from the anonymized data segment is shared with the partner organization.

![Ingress into perimeter and egress out of perimeter](https://docs.cloud.google.com/static/vpc-service-controls/images/directional_policy_anonymized_data_ingress_egress.png)

You want to define ingress and egress rules that enable sharing anonymized data with the partner organization and allow your PHI segment to manipulate the data in the anonymized data segment.

Assume that you have defined the following perimeters:
    
    
    # PhiPerimeter
    name: accessPolicies/222/servicePerimeters/PhiPerimeter
    status:
      resources:
      - projects/111
      restrictedServices:
      - storage.googleapis.com
      - bigquery.googleapis.com
      vpcAccessibleServices:
        enableRestriction: true
        allowedServices:
        - RESTRICTED_SERVICES
    title: PhiPerimeter
    
    
    
    # AnonPerimeter
    name: accessPolicies/222/servicePerimeters/AnonPerimeter
    status:
      resources:
      - projects/222
      restrictedServices:
      - storage.googleapis.com
      vpcAccessibleServices:
        enableRestriction: true
        allowedServices:
        - RESTRICTED_SERVICES
    title: AnonPerimeter
    

You can also assume that the partner organization project is 999. You can define the following ingress and egress rules:
    
    
    # Anon Perimeter
    
    echo """
    - ingressFrom:
        identityType: ANY_IDENTITY
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
    """ > anoningress.yaml
    
    
    
    
    echo """
    - egressTo:
        operations:
        - serviceName: storage.googleapis.com
          methodSelectors:
          - method: google.storage.Write
          - method: google.storage.objects.create
        resources:
        - projects/999
      egressFrom:
        identityType: ANY_IDENTITY
    """ > anonegress.yaml
    
    
    
    # PHI Perimeter
    
    echo """
    - egressTo:
        operations:
        - serviceName: storage.googleapis.com
          methodSelectors:
          - method: \"*\"
        resources:
        - projects/222
      egressFrom:
        identityType: ANY_IDENTITY
    """ > phiegress.yaml
    

Apply the ingress and egress rules by running the following commands:
    
    
    gcloud beta access-context-manager perimeters update AnonPerimeter --set-ingress-policies=anoningress.yaml --set-egress-policies=anonegress.yaml
    
    
    
    gcloud beta access-context-manager perimeters update PhiPerimeter --set-egress-policies=phiegress.yaml
    

### Grant access to a third-party Compute Engine disk image

The following diagram shows a Compute Engine resource in a service perimeter that requires access to a Compute Engine disk image in a third-party image project that is outside the perimeter:

![Egress to image project](https://docs.cloud.google.com/static/vpc-service-controls/images/directional_policy_third_party_compute_engine_egress.png)

Assume that you have defined the following perimeter:
    
    
    name: accessPolicies/222/servicePerimeters/Example
    status:
      resources:
      - projects/111
      - projects/222
      restrictedServices:
      - compute.googleapis.com
      - containerregistry.googleapis.com
    title: Example
    

You now need to grant read access to disk images in `project 999`, which is in a different organization. You then define the following egress rule in a file and save the file as `compute.yaml`:
    
    
    echo """
    - egressTo:
        operations:
        - serviceName: compute.googleapis.com
          methodSelectors:
          - method: InstancesService.Insert
        resources:
        - projects/999
      egressFrom:
        identityType: ANY_IDENTITY
    """ > compute.yaml
    

Apply the egress rule by running the following command:
    
    
    gcloud beta access-context-manager perimeters update Example --set-egress-policies=compute.yaml
    

### Read a BigQuery dataset by allowing private access from a VPC network outside the perimeter

The following diagram shows multiple partner VPC networks outside the perimeter that need to read from a BigQuery resource inside a perimeter:

![Egress to image project](https://docs.cloud.google.com/static/vpc-service-controls/images/directional_policy_bigquery_ingress.png)

You can assume that you use the same perimeter as [example 1](https://docs.cloud.google.com/vpc-service-controls/docs/secure-data-exchange#access-google-cloud-resource-outside-the-perimeter):
    
    
    name: accessPolicies/222/servicePerimeters/Example
    status:
      resources:
      - projects/111
      restrictedServices:
      - bigquery.googleapis.com
      - containerregistry.googleapis.com
    title: Example
    

Your goal is to allow read access from a VPC network outside the perimeter of various partners. Define the following ingress rule in a file and save the file as `partneringress.yaml`:
    
    
    echo """
    - ingressFrom:
        identityType: ANY_IDENTITY
        sources:
        - resource: projects/888
        - resource: projects/999
      ingressTo:
        operations:
        - serviceName: bigquery.googleapis.com
          methodSelectors:
          - permission: bigquery.datasets.get
          - permission: bigquery.tables.list
          - permission: bigquery.tables.get
          - permission: bigquery.tables.getData
          - permission: bigquery.jobs.create
        resources:
        - \"*\"
    
    """ > partneringress.yaml
    

Apply the ingress rule by running the following command:
    
    
    gcloud beta access-context-manager perimeters update Example --set-ingress-policies=partneringress.yaml
    

For more flexibility and control, BigQuery uses `- permission:` `methodSelectors` rather than the `- method:` `methodSelectors` that is used by most services. A single BigQuery method (RunQuery) can operate in different ways on several different resources, and aligning with the permissions model enables more flexibility and control.

### Load into a Cloud Storage bucket (write) by allowing private access from a VPC network outside the perimeter

You can assume that you use same perimeter as [example 1](https://docs.cloud.google.com/vpc-service-controls/docs/secure-data-exchange#access-google-cloud-resource-outside-the-perimeter):
    
    
    name: accessPolicies/222/servicePerimeters/Example
    status:
      resources:
      - projects/111
      restrictedServices:
      - storage.googleapis.com
      - containerregistry.googleapis.com
    title: Example
    

Your goal is to allow access from a VPC network outside the perimeter to enable a partner to write data to the bucket inside the perimeter. You define an ingress rule and save the file as `partneringress.yaml`:
    
    
    echo """
    - ingressFrom:
        identityType: ANY_IDENTITY
        sources:
        - resource: projects/222
      ingressTo:
        operations:
        - serviceName: storage.googleapis.com
          methodSelectors:
          - method: google.storage.objects.create
        resources:
        - \"*\"
    """ > partneringress.yaml
    

Apply the ingress rule by running the following command:
    
    
    gcloud beta access-context-manager perimeters update Example --set-ingress-policies=partneringress.yaml
    

### Share logs in a separate perimeter by allowing projects from multiple perimeters to share logs

In this use case, assume that an enterprise has a shared project for collection of log data from across their Google Cloud deployment. The enterprise needs to be able to log data from multiple different VPC Service Controls perimeters into the shared logs project, which is in its own perimeter. The logs project should not access any resources other than the logs.

Assume that you have defined the following three perimeters:
    
    
    # Sensitive 1
    name: accessPolicies/222/servicePerimeters/Sensitive1
    status:
      resources:
      - projects/111
      restrictedServices:
      - bigquery.googleapis.com
      - containerregistry.googleapis.com
      - logging.googleapis.com
      vpcAccessibleServices:
        enableRestriction: true
        allowedServices:
        - RESTRICTED_SERVICES
    title: Sensitive Data 1
    
    
    
    # Sensitive 2
    name: accessPolicies/222/servicePerimeters/Sensitive2
    status:
      resources:
      - projects/222
      restrictedServices:
      - bigquery.googleapis.com
      - containerregistry.googleapis.com
      - logging.googleapis.com
      vpcAccessibleServices:
        enableRestriction: true
        allowedServices:
        - RESTRICTED_SERVICES
    title: Sensitive Data 2
    
    
    
    #Logs
    name: accessPolicies/222/servicePerimeters/Logs
    status:
      resources:
      - projects/777
      restrictedServices:
      - logging.googleapis.com
      vpcAccessibleServices:
        enableRestriction: true
        allowedServices:
        - RESTRICTED_SERVICES
    title: Logs Perimeter
    

To allow `Sensitive1` and `Sensitive2` to write logs to Logs perimeter, define the following egress rule in a file and save the file as `logsegress.yaml`:
    
    
    echo """
    - egressTo:
        operations:
        - serviceName: logging.googleapis.com
          methodSelectors:
          - method: LoggingServiceV2.WriteLogEntries
          - method: LoggingService.WriteLogEntries
        resources:
        - projects/777
      egressFrom:
        identityType: ANY_IDENTITY
    """ > logsegress.yaml
    

Apply the egress rules by running the following commands:
    
    
    gcloud beta access-context-manager perimeters update Sensitive1 --set-egress-policies=logsegress.yaml
    
    
    
    gcloud beta access-context-manager perimeters update Sensitive2 --set-egress-policies=logsegress.yaml
    

A similar configuration can be specified for any other sensitive data perimeter that needs to write to the logs perimeter.

## What's next

  * [Configuring ingress and egress policies](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies)
  * [Context-aware access with ingress rules](https://docs.cloud.google.com/vpc-service-controls/docs/context-aware-access)
  * [Ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
