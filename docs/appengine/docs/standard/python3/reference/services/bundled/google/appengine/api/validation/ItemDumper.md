---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/ItemDumper/
title: google.appengine.api.validation.ItemDumper \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T10:30:36.063203+00:00
---

# google.appengine.api.validation.ItemDumper  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/ItemDumper/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.validation.ItemDumper Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L65-L73) For dumping `validation.Items`. Respects `SortedDict` key ordering. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.api.validation.ItemDumper(
        stream,
        default_style=None,
        default_flow_style=None,
        canonical=None,
        indent=None,
        width=None,
        allow_unicode=None,
        line_break=None,
        encoding=None,
        explicit_start=None,
        explicit_end=None,
        version=None,
        tags=None,
        block_seq_indent=None,
        top_level_colon_align=None,
        prefix_colon=None
    )
    

| 

## Attributes  
  
---  
  
`emitter` |   
`flow_level` |   
`parser` |   
`processing_version` |   
`resolver` |   
`serializer` |   
`stream` |   
  
## Methods

### `add_implicit_resolver`
    
    
    @classmethod
    add_implicit_resolver(
        tag, regexp, first
    )
    

### `add_implicit_resolver_base`
    
    
    @classmethod
    add_implicit_resolver_base(
        tag, regexp, first
    )
    

### `add_multi_representer`
    
    
    @classmethod
    add_multi_representer(
        data_type, representer
    )
    

### `add_path_resolver`
    
    
    @classmethod
    add_path_resolver(
        tag, path, kind=None
    )
    

### `add_representer`
    
    
    @classmethod
    add_representer(
        data_type, representer
    )
    

### `analyze_scalar`
    
    
    analyze_scalar(
        scalar
    )
    

### `anchor_node`
    
    
    anchor_node(
        node
    )
    

### `ascend_resolver`
    
    
    ascend_resolver()
    

### `check_empty_document`
    
    
    check_empty_document()
    

### `check_empty_mapping`
    
    
    check_empty_mapping()
    

### `check_empty_sequence`
    
    
    check_empty_sequence()
    

### `check_resolver_prefix`
    
    
    check_resolver_prefix(
        depth, path, kind, current_node, current_index
    )
    

### `check_simple_key`
    
    
    check_simple_key()
    

### `choose_scalar_style`
    
    
    choose_scalar_style()
    

### `close`
    
    
    close()
    

### `descend_resolver`
    
    
    descend_resolver(
        current_node, current_index
    )
    

### `determine_block_hints`
    
    
    determine_block_hints(
        text
    )
    

### `dispose`
    
    
    dispose()
    

### `emit`
    
    
    emit(
        event
    )
    

### `expect_alias`
    
    
    expect_alias()
    

### `expect_block_mapping`
    
    
    expect_block_mapping()
    

### `expect_block_mapping_key`
    
    
    expect_block_mapping_key(
        first=False
    )
    

### `expect_block_mapping_simple_value`
    
    
    expect_block_mapping_simple_value()
    

### `expect_block_mapping_value`
    
    
    expect_block_mapping_value()
    

### `expect_block_sequence`
    
    
    expect_block_sequence()
    

### `expect_block_sequence_item`
    
    
    expect_block_sequence_item(
        first=False
    )
    

### `expect_document_end`
    
    
    expect_document_end()
    

### `expect_document_root`
    
    
    expect_document_root()
    

### `expect_document_start`
    
    
    expect_document_start(
        first=False
    )
    

### `expect_first_block_mapping_key`
    
    
    expect_first_block_mapping_key()
    

### `expect_first_block_sequence_item`
    
    
    expect_first_block_sequence_item()
    

### `expect_first_document_start`
    
    
    expect_first_document_start()
    

### `expect_first_flow_mapping_key`
    
    
    expect_first_flow_mapping_key()
    

### `expect_first_flow_sequence_item`
    
    
    expect_first_flow_sequence_item()
    

### `expect_flow_mapping`
    
    
    expect_flow_mapping(
        single=False, force_flow_indent=False
    )
    

### `expect_flow_mapping_key`
    
    
    expect_flow_mapping_key()
    

### `expect_flow_mapping_simple_value`
    
    
    expect_flow_mapping_simple_value()
    

