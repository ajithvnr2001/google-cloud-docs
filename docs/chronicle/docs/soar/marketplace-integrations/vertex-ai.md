---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/vertex-ai/
title: Integrate Vertex AI with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:54:07.010154+00:00
---

# Integrate Vertex AI with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/vertex-ai/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Vertex AI with Google SecOps

This document explains how to integrate Vertex AI with Google Security Operations.

**Note:** The Vertex AI integration works with any generally available (GA) model accessible using the Vertex AI API endpoint. 

**Important:** We strongly recommend using only GA models in production environments. Models in Preview may have instability, breaking changes, or limited support.

This integration supports a wide range of the following models, including:

  * **Foundation Models:** View a catalog of pre-trained models in [Vertex AI Model Garden](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-garden/explore-models). 
  * **Third-Party Models:** For a specific list of supported partner models, see the available [Vertex AI partner models](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/partner-models/use-partner-models). 
  * **Open-Source Models:** For a specific list of supported open-source models, see the available [Vertex AI open-source models](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-garden/available-models). 
  * **Fine-Tuned Models:** Use fine-tuned versions to customize models for your specific needs. For more information, see [tuning models](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/tune-models). 
  * **Custom-Trained Models:** Use models you've built and trained. For details on how to use your own models with Vertex AI, see [custom training](https://docs.cloud.google.com/vertex-ai/docs/training/overview). 



## Use cases

The **Vertex AI** integration supports the following use cases:

  * **Automated malicious email analysis** : Analyze raw EML files to extract threat levels, identify phishing links or social engineering indicators, and recommend verification steps.

  * **Contextual entity enrichment** : Generate natural language summaries of security entities to accelerate investigator comprehension during triage.

  * **Flexible playbook orchestration** : Run unstructured generative text prompts inside playbooks to assist with predictive defense or complex security analysis.

  * **Custom data transformation** : Automate programmatic transformations of arbitrary JSON data structures using natural language instructions.




## Before you begin

Before you configure the **Vertex AI** integration in Google SecOps, complete the following prerequisite steps:

  1. Create a service account.

  2. Grant the necessary Identity and Access Management roles to your service account.

  3. Choose and configure one of the following authentication methods:

     * **Option 1:Workload Identity (recommended)**: This method uses short-lived tokens using service account impersonation.

     * **Option 2:Service account JSON key**: This method relies on a static, long-lived secret key file.




