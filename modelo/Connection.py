from neo4j import GraphDatabase,basic_auth


class Connection(object):

    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth = basic_auth(user, password))

    def close(self):
        self._driver.close()

    def ventasPorDiaSemana(self):
        session = self._driver.session()
        result = list(session.run("MATCH p=()-[r:COMPRA]->(f:factura) where length(r.fecha)=19 WITH apoc.date.fields(r.fecha, 'dd/MM/yyyy HH:mm:ss') as fecha RETURN fecha.weekdays as day, count(fecha) as CO order by day"))

        return result

    def pintarAlgo(self):
        session = self._driver.session()
        result = list(session.run("Match (n) return n limit 100"))
        message = ""
        for record in result:
            message += str(record["n"]["id"]) + "\n"

        return message

    def aMasCompradosC(self,id):
        session = self._driver.session()
        if id == "":
            id = "1076"
        result = list(session.run("MATCH p=(c:cliente)-[x:COMPRA]->(f:factura)-[co:CONTIENE]->"
                                  "(a:articulo) WHERE c.id = '"+id+
                                  "' RETURN a,count(a), count(a) * toFloat(co.cantidad) as num ORDER BY num DESC LIMIT 5"))
        # Crear Esctructura que sepamos trabajar con ella y pasarlo!!

        return result

    def frecuenciaArticulo(self,id_interno):
        session = self._driver.session()
        if id_interno == "":
            id_interno = "78461"

        result = list(session.run("MATCH (c:cliente)-[:COMPRA]->(f:factura)-[co:CONTIENE]->" 
                                  "(a:articulo) WHERE a.id_interno = '"+id_interno+
                                  "' RETURN a,count(a) as num,keys(a) ORDER BY num DESC Limit 5"))
        return result


    def sacarKeys(self):
        session = self._driver.session()

        keys = [[],[],[],[]]

        keys[0] = list(session.run("MATCH (n:articulo) RETURN DISTINCT keys(n) LIMIT 1"))

        keys[1] = list(session.run("MATCH (n:cliente) RETURN DISTINCT keys(n) LIMIT 1"))

        keys[2] = list(session.run("MATCH (n:proveedor) RETURN DISTINCT keys(n) LIMIT 1"))

        keys[3] = list(session.run("MATCH (n:factura) RETURN DISTINCT keys(n) LIMIT 1"))

        return keys