### `expect_flow_mapping_value`
    
    
    expect_flow_mapping_value()
    

### `expect_flow_sequence`
    
    
    expect_flow_sequence(
        force_flow_indent=False
    )
    

### `expect_flow_sequence_item`
    
    
    expect_flow_sequence_item()
    

### `expect_node`
    
    
    expect_node(
        root=False, sequence=False, mapping=False, simple_key=False
    )
    

### `expect_nothing`
    
    
    expect_nothing()
    

### `expect_scalar`
    
    
    expect_scalar()
    

### `expect_stream_start`
    
    
    expect_stream_start()
    

### `flush_stream`
    
    
    flush_stream()
    

### `generate_anchor`
    
    
    generate_anchor(
        node
    )
    

### `ignore_aliases`
    
    
    ignore_aliases(
        data
    )
    

### `increase_indent`
    
    
    increase_indent(
        flow=False, sequence=None, indentless=False
    )
    

### `need_events`
    
    
    need_events(
        count
    )
    

### `need_more_events`
    
    
    need_more_events()
    

### `open`
    
    
    open()
    

### `prepare_anchor`
    
    
    prepare_anchor(
        anchor
    )
    

### `prepare_tag`
    
    
    prepare_tag(
        tag
    )
    

### `prepare_tag_handle`
    
    
    prepare_tag_handle(
        handle
    )
    

### `prepare_tag_prefix`
    
    
    prepare_tag_prefix(
        prefix
    )
    

### `prepare_version`
    
    
    prepare_version(
        version
    )
    

### `process_anchor`
    
    
    process_anchor(
        indicator
    )
    

### `process_scalar`
    
    
    process_scalar()
    

### `process_tag`
    
    
    process_tag()
    

### `represent`
    
    
    represent(
        data
    )
    

### `represent_binary`
    
    
    represent_binary(
        data
    )
    

### `represent_bool`
    
    
    represent_bool(
        data, anchor=None
    )
    

### `represent_data`
    
    
    represent_data(
        data
    )
    

### `represent_date`
    
    
    represent_date(
        data
    )
    

### `represent_datetime`
    
    
    represent_datetime(
        data
    )
    

### `represent_dict`
    
    
    represent_dict(
        data
    )
    

### `represent_float`
    
    
    represent_float(
        data
    )
    

### `represent_int`
    
    
    represent_int(
        data
    )
    

### `represent_key`
    
    
    represent_key(
        data
    )
    

David Fraser: Extract a method to represent keys in mappings, so that a subclass can choose not to quote them (for example) used in represent_mapping https://bitbucket.org/davidfraser/pyyaml/commits/d81df6eb95f20cac4a79eed95ae553b5c6f77b8c

### `represent_list`
    
    
    represent_list(
        data
    )
    

### `represent_mapping`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/validation.py#L68-L73)
    
    
    represent_mapping(
        tag, mapping, flow_style=None
    )
    

### `represent_none`
    
    
    represent_none(
        data
    )
    

### `represent_omap`
    
    
    represent_omap(
        tag, omap, flow_style=None
    )
    

### `represent_ordereddict`
    
    
    represent_ordereddict(
        data
    )
    

### `represent_scalar`
    
    
    represent_scalar(
        tag, value, style=None, anchor=None
    )
    

### `represent_sequence`
    
    
    represent_sequence(
        tag, sequence, flow_style=None
    )
    

### `represent_set`
    
    
    represent_set(
        data
    )
    

### `represent_str`
    
    
    represent_str(
        data
    )
    

### `represent_undefined`
    
    
    represent_undefined(
        data
    )
    

### `represent_yaml_object`
    
    
    represent_yaml_object(
        tag, data, cls, flow_style=None
    )
    

### `resolve`
    
    
    resolve(
        kind, value, implicit
    )
    

### `serialize`
    
    
    serialize(
        node
    )
    

### `serialize_node`
    
    
    serialize_node(
        node, parent, index
    )
    

### `write_comment`
    
    
    write_comment(
        comment, pre=False
    )
    

### `write_double_quoted`
    
    
    write_double_quoted(
        text, split=True
    )
    

### `write_folded`
    
    
    write_folded(
        text
    )
    

### `write_indent`
    
    
    write_indent()
    

