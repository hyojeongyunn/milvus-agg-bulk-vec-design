# Dynamic Configuration Change

## Execution Setting
1. Binary milvus install
```
$ cd /path/to/milvus/top/folder
$ make install
```

2. Set up `etcd`, `minio`
Follow instructions from [depolyments/binary](https://github.com/milvus-io/milvus/tree/master/deployments/binary)

## How to set up dynamic config
```
$ cd path/to/etcd*
```

- update
```
$ ./etcdctl put /home/config/proxy/{key of the configuration variable to update} {value to update}
```

- show
```
$ ./etcdctl get /home/config/proxy/MaxVectorFieldNum
```