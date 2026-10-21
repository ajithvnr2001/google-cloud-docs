---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-set-up-project/
title: Set up a project for Vertex AI \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:05:53.886193+00:00
---

# Set up a project for Vertex AI  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-set-up-project/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Set up a project for Vertex AI Stay organized with collections  Save and categorize content based on your preferences. 

This page guides you through how to set up a project to run Vertex AI services on Google Distributed Cloud (GDC) air-gapped. It includes steps for configuring your development environment with the gdcloud CLI, the trust bundle certificate authority (CA), and your service accounts, so you can begin integrating machine learning into your applications and workflows.

This page is for application developers within application operator groups who are responsible for optimizing air-gapped applications and workflows with AI features. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Ask an administrator to set up a project for you

Most tasks to set up a project require platform administrator access. An administrator must determine a meaningful project name and project ID to identify the project. If you are part of an organization or plan to create multiple projects, consider what naming conventions and entities are recognized on Distributed Cloud. For more information, see [Resource hierarchy](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/resource-hierarchy).

If you lack the necessary permissions, ask your administrator to set up the project on your behalf.

Set up a project by following the instructions in this document.

**Note:** Certain tasks in Vertex AI require that you use additional Distributed Cloud components besides Vertex AI. For example, online predictions use Distributed Cloud storage buckets to store artifacts such as datasets and models. Also, to track costs for projects, you require a billing account. You might need to perform additional setup tasks and obtain additional roles to use other Distributed Cloud components.

## Before you begin

To get the permissions that you need to create a project and configure service accounts, ask your Organization IAM Admin or Project IAM Admin to grant you the following roles in your project namespace:

  * To create a project, obtain the Project Creator (`project-creator`) role.
  * To create service accounts, obtain the Project IAM Admin (`project-iam-admin`) role.



For information about these roles, see [Prepare IAM permissions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-ao-permissions). To learn how to grant permissions to a subject, see [Grant and revoke access](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/set-up-role-bindings).

Then, [create a project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-a-project) to group your Vertex AI services together. [Ensure that billing is enabled for your Distributed Cloud project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/billing/manage-billing-accounts).

## Install the gdcloud CLI

To activate Distributed Cloud services and gain access to tools and components, install the gdcloud CLI.

Follow these steps to install the gdcloud CLI:

  1. [Download the gdcloud CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-download).
  2. Initialize the gdcloud CLI:
         
         gdcloud init
         

For more information, see [Install the gdcloud CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-install).

  3. Authenticate with gdcloud CLI:
         
         gdcloud auth login
         

For more information about how to authenticate with your configured identity provider and get a kubeconfig file for your user identity and Kubernetes cluster, see [the gdcloud CLI authentication](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-auth).




## Set up service accounts

Service accounts, also referred to as service identities, play a crucial role in managing your Vertex AI services. They are the accounts that your workloads use to access Vertex AI services and AI models and make authorized API calls programmatically. For example, service accounts can manage your Vertex AI Workbench notebook to transcribe audio files using the Speech-to-Text API. Similar to a user account, service accounts can be granted permissions and roles, providing a secure and controlled environment, but they can't sign in like a human user.

You can set up service accounts for Vertex AI services by specifying the name of your service account, your project ID, and the name of a JSON file for key pairs.

To learn more about how to create a service account, assign role bindings to it, and create and add key pairs, see [Manage service accounts](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/service-identities).

Follow these steps to set up service accounts using the gdcloud CLI:

  1. Create a service account:
         
         gdcloud iam service-accounts create SERVICE_ACCOUNT --project=PROJECT_ID
         

Replace the following:

     * `SERVICE_ACCOUNT`: the name of the service account. The name must be unique within the project namespace.
     * `PROJECT_ID`: the project ID where you want to create the service account. If `gdcloud init` is already set, then you can omit the `--project` flag.
  2. Create the application default credentials JSON file and the public and private key pairs:
         
         gdcloud iam service-accounts keys create APPLICATION_DEFAULT_CREDENTIALS_FILENAME \
             --project=PROJECT_ID \
             --iam-account=SERVICE_ACCOUNT \
             --ca-cert-path=CA_CERTIFICATE_PATH
         

Replace the following:

     * `APPLICATION_DEFAULT_CREDENTIALS_FILENAME`: the name of the JSON file, such as `my-service-key.json`.
     * `PROJECT_ID`: the project to create the key for.
     * `SERVICE_ACCOUNT`: the name of the service account to add the key for.
     * `CA_CERTIFICATE_PATH`: an optional flag for the path to the certificate authority (CA) certificate that verifies the authentication endpoint. If you don't specify this path, the system CA certificates are used. You must install the CA in the system CA certificates.

Distributed Cloud adds the public key to the service account keys you use to verify the JSON web tokens (JWT) that the private key signs. The private key is written to the application default credentials JSON file.

  3. Grant the service account access to project resources by assigning a role binding. The name of the role depends on the Vertex AI service you want to use the service account for.
         
         gdcloud iam service-accounts add-iam-policy-binding \
             --project=PROJECT_ID \
             --iam-account=SERVICE_ACCOUNT \
             --role=ROLE
         

Replace the following:

     * `PROJECT_ID`: the project to create the role binding in.
     * `SERVICE_ACCOUNT`: the name of the service account to use.
     * `ROLE`: the predefined role to assign to the service account. Specify roles in the format `Role/name` where _Role_ is the Kubernetes type, such as `Role` or `ProjectRole`, and _name_ is the Kubernetes resource name of the predefined role. For example, the following are roles that you can assign to service accounts to use some of the Vertex AI pre-trained APIs:

       * To assign the AI OCR Developer (`ai-ocr-developer`) role, set the role to `Role/ai-ocr-developer`.
       * To assign the AI Speech Developer (`ai-speech-developer`) role, set the role to `Role/ai-speech-developer`.
       * To assign the AI Translation Developer (`ai-translation-developer`) role, set the role to `Role/ai-translation-developer`.
**Note:** To learn more about predefined roles and the names you must assign depending on the Vertex AI service or model you want to use, see [Prepare IAM permissions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-ao-permissions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
