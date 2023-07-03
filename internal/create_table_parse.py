"""
<S> = "create" <G>
<G> = "global" <T>| "local" <T>| <T>
<T> = "temporary" <U> | "temp" <U> | <U>
<U> = "table" <N> | "table if not exist" <N>
<N> = <NAME> ( <R>
<R> = <NAME> <TYPE> <COLLATE> <ROW_RESTRICT> <ROW TRANSFER>
<ROW TRANSFER> = "," <R> | <TR>
<TR> = <TABLE_RESTRICT> <RESTRICT TRANSFER> | <RESTRICT TRANSFER>
<RESTRICT TRANSFER> = "," <TR> | <LIKE>
<LIKE> = "like" <NAME> <COPY_METHOD> <END_LIKE> | <END_LIKE>
<END_LIKE> = ) <I>
<I> = INHERIT (<NAME>) <PARTITION_BY> | <PARTITION_BY>
<PARTITION_BY> = "partition by" <METHOD> <FIELD_OR_EXPRESSION> <COLLATE> <OPERATOR_CLASS> <USING> | <USING>
<USING> = "using" <METHOD> <WITH> | <WITH>
<WITH> = "with" ( <PARAMS> ) <ON_COMMIT> | "without oids" <ON_COMMIT> | <ON_COMMIT>
<ON_COMMIT> = "on commit" <ON_COMMIT_METHOD> <TABLESPACE> | <TABLESPACE>
<TABLESPACE> = "tablespace" <NAME> ; | ;


<PARAMS> = <USUAL_PARAM> <PARAMS_TRANSFER>
<USUAL_PARAM> = <NAME>="<NAME>" <PARAMS_TRANSFER>
<PARAMS_TRANSFER> = , <USUAL_PARAM> | eps


<METHOD> = PRESERVE ROWS | DELETE ROWS | DROP
<COLLATE> = COLLATE <COLLATE_RULE> | eps
<COLLATE_RULE> = <NAME>
<RESTRICT> = <NAME>
<TABLE_RESTRICT> = ...
<NAME> = \S+
"""