### `write_indicator`
    
    
    write_indicator(
        indicator, need_whitespace, whitespace=False, indention=False
    )
    

### `write_line_break`
    
    
    write_line_break(
        data=None
    )
    

### `write_literal`
    
    
    write_literal(
        text, comment=None
    )
    

### `write_plain`
    
    
    write_plain(
        text, split=True
    )
    

### `write_post_comment`
    
    
    write_post_comment(
        event
    )
    

### `write_pre_comment`
    
    
    write_pre_comment(
        event
    )
    

### `write_single_quoted`
    
    
    write_single_quoted(
        text, split=True
    )
    

### `write_stream_end`
    
    
    write_stream_end()
    

### `write_stream_start`
    
    
    write_stream_start()
    

### `write_tag_directive`
    
    
    write_tag_directive(
        handle_text, prefix_text
    )
    

### `write_version_directive`
    
    
    write_version_directive(
        version_text
    )
    

## Class Variables  
  
---  
  
ANCHOR_RE |  Instance of `ruamel.yaml.util.LazyEval` Compiled regular expression object.   
ANCHOR_TEMPLATE |  `'id%03d'`  
DEFAULT_MAPPING_TAG |  `'tag:yaml.org,2002:map'`  
DEFAULT_SCALAR_TAG |  `'tag:yaml.org,2002:str'`  
DEFAULT_SEQUENCE_TAG |  `'tag:yaml.org,2002:seq'`  
DEFAULT_TAG_PREFIXES | 
    
    
    {
     '!': '!',
     'tag:yaml.org,2002:': '!!'
    }
      
  
ESCAPE_REPLACEMENTS | 
    
    
    {
     '"': '"',
     '\\': '\\',
     '\n': 'n',
     '\r': 'r',
     '\t': 't',
     '\u2028': 'L',
     '\u2029': 'P',
     '\x00': '0',
     '\x07': 'a',
     '\x08': 'b',
     '\x0b': 'v',
     '\x0c': 'f',
     '\x1b': 'e',
     '\x85': 'N',
     '\xa0': '_'
    }
      
  
