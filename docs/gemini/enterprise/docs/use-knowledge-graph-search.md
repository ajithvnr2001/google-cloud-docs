---
url: https://docs.cloud.google.com/gemini/enterprise/docs/use-knowledge-graph-search/
title: Knowledge Graph: Powering intelligent and context-aware search \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:11:07.090052+00:00
---

# Knowledge Graph: Powering intelligent and context-aware search  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/use-knowledge-graph-search/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Knowledge Graph: Powering intelligent and context-aware search Stay organized with collections  Save and categorize content based on your preferences. 

Knowledge Graph enhances Gemini Enterprise by linking data across three core pillars: **people** , **content** , and **interactions**. Knowledge Graph improves search quality and experience by understanding the relationship between different instances and entities in your corpus, providing deeper, context-aware search.

Knowledge Graph enhances search capabilities by:

  * Enriching people-related data with organizational context, including derived reporting lines and relationships to other entities.
  * Improving entity recognition, relationships, and intent understanding to discover more insights from user queries.
  * Improving search responses with precise, context-driven data, making it easier for users to locate relevant people and organizational information.



## Supported data sources for Knowledge Graph

Knowledge Graph is available for apps that have the following data sources:

  * [People data sources](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-people)
  * [People using custom connector](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-people-custom)
  * [Microsoft Entra ID](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/entra-id/connect-entra-id)
  * [Jira Cloud](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-cloud)
  * [Jira Data Center](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-dc)
  * [SharePoint Cloud](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-sharepoint)



## Before you begin

To use Knowledge Graph features, you **must** first connect people data to the Knowledge Graph by configuring a [People connector](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-people). Without connecting people data, these features don't function properly.

People data powers key Knowledge Graph capabilities, including the following:

  * Entity resolution
  * Context understanding
  * Personalization
  * Autocomplete
  * Recommendations



### Supported sources for people data

Each app can have only one people connector. However, you can set up different people connectors for different apps. Choose a data source based on your identity system:

  * If your organization uses Google Cloud Identity, use the [Advanced Google Identity connector](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-people).

  * If you are using the [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation), select the corresponding third-party sources or native sources.




Gemini Enterprise supports the following options for ingesting people's data into the Knowledge Graph:

  * Workspace sources

The Advanced Google Identity connector syncs people data from Google Workspace, directly copying into the Gemini Enterprise index. By copying data into the index, this connector enables full Knowledge Graph functionality, including natural language processing (NLP). The [Advanced Google Identity connector](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-people) is _cloud-native_ and behaves similarly to the Advanced Drive connector by persisting data in the index.

When the connector is active, you must:

    1. Unlink the existing **People Search** data store if it is in use.
    2. Add the new data store to your engine.
  * Native sources

Custom people connector lets you to upload people data from BigQuery or Cloud Storage using a Google-specified schema. This is ideal for organizations with custom or hybrid identity sources.

  * Third-party sources

