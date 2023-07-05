"""
<S> = "create" <G>
<G> = global <T> | local <T> | <U>
<T> = "temporary" <U> | "temp" <U>
<U>  = "unlogged" <TABLE> | <TABLE>
<TABLE> = "table" <N> | "table if not exist" <N>
<N> = <TABLE_NAME> ( <R> | <LIKE>
<R> = <COLL_NAME> <TYPE> <COLLATE> <ROW_RESTRICT> <ROW TRANSFER>
<ROW TRANSFER> = "," <R> | <TR>
<TR> = <TABLE_RESTRICT> <RESTRICT TRANSFER>
<RESTRICT TRANSFER> = "," <TR> | <ENT_ROWS_RESTRICTIONS_LIKE>
<LIKE> = "like" <PARRENT_NAME> <COPY_METHOD> <ENT_ROWS_RESTRICTIONS_LIKE>
<ENT_ROWS_RESTRICTIONS_LIKE> = ) <I>
<I> = INHERITS (<PARRENT_NAME>) <PARTITION_BY> | <PARTITION_BY>
<PARTITION_BY> = "partition by" <PARTITION_METHOD> <FIELD_OR_EXPRESSION> <COLLATE> <OPERATOR_CLASS> <USING> | <USING>
<USING> = "using" <USING_METHOD> <WITH> | <WITH>
<WITH> = "with" <PARAMS> <ON_COMMIT> | "without oids" <ON_COMMIT> | <ON_COMMIT>
<ON_COMMIT> = "on commit" <ON_COMMIT_METHOD> <TABLESPACE> | <TABLESPACE>
<TABLESPACE> = "tablespace" <NAME> ; | ;


<USING_METHOD> = ...
<COPY_METHOD> = ...
<PARTITION_METHOD> = ....

<PARAMS> = ( <USUAL_PARAM>
<USUAL_PARAM> = <PARAM_NAME>="<PARAM_VALUE>" <PARAMS_TRANSFER>
<PARAMS_TRANSFER> = , <USUAL_PARAM> | )


<COLLATE> = COLLATE <COLLATE_RULE>
<COLLATE_RULE> = <NAME>
<RESTRICT> = <NAME>
<TABLE_RESTRICT> = ...
<NAME> = \S+
"""

