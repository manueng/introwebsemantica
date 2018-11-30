from rdflib import URIRef, BNode, Literal, Namespace, RDF, Graph
from SPARQLWrapper import SPARQLWrapper, JSON
import rdfextras
g = Graph()
g.parse("/home/usuario/.cache/.fr-nCZyvZ/file-output-minimal.rdf")

print(len(g))
rdfextras.registerplugins()


sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setQuery("""
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT ?label
    WHERE { <http://dbpedia.org/resource/Carro> rdfs:label ?label }
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

for result in results["results"]["bindings"]:
    print(result["label"]["value"])