MAX_SIMPLE_KEY_LENGTH |  `128`  
inf_value |  `inf`  
yaml_implicit_resolvers | 
    
    
    {
     '!': [('tag:yaml.org,2002:yaml', <ruamel.yaml.util.LazyEval object>)],
     '&': [('tag:yaml.org,2002:yaml', <ruamel.yaml.util.LazyEval object>)],
     '': [('tag:yaml.org,2002:null', <ruamel.yaml.util.LazyEval object>)],
     '*': [('tag:yaml.org,2002:yaml', <ruamel.yaml.util.LazyEval object>)],
     '+': [('tag:yaml.org,2002:float', <ruamel.yaml.util.LazyEval object>), ('tag:yaml.org,2002:int', <ruamel.yaml.util.LazyEval object>)],
     '-': [('tag:yaml.org,2002:float', <ruamel.yaml.util.LazyEval object>), ('tag:yaml.org,2002:int', <ruamel.yaml.util.LazyEval object>)],
     '.': [('tag:yaml.org,2002:float', <ruamel.yaml.util.LazyEval object>)],
     '0': [('tag:yaml.org,2002:float', <ruamel.yaml.util.LazyEval object>), ('tag:yaml.org,2002:int', <ruamel.yaml.util.LazyEval object>), ('tag:yaml.org,2002:timestamp', <ruamel.yaml.util.LazyEval object>)],
     '1': [('tag:yaml.org,2002:float', <ruamel.yaml.util.LazyEval object>), ('tag:yaml.org,2002:int', <ruamel.yaml.util.LazyEval object>), ('tag:yaml.org,2002:timestamp', <ruamel.yaml.util.LazyEval object>)],
     '2': [('tag:yaml.org,2002:float', <ruamel.yaml.util.LazyEval object>), ('tag:yaml.org,2002:int', <ruamel.yaml.util.LazyEval object>), ('tag:yaml.org,2002:timestamp', <ruamel.yaml.util.LazyEval object>)],
     '3': [('tag:yaml.org,2002:float', <ruamel.yaml.util.LazyEval object>), ('tag:yaml.org,2002:int', <ruamel.yaml.util.LazyEval object>), ('tag:yaml.org,2002:timestamp', <ruamel.yaml.util.LazyEval object>)],
     '4': [('tag:yaml.org,2002:float', <ruamel.yaml.util.LazyEval object>), ('tag:yaml.org,2002:int', <ruamel.yaml.util.LazyEval object>), ('tag:yaml.org,2002:timestamp', <ruamel.yaml.util.LazyEval object>)],
     '5': [('tag:yaml.org,2002:float', <ruamel.yaml.util.LazyEval object>), ('tag:yaml.org,2002:int', <ruamel.yaml.util.LazyEval object>), ('tag:yaml.org,2002:timestamp', <ruamel.yaml.util.LazyEval object>)],
     '6': [('tag:yaml.org,2002:float', <ruamel.yaml.util.LazyEval object>), ('tag:yaml.org,2002:int', <ruamel.yaml.util.LazyEval object>), ('tag:yaml.org,2002:timestamp', <ruamel.yaml.util.LazyEval object>)],
     '7': [('tag:yaml.org,2002:float', <ruamel.yaml.util.LazyEval object>), ('tag:yaml.org,2002:int', <ruamel.yaml.util.LazyEval object>), ('tag:yaml.org,2002:timestamp', <ruamel.yaml.util.LazyEval object>)],
     '8': [('tag:yaml.org,2002:float', <ruamel.yaml.util.LazyEval object>), ('tag:yaml.org,2002:int', <ruamel.yaml.util.LazyEval object>), ('tag:yaml.org,2002:timestamp', <ruamel.yaml.util.LazyEval object>)],
     '9': [('tag:yaml.org,2002:float', <ruamel.yaml.util.LazyEval object>), ('tag:yaml.org,2002:int', <ruamel.yaml.util.LazyEval object>), ('tag:yaml.org,2002:timestamp', <ruamel.yaml.util.LazyEval object>)],
     '<': [('tag:yaml.org,2002:merge', <ruamel.yaml.util.LazyEval object>)],
     '=': [('tag:yaml.org,2002:value', <ruamel.yaml.util.LazyEval object>)],
     'F': [('tag:yaml.org,2002:bool', <ruamel.yaml.util.LazyEval object>)],
     'N': [('tag:yaml.org,2002:null', <ruamel.yaml.util.LazyEval object>)],
     'T': [('tag:yaml.org,2002:bool', <ruamel.yaml.util.LazyEval object>)],
     'f': [('tag:yaml.org,2002:bool', <ruamel.yaml.util.LazyEval object>)],
     'n': [('tag:yaml.org,2002:null', <ruamel.yaml.util.LazyEval object>)],
     't': [('tag:yaml.org,2002:bool', <ruamel.yaml.util.LazyEval object>)],
     '~': [('tag:yaml.org,2002:null', <ruamel.yaml.util.LazyEval object>)]
    }
      
  
yaml_multi_representers | 
    
    
    {
    
    }
      
  
yaml_path_resolvers | 
    
    
    {
    
    }
      
  
yaml_representers | 
    
    
    {
     <class 'NoneType'>: <function SafeRepresenter.represent_none>,
     <class 'bool'>: <function SafeRepresenter.represent_bool>,
     <class 'bytes'>: <function SafeRepresenter.represent_binary>,
     <class 'collections.OrderedDict'>: <function SafeRepresenter.represent_ordereddict>,
     <class 'datetime.date'>: <function SafeRepresenter.represent_date>,
     <class 'datetime.datetime'>: <function SafeRepresenter.represent_datetime>,
     <class 'dict'>: <function SafeRepresenter.represent_dict>,
     <class 'float'>: <function SafeRepresenter.represent_float>,
     <class 'google.appengine.api.validation.SortedDict'>: <function SafeRepresenter.represent_dict>,
     <class 'int'>: <function SafeRepresenter.represent_int>,
     <class 'list'>: <function SafeRepresenter.represent_list>,
     <class 'ruamel.yaml.compat.ordereddict'>: <function SafeRepresenter.represent_ordereddict>,
     <class 'set'>: <function SafeRepresenter.represent_set>,
     <class 'str'>: <function SafeRepresenter.represent_str>,
     <class 'tuple'>: <function SafeRepresenter.represent_list>,
     None: <function SafeRepresenter.represent_undefined>
    }
      
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
