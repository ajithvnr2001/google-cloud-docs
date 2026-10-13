---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-MetadataJob-ImportJobSpec-ImportJobScope/
title: Dataplex V1 API - Class Google::Cloud::Dataplex::V1::MetadataJob::ImportJobSpec::ImportJobScope (v2.10.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:53:11.397138+00:00
---

# Dataplex V1 API - Class Google::Cloud::Dataplex::V1::MetadataJob::ImportJobSpec::ImportJobScope (v2.10.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-MetadataJob-ImportJobSpec-ImportJobScope/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dataplex V1 API - Class Google::Cloud::Dataplex::V1::MetadataJob::ImportJobSpec::ImportJobScope (v2.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.10.1 (latest)  2.10.0  2.9.0  2.8.1  2.7.0  2.6.1  2.5.0  2.4.1  2.3.1  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.1  0.23.0  0.22.0  0.21.1  0.20.0  0.19.0  0.18.2  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.1  0.9.0  0.8.0  0.7.0  0.6.1  0.5.1  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Dataplex V1 API class Google::Cloud::Dataplex::V1::MetadataJob::ImportJobSpec::ImportJobScope.

A boundary on the scope of impact that the metadata import job can have.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #aspect_types
    
    
    def aspect_types() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Optional. The aspect types that are in scope for the import job, specified as relative resource names in the format `projects/{project_number_or_id}/locations/{location_id}/aspectTypes/{aspect_type_id}`. The job modifies only the aspects that belong to these aspect types.

This field is required when creating an aspect-only import job.

If the metadata import file attempts to modify an aspect whose type isn't included in this list, the import job is halted before modifying any entries or aspects.

The location of an aspect type must either match the location of the job, or the aspect type must be global. 




### #aspect_types=
    
    
    def aspect_types=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Optional. The aspect types that are in scope for the import job, specified as relative resource names in the format `projects/{project_number_or_id}/locations/{location_id}/aspectTypes/{aspect_type_id}`. The job modifies only the aspects that belong to these aspect types.

This field is required when creating an aspect-only import job.

If the metadata import file attempts to modify an aspect whose type isn't included in this list, the import job is halted before modifying any entries or aspects.

The location of an aspect type must either match the location of the job, or the aspect type must be global. 




**Returns**

  * (::Array<::String>) — Optional. The aspect types that are in scope for the import job, specified as relative resource names in the format `projects/{project_number_or_id}/locations/{location_id}/aspectTypes/{aspect_type_id}`. The job modifies only the aspects that belong to these aspect types.

This field is required when creating an aspect-only import job.

If the metadata import file attempts to modify an aspect whose type isn't included in this list, the import job is halted before modifying any entries or aspects.

The location of an aspect type must either match the location of the job, or the aspect type must be global. 




### #entry_groups
    
    
    def entry_groups() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Required. The entry groups that are in scope for the import job, specified as relative resource names in the format `projects/{project_number_or_id}/locations/{location_id}/entryGroups/{entry_group_id}`. Only entries and aspects that belong to the specified entry groups are affected by the job.

The entry groups and the job must be in the same location. 




### #entry_groups=
    
    
    def entry_groups=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Required. The entry groups that are in scope for the import job, specified as relative resource names in the format `projects/{project_number_or_id}/locations/{location_id}/entryGroups/{entry_group_id}`. Only entries and aspects that belong to the specified entry groups are affected by the job.

The entry groups and the job must be in the same location. 




**Returns**

  * (::Array<::String>) — Required. The entry groups that are in scope for the import job, specified as relative resource names in the format `projects/{project_number_or_id}/locations/{location_id}/entryGroups/{entry_group_id}`. Only entries and aspects that belong to the specified entry groups are affected by the job.

The entry groups and the job must be in the same location. 




### #entry_link_types
    
    
    def entry_link_types() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Optional. The entry link types that are in scope for the import job, specified as relative resource names in the format `projects/{project_number_or_id}/locations/{location_id}/entryLinkTypes/{entry_link_type_id}`. The job modifies only the entryLinks that belong to these entry link types.

If the metadata import file attempts to create or delete an entry link whose entry link type isn't included in this list, the import job will skip those entry links. 




### #entry_link_types=
    
    
    def entry_link_types=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Optional. The entry link types that are in scope for the import job, specified as relative resource names in the format `projects/{project_number_or_id}/locations/{location_id}/entryLinkTypes/{entry_link_type_id}`. The job modifies only the entryLinks that belong to these entry link types.

If the metadata import file attempts to create or delete an entry link whose entry link type isn't included in this list, the import job will skip those entry links. 




**Returns**

  * (::Array<::String>) — Optional. The entry link types that are in scope for the import job, specified as relative resource names in the format `projects/{project_number_or_id}/locations/{location_id}/entryLinkTypes/{entry_link_type_id}`. The job modifies only the entryLinks that belong to these entry link types.

If the metadata import file attempts to create or delete an entry link whose entry link type isn't included in this list, the import job will skip those entry links. 




### #entry_types
    
    
    def entry_types() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Required. The entry types that are in scope for the import job, specified as relative resource names in the format `projects/{project_number_or_id}/locations/{location_id}/entryTypes/{entry_type_id}`. The job modifies only the entries and aspects that belong to these entry types.

If the metadata import file attempts to modify an entry whose type isn't included in this list, the import job is halted before modifying any entries or aspects.

The location of an entry type must either match the location of the job, or the entry type must be global. 




### #entry_types=
    
    
    def entry_types=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Required. The entry types that are in scope for the import job, specified as relative resource names in the format `projects/{project_number_or_id}/locations/{location_id}/entryTypes/{entry_type_id}`. The job modifies only the entries and aspects that belong to these entry types.

If the metadata import file attempts to modify an entry whose type isn't included in this list, the import job is halted before modifying any entries or aspects.

The location of an entry type must either match the location of the job, or the entry type must be global. 




**Returns**

  * (::Array<::String>) — Required. The entry types that are in scope for the import job, specified as relative resource names in the format `projects/{project_number_or_id}/locations/{location_id}/entryTypes/{entry_type_id}`. The job modifies only the entries and aspects that belong to these entry types.

If the metadata import file attempts to modify an entry whose type isn't included in this list, the import job is halted before modifying any entries or aspects.

The location of an entry type must either match the location of the job, or the entry type must be global. 




### #glossaries
    
    
    def glossaries() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Optional. The glossaries that are in scope for the import job, specified as relative resource names in the format `projects/{project_number_or_id}/locations/{location_id}/glossaries/{glossary_id}`.

While importing Business Glossary entries, the user must provide glossaries. While importing entries, the user does not have to provide glossaries. If the metadata import file attempts to modify Business Glossary entries whose glossary isn't included in this list, the import job will skip those entries.

The location of a glossary must either match the location of the job, or the glossary must be global. 




### #glossaries=
    
    
    def glossaries=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Optional. The glossaries that are in scope for the import job, specified as relative resource names in the format `projects/{project_number_or_id}/locations/{location_id}/glossaries/{glossary_id}`.

While importing Business Glossary entries, the user must provide glossaries. While importing entries, the user does not have to provide glossaries. If the metadata import file attempts to modify Business Glossary entries whose glossary isn't included in this list, the import job will skip those entries.

The location of a glossary must either match the location of the job, or the glossary must be global. 




**Returns**

  * (::Array<::String>) — Optional. The glossaries that are in scope for the import job, specified as relative resource names in the format `projects/{project_number_or_id}/locations/{location_id}/glossaries/{glossary_id}`.

While importing Business Glossary entries, the user must provide glossaries. While importing entries, the user does not have to provide glossaries. If the metadata import file attempts to modify Business Glossary entries whose glossary isn't included in this list, the import job will skip those entries.

The location of a glossary must either match the location of the job, or the glossary must be global. 




### #referenced_entry_scopes
    
    
    def referenced_entry_scopes() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Optional. Defines the scope of entries that can be referenced in the entry links.

Currently, projects are supported as valid scopes. Format: `projects/{project_number_or_id}`

If the metadata import file attempts to create an entry link which references an entry that is not in the scope, the import job will skip that entry link. 




### #referenced_entry_scopes=
    
    
    def referenced_entry_scopes=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Optional. Defines the scope of entries that can be referenced in the entry links.

Currently, projects are supported as valid scopes. Format: `projects/{project_number_or_id}`

If the metadata import file attempts to create an entry link which references an entry that is not in the scope, the import job will skip that entry link. 




**Returns**

  * (::Array<::String>) — Optional. Defines the scope of entries that can be referenced in the entry links.

Currently, projects are supported as valid scopes. Format: `projects/{project_number_or_id}`

If the metadata import file attempts to create an entry link which references an entry that is not in the scope, the import job will skip that entry link. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
