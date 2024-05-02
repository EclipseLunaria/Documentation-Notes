# Abstract
In many use cases it is important to quickly search for some or all instance of a user specified strings. This is especially true in regards to unstructured data. For example, take searching through library data. You may want to simultaniously search for multiple instances or keywords such as:
- Signature
- Title
- Abstract
- Authors
Scanning each document for all the keyword would take much too long to search each document each keyword. 

We can solve this by introducing a secondary index of sorts containing keyword fragments. searching the index of the user specified
keywords yields a superset of the documents required. The Superset contains documents with fragments present but but keywords do not. We want to reject the the documents with only fragments thus we search the document for the user specified keywords. [[Aho corasick]] describes an efficient algorithm for this. The algorithm preprocesses the keywords in linear time in the **Sum of the total lengths of keywords**. Then searches for keyword occurrences in the document in linear time in document length at its worst case.

The Idea of the algorithm was inspired by the ideas of [[Knuth-Morris-Pratt Algorithm]]. and [[Finite State Machines]]

Given only one keyword [[Boyer-Moore String Search Algorithm]] is faster on average

# Structure of The Preprocessed Set of Keywords

## Trie Structure
### Trie Invariants
A trie is a tree T such that:
1. Each node v of T, except the root is labeled by some character a = I(v), an alphabet of some alphabet A
2. The root r is labeled with Null, denoting an empty word
3. If the nodes v1 and v2 share the same parent node v, v1 != v2 then I(v1) != I(v2)

### Trie Path
We say that path v<sub>1</sub>,...,v<sub>m</sub> of T where v<sub>i+1</sub> is the son of v<sub>i</sub> represents a the word |(v<sub>1</sub>) |(v<sub>2</sub>)... |(v<sub>m</sub>)

This word we denote by w(v<sub>1</sub>) if and only if v<sub>1</sub> = r, the root

### Trie Depth

We denote each nodes depth by:
d(v) = | 0                 if v = r, the root
	  |  d('v) + 1     if v is son of 'v
then:
d(T) = max {d(v); v $\in$  T}
denotes the depth of the trie T

### Set of Keywords
let K = w<sub>1</sub>,...w<sub>r</sub> be the set of keywords on some alphabet A which we want to search for in some document D.
While similar to [[Aho corasick]] representing K as a Trie. However, we base our Trie T on the reversed Keywords


## Citation

![[commentz-walter-search.pdf]]