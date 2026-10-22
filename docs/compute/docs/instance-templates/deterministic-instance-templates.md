---
url: https://docs.cloud.google.com/compute/docs/instance-templates/deterministic-instance-templates/
title: Deterministic instance templates \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:54.038906+00:00
---

# Deterministic instance templates  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-templates/deterministic-instance-templates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Deterministic instance templates Stay organized with collections  Save and categorize content based on your preferences. 

This page describes when and why to create deterministic instance templates. Deterministic instance templates make explicitly clear the type of third-party services or apps to install on your instances when the instance template is deployed. By creating deterministic instance templates, you minimize ambiguity and unexpected behavior from your instance templates.

## Why create deterministic instance templates

In general, we recommend that the properties of your instance template be as explicit and deterministic as possible. If you employ startup scripts in your instance templates that install or use third-party services, make sure that these scripts provide explicit information, such as the version of app to install. Compute Engine can only rely on information defined in the template and has no control over referenced third-party services. If your template is too vague, your instance template might behave unexpectedly.

For example, consider the following command to create an instance template with a startup script that installs apache2 and uses a file that is hosted on an external server:

**Note:** This is just an example snippet pointing to a non-existent server at 108.59.87.185. Copying this example directly fails when the script attempts to connect to 108.59.87.185. Instead, replace the last line with your own server information, if applicable.
    
    
    gcloud compute instance-templates create example-template-with-startup \
        --image-family debian-9 \
        --image-project debian-cloud \
        --metadata startup-script='#! /bin/bash
        sudo apt install -y apache2
        scp myuser@108.59.87.185:index.php /var/www/'
    

There are two potential issues with this startup script:

  * The script does not explicitly define which version of apache2 to install, and relies on the current version available in the `apt` repository.
  * The script relies on a file hosted on a third-party that isn't versioned and could have been changed since the last time the instance template was used.



If you use an [autoscaler](https://docs.cloud.google.com/compute/docs/autoscaler), a non-deterministic instance template can cause your autoscaler to add new instances to a [managed instance group](https://docs.cloud.google.com/compute/docs/instance-groups) with a different configuration, such as a different version of apache2.

Similarly, if you applied this template to a managed instance group, [updated the group to a different template](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs) service, and then decided to roll back to the previous template, you might end up with instances that use a different version of apache2 or index.php file than before the update because your instances would always fetch the most recent version at startup.

## Avoiding ambiguous or unexpected instance template behavior

To avoid unexpected template behavior, use the following methods:

  * Use [container-optimized images](https://docs.cloud.google.com/compute/docs/containers#container_images) or Docker, with Docker tags. For example, we recommend that you assign new tags for every new build of your Docker image, and use these tags in your instance templates instead of the default latest tag. For a container-optimized image, you can explicitly reference a particular build of your image in your manifest file. The example below uses Docker image "myimage" at version tagged with "version_2_1_3":
        
        version: v1beta2
        containers:
          - name: simple-echo
            image: myimage:version_2_1_3
               [ rest of your manifest file ]
        

  * [Create a custom image](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images) to use as the image for the template. This is preferable to startup scripts because it guarantees that every instance is the same. Startup scripts might have different results after distribution package updates. Use startup scripts in your instance templates for prototyping and rapid development, and use custom images when you are ready to deploy production-quality services.

  * If you do use startup scripts, consider updating your scripts to be deterministic. For example, create a new version of the previous template, and specify a deterministic startup script as follows:
        
        gcloud compute instance-templates create example-template-with-startup-2-1-3 \
            --image-family debian-9 \
            --image-project debian-cloud \
            --metadata startup-script='#! /bin/bash
            sudo apt install -y apache2=2.2.20-1ubuntu1
            scp myuser@108.59.87.185:version_2_1_3/index.php /var/www/'
        

where "version_2_1_3" is a subdirectory containing PHP scripts for the version 2.1.3 of your service.

  * When specifying an instance template—for example when you are creating or updating a managed instance group—Google recommends that you specify the template's ID value instead of its name value. Although both values are valid, the ID is unique, which means that the instance template that you specify is the one that is used when creating VMs from that instance template. Using an ID instead of a name helps to mitigate potential security vulnerabilities—for example, [TOCTOU](https://en.wikipedia.org/wiki/Time_of_check_to_time_of_use_vulnerability) vulnerabilities, where an attacker can delete a template and recreate it with the same name prior to its use.

To view the ID of an instance template, see [Get information about an instance template](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template).




## What's next

  * [Create an instance template](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates).
  * [Manage your instance templates](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
