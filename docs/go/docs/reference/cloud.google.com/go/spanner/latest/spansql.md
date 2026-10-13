---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/spansql/
title: Cloud Spanner - Package cloud.google.com/go/spanner/spansql (v1.96.1) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:42:59.039797+00:00
---

# Cloud Spanner - Package cloud.google.com/go/spanner/spansql (v1.96.1)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/spansql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  Cloud Spanner - Package cloud.google.com/go/spanner/spansql (v1.96.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.96.1 (latest)  1.96.0  1.95.1  1.94.0  1.93.0  1.92.0  1.91.0  1.90.0  1.89.0  1.88.0  1.87.0  1.86.1  1.85.1  1.84.1  1.83.0  1.82.0  1.81.1  1.80.0  1.79.0  1.78.0  1.77.0  1.76.1  1.75.0  1.74.0  1.73.0  1.72.0  1.71.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.1  1.52.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.1  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.1  1.33.0  1.32.0  1.31.0  1.30.1  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.1  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.1  1.13.0 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/spanner/spansql). 

Package spansql contains types and a parser for the Cloud Spanner SQL dialect. 

To parse, use one of the Parse functions (ParseDDL, ParseDDLStmt, ParseQuery, etc.). 

Sources:
    
    
    https://cloud.google.com/spanner/docs/lexical
    https://cloud.google.com/spanner/docs/query-syntax
    https://cloud.google.com/spanner/docs/data-definition-language

##  Constants 

