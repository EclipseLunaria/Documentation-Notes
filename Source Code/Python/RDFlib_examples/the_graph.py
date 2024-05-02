from rdflib import Graph
from pprint import pprint
g = Graph()

# The Schema.org schema may be found at: https://schema.org/docs/developers.html
g.parse('https://schema.org/version/latest/schemaorg-current-https.jsonld')

object_set = set()
predicate_set = set()
subject_set = set()

for s, p, o in g:
        subject_set.add(s)
        object_set.add(o)
        predicate_set.add(str(p))
        if "source" in p.lower():
            print(s, p, o)

# print("Predicate Set")
# pprint(predicate_set)

# # print("Object Set")
# # print(object_set)

# # print("Subject Set:")
# # print(subject_set)

# print(f"Set Lengths: predicate set {len(predicate_set)}") #, object set: {len(object_set)}, subject set: {len(subject_set)}")
# for p in predicate_set:
#         print(p)