---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/custom-highlights-api/
title: Analyze conversations using Custom Highlights \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:10:44.782250+00:00
---

# Analyze conversations using Custom Highlights  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/custom-highlights-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Analyze conversations using Custom Highlights Stay organized with collections  Save and categorize content based on your preferences. 

## Overview

Custom Highlights functions in a similar way as the [Smart Highlights](https://docs.cloud.google.com/gemini-enterprise-cx/insights/smart-highlights) feature. A **highlight** contains keywords, phrases or sentences that CX Insights recognizes as being important to determining the user's intent. If highlights are present, they are labeled in the returned transcript. Smart Highlights automatically detects highlights based on a range of pre-set scenarios, while Custom Highlights lets you specify custom criteria that should be recognized as highlights.

A custom highlight can be made up of one or more **phrase match rule groups**. A phrase match rule group contains one or more **rules**. You can use the following parameters to customize the behavior of your rules.

### Rules to determine a match

You can specify whether a highlight should be detected if only one of the rule groups resolves to `true`, or if all of the rule groups resolve to `true`. Similarly, you can specify that a rule group should resolve to `true` if only one of its rules is met, or if conditions for all rules in the rule group must be met.

## Create a custom highlight using the Contact Center AI Insights API

### Detect "any of" a list of specified query strings

The following sample creates a [`PhraseMatcher`](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.phraseMatchers#resource:-phrasematcher) object that tells CX Insights to add highlight labels to **either** of two phrases whenever they appear in a conversation. Both phrases don't need to appear in order to be detected as a highlight.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `contactcenterinsights.phraseMatchers.create`



### REST

See the [PhraseMatcherType](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.phraseMatchers#PhraseMatcherType) and [PhraseMatchRuleGroupType](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.phraseMatchers#PhraseMatchRuleGroupType) reference documentation for complete details. Substituting `PHONE` and `CELLPHONE` for the two `query` fields should result in the sample output.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID.
  * DISPLAY_NAME: the human-readible name of the phrase matcher.
  * QUERY: the word or phrase to be matched.

**Note:** All the examples are using the global Customer Experience Insights instance. Refer to [Regionalization](https://docs.cloud.google.com/gemini-enterprise-cx/insights/docs/regionalization) for instructions on using regional instances. 

HTTP method and URL: 
    
    
    POST https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/phraseMatchers

Request JSON body: 
    
    
    {
      "display_name": DISPLAY_NAME,
      "type": "ANY_OF",
      "active": true,
      "phrase_match_rule_groups": {
        "type": "ANY_OF",
        "phrase_match_rules": {
          "query": QUERY
          "config": {
            "exact_match_config": {}
          }
        },
        "phrase_match_rules": {
          "query": QUERY
          "config": {
            "exact_match_config": {}
          }
        }
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/phraseMatchers"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/phraseMatchers" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/us-central1/phraseMatchers/PHRASE_MATCHER_ID",
      "revisionId": "REVISION_ID",
      "revisionCreateTime": "2021-01-20T10:10:10.123000Z",
      "displayName": "PHONE_SERVICE",
      "type": "ANY_OF",
      "active": true,
      "phraseMatchRuleGroups": [
        {
          "type": "ANY_OF",
          "phraseMatchRules": [
            {
              "query": "PHONE",
              "config": {
                "exactMatchConfig": {}
              }
            },
            {
              "query": "CELLPHONE",
              "config": {
                "exactMatchConfig": {}
              }
            }
          ]
        }
      ],
      "activationUpdateTime": "2021-01-20T10:10:10.123000Z"
    }
    

### Python

To authenticate to CX Insights, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import contact_center_insights_v1
    
    
    def create_phrase_matcher_any_of(
        project_id: str,
    ) -> contact_center_insights_v1.PhraseMatcher:
        """Creates a phrase matcher that matches any of the specified queries.
    
        Args:
            project_id:
                The project identifier. For example, 'my-project'.
    
        Returns:
            A phrase matcher.
        """
        # Construct a parent resource.
        parent = (
            contact_center_insights_v1.ContactCenterInsightsClient.common_location_path(
                project_id, "us-central1"
            )
        )
    
        # Construct a phrase matcher that matches any of its rule groups.
        phrase_matcher = contact_center_insights_v1.PhraseMatcher()
        phrase_matcher.display_name = "PHONE_SERVICE"
        phrase_matcher.type_ = (
            contact_center_insights_v1.PhraseMatcher.PhraseMatcherType.ANY_OF
        )
        phrase_matcher.active = True
    
        # Construct a rule group to match the word "PHONE" or "CELLPHONE", ignoring case sensitivity.
        rule_group = contact_center_insights_v1.PhraseMatchRuleGroup()
        rule_group.type_ = (
            contact_center_insights_v1.PhraseMatchRuleGroup.PhraseMatchRuleGroupType.ANY_OF
        )
    
        for word in ["PHONE", "CELLPHONE"]:
            rule = contact_center_insights_v1.PhraseMatchRule()
            rule.query = word
            rule.config.exact_match_config = contact_center_insights_v1.ExactMatchConfig()
            rule_group.phrase_match_rules.append(rule)
        phrase_matcher.phrase_match_rule_groups.append(rule_group)
    
        # Call the Insights client to create a phrase matcher.
        insights_client = contact_center_insights_v1.ContactCenterInsightsClient()
        phrase_matcher = insights_client.create_phrase_matcher(
            parent=parent, phrase_matcher=phrase_matcher
        )
    
        print(f"Created {phrase_matcher.name}")
        return phrase_matcher
    
    

### Java

To authenticate to CX Insights, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.contactcenterinsights.v1.[ContactCenterInsightsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ContactCenterInsightsClient.html);
    import com.google.cloud.contactcenterinsights.v1.[ExactMatchConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ExactMatchConfig.html);
    import com.google.cloud.contactcenterinsights.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.LocationName.html);
    import com.google.cloud.contactcenterinsights.v1.[PhraseMatchRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.PhraseMatchRule.html);
    import com.google.cloud.contactcenterinsights.v1.[PhraseMatchRuleConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.PhraseMatchRuleConfig.html);
    import com.google.cloud.contactcenterinsights.v1.[PhraseMatchRuleGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.PhraseMatchRuleGroup.html);
    import com.google.cloud.contactcenterinsights.v1.[PhraseMatcher](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.PhraseMatcher.html);
    import java.io.IOException;
    
    public class CreatePhraseMatcherAnyOf {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace this variable before running the sample.
        String projectId = "my_project_id";
    
        createPhraseMatcherAnyOf(projectId);
      }
    
      public static [PhraseMatcher](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.PhraseMatcher.html) createPhraseMatcherAnyOf(String projectId) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([ContactCenterInsightsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ContactCenterInsightsClient.html) client = [ContactCenterInsightsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ContactCenterInsightsClient.html).create()) {
          // Construct a phrase matcher that matches any of its rule groups.
          [PhraseMatcher](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.PhraseMatcher.html).Builder phraseMatcher =
              [PhraseMatcher](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.PhraseMatcher.html).newBuilder()
                  .setDisplayName("PHONE_SERVICE")
                  .setTypeValue(2)
                  .setActive(true);
    
          // Construct a rule group to match the word "PHONE" or "CELLPHONE", ignoring case sensitivity.
          [PhraseMatchRuleGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.PhraseMatchRuleGroup.html).Builder ruleGroup = [PhraseMatchRuleGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.PhraseMatchRuleGroup.html).newBuilder().setTypeValue(2);
    
          String[] words = {"PHONE", "CELLPHONE"};
          for (String w : words) {
            [PhraseMatchRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.PhraseMatchRule.html).Builder rule =
                [PhraseMatchRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.PhraseMatchRule.html).newBuilder()
                    .setQuery(w)
                    .[setConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.PhraseMatchRule.Builder.html#com_google_cloud_contactcenterinsights_v1_PhraseMatchRule_Builder_setConfig_com_google_cloud_contactcenterinsights_v1_PhraseMatchRuleConfig_)(
                        [PhraseMatchRuleConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.PhraseMatchRuleConfig.html).newBuilder()
                            .[setExactMatchConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.PhraseMatchRuleConfig.Builder.html#com_google_cloud_contactcenterinsights_v1_PhraseMatchRuleConfig_Builder_setExactMatchConfig_com_google_cloud_contactcenterinsights_v1_ExactMatchConfig_)([ExactMatchConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ExactMatchConfig.html).newBuilder().build())
                            .build());
            ruleGroup.[addPhraseMatchRules](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.PhraseMatchRuleGroup.Builder.html#com_google_cloud_contactcenterinsights_v1_PhraseMatchRuleGroup_Builder_addPhraseMatchRules_com_google_cloud_contactcenterinsights_v1_PhraseMatchRule_)(rule.build());
          }
          phraseMatcher.[addPhraseMatchRuleGroups](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.PhraseMatcher.Builder.html#com_google_cloud_contactcenterinsights_v1_PhraseMatcher_Builder_addPhraseMatchRuleGroups_com_google_cloud_contactcenterinsights_v1_PhraseMatchRuleGroup_)(ruleGroup.build());
    
          // Construct a parent resource.
          [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.LocationName.html) parent = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.LocationName.html).of(projectId, "us-central1");
    
          // Call the Insights client to create a phrase matcher.
          [PhraseMatcher](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.PhraseMatcher.html) response = client.createPhraseMatcher(parent, phraseMatcher.build());
          System.out.printf("Created %s%n", response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.PhraseMatcher.html#com_google_cloud_contactcenterinsights_v1_PhraseMatcher_getName__)());
          return response;
        }
      }
    }
    

### Node.js

To authenticate to CX Insights, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment this variable before running the sample.
     */
    // const projectId = 'my_project_id';
    
    // Imports the Contact Center Insights client.
    const {
      ContactCenterInsightsClient,
    } = require('[@google-cloud/contact-center-insights](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/overview.html)');
    
    // Instantiates a client.
    const client = new [ContactCenterInsightsClient](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/overview.html)();
    
    async function createPhraseMatcherAnyOf() {
      const [phraseMatcher] = await client.createPhraseMatcher({
        parent: client.[locationPath](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/contact-center-insights/v1.contactcenterinsightsclient.html)(projectId, 'us-central1'),
        phraseMatcher: {
          displayName: 'PHONE_SERVICE',
          type: 'ANY_OF',
          active: true,
          phraseMatchRuleGroups: [
            {
              type: 'ANY_OF',
              phraseMatchRules: [
                {
                  query: 'PHONE',
                  config: {
                    exactMatchConfig: {},
                  },
                },
                {
                  query: 'CELLPHONE',
                  config: {
                    exactMatchConfig: {},
                  },
                },
              ],
            },
          ],
        },
      });
      console.info(`Created ${phraseMatcher.name}`);
    }
    createPhraseMatcherAnyOf();

### Detect "all of" a list of specified query strings

The following sample creates a [`PhraseMatcher`](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.phraseMatchers#resource:-phrasematcher) object that tells CX Insights to add highlight labels to conversations that **do** contain the query words in the first [`phraseMatchRuleGroups`](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.phraseMatchers#phrasematchrulegroup) but also **do not** contain the query words in the second ['phraseMatchRuleGroups`](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.phraseMatchers#phrasematchrulegroup).

**Note:** `no (shipping OR delivery)` is equivalent to `(no shipping AND no delivery)`.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `contactcenterinsights.phraseMatchers.create`



### REST

See the [PhraseMatcherType](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.phraseMatchers#PhraseMatcherType) and [PhraseMatchRuleGroupType](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.phraseMatchers#PhraseMatchRuleGroupType) reference documentation for complete details. Substituting `PHONE` and `CELLPHONE` for the two `query` fields and `SHIPPING` and `DELIVERY` for the second two `query` fields should result in the sample output. The sample tells CX Insights to add highlight labels to conversations that contain "phone" and "cellphone" but don't contain "shipping" or "delivery".

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID.
  * DISPLAY_NAME: the human-readible name of the phrase matcher.
  * QUERY: the word or phrase to be matched.

**Note:** All the examples are using the global Customer Experience Insights instance. Refer to [Regionalization](https://docs.cloud.google.com/gemini-enterprise-cx/insights/docs/regionalization) for instructions on using regional instances. 

HTTP method and URL: 
    
    
    POST https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/phraseMatchers

Request JSON body: 
    
    
    {
      "display_name": DISPLAY_NAME,
      "type": "ALL_OF",
      "active": true,
      "phrase_match_rule_groups": {
        "type": "ANY_OF",
        "phrase_match_rules": {
          "query": QUERY
          "config": {
            "exact_match_config": {}
          }
        },
        "phrase_match_rules": {
          "query": QUERY
          "config": {
            "exact_match_config": {}
          }
        },
        "phrase_match_rule_groups": {
          "type": "ALL_OF",
          "phrase_match_rules": {
            "query": QUERY
            "negated": "true"
            "config": {
              "exact_match_config": {}
            }
          },
          "phrase_match_rules": {
            "query": QUERY
            "negated": "true"
            "config": {
              "exact_match_config": {}
            }
          }
        }
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/phraseMatchers"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/phraseMatchers" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/us-central1/phraseMatchers/PHRASE_MATCHER_ID",
      "revisionId": "456456456",
      "revisionCreateTime": "2021-01-20T10:10:10.123000Z",
      "displayName": "NON_SHIPPING_PHONE_SERVICE",
      "type": "ALL_OF",
      "active": true,
      "phraseMatchRuleGroups": [
        {
          "type": "ANY_OF",
          "phraseMatchRules": [
            {
              "query": "PHONE",
              "config": {
                "exactMatchConfig": {}
              }
            },
            {
              "query": "CELLPHONE",
              "config": {
                "exactMatchConfig": {}
              }
            }
          ]
        },
        {
          "type": "ALL_OF",
          "phraseMatchRules": [
            {
              "query": "SHIPPING",
              "negated": true,
              "config": {
                "exactMatchConfig": {}
              }
            },
            {
              "query": "DELIVERY",
              "negated": true,
              "config": {
                "exactMatchConfig": {}
              }
            }
          ]
        }
      ],
      "activationUpdateTime": "2021-01-20T10:10:10.123000Z"
    }
    

### Python

To authenticate to CX Insights, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import contact_center_insights_v1
    
    
    def create_phrase_matcher_all_of(
        project_id: str,
    ) -> contact_center_insights_v1.PhraseMatcher:
        """Creates a phrase matcher that matches all specified queries.
    
        Args:
            project_id:
                The project identifier. For example, 'my-project'.
    
        Returns:
            A phrase matcher.
        """
        # Construct a parent resource.
        parent = (
            contact_center_insights_v1.ContactCenterInsightsClient.common_location_path(
                project_id, "us-central1"
            )
        )
    
        # Construct a phrase matcher that matches all of its rule groups.
        phrase_matcher = contact_center_insights_v1.PhraseMatcher()
        phrase_matcher.display_name = "NON_SHIPPING_PHONE_SERVICE"
        phrase_matcher.type_ = (
            contact_center_insights_v1.PhraseMatcher.PhraseMatcherType.ALL_OF
        )
        phrase_matcher.active = True
    
        # Construct a rule group to match the word "PHONE" or "CELLPHONE", ignoring case sensitivity.
        rule_group_phone_or_cellphone = contact_center_insights_v1.PhraseMatchRuleGroup()
        rule_group_phone_or_cellphone.type_ = (
            contact_center_insights_v1.PhraseMatchRuleGroup.PhraseMatchRuleGroupType.ANY_OF
        )
    
        for word in ["PHONE", "CELLPHONE"]:
            rule = contact_center_insights_v1.PhraseMatchRule()
            rule.query = word
            rule.config.exact_match_config = contact_center_insights_v1.ExactMatchConfig()
            rule_group_phone_or_cellphone.phrase_match_rules.append(rule)
        phrase_matcher.phrase_match_rule_groups.append(rule_group_phone_or_cellphone)
    
        # Construct another rule group to not match the word "SHIPPING" or "DELIVERY", ignoring case sensitivity.
        rule_group_not_shipping_or_delivery = (
            contact_center_insights_v1.PhraseMatchRuleGroup()
        )
        rule_group_not_shipping_or_delivery.type_ = (
            contact_center_insights_v1.PhraseMatchRuleGroup.PhraseMatchRuleGroupType.ALL_OF
        )
    
        for word in ["SHIPPING", "DELIVERY"]:
            rule = contact_center_insights_v1.PhraseMatchRule()
            rule.query = word
            rule.negated = True
            rule.config.exact_match_config = contact_center_insights_v1.ExactMatchConfig()
            rule_group_not_shipping_or_delivery.phrase_match_rules.append(rule)
        phrase_matcher.phrase_match_rule_groups.append(rule_group_not_shipping_or_delivery)
    
        # Call the Insights client to create a phrase matcher.
        insights_client = contact_center_insights_v1.ContactCenterInsightsClient()
        phrase_matcher = insights_client.create_phrase_matcher(
            parent=parent, phrase_matcher=phrase_matcher
        )
    
        print(f"Created {phrase_matcher.name}")
        return phrase_matcher
    
    

### Java

To authenticate to CX Insights, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.contactcenterinsights.v1.[ContactCenterInsightsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ContactCenterInsightsClient.html);
    import com.google.cloud.contactcenterinsights.v1.[ExactMatchConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ExactMatchConfig.html);
    import com.google.cloud.contactcenterinsights.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.LocationName.html);
    import com.google.cloud.contactcenterinsights.v1.[PhraseMatchRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.PhraseMatchRule.html);
    import com.google.cloud.contactcenterinsights.v1.[PhraseMatchRuleConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.PhraseMatchRuleConfig.html);
    import com.google.cloud.contactcenterinsights.v1.[PhraseMatchRuleGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.PhraseMatchRuleGroup.html);
    import com.google.cloud.contactcenterinsights.v1.[PhraseMatcher](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.PhraseMatcher.html);
    import java.io.IOException;
    
    public class CreatePhraseMatcherAllOf {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace this variable before running the sample.
        String projectId = "my_project_id";
    
        createPhraseMatcherAllOf(projectId);
      }
    
      public static [PhraseMatcher](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.PhraseMatcher.html) createPhraseMatcherAllOf(String projectId) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([ContactCenterInsightsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ContactCenterInsightsClient.html) client = [ContactCenterInsightsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ContactCenterInsightsClient.html).create()) {
          // Construct a phrase matcher that matches all of its rule groups.
          [PhraseMatcher](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.PhraseMatcher.html).Builder phraseMatcher =
              [PhraseMatcher](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.PhraseMatcher.html).newBuilder()
                  .setDisplayName("NON_SHIPPING_PHONE_SERVICE")
                  .setTypeValue(1)
                  .setActive(true);
    
          // Construct a rule group to match the word "PHONE" or "CELLPHONE", ignoring case sensitivity.
          [PhraseMatchRuleGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.PhraseMatchRuleGroup.html).Builder ruleGroup1 = [PhraseMatchRuleGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.PhraseMatchRuleGroup.html).newBuilder().setTypeValue(2);
    
          String[] words1 = {"PHONE", "CELLPHONE"};
          for (String w : words1) {
            [PhraseMatchRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.PhraseMatchRule.html).Builder rule =
                [PhraseMatchRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.PhraseMatchRule.html).newBuilder()
                    .setQuery(w)
                    .[setConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.PhraseMatchRule.Builder.html#com_google_cloud_contactcenterinsights_v1_PhraseMatchRule_Builder_setConfig_com_google_cloud_contactcenterinsights_v1_PhraseMatchRuleConfig_)(
                        [PhraseMatchRuleConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.PhraseMatchRuleConfig.html).newBuilder()
                            .[setExactMatchConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.PhraseMatchRuleConfig.Builder.html#com_google_cloud_contactcenterinsights_v1_PhraseMatchRuleConfig_Builder_setExactMatchConfig_com_google_cloud_contactcenterinsights_v1_ExactMatchConfig_)([ExactMatchConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ExactMatchConfig.html).newBuilder().build())
                            .build());
            ruleGroup1.[addPhraseMatchRules](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.PhraseMatchRuleGroup.Builder.html#com_google_cloud_contactcenterinsights_v1_PhraseMatchRuleGroup_Builder_addPhraseMatchRules_com_google_cloud_contactcenterinsights_v1_PhraseMatchRule_)(rule.build());
          }
          phraseMatcher.[addPhraseMatchRuleGroups](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.PhraseMatcher.Builder.html#com_google_cloud_contactcenterinsights_v1_PhraseMatcher_Builder_addPhraseMatchRuleGroups_com_google_cloud_contactcenterinsights_v1_PhraseMatchRuleGroup_)(ruleGroup1.build());
    
          // Construct another rule group to not match the word "SHIPPING" or "DELIVERY",
          // ignoring case sensitivity.
          [PhraseMatchRuleGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.PhraseMatchRuleGroup.html).Builder ruleGroup2 = [PhraseMatchRuleGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.PhraseMatchRuleGroup.html).newBuilder().setTypeValue(1);
    
          String[] words2 = {"SHIPPING", "DELIVERY"};
          for (String w : words2) {
            [PhraseMatchRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.PhraseMatchRule.html).Builder rule =
                [PhraseMatchRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.PhraseMatchRule.html).newBuilder()
                    .setQuery(w)
                    .[setNegated](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.PhraseMatchRule.Builder.html#com_google_cloud_contactcenterinsights_v1_PhraseMatchRule_Builder_setNegated_boolean_)(true)
                    .[setConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.PhraseMatchRule.Builder.html#com_google_cloud_contactcenterinsights_v1_PhraseMatchRule_Builder_setConfig_com_google_cloud_contactcenterinsights_v1_PhraseMatchRuleConfig_)(
                        [PhraseMatchRuleConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.PhraseMatchRuleConfig.html).newBuilder()
                            .[setExactMatchConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.PhraseMatchRuleConfig.Builder.html#com_google_cloud_contactcenterinsights_v1_PhraseMatchRuleConfig_Builder_setExactMatchConfig_com_google_cloud_contactcenterinsights_v1_ExactMatchConfig_)([ExactMatchConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ExactMatchConfig.html).newBuilder().build())
                            .build());
            ruleGroup2.[addPhraseMatchRules](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.PhraseMatchRuleGroup.Builder.html#com_google_cloud_contactcenterinsights_v1_PhraseMatchRuleGroup_Builder_addPhraseMatchRules_com_google_cloud_contactcenterinsights_v1_PhraseMatchRule_)(rule.build());
          }
          phraseMatcher.[addPhraseMatchRuleGroups](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.PhraseMatcher.Builder.html#com_google_cloud_contactcenterinsights_v1_PhraseMatcher_Builder_addPhraseMatchRuleGroups_com_google_cloud_contactcenterinsights_v1_PhraseMatchRuleGroup_)(ruleGroup2.build());
    
          // Construct a parent resource.
          [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.LocationName.html) parent = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.LocationName.html).of(projectId, "us-central1");
    
          // Call the Insights client to create a phrase matcher.
          [PhraseMatcher](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.PhraseMatcher.html) response = client.createPhraseMatcher(parent, phraseMatcher.build());
          System.out.printf("Created %s%n", response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.PhraseMatcher.html#com_google_cloud_contactcenterinsights_v1_PhraseMatcher_getName__)());
          return response;
        }
      }
    }
    

### Node.js

To authenticate to CX Insights, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment this variable before running the sample.
     */
    // const projectId = 'my_project_id';
    
    // Imports the Contact Center Insights client.
    const {
      ContactCenterInsightsClient,
    } = require('[@google-cloud/contact-center-insights](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/overview.html)');
    
    // Instantiates a client.
    const client = new [ContactCenterInsightsClient](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/overview.html)();
    
    async function createPhraseMatcherAllOf() {
      const [phraseMatcher] = await client.createPhraseMatcher({
        parent: client.[locationPath](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/contact-center-insights/v1.contactcenterinsightsclient.html)(projectId, 'us-central1'),
        phraseMatcher: {
          displayName: 'NON_SHIPPING_PHONE_SERVICE',
          type: 'ALL_OF',
          active: true,
          phraseMatchRuleGroups: [
            {
              type: 'ANY_OF',
              phraseMatchRules: [
                {
                  query: 'PHONE',
                  config: {
                    exactMatchConfig: {},
                  },
                },
                {
                  query: 'CELLPHONE',
                  config: {
                    exactMatchConfig: {},
                  },
                },
              ],
            },
            {
              type: 'ALL_OF',
              phraseMatchRules: [
                {
                  query: 'SHIPPING',
                  negated: true,
                  config: {
                    exactMatchConfig: {},
                  },
                },
                {
                  query: 'DELIVERY',
                  negated: true,
                  config: {
                    exactMatchConfig: {},
                  },
                },
              ],
            },
          ],
        },
      });
      console.info(`Created ${phraseMatcher.name}`);
    }
    createPhraseMatcherAllOf();

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