### True, False
    
    
    const (
    	True  = BoolLiteral([true](https://pkg.go.dev/builtin#true))
    	False = BoolLiteral([false](https://pkg.go.dev/builtin#false))
    )

### MaxLen
    
    
    const MaxLen = math.MaxInt64

MaxLen is a sentinel for Type's Len field, representing the MAX value.

### Null
    
    
    const Null = NullLiteral(0)

### Star
    
    
    const Star = StarExpr(0)

Star represents a "*" in an expression.

## Functions 

### func IsKeyword 
    
    
    func IsKeyword(id [string](https://pkg.go.dev/builtin#string)) [bool](https://pkg.go.dev/builtin#bool)

IsKeyword reports whether the identifier is a reserved keyword.

## AddColumn
    
    
    type AddColumn struct {
    	IfNotExists [bool](https://pkg.go.dev/builtin#bool)
    	Def         ColumnDef
    }

### func (AddColumn) SQL 
    
    
    func (ac AddColumn) SQL() [string](https://pkg.go.dev/builtin#string)

## AddConstraint
    
    
    type AddConstraint struct{ Constraint TableConstraint }

### func (AddConstraint) SQL 
    
    
    func (ac AddConstraint) SQL() [string](https://pkg.go.dev/builtin#string)

## AddRowDeletionPolicy
    
    
    type AddRowDeletionPolicy struct{ RowDeletionPolicy RowDeletionPolicy }

### func (AddRowDeletionPolicy) SQL 
    
    
    func (ardp AddRowDeletionPolicy) SQL() [string](https://pkg.go.dev/builtin#string)

## AddStoredColumn
    
    
    type AddStoredColumn struct{ Name ID }

### func (AddStoredColumn) SQL 
    
    
    func (asc AddStoredColumn) SQL() [string](https://pkg.go.dev/builtin#string)

## AddSynonym
    
    
    type AddSynonym struct{ Name ID }

### func (AddSynonym) SQL 
    
    
    func (as AddSynonym) SQL() [string](https://pkg.go.dev/builtin#string)

## AggregateHaving
    
    
    type AggregateHaving struct {
    	Condition AggregateHavingCondition
    	Expr      Expr
    }

AggregateHaving represents the HAVING clause specific to aggregate functions, restricting rows based on a maximal or minimal value.

## AggregateHavingCondition
    
    
    type AggregateHavingCondition [int](https://pkg.go.dev/builtin#int)

AggregateHavingCondition represents the condition (MAX or MIN) for the AggregateHaving clause.

### HavingMax, HavingMin
    
    
    const (
    	HavingMax AggregateHavingCondition = [iota](https://pkg.go.dev/builtin#iota)
    	HavingMin
    )

## AlterChangeStream
    
    
    type AlterChangeStream struct {
    	Name       ID
    	Alteration ChangeStreamAlteration
    
    	Position Position
    }

AlterChangeStream represents a ALTER CHANGE STREAM statement.

### func (*AlterChangeStream) Pos 
    
    
    func (acs *AlterChangeStream) Pos() Position

### func (AlterChangeStream) SQL 
    
    
    func (acs AlterChangeStream) SQL() [string](https://pkg.go.dev/builtin#string)

### func (*AlterChangeStream) String 
    
    
    func (acs *AlterChangeStream) String() [string](https://pkg.go.dev/builtin#string)

## AlterChangeStreamOptions
    
    
    type AlterChangeStreamOptions struct{ Options ChangeStreamOptions }

### func (AlterChangeStreamOptions) SQL 
    
    
    func (ao AlterChangeStreamOptions) SQL() [string](https://pkg.go.dev/builtin#string)

## AlterColumn
    
    
    type AlterColumn struct {
    	Name       ID
    	Alteration ColumnAlteration
    }

### func (AlterColumn) SQL 
    
    
    func (ac AlterColumn) SQL() [string](https://pkg.go.dev/builtin#string)

## AlterDatabase
    
    
    type AlterDatabase struct {
    	Name       ID
    	Alteration DatabaseAlteration
    
    	Position Position // position of the "ALTER" token
    }

AlterDatabase represents an ALTER DATABASE statement. <https://cloud.google.com/spanner/docs/data-definition-language#alter-database>

### func (*AlterDatabase) Pos 
    
    
    func (ad *AlterDatabase) Pos() Position

### func (AlterDatabase) SQL 
    
    
    func (ad AlterDatabase) SQL() [string](https://pkg.go.dev/builtin#string)

### func (*AlterDatabase) String 
    
    
    func (ad *AlterDatabase) String() [string](https://pkg.go.dev/builtin#string)

## AlterIndex
    
    
    type AlterIndex struct {
    	Name       ID
    	Alteration IndexAlteration
    
    	Position Position // position of the "ALTER" token
    }

### func (*AlterIndex) Pos 
    
    
    func (as *AlterIndex) Pos() Position

### func (AlterIndex) SQL 
    
    
    func (ai AlterIndex) SQL() [string](https://pkg.go.dev/builtin#string)

### func (*AlterIndex) String 
    
    
    func (as *AlterIndex) String() [string](https://pkg.go.dev/builtin#string)

## AlterProtoBundle
    
    
    type AlterProtoBundle struct {
    	AddTypes, UpdateTypes, DeleteTypes [][string](https://pkg.go.dev/builtin#string)
    	Position                           Position
    }

AlterProtoBundle represents a ALTER PROTO BUNDLE statement. <https://cloud.google.com/spanner/docs/reference/standard-sql/data-definition-language#alter-proto-bundle>

### func (*AlterProtoBundle) Pos 
    
    
    func (ap *AlterProtoBundle) Pos() Position

### func (AlterProtoBundle) SQL 
    
    
    func (ap AlterProtoBundle) SQL() [string](https://pkg.go.dev/builtin#string)

### func (*AlterProtoBundle) String 
    
    
    func (ap *AlterProtoBundle) String() [string](https://pkg.go.dev/builtin#string)

## AlterSearchIndex
    
    
    type AlterSearchIndex struct {
    	Name       ID
    	Alteration IndexAlteration
    
    	Position Position // position of the "ALTER" token
    }

AlterSearchIndex represents a ALTER SEARCH INDEX statement. <https://cloud.google.com/spanner/docs/data-definition-language#alter-search-index>

### func (*AlterSearchIndex) Pos 
    
    
    func (as *AlterSearchIndex) Pos() Position

### func (AlterSearchIndex) SQL 
    
    
    func (ai AlterSearchIndex) SQL() [string](https://pkg.go.dev/builtin#string)

### func (*AlterSearchIndex) String 
    
    
    func (as *AlterSearchIndex) String() [string](https://pkg.go.dev/builtin#string)

## AlterSequence
    
    
    type AlterSequence struct {
    	Name       ID
    	Alteration SequenceAlteration
    
    	Position Position
    }

AlterSequence represents an ALTER SEQUENCE statement. <https://cloud.google.com/spanner/docs/reference/standard-sql/data-definition-language#alter-sequence>

### func (*AlterSequence) Pos 
    
    
    func (as *AlterSequence) Pos() Position

### func (AlterSequence) SQL 
    
    
    func (as AlterSequence) SQL() [string](https://pkg.go.dev/builtin#string)

### func (*AlterSequence) String 
    
    
    func (as *AlterSequence) String() [string](https://pkg.go.dev/builtin#string)

## AlterStatistics
    
    
    type AlterStatistics struct {
    	Name       ID
    	Alteration StatisticsAlteration
    
    	Position Position // position of the "ALTER" token
    }

AlterStatistics represents an ALTER STATISTICS statement. <https://cloud.google.com/spanner/docs/data-definition-language#alter-statistics>

### func (*AlterStatistics) Pos 
    
    
    func (as *AlterStatistics) Pos() Position

### func (AlterStatistics) SQL 
    
    
    func (as AlterStatistics) SQL() [string](https://pkg.go.dev/builtin#string)

### func (*AlterStatistics) String 
    
    
    func (as *AlterStatistics) String() [string](https://pkg.go.dev/builtin#string)

## AlterTable
    
    
    type AlterTable struct {
    	Name       ID
    	Alteration TableAlteration
    
    	Position Position // position of the "ALTER" token
    }

AlterTable represents an ALTER TABLE statement. <https://cloud.google.com/spanner/docs/data-definition-language#alter_table>

### func (*AlterTable) Pos 
    
    
    func (at *AlterTable) Pos() Position

### func (AlterTable) SQL 
    
    
    func (at AlterTable) SQL() [string](https://pkg.go.dev/builtin#string)

### func (*AlterTable) String 
    
    
    func (at *AlterTable) String() [string](https://pkg.go.dev/builtin#string)

## AlterWatch
    
    
    type AlterWatch struct {
    	WatchAllTables [bool](https://pkg.go.dev/builtin#bool)
    	Watch          []WatchDef
    }

### func (AlterWatch) SQL 
    
    
    func (scsw AlterWatch) SQL() [string](https://pkg.go.dev/builtin#string)

## ArithOp
    
    
    type ArithOp struct {
    	Op       ArithOperator
    	LHS, RHS Expr // only RHS is set for Neg, Plus, BitNot
    }

### func (ArithOp) SQL 
    
    
    func (ao ArithOp) SQL() [string](https://pkg.go.dev/builtin#string)

## ArithOperator
    
    
    type ArithOperator [int](https://pkg.go.dev/builtin#int)

### Neg, Plus, BitNot, Mul, Div, Concat, Add, Sub, BitShl, BitShr, BitAnd, BitXor, BitOr
    
    
    const (
    	Neg    ArithOperator = [iota](https://pkg.go.dev/builtin#iota) // unary -
    	Plus                        // unary +
    	BitNot                      // unary ~
    	Mul                         // *
    	Div                         // /
    	Concat                      // ||
    	Add                         // +
    	Sub                         // -
    	BitShl                      // < bitshr="">>
    	BitAnd                      // &
    	BitXor                      // ^
    	BitOr                       // |
    )

## Array
    
    
    type Array []Expr

Array represents an array literal.

### func (Array) SQL 
    
    
    func (a Array) SQL() [string](https://pkg.go.dev/builtin#string)

## ArraySubquery
    
    
    type ArraySubquery struct {
    	Query Query
    }

### func (ArraySubquery) SQL 
    
    
    func (as ArraySubquery) SQL() [string](https://pkg.go.dev/builtin#string)

## AtTimeZoneExpr
    
    
    type AtTimeZoneExpr struct {
    	Expr Expr
    	Type Type
    	Zone [string](https://pkg.go.dev/builtin#string)
    }

### func (AtTimeZoneExpr) SQL 
    
    
    func (aze AtTimeZoneExpr) SQL() [string](https://pkg.go.dev/builtin#string)

## BoolExpr
    
    
    type BoolExpr interface {
    	Expr
    	// contains filtered or unexported methods
    }

## BoolLiteral
    
    
    type BoolLiteral [bool](https://pkg.go.dev/builtin#bool)

### func (BoolLiteral) SQL 
    
    
    func (b BoolLiteral) SQL() [string](https://pkg.go.dev/builtin#string)

## BytesLiteral
    
    
    type BytesLiteral [string](https://pkg.go.dev/builtin#string)

BytesLiteral represents a bytes literal. <https://cloud.google.com/spanner/docs/lexical#string-and-bytes-literals>

### func (BytesLiteral) SQL 
    
    
    func (bl BytesLiteral) SQL() [string](https://pkg.go.dev/builtin#string)

## Case
    
    
    type Case struct {
    	Expr        Expr
    	WhenClauses []WhenClause
    	ElseResult  Expr
    }

### func (Case) SQL 
    
    
    func (c Case) SQL() [string](https://pkg.go.dev/builtin#string)

## ChangeStreamAlteration
    
    
    type ChangeStreamAlteration interface {
    	SQL() [string](https://pkg.go.dev/builtin#string)
    	// contains filtered or unexported methods
    }

## ChangeStreamOptions
    
    
    type ChangeStreamOptions struct {
    	RetentionPeriod  *[string](https://pkg.go.dev/builtin#string)
    	ValueCaptureType *[string](https://pkg.go.dev/builtin#string)
    }

### func (ChangeStreamOptions) SQL 
    
    
    func (cso ChangeStreamOptions) SQL() [string](https://pkg.go.dev/builtin#string)

## Check
    
    
    type Check struct {
    	Expr BoolExpr
    
    	Position Position // position of the "CHECK" token
    }

Check represents a check constraint as part of a CREATE TABLE or ALTER TABLE statement.

### func (Check) Pos 
    
    
    func (c Check) Pos() Position

### func (Check) SQL 
    
    
    func (c Check) SQL() [string](https://pkg.go.dev/builtin#string)

## Coalesce
    
    
    type Coalesce struct {
    	ExprList []Expr
    }

### func (Coalesce) SQL 
    
    
    func (c Coalesce) SQL() [string](https://pkg.go.dev/builtin#string)

## ColumnAlteration
    
    
    type ColumnAlteration interface {
    	SQL() [string](https://pkg.go.dev/builtin#string)
    	// contains filtered or unexported methods
    }

ColumnAlteration is satisfied by SetColumnType and SetColumnOptions.

## ColumnDef
    
    
    type ColumnDef struct {
    	Name    ID
    	Type    Type
    	NotNull [bool](https://pkg.go.dev/builtin#bool)
    	Hidden  [bool](https://pkg.go.dev/builtin#bool)
    
    	Default   Expr // set if this column has a default value
    	Generated Expr // set of this is a generated column
    
    	Options ColumnOptions
    
    	Position Position // position of the column name
    }

ColumnDef represents a column definition as part of a CREATE TABLE or ALTER TABLE statement.

### func (ColumnDef) Pos 
    
    
    func (cd ColumnDef) Pos() Position

### func (ColumnDef) SQL 
    
    
    func (cd ColumnDef) SQL() [string](https://pkg.go.dev/builtin#string)

## ColumnOptions
    
    
    type ColumnOptions struct {
    	// AllowCommitTimestamp represents a column OPTIONS.
    	// `true` if query is `OPTIONS (allow_commit_timestamp = true)`
    	// `false` if query is `OPTIONS (allow_commit_timestamp = null)`
    	// `nil` if there are no OPTIONS
    	AllowCommitTimestamp *[bool](https://pkg.go.dev/builtin#bool)
    }

ColumnOptions represents options on a column as part of a CREATE TABLE or ALTER TABLE statement.

### func (ColumnOptions) SQL 
    
    
    func (co ColumnOptions) SQL() [string](https://pkg.go.dev/builtin#string)

## Comment
    
    
    type Comment struct {
    	Marker   [string](https://pkg.go.dev/builtin#string) // Opening marker; one of "#", "--", "/*".
    	Isolated [bool](https://pkg.go.dev/builtin#bool)   // Whether this comment is on its own line.
    	// Start and End are the position of the opening and terminating marker.
    	Start, End Position
    	Text       [][string](https://pkg.go.dev/builtin#string)
    }

Comment represents a comment.

### func (*Comment) Pos 
    
    
    func (c *Comment) Pos() Position

### func (*Comment) String 
    
    
    func (c *Comment) String() [string](https://pkg.go.dev/builtin#string)

## ComparisonOp
    
    
    type ComparisonOp struct {
    	Op       ComparisonOperator
    	LHS, RHS Expr
    
    	// RHS2 is the third operand for BETWEEN.
    	// "

### func (ComparisonOp) SQL 
    
    
    func (co ComparisonOp) SQL() [string](https://pkg.go.dev/builtin#string)

## ComparisonOperator
    
    
    type ComparisonOperator [int](https://pkg.go.dev/builtin#int)

### Lt, Le, Gt, Ge, Eq, Ne, Like, NotLike, Between, NotBetween
    
    
    const (
    	Lt ComparisonOperator = [iota](https://pkg.go.dev/builtin#iota)
    	Le
    	Gt
    	Ge
    	Eq
    	Ne // both "!=" and "<>"
    	Like
    	NotLike
    	Between
    	NotBetween
    )

## Constraint
    
    
    type Constraint interface {
    	SQL() [string](https://pkg.go.dev/builtin#string)
    	Node
    	// contains filtered or unexported methods
    }

## CreateChangeStream
    
    
    type CreateChangeStream struct {
    	Name           ID
    	Watch          []WatchDef
    	WatchAllTables [bool](https://pkg.go.dev/builtin#bool)
    	Options        ChangeStreamOptions
    
    	Position Position
    }

CreateChangeStream represents a CREATE CHANGE STREAM statement. <https://cloud.google.com/spanner/docs/change-streams/manage>

### func (*CreateChangeStream) Pos 
    
    
    func (cs *CreateChangeStream) Pos() Position

### func (CreateChangeStream) SQL 
    
    
    func (cs CreateChangeStream) SQL() [string](https://pkg.go.dev/builtin#string)

### func (*CreateChangeStream) String 
    
    
    func (cs *CreateChangeStream) String() [string](https://pkg.go.dev/builtin#string)

## CreateIndex
    
    
    type CreateIndex struct {
    	Name    ID
    	Table   ID
    	Columns []KeyPart
    
    	Unique       [bool](https://pkg.go.dev/builtin#bool)
    	NullFiltered [bool](https://pkg.go.dev/builtin#bool)
    	IfNotExists  [bool](https://pkg.go.dev/builtin#bool)
    
    	Storing    []ID
    	Interleave ID
    
    	Position Position // position of the "CREATE" token
    }

CreateIndex represents a CREATE INDEX statement. <https://cloud.google.com/spanner/docs/data-definition-language#create-index>

### func (*CreateIndex) Pos 
    
    
    func (ci *CreateIndex) Pos() Position

### func (CreateIndex) SQL 
    
    
    func (ci CreateIndex) SQL() [string](https://pkg.go.dev/builtin#string)

### func (*CreateIndex) String 
    
    
    func (ci *CreateIndex) String() [string](https://pkg.go.dev/builtin#string)

## CreateProtoBundle
    
    
    type CreateProtoBundle struct {
    	Types    [][string](https://pkg.go.dev/builtin#string)
    	Position Position
    }

CreateProtoBundle represents a CREATE PROTO BUNDLE statement. <https://cloud.google.com/spanner/docs/reference/standard-sql/data-definition-language#create-proto-bundle>

### func (*CreateProtoBundle) Pos 
    
    
    func (cp *CreateProtoBundle) Pos() Position

### func (CreateProtoBundle) SQL 
    
    
    func (cp CreateProtoBundle) SQL() [string](https://pkg.go.dev/builtin#string)

### func (*CreateProtoBundle) String 
    
    
    func (cp *CreateProtoBundle) String() [string](https://pkg.go.dev/builtin#string)

## CreateRole
    
    
    type CreateRole struct {
    	Name ID
    
    	Position Position // position of the "CREATE" token
    }

CreateRole represents a CREATE Role statement. <https://cloud.google.com/spanner/docs/reference/standard-sql/data-definition-language#create_role>

### func (*CreateRole) Pos 
    
    
    func (cr *CreateRole) Pos() Position

### func (CreateRole) SQL 
    
    
    func (cr CreateRole) SQL() [string](https://pkg.go.dev/builtin#string)

### func (*CreateRole) String 
    
    
    func (cr *CreateRole) String() [string](https://pkg.go.dev/builtin#string)

## CreateSearchIndex
    
    
    type CreateSearchIndex struct {
    	Name    ID
    	Table   ID
    	Columns []KeyPart
    
    	Storing        []ID
    	PartitionBy    []ID
    	OrderBy        []Order
    	WhereIsNotNull []ID
    	Interleave     ID
    	Options        SearchIndexOptions
    
    	Position Position // position of the "CREATE" token
    }

CreateSearchIndex represents a CREATE SEARCH INDEX statement. <https://cloud.google.com/spanner/docs/data-definition-language#create-search-index>

### func (*CreateSearchIndex) Pos 
    
    
    func (ci *CreateSearchIndex) Pos() Position

### func (CreateSearchIndex) SQL 
    
    
    func (csi CreateSearchIndex) SQL() [string](https://pkg.go.dev/builtin#string)

### func (*CreateSearchIndex) String 
    
    
    func (ci *CreateSearchIndex) String() [string](https://pkg.go.dev/builtin#string)

## CreateSequence
    
    
    type CreateSequence struct {
    	Name        ID
    	IfNotExists [bool](https://pkg.go.dev/builtin#bool)
    	Options     SequenceOptions
    
    	Position Position
    }

CreateSequence represents an ALTER SEQUENCE statement. <https://cloud.google.com/spanner/docs/reference/standard-sql/data-definition-language#create-sequence>

### func (*CreateSequence) Pos 
    
    
    func (cs *CreateSequence) Pos() Position

### func (CreateSequence) SQL 
    
    
    func (cs CreateSequence) SQL() [string](https://pkg.go.dev/builtin#string)

### func (*CreateSequence) String 
    
    
    func (cs *CreateSequence) String() [string](https://pkg.go.dev/builtin#string)

## CreateTable
    
    
    type CreateTable struct {
    	Name              ID
    	IfNotExists       [bool](https://pkg.go.dev/builtin#bool)
    	Columns           []ColumnDef
    	Constraints       []TableConstraint
    	PrimaryKey        []KeyPart
    	Interleave        *Interleave
    	RowDeletionPolicy *RowDeletionPolicy
    	Synonym           ID // may be empty
    
    	Position Position // position of the "CREATE" token
    }

CreateTable represents a CREATE TABLE statement. <https://cloud.google.com/spanner/docs/data-definition-language#create_table>

### func (*CreateTable) Pos 
    
    
    func (ct *CreateTable) Pos() Position

### func (CreateTable) SQL 
    
    
    func (ct CreateTable) SQL() [string](https://pkg.go.dev/builtin#string)

### func (*CreateTable) String 
    
    
    func (ct *CreateTable) String() [string](https://pkg.go.dev/builtin#string)

## CreateView
    
    
    type CreateView struct {
    	Name         ID
    	OrReplace    [bool](https://pkg.go.dev/builtin#bool)
    	SecurityType SecurityType
    	Query        Query
    
    	Position Position // position of the "CREATE" token
    }

CreateView represents a CREATE [OR REPLACE] VIEW statement. <https://cloud.google.com/spanner/docs/data-definition-language#view_statements>

### func (*CreateView) Pos 
    
    
    func (cv *CreateView) Pos() Position

### func (CreateView) SQL 
    
    
    func (cv CreateView) SQL() [string](https://pkg.go.dev/builtin#string)

### func (*CreateView) String 
    
    
    func (cv *CreateView) String() [string](https://pkg.go.dev/builtin#string)

## DDL
    
    
    type DDL struct {
    	List []DDLStmt
    
    	Filename [string](https://pkg.go.dev/builtin#string) // if known at parse time
    
    	Comments []*Comment // all comments, sorted by position
    }

DDL represents a Data Definition Language (DDL) file.

### func ParseDDL 
    
    
    func ParseDDL(filename, s [string](https://pkg.go.dev/builtin#string)) (*DDL, [error](https://pkg.go.dev/builtin#error))

ParseDDL parses a DDL file.

The provided filename is used for error reporting and will appear in the returned structure.

### func (*DDL) InlineComment 
    
    
    func (d *DDL) InlineComment(n Node) *Comment

InlineComment returns the comment on the same line as a node, or nil if there's no inline comment. The returned comment is guaranteed to be a single line.

### func (*DDL) LeadingComment 
    
    
    func (d *DDL) LeadingComment(n Node) *Comment

LeadingComment returns the comment that immediately precedes a node, or nil if there's no such comment.

## DDLStmt
    
    
    type DDLStmt interface {
    	SQL() [string](https://pkg.go.dev/builtin#string)
    	Node
    	// contains filtered or unexported methods
    }

DDLStmt is satisfied by a type that can appear in a DDL.

### func ParseDDLStmt 
    
    
    func ParseDDLStmt(s [string](https://pkg.go.dev/builtin#string)) (DDLStmt, [error](https://pkg.go.dev/builtin#error))

ParseDDLStmt parses a single DDL statement.

## DML
    
    
    type DML struct {
    	List []DMLStmt
    
    	Filename [string](https://pkg.go.dev/builtin#string) // if known at parse time
    
    	Comments []*Comment // all comments, sorted by position
    }

DML represents a Data Manipulation Language (DML) file.

### func ParseDML 
    
    
    func ParseDML(filename, s [string](https://pkg.go.dev/builtin#string)) (*DML, [error](https://pkg.go.dev/builtin#error))

ParseDML parses a DML file.

The provided filename is used for error reporting and will appear in the returned structure.

### func (*DML) InlineComment 
    
    
    func (d *DML) InlineComment(n Node) *Comment

InlineComment returns the comment on the same line as a node, or nil if there's no inline comment. The returned comment is guaranteed to be a single line.

### func (*DML) LeadingComment 
    
    
    func (d *DML) LeadingComment(n Node) *Comment

LeadingComment returns the comment that immediately precedes a node, or nil if there's no such comment.

## DMLStmt
    
    
    type DMLStmt interface {
    	SQL() [string](https://pkg.go.dev/builtin#string)
    	// contains filtered or unexported methods
    }

DMLStmt is satisfied by a type that is a DML statement.

### func ParseDMLStmt 
    
    
    func ParseDMLStmt(s [string](https://pkg.go.dev/builtin#string)) (DMLStmt, [error](https://pkg.go.dev/builtin#error))

ParseDMLStmt parses a single DML statement.

## DatabaseAlteration
    
    
    type DatabaseAlteration interface {
    	SQL() [string](https://pkg.go.dev/builtin#string)
    	// contains filtered or unexported methods
    }

## DatabaseOptions
    
    
    type DatabaseOptions struct {
    	OptimizerVersion           *[int](https://pkg.go.dev/builtin#int)
    	OptimizerStatisticsPackage *[string](https://pkg.go.dev/builtin#string)
    	VersionRetentionPeriod     *[string](https://pkg.go.dev/builtin#string)
    	EnableKeyVisualizer        *[bool](https://pkg.go.dev/builtin#bool)
    	DefaultLeader              *[string](https://pkg.go.dev/builtin#string)
    }

DatabaseOptions represents options on a database as part of a ALTER DATABASE statement.

### func (DatabaseOptions) SQL 
    
    
    func (do DatabaseOptions) SQL() [string](https://pkg.go.dev/builtin#string)

## DateLiteral
    
    
    type DateLiteral civil.Date

DateLiteral represents a date literal. <https://cloud.google.com/spanner/docs/lexical#date_literals>

### func (DateLiteral) SQL 
    
    
    func (dl DateLiteral) SQL() [string](https://pkg.go.dev/builtin#string)

## DefinitionExpr
    
    
    type DefinitionExpr struct {
    	Key   [string](https://pkg.go.dev/builtin#string)
    	Value Expr
    }

### func (DefinitionExpr) SQL 
    
    
    func (de DefinitionExpr) SQL() [string](https://pkg.go.dev/builtin#string)

## Delete
    
    
    type Delete struct {
    	Table ID
    	Where BoolExpr
    }

Delete represents a DELETE statement. <https://cloud.google.com/spanner/docs/dml-syntax#delete-statement>

### func (*Delete) SQL 
    
    
    func (d *Delete) SQL() [string](https://pkg.go.dev/builtin#string)

### func (*Delete) String 
    
    
    func (d *Delete) String() [string](https://pkg.go.dev/builtin#string)

## DropChangeStream
    
    
    type DropChangeStream struct {
    	Name ID
    
    	Position Position
    }

DropChangeStream represents a DROP CHANGE STREAM statement.

### func (*DropChangeStream) Pos 
    
    
    func (dc *DropChangeStream) Pos() Position

### func (DropChangeStream) SQL 
    
    
    func (dc DropChangeStream) SQL() [string](https://pkg.go.dev/builtin#string)

### func (*DropChangeStream) String 
    
    
    func (dc *DropChangeStream) String() [string](https://pkg.go.dev/builtin#string)

## DropChangeStreamWatch
    
    
    type DropChangeStreamWatch struct{}

### func (DropChangeStreamWatch) SQL 
    
    
    func (dcsw DropChangeStreamWatch) SQL() [string](https://pkg.go.dev/builtin#string)

## DropColumn
    
    
    type DropColumn struct{ Name ID }

### func (DropColumn) SQL 
    
    
    func (dc DropColumn) SQL() [string](https://pkg.go.dev/builtin#string)

## DropConstraint
    
    
    type DropConstraint struct{ Name ID }

### func (DropConstraint) SQL 
    
    
    func (dc DropConstraint) SQL() [string](https://pkg.go.dev/builtin#string)

## DropDefault
    
    
    type DropDefault struct{}

### func (DropDefault) SQL 
    
    
    func (dp DropDefault) SQL() [string](https://pkg.go.dev/builtin#string)

## DropIndex
    
    
    type DropIndex struct {
    	Name     ID
    	IfExists [bool](https://pkg.go.dev/builtin#bool)
    
    	Position Position // position of the "DROP" token
    }

DropIndex represents a DROP INDEX statement. <https://cloud.google.com/spanner/docs/data-definition-language#drop-index>

### func (*DropIndex) Pos 
    
    
    func (di *DropIndex) Pos() Position

### func (DropIndex) SQL 
    
    
    func (di DropIndex) SQL() [string](https://pkg.go.dev/builtin#string)

### func (*DropIndex) String 
    
    
    func (di *DropIndex) String() [string](https://pkg.go.dev/builtin#string)

## DropProtoBundle
    
    
    type DropProtoBundle struct {
    	Position Position
    }

DropProtoBundle represents a DROP PROTO BUNDLE statement. <https://cloud.google.com/spanner/docs/reference/standard-sql/data-definition-language#drop-proto-bundle>

### func (*DropProtoBundle) Pos 
    
    
    func (dp *DropProtoBundle) Pos() Position

### func (DropProtoBundle) SQL 
    
    
    func (do DropProtoBundle) SQL() [string](https://pkg.go.dev/builtin#string)

### func (*DropProtoBundle) String 
    
    
    func (dp *DropProtoBundle) String() [string](https://pkg.go.dev/builtin#string)

## DropRole
    
    
    type DropRole struct {
    	Name ID
    
    	Position Position // position of the "DROP" token
    }

DropRole represents a DROP ROLE statement. <https://cloud.google.com/spanner/docs/reference/standard-sql/data-definition-language#drop_role>

### func (*DropRole) Pos 
    
    
    func (dr *DropRole) Pos() Position

### func (DropRole) SQL 
    
    
    func (dr DropRole) SQL() [string](https://pkg.go.dev/builtin#string)

### func (*DropRole) String 
    
    
    func (dr *DropRole) String() [string](https://pkg.go.dev/builtin#string)

## DropRowDeletionPolicy
    
    
    type DropRowDeletionPolicy struct{}

### func (DropRowDeletionPolicy) SQL 
    
    
    func (drdp DropRowDeletionPolicy) SQL() [string](https://pkg.go.dev/builtin#string)

## DropSearchIndex
    
    
    type DropSearchIndex struct {
    	Name     ID
    	IfExists [bool](https://pkg.go.dev/builtin#bool)
    
    	Position Position // position of the "DROP" token
    }

DropSearchIndex represents a DROP SEARCH INDEX statement. <https://cloud.google.com/spanner/docs/data-definition-language#drop-search-index>

### func (*DropSearchIndex) Pos 
    
    
    func (di *DropSearchIndex) Pos() Position

### func (DropSearchIndex) SQL 
    
    
    func (di DropSearchIndex) SQL() [string](https://pkg.go.dev/builtin#string)

### func (*DropSearchIndex) String 
    
    
    func (di *DropSearchIndex) String() [string](https://pkg.go.dev/builtin#string)

## DropSequence
    
    
    type DropSequence struct {
    	Name     ID
    	IfExists [bool](https://pkg.go.dev/builtin#bool)
    
    	Position Position
    }

DropSequence represents a DROP SEQUENCE statement. <https://cloud.google.com/spanner/docs/reference/standard-sql/data-definition-language#drop-sequence>

### func (*DropSequence) Pos 
    
    
    func (ds *DropSequence) Pos() Position

### func (DropSequence) SQL 
    
    
    func (do DropSequence) SQL() [string](https://pkg.go.dev/builtin#string)

### func (*DropSequence) String 
    
    
    func (ds *DropSequence) String() [string](https://pkg.go.dev/builtin#string)

## DropStoredColumn
    
    
    type DropStoredColumn struct{ Name ID }

### func (DropStoredColumn) SQL 
    
    
    func (dsc DropStoredColumn) SQL() [string](https://pkg.go.dev/builtin#string)

## DropSynonym
    
    
    type DropSynonym struct{ Name ID }

### func (DropSynonym) SQL 
    
    
    func (ds DropSynonym) SQL() [string](https://pkg.go.dev/builtin#string)

## DropTable
    
    
    type DropTable struct {
    	Name     ID
    	IfExists [bool](https://pkg.go.dev/builtin#bool)
    
    	Position Position // position of the "DROP" token
    }

DropTable represents a DROP TABLE statement. <https://cloud.google.com/spanner/docs/data-definition-language#drop_table>

### func (*DropTable) Pos 
    
    
    func (dt *DropTable) Pos() Position

### func (DropTable) SQL 
    
    
    func (dt DropTable) SQL() [string](https://pkg.go.dev/builtin#string)

### func (*DropTable) String 
    
    
    func (dt *DropTable) String() [string](https://pkg.go.dev/builtin#string)

## DropView
    
    
    type DropView struct {
    	Name ID
    
    	Position Position // position of the "DROP" token
    }

DropView represents a DROP VIEW statement. <https://cloud.google.com/spanner/docs/data-definition-language#drop-view>

### func (*DropView) Pos 
    
    
    func (dv *DropView) Pos() Position

### func (DropView) SQL 
    
    
    func (dv DropView) SQL() [string](https://pkg.go.dev/builtin#string)

### func (*DropView) String 
    
    
    func (dv *DropView) String() [string](https://pkg.go.dev/builtin#string)

## ExistsOp
    
    
    type ExistsOp struct {
    	Subquery Query
    }

### func (ExistsOp) SQL 
    
    
    func (eo ExistsOp) SQL() [string](https://pkg.go.dev/builtin#string)

## Expr
    
    
    type Expr interface {
    	SQL() [string](https://pkg.go.dev/builtin#string)
    	// contains filtered or unexported methods
    }

## ExtractExpr
    
    
    type ExtractExpr struct {
    	Part [string](https://pkg.go.dev/builtin#string)
    	Type Type
    	Expr Expr
    }

### func (ExtractExpr) SQL 
    
    
    func (ee ExtractExpr) SQL() [string](https://pkg.go.dev/builtin#string)

## FloatLiteral
    
    
    type FloatLiteral [float64](https://pkg.go.dev/builtin#float64)

FloatLiteral represents a floating point literal. <https://cloud.google.com/spanner/docs/lexical#floating-point-literals>

### func (FloatLiteral) SQL 
    
    
    func (fl FloatLiteral) SQL() [string](https://pkg.go.dev/builtin#string)

## ForeignKey
    
    
    type ForeignKey struct {
    	Columns    []ID
    	RefTable   ID
    	RefColumns []ID
    	OnDelete   OnDelete
    
    	Position Position // position of the "FOREIGN" token
    }

ForeignKey represents a foreign key definition as part of a CREATE TABLE or ALTER TABLE statement.

### func (ForeignKey) Pos 
    
    
    func (fk ForeignKey) Pos() Position

### func (ForeignKey) SQL 
    
    
    func (fk ForeignKey) SQL() [string](https://pkg.go.dev/builtin#string)

## Func
    
    
    type Func struct {
    	Name [string](https://pkg.go.dev/builtin#string) // not ID
    	Args []Expr
    
    	Distinct      [bool](https://pkg.go.dev/builtin#bool)
    	NullsHandling NullsHandling
    	Having        *AggregateHaving
    }

Func represents a function call.

### func (Func) SQL 
    
    
    func (f Func) SQL() [string](https://pkg.go.dev/builtin#string)

## GrantRole
    
    
    type GrantRole struct {
    	ToRoleNames       []ID
    	GrantRoleNames    []ID
    	Privileges        []Privilege
    	TableNames        []ID
    	TvfNames          []ID
    	ViewNames         []ID
    	ChangeStreamNames []ID
    
    	Position Position // position of the "GRANT" token
    }

GrantRole represents a GRANT statement. <https://cloud.google.com/spanner/docs/reference/standard-sql/data-definition-language#grant_statement>

### func (*GrantRole) Pos 
    
    
    func (gr *GrantRole) Pos() Position

### func (GrantRole) SQL 
    
    
    func (gr GrantRole) SQL() [string](https://pkg.go.dev/builtin#string)

### func (*GrantRole) String 
    
    
    func (gr *GrantRole) String() [string](https://pkg.go.dev/builtin#string)

## ID
    
    
    type ID [string](https://pkg.go.dev/builtin#string)

ID represents an identifier. <https://cloud.google.com/spanner/docs/lexical#identifiers>

### func (ID) SQL 
    
    
    func (id ID) SQL() [string](https://pkg.go.dev/builtin#string)

## If
    
    
    type If struct {
    	Expr       Expr
    	TrueResult Expr
    	ElseResult Expr
    }

### func (If) SQL 
    
    
    func (i If) SQL() [string](https://pkg.go.dev/builtin#string)

## IfNull
    
    
    type IfNull struct {
    	Expr       Expr
    	NullResult Expr
    }

### func (IfNull) SQL 
    
    
    func (in IfNull) SQL() [string](https://pkg.go.dev/builtin#string)

## InOp
    
    
    type InOp struct {
    	LHS    Expr
    	Neg    [bool](https://pkg.go.dev/builtin#bool)
    	RHS    []Expr
    	Unnest [bool](https://pkg.go.dev/builtin#bool)
    }

### func (InOp) SQL 
    
    
    func (io InOp) SQL() [string](https://pkg.go.dev/builtin#string)

## IndexAlteration
    
    
    type IndexAlteration interface {
    	SQL() [string](https://pkg.go.dev/builtin#string)
    	// contains filtered or unexported methods
    }

## Insert
    
    
    type Insert struct {
    	Table   ID
    	Columns []ID
    	Input   ValuesOrSelect
    }

Insert represents an INSERT statement. <https://cloud.google.com/spanner/docs/dml-syntax#insert-statement>

### func (*Insert) SQL 
    
    
    func (i *Insert) SQL() [string](https://pkg.go.dev/builtin#string)

### func (*Insert) String 
    
    
    func (i *Insert) String() [string](https://pkg.go.dev/builtin#string)

## IntegerLiteral
    
    
    type IntegerLiteral [int64](https://pkg.go.dev/builtin#int64)

IntegerLiteral represents an integer literal. <https://cloud.google.com/spanner/docs/lexical#integer-literals>

### func (IntegerLiteral) SQL 
    
    
    func (il IntegerLiteral) SQL() [string](https://pkg.go.dev/builtin#string)

## Interleave
    
    
    type Interleave struct {
    	Parent   ID
    	OnDelete OnDelete
    }

Interleave represents an interleave clause of a CREATE TABLE statement.

## IntervalExpr
    
    
    type IntervalExpr struct {
    	Expr     Expr
    	DatePart [string](https://pkg.go.dev/builtin#string)
    }

### func (IntervalExpr) SQL 
    
    
    func (ie IntervalExpr) SQL() [string](https://pkg.go.dev/builtin#string)

## IsExpr
    
    
    type IsExpr interface {
    	Expr
    	// contains filtered or unexported methods
    }

## IsOp
    
    
    type IsOp struct {
    	LHS Expr
    	Neg [bool](https://pkg.go.dev/builtin#bool)
    	RHS IsExpr
    }

### func (IsOp) SQL 
    
    
    func (io IsOp) SQL() [string](https://pkg.go.dev/builtin#string)

## JSONLiteral
    
    
    type JSONLiteral [][byte](https://pkg.go.dev/builtin#byte)

JSONLiteral represents a JSON literal <https://cloud.google.com/spanner/docs/reference/standard-sql/lexical#json_literals>

### func (JSONLiteral) SQL 
    
    
    func (jl JSONLiteral) SQL() [string](https://pkg.go.dev/builtin#string)

## JoinType
    
    
    type JoinType [int](https://pkg.go.dev/builtin#int)

### InnerJoin, CrossJoin, FullJoin, LeftJoin, RightJoin
    
    
    const (
    	InnerJoin JoinType = [iota](https://pkg.go.dev/builtin#iota)
    	CrossJoin
    	FullJoin
    	LeftJoin
    	RightJoin
    )

## KeyPart
    
    
    type KeyPart struct {
    	Column ID
    	Desc   [bool](https://pkg.go.dev/builtin#bool)
    }

KeyPart represents a column specification as part of a primary key or index definition.

### func (KeyPart) SQL 
    
    
    func (kp KeyPart) SQL() [string](https://pkg.go.dev/builtin#string)

## LiteralOrParam
    
    
    type LiteralOrParam interface {
    	SQL() [string](https://pkg.go.dev/builtin#string)
    	// contains filtered or unexported methods
    }

LiteralOrParam is implemented by integer literal and parameter values.

## LogicalOp
    
    
    type LogicalOp struct {
    	Op       LogicalOperator
    	LHS, RHS BoolExpr // only RHS is set for Not
    }

### func (LogicalOp) SQL 
    
    
    func (lo LogicalOp) SQL() [string](https://pkg.go.dev/builtin#string)

## LogicalOperator
    
    
    type LogicalOperator [int](https://pkg.go.dev/builtin#int)

### And, Or, Not
    
    
    const (
    	And LogicalOperator = [iota](https://pkg.go.dev/builtin#iota)
    	Or
    	Not
    )

## Node
    
    
    type Node interface {
    	Pos() Position
    }

Node is implemented by concrete types in this package that represent things appearing in a DDL file.

## NullIf
    
    
    type NullIf struct {
    	Expr        Expr
    	ExprToMatch Expr
    }

### func (NullIf) SQL 
    
    
    func (ni NullIf) SQL() [string](https://pkg.go.dev/builtin#string)

## NullLiteral
    
    
    type NullLiteral [int](https://pkg.go.dev/builtin#int)

### func (NullLiteral) SQL 
    
    
    func (NullLiteral) SQL() [string](https://pkg.go.dev/builtin#string)

## NullsHandling
    
    
    type NullsHandling [int](https://pkg.go.dev/builtin#int)

NullsHandling represents the method of dealing with NULL values in aggregate functions.

### NullsHandlingUnspecified, RespectNulls, IgnoreNulls
    
    
    const (
    	NullsHandlingUnspecified NullsHandling = [iota](https://pkg.go.dev/builtin#iota)
    	RespectNulls
    	IgnoreNulls
    )

## OnDelete
    
    
    type OnDelete [int](https://pkg.go.dev/builtin#int)

### NoActionOnDelete, CascadeOnDelete
    
    
    const (
    	NoActionOnDelete OnDelete = [iota](https://pkg.go.dev/builtin#iota)
    	CascadeOnDelete
    )

### func (OnDelete) SQL 
    
    
    func (od OnDelete) SQL() [string](https://pkg.go.dev/builtin#string)

## Order
    
    
    type Order struct {
    	Expr Expr
    	Desc [bool](https://pkg.go.dev/builtin#bool)
    }

### func (Order) SQL 
    
    
    func (o Order) SQL() [string](https://pkg.go.dev/builtin#string)

## Param
    
    
    type Param [string](https://pkg.go.dev/builtin#string)

Param represents a query parameter.

### func (Param) SQL 
    
    
    func (p Param) SQL() [string](https://pkg.go.dev/builtin#string)

## Paren
    
    
    type Paren struct {
    	Expr Expr
    }

Paren represents a parenthesised expression.

### func (Paren) SQL 
    
    
    func (p Paren) SQL() [string](https://pkg.go.dev/builtin#string)

## PathExp
    
    
    type PathExp []ID

PathExp represents a path expression.

The grammar for path expressions is not defined (see b/169017423 internally), so this captures the most common form only, namely a dotted sequence of identifiers.

### func (PathExp) SQL 
    
    
    func (pe PathExp) SQL() [string](https://pkg.go.dev/builtin#string)

## Position
    
    
    type Position struct {
    	Line   [int](https://pkg.go.dev/builtin#int) // 1-based line number
    	Offset [int](https://pkg.go.dev/builtin#int) // 0-based byte offset
    }

Position describes a source position in an input DDL file. It is only valid if the line number is positive.

### func (Position) IsValid 
    
    
    func (pos Position) IsValid() [bool](https://pkg.go.dev/builtin#bool)

### func (Position) String 
    
    
    func (pos Position) String() [string](https://pkg.go.dev/builtin#string)

## Privilege
    
    
    type Privilege struct {
    	Type    PrivilegeType
    	Columns []ID
    }

Privilege represents privilege to grant or revoke.

## PrivilegeType
    
    
    type PrivilegeType [int](https://pkg.go.dev/builtin#int)

### PrivilegeTypeSelect, PrivilegeTypeInsert, PrivilegeTypeUpdate, PrivilegeTypeDelete
    
    
    const (
    	PrivilegeTypeSelect PrivilegeType = [iota](https://pkg.go.dev/builtin#iota)
    	PrivilegeTypeInsert
    	PrivilegeTypeUpdate
    	PrivilegeTypeDelete
    )

### func (PrivilegeType) SQL 
    
    
    func (pt PrivilegeType) SQL() [string](https://pkg.go.dev/builtin#string)

## Query
    
    
    type Query struct {
    	Select Select
    	Order  []Order
    
    	Limit, Offset LiteralOrParam
    }

Query represents a query statement. <https://cloud.google.com/spanner/docs/query-syntax#sql-syntax>

### func ParseQuery 
    
    
    func ParseQuery(s [string](https://pkg.go.dev/builtin#string)) (Query, [error](https://pkg.go.dev/builtin#error))

ParseQuery parses a query string.

### func (Query) SQL 
    
    
    func (q Query) SQL() [string](https://pkg.go.dev/builtin#string)

## RenameTable
    
    
    type RenameTable struct {
    	TableRenameOps []TableRenameOp
    
    	Position Position // position of the "RENAME" token
    }

RenameTable represents a RENAME TABLE statement.

### func (*RenameTable) Pos 
    
    
    func (rt *RenameTable) Pos() Position

### func (RenameTable) SQL 
    
    
    func (rt RenameTable) SQL() [string](https://pkg.go.dev/builtin#string)

### func (*RenameTable) String 
    
    
    func (rt *RenameTable) String() [string](https://pkg.go.dev/builtin#string)

## RenameTo
    
    
    type RenameTo struct {
    	ToName  ID
    	Synonym ID // may be empty
    }

### func (RenameTo) SQL 
    
    
    func (rt RenameTo) SQL() [string](https://pkg.go.dev/builtin#string)

## ReplaceRowDeletionPolicy
    
    
    type ReplaceRowDeletionPolicy struct{ RowDeletionPolicy RowDeletionPolicy }

### func (ReplaceRowDeletionPolicy) SQL 
    
    
    func (rrdp ReplaceRowDeletionPolicy) SQL() [string](https://pkg.go.dev/builtin#string)

## RevokeRole
    
    
    type RevokeRole struct {
    	FromRoleNames     []ID
    	RevokeRoleNames   []ID
    	Privileges        []Privilege
    	TableNames        []ID
    	TvfNames          []ID
    	ViewNames         []ID
    	ChangeStreamNames []ID
    	Position          Position // position of the "REVOKE" token
    }

RevokeRole represents a REVOKE statement. <https://cloud.google.com/spanner/docs/reference/standard-sql/data-definition-language#revoke_statement>

### func (*RevokeRole) Pos 
    
    
    func (rr *RevokeRole) Pos() Position

### func (RevokeRole) SQL 
    
    
    func (rr RevokeRole) SQL() [string](https://pkg.go.dev/builtin#string)

### func (*RevokeRole) String 
    
    
    func (rr *RevokeRole) String() [string](https://pkg.go.dev/builtin#string)

## RowDeletionPolicy
    
    
    type RowDeletionPolicy struct {
    	Column  ID
    	NumDays [int64](https://pkg.go.dev/builtin#int64)
    }

RowDeletionPolicy represents an row deletion policy clause of a CREATE, ALTER TABLE statement.

### func (RowDeletionPolicy) SQL 
    
    
    func (rdp RowDeletionPolicy) SQL() [string](https://pkg.go.dev/builtin#string)

## ScalarSubquery
    
    
    type ScalarSubquery struct {
    	Query Query
    }

### func (ScalarSubquery) SQL 
    
    
    func (ss ScalarSubquery) SQL() [string](https://pkg.go.dev/builtin#string)

## SearchIndexOptions
    
    
    type SearchIndexOptions struct {
    	SortOrderSharding         *[bool](https://pkg.go.dev/builtin#bool)
    	DisableAutomaticUIDColumn *[bool](https://pkg.go.dev/builtin#bool)
    }

SearchIndexOptions represents options on a search index as part of a CREATE SEARCH INDEX statement.

### func (SearchIndexOptions) SQL 
    
    
    func (opts SearchIndexOptions) SQL() [string](https://pkg.go.dev/builtin#string)

## SecurityType
    
    
    type SecurityType [int](https://pkg.go.dev/builtin#int)

### Invoker, Definer
    
    
    const (
    	Invoker SecurityType = [iota](https://pkg.go.dev/builtin#iota)
    	Definer
    )

### func (SecurityType) SQL 
    
    
    func (st SecurityType) SQL() [string](https://pkg.go.dev/builtin#string)

## Select
    
    
    type Select struct {
    	Distinct [bool](https://pkg.go.dev/builtin#bool)
    	AsStruct [bool](https://pkg.go.dev/builtin#bool) // SELECT AS STRUCT
    	List     []Expr
    	From     []SelectFrom
    	Where    BoolExpr
    	GroupBy  []Expr
    
    	// When the FROM clause has TABLESAMPLE operators,
    	// TableSamples will be populated 1:1 with From;
    	// FROM clauses without will have a nil value.
    	TableSamples []*TableSample
    
    	// If the SELECT list has explicit aliases ("AS alias"),
    	// ListAliases will be populated 1:1 with List;
    	// aliases that are present will be non-empty.
    	ListAliases []ID
    }

Select represents a SELECT statement. <https://cloud.google.com/spanner/docs/query-syntax#select-list>

### func (Select) SQL 
    
    
    func (sel Select) SQL() [string](https://pkg.go.dev/builtin#string)

## SelectFrom
    
    
    type SelectFrom interface {
    	SQL() [string](https://pkg.go.dev/builtin#string)
    	// contains filtered or unexported methods
    }

SelectFrom represents the FROM clause of a SELECT. <https://cloud.google.com/spanner/docs/query-syntax#from_clause>

## SelectFromJoin
    
    
    type SelectFromJoin struct {
    	Type     JoinType
    	LHS, RHS SelectFrom
    
    	// Join condition.
    	// At most one of {On,Using} may be set.
    	On    BoolExpr
    	Using []ID
    
    	// Hints are suggestions for how to evaluate a join.
    	// https://cloud.google.com/spanner/docs/query-syntax#join-hints
    	Hints map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string)
    }

SelectFromJoin is a SelectFrom that joins two other SelectFroms. <https://cloud.google.com/spanner/docs/query-syntax#join_types>

### func (SelectFromJoin) SQL 
    
    
    func (sfj SelectFromJoin) SQL() [string](https://pkg.go.dev/builtin#string)

## SelectFromTable
    
    
    type SelectFromTable struct {
    	Table ID
    	Alias ID // empty if not aliased
    	Hints map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string)
    }

SelectFromTable is a SelectFrom that specifies a table to read from.

### func (SelectFromTable) SQL 
    
    
    func (sft SelectFromTable) SQL() [string](https://pkg.go.dev/builtin#string)

## SelectFromUnnest
    
    
    type SelectFromUnnest struct {
    	Expr  Expr
    	Alias ID // empty if not aliased
    
    }

SelectFromUnnest is a SelectFrom that yields a virtual table from an array. <https://cloud.google.com/spanner/docs/query-syntax#unnest>

### func (SelectFromUnnest) SQL 
    
    
    func (sfu SelectFromUnnest) SQL() [string](https://pkg.go.dev/builtin#string)

## SequenceAlteration
    
    
    type SequenceAlteration interface {
    	SQL() [string](https://pkg.go.dev/builtin#string)
    	// contains filtered or unexported methods
    }

## SequenceExpr
    
    
    type SequenceExpr struct {
    	Name ID
    }

### func (SequenceExpr) SQL 
    
    
    func (se SequenceExpr) SQL() [string](https://pkg.go.dev/builtin#string)

## SequenceOptions
    
    
    type SequenceOptions struct {
    	SequenceKind     *[string](https://pkg.go.dev/builtin#string)
    	SkipRangeMin     *[int](https://pkg.go.dev/builtin#int)
    	SkipRangeMax     *[int](https://pkg.go.dev/builtin#int)
    	StartWithCounter *[int](https://pkg.go.dev/builtin#int)
    }

SequenceOptions represents options on a sequence as part of a CREATE SEQUENCE and ALTER SEQUENCE statement.

### func (SequenceOptions) SQL 
    
    
    func (so SequenceOptions) SQL() [string](https://pkg.go.dev/builtin#string)

## SetColumnOptions
    
    
    type SetColumnOptions struct{ Options ColumnOptions }

### func (SetColumnOptions) SQL 
    
    
    func (sco SetColumnOptions) SQL() [string](https://pkg.go.dev/builtin#string)

## SetColumnType
    
    
    type SetColumnType struct {
    	Type    Type
    	NotNull [bool](https://pkg.go.dev/builtin#bool)
    	Default Expr
    }

### func (SetColumnType) SQL 
    
    
    func (sct SetColumnType) SQL() [string](https://pkg.go.dev/builtin#string)

## SetDatabaseOptions
    
    
    type SetDatabaseOptions struct{ Options DatabaseOptions }

### func (SetDatabaseOptions) SQL 
    
    
    func (sdo SetDatabaseOptions) SQL() [string](https://pkg.go.dev/builtin#string)

## SetDefault
    
    
    type SetDefault struct {
    	Default Expr
    }

### func (SetDefault) SQL 
    
    
    func (sd SetDefault) SQL() [string](https://pkg.go.dev/builtin#string)

## SetOnDelete
    
    
    type SetOnDelete struct{ Action OnDelete }

### func (SetOnDelete) SQL 
    
    
    func (sod SetOnDelete) SQL() [string](https://pkg.go.dev/builtin#string)

## SetSequenceOptions
    
    
    type SetSequenceOptions struct{ Options SequenceOptions }

### func (SetSequenceOptions) SQL 
    
    
    func (sa SetSequenceOptions) SQL() [string](https://pkg.go.dev/builtin#string)

## SetStatisticsOptions
    
    
    type SetStatisticsOptions struct{ Options StatisticsOptions }

### func (SetStatisticsOptions) SQL 
    
    
    func (sso SetStatisticsOptions) SQL() [string](https://pkg.go.dev/builtin#string)

## StarExpr
    
    
    type StarExpr [int](https://pkg.go.dev/builtin#int)

### func (StarExpr) SQL 
    
    
    func (StarExpr) SQL() [string](https://pkg.go.dev/builtin#string)

## StatisticsAlteration
    
    
    type StatisticsAlteration interface {
    	SQL() [string](https://pkg.go.dev/builtin#string)
    	// contains filtered or unexported methods
    }

## StatisticsOptions
    
    
    type StatisticsOptions struct {
    	AllowGC *[bool](https://pkg.go.dev/builtin#bool)
    }

StatisticsOptions represents options on a statistics as part of a ALTER STATISTICS statement.

### func (StatisticsOptions) SQL 
    
    
    func (sa StatisticsOptions) SQL() [string](https://pkg.go.dev/builtin#string)

## StringLiteral
    
    
    type StringLiteral [string](https://pkg.go.dev/builtin#string)

StringLiteral represents a string literal. <https://cloud.google.com/spanner/docs/lexical#string-and-bytes-literals>

### func (StringLiteral) SQL 
    
    
    func (sl StringLiteral) SQL() [string](https://pkg.go.dev/builtin#string)

## StructLiteral
    
    
    type StructLiteral struct {
    	Fields []Expr
    	// FieldTypes is optional and populated for typed struct literals.
    	// STRUCT

StructLiteral represents a struct literal. <https://cloud.google.com/spanner/docs/query-syntax#struct_type>

### func (StructLiteral) SQL 
    
    
    func (sl StructLiteral) SQL() [string](https://pkg.go.dev/builtin#string)

## TableAlteration
    
    
    type TableAlteration interface {
    	SQL() [string](https://pkg.go.dev/builtin#string)
    	// contains filtered or unexported methods
    }

TableAlteration is satisfied by AddColumn, DropColumn, AddConstraint, DropConstraint, SetOnDelete, AlterColumn, AddRowDeletionPolicy, ReplaceRowDeletionPolicy, DropRowDeletionPolicy, RenameTo, AddSynonym, and DropSynonym.

## TableConstraint
    
    
    type TableConstraint struct {
    	Name       ID // may be empty
    	Constraint Constraint
    
    	Position Position // position of the "CONSTRAINT" token, or Constraint.Pos()
    }

TableConstraint represents a constraint on a table.

### func (TableConstraint) Pos 
    
    
    func (tc TableConstraint) Pos() Position

### func (TableConstraint) SQL 
    
    
    func (tc TableConstraint) SQL() [string](https://pkg.go.dev/builtin#string)

## TableRenameOp
    
    
    type TableRenameOp struct {
    	FromName ID
    	ToName   ID
    }

## TableSample
    
    
    type TableSample struct {
    	Method   TableSampleMethod
    	Size     Expr
    	SizeType TableSampleSizeType
    }

## TableSampleMethod
    
    
    type TableSampleMethod [int](https://pkg.go.dev/builtin#int)

### Bernoulli, Reservoir
    
    
    const (
    	Bernoulli TableSampleMethod = [iota](https://pkg.go.dev/builtin#iota)
    	Reservoir
    )

## TableSampleSizeType
    
    
    type TableSampleSizeType [int](https://pkg.go.dev/builtin#int)

### PercentTableSample, RowsTableSample
    
    
    const (
    	PercentTableSample TableSampleSizeType = [iota](https://pkg.go.dev/builtin#iota)
    	RowsTableSample
    )

## TimestampLiteral
    
    
    type TimestampLiteral time.Time

TimestampLiteral represents a timestamp literal. <https://cloud.google.com/spanner/docs/lexical#timestamp_literals>

### func (TimestampLiteral) SQL 
    
    
    func (tl TimestampLiteral) SQL() [string](https://pkg.go.dev/builtin#string)

## Type
    
    
    type Type struct {
    	Array [bool](https://pkg.go.dev/builtin#bool)
    	Base  TypeBase // Bool, Int64, Float64, Numeric, String, Bytes, Date, Timestamp
    	Len   [int64](https://pkg.go.dev/builtin#int64)    // if Base is String or Bytes; may be MaxLen
    	// fully-qualified Protocol Buffer Message or Enum type-name (including
    	// leading dot-separated namespace)
    	// non-empty if Base is ProtoMessage or ProtoEnum
    	ProtoRef [string](https://pkg.go.dev/builtin#string)
    }

Type represents a column type.

### func (Type) SQL 
    
    
    func (t Type) SQL() [string](https://pkg.go.dev/builtin#string)

## TypeBase
    
    
    type TypeBase [int](https://pkg.go.dev/builtin#int)

### Bool, Int64, Float64, Numeric, String, Bytes, Date, Timestamp, JSON, Proto, Enum, Tokenlist, UUID
    
    
    const (
    	Bool TypeBase = [iota](https://pkg.go.dev/builtin#iota)
    	Int64
    	Float64
    	Numeric
    	String
    	Bytes
    	Date
    	Timestamp
    	JSON
    	Proto
    	Enum // Enum used in CAST expressions
    	Tokenlist
    	UUID
    )

### func (TypeBase) SQL 
    
    
    func (tb TypeBase) SQL() [string](https://pkg.go.dev/builtin#string)

## TypedExpr
    
    
    type TypedExpr struct {
    	Type Type
    	Expr Expr
    }

TypedExpr represents a typed expression in the form `expr AS type_name`, e.g. `'17' AS INT64`.

### func (TypedExpr) SQL 
    
    
    func (te TypedExpr) SQL() [string](https://pkg.go.dev/builtin#string)

## Update
    
    
    type Update struct {
    	Table ID
    	Items []UpdateItem
    	Where BoolExpr
    }

Update represents an UPDATE statement. <https://cloud.google.com/spanner/docs/dml-syntax#update-statement>

### func (*Update) SQL 
    
    
    func (u *Update) SQL() [string](https://pkg.go.dev/builtin#string)

### func (*Update) String 
    
    
    func (u *Update) String() [string](https://pkg.go.dev/builtin#string)

## UpdateItem
    
    
    type UpdateItem struct {
    	Column ID
    	Value  Expr // or nil for DEFAULT
    }

## Values
    
    
    type Values [][]Expr

Values represents one or more lists of expressions passed to an `INSERT` statement.

### func (Values) SQL 
    
    
    func (v Values) SQL() [string](https://pkg.go.dev/builtin#string)

### func (Values) String 
    
    
    func (v Values) String() [string](https://pkg.go.dev/builtin#string)

## ValuesOrSelect
    
    
    type ValuesOrSelect interface {
    	SQL() [string](https://pkg.go.dev/builtin#string)
    	// contains filtered or unexported methods
    }

## WatchDef
    
    
    type WatchDef struct {
    	Table        ID
    	Columns      []ID
    	WatchAllCols [bool](https://pkg.go.dev/builtin#bool)
    
    	Position Position
    }

### func (WatchDef) Pos 
    
    
    func (wd WatchDef) Pos() Position

### func (WatchDef) SQL 
    
    
    func (w WatchDef) SQL() [string](https://pkg.go.dev/builtin#string)

## WhenClause
    
    
    type WhenClause struct {
    	Cond   Expr
    	Result Expr
    }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
