from flask import Flask, request
from rdflib import Graph, Namespace, Literal, RDF,URIRef
from rdflib.namespace import DC, DCTERMS, DOAP, FOAF, SKOS, OWL, RDF, RDFS, VOID, XMLNS, XSD
from pyparsing import ParseException
from tabulate import tabulate

g= Graph()
g.parse(r"D:\Fast NU\5th semester (pro) shit\KRR\Project\Phase-III\Output Ontologies\Ontology With Data.rdf", format="xml")

aiiso = Namespace('http://purl.org/vocab/aiiso/schema#')
oloud = Namespace('http://lod.nik.uni-obuda.hu/oloud/oloud#')
dbo = Namespace('http://dbpedia.org/ontology/')
resource = Namespace('http://www.semanticweb.org/abdul/ontologies/2023/University/Resource/')

g.bind("foaf", FOAF)
g.bind("xsd", XSD)
g.bind("owl", OWL)
g.bind("dbo", dbo)
g.bind("oloud", oloud)
g.bind("aiiso", aiiso)
g.bind("resource", resource)

app = Flask(__name__)
 
@app.route('/q', methods=['POST', 'GET'])
def login():
    query = request.args.get('query')
    try:
        qres = g.query(query.strip())
    except (ParseException, AttributeError):
        return "Invalid Query\n" + query 
    else:
        
        temp = list(qres)
        temp.insert(0, [str(v) for v in qres.vars])
        print('Query', query)
        print('Result', list(qres))
        print('temp', temp)
        return tabulate(temp, tablefmt='html')
 
if __name__ == '__main__':
    app.run(debug=True, port=4444)