Gemini Enterprise supports third-party identity providers to ingest people data. For more information see [Workforce Identity Federation for third-party identity providers](https://docs.cloud.google.com/gemini/enterprise/docs/configure-identity-provider#workforce-id-fed-for-third-party-idps).




## About query annotation with Knowledge Graph

Query annotation with Knowledge Graph enhances search query understanding by associating structured data with search terms. This process improves the accuracy and relevance of search results by leveraging contextual insights from the Knowledge Graph.

Unlike standalone information panels, query annotation functions independently by enriching search queries with metadata, allowing for more precise entity detection, entity linking, and user context understanding. When you enter a search term, the Knowledge Graph helps categorize and interpret the query based on its relationship to people, organizations, issues, or other entities.

The key components of query annotation include:

  * **Mention detection** : Identifies key entities (for example, people) and relationships (for example, manager) in a search query and associates them with structured data.

  * **User context understanding** : Analyzes the context of the user and retrieves related user signals (for example, top coworkers) to refine search relevance.

  * **Entity linking** : Resolves ambiguities by linking terms to their most relevant entities (for example, distinguishing between "Apple" as a company versus a fruit).




## Knowledge Graph panels

After the knowledge graph is enabled, the search engine integrates the enriched panels into search results, delivering more precise, context-driven information to help users quickly find relevant people, roles, and organizations. When you perform a search, the `search` API responds with detailed panels that provide additional context and insights related to the search query.

The following panel types appear on the search results page, enhancing your ability to identify relevant entities.

  * **People panel** : This panel includes information such as the person's job title, department, and relationships to other people (for example, management chain, direct reports, and teammates). It helps you to quickly find relevant people and their roles within the organization. The People panel is enhanced with Knowledge Graph and people are displayed as long-form cards, providing a comprehensive view of the person's role and relationships within the organization. The Knowledge Graph search API response includes enriched data panels in a unified, one-box search format. The People panel contains job title, department, and related people information (such as management chain, direct reports, or teammates with the same managers). The Knowledge Graph-derived fields are returned in `derived_struct_data` within the People panel result.

  * **Organization panel** : This panel provides key details about the organization, such as its name, description, and website information. The Knowledge Graph search API response includes enriched data panels in a unified, one-box search format. The Organization panel displays organization name, description, and website information.The Organization results are returned in the `knowledge_graph_results` field within the Organization panel result.


**Note:** Security is maintained by applying access control lists (ACL) checks to ensure users see only authorized Knowledge Graph entities.

## Knowledge Graph configurations

Knowledge Graph enhances search results by integrating enriched panels with precise, context-driven information from internal and external data sources.

### Types of Knowledge Graphs

There are two types of Knowledge Graphs:

  * **Google Cloud Knowledge Graph** : Expands search results by incorporating external data sources. This broadens the scope of search results and enhances relevance with additional insights. Google Cloud Knowledge Graph is only available on apps set to the **Global** location.

  * **Private Knowledge Graph** : Leverages internal organizational data to generate enriched search results. It improves relevance by incorporating proprietary knowledge, such as relationships, roles, and job titles, and provides more contextually accurate query annotations.




### Change Knowledge Graph configurations

Knowledge Graph configurations are enabled for all Gemini Enterprise apps. Before making changes, you can see the impact on search results as follows:

Configuration | Enabled | Disabled  
---|---|---  
**Google Cloud Knowledge Graph** | Expands search with external data. | Limits search to internal data.  
**Private Knowledge Graph** | Enhances search with internal data. | Removes internal derived data.  
  
To modify Knowledge Graph configurations, see the Manage Knowledge Graph configuration section.

### Private Knowledge Graph structure and mapping

The private Knowledge Graph uses a property graph data model. It is designed for enterprise use cases and supports specific types of entities and relationships. You can retrieve the data from documents imported through supported connectors. The private Knowledge Graph uses internal rules to:

  1. Map data from the original data store schema to entity properties.
  2. Create relationships between entities by linking identifiers.



The Knowledge Graph engine constructs its graph by applying these internal rules to all documents from the supported connectors.

#### Knowledge Graph entity types and relationships

Knowledge Graph entity types | Knowledge Graph relationship types | Connectors supported  
---|---|---  
Person | Manager | Workspace sources → People search  
| Dotted-line report | People using custom connector  
  
#### Mapping from data source schema to entity properties

Source document field | Notes  
---|---  
`name.familyName`, `name.givenName`, `name.displayName` | A concatenation of `givenName` and `familyName`. If empty, use `displayName`.  
`personId` | Used to uniquely identify a person.  
`employeeId` | -  
`employmentStatus` | -  
`organizations[0].jobTitle` | The job title in the first element of organizations (array).  
`websites[0].value` | The first value of the websites (array).  
`topCoworkers` | -  
  
## Lifecycle of the Knowledge Graph

The Knowledge Graph for your engine goes through several states as it is enabled, updated, and managed. Understanding the following states helps you know what to expect and what actions are available to you.

  * `unspecified`

The Knowledge Graph is not enabled for the engine or is pending initialization. To enable it, you must configure the `knowledge_graph_config.enable_private_knowledge_graph` setting to `true`.

  * `initialization`

The initial Knowledge Graph construction is running. During this state, the Knowledge Graph is not available for processing.

While in the `initialization` state:

    * You cannot enable or disable the Knowledge Graph.
    * You cannot delete the engine.
    * Changes from linking or unlinking Knowledge Graph-supported data stores are not immediately reflected in the graph. For more information, see the supported data sources for Knowledge Graph.
  * `active`

The Knowledge Graph is reliable and actively serving. This is the selected state for a functional Knowledge Graph.

  * `batch_update`

The Knowledge Graph is updating to incorporate recent changes from its source data. A change in the supported data source for the Knowledge Graph, or a periodic synchronization between the Knowledge Graph and its supported data source, triggers this action. The Knowledge Graph remains active, but it is potentially out of sync with the changed source data because the updates are still in progress.

While in the `batch_update` state:

    * You cannot enable or disable the Knowledge Graph.
    * You cannot delete the engine.
    * Changes from linking or unlinking Knowledge Graph-supported data stores are subject to delayed reflection in the graph. For more information, see the supported data sources for Knowledge Graph.
  * `deleting`

The Knowledge Graph is disabled for the engine and is being deleted. The Knowledge Graph is not available for processing.

While in the `deleting` state:

    * You cannot enable or disable the Knowledge Graph.
    * You cannot delete the engine.

**Note:** The current Knowledge Graph state does not reflect the availability or quality of your data. For example, a Knowledge Graph can be in the `active` state even if it is empty because it lacks supported data sources.

## Manage Knowledge Graph configuration

You can manage configurations using the console or API.

Before you begin:

  1. You must have created a Gemini Enterprise app.
  2. Review Changing Knowledge Graph configurations to see the impact of changing configurations on existing apps.



Use the following procedure to update Knowledge Graph configurations in the console:

###  Console 

To use the Google Cloud console to manage Knowledge Graph configurations, follow these steps:

  1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. On the **Apps** page, click the app whose Knowledge Graph configurations you want to update.

  3. Navigate to **Configurations** > **Knowledge Graph** tab.

  4. Toggle **Google Cloud Knowledge Graph** or **Private Knowledge Graph** based on your needs.

  5. Click the **Save** button after confirming any prompts or warnings.




The effects of enabling and disabling Knowledge Graph are as follows:

  1. **Google Cloud Knowledge Graph** :

     * Enabling the Google Cloud Knowledge Graph grants access to enriched data from external sources, broadening search context.
     * Disabling it limits search results to internal data, removing access to external context.
  2. **Private Knowledge Graph** :

     * Enabling the private Knowledge Graph regenerates internal derived data, and query annotations return after up to a day.
     * Disabling it deletes internal derived data and removes query annotations, reducing search accuracy and richness.



###  API 

You can modify Knowledge Graph settings using the API:

**Key Term:** In Gemini Enterprise, the term _app_ can be used interchangeably with the term _engine_ in the context of APIs. A Gemini Enterprise engine is a generic search engine where the `app_type` field is set to `APP_TYPE_INTRANET`.
    
    
      {
        "engine": {
          "name": "projects/<project_id>/locations/<location>/collections/<collection_id>/engines/<engine_id>",
          "knowledge_graph_config": {
            "enable_cloud_knowledge_graph": true,
            "enable_private_knowledge_graph": true
          }
        },
        "update_mask": {
          "paths": "knowledge_graph_config"
        }
      }
    
    

### View knowledge panels in search results

You can view how the Knowledge Graph-enriched search results are displayed in your search application. For panel-based search interfaces, the Knowledge Graph panel appears as an enriched information box alongside regular search results. It integrates relevant entity details, such as names, descriptions, images, and relationships, providing a more informative and contextually relevant search experience. These boosted results help you quickly find key insights related to your query.

The following JSON example shows how a People panel appears in an API response:
    
    
          one_box_results: [
            {
              one_box_type: PEOPLE
              search_results: [
                {
                  document: {
                    name: "projects/<pii data>/locations/global/collections/default_collection/dataStores/people-v17-df-sprint_1731449540556/branches/0/documents/<name>"
                    derived_struct_data: {
                      fields: [
                        {
                          key: "management_chain"
                          value: {
                            list_value: {
                              values: [
                                {
                                  struct_value: {
                                    fields: [
                                      {
                                        key: "person_id"
                                        value: {
    
                                          string_value: "<persons name>"
                                        }
                                      },
                                      {
                                        key: "job_title"
                                        value: {
                                          string_value: "Account Executive"
                                        }
                                      },
                                      {
                                        key: "name"
                                        value: {
                                          string_value: "<persons name>"
                                        }
                                      }
                                    ]
                                  }
                                },
                                {
                                  struct_value: {
                                    fields: [
                                      {
                                        key: "name"
                                        value: {
                                          string_value: "<persons name>"
                                        }
                                      },
                                      {
                                        key: "job_title"
                                        value: {
    
                                          string_value: "Account Executive"
                                        }
                                      },
                                      {
                                        key: "person_id"
                                        value: {
    
                                          string_value: "<persons name>"
                                        }
                                      }
                                    ]
                                  }
                                }
    
                              ]
                            }
                          }
                        },
                        {
    
                          key: "teammates_with_same_manager"
                          value: {
    
                            list_value: {
    
                              values: [
                                {
    
                                  struct_value: {
    
                                    fields: [
                                      {
    
                                        key: "person_id"
                                        value: {
    
                                          string_value: "<persons name>"
                                        }
                                      },
                                      {
    
                                        key: "job_title"
                                        value: {
    
                                          string_value: "Account Executive"
                                        }
                                      },
                                      {
    
                                        key: "name"
                                        value: {
    
                                          string_value: "<persons name>"
                                        }
                                      }
                                    ]
                                  }
                                }
                              ]
                            }
                          }
                        },
                        {
                          key: "direct_reports"
                          value: {
                            list_value: {
                              values: [
                                {
                                  struct_value: {
                                    fields: [
                                      {
                                        key: "job_title"
                                        value: {
                                          string_value: "Account Strategist, Lead Generation"
                                        }
                                      },
                                      {
                                        key: "name"
                                        value: {
                                          string_value: "<persons name>"
                                        }
                                      },
                                      {
                                        key: "person_id"
                                        value: {
                                          string_value: "<persons name>"
                                        }
                                      }
                                    ]
                                  }
                                },
                                {
                                  struct_value: {
                                    fields: [
                                      {
                                        key: "person_id"
                                        value: {
                                          string_value: "<persons name>"
                                        }
                                      },
                                      {
                                        key: "name"
                                        value: {
                                          string_value: "<persons name>"
                                        }
                                      },
                                      {
                                        key: "job_title"
                                        value: {
    
                                          string_value: "Account Strategist, Mid-Market Sales, Google Customer Solutions"
                                        }
                                      }
                                    ]
                                  }
                                }
                              ]
                            }
                          }
                        }
                      ]
                    }
                  }
                }
              ]
            }
          ]
    
    

The following JSON example shows how an Organization panel appears in an API response:
    
    
          {
            one_box_type: ORGANIZATION
            knowledge_graph_results: [
              {
                knowledge_graph_source_type: CLOUD_KG
                context: {
                  struct_value: {
                    fields: [
                      {
                        key: "@vocab"
                        value: {
                          string_value: "http://schema.org/"
                        }
                      }
                    ]
                  }
                }
                type: {
                  string_value: "ItemList"
                }
                item_list_element: {
                  values: [
                    {
                      struct_value: {
                        fields: [
                          {
                            key: "result"
                            value: {
                              struct_value: {
                                fields: [
                                  {
                                    key: "@id"
                                    value: {
                                      string_value: "c-025prnpgp"
                                    }
                                  },
                                  {
                                    key: "identifier"
                                    value: {
                                      list_value: {
                                        values: [
                                          {
                                            struct_value: {
                                              fields: [
                                                {
                                                  key: "name"
                                                  value: {
                                                    string_value: "googleKgMID"
                                                  }
                                                },
                                                {
                                                  key: "value"
                                                  value: {
                                                    string_value: "/m/0k8z"
                                                  }
                                                },
                                                {
                                                  key: "@type"
                                                  value: {
                                                    string_value: "PropertyValue"
                                                  }
                                                }
                                              ]
                                            }
                                          },
                                          {
                                            struct_value: {
                                              fields: [
                                                {
                                                  key: "value"
                                                  value: {
    
                                                    string_value: "Q312"
                                                  }
                                                },
                                                {
                                                  key: "@type"
                                                  value: {
                                                    string_value: "PropertyValue"
                                                  }
                                                },
                                                {
                                                  key: "name"
                                                  value: {
    
                                                    string_value: "wikidataQID"
                                                  }
                                                }
                                              ]
                                            }
                                          }
                                        ]
                                      }
                                    }
                                  },
                                  {
                                    key: "@type"
                                    value: {
                                      list_value: {
                                        values: [
                                          {
                                            string_value: "Corporation"
                                          },
                                          {
                                            string_value: "Thing"
                                          },
                                          {
                                            string_value: "Organization"
                                          }
                                        ]
                                      }
                                    }
                                  },
                                  {
                                    key: "name"
                                    value: {
                                      string_value: "Apple"
                                    }
                                  },
                                  {
                                    key: "detailedDescription"
                                    value: {
                                      struct_value: {
                                        fields: [
                                          {
                                            key: "url"
                                            value: {
                                              string_value: "https://en.wikipedia.org/wiki/Apple_Inc."
                                            }
                                          },
                                          {
                                            key: "articleBody"
                                            value: {
                                              string_value: "Apple Inc. is an American multinational corporation and technology company headquartered and incorporated in Cupertino, California, in Silicon Valley. It is best known for its consumer electronics, software, and services. "
                                            }
                                          },
                                          {
                                            key: "license"
                                            value: {
    
                                              string_value: "https://en.wikipedia.org/wiki/Wikipedia:Text_of_Creative_Commons_Attribution-ShareAlike_3.0_Unported_License"
                                            }
                                          }
                                        ]
                                      }
                                    }
                                  },
                                  {
                                    key: "description"
                                    value: {
                                      string_value: "Technology company"
                                    }
                                  },
                                  {
                                    key: "image"
                                    value: {
                                      struct_value: {
                                        fields: [
                                          {
                                            key: "contentUrl"
                                            value: {
                                              string_value: "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTMHrvLPmr_8yVjoTYsyxhRGtPMcA90bcJl9_RehtJU0tr64KNR"
                                            }
                                          },
                                          {
                                            key: "url"
                                            value: {
    
                                              string_value: "https://commons.wikimedia.org/wiki/File:Apple_logo_black.svg"
                                            }
                                          }
                                        ]
                                      }
                                    }
                                  },
                                  {
                                    key: "url"
                                    value: {
    
                                      string_value: "http://www.apple.com/"
                                    }
                                  }
                                ]
                              }
                            }
                          }
                        ]
                      }
                    }
                  ]
                }
              }
            ]
          }
    
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
