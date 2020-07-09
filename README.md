# ETL
## 1. Activación BD grafos
## 2. Creación de nodos
## 3. Relación de nodos


# 1. Activación BD grafos

## 1.1 Ingresar configuraciones Neo4j
    vim /etc/neo4j/neo4j.conf

## 1.2 Definir nombre BD
    dbms.active_database = nombre_prueba.db
 
## 1.3 Inicializar BD
    systemctl start neo4j
    
# 2. Creación de nodos
    Python: PostgreSQL() - Neo4j()
    
# 3. Relación de nodos

## 3.1 Acceder consola Cypher
    /usr/bin/cypher-shell -u neo4j -p password
    
## 3.2 Ejecutar consultas
    neo4j> MATCH (p:Pac), (e:Entidad) WHERE NOT (p)<-[:TIENE_PAC]-(e) AND p.idPersona = e.idEntidad CREATE (e)-[:TIENE_PAC]->(p);

    
