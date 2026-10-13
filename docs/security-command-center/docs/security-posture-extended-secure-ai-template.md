---
url: https://docs.cloud.google.com/security-command-center/docs/security-posture-extended-secure-ai-template/
title: Predefined posture template for secure AI, extended \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:13:56.419255+00:00
---

# Predefined posture template for secure AI, extended  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/security-posture-extended-secure-ai-template/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Predefined posture template for secure AI, extended Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation)) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page describes the preventative and detective policies that are included in the v1.0 version of the predefined posture template for secure AI, extended. This posture template includes two policy sets:

  * A policy set that includes organization policies that apply to Gemini Enterprise Agent Platform workloads.

  * A policy set that includes custom Security Health Analytics detectors that apply to Gemini Enterprise Agent Platform workloads.




You can use this predefined posture template to configure a security posture that helps protect Gemini and Gemini Enterprise Agent Platform resources. If you want to deploy this predefined posture template, you must customize some of the policies so that they apply to your environment.

## Organization policy constraints

The following table describes the organization policies that are included in this posture.

Policy | Description | Compliance standard  
---|---|---  
`ainotebooks.accessMode` | This constraint defines the modes of access that are allowed to Vertex AI Workbench notebooks and instances.You must configure this value when you adopt this predefined posture template. | NIST SP 800-53 control: AC-3(3) and AC-6(1)  
`ainotebooks.disableFileDownloads` | This constraint prevents the creation of Vertex AI Workbench instances with the file download option enabled. By default, the file download option can be enabled on any Vertex AI Workbench instance. The value is `true` to turn off file downloads on new Vertex AI Workbench instances. | NIST SP 800-53 control: AC-3(1)  
`ainotebooks.disableRootAccess` | This constraint prevents newly created Vertex AI Workbench user-managed notebooks and instances from enabling root access. By default, Vertex AI Workbench user-managed notebooks and instances can have root access enabled.The value is `true` to disable root access on new Vertex AI Workbench user-managed notebooks and instances. | NIST SP 800-53 control: AC-3 and AC-6(2)  
`ainotebooks.disableTerminal` | This constraint prevents the creation of Vertex AI Workbench instances with the terminal enabled. By default, the terminal can be enabled on Vertex AI Workbench instances.The value is `true` to disable the terminal on new Vertex AI Workbench instances. | NIST SP 800-53 control: AC-3, AC-6, and CM-2  
`ainotebooks.environmentOptions` | This constraint defines the VM and container image options a user can select when creating new Vertex AI Workbench notebooks and instances where this constraint is enforced. The options to be allowed or denied must be listed explicitly. Values are the following:
    
    
    policy_rules:
    - values:
        allowed_values:
        - is:ainotebooks-vm/deeplearning-platform-release/image-family/tf-1-15-cpu
        - is:ainotebooks-vm/deeplearning-platform-release/image-family/tf-2-1-cpu
        - is:ainotebooks-vm/deeplearning-platform-release/image-family/tf-1-15-gpu
        - is:ainotebooks-vm/deeplearning-platform-release/image-family/tf-2-1-gpu
        - is:ainotebooks-vm/deeplearning-platform-release/image-family/caffe1-latest-cpu-experimental
        - is:ainotebooks-vm/deeplearning-platform-release/image-name/r-3-6-cpu-experimental-20200617
        - is:ainotebooks-vm/deeplearning-platform-release/image-name/tf2-ent-2-1-cpu-20200613
        - is:ainotebooks-vm/deeplearning-platform-release/image-name/tf2-2-2-cu101-20200616
        - is:ainotebooks-vm/deeplearning-platform-release/image-name/tf-1-15-cu100-20200615
        - is:ainotebooks-vm/deeplearning-platform-release/image-name/pytorch-latest-cpu-20200615
        - is:ainotebooks-container/gcr.io/deeplearning-platform-release/tf-gpu.1-15
        - is:ainotebooks-container/gcr.io/deeplearning-platform-release/tf-cpu.1-15:latest
        - is:ainotebooks-container/gcr.io/deeplearning-platform-release/tf-cpu.1-15:m48
        - is:ainotebooks-container/gcr.io/deeplearning-platform-release/tf-cpu.1-15:m46
        - is:ainotebooks-container/custom-container:latest
    

| NIST SP 800-53 control: AC-3, AC-6, and CM-2  
`ainotebooks.requireAutoUpgradeSchedule` | This constraint requires that newly created Vertex AI Workbench user-managed notebooks and instances have an automatic upgrade schedule set.The value is `true` to require automatic scheduled upgrades on new Vertex AI Workbench user-managed notebooks and instances. | NIST SP 800-53 control: AU-9, CM-2, and CM-6  
`ainotebooks.restrictPublicIp` | This constraint restricts public IP access to newly created Vertex AI Workbench notebooks and instances. By default, public IPs can access Vertex AI Workbench notebooks and instances.The value is `true` to restrict public IP access on new Vertex AI Workbench notebooks and instances. | NIST SP 800-53 control: AC-3, AC-4, and SC-7  
`ainotebooks.restrictVpcNetworks` | This list defines the VPC networks a user can select when creating new Vertex AI Workbench instances where this constraint is enforced.You must configure this value when you adopt this predefined posture template. | NIST SP 800-53 control: AC-3, AC-4, and CM-2  
  
