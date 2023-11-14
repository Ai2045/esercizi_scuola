import bottle
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="todolist"
)

cursor = mydb.cursor()
app = bottle.Bottle()


@app.route('/query1')
def query1():
    cursor.execute("SELECT *FROM utenti")
    result = cursor.fetchall()
    return bottle.template('gestione_todolist/'+'result_template.tpl', result=result)

@app.route('/query2')
def query2():
    cursor.execute("""
    SELECT *
    FROM utenti
    LEFT JOIN todos ON utenti.id = utente_id
    WHERE utenti.id IS NULL;
""")
    result = cursor.fetchall()
    return bottle.template('gestione_todolist/'+'result_template.tpl', result=result)

@app.route('/query3')
def query3():
    cursor.execute("""
    SELECT *
    FROM utenti
    WHERE cognome = %s;
""", ('Rossi',))
    result = cursor.fetchall()
    return bottle.template('gestione_todolist/'+'result_template.tpl', result=result)

@app.route('/query4')
def query4():
    cursor.execute("""
    SELECT *
    FROM utenti
    WHERE data_nascita BETWEEN %s AND %s;
""", ('1999-01-01', '1999-12-31'))
    result = cursor.fetchall()
    return bottle.template('gestione_todolist/'+'result_template.tpl', result=result)

@app.route('/query5')
def query5():
    cursor.execute("""
    SELECT *
    FROM todos
    WHERE data_inserimento BETWEEN %s AND %s;
""", ('2023-01-01', '2023-12-31'))
    
    result = cursor.fetchall()
    return bottle.template('gestione_todolist/'+'result_template.tpl', result=result)

@app.route('/query6')
def query6():
    cursor.execute("""
    SELECT *
    FROM todos
    WHERE data_scadenza IS NULL;
""")
    result = cursor.fetchall()
    return bottle.template('gestione_todolist/'+'result_template.tpl', result=result)

@app.route('/query7')
def query7():
    cursor.execute("""
    SELECT *
    FROM todos
    WHERE data_scadenza IS NOT NULL;
""")
    result = cursor.fetchall()
    return bottle.template('gestione_todolist/'+'result_template.tpl', result=result)

@app.route('/query8')
def query8():
    cursor.execute("""
    SELECT todos.id, data_inserimento, data_scadenza, descrizione
    FROM todos
    JOIN todos_tags ON todos.id = todo_id
    JOIN tags ON tag_tipologia = tipologia
    WHERE tipologia = %s;
""", ('lavoro',))
    result = cursor.fetchall()
    return bottle.template('gestione_todolist/'+'result_template.tpl', result=result)


@app.route('/query9')
def query9():
    cursor.execute("""
    SELECT todos.id, data_inserimento, data_scadenza, descrizione
    FROM todos
    LEFT JOIN todos_tags ON todos.id = todo_id
    WHERE tag_tipologia IS NULL;
""")
    result = cursor.fetchall()
    return bottle.template('gestione_todolist/'+'result_template.tpl', result=result)


@app.route('/query10')
def query10():
    cursor.execute("""
    SELECT utenti.id, data_inserimento, data_scadenza, descrizione
    FROM utenti
    JOIN todos ON utenti.id = todos.utente_id
    WHERE data_inserimento BETWEEN %s AND %s
    AND nome = %s;
""", ('2023-01-01', '2023-12-31', 'Paolo'))
    result = cursor.fetchall()
    return bottle.template('gestione_todolist/'+'result_template.tpl', result=result)


app.run(host='localhost', port=3000, debug=True)
