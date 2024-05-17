# Logging in Milvus for developer
- "How to set log-level of milvus"
- "How to write log in milvus code-level"

You must know this when you are dealing with milvus debugging.

## Execution Setting
1. Binary milvus install
```
$ cd /path/to/milvus/top/folder
$ make install
```

2. Set up `etcd`, `minio`
Follow instructions from [depolyments/binary](https://github.com/milvus-io/milvus/tree/master/deployments/binary)

## Set log level
- update
```
$ curl -X PUT localhost:9091/log/level -d level={log level option}
```

- show
```
$ curl -X GET localhost:9091/log/level
```

### Options of log
- debug
- info
- warn
- error
- dpanic
- panic
- fatal

## Write log inside the code

For example
```
import (
    "github.com/milvus-io/milvus/pkg/log"
)

...

def someFunc() {
    ...
    log.Ctx(ctx).Debug("Caller",
	zap.Int("variable with int type", intTypeVar),
	zap.String("variable with string type", stringTypeVar))
    ...
}
```
This log would be shown when the `level=debug`.

## Reference
[(docs) Dynamically change log levels in the milvus](https://milvus.io/blog/dynamically-change-log-levels-in-the-milvus-vector-database.md)   
[(medium) Dynamically change log levels in the milvus](https://medium.com/vector-database/dynamically-change-log-levels-in-the-milvus-vector-database-252d467e5052)  
[(docs) configure log](https://milvus.io/docs/configure_log.md)