For detailed information regarding service charges, review [Vertex AI pricing](https://docs.cloud.google.com/vertex-ai/generative-ai/pricing).

### Create a service account

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts**.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Click **add Create service account**.

  3. Provide a name and description, and click **Done**. Note the service account's **Email address**.




### Grant IAM roles

To allow the integration to interact with platform services, you must grant permissions to your principal. 

  1. In the Google Cloud console, go to **IAM**.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Find your service account and click **Edit principal** (edit).

  3. Click **Add another role** and select **Vertex AI User** (`roles/aiplatform.user`).

  4. Click **Save**.




### Configure Workload Identity credentials

Workload Identity is the recommended approach because it uses short-lived access tokens using service account impersonation.

#### Identify the unique instance identity

Establishing a connection requires granting your Google SecOps instance permission to impersonate your service account.

  1. In Google SecOps, go to **Content Hub > Response Integrations**.

  2. Select the **Vertex AI** integration and enter your service account email in **Workload Identity Email**.

  3. Click **Save > Test**. The test is expected to fail.

  4. Click close_small next to the **Test** button and locate the identity email beginning with `gke-init-python@...` or `soar-python@...`.

  5. Copy this unique email address.




#### Authorize the instance identity in Google Cloud

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts**.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Select the target service account and go to **Permissions > Grant Access**.

  3. Paste the unique email address into **New principals** and assign the **Service Account Token Creator** role (`roles/iam.serviceAccountTokenCreator`).




### Configure a JSON key

Static, long-lived secret key files require manual rotation. Only use this method if Workload Identity authentication is unavailable.

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts** and select your service account.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Go to the **Keys** tab and click **Add key > Create new key**.

  3. Select **JSON** and click **Create**. The browser downloads the JSON file to your computer.




## Integration parameters

The **Vertex AI** integration requires the following parameters:

Parameter | Description  
---|---  
`API Root` | Required. The API root of the Vertex AI instance. The default value is `https://LOCATION-aiplatform.googleapis.com`.  
`Workload Identity Email` | Optional. The client email address of your service account. Only configure this parameter if you're authenticating using a Workload Identity. If configured, `Service Account JSON File Content` is ignored.  
`Service Account JSON File Content` | Optional. The full content of the service account key JSON file. Configure this parameter for service account key authentication.  
`Project ID` | Optional. The project ID to target in Pub/Sub. If no value is provided, the integration retrieves the ID from the service account credentials.  
`Default Model` | Optional. The name of the default model to target. The default value is `gemini-1.5-flash-002`.  
`Location` | Optional. The location ID for the Vertex AI API. If no value is provided, the integration extracts the location ID from the API root.  
`Verify SSL` | Required. Validates the SSL certificate for the connection to the server. Enabled by default.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Analyze EML

**Preview:** This action is in preview.

Use the **Analyze EML** action to analyze EML files using Vertex AI. This action submits every file individually.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Analyze EML** action requires the following parameters:

Parameter | Description  
---|---  
`Model ID` | _Optional_ The ID of the model to use, such as `gemini-1.5-flash-002`.  
`Temperature` | _Optional_ The value to control the degree of randomness in a token selection. This parameter accepts `float` data type values.For more information about temperature values, see [Experiment with the parameter values](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/adjust-parameter-values#temperature).  
`Files To Analyze` | _Required_ A comma-separated list of EML files to submit for analysis.  
`Max Output Tokens` | _Optional_ The maximum number of output tokens to generate in every response.A token is approximately four characters. 100 tokens correspond to roughly 60-80 words. This limit applies to every individual entity.For more information, see [Experiment with parameter values](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/adjust-parameter-values#max-output-tokens).The default value is `100`.  
  
#### Action outputs

The **Analyze EML** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Analyze EML** action:
    
    
    [{
       "Entity": "file",
       "EntityResult": {
           "raw": "{\"threat_level\": \"High\", \"threats_found\": [{\"threat\": \"Phishing Links\", \"explanation\": \"Multiple links point",
           "extracted_info": {
               "threat_level": "High",
               "threats_found": [
                   {
                       "threat": "Phishing Links",
                       "explanation": "Multiple links point to example.com, a suspicious domain likely used for phishing campaigns.",
                       "example": "URL"
                   },
                   {
                       "threat": "Social Engineering",
                       "explanation": "The email uses urgency and scarcity tactics, pressuring the recipient to click links quickly.",
                       "example": "Register Now and Save $1,000 on all 2-Day Project Management (Fundamentals)"
                   },
                   {
                       "threat": "Suspicious Domain",
                       "explanation": "The email uses the domain example.com', which is not commonly associated with legitimate businesses or organizations and may be a newly registered domain for malicious purposes. This should be checked for validity and legitimacy. The email also uses the domain pdu-xl.com which may also be suspicious.",
                       "example": "example.com"
                   }
               ],
               "verification_steps": [
                   "Check the domain reputation of example.com using online tools like VirusTotal or URLVoid.",
                   "Analyze email headers to identify the true sender's IP address and location using email analysis tools.",
                   "Verify the legitimacy of mentioned products or services by independently contacting the companies mentioned."
               ],
               "protection_measures": [
                   "Avoid clicking links in suspicious emails. Hover over links to check the actual URL in a separate tool.",
                   "Enable email filtering and anti-phishing features in your email client.",
                   "Regularly update your antivirus and anti-malware software.",
                   "Educate users about social engineering tactics and phishing schemes."
               ]
           },
           "usageMetadata": {
               "promptTokenCount": 12,
               "candidatesTokenCount": 778,
               "totalTokenCount": 790
           }
       }
    }]
    

##### Output messages

The **Analyze EML** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully analysed the following EML files using Vertex AI: FILE_PATHS` | The action succeeded.  
`Error executing action "Analyze EML". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Analyze EML** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Describe Entity

**Preview:** This action is in preview.

Use the **Describe Entity** action to summarize information about entities using Vertex AI.

This action runs on all Google SecOps entities and submits every entity individually.

#### Action inputs

The **Describe Entity** action requires the following parameters:

Parameter | Description  
---|---  
`Model ID` | _Optional_ The ID of the model to use, such as `gemini-1.5-flash-002`.  
`Temperature` | _Optional_ The value to control the degree of randomness in a token selection. This parameter accepts `float` data type values.For more information about temperature values, see [Experiment with the parameter values](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/adjust-parameter-values#temperature).  
`Exclude Fields` | _Optional_ A comma-separated list of the Google SecOps entity metadata fields to exclude during the entity summary generation.  
`Force Refresh` | _Optional_ If selected, the action ignores the `Refresh After (Days)` parameter and hash validation and regenerates the entity summary for every action run.Not selected by default.  
`Refresh After (Days)` | _Required_ The number of days for the action to wait before refreshing the entity summary.The action generates a hash value that is based on all inputs that are sent Vertex AI excluding values from the `Fields To Ignore` parameter. If the hash value has changed, the action refreshes the summary after the set number of days. If the hash value didn't change, the action doesn't refresh the summary even if the `Refresh After (Days)` parameter value is earlier than the latest summary generation time.The action validates the hash value of the latest actual generated summary and ignores the cached hash value. The default value is `30`.  
`Max Output Tokens` | _Optional_ The maximum number of output tokens to generate in every response.A token is approximately four characters. 100 tokens correspond to roughly 60-80 words. This limit applies to every individual entity.For more information, see [Experiment with parameter values](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/adjust-parameter-values#max-output-tokens).  
  
#### Action outputs

The **Describe Entity** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Describe Entity** action:
    
    
    [
        {
            "Entity": "1B16D64CE18772B8F77C74C3D4DC24AA066BB117",
            "EntityResult": {
                "summary": "This is a suspicious, enriched, internal file hash (SHA1: 1B16D64CE18772B8F77C74C3D4DC24AA066BB117) identified as a Microsoft Excel 2007+ file (\"FC090000\") located on a user's desktop.  VirusTotal analysis shows 3 malicious flags out of 65 total engines.  The file contains macros, is potentially obfuscated, and exhibits behaviors like writing to files, running DLLs, and downloading content.  It was last modified on 2024-11-13 and created on 2021-07-07.  The file is linked to a single case (\"potential_apt_doc_files\") which was closed.  The file is flagged as an artifact but not vulnerable or a pivot point.\n",
                "usageMetadata": {
                    "promptTokenCount": 12,
                    "candidatesTokenCount": 778,
                    "totalTokenCount": 790
                }
            }
        }
    ]
    

##### Output messages

The **Describe Entity** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully summarized the entity based on the available information using Vertex AI.` | The action succeeded.  
`Error executing action "Describe Entity". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Describe Entity** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Execute Prompt

**Preview:** This action is in preview.

Use the **Execute Prompt** action to execute individual text prompts using Vertex AI.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Execute Prompt** action requires the following parameters:

Parameter | Description  
---|---  
`Model ID` | _Optional_ The ID of the model to use, such as `gemini-1.5-flash-002`.  
`Text Prompt` | _Required_ The text instructions to include in the prompt.  
`Temperature` | _Optional_ The value to control the degree of randomness in a token selection. This parameter accepts `float` data type values.For more information about temperature values, see [Experiment with the parameter values](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/adjust-parameter-values#temperature).  
`Candidate Count` | _Optional_ The number of response variations to return in every action run.For every request, the billing applies to an input token once and every output token of all generated candidates.  
`Response MIME Type` | _Optional_ The media (MIME) type of the output response for the generated candidate text.The response media (MIME) type is available for the following models: `gemini-1.5-pro`, `gemini-1.5-flash`.The possible values are as follows:

  * `application/json`
  * `text/plain`
  * `text/x.enum`

The default value is `text/plain`.  
`Response Schema` | _Optional_ The schema for the generated candidate text to follow.To use this parameter, configure the `Response MIME Type` parameter.The response schema is available for the following models: `gemini-1.5-pro`, `gemini-1.5-flash`.   
`Max Input Tokens` | _Optional_ The maximum number of input tokens to submit. One token consists of up to four characters. 100 tokens can correspond to 60-80 words.If you don't set a value, the action executes any prompt. If the number of tokens exceeds the configured maximum number, the action fails.  
`Max Output Tokens` | _Optional_ The maximum number of output tokens to generate in every response.A token is approximately four characters. 100 tokens correspond to roughly 60-80 words. This limit applies to every individual entity.For more information, see [Experiment with parameter values](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/adjust-parameter-values#max-output-tokens).  
  
#### Action outputs

The **Execute Prompt** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Execute Prompt** action:
    
    
    {
      "candidates": [
        {
          "content": {
            "role": "model",
            "parts": [
              {
                "text": "Responding to a malicious email requires a layered approach.  Here's a breakdown of remediation steps, prioritizing actions based on urgency:\n\n**Immediate Actions (within minutes):**\n\n1. **Do NOT click any links or open any attachments.** This is paramount.  Malicious links can download malware, and attachments can contain viruses or exploits.\n\n2. **Disconnect from the internet (if possible).** This limits the damage the malware can do if it's already on your system.  Unplug your ethernet cable or turn off Wi-Fi.\n\n3. **Close the email immediately.** Don't even hover over links or attachments; the preview might be enough to trigger some malware.\n\n**Investigative Actions (within hours):**\n\n4. **Check your email account for unauthorized access.**  Look for unfamiliar sent emails, changed settings (like forwarding rules), or new accounts added.\n\n5. **Run a full system scan with your antivirus software.**  Ensure your antivirus definitions are up-to-date before running the scan.  Consider a second opinion scan with a different reputable antivirus program.\n\n6. **Review your computer's processes (Task Manager on Windows, Activity Monitor on macOS).** Look for unfamiliar processes consuming significant resources.  This could indicate malware activity.\n\n7. **Check your network connections.**  See if any unauthorized connections exist.\n\n8. **Change your email password immediately.** Use a strong, unique password.  Consider using a password manager.\n\n9. **If you clicked a link or opened an attachment, consider the potential impact.** Did you enter credentials?  Did you download a file?  The severity of action needed depends on this.\n\n**Remediation Actions (within days):**\n\n10. **Contact your IT department or security professional.**  They can provide expert guidance and assist with more advanced remediation steps.\n\n11. **Consider more advanced malware scanning tools.**  There are specialized tools that can detect malware missed by standard antivirus.\n\n12. **Review your operating system's security settings.**  Ensure firewalls are enabled and that other security features are adequately configured.\n\n13. **Report the malicious email to your email provider.** This helps them remove the email and prevent others from being affected. You can often do this by forwarding the email to an abuse reporting address provided by your provider.  Report it to the appropriate authorities if you suspect the email involves a crime.\n\n14. **Monitor your accounts and financial records for suspicious activity.**  Phishing emails often aim to steal credentials and financial information.\n\n**Preventive Actions (ongoing):**\n\n15. **Implement strong email filtering.** Use spam filters and configure your email provider's security settings to block suspicious emails.\n\n16. **Train yourself and others to identify phishing emails.**  Be wary of emails with unusual addresses, grammatical errors, urgent requests, or suspicious attachments.\n\n17. **Keep your software up to date.** Regularly update your operating system, applications, and antivirus software.\n\n18. **Use strong, unique passwords for all accounts.**  A password manager can assist with this.\n\n19. **Enable two-factor authentication (2FA) wherever possible.** This adds an extra layer of security to your accounts.\n\n\n**If you suspect your personal data or financial information has been compromised:**\n\n* **Contact your bank and credit card companies immediately.**  Report any suspicious transactions and consider placing a fraud alert on your accounts.\n* **Consider credit monitoring services.**  This can help you detect and respond to identity theft.\n\n\nThe severity of the remediation steps depends on the nature of the malicious email and what actions you took in response to it. If you're unsure about any step, err on the side of caution and seek professional help.\n"
              }
            ]
          },
          "finishReason": "STOP",
          "avgLogprobs": -0.4171245741660307
        }
      ],
      "usageMetadata": {
        "promptTokenCount": 12,
        "candidatesTokenCount": 778,
        "totalTokenCount": 790
      },
      "modelVersion": "gemini-1.5-flash-002",
    "Text_context": ""
    "extracted_info": ""
    }
    

##### Output messages

The **Execute Prompt** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully executed a prompt.` | The action succeeded.  
`Error executing action "Execute Prompt". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Execute Prompt** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Ping

Use the **Ping** action to test the connectivity to Vertex AI.

This action doesn't run on Google SecOps entities. 

#### Action inputs

None.

#### Action outputs

The **Ping** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Ping** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully connected to Vertex AI with the provided connection parameters!` | The action succeeded.  
`Failed to connect to Vertex AI. The API root that you provided doesn't match the following expected pattern: "https://((\w|-)+)-aiplatform.googleapis.com". Check the spelling.` `Failed to connect to Vertex AI! The error is ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Transform Data

**Preview:** This action is in preview.

Use the **Transform Data** action to perform data transformations using Vertex AI.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Transform Data** action requires the following parameters:

Parameter | Description  
---|---  
`Model ID` | _Optional_ The ID of the model to use, such as `gemini-1.5-flash-002`.  
`Text Prompt` | _Required_ The text instructions to include in the prompt.  
`Temperature` | _Optional_ The value to control the degree of randomness in a token selection. This parameter accepts `float` data type values.For more information about temperature values, see [Experiment with the parameter values](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/adjust-parameter-values#temperature).  
`JSON Object` | _Required_ The JSON object to use as an action input.  
`Max Output Tokens` | _Required_ The maximum number of output tokens to generate in every response.A token is approximately four characters. 100 tokens correspond to roughly 60-80 words. This limit applies to every individual entity.For more information, see [Experiment with parameter values](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/adjust-parameter-values#max-output-tokens).The default value is `100`.  
  
#### Action outputs

The **Transform Data** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Transform Data** action:
    
    
    {
      "candidates": [
        {
          "content": {
            "role": "model",
            "parts": [
              {
                "text": "Respondo it. If you're unsure about any step, err on the side of caution and seek professional help.\n"
              }
            ]
          },
          "finishReason": "STOP",
          "avgLogprobs": -0.4171245741660307
        }
      ],
      "usageMetadata": {
        "promptTokenCount": 12,
        "candidatesTokenCount": 778,
        "totalTokenCount": 790
      },
      "modelVersion": "gemini-1.5-flash-002",
    "Text_context": ""
    "extracted_info": ""
    }
    

##### Output messages

The **Transform Data** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully transformed provided data.` | The action succeeded.  
`Error executing action "Transform Data". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Transform Data** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
