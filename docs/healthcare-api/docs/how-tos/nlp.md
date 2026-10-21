---
url: https://docs.cloud.google.com/healthcare-api/docs/how-tos/nlp/
title: Use the Healthcare Natural Language API \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:01:53.396900+00:00
---

# Use the Healthcare Natural Language API  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/how-tos/nlp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Use the Healthcare Natural Language API Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** The Healthcare Natural Language API is deprecated and will be shut down on May 27, 2026. For more information, see [Deprecations](https://docs.cloud.google.com/healthcare-api/docs/deprecations). 

This page explains how to enable the Healthcare Natural Language API, configure permissions, and call the [`analyzeEntities`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.services.nlp/analyzeEntities) method to extract medical insights from medical text.

## Overview

The Healthcare Natural Language API provides machine learning solutions for deriving insights from medical text. The Healthcare Natural Language API is part of the Cloud Healthcare API. For an overview of the Healthcare Natural Language API, see the [Healthcare Natural Language API conceptual documentation](https://docs.cloud.google.com/healthcare-api/docs/concepts/nlp).

The Healthcare Natural Language API parses unstructured medical text such as medical records or insurance claims. It then generates a structured data representation of the medical knowledge entities stored in these data sources for downstream analysis and automation. For example, you can:

  * Extract information about medical concepts like diseases, medications, medical devices, procedures, and their clinically relevant attributes
  * Map medical concepts to standard medical vocabularies such as RxNorm, ICD-10, MeSH, and SNOMED CT (US and UK users only)
  * Derive medical insights from text and integrate them with data analytics products in Google Cloud

**Note:** You don't need to create a dataset in the Cloud Healthcare API to use the Healthcare Natural Language API.

## Available locations

The Healthcare Natural Language API is available in the following locations:

Location name | Location description  
---|---  
[`asia-south1`](https://cloud.google.com/about/locations/?region=asia-pacific#asia-pacific) | Mumbai, India  
[`australia-southeast1`](https://cloud.google.com/about/locations/?region=asia-pacific#asia-pacific) | Sydney, Australia  
[`europe-west2`](https://cloud.google.com/about/locations/?region=europe#europe) | London, UK  
[`europe-west4`](https://cloud.google.com/about/locations/?region=europe#europe) | Netherlands  
[`northamerica-northeast1`](https://cloud.google.com/about/locations/?region=americas#americas) | Montréal, Canada  
[`us-central1`](https://cloud.google.com/about/locations/?region=americas#americas) | Iowa, USA  
  
## Enable the Healthcare Natural Language API

Before you begin using the Healthcare Natural Language API, you must enable the API for your Google Cloud project. You can use the Healthcare Natural Language API without enabling or using features of the Cloud Healthcare API.

To enable the API, complete the following steps:

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Create a service account: 

     1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     2. In the Google Cloud console, go to the **Create service account** page. 

[Go to Create service account](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)
     3. Select your project. 
     4. In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name. 

In the **Service account description** field, enter a description. For example, `Service account for quickstart`. 

     5. Click **Create and continue**. 
     6. Grant the **Project > Owner** role to the service account. 

To grant the role, find the **Select a role** list, then select **Project > Owner**. 

**Note** : The **Role** field affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. In production environments, do not grant the Owner, Editor, or Viewer roles. Instead, grant a [predefined role](https://docs.cloud.google.com/iam/docs/understanding-roles#predefined_roles) or [custom role](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) that meets your needs. 
     7. Click **Continue**. 
     8. Click **Done** to finish creating the service account. 

Do not close your browser window. You will use it in the next step. 

  5. Create a service account key: 

     1. In the Google Cloud console, click the email address for the service account that you created. 
     2. Click **Keys**. 
     3. Click **Add key** , and then click **Create new key**. 
     4. Click **Create**. A JSON key file is downloaded to your computer. 
     5. Click **Close**. 
  6. Set the environment variable `GOOGLE_APPLICATION_CREDENTIALS` to the path of the JSON file that contains your credentials. This variable applies only to your current shell session, so if you open a new session, set the variable again. 

**Example:** Linux or macOS
         
         export GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"

Replace `KEY_PATH` with the path of the JSON file that contains your credentials.

For example:
         
         export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/service-account-file.json"

**Example:** Windows

For PowerShell:
         
         $env:GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"

Replace `KEY_PATH` with the path of the JSON file that contains your credentials.

For example:
         
         $env:GOOGLE_APPLICATION_CREDENTIALS="C:\Users\username\Downloads\service-account-file.json"

For command prompt:
         
         set GOOGLE_APPLICATION_CREDENTIALS=KEY_PATH

Replace `KEY_PATH` with the path of the JSON file that contains your credentials.

  7. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. Create a service account: 

     1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     2. In the Google Cloud console, go to the **Create service account** page. 

[Go to Create service account](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)
     3. Select your project. 
     4. In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name. 

In the **Service account description** field, enter a description. For example, `Service account for quickstart`. 

     5. Click **Create and continue**. 
     6. Grant the **Project > Owner** role to the service account. 

To grant the role, find the **Select a role** list, then select **Project > Owner**. 

**Note** : The **Role** field affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. In production environments, do not grant the Owner, Editor, or Viewer roles. Instead, grant a [predefined role](https://docs.cloud.google.com/iam/docs/understanding-roles#predefined_roles) or [custom role](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) that meets your needs. 
     7. Click **Continue**. 
     8. Click **Done** to finish creating the service account. 

Do not close your browser window. You will use it in the next step. 

  10. Create a service account key: 

     1. In the Google Cloud console, click the email address for the service account that you created. 
     2. Click **Keys**. 
     3. Click **Add key** , and then click **Create new key**. 
     4. Click **Create**. A JSON key file is downloaded to your computer. 
     5. Click **Close**. 
  11. Set the environment variable `GOOGLE_APPLICATION_CREDENTIALS` to the path of the JSON file that contains your credentials. This variable applies only to your current shell session, so if you open a new session, set the variable again. 

**Example:** Linux or macOS
         
         export GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"

Replace `KEY_PATH` with the path of the JSON file that contains your credentials.

For example:
         
         export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/service-account-file.json"

**Example:** Windows

For PowerShell:
         
         $env:GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"

Replace `KEY_PATH` with the path of the JSON file that contains your credentials.

For example:
         
         $env:GOOGLE_APPLICATION_CREDENTIALS="C:\Users\username\Downloads\service-account-file.json"

For command prompt:
         
         set GOOGLE_APPLICATION_CREDENTIALS=KEY_PATH

Replace `KEY_PATH` with the path of the JSON file that contains your credentials.

  12. Enable the Cloud Healthcare API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=healthcare.googleapis.com&redirect=https%3A//cloud.google.com/healthcare-api/docs/store-healthcare-data-rest)

  13. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  14. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  15. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init




## Set up permissions

To use the features in this guide, you must have the `healthcare.nlpservice.analyzeEntities` [permission](https://docs.cloud.google.com/iam/docs/overview#permissions), which is included in the `healthcare.nlpServiceViewer` [role](https://docs.cloud.google.com/iam/docs/overview#roles).

To assign this role, run the [`gcloud projects add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) command:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member serviceAccount:SERVICE_ACCOUNT_ID \
        --role roles/healthcare.nlpServiceViewer

## Extract entities, relations, and contextual attributes

The Healthcare Natural Language API uses context-aware models to extract medical entities, relations, and contextual attributes. Each text entity is extracted into a medical dictionary entry. To extract this level of medical insights from medical text, use the [`projects.locations.services.nlp.analyzeEntities`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.services.nlp/analyzeEntities) method.

To include the SNOMED CT licensed vocabulary in your entity mentions, see [Include licensed vocabularies](https://docs.cloud.google.com/healthcare-api/docs/how-tos/nlp#including_licensed_vocabularies).

To extract medical insights from medical text using the Healthcare Natural Language API, make a `POST` request and specify the target text in the [`documentContent`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.services.nlp/analyzeEntities#body.request_body.FIELDS.document_content) field. The maximum size of the medical text is 20,000 Unicode characters.

The following samples show how to use the `analyzeEntities` method to extract medical insights from the medical text "Insulin regimen 5 units IV will be administered for diabetes.".

### REST

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project
  * `LOCATION`: the dataset location



Request JSON body: 
    
    
    {
      "documentContent": "Insulin regimen 5 units IV will be administered for diabetes."
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "documentContent": "Insulin regimen 5 units IV will be administered for diabetes."
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/services/nlp:analyzeEntities"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "documentContent": "Insulin regimen 5 units IV will be administered for diabetes."
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json" `  
        -InFile request.json `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/services/nlp:analyzeEntities" | Select-Object -Expand Content

If the request is successful, the response includes the following information: 

  * Recognized medical knowledge entities
  * Functional features
  * Relations between the recognized entities
  * Contextual attributes
  * Mappings of the medical knowledge entities into standard terminologies



For a list of supported entity, attribute, and relation types, see the [Healthcare Natural Language API features](https://docs.cloud.google.com/healthcare-api/docs/concepts/nlp#entity_analysis_response_fields).

The following response identifies Therapeutic Insulin, the entity with code `C581` in the NCI terminology system, as the medication. The response also includes the confidence score assigned to the response. For more information about the response fields, see the [`analyzeEntities`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.services.nlp/analyzeEntities#response-body) documentation. 

#### Response
    
    
    {
      "entityMentions": [
        {
          "mentionId": "1",
          "type": "MEDICINE",
          "text": {
            "content": "Insulin regimen",
            "beginOffset": 0
          },
          "linkedEntities": [
            {
              "entityId": "UMLS/C0021641"
            },
            {
              "entityId": "UMLS/C0795635"
            },
            {
              "entityId": "UMLS/C1533581"
            },
            {
              "entityId": "UMLS/C3537244"
            },
            {
              "entityId": "UMLS/C3714501"
            }
          ],
          "temporalAssessment": {
            "value": "UPCOMING",
            "confidence": 0.95375925302505493
          },
          "certaintyAssessment": {
            "value": "LIKELY",
            "confidence": 0.618984580039978
          },
          "subject": {
            "value": "PATIENT",
            "confidence": 0.99964696168899536
          },
          "confidence": 0.62128835916519165
        },
        {
          "mentionId": "2",
          "type": "MED_DOSE",
          "text": {
            "content": "5 units",
            "beginOffset": 16
          },
          "confidence": 0.78806477785110474
        },
        {
          "mentionId": "3",
          "type": "MED_ROUTE",
          "text": {
            "content": "IV",
            "beginOffset": 24
          },
          "linkedEntities": [
            {
              "entityId": "UMLS/C0348016"
            }
          ],
          "confidence": 0.8927428126335144
        },
        {
          "mentionId": "4",
          "type": "PROBLEM",
          "text": {
            "content": "diabetes",
            "beginOffset": 52
          },
          "linkedEntities": [
            {
              "entityId": "UMLS/C0011847"
            },
            {
              "entityId": "UMLS/C0011849"
            },
            {
              "entityId": "UMLS/C0241863"
            }
          ],
          "temporalAssessment": {
            "value": "CURRENT",
            "confidence": 0.91680806875228882
          },
          "certaintyAssessment": {
            "value": "LIKELY",
            "confidence": 0.98018729686737061
          },
          "subject": {
            "value": "PATIENT",
            "confidence": 0.99965417385101318
          },
          "confidence": 0.99518013000488281
        }
      ],
      "entities": [
        {
          "entityId": "UMLS/C0011847",
          "preferredTerm": "Diabetes",
          "vocabularyCodes": [
            "ICD10CM/E11",
            "LNC/LA10529-8",
            "LNC/LP128793-9",
            "LNC/MTHU040702",
            "MTH/NOCODE",
            "OMIM/MTHU050182"
          ]
        },
        {
          "entityId": "UMLS/C0011849",
          "preferredTerm": "Diabetes Mellitus",
          "vocabularyCodes": [
            "HPO/HP:0000819",
            "ICD10CM/E08-E13",
            "ICD9CM/250",
            "LNC/LA14291-1",
            "LNC/LA27539-8",
            "LNC/LP74722-7",
            "LNC/MTHU020781",
            "MEDLINEPLUS/4",
            "MSH/D003920",
            "MTH/NOCODE",
            "MTH/U000263",
            "NCI/C2985",
            "OMIM/MTHU036798"
          ]
        },
        {
          "entityId": "UMLS/C0021641",
          "preferredTerm": "Insulin",
          "vocabularyCodes": [
            "FMA/83365",
            "LNC/LA15805-7",
            "LNC/LP14676-8",
            "LNC/LP16325-0",
            "LNC/LP32542-0",
            "LNC/LP70329-5",
            "LNC/MTHU002108",
            "LNC/MTHU019392",
            "MSH/D007328",
            "MTH/NOCODE"
          ]
        },
        {
          "entityId": "UMLS/C0241863",
          "preferredTerm": "Diabetic",
          "vocabularyCodes": [
            "LNC/LA26134-9"
          ]
        },
        {
          "entityId": "UMLS/C0348016",
          "preferredTerm": "Intravenous",
          "vocabularyCodes": [
            "LNC/LA9437-0",
            "LNC/LP32453-0",
            "MTH/NOCODE",
            "NCI/C13346"
          ]
        },
        {
          "entityId": "UMLS/C0795635",
          "preferredTerm": "insulin, regular, human",
          "vocabularyCodes": [
            "LNC/LP17001-6",
            "MSH/D061386",
            "MTH/NOCODE",
            "NCI/C29125",
            "RXNORM/253182",
            "VANDF/4017559",
            "VANDF/4017569",
            "VANDF/4019786"
          ]
        },
        {
          "entityId": "UMLS/C1533581",
          "preferredTerm": "Therapeutic Insulin",
          "vocabularyCodes": [
            "MTH/NOCODE",
            "NCI/C581"
          ]
        },
        {
          "entityId": "UMLS/C3537244",
          "preferredTerm": "Insulins",
          "vocabularyCodes": [
            "MSH/D061385",
            "MTH/NOCODE"
          ]
        },
        {
          "entityId": "UMLS/C3714501",
          "preferredTerm": "Insulin Drug Class",
          "vocabularyCodes": [
            "MTH/NOCODE",
            "VANDF/4021631"
          ]
        }
      ],
      "relationships": [
        {
          "subjectId": "1",
          "objectId": "2",
          "confidence": 0.99964696168899536
        },
        {
          "subjectId": "1",
          "objectId": "3",
          "confidence": 0.99964696168899536
        },
        {
          "subjectId": "4",
          "objectId": "1",
          "confidence": 0.68552839756011963
        }
      ]
    }
    

## Include licensed vocabularies

By default, Healthcare Natural Language API responses include the [supported medical vocabularies](https://docs.cloud.google.com/healthcare-api/docs/concepts/nlp#supported_medical_vocabularies).

You can include the [SNOMED Clinical Terms, US Version (SNOMEDCT_US)](https://www.nlm.nih.gov/healthit/snomedct/us_edition.html) vocabulary in the response if your request meets the following requirements:

  * The API request originates in the US.
  * The `licensedVocabularies` field in the request body has the value `SNOMEDCT_US`.



If you don't require the SNOMED CT vocabulary, then none of these restrictions apply.

**Note:** By default, the [International Classification of Diseases, Tenth Revision, Clinical Modification (ICD10CM)](https://www.cdc.gov/nchs/icd/icd10cm.htm) vocabulary is included in all responses and is supported in all available locations. Adding `ICD10CM` as a `licensedVocabularies` field doesn't change the response. However, you can add `ICD10CM` as a value to the `licensedVocabularies` field without any location restrictions or without resulting in any errors.

The following sample shows how to include the SNOMED CT licensed vocabulary in the [`LicensedVocabularies`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.services.nlp/analyzeEntities#LicensedVocabulary) object to extract medical insights from the medical text "Insulin regimen 5 units IV will be administered for diabetes.".

### REST

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project
  * `LOCATION`: the dataset location



Request JSON body: 
    
    
    {
      "documentContent": "Insulin regimen 5 units IV will be administered for diabetes.",
      "licensedVocabularies": [
        "SNOMEDCT_US",
        "ICD10CM"
      ]
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "documentContent": "Insulin regimen 5 units IV will be administered for diabetes.",
      "licensedVocabularies": [
        "SNOMEDCT_US",
        "ICD10CM"
      ]
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/services/nlp:analyzeEntities"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "documentContent": "Insulin regimen 5 units IV will be administered for diabetes.",
      "licensedVocabularies": [
        "SNOMEDCT_US",
        "ICD10CM"
      ]
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json" `  
        -InFile request.json `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/services/nlp:analyzeEntities" | Select-Object -Expand Content

If the request is successful, the response includes vocabulary codes from the `SNOMEDCT_US` and `ICD10CM` licensed vocabularies. The output is the following and the requested licensed vocabulary codes are in bold: 

#### Response
    
    
    {
      "entityMentions": [
        {
          "mentionId": "1",
          "type": "MEDICINE",
          "text": {
            "content": "Insulin regimen",
            "beginOffset": 0
          },
          "linkedEntities": [
            {
              "entityId": "UMLS/C0021641"
            },
            {
              "entityId": "UMLS/C0795635"
            },
            {
              "entityId": "UMLS/C1533581"
            },
            {
              "entityId": "UMLS/C3537244"
            },
            {
              "entityId": "UMLS/C3714501"
            }
          ],
          "temporalAssessment": {
            "value": "UPCOMING",
            "confidence": 0.95375925302505493
          },
          "certaintyAssessment": {
            "value": "LIKELY",
            "confidence": 0.618984580039978
          },
          "subject": {
            "value": "PATIENT",
            "confidence": 0.99964696168899536
          },
          "confidence": 0.62128835916519165
        },
        {
          "mentionId": "2",
          "type": "MED_DOSE",
          "text": {
            "content": "5 units",
            "beginOffset": 16
          },
          "confidence": 0.78806477785110474
        },
        {
          "mentionId": "3",
          "type": "MED_ROUTE",
          "text": {
            "content": "IV",
            "beginOffset": 24
          },
          "linkedEntities": [
            {
              "entityId": "UMLS/C0348016"
            }
          ],
          "confidence": 0.8927428126335144
        },
        {
          "mentionId": "4",
          "type": "PROBLEM",
          "text": {
            "content": "diabetes",
            "beginOffset": 52
          },
          "linkedEntities": [
            {
              "entityId": "UMLS/C0011847"
            },
            {
              "entityId": "UMLS/C0011849"
            },
            {
              "entityId": "UMLS/C0241863"
            }
          ],
          "temporalAssessment": {
            "value": "CURRENT",
            "confidence": 0.91680806875228882
          },
          "certaintyAssessment": {
            "value": "LIKELY",
            "confidence": 0.98018729686737061
          },
          "subject": {
            "value": "PATIENT",
            "confidence": 0.99965417385101318
          },
          "confidence": 0.99518013000488281
        }
      ],
      "entities": [
        {
          "entityId": "UMLS/C0011847",
          "preferredTerm": "Diabetes",
          "vocabularyCodes": [
            "ICD10CM/E11",
            "LNC/LA10529-8",
            "LNC/LP128793-9",
            "LNC/MTHU040702",
            "MTH/NOCODE",
            "OMIM/MTHU050182"
          ]
        },
        {
          "entityId": "UMLS/C0011849",
          "preferredTerm": "Diabetes Mellitus",
          "vocabularyCodes": [
            "HPO/HP:0000819",
            "ICD10CM/E08-E13",
            "ICD9CM/250",
            "LNC/LA14291-1",
            "LNC/LA27539-8",
            "LNC/LP74722-7",
            "LNC/MTHU020781",
            "MEDLINEPLUS/4",
            "MSH/D003920",
            "MTH/NOCODE",
            "MTH/U000263",
            "NCI/C2985",
            "OMIM/MTHU036798",
            "SNOMEDCT_US/73211009"
          ]
        },
        {
          "entityId": "UMLS/C0021641",
          "preferredTerm": "Insulin",
          "vocabularyCodes": [
            "FMA/83365",
            "LNC/LA15805-7",
            "LNC/LP14676-8",
            "LNC/LP16325-0",
            "LNC/LP32542-0",
            "LNC/LP70329-5",
            "LNC/MTHU002108",
            "LNC/MTHU019392",
            "MSH/D007328",
            "MTH/NOCODE",
            "SNOMEDCT_US/39487003",
            "SNOMEDCT_US/412222002",
            "SNOMEDCT_US/67866001"
          ]
        },
        {
          "entityId": "UMLS/C0241863",
          "preferredTerm": "Diabetic",
          "vocabularyCodes": [
            "LNC/LA26134-9"
          ]
        },
        {
          "entityId": "UMLS/C0348016",
          "preferredTerm": "Intravenous",
          "vocabularyCodes": [
            "LNC/LA9437-0",
            "LNC/LP32453-0",
            "MTH/NOCODE",
            "NCI/C13346",
            "SNOMEDCT_US/255560000"
          ]
        },
        {
          "entityId": "UMLS/C0795635",
          "preferredTerm": "insulin, regular, human",
          "vocabularyCodes": [
            "LNC/LP17001-6",
            "MSH/D061386",
            "MTH/NOCODE",
            "NCI/C29125",
            "RXNORM/253182",
            "SNOMEDCT_US/126210001",
            "SNOMEDCT_US/417423002",
            "SNOMEDCT_US/420609005",
            "SNOMEDCT_US/96367001",
            "VANDF/4017559",
            "VANDF/4017569",
            "VANDF/4019786"
          ]
        },
        {
          "entityId": "UMLS/C1533581",
          "preferredTerm": "Therapeutic Insulin",
          "vocabularyCodes": [
            "MTH/NOCODE",
            "NCI/C581"
          ]
        },
        {
          "entityId": "UMLS/C3537244",
          "preferredTerm": "Insulins",
          "vocabularyCodes": [
            "MSH/D061385",
            "MTH/NOCODE"
          ]
        },
        {
          "entityId": "UMLS/C3714501",
          "preferredTerm": "Insulin Drug Class",
          "vocabularyCodes": [
            "MTH/NOCODE",
            "VANDF/4021631"
          ]
        }
      ],
      "relationships": [
        {
          "subjectId": "1",
          "objectId": "2",
          "confidence": 0.99964696168899536
        },
        {
          "subjectId": "1",
          "objectId": "3",
          "confidence": 0.99964696168899536
        },
        {
          "subjectId": "4",
          "objectId": "1",
          "confidence": 0.68552839756011963
        }
      ]
    }
    

## Extract output as a FHIR R4 bundle

You can extract entities from text and map them to FHIR R4 resources and elements. The resulting FHIR R4 bundle includes all entities, entity mentions, and relationships in JSON format. For example, the Healthcare Natural Language API maps the base entity `PROBLEM` to the `Condition` FHIR R4 resource and the entity `PROBLEM.ANATOMICAL_STRUCTURE` to the `Condition.bodySite` FHIR element. For a list of other mappings, see [Healthcare Natural Language API output as a FHIR bundle](https://docs.cloud.google.com/healthcare-api/docs/concepts/nlp#nlp-fhir-ref-table).

The following samples show how to extract medical insights from the medical text "Insulin regimen 5 units IV will be administered for diabetes." in a FHIR R4 bundle. For more information, see [`AlternativeOutputFormat`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.services.nlp/analyzeEntities#alternativeoutputformat) object.

### REST

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project
  * `LOCATION`: the dataset location



Request JSON body: 
    
    
    {
      "documentContent": "Insulin regimen 5 units IV will be administered for diabetes.",
      "alternativeOutputFormat": "FHIR_BUNDLE"
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "documentContent": "Insulin regimen 5 units IV will be administered for diabetes.",
      "alternativeOutputFormat": "FHIR_BUNDLE"
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/services/nlp:analyzeEntities"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "documentContent": "Insulin regimen 5 units IV will be administered for diabetes.",
      "alternativeOutputFormat": "FHIR_BUNDLE"
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json" `  
        -InFile request.json `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/services/nlp:analyzeEntities" | Select-Object -Expand Content

If the request is successful, the response contains a JSON object with the following entries: 

  * The recognized entity mentions with the entities and their relationships in a format similar to the output in [ Extract entities, relations, and contextual attributes](https://docs.cloud.google.com/healthcare-api/docs/how-tos/nlp#extract-entities). 
  * A `fhirBundle` key containing a string-formatted FHIR Bundle resource. The FHIR bundle includes all the entities, the entity mentions, and the relationships in JSON format. 



#### Response
    
    
    {
      "entityMentions": [
        {
          "mentionId": "1",
          "type": "MEDICINE",
          "text": {
            "content": "Insulin regimen",
            "beginOffset": 0
          },
          "linkedEntities": [
            {
              "entityId": "UMLS/C0021641"
            },
            {
              "entityId": "UMLS/C0795635"
            },
            {
              "entityId": "UMLS/C1533581"
            },
            {
              "entityId": "UMLS/C3537244"
            },
            {
              "entityId": "UMLS/C3714501"
            }
          ],
          "temporalAssessment": {
            "value": "UPCOMING",
            "confidence": 0.95375925302505493
          },
          "certaintyAssessment": {
            "value": "LIKELY",
            "confidence": 0.618984580039978
          },
          "subject": {
            "value": "PATIENT",
            "confidence": 0.99964696168899536
          },
          "confidence": 0.62128835916519165
        },
        {
          "mentionId": "2",
          "type": "MED_DOSE",
          "text": {
            "content": "5 units",
            "beginOffset": 16
          },
          "confidence": 0.78806477785110474
        },
        {
          "mentionId": "3",
          "type": "MED_ROUTE",
          "text": {
            "content": "IV",
            "beginOffset": 24
          },
          "linkedEntities": [
            {
              "entityId": "UMLS/C0348016"
            }
          ],
          "confidence": 0.8927428126335144
        },
        {
          "mentionId": "4",
          "type": "PROBLEM",
          "text": {
            "content": "diabetes",
            "beginOffset": 52
          },
          "linkedEntities": [
            {
              "entityId": "UMLS/C0011847"
            },
            {
              "entityId": "UMLS/C0011849"
            },
            {
              "entityId": "UMLS/C0241863"
            }
          ],
          "temporalAssessment": {
            "value": "CURRENT",
            "confidence": 0.91680806875228882
          },
          "certaintyAssessment": {
            "value": "LIKELY",
            "confidence": 0.98018729686737061
          },
          "subject": {
            "value": "PATIENT",
            "confidence": 0.99965417385101318
          },
          "confidence": 0.99518013000488281
        }
      ],
      "entities": [
        {
          "entityId": "UMLS/C0011847",
          "preferredTerm": "Diabetes",
          "vocabularyCodes": [
            "ICD10CM/E11",
            "LNC/LA10529-8",
            "LNC/LP128793-9",
            "LNC/MTHU040702",
            "MTH/NOCODE",
            "OMIM/MTHU050182"
          ]
        },
        {
          "entityId": "UMLS/C0011849",
          "preferredTerm": "Diabetes Mellitus",
          "vocabularyCodes": [
            "HPO/HP:0000819",
            "ICD10CM/E08-E13",
            "ICD9CM/250",
            "LNC/LA14291-1",
            "LNC/LA27539-8",
            "LNC/LP74722-7",
            "LNC/MTHU020781",
            "MEDLINEPLUS/4",
            "MSH/D003920",
            "MTH/NOCODE",
            "MTH/U000263",
            "NCI/C2985",
            "OMIM/MTHU036798"
          ]
        },
        {
          "entityId": "UMLS/C0021641",
          "preferredTerm": "Insulin",
          "vocabularyCodes": [
            "FMA/83365",
            "LNC/LA15805-7",
            "LNC/LP14676-8",
            "LNC/LP16325-0",
            "LNC/LP32542-0",
            "LNC/LP70329-5",
            "LNC/MTHU002108",
            "LNC/MTHU019392",
            "MSH/D007328",
            "MTH/NOCODE"
          ]
        },
        {
          "entityId": "UMLS/C0241863",
          "preferredTerm": "Diabetic",
          "vocabularyCodes": [
            "LNC/LA26134-9"
          ]
        },
        {
          "entityId": "UMLS/C0348016",
          "preferredTerm": "Intravenous",
          "vocabularyCodes": [
            "LNC/LA9437-0",
            "LNC/LP32453-0",
            "MTH/NOCODE",
            "NCI/C13346"
          ]
        },
        {
          "entityId": "UMLS/C0795635",
          "preferredTerm": "insulin, regular, human",
          "vocabularyCodes": [
            "LNC/LP17001-6",
            "MSH/D061386",
            "MTH/NOCODE",
            "NCI/C29125",
            "RXNORM/253182",
            "VANDF/4017559",
            "VANDF/4017569",
            "VANDF/4019786"
          ]
        },
        {
          "entityId": "UMLS/C1533581",
          "preferredTerm": "Therapeutic Insulin",
          "vocabularyCodes": [
            "MTH/NOCODE",
            "NCI/C581"
          ]
        },
        {
          "entityId": "UMLS/C3537244",
          "preferredTerm": "Insulins",
          "vocabularyCodes": [
            "MSH/D061385",
            "MTH/NOCODE"
          ]
        },
        {
          "entityId": "UMLS/C3714501",
          "preferredTerm": "Insulin Drug Class",
          "vocabularyCodes": [
            "MTH/NOCODE",
            "VANDF/4021631"
          ]
        }
      ],
      "relationships": [
        {
          "subjectId": "1",
          "objectId": "2",
          "confidence": 0.99964696168899536
        },
        {
          "subjectId": "1",
          "objectId": "3",
          "confidence": 0.99964696168899536
        },
        {
          "subjectId": "4",
          "objectId": "1",
          "confidence": 0.68552839756011963
        }
      ],
      "fhirBundle": "{\n    \"entry\": [\n      {\n        \"fullUrl\": \"urn:uuid:7e6e2323-f9e3-4241-bb84-1a8ff997ef99\",\n        \"request\": {\n          \"method\": \"POST\",\n          \"url\": \"Condition\"\n        },\n        \"resource\": {\n          \"category\": [\n            {\n              \"coding\": [\n                {\n                  \"code\": \"problem-list-item\",\n                  \"display\": \"Problem List Item\",\n                  \"system\": \"http://terminology.hl7.org/CodeSystem/condition-category\"\n                }\n              ]\n            }\n          ],\n          \"clinicalStatus\": {\n            \"coding\": [\n              {\n                \"code\": \"active\",\n                \"system\": \"http://terminology.hl7.org/CodeSystem/condition-clinical\"\n              }\n            ]\n          },\n          \"evidence\": [\n            {\n              \"code\": [\n                {\n                  \"coding\": [\n                    {\n                      \"code\": \"C0011847\",\n                      \"system\": \"http://terminology.hl7.org/CodeSystem/umls\"\n                    },\n                    {\n                      \"code\": \"C0011849\",\n                      \"system\": \"http://terminology.hl7.org/CodeSystem/umls\"\n                    },\n                    {\n                      \"code\": \"C0241863\",\n                      \"system\": \"http://terminology.hl7.org/CodeSystem/umls\"\n                    }\n                  ]\n                }\n              ]\n            }\n          ],\n          \"extension\": [\n            {\n              \"url\": \"temporalrelationship\",\n              \"valueCode\": \"CURRENT\"\n            },\n            {\n              \"url\": \"certaintyassessment\",\n              \"valueCode\": \"LIKELY\"\n            },\n            {\n              \"url\": \"g.co/fhir/StructureDefinition/healthcare_nlp\",\n              \"valueCodeableConcept\": {\n                \"coding\": [\n                  {\n                    \"code\": \"C0011847\",\n                    \"system\": \"http://terminology.hl7.org/CodeSystem/umls\"\n                  },\n                  {\n                    \"code\": \"C0011849\",\n                    \"system\": \"http://terminology.hl7.org/CodeSystem/umls\"\n                  },\n                  {\n                    \"code\": \"C0241863\",\n                    \"system\": \"http://terminology.hl7.org/CodeSystem/umls\"\n                  }\n                ]\n              }\n            },\n            {\n              \"url\": \"source\",\n              \"valueReference\": {\n                \"id\": \"#Document1\"\n              }\n            },\n            {\n              \"url\": \"source_offset\",\n              \"valueInteger\": 52\n            },\n            {\n              \"url\": \"entityconfidence\",\n              \"valueDecimal\": 0.995180\n            }\n          ],\n          \"meta\": {\n            \"source\": \"https://healthcare.googleapis.com/v1alpha2/projects/\u003cPROJECTNAME\u003e/locations/\u003cLOCATION\u003e/services/nlp:analyzeEntities\"\n          },\n          \"resourceType\": \"Condition\",\n          \"subject\": {\n            \"reference\": \"Patient/Patient/\u003cPATIENT_ID\u003e\"\n          },\n          \"text\": {\n            \"div\": \"\u003cdiv xmlns=\\\"http://www.w3.org/1999/xhtml\\\"\u003e\u003cPreferred Term\u003e \u003cOptional: Date\u003e\u003c/div\u003e\",\n            \"status\": \"generated\"\n          },\n          \"verificationStatus\": {\n            \"coding\": [\n              {\n                \"code\": \"confirmed\",\n                \"system\": \"http://terminology.hl7.org/CodeSystem/condition-ver-status\"\n              }\n            ]\n          }\n        }\n      },\n      {\n        \"fullUrl\": \"urn:uuid:04be4df6-4bbc-4fb5-a62f-fb82e644b8d2\",\n        \"request\": {\n          \"method\": \"POST\",\n          \"url\": \"MedicationStatement\"\n        },\n        \"resource\": {\n          \"dosage\": [\n            {\n              \"route\": {\n                \"coding\": [\n                  {\n                    \"code\": \"C0348016\",\n                    \"system\": \"http://terminology.hl7.org/CodeSystem/umls\"\n                  }\n                ]\n              }\n            }\n          ],\n          \"effectivePeriod\": {\n            \"start\": \"2024-02-06T16:55:32+00:00\"\n          },\n          \"extension\": [\n            {\n              \"url\": \"dosage\",\n              \"valueString\": \"5 units\"\n            },\n            {\n              \"url\": \"temporalrelationship\",\n              \"valueCode\": \"UPCOMING\"\n            },\n            {\n              \"url\": \"certaintyassessment\",\n              \"valueCode\": \"LIKELY\"\n            },\n            {\n              \"url\": \"entityconfidence\",\n              \"valueDecimal\": 0.621288\n            }\n          ],\n          \"medicationCodeableConcept\": {\n            \"coding\": [\n              {\n                \"code\": \"C0021641\",\n                \"system\": \"http://terminology.hl7.org/CodeSystem/umls\"\n              },\n              {\n                \"code\": \"C0795635\",\n                \"system\": \"http://terminology.hl7.org/CodeSystem/umls\"\n              },\n              {\n                \"code\": \"C1533581\",\n                \"system\": \"http://terminology.hl7.org/CodeSystem/umls\"\n              },\n              {\n                \"code\": \"C3537244\",\n                \"system\": \"http://terminology.hl7.org/CodeSystem/umls\"\n              },\n              {\n                \"code\": \"C3714501\",\n                \"system\": \"http://terminology.hl7.org/CodeSystem/umls\"\n              }\n            ],\n            \"text\": \"Insulin regimen\"\n          },\n          \"meta\": {\n            \"source\": \"https://healthcare.googleapis.com/v1alpha2/projects/\u003cPROJECTNAME\u003e/locations/\u003cLOCATION\u003e/services/nlp:analyzeEntities\"\n          },\n          \"reasonReference\": [\n            {\n              \"display\": \"7e6e2323-f9e3-4241-bb84-1a8ff997ef99\"\n            }\n          ],\n          \"resourceType\": \"MedicationStatement\",\n          \"status\": \"active\",\n          \"subject\": {\n            \"reference\": \"Patient/Patient/\u003cPATIENT_ID\u003e\"\n          },\n          \"text\": {\n            \"div\": \"\u003cdiv xmlns=\\\"http://www.w3.org/1999/xhtml\\\"\u003e\u003c/div\u003e\",\n            \"status\": \"generated\"\n          }\n        }\n      },\n      {\n        \"fullUrl\": \"urn:uuid:f62fdb4b-a561-4855-96c8-23e41d8ad7b0\",\n        \"request\": {\n          \"method\": \"POST\",\n          \"url\": \"DocumentReference\"\n        },\n        \"resource\": {\n          \"content\": [\n            {\n              \"attachment\": {\n                \"url\": \"\u003cDOC_REFER\u003e\"\n              }\n            }\n          ],\n          \"meta\": {\n            \"source\": \"https://healthcare.googleapis.com/v1alpha2/projects/\u003cPROJECTNAME\u003e/locations/\u003cLOCATION\u003e/services/nlp:analyzeEntities\"\n          },\n          \"resourceType\": \"DocumentReference\",\n          \"status\": \"current\",\n          \"subject\": {\n            \"id\": \"Patient/\u003cPATIENT_ID\u003e\"\n          }\n        }\n      }\n    ],\n    \"resourceType\": \"Bundle\",\n    \"type\": \"transaction\"\n  }"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
