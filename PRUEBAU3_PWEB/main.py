from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ej1():
    if request.method == 'POST':
        not1 = int(request.form['nota_1'])
        not2 = int(request.form['nota_2'])
        not3 = int(request.form['nota_3'])
        asist = int(request.form['asistencia'])
        promedio = round(float((not1 + not2 + not3)/3), 1)
        if asist >= 75 and promedio >= 40:
            return render_template('ejercicio1.html', resultado=f'Promedio: {promedio}', estado='Estado: Aprobado.')
        elif asist < 75 and promedio >= 40:
            return render_template('ejercicio1.html', resultado=f'Promedio: {promedio}', estado='Estado: Reprobado por inasitencia.')
        elif asist >= 75 and promedio < 40:
            return render_template('ejercicio1.html', resultado=f'Promedio: {promedio}', estado='Estado: Reprobado por calificaciones.')
        else:
            return render_template('ejercicio1.html', resultado=f'Promedio: {promedio}', estado='Estado: Reprobado por ambos criterios.')
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ej2():
    if request.method == 'POST':
        nom1 = request.form['nombre_1']
        nom2 = request.form['nombre_2']
        nom3 = request.form['nombre_3']
        ext1 = len(nom1)
        ext2 = len(nom2)
        ext3 = len(nom3)
        if ext1 > ext2 and ext1 > ext3:
            return render_template('ejercicio2.html', oracion=f'El nombre con mayor cantidad de caracteres es: {nom1}', ext=f'El nombre tiene: {ext1} caracteres')
        elif ext2 > ext1 and ext2 > ext3:
            return render_template('ejercicio2.html', oracion=f'El nombre con mayor cantidad de caracteres es: {nom2}', ext=f'El nombre tiene: {ext2} caracteres')
        elif ext3 > ext1 and ext3 > ext2:
            return render_template('ejercicio2.html', oracion=f'El nombre con mayor cantidad de caracteres es: {nom3}', ext=f'El nombre tiene: {ext3} caracteres')
        else:
            nom4 = 'Hay 2 o más nombres con la misma extensión'
            return render_template('ejercicio2.html', oracion=nom4)
    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)