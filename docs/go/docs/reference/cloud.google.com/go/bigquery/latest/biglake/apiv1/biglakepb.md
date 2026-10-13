---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1/biglakepb/
title: BigLake API v1 - Package cloud.google.com/go/bigquery/biglake/apiv1/biglakepb (v1.85.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:57:38.244260+00:00
---

# BigLake API v1 - Package cloud.google.com/go/bigquery/biglake/apiv1/biglakepb (v1.85.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1/biglakepb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  BigLake API v1 - Package cloud.google.com/go/bigquery/biglake/apiv1/biglakepb (v1.85.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.85.0 (latest)  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.1  1.78.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.1  1.72.0  1.71.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.2  1.65.0  1.64.0  1.63.1  1.62.0  1.61.0  1.60.0  1.59.1  1.58.0  1.57.1  1.54.0  1.53.0  1.52.0  1.51.2  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.1  1.33.0  1.32.0  1.31.0  1.30.2  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.1  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/bigquery/biglake/apiv1/biglakepb). 

##  Constants 

### MetastoreService_CreateCatalog_FullMethodName, MetastoreService_DeleteCatalog_FullMethodName, MetastoreService_GetCatalog_FullMethodName, MetastoreService_ListCatalogs_FullMethodName, MetastoreService_CreateDatabase_FullMethodName, MetastoreService_DeleteDatabase_FullMethodName, MetastoreService_UpdateDatabase_FullMethodName, MetastoreService_GetDatabase_FullMethodName, MetastoreService_ListDatabases_FullMethodName, MetastoreService_CreateTable_FullMethodName, MetastoreService_DeleteTable_FullMethodName, MetastoreService_UpdateTable_FullMethodName, MetastoreService_RenameTable_FullMethodName, MetastoreService_GetTable_FullMethodName, MetastoreService_ListTables_FullMethodName
    
    
    const (
    	MetastoreService_CreateCatalog_FullMethodName  = "/google.cloud.bigquery.biglake.v1.MetastoreService/CreateCatalog"
    	MetastoreService_DeleteCatalog_FullMethodName  = "/google.cloud.bigquery.biglake.v1.MetastoreService/DeleteCatalog"
    	MetastoreService_GetCatalog_FullMethodName     = "/google.cloud.bigquery.biglake.v1.MetastoreService/GetCatalog"
    	MetastoreService_ListCatalogs_FullMethodName   = "/google.cloud.bigquery.biglake.v1.MetastoreService/ListCatalogs"
    	MetastoreService_CreateDatabase_FullMethodName = "/google.cloud.bigquery.biglake.v1.MetastoreService/CreateDatabase"
    	MetastoreService_DeleteDatabase_FullMethodName = "/google.cloud.bigquery.biglake.v1.MetastoreService/DeleteDatabase"
    	MetastoreService_UpdateDatabase_FullMethodName = "/google.cloud.bigquery.biglake.v1.MetastoreService/UpdateDatabase"
    	MetastoreService_GetDatabase_FullMethodName    = "/google.cloud.bigquery.biglake.v1.MetastoreService/GetDatabase"
    	MetastoreService_ListDatabases_FullMethodName  = "/google.cloud.bigquery.biglake.v1.MetastoreService/ListDatabases"
    	MetastoreService_CreateTable_FullMethodName    = "/google.cloud.bigquery.biglake.v1.MetastoreService/CreateTable"
    	MetastoreService_DeleteTable_FullMethodName    = "/google.cloud.bigquery.biglake.v1.MetastoreService/DeleteTable"
    	MetastoreService_UpdateTable_FullMethodName    = "/google.cloud.bigquery.biglake.v1.MetastoreService/UpdateTable"
    	MetastoreService_RenameTable_FullMethodName    = "/google.cloud.bigquery.biglake.v1.MetastoreService/RenameTable"
    	MetastoreService_GetTable_FullMethodName       = "/google.cloud.bigquery.biglake.v1.MetastoreService/GetTable"
    	MetastoreService_ListTables_FullMethodName     = "/google.cloud.bigquery.biglake.v1.MetastoreService/ListTables"
    )

## Variables 

### TableView_name, TableView_value
    
    
    var (
    	TableView_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "TABLE_VIEW_UNSPECIFIED",
    		1: "BASIC",
    		2: "FULL",
    	}
    	TableView_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"TABLE_VIEW_UNSPECIFIED": 0,
    		"BASIC":                  1,
    		"FULL":                   2,
    	}
    )

Enum value maps for TableView.

### Database_Type_name, Database_Type_value
    
    
    var (
    	Database_Type_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "TYPE_UNSPECIFIED",
    		1: "HIVE",
    	}
    	Database_Type_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"TYPE_UNSPECIFIED": 0,
    		"HIVE":             1,
    	}
    )

Enum value maps for Database_Type.

### Table_Type_name, Table_Type_value
    
    
    var (
    	Table_Type_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "TYPE_UNSPECIFIED",
    		1: "HIVE",
    	}
    	Table_Type_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"TYPE_UNSPECIFIED": 0,
    		"HIVE":             1,
    	}
    )

Enum value maps for Table_Type.

### File_google_cloud_bigquery_biglake_v1_metastore_proto
    
    
    var File_google_cloud_bigquery_biglake_v1_metastore_proto protoreflect.FileDescriptor

### MetastoreService_ServiceDesc
    
    
    var MetastoreService_ServiceDesc = grpc.ServiceDesc{
    	ServiceName: "google.cloud.bigquery.biglake.v1.MetastoreService",
    	HandlerType: (*MetastoreServiceServer)([nil](https://pkg.go.dev/builtin#nil)),
    	Methods: []grpc.MethodDesc{
    		{
    			MethodName: "CreateCatalog",
    			Handler:    _MetastoreService_CreateCatalog_Handler,
    		},
    		{
    			MethodName: "DeleteCatalog",
    			Handler:    _MetastoreService_DeleteCatalog_Handler,
    		},
    		{
    			MethodName: "GetCatalog",
    			Handler:    _MetastoreService_GetCatalog_Handler,
    		},
    		{
    			MethodName: "ListCatalogs",
    			Handler:    _MetastoreService_ListCatalogs_Handler,
    		},
    		{
    			MethodName: "CreateDatabase",
    			Handler:    _MetastoreService_CreateDatabase_Handler,
    		},
    		{
    			MethodName: "DeleteDatabase",
    			Handler:    _MetastoreService_DeleteDatabase_Handler,
    		},
    		{
    			MethodName: "UpdateDatabase",
    			Handler:    _MetastoreService_UpdateDatabase_Handler,
    		},
    		{
    			MethodName: "GetDatabase",
    			Handler:    _MetastoreService_GetDatabase_Handler,
    		},
    		{
    			MethodName: "ListDatabases",
    			Handler:    _MetastoreService_ListDatabases_Handler,
    		},
    		{
    			MethodName: "CreateTable",
    			Handler:    _MetastoreService_CreateTable_Handler,
    		},
    		{
    			MethodName: "DeleteTable",
    			Handler:    _MetastoreService_DeleteTable_Handler,
    		},
    		{
    			MethodName: "UpdateTable",
    			Handler:    _MetastoreService_UpdateTable_Handler,
    		},
    		{
    			MethodName: "RenameTable",
    			Handler:    _MetastoreService_RenameTable_Handler,
    		},
    		{
    			MethodName: "GetTable",
    			Handler:    _MetastoreService_GetTable_Handler,
    		},
    		{
    			MethodName: "ListTables",
    			Handler:    _MetastoreService_ListTables_Handler,
    		},
    	},
    	Streams:  []grpc.StreamDesc{},
    	Metadata: "google/cloud/bigquery/biglake/v1/metastore.proto",
    }

MetastoreService_ServiceDesc is the grpc.ServiceDesc for MetastoreService service. It's only intended for direct use with grpc.RegisterService, and not to be introspected or modified (even as a copy)

## Functions 

### func RegisterMetastoreServiceServer 
    
    
    func RegisterMetastoreServiceServer(s [grpc](https://pkg.go.dev/google.golang.org/grpc).[ServiceRegistrar](https://pkg.go.dev/google.golang.org/grpc#ServiceRegistrar), srv MetastoreServiceServer)

## Catalog
    
    
    type Catalog struct {
    
    	// Output only. The resource name.
    	// Format:
    	// projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Output only. The creation time of the catalog.
    	CreateTime *timestamppb.Timestamp `protobuf:"bytes,2,opt,name=create_time,json=createTime,proto3" json:"create_time,omitempty"`
    	// Output only. The last modification time of the catalog.
    	UpdateTime *timestamppb.Timestamp `protobuf:"bytes,3,opt,name=update_time,json=updateTime,proto3" json:"update_time,omitempty"`
    	// Output only. The deletion time of the catalog. Only set after the catalog
    	// is deleted.
    	DeleteTime *timestamppb.Timestamp `protobuf:"bytes,4,opt,name=delete_time,json=deleteTime,proto3" json:"delete_time,omitempty"`
    	// Output only. The time when this catalog is considered expired. Only set
    	// after the catalog is deleted.
    	ExpireTime *timestamppb.Timestamp `protobuf:"bytes,5,opt,name=expire_time,json=expireTime,proto3" json:"expire_time,omitempty"`
    	// contains filtered or unexported fields
    }

Catalog is the container of databases.

### func (*Catalog) Descriptor 
    
    
    func (*Catalog) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Catalog.ProtoReflect.Descriptor instead.

### func (*Catalog) GetCreateTime 
    
    
    func (x *Catalog) GetCreateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Catalog) GetDeleteTime 
    
    
    func (x *Catalog) GetDeleteTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Catalog) GetExpireTime 
    
    
    func (x *Catalog) GetExpireTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Catalog) GetName 
    
    
    func (x *Catalog) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*Catalog) GetUpdateTime 
    
    
    func (x *Catalog) GetUpdateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Catalog) ProtoMessage 
    
    
    func (*Catalog) ProtoMessage()

