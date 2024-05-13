# Advanced Multi-Vector Query Processing in Milvus

## Summary


## Background

Multi-vector search란, 지칭하고자 하는 대상이 하나의 벡터가 아닌 여러 개의 벡터 임베딩으로 표현될 때, 쿼리로 주어진 여러 개의 벡터 (multi-vector)와 가장 유사한 K개의 대상을 반환하는 search이다.
multi-vector search의 use case로는 multimodal 혹은 late-interaction IR 모델 등이 있다.
(single vector search와의 차이점)

Multi-vector search는 임베딩 함수의 특성에 따라, 두 갈래의 구분을 가질 수 있다.
첫번째는, 대상이 가지는 여러 개의 벡터 임베딩이 동일한 embedding space를 공유하는 것이다. 이는 Colbert와 같은 late-ineraction 기반의 IR 모델을 예로 들 수 있다.
두번째는, 대상이 가지는 여러 개의 벡터 임베딩이 다른 embedding space를 공유하는 것이다. 이는 multimodal을 예로 들 수 있다.

## Motivation

가장 최신의 밀버스에서는 multi-vector search를 지원한다.
하지만, multi-vector search의 다양한 use case를 고려하지 않고, 구현되어 있어 다음과 같은 한계를 가지고 있다.
- 현재의 multi-vector search는 대상이 갖는 여러 개의 벡터 임베딩이 다른 embedding space를 공유함을 가정한다. 따라서, 여러 개의 벡터 임베딩이 동일한 embedding space를 공유하는 경우, 유저 단에서 single-vector search를 통해 얻은 결과를 다시 process해야 한다.
- 여러 개의 벡터 임베딩이 다른 embedding space를 공유할 때, 최종적으로 반환할 K개의 대상을 찾을 때, 항상 각 embedding space 별로 계산된 score의 합만을 고려해야 한다. 즉, 반환할 대상을 선정하는 점수를 계산하는 aggregation function이 sum 밖에 존재하지 않는다. 유저의 application 별로 aggregation function이 max, mean과 같은 다양한 함수를 지원할 필요가 있음에도 불구하고, 항상 합을 기준으로 반환 대상을 선정하기 때문에, 다양한 application을 지원할 수 없다.

따라서, 본 디자인에서는 위와 같은 한계점을 극복하여, multi-vector search의 다양한 use case를 고려한 밀버스 구현을 통해, 밀버스의 functionality를 넓히고자 한다.

## Goals
- Support various aggregation function for multi-vector search where it does not share the same embedding space
- Support search for multi-vector search where it does share the same embedding space

## Non-goals
- Support various SDK interfaces (e.g., Python, Java, etc) (In this implementation, we control the search with dynamic configs by etcd. Matching with various SDKs is another implementation project.)

## Design Details
Lists of APIs to be modified
1. rankSearchResultData - internal/proxy/search_util.go
2. reduceSearchResultDataWithGroupBy - internal/proxy/search_util.go

TODO:

## Compatibility, Deprecation, and Migration Plan(optional)

Compatible with old versions.


## Test Plan

Correctness aspects
- Verify the ability of aggregation functions
    - Aggregation function for multi-vector search where it does not share the same embedding space
    - Aggregation function for multi-vector search where it does share the same embedding space

Performance aspects
- Perform late-interaction IR model (i.e., Colbert) and compare effectiveness (e.g., recall) whether it can achieved comparable 


## References(optional)
[hybrid_search; control the result based on score](https://stackoverflow.com/questions/76489090/in-weaviate-hybrid-search-is-there-a-way-to-control-the-results-based-on-score)