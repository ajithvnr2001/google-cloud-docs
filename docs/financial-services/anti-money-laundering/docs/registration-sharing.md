---
url: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/registration-sharing/
title: Party registration sharing for multiple instances \u00a0|\u00a0 Anti Money Laundering AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:01:54.442746+00:00
---

# Party registration sharing for multiple instances  |  Anti Money Laundering AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/registration-sharing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Anti Money Laundering AI ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs)
  * [ Guides ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/overview)



Send feedback 

#  Party registration sharing for multiple instances Stay organized with collections  Save and categorize content based on your preferences. 

You can share an AML AI instance's registered parties with up to two additional instances in the same Google Cloud region for predictions. This allows your organization to train models on real data without impacting performance of the main AML AI instance that you use to generate AML alerts and without paying twice for registering the same parties.

The main AML AI instance is the host where you register your parties. The additional instance or instances, referred to as consumers, don't need to register parties. Instead, you can generate predictions for any party registered in the host instance. Typically these instances are used for less critical tasks, such as training and evaluating new models prior to deployment to the main instance.

## Before you begin

Select an instance to use as the host. This is usually the instance that you use to generate production alerts.

Select one or two instances to use as consumers. These are usually the instances you use to create, evaluate, and analyze AML AI models.

**Note:** We recommend that you use instances that have no registered parties. If parties exist on the consumer instances, you should deregister them as soon as possible to avoid unnecessary charges. See [Register your parties](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/register-parties) for instructions on registering and deregistering parties.

The host and consumer instances must reside in the same Google Cloud region and belong to the same project or projects within the same organization.

## Configure the host instance

To configure an instance to be the host instance for registration sharing, designate up to two instances as the chosen consumer instances in the `valid_party_registration_sharing_consumer_instances` field.

You can set this field when you [create the host Instance](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/create-and-manage-instances), or you can update this field in an existing instance using the [projects.locations.instances.patch](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances/patch) request.

This field is a string list, with a maximum length of 2.

Before using any of the request data, make the following replacements:

  * LOCATION: the location of the host and consumer instances.
  * HOST_PROJECT_ID: a user-defined identifier for the project that contains the host instance.
  * HOST_INSTANCE_ID: a user-defined identifier for the host instance.
  * CONSUMER_PROJECT_ID: a user-defined identifier for the project that contains the consumer instance.
  * CONSUMER_INSTANCE_ID: a user-defined identifier for the consumer instance.



Save the request body in a file named request.json. Run the following command in the terminal to create or overwrite this file in the current directory:
    
    
    cat > request.json << 'EOF'
    {
      "valid_party_registration_sharing_consumer_instances": [
        "projects/CONSUMER_PROJECT_ID/locations/LOCATION/instances/CONSUMER_INSTANCE_ID"
     ]
    }
    EOF
    
    

Use a curl command to call its HTTP endpoint, as shown in the following example.
    
    
     curl -X PATCH \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         -d @request.json \
    "https://financialservices.googleapis.com/v1/projects/HOST_PROJECT_ID/locations/LOCATION/instances/HOST_INSTANCE_ID?updateMask=valid_party_registration_sharing_consumer_instances"
    
    

## Configure the consumer instance

Configure each consumer instance using the `party_registration_sharing_host_instance` field. This field is a string.

Save the request body in a file named request.json. Run the following command in the terminal to create or overwrite this file in the current directory:
    
    
    cat > request.json << 'EOF'
    
      {
        "party_registration_sharing_host_instance": "projects/HOST_PROJECT_ID/locations/LOCATION/instances/HOST_INSTANCE_ID"
      }
    EOF
    
    

Use a curl command to call its HTTP endpoint, as shown in the following example.
    
    
    curl -X PATCH \
     -H "Authorization: Bearer $(gcloud auth print-access-token)" \
     -H "Content-Type: application/json; charset=utf-8" \
     -d @request.json \
     "https://financialservices.googleapis.com/v1/projects/CONSUMER_PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID?updateMask=party_registration_sharing_host_instance"
    
    

## Configure VPC-SC

If the host and consumer instances use different VPC-SC perimeters, configure a [VPC-SC Perimeter Bridge](https://docs.cloud.google.com/vpc-service-controls/docs/share-across-perimeters) or [Ingress/Egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) for the projects that contain the instances.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