### func (*Catalog) ProtoReflect 
    
    
    func (x *Catalog) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Catalog) Reset 
    
    
    func (x *Catalog) Reset()

### func (*Catalog) String 
    
    
    func (x *Catalog) String() [string](https://pkg.go.dev/builtin#string)

## CreateCatalogRequest
    
    
    type CreateCatalogRequest struct {
    
    	// Required. The parent resource where this catalog will be created.
    	// Format: projects/{project_id_or_number}/locations/{location_id}
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Required. The catalog to create.
    	// The `name` field does not need to be provided.
    	Catalog *Catalog `protobuf:"bytes,2,opt,name=catalog,proto3" json:"catalog,omitempty"`
    	// Required. The ID to use for the catalog, which will become the final
    	// component of the catalog's resource name.
    	CatalogId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=catalog_id,json=catalogId,proto3" json:"catalog_id,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the CreateCatalog method.

### func (*CreateCatalogRequest) Descriptor 
    
    
    func (*CreateCatalogRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CreateCatalogRequest.ProtoReflect.Descriptor instead.

### func (*CreateCatalogRequest) GetCatalog 
    
    
    func (x *CreateCatalogRequest) GetCatalog() *Catalog

### func (*CreateCatalogRequest) GetCatalogId 
    
    
    func (x *CreateCatalogRequest) GetCatalogId() [string](https://pkg.go.dev/builtin#string)

### func (*CreateCatalogRequest) GetParent 
    
    
    func (x *CreateCatalogRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*CreateCatalogRequest) ProtoMessage 
    
    
    func (*CreateCatalogRequest) ProtoMessage()

### func (*CreateCatalogRequest) ProtoReflect 
    
    
    func (x *CreateCatalogRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CreateCatalogRequest) Reset 
    
    
    func (x *CreateCatalogRequest) Reset()

### func (*CreateCatalogRequest) String 
    
    
    func (x *CreateCatalogRequest) String() [string](https://pkg.go.dev/builtin#string)

## CreateDatabaseRequest
    
    
    type CreateDatabaseRequest struct {
    
    	// Required. The parent resource where this database will be created.
    	// Format:
    	// projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Required. The database to create.
    	// The `name` field does not need to be provided.
    	Database *Database `protobuf:"bytes,2,opt,name=database,proto3" json:"database,omitempty"`
    	// Required. The ID to use for the database, which will become the final
    	// component of the database's resource name.
    	DatabaseId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=database_id,json=databaseId,proto3" json:"database_id,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the CreateDatabase method.

### func (*CreateDatabaseRequest) Descriptor 
    
    
    func (*CreateDatabaseRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CreateDatabaseRequest.ProtoReflect.Descriptor instead.

### func (*CreateDatabaseRequest) GetDatabase 
    
    
    func (x *CreateDatabaseRequest) GetDatabase() *Database

### func (*CreateDatabaseRequest) GetDatabaseId 
    
    
    func (x *CreateDatabaseRequest) GetDatabaseId() [string](https://pkg.go.dev/builtin#string)

### func (*CreateDatabaseRequest) GetParent 
    
    
    func (x *CreateDatabaseRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*CreateDatabaseRequest) ProtoMessage 
    
    
    func (*CreateDatabaseRequest) ProtoMessage()

### func (*CreateDatabaseRequest) ProtoReflect 
    
    
    func (x *CreateDatabaseRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CreateDatabaseRequest) Reset 
    
    
    func (x *CreateDatabaseRequest) Reset()

### func (*CreateDatabaseRequest) String 
    
    
    func (x *CreateDatabaseRequest) String() [string](https://pkg.go.dev/builtin#string)

## CreateTableRequest
    
    
    type CreateTableRequest struct {
    
    	// Required. The parent resource where this table will be created.
    	// Format:
    	// projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}/databases/{database_id}
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Required. The table to create. The `name` field does not need to be
    	// provided for the table creation.
    	Table *Table `protobuf:"bytes,2,opt,name=table,proto3" json:"table,omitempty"`
    	// Required. The ID to use for the table, which will become the final
    	// component of the table's resource name.
    	TableId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=table_id,json=tableId,proto3" json:"table_id,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the CreateTable method.

### func (*CreateTableRequest) Descriptor 
    
    
    func (*CreateTableRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CreateTableRequest.ProtoReflect.Descriptor instead.

### func (*CreateTableRequest) GetParent 
    
    
    func (x *CreateTableRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*CreateTableRequest) GetTable 
    
    
    func (x *CreateTableRequest) GetTable() *Table

### func (*CreateTableRequest) GetTableId 
    
    
    func (x *CreateTableRequest) GetTableId() [string](https://pkg.go.dev/builtin#string)

### func (*CreateTableRequest) ProtoMessage 
    
    
    func (*CreateTableRequest) ProtoMessage()

### func (*CreateTableRequest) ProtoReflect 
    
    
    func (x *CreateTableRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CreateTableRequest) Reset 
    
    
    func (x *CreateTableRequest) Reset()

### func (*CreateTableRequest) String 
    
    
    func (x *CreateTableRequest) String() [string](https://pkg.go.dev/builtin#string)

## Database
    
    
    type Database struct {
    
    	// Options specified for the database type.
    	//
    	// Types that are valid to be assigned to Options:
    	//
    	//	*Database_HiveOptions
    	Options isDatabase_Options `protobuf_oneof:"options"`
    	// Output only. The resource name.
    	// Format:
    	// projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}/databases/{database_id}
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Output only. The creation time of the database.
    	CreateTime *timestamppb.Timestamp `protobuf:"bytes,2,opt,name=create_time,json=createTime,proto3" json:"create_time,omitempty"`
    	// Output only. The last modification time of the database.
    	UpdateTime *timestamppb.Timestamp `protobuf:"bytes,3,opt,name=update_time,json=updateTime,proto3" json:"update_time,omitempty"`
    	// Output only. The deletion time of the database. Only set after the database
    	// is deleted.
    	DeleteTime *timestamppb.Timestamp `protobuf:"bytes,4,opt,name=delete_time,json=deleteTime,proto3" json:"delete_time,omitempty"`
    	// Output only. The time when this database is considered expired. Only set
    	// after the database is deleted.
    	ExpireTime *timestamppb.Timestamp `protobuf:"bytes,5,opt,name=expire_time,json=expireTime,proto3" json:"expire_time,omitempty"`
    	// The database type.
    	Type Database_Type `protobuf:"varint,6,opt,name=type,proto3,enum=google.cloud.bigquery.biglake.v1.Database_Type" json:"type,omitempty"`
    	// contains filtered or unexported fields
    }

Database is the container of tables.

### func (*Database) Descriptor 
    
    
    func (*Database) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Database.ProtoReflect.Descriptor instead.

### func (*Database) GetCreateTime 
    
    
    func (x *Database) GetCreateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Database) GetDeleteTime 
    
    
    func (x *Database) GetDeleteTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Database) GetExpireTime 
    
    
    func (x *Database) GetExpireTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Database) GetHiveOptions 
    
    
    func (x *Database) GetHiveOptions() *HiveDatabaseOptions

### func (*Database) GetName 
    
    
    func (x *Database) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*Database) GetOptions 
    
    
    func (x *Database) GetOptions() isDatabase_Options

### func (*Database) GetType 
    
    
    func (x *Database) GetType() Database_Type

### func (*Database) GetUpdateTime 
    
    
    func (x *Database) GetUpdateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Database) ProtoMessage 
    
    
    func (*Database) ProtoMessage()

### func (*Database) ProtoReflect 
    
    
    func (x *Database) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Database) Reset 
    
    
    func (x *Database) Reset()

### func (*Database) String 
    
    
    func (x *Database) String() [string](https://pkg.go.dev/builtin#string)

## Database_HiveOptions
    
    
    type Database_HiveOptions struct {
    	// Options of a Hive database.
    	HiveOptions *HiveDatabaseOptions `protobuf:"bytes,7,opt,name=hive_options,json=hiveOptions,proto3,oneof"`
    }

## Database_Type
    
    
    type Database_Type [int32](https://pkg.go.dev/builtin#int32)

The database type.

### Database_TYPE_UNSPECIFIED, Database_HIVE
    
    
    const (
    	// The type is not specified.
    	Database_TYPE_UNSPECIFIED Database_Type = 0
    	// Represents a database storing tables compatible with Hive Metastore
    	// tables.
    	Database_HIVE Database_Type = 1
    )

### func (Database_Type) Descriptor 
    
    
    func (Database_Type) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Database_Type) Enum 
    
    
    func (x Database_Type) Enum() *Database_Type

### func (Database_Type) EnumDescriptor 
    
    
    func (Database_Type) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Database_Type.Descriptor instead.

### func (Database_Type) Number 
    
    
    func (x Database_Type) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Database_Type) String 
    
    
    func (x Database_Type) String() [string](https://pkg.go.dev/builtin#string)

### func (Database_Type) Type 
    
    
    func (Database_Type) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## DeleteCatalogRequest
    
    
    type DeleteCatalogRequest struct {
    
    	// Required. The name of the catalog to delete.
    	// Format:
    	// projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the DeleteCatalog method.

### func (*DeleteCatalogRequest) Descriptor 
    
    
    func (*DeleteCatalogRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DeleteCatalogRequest.ProtoReflect.Descriptor instead.

### func (*DeleteCatalogRequest) GetName 
    
    
    func (x *DeleteCatalogRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteCatalogRequest) ProtoMessage 
    
    
    func (*DeleteCatalogRequest) ProtoMessage()

### func (*DeleteCatalogRequest) ProtoReflect 
    
    
    func (x *DeleteCatalogRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DeleteCatalogRequest) Reset 
    
    
    func (x *DeleteCatalogRequest) Reset()

### func (*DeleteCatalogRequest) String 
    
    
    func (x *DeleteCatalogRequest) String() [string](https://pkg.go.dev/builtin#string)

## DeleteDatabaseRequest
    
    
    type DeleteDatabaseRequest struct {
    
    	// Required. The name of the database to delete.
    	// Format:
    	// projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}/databases/{database_id}
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the DeleteDatabase method.

### func (*DeleteDatabaseRequest) Descriptor 
    
    
    func (*DeleteDatabaseRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DeleteDatabaseRequest.ProtoReflect.Descriptor instead.

### func (*DeleteDatabaseRequest) GetName 
    
    
    func (x *DeleteDatabaseRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteDatabaseRequest) ProtoMessage 
    
    
    func (*DeleteDatabaseRequest) ProtoMessage()

### func (*DeleteDatabaseRequest) ProtoReflect 
    
    
    func (x *DeleteDatabaseRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DeleteDatabaseRequest) Reset 
    
    
    func (x *DeleteDatabaseRequest) Reset()

### func (*DeleteDatabaseRequest) String 
    
    
    func (x *DeleteDatabaseRequest) String() [string](https://pkg.go.dev/builtin#string)

## DeleteTableRequest
    
    
    type DeleteTableRequest struct {
    
    	// Required. The name of the table to delete.
    	// Format:
    	// projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}/databases/{database_id}/tables/{table_id}
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the DeleteTable method.

### func (*DeleteTableRequest) Descriptor 
    
    
    func (*DeleteTableRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use DeleteTableRequest.ProtoReflect.Descriptor instead.

### func (*DeleteTableRequest) GetName 
    
    
    func (x *DeleteTableRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*DeleteTableRequest) ProtoMessage 
    
    
    func (*DeleteTableRequest) ProtoMessage()

### func (*DeleteTableRequest) ProtoReflect 
    
    
    func (x *DeleteTableRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*DeleteTableRequest) Reset 
    
    
    func (x *DeleteTableRequest) Reset()

### func (*DeleteTableRequest) String 
    
    
    func (x *DeleteTableRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetCatalogRequest
    
    
    type GetCatalogRequest struct {
    
    	// Required. The name of the catalog to retrieve.
    	// Format:
    	// projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the GetCatalog method.

### func (*GetCatalogRequest) Descriptor 
    
    
    func (*GetCatalogRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetCatalogRequest.ProtoReflect.Descriptor instead.

### func (*GetCatalogRequest) GetName 
    
    
    func (x *GetCatalogRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetCatalogRequest) ProtoMessage 
    
    
    func (*GetCatalogRequest) ProtoMessage()

### func (*GetCatalogRequest) ProtoReflect 
    
    
    func (x *GetCatalogRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetCatalogRequest) Reset 
    
    
    func (x *GetCatalogRequest) Reset()

### func (*GetCatalogRequest) String 
    
    
    func (x *GetCatalogRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetDatabaseRequest
    
    
    type GetDatabaseRequest struct {
    
    	// Required. The name of the database to retrieve.
    	// Format:
    	// projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}/databases/{database_id}
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the GetDatabase method.

### func (*GetDatabaseRequest) Descriptor 
    
    
    func (*GetDatabaseRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetDatabaseRequest.ProtoReflect.Descriptor instead.

### func (*GetDatabaseRequest) GetName 
    
    
    func (x *GetDatabaseRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetDatabaseRequest) ProtoMessage 
    
    
    func (*GetDatabaseRequest) ProtoMessage()

### func (*GetDatabaseRequest) ProtoReflect 
    
    
    func (x *GetDatabaseRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetDatabaseRequest) Reset 
    
    
    func (x *GetDatabaseRequest) Reset()

### func (*GetDatabaseRequest) String 
    
    
    func (x *GetDatabaseRequest) String() [string](https://pkg.go.dev/builtin#string)

## GetTableRequest
    
    
    type GetTableRequest struct {
    
    	// Required. The name of the table to retrieve.
    	// Format:
    	// projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}/databases/{database_id}/tables/{table_id}
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the GetTable method.

### func (*GetTableRequest) Descriptor 
    
    
    func (*GetTableRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use GetTableRequest.ProtoReflect.Descriptor instead.

### func (*GetTableRequest) GetName 
    
    
    func (x *GetTableRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*GetTableRequest) ProtoMessage 
    
    
    func (*GetTableRequest) ProtoMessage()

### func (*GetTableRequest) ProtoReflect 
    
    
    func (x *GetTableRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*GetTableRequest) Reset 
    
    
    func (x *GetTableRequest) Reset()

### func (*GetTableRequest) String 
    
    
    func (x *GetTableRequest) String() [string](https://pkg.go.dev/builtin#string)

## HiveDatabaseOptions
    
    
    type HiveDatabaseOptions struct {
    
    	// Cloud Storage folder URI where the database data is stored, starting with
    	// "gs://".
    	LocationUri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=location_uri,json=locationUri,proto3" json:"location_uri,omitempty"`
    	// Stores user supplied Hive database parameters.
    	Parameters map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,rep,name=parameters,proto3" json:"parameters,omitempty" protobuf_key:"bytes,1,opt,name=key" protobuf_val:"bytes,2,opt,name=value"`
    	// contains filtered or unexported fields
    }

Options of a Hive database.

### func (*HiveDatabaseOptions) Descriptor 
    
    
    func (*HiveDatabaseOptions) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use HiveDatabaseOptions.ProtoReflect.Descriptor instead.

### func (*HiveDatabaseOptions) GetLocationUri 
    
    
    func (x *HiveDatabaseOptions) GetLocationUri() [string](https://pkg.go.dev/builtin#string)

### func (*HiveDatabaseOptions) GetParameters 
    
    
    func (x *HiveDatabaseOptions) GetParameters() map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string)

### func (*HiveDatabaseOptions) ProtoMessage 
    
    
    func (*HiveDatabaseOptions) ProtoMessage()

### func (*HiveDatabaseOptions) ProtoReflect 
    
    
    func (x *HiveDatabaseOptions) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*HiveDatabaseOptions) Reset 
    
    
    func (x *HiveDatabaseOptions) Reset()

### func (*HiveDatabaseOptions) String 
    
    
    func (x *HiveDatabaseOptions) String() [string](https://pkg.go.dev/builtin#string)

## HiveTableOptions
    
    
    type HiveTableOptions struct {
    
    	// Stores user supplied Hive table parameters.
    	Parameters map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,rep,name=parameters,proto3" json:"parameters,omitempty" protobuf_key:"bytes,1,opt,name=key" protobuf_val:"bytes,2,opt,name=value"`
    	// Hive table type. For example, MANAGED_TABLE, EXTERNAL_TABLE.
    	TableType [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=table_type,json=tableType,proto3" json:"table_type,omitempty"`
    	// Stores physical storage information of the data.
    	StorageDescriptor *HiveTableOptions_StorageDescriptor `protobuf:"bytes,3,opt,name=storage_descriptor,json=storageDescriptor,proto3" json:"storage_descriptor,omitempty"`
    	// contains filtered or unexported fields
    }

Options of a Hive table.

### func (*HiveTableOptions) Descriptor 
    
    
    func (*HiveTableOptions) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use HiveTableOptions.ProtoReflect.Descriptor instead.

### func (*HiveTableOptions) GetParameters 
    
    
    func (x *HiveTableOptions) GetParameters() map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string)

### func (*HiveTableOptions) GetStorageDescriptor 
    
    
    func (x *HiveTableOptions) GetStorageDescriptor() *HiveTableOptions_StorageDescriptor

### func (*HiveTableOptions) GetTableType 
    
    
    func (x *HiveTableOptions) GetTableType() [string](https://pkg.go.dev/builtin#string)

### func (*HiveTableOptions) ProtoMessage 
    
    
    func (*HiveTableOptions) ProtoMessage()

### func (*HiveTableOptions) ProtoReflect 
    
    
    func (x *HiveTableOptions) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*HiveTableOptions) Reset 
    
    
    func (x *HiveTableOptions) Reset()

### func (*HiveTableOptions) String 
    
    
    func (x *HiveTableOptions) String() [string](https://pkg.go.dev/builtin#string)

## HiveTableOptions_SerDeInfo
    
    
    type HiveTableOptions_SerDeInfo struct {
    
    	// The fully qualified Java class name of the serialization library.
    	SerializationLib [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=serialization_lib,json=serializationLib,proto3" json:"serialization_lib,omitempty"`
    	// contains filtered or unexported fields
    }

Serializer and deserializer information.

### func (*HiveTableOptions_SerDeInfo) Descriptor 
    
    
    func (*HiveTableOptions_SerDeInfo) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use HiveTableOptions_SerDeInfo.ProtoReflect.Descriptor instead.

### func (*HiveTableOptions_SerDeInfo) GetSerializationLib 
    
    
    func (x *HiveTableOptions_SerDeInfo) GetSerializationLib() [string](https://pkg.go.dev/builtin#string)

### func (*HiveTableOptions_SerDeInfo) ProtoMessage 
    
    
    func (*HiveTableOptions_SerDeInfo) ProtoMessage()

### func (*HiveTableOptions_SerDeInfo) ProtoReflect 
    
    
    func (x *HiveTableOptions_SerDeInfo) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*HiveTableOptions_SerDeInfo) Reset 
    
    
    func (x *HiveTableOptions_SerDeInfo) Reset()

### func (*HiveTableOptions_SerDeInfo) String 
    
    
    func (x *HiveTableOptions_SerDeInfo) String() [string](https://pkg.go.dev/builtin#string)

## HiveTableOptions_StorageDescriptor
    
    
    type HiveTableOptions_StorageDescriptor struct {
    
    	// Cloud Storage folder URI where the table data is stored, starting with
    	// "gs://".
    	LocationUri [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=location_uri,json=locationUri,proto3" json:"location_uri,omitempty"`
    	// The fully qualified Java class name of the input format.
    	InputFormat [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=input_format,json=inputFormat,proto3" json:"input_format,omitempty"`
    	// The fully qualified Java class name of the output format.
    	OutputFormat [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=output_format,json=outputFormat,proto3" json:"output_format,omitempty"`
    	// Serializer and deserializer information.
    	SerdeInfo *HiveTableOptions_SerDeInfo `protobuf:"bytes,4,opt,name=serde_info,json=serdeInfo,proto3" json:"serde_info,omitempty"`
    	// contains filtered or unexported fields
    }

Stores physical storage information of the data.

### func (*HiveTableOptions_StorageDescriptor) Descriptor 
    
    
    func (*HiveTableOptions_StorageDescriptor) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use HiveTableOptions_StorageDescriptor.ProtoReflect.Descriptor instead.

### func (*HiveTableOptions_StorageDescriptor) GetInputFormat 
    
    
    func (x *HiveTableOptions_StorageDescriptor) GetInputFormat() [string](https://pkg.go.dev/builtin#string)

### func (*HiveTableOptions_StorageDescriptor) GetLocationUri 
    
    
    func (x *HiveTableOptions_StorageDescriptor) GetLocationUri() [string](https://pkg.go.dev/builtin#string)

### func (*HiveTableOptions_StorageDescriptor) GetOutputFormat 
    
    
    func (x *HiveTableOptions_StorageDescriptor) GetOutputFormat() [string](https://pkg.go.dev/builtin#string)

### func (*HiveTableOptions_StorageDescriptor) GetSerdeInfo 
    
    
    func (x *HiveTableOptions_StorageDescriptor) GetSerdeInfo() *HiveTableOptions_SerDeInfo

### func (*HiveTableOptions_StorageDescriptor) ProtoMessage 
    
    
    func (*HiveTableOptions_StorageDescriptor) ProtoMessage()

### func (*HiveTableOptions_StorageDescriptor) ProtoReflect 
    
    
    func (x *HiveTableOptions_StorageDescriptor) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*HiveTableOptions_StorageDescriptor) Reset 
    
    
    func (x *HiveTableOptions_StorageDescriptor) Reset()

### func (*HiveTableOptions_StorageDescriptor) String 
    
    
    func (x *HiveTableOptions_StorageDescriptor) String() [string](https://pkg.go.dev/builtin#string)

## ListCatalogsRequest
    
    
    type ListCatalogsRequest struct {
    
    	// Required. The parent, which owns this collection of catalogs.
    	// Format: projects/{project_id_or_number}/locations/{location_id}
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// The maximum number of catalogs to return. The service may return fewer than
    	// this value.
    	// If unspecified, at most 50 catalogs will be returned.
    	// The maximum value is 1000; values above 1000 will be coerced to 1000.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// A page token, received from a previous `ListCatalogs` call.
    	// Provide this to retrieve the subsequent page.
    	//
    	// When paginating, all other parameters provided to `ListCatalogs` must match
    	// the call that provided the page token.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the ListCatalogs method.

### func (*ListCatalogsRequest) Descriptor 
    
    
    func (*ListCatalogsRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListCatalogsRequest.ProtoReflect.Descriptor instead.

### func (*ListCatalogsRequest) GetPageSize 
    
    
    func (x *ListCatalogsRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListCatalogsRequest) GetPageToken 
    
    
    func (x *ListCatalogsRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListCatalogsRequest) GetParent 
    
    
    func (x *ListCatalogsRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListCatalogsRequest) ProtoMessage 
    
    
    func (*ListCatalogsRequest) ProtoMessage()

### func (*ListCatalogsRequest) ProtoReflect 
    
    
    func (x *ListCatalogsRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListCatalogsRequest) Reset 
    
    
    func (x *ListCatalogsRequest) Reset()

### func (*ListCatalogsRequest) String 
    
    
    func (x *ListCatalogsRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListCatalogsResponse
    
    
    type ListCatalogsResponse struct {
    
    	// The catalogs from the specified project.
    	Catalogs []*Catalog `protobuf:"bytes,1,rep,name=catalogs,proto3" json:"catalogs,omitempty"`
    	// A token, which can be sent as `page_token` to retrieve the next page.
    	// If this field is omitted, there are no subsequent pages.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Response message for the ListCatalogs method.

### func (*ListCatalogsResponse) Descriptor 
    
    
    func (*ListCatalogsResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListCatalogsResponse.ProtoReflect.Descriptor instead.

### func (*ListCatalogsResponse) GetCatalogs 
    
    
    func (x *ListCatalogsResponse) GetCatalogs() []*Catalog

### func (*ListCatalogsResponse) GetNextPageToken 
    
    
    func (x *ListCatalogsResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListCatalogsResponse) ProtoMessage 
    
    
    func (*ListCatalogsResponse) ProtoMessage()

### func (*ListCatalogsResponse) ProtoReflect 
    
    
    func (x *ListCatalogsResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListCatalogsResponse) Reset 
    
    
    func (x *ListCatalogsResponse) Reset()

### func (*ListCatalogsResponse) String 
    
    
    func (x *ListCatalogsResponse) String() [string](https://pkg.go.dev/builtin#string)

## ListDatabasesRequest
    
    
    type ListDatabasesRequest struct {
    
    	// Required. The parent, which owns this collection of databases.
    	// Format:
    	// projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// The maximum number of databases to return. The service may return fewer
    	// than this value.
    	// If unspecified, at most 50 databases will be returned.
    	// The maximum value is 1000; values above 1000 will be coerced to 1000.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// A page token, received from a previous `ListDatabases` call.
    	// Provide this to retrieve the subsequent page.
    	//
    	// When paginating, all other parameters provided to `ListDatabases` must
    	// match the call that provided the page token.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the ListDatabases method.

### func (*ListDatabasesRequest) Descriptor 
    
    
    func (*ListDatabasesRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListDatabasesRequest.ProtoReflect.Descriptor instead.

### func (*ListDatabasesRequest) GetPageSize 
    
    
    func (x *ListDatabasesRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListDatabasesRequest) GetPageToken 
    
    
    func (x *ListDatabasesRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListDatabasesRequest) GetParent 
    
    
    func (x *ListDatabasesRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListDatabasesRequest) ProtoMessage 
    
    
    func (*ListDatabasesRequest) ProtoMessage()

### func (*ListDatabasesRequest) ProtoReflect 
    
    
    func (x *ListDatabasesRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListDatabasesRequest) Reset 
    
    
    func (x *ListDatabasesRequest) Reset()

### func (*ListDatabasesRequest) String 
    
    
    func (x *ListDatabasesRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListDatabasesResponse
    
    
    type ListDatabasesResponse struct {
    
    	// The databases from the specified catalog.
    	Databases []*Database `protobuf:"bytes,1,rep,name=databases,proto3" json:"databases,omitempty"`
    	// A token, which can be sent as `page_token` to retrieve the next page.
    	// If this field is omitted, there are no subsequent pages.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Response message for the ListDatabases method.

### func (*ListDatabasesResponse) Descriptor 
    
    
    func (*ListDatabasesResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListDatabasesResponse.ProtoReflect.Descriptor instead.

### func (*ListDatabasesResponse) GetDatabases 
    
    
    func (x *ListDatabasesResponse) GetDatabases() []*Database

### func (*ListDatabasesResponse) GetNextPageToken 
    
    
    func (x *ListDatabasesResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListDatabasesResponse) ProtoMessage 
    
    
    func (*ListDatabasesResponse) ProtoMessage()

### func (*ListDatabasesResponse) ProtoReflect 
    
    
    func (x *ListDatabasesResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListDatabasesResponse) Reset 
    
    
    func (x *ListDatabasesResponse) Reset()

### func (*ListDatabasesResponse) String 
    
    
    func (x *ListDatabasesResponse) String() [string](https://pkg.go.dev/builtin#string)

## ListTablesRequest
    
    
    type ListTablesRequest struct {
    
    	// Required. The parent, which owns this collection of tables.
    	// Format:
    	// projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}/databases/{database_id}
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// The maximum number of tables to return. The service may return fewer than
    	// this value.
    	// If unspecified, at most 50 tables will be returned.
    	// The maximum value is 1000; values above 1000 will be coerced to 1000.
    	PageSize [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
    	// A page token, received from a previous `ListTables` call.
    	// Provide this to retrieve the subsequent page.
    	//
    	// When paginating, all other parameters provided to `ListTables` must match
    	// the call that provided the page token.
    	PageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
    	// The view for the returned tables.
    	View TableView `protobuf:"varint,4,opt,name=view,proto3,enum=google.cloud.bigquery.biglake.v1.TableView" json:"view,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the ListTables method.

### func (*ListTablesRequest) Descriptor 
    
    
    func (*ListTablesRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListTablesRequest.ProtoReflect.Descriptor instead.

### func (*ListTablesRequest) GetPageSize 
    
    
    func (x *ListTablesRequest) GetPageSize() [int32](https://pkg.go.dev/builtin#int32)

### func (*ListTablesRequest) GetPageToken 
    
    
    func (x *ListTablesRequest) GetPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListTablesRequest) GetParent 
    
    
    func (x *ListTablesRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*ListTablesRequest) GetView 
    
    
    func (x *ListTablesRequest) GetView() TableView

### func (*ListTablesRequest) ProtoMessage 
    
    
    func (*ListTablesRequest) ProtoMessage()

### func (*ListTablesRequest) ProtoReflect 
    
    
    func (x *ListTablesRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListTablesRequest) Reset 
    
    
    func (x *ListTablesRequest) Reset()

### func (*ListTablesRequest) String 
    
    
    func (x *ListTablesRequest) String() [string](https://pkg.go.dev/builtin#string)

## ListTablesResponse
    
    
    type ListTablesResponse struct {
    
    	// The tables from the specified database.
    	Tables []*Table `protobuf:"bytes,1,rep,name=tables,proto3" json:"tables,omitempty"`
    	// A token, which can be sent as `page_token` to retrieve the next page.
    	// If this field is omitted, there are no subsequent pages.
    	NextPageToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
    	// contains filtered or unexported fields
    }

Response message for the ListTables method.

### func (*ListTablesResponse) Descriptor 
    
    
    func (*ListTablesResponse) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ListTablesResponse.ProtoReflect.Descriptor instead.

### func (*ListTablesResponse) GetNextPageToken 
    
    
    func (x *ListTablesResponse) GetNextPageToken() [string](https://pkg.go.dev/builtin#string)

### func (*ListTablesResponse) GetTables 
    
    
    func (x *ListTablesResponse) GetTables() []*Table

### func (*ListTablesResponse) ProtoMessage 
    
    
    func (*ListTablesResponse) ProtoMessage()

### func (*ListTablesResponse) ProtoReflect 
    
    
    func (x *ListTablesResponse) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*ListTablesResponse) Reset 
    
    
    func (x *ListTablesResponse) Reset()

### func (*ListTablesResponse) String 
    
    
    func (x *ListTablesResponse) String() [string](https://pkg.go.dev/builtin#string)

## MetastoreServiceClient
    
    
    type MetastoreServiceClient interface {
    	// Creates a new catalog.
    	CreateCatalog(ctx context.Context, in *CreateCatalogRequest, opts ...grpc.CallOption) (*Catalog, [error](https://pkg.go.dev/builtin#error))
    	// Deletes an existing catalog specified by the catalog ID.
    	DeleteCatalog(ctx context.Context, in *DeleteCatalogRequest, opts ...grpc.CallOption) (*Catalog, [error](https://pkg.go.dev/builtin#error))
    	// Gets the catalog specified by the resource name.
    	GetCatalog(ctx context.Context, in *GetCatalogRequest, opts ...grpc.CallOption) (*Catalog, [error](https://pkg.go.dev/builtin#error))
    	// List all catalogs in a specified project.
    	ListCatalogs(ctx context.Context, in *ListCatalogsRequest, opts ...grpc.CallOption) (*ListCatalogsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Creates a new database.
    	CreateDatabase(ctx context.Context, in *CreateDatabaseRequest, opts ...grpc.CallOption) (*Database, [error](https://pkg.go.dev/builtin#error))
    	// Deletes an existing database specified by the database ID.
    	DeleteDatabase(ctx context.Context, in *DeleteDatabaseRequest, opts ...grpc.CallOption) (*Database, [error](https://pkg.go.dev/builtin#error))
    	// Updates an existing database specified by the database ID.
    	UpdateDatabase(ctx context.Context, in *UpdateDatabaseRequest, opts ...grpc.CallOption) (*Database, [error](https://pkg.go.dev/builtin#error))
    	// Gets the database specified by the resource name.
    	GetDatabase(ctx context.Context, in *GetDatabaseRequest, opts ...grpc.CallOption) (*Database, [error](https://pkg.go.dev/builtin#error))
    	// List all databases in a specified catalog.
    	ListDatabases(ctx context.Context, in *ListDatabasesRequest, opts ...grpc.CallOption) (*ListDatabasesResponse, [error](https://pkg.go.dev/builtin#error))
    	// Creates a new table.
    	CreateTable(ctx context.Context, in *CreateTableRequest, opts ...grpc.CallOption) (*Table, [error](https://pkg.go.dev/builtin#error))
    	// Deletes an existing table specified by the table ID.
    	DeleteTable(ctx context.Context, in *DeleteTableRequest, opts ...grpc.CallOption) (*Table, [error](https://pkg.go.dev/builtin#error))
    	// Updates an existing table specified by the table ID.
    	UpdateTable(ctx context.Context, in *UpdateTableRequest, opts ...grpc.CallOption) (*Table, [error](https://pkg.go.dev/builtin#error))
    	// Renames an existing table specified by the table ID.
    	RenameTable(ctx context.Context, in *RenameTableRequest, opts ...grpc.CallOption) (*Table, [error](https://pkg.go.dev/builtin#error))
    	// Gets the table specified by the resource name.
    	GetTable(ctx context.Context, in *GetTableRequest, opts ...grpc.CallOption) (*Table, [error](https://pkg.go.dev/builtin#error))
    	// List all tables in a specified database.
    	ListTables(ctx context.Context, in *ListTablesRequest, opts ...grpc.CallOption) (*ListTablesResponse, [error](https://pkg.go.dev/builtin#error))
    }

MetastoreServiceClient is the client API for MetastoreService service.

For semantics around ctx use and closing/ending streaming RPCs, please refer to <https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream>.

### func NewMetastoreServiceClient 
    
    
    func NewMetastoreServiceClient(cc [grpc](https://pkg.go.dev/google.golang.org/grpc).[ClientConnInterface](https://pkg.go.dev/google.golang.org/grpc#ClientConnInterface)) MetastoreServiceClient

## MetastoreServiceServer
    
    
    type MetastoreServiceServer interface {
    	// Creates a new catalog.
    	CreateCatalog(context.Context, *CreateCatalogRequest) (*Catalog, [error](https://pkg.go.dev/builtin#error))
    	// Deletes an existing catalog specified by the catalog ID.
    	DeleteCatalog(context.Context, *DeleteCatalogRequest) (*Catalog, [error](https://pkg.go.dev/builtin#error))
    	// Gets the catalog specified by the resource name.
    	GetCatalog(context.Context, *GetCatalogRequest) (*Catalog, [error](https://pkg.go.dev/builtin#error))
    	// List all catalogs in a specified project.
    	ListCatalogs(context.Context, *ListCatalogsRequest) (*ListCatalogsResponse, [error](https://pkg.go.dev/builtin#error))
    	// Creates a new database.
    	CreateDatabase(context.Context, *CreateDatabaseRequest) (*Database, [error](https://pkg.go.dev/builtin#error))
    	// Deletes an existing database specified by the database ID.
    	DeleteDatabase(context.Context, *DeleteDatabaseRequest) (*Database, [error](https://pkg.go.dev/builtin#error))
    	// Updates an existing database specified by the database ID.
    	UpdateDatabase(context.Context, *UpdateDatabaseRequest) (*Database, [error](https://pkg.go.dev/builtin#error))
    	// Gets the database specified by the resource name.
    	GetDatabase(context.Context, *GetDatabaseRequest) (*Database, [error](https://pkg.go.dev/builtin#error))
    	// List all databases in a specified catalog.
    	ListDatabases(context.Context, *ListDatabasesRequest) (*ListDatabasesResponse, [error](https://pkg.go.dev/builtin#error))
    	// Creates a new table.
    	CreateTable(context.Context, *CreateTableRequest) (*Table, [error](https://pkg.go.dev/builtin#error))
    	// Deletes an existing table specified by the table ID.
    	DeleteTable(context.Context, *DeleteTableRequest) (*Table, [error](https://pkg.go.dev/builtin#error))
    	// Updates an existing table specified by the table ID.
    	UpdateTable(context.Context, *UpdateTableRequest) (*Table, [error](https://pkg.go.dev/builtin#error))
    	// Renames an existing table specified by the table ID.
    	RenameTable(context.Context, *RenameTableRequest) (*Table, [error](https://pkg.go.dev/builtin#error))
    	// Gets the table specified by the resource name.
    	GetTable(context.Context, *GetTableRequest) (*Table, [error](https://pkg.go.dev/builtin#error))
    	// List all tables in a specified database.
    	ListTables(context.Context, *ListTablesRequest) (*ListTablesResponse, [error](https://pkg.go.dev/builtin#error))
    }

MetastoreServiceServer is the server API for MetastoreService service. All implementations should embed UnimplementedMetastoreServiceServer for forward compatibility

## RenameTableRequest
    
    
    type RenameTableRequest struct {
    
    	// Required. The table's `name` field is used to identify the table to rename.
    	// Format:
    	// projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}/databases/{database_id}/tables/{table_id}
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Required. The new `name` for the specified table, must be in the same
    	// database. Format:
    	// projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}/databases/{database_id}/tables/{table_id}
    	NewName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=new_name,json=newName,proto3" json:"new_name,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the RenameTable method in MetastoreService

### func (*RenameTableRequest) Descriptor 
    
    
    func (*RenameTableRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use RenameTableRequest.ProtoReflect.Descriptor instead.

### func (*RenameTableRequest) GetName 
    
    
    func (x *RenameTableRequest) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*RenameTableRequest) GetNewName 
    
    
    func (x *RenameTableRequest) GetNewName() [string](https://pkg.go.dev/builtin#string)

### func (*RenameTableRequest) ProtoMessage 
    
    
    func (*RenameTableRequest) ProtoMessage()

### func (*RenameTableRequest) ProtoReflect 
    
    
    func (x *RenameTableRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*RenameTableRequest) Reset 
    
    
    func (x *RenameTableRequest) Reset()

### func (*RenameTableRequest) String 
    
    
    func (x *RenameTableRequest) String() [string](https://pkg.go.dev/builtin#string)

## Table
    
    
    type Table struct {
    
    	// Options specified for the table type.
    	//
    	// Types that are valid to be assigned to Options:
    	//
    	//	*Table_HiveOptions
    	Options isTable_Options `protobuf_oneof:"options"`
    	// Output only. The resource name.
    	// Format:
    	// projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}/databases/{database_id}/tables/{table_id}
    	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
    	// Output only. The creation time of the table.
    	CreateTime *timestamppb.Timestamp `protobuf:"bytes,2,opt,name=create_time,json=createTime,proto3" json:"create_time,omitempty"`
    	// Output only. The last modification time of the table.
    	UpdateTime *timestamppb.Timestamp `protobuf:"bytes,3,opt,name=update_time,json=updateTime,proto3" json:"update_time,omitempty"`
    	// Output only. The deletion time of the table. Only set after the table is
    	// deleted.
    	DeleteTime *timestamppb.Timestamp `protobuf:"bytes,4,opt,name=delete_time,json=deleteTime,proto3" json:"delete_time,omitempty"`
    	// Output only. The time when this table is considered expired. Only set after
    	// the table is deleted.
    	ExpireTime *timestamppb.Timestamp `protobuf:"bytes,5,opt,name=expire_time,json=expireTime,proto3" json:"expire_time,omitempty"`
    	// The table type.
    	Type Table_Type `protobuf:"varint,6,opt,name=type,proto3,enum=google.cloud.bigquery.biglake.v1.Table_Type" json:"type,omitempty"`
    	// The checksum of a table object computed by the server based on the value of
    	// other fields. It may be sent on update requests to ensure the client has an
    	// up-to-date value before proceeding. It is only checked for update table
    	// operations.
    	Etag [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,8,opt,name=etag,proto3" json:"etag,omitempty"`
    	// contains filtered or unexported fields
    }

Represents a table.

### func (*Table) Descriptor 
    
    
    func (*Table) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Table.ProtoReflect.Descriptor instead.

### func (*Table) GetCreateTime 
    
    
    func (x *Table) GetCreateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Table) GetDeleteTime 
    
    
    func (x *Table) GetDeleteTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Table) GetEtag 
    
    
    func (x *Table) GetEtag() [string](https://pkg.go.dev/builtin#string)

### func (*Table) GetExpireTime 
    
    
    func (x *Table) GetExpireTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Table) GetHiveOptions 
    
    
    func (x *Table) GetHiveOptions() *HiveTableOptions

### func (*Table) GetName 
    
    
    func (x *Table) GetName() [string](https://pkg.go.dev/builtin#string)

### func (*Table) GetOptions 
    
    
    func (x *Table) GetOptions() isTable_Options

### func (*Table) GetType 
    
    
    func (x *Table) GetType() Table_Type

### func (*Table) GetUpdateTime 
    
    
    func (x *Table) GetUpdateTime() *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp)

### func (*Table) ProtoMessage 
    
    
    func (*Table) ProtoMessage()

### func (*Table) ProtoReflect 
    
    
    func (x *Table) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*Table) Reset 
    
    
    func (x *Table) Reset()

### func (*Table) String 
    
    
    func (x *Table) String() [string](https://pkg.go.dev/builtin#string)

## TableView
    
    
    type TableView [int32](https://pkg.go.dev/builtin#int32)

View on Table. Represents which fields will be populated for calls that return Table objects.

### TableView_TABLE_VIEW_UNSPECIFIED, TableView_BASIC, TableView_FULL
    
    
    const (
    	// Default value. The API will default to the BASIC view.
    	TableView_TABLE_VIEW_UNSPECIFIED TableView = 0
    	// Include only table names.
    	// This is the default value.
    	TableView_BASIC TableView = 1
    	// Include everything.
    	TableView_FULL TableView = 2
    )

### func (TableView) Descriptor 
    
    
    func (TableView) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (TableView) Enum 
    
    
    func (x TableView) Enum() *TableView

### func (TableView) EnumDescriptor 
    
    
    func (TableView) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use TableView.Descriptor instead.

### func (TableView) Number 
    
    
    func (x TableView) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (TableView) String 
    
    
    func (x TableView) String() [string](https://pkg.go.dev/builtin#string)

### func (TableView) Type 
    
    
    func (TableView) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## Table_HiveOptions
    
    
    type Table_HiveOptions struct {
    	// Options of a Hive table.
    	HiveOptions *HiveTableOptions `protobuf:"bytes,7,opt,name=hive_options,json=hiveOptions,proto3,oneof"`
    }

## Table_Type
    
    
    type Table_Type [int32](https://pkg.go.dev/builtin#int32)

The table type.

### Table_TYPE_UNSPECIFIED, Table_HIVE
    
    
    const (
    	// The type is not specified.
    	Table_TYPE_UNSPECIFIED Table_Type = 0
    	// Represents a table compatible with Hive Metastore tables.
    	Table_HIVE Table_Type = 1
    )

### func (Table_Type) Descriptor 
    
    
    func (Table_Type) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (Table_Type) Enum 
    
    
    func (x Table_Type) Enum() *Table_Type

### func (Table_Type) EnumDescriptor 
    
    
    func (Table_Type) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Table_Type.Descriptor instead.

### func (Table_Type) Number 
    
    
    func (x Table_Type) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (Table_Type) String 
    
    
    func (x Table_Type) String() [string](https://pkg.go.dev/builtin#string)

### func (Table_Type) Type 
    
    
    func (Table_Type) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## UnimplementedMetastoreServiceServer
    
    
    type UnimplementedMetastoreServiceServer struct {
    }

UnimplementedMetastoreServiceServer should be embedded to have forward compatible implementations.

### func (UnimplementedMetastoreServiceServer) CreateCatalog 
    
    
    func (UnimplementedMetastoreServiceServer) CreateCatalog([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *CreateCatalogRequest) (*Catalog, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMetastoreServiceServer) CreateDatabase 
    
    
    func (UnimplementedMetastoreServiceServer) CreateDatabase([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *CreateDatabaseRequest) (*Database, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMetastoreServiceServer) CreateTable 
    
    
    func (UnimplementedMetastoreServiceServer) CreateTable([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *CreateTableRequest) (*Table, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMetastoreServiceServer) DeleteCatalog 
    
    
    func (UnimplementedMetastoreServiceServer) DeleteCatalog([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *DeleteCatalogRequest) (*Catalog, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMetastoreServiceServer) DeleteDatabase 
    
    
    func (UnimplementedMetastoreServiceServer) DeleteDatabase([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *DeleteDatabaseRequest) (*Database, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMetastoreServiceServer) DeleteTable 
    
    
    func (UnimplementedMetastoreServiceServer) DeleteTable([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *DeleteTableRequest) (*Table, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMetastoreServiceServer) GetCatalog 
    
    
    func (UnimplementedMetastoreServiceServer) GetCatalog([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetCatalogRequest) (*Catalog, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMetastoreServiceServer) GetDatabase 
    
    
    func (UnimplementedMetastoreServiceServer) GetDatabase([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetDatabaseRequest) (*Database, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMetastoreServiceServer) GetTable 
    
    
    func (UnimplementedMetastoreServiceServer) GetTable([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *GetTableRequest) (*Table, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMetastoreServiceServer) ListCatalogs 
    
    
    func (UnimplementedMetastoreServiceServer) ListCatalogs([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListCatalogsRequest) (*ListCatalogsResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMetastoreServiceServer) ListDatabases 
    
    
    func (UnimplementedMetastoreServiceServer) ListDatabases([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListDatabasesRequest) (*ListDatabasesResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMetastoreServiceServer) ListTables 
    
    
    func (UnimplementedMetastoreServiceServer) ListTables([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *ListTablesRequest) (*ListTablesResponse, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMetastoreServiceServer) RenameTable 
    
    
    func (UnimplementedMetastoreServiceServer) RenameTable([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *RenameTableRequest) (*Table, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMetastoreServiceServer) UpdateDatabase 
    
    
    func (UnimplementedMetastoreServiceServer) UpdateDatabase([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *UpdateDatabaseRequest) (*Database, [error](https://pkg.go.dev/builtin#error))

### func (UnimplementedMetastoreServiceServer) UpdateTable 
    
    
    func (UnimplementedMetastoreServiceServer) UpdateTable([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *UpdateTableRequest) (*Table, [error](https://pkg.go.dev/builtin#error))

## UnsafeMetastoreServiceServer
    
    
    type UnsafeMetastoreServiceServer interface {
    	// contains filtered or unexported methods
    }

UnsafeMetastoreServiceServer may be embedded to opt out of forward compatibility for this service. Use of this interface is not recommended, as added methods to MetastoreServiceServer will result in compilation errors.

## UpdateDatabaseRequest
    
    
    type UpdateDatabaseRequest struct {
    
    	// Required. The database to update.
    	//
    	// The database's `name` field is used to identify the database to update.
    	// Format:
    	// projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}/databases/{database_id}
    	Database *Database `protobuf:"bytes,1,opt,name=database,proto3" json:"database,omitempty"`
    	// The list of fields to update.
    	//
    	// For the `FieldMask` definition, see
    	// https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask
    	// If not set, defaults to all of the fields that are allowed to update.
    	UpdateMask *fieldmaskpb.FieldMask `protobuf:"bytes,2,opt,name=update_mask,json=updateMask,proto3" json:"update_mask,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the UpdateDatabase method.

### func (*UpdateDatabaseRequest) Descriptor 
    
    
    func (*UpdateDatabaseRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UpdateDatabaseRequest.ProtoReflect.Descriptor instead.

### func (*UpdateDatabaseRequest) GetDatabase 
    
    
    func (x *UpdateDatabaseRequest) GetDatabase() *Database

### func (*UpdateDatabaseRequest) GetUpdateMask 
    
    
    func (x *UpdateDatabaseRequest) GetUpdateMask() *[fieldmaskpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb).[FieldMask](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb#FieldMask)

### func (*UpdateDatabaseRequest) ProtoMessage 
    
    
    func (*UpdateDatabaseRequest) ProtoMessage()

### func (*UpdateDatabaseRequest) ProtoReflect 
    
    
    func (x *UpdateDatabaseRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UpdateDatabaseRequest) Reset 
    
    
    func (x *UpdateDatabaseRequest) Reset()

### func (*UpdateDatabaseRequest) String 
    
    
    func (x *UpdateDatabaseRequest) String() [string](https://pkg.go.dev/builtin#string)

## UpdateTableRequest
    
    
    type UpdateTableRequest struct {
    
    	// Required. The table to update.
    	//
    	// The table's `name` field is used to identify the table to update.
    	// Format:
    	// projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}/databases/{database_id}/tables/{table_id}
    	Table *Table `protobuf:"bytes,1,opt,name=table,proto3" json:"table,omitempty"`
    	// The list of fields to update.
    	//
    	// For the `FieldMask` definition, see
    	// https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask
    	// If not set, defaults to all of the fields that are allowed to update.
    	UpdateMask *fieldmaskpb.FieldMask `protobuf:"bytes,2,opt,name=update_mask,json=updateMask,proto3" json:"update_mask,omitempty"`
    	// contains filtered or unexported fields
    }

Request message for the UpdateTable method.

### func (*UpdateTableRequest) Descriptor 
    
    
    func (*UpdateTableRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use UpdateTableRequest.ProtoReflect.Descriptor instead.

### func (*UpdateTableRequest) GetTable 
    
    
    func (x *UpdateTableRequest) GetTable() *Table

### func (*UpdateTableRequest) GetUpdateMask 
    
    
    func (x *UpdateTableRequest) GetUpdateMask() *[fieldmaskpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb).[FieldMask](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb#FieldMask)

### func (*UpdateTableRequest) ProtoMessage 
    
    
    func (*UpdateTableRequest) ProtoMessage()

### func (*UpdateTableRequest) ProtoReflect 
    
    
    func (x *UpdateTableRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*UpdateTableRequest) Reset 
    
    
    func (x *UpdateTableRequest) Reset()

### func (*UpdateTableRequest) String 
    
    
    func (x *UpdateTableRequest) String() [string](https://pkg.go.dev/builtin#string)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-25 UTC."],[],[]] 