## Security Health Analytics detectors

The following table describes the custom modules for Security Health Analytics that are included in the predefined posture template.

Detector name | Applicable resource | Description | Compliance standards  
---|---|---|---  
vertexAIDataSetCMEKDisabled | `aiplatform.googleapis.com/Dataset` | This detector checks whether any dataset isn't encrypted using a [customer-managed encryption key (CMEK)](https://docs.cloud.google.com/vertex-ai/docs/general/cmek). To resolve this finding, verify that you created the key and key ring, set up permissions, and provided the key when you created your dataset. For instructions, see [Configure CMEK for your resources](https://docs.cloud.google.com/vertex-ai/docs/general/cmek#configure-cmek). | NIST SP 800-53 control: SC-12 and SC-13  
vertexAIModelCMEKDisabled | `aiplatform.googleapis.com/Model` | This detector checks whether a model isn't encrypted using a CMEK. To resolve this finding, verify that you created the key and key ring, set up permissions, and provided the key when you created your model. For instructions, see [Configure CMEK for your resources](https://docs.cloud.google.com/vertex-ai/docs/general/cmek#configure-cmek). | NIST SP 800-53 control: SC-12 and SC-13  
vertexAIEndpointCMEKDisabled | `aiplatform.googleapis.com/Endpoint` | This detector checks whether an [endpoint](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.endpoints) isn't encrypted using a CMEK. To resolve this finding, verify that you created the key and key ring, set up permissions, and provided the key when you created your endpoint. For instructions, see [Configure CMEK for your resources](https://docs.cloud.google.com/vertex-ai/docs/general/cmek#configure-cmek). | NIST SP 800-53 control: SC-12 and SC-13  
vertexAITrainingPipelineCMEKDisabled | `aiplatform.googleapis.com/TrainingPipeline` | This detector checks whether a [training pipeline](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.trainingPipelines) isn't encrypted using a CMEK. To resolve this finding, verify that you created the key and key ring, set up permissions, and provided the key when you created your training pipeline. For instructions, see [Configure CMEK for your resources](https://docs.cloud.google.com/vertex-ai/docs/general/cmek#configure-cmek). | NIST SP 800-53 control: SC-12 and SC-13  
vertexAICustomJobCMEKDisabled | `aiplatform.googleapis.com/CustomJob` | This detector checks whether a [job that runs a custom workload](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.customJobs) isn't encrypted using a CMEK. To resolve this finding, verify that you created the key and key ring, set up permissions, and provided the key when you created your custom job. For instructions, see [Configure CMEK for your resources](https://docs.cloud.google.com/vertex-ai/docs/general/cmek#configure-cmek). | NIST SP 800-53 control: SC-12 and SC-13  
vertexAIDataLabelingJobHyperparameterTuningJobCMEKDisabled | `aiplatform.googleapis.com/HyperparameterTuningJob` | This detector checks whether a [hyperparameter tuning job](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.hyperparameterTuningJobs) isn't encrypted using a CMEK. To resolve this finding, verify that you created the key and key ring, set up permissions, and provided the key when you created your hyperparameter tuning job. For instructions, see [Configure CMEK for your resources](https://docs.cloud.google.com/vertex-ai/docs/general/cmek#configure-cmek). | NIST SP 800-53 control: SC-12 and SC-13  
  
## View the posture template

To view the posture template for secure AI, extended, do the following: 

### gcloud

Before using any of the command data below, make the following replacements: 

  * `ORGANIZATION_ID`: the numeric ID of the organization. 



Execute the [`gcloud scc posture-templates describe`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/posture-templates/describe) command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud scc posture-templates describe \
        organizations/ORGANIZATION_ID/locations/global/postureTemplates/secure_ai_extended

#### Windows (PowerShell)
    
    
    gcloud scc posture-templates describe `
        organizations/ORGANIZATION_ID/locations/global/postureTemplates/secure_ai_extended

#### Windows (cmd.exe)
    
    
    gcloud scc posture-templates describe ^
        organizations/ORGANIZATION_ID/locations/global/postureTemplates/secure_ai_extended

The response contains the posture template.

### REST

Before using any of the request data, make the following replacements: 

  * `ORGANIZATION_ID`: the numeric ID of the organization. 



HTTP method and URL: 
    
    
    GET https://securityposture.googleapis.com/v1/organizations/ORGANIZATION_ID/locations/global/postureTemplates/secure_ai_extended

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://securityposture.googleapis.com/v1/organizations/ORGANIZATION_ID/locations/global/postureTemplates/secure_ai_extended"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://securityposture.googleapis.com/v1/organizations/ORGANIZATION_ID/locations/global/postureTemplates/secure_ai_extended" | Select-Object -Expand Content

The response contains the posture template.

## What's next

  * [Create a security posture using this predefined posture template](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-posture).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
